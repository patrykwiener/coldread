# Eval results

Each run below comes from `claude plugin eval`, which runs every case with and without the plugin in a clean session that loads no CLAUDE.md file. A score is the share of a case's graders that passed, averaged over runs.

## 2026-10-09: chat rules, v0.1

The rules raised the suite score from 75% to 92%. All of the gain came from the four Polish cases, which are rebuilt from the maintainer's real confusions. The four English cases scored the same with and without the rules.

Setup: Claude Code 2.1.295, the default agent model Claude Opus 5.5, Haiku as judge, 8 cases, 3 runs per arm. The run took 5.5 minutes and cost $3.73.

| Case | With rules | Without | Difference |
|---|---|---|---|
| pl-heating-verdict | 100% | 44% | +56 |
| pl-jastrych | 83% | 50% | +33 |
| pl-handles-verdict | 89% | 67% | +22 |
| pl-lrv | 89% | 67% | +22 |
| en-duplicate-rows | 75% | 75% | 0 |
| en-mutex-semaphore | 100% | 100% | 0 |
| en-task-report | 100% | 100% | 0 |
| guard-coding | 100% | 100% | 0 |
| All cases | 92% | 75% | +17 |

The graders that moved, as runs passed out of 3, with rules against without:

- The first sentence answers the question: 3 against 0 for jastrych and for the question about Light Reflectance Value (LRV), and 3 against 1 for the heating verdict.
- Numbers instead of adjectives such as "cheaper": 3 against 0 for heating.
- At most four points: 2 against 0 for the kitchen handles.
- Trade terms explained where they first appear: 1 against 0 for jastrych. This is the weakest rule.

The coding guard passed 3 of 3 in both arms, so in this case the rules did not make plain coding worse.

What this run does not show:

- The English cases sit at the ceiling in both arms. Either Claude already answers them well, or their graders are too easy. Harder English cases are needed before anything can be said about English.
- Three runs per arm is little. One run changes a grader's pass rate by 33 points, so single-run differences can be noise.
- The same author wrote the rules, the cases and the graders. The Polish cases come from the confusions the rules were written against. Cases from another author would show whether the gain carries over.
- The judge is a model, not a person. The blind reading tests further down add a human reader.

One grader changed after this run. The causal-prose grader of en-duplicate-rows failed answers that linked causes with "because" and "so" inside a numbered list of events, which the rules allow. It now accepts such a list when each item says why it led to the next.

## 2026-10-09: /coldread:write, one smoke run

One run per arm of write-slack-pm-pl, a Polish Slack message to a PM written from notes that contain private labels. Both arms scored 75%. The run with the skill cost $0.31 and took 6 turns. The run without it cost $0.10 and took 1 turn.

The run shows that the pipeline works under eval. The skill fired without being named, the cold reader ran, and the skill skipped Vale for Polish text and said so. The report quoted the ask next to the cold reader's own reading of it.

The graders do not capture two differences:

- Only the run with the skill named two facts the PM needs and the notes do not give: what happens when an upload over 2 GB fails, and how many exports exceed 2 GB.
- Both runs kept the labels `Phase A`, `D3` and `option B`, because the notes do not say what the labels mean. The skill should drop such a label when the reader does not need it for the decision, and list the removal in its report. That change is the next one to measure.

## 2026-10-09: /coldread:write, full run

The skill raised the suite score from about 50% to 76%. This run already included the change that drops unexplained labels from the user's notes. Setup as above: 4 cases, 3 runs per arm, 5.7 minutes, $4.11 at list price. A run with the skill cost about 3 times as much as one without: $0.22 to $0.28 against $0.09 to $0.10.

| Case | With skill | Without | Difference |
|---|---|---|---|
| write-trigger-pl | 67% | 0% | +67 |
| write-pr-en | 100% | 78% | +22 |
| write-slack-pm-pl | 80% | 67% | +13 |
| write-rewrite-facts | 56% | 56% | 0 |
| All cases | 76% | 50% | +26 |

What improved, as runs passed out of 3 with the skill against without:

- The skill fired in all 12 runs without being named, including the two Polish requests.
- The ask in the first two sentences: 3 against 1 for the PR, and 2 against 0 for the Polish PR.
- Unexplained labels from the notes kept out of the Slack message: 3 against 0. This is the change made after the smoke run.
- Facts the PM needs that the notes lack, named: 3 against 2.

Where the skill did worse, and why:

- Slack ask in the first two sentences: 0 against 2. The skill opened with the Thursday deadline and "we have two options", then listed the options below. A reader who stops after two sentences knows a decision is due, but not between what. The skill's own rule asks for the opposite.
- The rewrite case is partly a fault of the test. Its source sentence can be read two ways: either the cutover happened on 2 June, or the duplicate rate was measured then. The run without the skill flagged that. The skill picked one reading, and in one run it merged the migration and the cutover to answer a cold-reader question, which changes a fact it could not check. The case also did not name the reader. So the skill assumed an engineer who knows what idempotency means, while the grader expected that term explained.

## 2026-10-09: after the fixes

Three changes followed the full run, then the affected cases ran again with 3 runs per arm:

- /coldread:write now names the options of a choice in its first two sentences. It no longer guesses a fact to settle an ambiguous source or to answer a cold-reader question.
- The rewrite case now has a source sentence that reads one way only, and it names the reader. Its facts grader is split in two: whether the original facts survive, and whether the text invents claims about the system.
- The chat causal-prose grader accepts a numbered list of events when each item says why it led to the next.

| Case | Before: with / without | After: with / without |
|---|---|---|
| write-slack-pm-pl | 80% / 67% | 93% / 60% |
| write-rewrite-facts | 56% / 56% | 92% / 67% |
| en-duplicate-rows | 75% / 75% | 100% / 83% |

The rewrite case and the chat case changed between the two runs, so their before and after scores are not a clean comparison. Only the Slack case ran the same test against the changed skill.

- Slack: the ask came first in 2 of 3 runs with the skill, against 0 of 3 before the change. The skill also named facts the PM needs that the notes lack in 3 of 3 runs, against 1 of 3 without it.
- Rewrite: both arms kept every original fact in 3 of 3 runs, and both invented a claim about the system in 1 of 3 runs. The skill's gain came only from telling the user what it changed, in 3 of 3 runs against 0 of 3 without it.
- Chat: the first sentence answered the question in 3 of 3 runs with the rules, against 1 of 3 without them. Both arms now pass the causal-prose grader.

Known limit: in eval runs, /coldread:write reported that it could not run shell commands, so it skipped Vale. The likely cause, not verified, is that the eval sandbox blocks the home directory, where the plugin and its Vale rules live. Until that is solved, the write suite measures the skill without its lint step.

## 2026-10-09: harder cases and the trade-terms rule

Two changes, then the full chat suite ran again with 13 cases and 3 runs per arm. The run took 10 minutes and cost $6.34 at list price.

- The trade-terms rule now says: when the About me note marks the user a layman in the topic, or when Claude cannot tell, every trade word counts as new.
- Five new cases: two Polish ones with the About me note a real user has, and three harder English ones.

With the rules the suite scored 85%, without them about 67%. The harder English cases show a difference, so the flat English result of the first run came from tests that were too easy.

| New case | With rules | Without | Difference |
|---|---|---|---|
| en-oauth-analyst | 92% | 50% | +42 |
| pl-jastrych-aboutme | 83% | 50% | +33 |
| en-db-connections | 56% | 33% | +22 |
| pl-electrical-aboutme | 56% | 33% | +22 |
| en-queue-choice | 78% | 67% | +11 |

- OAuth for a data analyst: at most four points in 3 of 3 runs against 1 of 3, and authentication terms explained in 2 of 3 against 0 of 3.
- Database connections: the cause came first in 2 of 3 runs against 0 of 3. In every run both arms also listed three or more other possible causes, although the rules ask for the one or two that matter. That rule is not followed yet.
- The eight old cases moved by at most one run per grader against the first measurement, so the rule change made no visible difference there.

The trade-terms rule is still unproven. The grader failed an answer that explained every term from the question with examples and numbers, because it left words such as "uziemienie" unexplained. After the grader was relaxed to allow one unexplained side term, the five cases tagged jargon ran again in 5.5 minutes, for $2.73:

- OAuth: terms explained in 3 of 3 runs with the rules against 0 of 3 without.
- The electrical case and plain jastrych: 0 of 3 in both arms.
- Jastrych with the About me note: 1 of 3 against 0 of 3.

A model as judge cannot settle what a layman knows. A person needs to read these answers.

Noise: the same case with the same setup scored up to 11 points apart between two runs today, for example pl-lrv at 100% and 89% with the rules. At 3 runs per arm, differences below about 15 points are within that noise.

## 2026-10-09: blind reading test of the trade-terms rule

One reader rated the answers with and without the rules as equally easy in 3 of 3 pairs, and found no unclear word in any of the 6 answers. The answers with the rules were 20% to 36% shorter. The reader called them the deeper ones in all 3 pairs.

Setup: the maintainer, a layman in construction and electrical work, read three pairs of answers on a page that hid which answer came from which arm. The answers are the first run of each arm from the jargon re-run above, for pl-jastrych-aboutme, pl-electrical-aboutme and pl-jastrych. The order inside each pair was random: the rules wrote answer B in pairs 1 and 2 and answer A in pair 3. For each pair the reader marked the easier answer or a tie, and wrote down every unclear word in each answer.

| Pair | Case | Words with rules | Words without | Easier | Unclear words |
|---|---|---|---|---|---|
| 1 | pl-jastrych-aboutme | 356 | 446 | tie | none |
| 2 | pl-electrical-aboutme | 365 | 566 | tie | none |
| 3 | pl-jastrych | 317 | 428 | tie | none |

The word counts leave out Markdown markup, such as the pipes of a table.

The reader's comments point the same way in every pair. The answer with the rules explains more and goes deeper. The answer without the rules has headings, bullets and, in pairs 1 and 2, a table. The reader found the table easy to read and good for comparing. In pair 1 the table matched the state of the floor to the work it needs. In pair 2 it gave each electrical part with its purpose and a verdict.

What the test shows:

- The judge is stricter about terms than this reader. The terms-explained grader failed 5 of these 6 answers, yet the reader found no unclear word in any of them.
- Two answers without the rules failed the answer-first grader, and the reader rated them as easy as the answers with the rules.
- The rules saved 90 to 201 words per answer at the same ease.
- The rules push answers into prose and leave tables out, although a table helped this reader compare. The rules should allow a table after the explanation when the reader compares options or looks for their own case.

What the test does not show:

- One reader read three pairs. A tie in 3 of 3 pairs means this reader noticed no difference, not that there is none.
- The reader helped write the rules and could recognise their style. The page hid the arm, but not the style.
- The jastrych question comes from the reader's own earlier confusion, so the reader may have learned these terms since then.
- The page did not time the reading, so "easier" is the reader's own judgment.

## 2026-10-09: a table for comparisons

After the blind test, rule 5 gained one sentence. When the reader compares options or looks for their own case, the answer adds a table after the explanation, with one row per option or case and at most four columns. The full chat suite then ran again: 13 cases, 3 runs per arm, 10.6 minutes, $6.35 at list price.

The suite score did not change: 85% with the rules, about 65% without. The form of the answers did change:

| Measure | Before the change | After |
|---|---|---|
| Answers with the rules that contain a table | 3 of 39 | 28 of 39 |
| Answers without the rules that contain a table | 20 of 39 | 19 of 39 |
| Mean words with the rules | 341 | 376 |
| Mean words without the rules | 421 | 412 |

The word counts leave out the coding guard and the table markup.

One grader fell by two runs: at most four points in the OAuth case, from 3 of 3 to 1 of 3. Both failed runs combined numbered steps with a table of fields to fill in. Every other grader in the arm with the rules moved by at most one run, which is within the noise.

What this run shows:

- The new sentence works. The answers with the rules now use tables more often than the answers without them, 28 against 19, so the sentence may be too broad. Tables also appeared in a diagnosis, where they set the connection counts before and after a change side by side.
- The answers with the rules grew by 35 words on average and are still shorter than the answers without them.
- The judge does not score tables, so this run only shows that nothing else broke. Whether the tables help the reader is for a second blind round to show.

## 2026-10-09: second blind round, with the table sentence

The answers with the rules won or tied in every pair. The reader found them easier in 1 of 3 pairs and equally easy in 2. Asked which answer they would rather get, the reader picked the one with the rules in 2 pairs and had no preference in 1. Again no word was unclear in any of the 6 answers.

Setup: as in the first round, with new answers from the run above. For the arm with the rules the page used the first run whose answer contained a table, and for the arm without the rules the first run. This choice was fixed before the run finished. The page added one question: which answer would you rather get. The order inside each pair was random: the rules wrote answer A in pair 1 and answer B in pairs 2 and 3.

| Pair | Case | Words with rules | Words without | Easier | Rather get |
|---|---|---|---|---|---|
| 1 | pl-jastrych-aboutme | 393 | 513 | tie | with rules |
| 2 | pl-electrical-aboutme | 439 | 499 | with rules | with rules |
| 3 | pl-jastrych | 414 | 346 | tie | no preference |

The comments say what the reader wants from the layout:

- Prose for the explanation. In all 3 pairs the reader found the prose of the answer with the rules better.
- Headings over the parts of a long answer. The answer with the rules in pair 1 opened its paragraphs with bold words instead, and the reader missed real headings.
- Lists where the content is a list. The answer with the rules in pair 2 wrote two questions for the electrician as running prose. The reader liked the list of pros and cons in the answer without the rules in pair 1.
- Not too much markup. The answer without the rules in pair 2 had 4 headings, 16 list items and 22 bold phrases in 499 words. The reader found it hard to read.
- Symbols for limits. The reader, an engineer, reads "≤ 0,5%" faster than "najwyżej 0,5%".

The limits of the first round apply here too. The reader also knew the three questions by now, so both answers in each pair were easier than in the first round.

Next change: rule 5 asks for headings over the parts of a long answer, and for lists of items that are lists by nature, such as steps, pros and cons, and questions to ask. The preference for symbols goes into the reader's own About me note, because a layman may not read "≤".

## 2026-10-09: headings and lists

After the second blind round, rule 5 asks for prose in explanations and for lists only for items that are lists by nature, such as steps, pros and cons, and questions to ask. An answer longer than three paragraphs gets a short heading over each part after the opening answer. The full chat suite ran again: 13 cases, 3 runs per arm, 10.1 minutes, $6.41 at list price.

The suite scored 88% with the rules and about 69% without, against 85% and about 65% in the run before. Both changes are within the noise. The layout of the answers with the rules moved toward what the reader asked for:

| Per answer with the rules | Before the change | After |
|---|---|---|
| Headings | 1.3 | 2.9 |
| List items | 3.7 | 3.8 |
| Bold phrases | 4.6 | 3.1 |
| Answers with a table | 28 of 36 | 23 of 36 |
| Words | 376 | 389 |

In the same run the answers without the rules averaged 3.6 headings, 11.8 list items and 14.5 bold phrases. The counts leave out the coding guard.

Grader changes in the arm with the rules:

- Seven graders gained one run each, for example the answer came first in 3 of 3 runs of en-db-connections, against 2 of 3.
- The answer came first in 1 of 3 OAuth runs, against 3 of 3. All three openings say the same thing in nearly the same words, and the judge passed one 3 to 0 and failed the other two 1 to 2. This looks like judge noise.
- The answer came first in 2 of 3 runs of pl-jastrych-aboutme, against 3 of 3. The failed run opened with a title heading.

What this run shows:

- The answers with the rules now have nearly as many headings as the answers without them, but a third of their list items and a fifth of their bold phrases.
- The rule did not add lists: 3.8 items per answer, against 3.7. Whether lists now appear where the reader needs them, such as questions for a tradesman, only a reading can show.
- 3 of 36 answers with the rules still open with a title heading above the answer, as in the run before. Without the rules 21 of 36 do.

## 2026-10-09: third blind round, with headings and lists

The reader would rather get the answer with the rules in 3 of 3 pairs, and found both answers equally easy in all 3. No word was unclear in any of the 6 answers. In every pair the reader called the answer with the rules a little more concise.

Setup: as in the second round, with answers from the run above, the first run of each arm. The rules wrote answer A in pairs 1 and 2 and answer B in pair 3.

| Pair | Case | Words with / without | List items with / without | Bold phrases with / without |
|---|---|---|---|---|
| 1 | pl-jastrych-aboutme | 401 / 425 | 6 / 12 | 2 / 15 |
| 2 | pl-electrical-aboutme | 495 / 642 | 3 / 19 | 3 / 33 |
| 3 | pl-jastrych | 450 / 413 | 4 / 15 | 1 / 15 |

Both arms used 4 or 5 headings per answer. "Concise" did not mean fewer words: in pair 3 the answer with the rules was 37 words longer. It had a quarter of the list items and a fifteenth of the bold phrases.

The three rounds together, for the answer with the rules against the answer without:

| Round | Rules version | Easier | Rather get |
|---|---|---|---|
| 1 | trade terms, prose | 0 of 3, 3 ties | not asked |
| 2 | adds a table for comparisons | 1 of 3, 2 ties | 2 of 3, 1 no preference |
| 3 | adds headings and lists | 0 of 3, 3 ties | 3 of 3 |

The reader never found an answer without the rules easier or preferable. Ease ties in 8 of 9 pairs, which may be a ceiling: the reader read the same three questions in every round. Preference separated the arms: the reader picked the rules in 2 of 3 pairs after the table, and in 3 of 3 after the headings and lists.

The limits of the first round apply to all three: one reader, who helped write the rules and could recognise their style.

## 2026-10-09: no title above the answer

After the third blind round, rule 5 gained one sentence: never put a title above the opening answer. The full chat suite ran again: 13 cases, 3 runs per arm, 10.4 minutes, $6.41 at list price.

The sentence works. No answer with the rules opened with a title, against 3 of 36 in the run before. Without the rules 22 of 36 did.

The suite scored 83% with the rules and about 70% without, against 88% and about 69% in the run before. Two cases account for the drop, and in both the answers have the same shape as in the run before:

- en-db-connections: the answer came first in 0 of 3 runs, against 3 of 3. All six openings in the two runs name the same cause in nearly the same words: up to 120 connections against 97 that Postgres accepts. The judge passed all three before and failed all three now.
- pl-handles-verdict: at most four points in 1 of 3 runs, against 3 of 3. In both runs the answers hold a table with three rows, 2 or 3 list items and 230 to 270 words. In the arm without the rules, which did not change, the same grader went from 0 of 3 to 2 of 3.

So the noise per case is larger than the 11 points measured earlier: these two cases moved by 34 and 22 points on answers of the same shape. A difference between two runs of one case says little on its own. The blind readings weigh more.

## 2026-10-12: /coldread:write with the Polish lint rules

Since the last run of the write suite, the skill gained Polish Vale rules, rules for repository templates, line wrapping and English software terms in Polish text, and Polish style anchors. Vale also checks drafts saved as `.txt` now. The full write suite then ran again on Claude Code 2.1.296: 4 cases, 3 runs per arm, 18.4 minutes, $4.15 at list price.

The suite scored 85% with the skill and 59% without it, against 76% and about 50% in the full run of 9 October. A run with the skill still cost 2.8 times as much as one without.

| Case | With skill | Without | Last run of the case, with / without |
|---|---|---|---|
| write-slack-pm-pl | 100% | 80% | 93% / 60% |
| write-pr-en | 100% | 89% | 100% / 78% |
| write-rewrite-facts | 75% | 67% | 92% / 67% |
| write-trigger-pl | 67% | 0% | 67% / 0% |
| All cases | 85% | 59% | 76% / 50%, full run |

What changed:

- Vale ran. The report of every run with the skill gives a Vale result, 0 warnings each time, including the Polish config in both Polish cases. On 9 October the skill could not run shell commands under eval and skipped Vale. This run kept no traces, so the Vale results rest on the skill's own reports.
- Slack: the ask came first in 3 of 3 runs with the skill, against 2 of 3 last time. The labels `Phase A`, `option B` and `D3` stayed out of the message in 3 of 3 runs with the skill and 0 of 3 without it. Over the three runs of this case since the label rule, that makes 9 of 9 against 0 of 9.
- Rewrite: the skill stated a claim the source does not make in 3 of 3 runs, against 1 of 3 last time. The run without the skill did so in 2 of 3. One text opens with "Since the migration went live on 2 June", which merges the migration with the 2 June cutover, two events the source keeps apart. The skill's own rule forbids picking one reading of an ambiguous source. The judge split its votes in 2 of the 3 failed runs, so part of this drop may be noise.

What this run does not show:

- Which change caused which difference. The skill, the lint step and the Claude Code version all changed since the last run.
- Whether the Polish rules catch anything in practice. Vale reported 0 warnings in all 12 runs, and the reports do not say whether the skill fixed warnings before that.

## 2026-10-12: two names stay two things

After the run above, the rewrite rule in /coldread:write gained two sentences: treat two names in the source as two things unless you checked that they are one, because writing them as one event adds a fact. The example in the skill uses other names than the test case. The rewrite case then ran again: 3 runs per arm, 4.6 minutes, $0.95 at list price.

The skill kept the migration and the 2 June cutover apart in 3 of 3 runs, against merging them in the run above. The case still scored 83% in both arms, because the invented-claims grader does not test what the case was built for:

- It failed 2 of the 3 texts with the skill, unanimously. Both say that using the idempotency layer also cut the latency. The source supports that reading: the deduplication runs "yielding a 37% reduction in p95 latency".
- It passed 2 of the 3 texts without the skill, although both open with a claim the source does not make: that the 2 June cutover was the switch to a new system and the migration itself.

The grader needs to say both things before this case can measure the rule.
