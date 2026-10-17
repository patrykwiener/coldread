#!/usr/bin/env python3
"""Ask chat eval questions of a simulated claude.ai, then grade the answers.

  scripts/claudeai-sim.py fetch                              download the newest claude.ai system prompts
  scripts/claudeai-sim.py run --rules old=<file> new=<file>  answer each case with each rules file
  scripts/claudeai-sim.py judge                              grade every answer with its case's graders
  scripts/claudeai-sim.py report                             print pass rates and the shape of the answers

claude.ai answers under a system prompt of its own, which allows short answers, and
`claude plugin eval` keeps Claude Code's system prompt, so the eval suite cannot show
how the chat rules do in claude.ai. This script replaces Claude Code's system prompt
with the newest one Anthropic published for the model, then adds an About me note and
one rules file in a userPreferences block. That block is a guess: Anthropic does not
publish how claude.ai passes preferences. Each question runs through `claude -p` with
no tools and no user settings, so neither your CLAUDE.md nor your plugins reach it.

Answers and verdicts go to plugins/coldread-chat/evals/results/claudeai/, which git
ignores. A step skips the answers or verdicts it already has, so it can resume.
"""

import argparse
import datetime
import json
import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "plugins" / "coldread-chat" / "evals"
OUT = EVALS / "results" / "claudeai"
MODELS = ["claude-sonnet-5-5", "claude-opus-5-5"]
PROMPT_URL = "https://platform.claude.com/docs/en/release-notes/system-prompts/{model}.md"
CASES = ["pl-jastrych-aboutme", "pl-lrv", "pl-electrical-aboutme", "pl-handles-verdict",
         "en-db-connections", "pl-howto-roznicowka", "pl-plain-fact"]
ABOUT = ("## About me\n\nBackend and AI engineer; a layman in construction, interior design and "
         "electrical work. I read symbols such as ≤, ≥ and × faster than the words for them.")
JUDGE_MODEL = "claude-sonnet-5-5"
JUDGE_SYSTEM = ("You grade one chat response against one condition. Judge only that condition and "
                "ignore every other quality of the response. Reply with exactly PASS or FAIL on the "
                "first line, then one sentence that gives the reason.")


def claude(args, prompt, system=None, system_file=None):
    """Run `claude -p` in an empty folder with no user settings; return its JSON result."""
    command = ["claude", "-p", "--tools", "", "--setting-sources", "project", "--output-format", "json", *args]
    if system is not None:
        command += ["--system-prompt", system]
    if system_file is not None:
        command += ["--system-prompt-file", str(system_file)]
    with tempfile.TemporaryDirectory() as cwd:
        proc = subprocess.run(command + [prompt], cwd=cwd, capture_output=True, text=True, timeout=600)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip()[:300] or proc.stdout.strip()[:300])
    return json.loads(proc.stdout)


def fetch(_args):
    """Save the newest dated system prompt on each model's page, with its date."""
    for model in MODELS:
        page = subprocess.run(["curl", "-fsSL", PROMPT_URL.format(model=model)],
                              capture_output=True, text=True, timeout=120, check=True)
        lines = page.stdout.splitlines()
        start = next(i for i, line in enumerate(lines) if line.startswith("## "))
        blocks, inside = [[]], False
        for line in lines[start + 1:]:
            if line.startswith("## ") and not inside:
                break
            if line.startswith("```"):
                inside = not inside
                if not inside:
                    blocks.append([])
                continue
            if inside:
                blocks[-1].append(line)
        text = "\n".join("\n".join(block) for block in blocks if block)
        (OUT / "prompts").mkdir(parents=True, exist_ok=True)
        (OUT / "prompts" / f"{model}.txt").write_text(text + "\n")
        (OUT / "prompts" / f"{model}.date").write_text(lines[start][3:].strip() + "\n")
        print(f"{model}: version of {lines[start][3:].strip()}, {len(text)} characters")


def question(case):
    text = (EVALS / case / "prompt.md").read_text()
    return text.split("\n---\n", 1)[1].strip()


def answer(model, variant, rules, case, run, date):
    out = OUT / model / variant / case / f"{run}.json"
    if out.exists():
        return f"skip {model}/{variant}/{case}/{run}"
    base = (OUT / "prompts" / f"{model}.txt").read_text().replace("{{currentDateTime}}", date).rstrip()
    preferences = f"{ABOUT}\n\n{Path(rules).read_text().rstrip()}"
    with tempfile.TemporaryDirectory() as folder:
        system_file = Path(folder) / "system.txt"
        system_file.write_text(f"{base}\n\n<userPreferences>\n{preferences}\n</userPreferences>\n")
        data = claude(["--model", model], question(case), system_file=system_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"model": model, "variant": variant, "case": case, "run": run,
                               "text": data.get("result", ""), "cost_usd": data.get("total_cost_usd")},
                              ensure_ascii=False, indent=1))
    return f"ok {model}/{variant}/{case}/{run}"


def run(args):
    variants = dict(pair.split("=", 1) for pair in args.rules)
    jobs = [(args.model, name, path, case, n, args.date)
            for n in range(1, args.runs + 1) for name, path in variants.items() for case in args.cases]
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for status in pool.map(lambda job: answer(*job), jobs):
            print(status, flush=True)


def parse_grader(path):
    _, front, body = path.read_text().split("---", 2)
    meta = {}
    for line in front.strip().splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip("'\"")
    return meta, body.strip()


def verdict(grader, text):
    meta, body = parse_grader(grader)
    if meta.get("type") == "regex":
        flags = sum({"m": re.M, "i": re.I, "s": re.S}.get(letter, 0) for letter in meta.get("flags", ""))
        found = re.search(meta["pattern"], text, flags) is not None
        passed = found if meta.get("match", "contains") == "contains" else not found
        return {"verdict": "PASS" if passed else "FAIL", "reason": "regex", "cost_usd": 0.0}
    prompt = f"Condition:\n{body}\n\nThe final response:\n<<<\n{text}\n>>>"
    data = claude(["--model", JUDGE_MODEL], prompt, system=JUDGE_SYSTEM)
    reply = data.get("result", "").strip()
    first = reply.splitlines()[0].strip().upper() if reply else ""
    result = "PASS" if first.startswith("PASS") else "FAIL" if first.startswith("FAIL") else None
    return {"verdict": result, "reason": reply, "cost_usd": data.get("total_cost_usd") or 0.0}


def grade(answer_file):
    data = json.loads(answer_file.read_text())
    out = answer_file.with_suffix(".verdicts.json")
    verdicts = json.loads(out.read_text()) if out.exists() else {}
    for grader in sorted((EVALS / data["case"] / "graders").glob("*.md")):
        if verdicts.get(grader.stem, {}).get("verdict"):
            continue
        verdicts[grader.stem] = verdict(grader, data["text"])
        out.write_text(json.dumps(verdicts, ensure_ascii=False, indent=1))
    return f"graded {answer_file.relative_to(OUT)}"


def answers():
    return sorted(p for p in OUT.glob("claude-*/*/*/*.json") if not p.name.endswith(".verdicts.json"))


def judge(args):
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for status in pool.map(grade, answers()):
            print(status, flush=True)


def shape(text):
    lines = text.splitlines()
    return {
        "words": len(re.sub(r"[#*|`_>-]", " ", text).split()),
        "headings": sum(1 for line in lines if re.match(r"#{1,6} ", line)),
        "list items": sum(1 for line in lines if re.match(r"\s*(?:[-*+]|\d+\.) ", line)),
        "bold": len(re.findall(r"\*\*[^*]+\*\*", text)),
        "tables": int(any(line.startswith("|") for line in lines)),
    }


def report(_args):
    passes, shapes, cost = defaultdict(lambda: defaultdict(list)), defaultdict(lambda: defaultdict(list)), 0.0
    for path in answers():
        data = json.loads(path.read_text())
        arm = (data["model"], data["variant"])
        cost += data.get("cost_usd") or 0.0
        for name, value in shape(data["text"]).items():
            shapes[arm][name].append(value)
        verdicts = path.with_suffix(".verdicts.json")
        for grader, result in (json.loads(verdicts.read_text()) if verdicts.exists() else {}).items():
            cost += result.get("cost_usd") or 0.0
            if result["verdict"]:
                passes[arm][f"{data['case']}/{grader}"].append(result["verdict"] == "PASS")
    arms = sorted(shapes)
    print("Passes per grader, by model and rules file:\n")
    print("| Grader | " + " | ".join(f"{m.removeprefix('claude-')} {v}" for m, v in arms) + " |")
    print("|---|" + "---|" * len(arms))
    for grader in sorted({g for arm in arms for g in passes[arm]}):
        cells = [f"{sum(r)} of {len(r)}" if (r := passes[arm].get(grader)) else "-" for arm in arms]
        print(f"| {grader} | " + " | ".join(cells) + " |")
    print("\nShape of the answers, mean per answer:\n")
    print("| Model and rules | Answers | Words | Median words | Headings | List items | Bold | With a table |")
    print("|---|---|---|---|---|---|---|---|")
    for arm in arms:
        s = shapes[arm]
        n, words = len(s["words"]), sorted(s["words"])
        print(f"| {arm[0].removeprefix('claude-')} {arm[1]} | {n} | {sum(words) / n:.0f} | {words[n // 2]} | "
              f"{sum(s['headings']) / n:.1f} | {sum(s['list items']) / n:.1f} | {sum(s['bold']) / n:.1f} | "
              f"{sum(s['tables'])} of {n} |")
    print(f"\nCost at list price, answers and judge: ${cost:.2f}")


def main():
    parser = argparse.ArgumentParser(description="Ask chat eval questions of a simulated claude.ai, then grade the answers.")
    steps = parser.add_subparsers(dest="step", required=True)
    steps.add_parser("fetch").set_defaults(func=fetch)
    p = steps.add_parser("run")
    p.add_argument("--rules", nargs="+", required=True, metavar="NAME=FILE")
    p.add_argument("--model", default=MODELS[0], choices=MODELS)
    p.add_argument("--runs", type=int, default=3)
    p.add_argument("--cases", nargs="+", default=CASES)
    p.add_argument("--date", default=datetime.date.today().strftime("%A, %B %-d, %Y"),
                   help="the date that replaces {{currentDateTime}} in the prompt")
    p.add_argument("--jobs", type=int, default=4)
    p.set_defaults(func=run)
    p = steps.add_parser("judge")
    p.add_argument("--jobs", type=int, default=4)
    p.set_defaults(func=judge)
    steps.add_parser("report").set_defaults(func=report)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    sys.exit(main())
