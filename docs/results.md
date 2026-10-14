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

After the run above, the rewrite rule in /coldread:write gained two sentences. They say to treat two names in the source as two things unless you checked that they are one, because writing them as one event adds a fact. The example in the skill uses other names than the test case. The rewrite case then ran again: 3 runs per arm, 4.6 minutes, $0.95 at list price.

The skill kept the migration and the 2 June cutover apart in 3 of 3 runs, against merging them in the run above. The case still scored 83% in both arms, because the invented-claims grader does not test what the case was built for:

- It failed 2 of the 3 texts with the skill, unanimously. Both say that using the idempotency layer also cut the latency. The source supports that reading: the deduplication runs "yielding a 37% reduction in p95 latency".
- It passed 2 of the 3 texts without the skill. Both open with a claim the source does not make: that the 2 June cutover was the switch to a new system and the migration itself.

The grader needs to say both things before this case can measure the rule.

## 2026-10-12: the invented-claims grader, fixed

The invented-claims grader of the rewrite case now says what the source supports and what it does not. A text may say that the idempotency layer or the deduplication brought the latency down, because the source says the deduplication yields that drop. A text fails if it says that the migration happened on 2 June, or that the cutover switched to a new system. The grader also reads only the rewritten text, not Claude's report around it. The case then ran again: 3 runs per arm, 4.1 minutes, $0.94 at list price.

| Grader | With skill | Without |
|---|---|---|
| No invented claims | 2 of 3 | 0 of 3 |
| Facts kept | 3 of 3 | 3 of 3 |
| Plain words | 1 of 3 | 3 of 3 |
| Reports what changed | 3 of 3 | 0 of 3 |
| Case score | 75% | 50% |

- All 3 texts without the skill open with a sentence such as "Since we switched over to the new system on 2 June", which merges the migration with the cutover. The grader now fails them. None of the 3 texts with the skill merges the two events. The third text with the skill failed the grader unanimously, and the votes do not say which claim the judge objected to.
- Plain words fell from 3 of 3 to 1 of 3 with the skill. The two failed texts drop `leverages` and `robust` and explain idempotency, which is all the grader asks. The judge split its votes 1 to 2 in both, so this looks like judge noise.

## 2026-10-12: review comments, explainers and a claim check

The changed skill scored 86% on 8 cases, against 70% for the skill before the changes and 53% without it. The gains come from the four new cases, which test the new rules, so they favour the changed skill by design. /coldread:write gained these rules:

- The brief says where the text will be read. A review comment holds one problem in at most three sentences, with the fix as a suggestion block, and a nice-to-have stays in the report for the user. A chat message, an issue comment or a commit body gets no Details.
- When the reader must understand how something works, the skill defines each term with an example and follows one case from start to end.
- A new step checks that each claim in the main part has a source: the user's notes, a check that ran, or code that was read.
- A verified fact is tied to a commit, not to the day of the check. The text never points to a file on the writer's machine. Tests are split into what ran, what was only read and what is planned. An open question names nobody as its owner unless they agreed.
- A PR description, a review or a message gets no title heading. Details go before a section that a template keeps last, and a section for a second reader gets its own reader line.
- Vale flags paths on the writer's machine and the dates of checks. `lint.sh` also runs a repository's own rules from `.coldread/vale/styles`.

Setup: Claude Code 2.1.287 on a second computer, the default agent model, Sonnet as judge, 3 runs per arm. Bash was blocked there and files could not be written outside the case, so Vale, the word count and most cold reads did not run in either arm. The skill before the changes ran the same way. For six cases it was the version from before the five commits of the runs above. For the review and rewrite cases it was the version after them.

| Case | Skill before | Skill after | Without |
|---|---|---|---|
| write-review-comments-en | 58% | 100% | 50% |
| write-explain-en | 33% | 100% | 33% |
| write-design-notes-en | 53% | 100% | 40% |
| write-pr-en | 44% | 78% | 100% |
| write-pr-template-en | 100% | 78% | 67% |
| write-rewrite-facts | 75% | 75% | 75% |
| write-slack-pm-pl | 93% | 93% | 60% |
| write-trigger-pl | 100% | 67% | 0% |
| All cases | 70% | 86% | 53% |

What improved, as runs passed out of 3 with the changed skill against the skill before:

- Review: comments of at most three sentences 3 against 1, and the nice-to-have kept out of GitHub 3 against 0.
- Explainer: every term explained, most with an example, 3 against 0. One case followed from start to end 3 against 0. The quiz passed 3 of 3 in every arm, so it does not separate them.
- Design doc: no date of the re-check 3 against 0, nobody named as the one to decide 3 against 0, and no path to the author's file 3 against 2.

Where the changed skill did worse or did not move:

- Template: the product section passed 1 of 3 against 3 of 3. One text says users without a timezone get the email "at the same time as today" instead of at 09:00 UTC. Another keeps 09:00 UTC and still failed, and the votes do not say why.
- Trigger: the ask came first in 2 of 3 runs, in both runs of the changed skill, against 3 of 3. The failed text asks in its second sentence, after a long note about checks that could not run.
- Rewrite: no arm passed the invented-claims grader. On the first computer the skill passed 2 of 3 with the same grader, so the claim check made no difference here.
- PR: facts kept rose to 2 of 3 from 0 of 3. A word search finds all four facts in each of the three earlier texts, so those earlier failures are probably the judge's.

Reading every failed text changes the picture for the four cases that existed before. Both versions scored 78% on them, and the failures differ in kind:

- The skill before failed "the ask comes first" in two PR texts that open with a title heading. The judge counts the title as a sentence, so the ask lands third. The changed skill writes no title.
- The changed skill failed the same grader three times, and all three are judge errors. Two texts ask in their first sentence, as in "One trade-off needs your approval before merge: invoice download links become presigned S3 URLs…". The third, in Polish, asks for the review in its second sentence. The judge failed each by 3 votes to 0, so the three votes on one text are not independent checks.
- Its one failure of facts kept had split votes, and all four facts are in the text. Only the table size sits under "On staging", and the backup time follows in the next sentence.
- The template regression is real: one product section dropped the exact time. After this run, the rule for a second reader gained one sentence: simplify the words, not the facts. That sentence has not been measured yet.

Three things changed during this work, each before the run in the table. A first run of the changed skill scored 79% and showed three problems. A title above a PR description pushed the ask to its third sentence. The review summary used its follow-up for the nice-to-have. An open question still named who could decide. The skill now covers all three. The review case now gives the replacement line, because the skill rightly refused to guess code it could not see. The open-questions grader of the design doc case failed a text that met all its conditions, so it is now two graders.

Why Sonnet judges this run: with Haiku, a PR text that asks for the approval in its second sentence failed "the ask comes first" by 3 votes to 0. The same text failed "facts kept" with all four facts in it. Sonnet passed a Slack text of the same shape on every grader, for about $0.04 per run.

What this run does not show:

- Whether the changes help when Vale and the cold reader run, because neither ran here.
- How these scores compare with the runs above, because the judge, the computer and the Claude Code version all differ.
- How the rules hold up on cases from another author. One more caveat comes from this computer: its organisation-level instructions load into eval runs, and in one run they supplied surnames for two people the notes named by first name only.

All runs in this section cost $32.53 at list price. That includes the first run of the changed skill and a baseline judged by Haiku.

## 2026-10-12: the review and explainer rules, measured with Vale

The run in the section above could not run Vale or most cold reads. This run measured the changed skill again on the first computer, where both run. Setup: Claude Code 2.1.296, the default agent model, Haiku as judge, 8 cases, 3 runs per arm and 3 runs at a time. The skill on main ran in a second worktree on the same 8 cases. It needed no arm without a skill, because the run of the changed skill has one. The run of the changed skill took 12.8 minutes and cost $9.57, the run of main 9.0 minutes and $6.45.

The changed skill scored 90%, against 77% for the skill on main and 53% without a skill. The four new cases carry the gain, 83% against 57%. On the four older cases both versions stayed near the top, 96% against 98%. The last full run of those four, earlier today, gave 85% with the skill and 59% without it. Since then the rewrite case gained the rule on two names and a new grader, so that comparison is not clean.

| Case | Skill on main | Changed skill | Without |
|---|---|---|---|
| write-review-comments-en | 60% | 100% | 50% |
| write-explain-en | 50% | 100% | 33% |
| write-design-notes-en | 50% | 100% | 60% |
| write-pr-template-en | 67% | 33% | 89% |
| write-pr-en | 100% | 100% | 78% |
| write-rewrite-facts | 92% | 83% | 50% |
| write-slack-pm-pl | 100% | 100% | 67% |
| write-trigger-pl | 100% | 100% | 0% |
| All cases | 77% | 90% | 53% |

Vale ran. In each version, 23 of the 24 reports give a lint result, and the other one does not mention the lint at all. Each result was 0 warnings, except one review report that mentions two style suggestions, which the skill fixed.

What improved, as runs passed out of 3 with the changed skill against the skill on main:

- Review: comments of at most three sentences 3 against 0, and the nice-to-have kept out of GitHub 3 against 0.
- Explainer: terms explained with examples 3 against 0, and one case followed from start to end 3 against 0.
- Design doc: no date of the re-check 3 against 0, no path to the author's file 3 against 0, and nobody named as the one to decide 3 against 0.

Where the changed skill scored lower, every failed text was read:

- Template, 33% against 67%: most failures are the judge's. All three product sections name 09:00 UTC for users without a timezone, yet the judge failed two of them. It also failed a Tests section that keeps what ran apart from what did not. One failed text has nothing after its last section. The other two end with the attribution line "Generated with Claude Code" after the product section, which the grader counts as text after the last section. The skill on main did the same in one of its three texts.
- Rewrite, 83% against 92%: one text failed "reports what changed", although its report lists what it removed and added. Another failed "no invented claims". It keeps the migration and the cutover apart, but says that duplicates "no longer occur", close to the sentence that Sonnet failed below.

Both cases then ran again with Sonnet as judge, 3 runs per version with the skill, for $3.86:

| Case | Skill on main | Changed skill |
|---|---|---|
| write-pr-template-en | 100% | 92% |
| write-rewrite-facts | 83% | 75% |

- Template: Sonnet accepted the attribution line after the last section. Its one failure is a product section that says users without a timezone get reminders "at the old time" instead of at 09:00 UTC. Over both judges, 5 of 6 product sections from the changed skill name that time, against 4 of 6 from the skill on main.
- Rewrite: Sonnet failed 2 of 3 texts from main and 3 of 3 from the changed skill for the same kind of sentence. They say that the pipeline "no longer creates duplicates" or "no longer lets duplicates through", which makes the pipeline their cause, and the source does not say that. The one text that passed says the pipeline "removes duplicates reliably". Both versions share this weakness.

What this run does not show:

- Whether the sentence on trailers works. Over both judges, 3 of 6 template texts from each version end with the attribution line after the section that the template keeps last.
- How these scores compare with the run on the second computer, because the judge and the lint differ.
- How the rules hold up on cases from another author.

All runs in this section cost $19.88 at list price.

## 2026-10-12: nothing after the last section

The run above showed that the sentence on trailers did not work. In 3 of 6 template texts from each version, the attribution line "Generated with Claude Code" followed the section that the template keeps last. The rule now says that nothing may follow such a section, not even a trailer, and that the skill leaves the trailer out and says so in its report. The template case then ran 6 times with the changed skill and Haiku as judge, in 2.9 minutes, for $2.18.

No text put the attribution line after the last section, and all 6 reports say that the skill left it out. The case scored 88%. Every failed text was read:

- One text opens with a paragraph above Summary, which the template does not have. The judge failed its section order by 4 votes to 0.
- One text has nothing outside the template's sections, and the judge failed its section order by 2 votes to 1.
- One product section says that users without a timezone get reminders at "9 in the morning UK winter time" instead of at 09:00 UTC. A text from the skill on main did the same in the run above.

## 2026-10-13: channels, the user's voice, replies and OpenCode, without shell steps

/coldread:write scored 90% on 11 cases with the skill and 65% without it. Bash was blocked on this computer, so the skill ran without Vale, the word count and the facts check. Two new behaviours went wrong, a date kept in the design doc and a reply skill that asked instead of drafting. Both were fixed and measured again, in the next section.

Changes since the last run:

- The rules for a review, an explainer, a prompt for a new agent session, and long documents, sets and decision documents moved to files in `channels/`. The skill reads the file when the brief's channel calls for it.
- When a text goes out under the user's name, a How I write note in the user's instructions wins over the skill's own shape, such as its labels on review comments.
- The cold reader keeps its report under 300 words and retells the text's points, and the skill compares that retelling with the brief.
- A rewrite runs `facts.sh`, which lists the numbers and code spans that left the text. The skill never posts, sends or commits a text.
- `/coldread:reply` reads a message the user received and drafts the answer.
- Graders that a pattern can decide now use `regex` on a file the case asks Claude to save: in the design doc and template cases, and in two of the three new write cases.

Setup: Claude Code 2.1.287 on a third computer, the default agent model, Sonnet as judge, 11 cases, 3 runs per arm, `--allow-tools Write`. The Bash sandbox refused to start because `~/.docker/cli-plugins` holds links into Docker Desktop, and pointing `DOCKER_CONFIG` at an empty folder did not help. The run took 11.8 minutes and cost $13.00 at list price. A run with the skill cost 2.7 times as much as one without.

| Case | With skill | Without |
|---|---|---|
| write-trigger-pl | 100% | 0% |
| write-explain-en | 100% | 44% |
| write-review-comments-en | 92% | 50% |
| write-slack-pm-pl | 93% | 60% |
| write-design-notes-en | 83% | 61% |
| write-review-voice-en | 100% | 83% |
| write-rewrite-facts | 75% | 58% |
| write-pr-en | 100% | 100% |
| write-pr-template-en | 100% | 100% |
| write-prompt-handoff-en | 100% | 100% |
| reply-decode-pl | 50% | 58% |
| All cases | 90% | 65% |

What held after the move to channel files, as runs passed out of 3 with the skill against without:

- Explainer: terms explained with examples 3 against 1, and one case followed from start to end 3 against 0.
- Review: comments of at most three sentences 3 against 0, and the nice-to-have kept out of GitHub 3 against 0. One review stated that no test covers month-first files but did not ask for one, because the notes did not say the test belonged to this pull request. Its report said so.
- Voice: every comment ended on a question 3 against 1. Both arms kept labels and bold out, so a style quoted in the request is enough for Claude without the skill.

What went wrong:

- Design doc: all 3 texts with the skill kept the date of the re-check, as in "As of 6 October 2026, the staging numbers still hold". In the run on the second computer, none did. The cause was a sentence added to the skill: keep a date, "as of", when nothing else anchors a fact about a running environment. A narrower version of the sentence gave the same result in 3 of 3 runs, so the sentence is gone. A project that wants such dates can say so in its own instructions.
- Reply: in 2 of 3 runs the skill asked which option the user wanted and wrote no reply. Two graders were also stricter than their case. One failed an opening that named Ania's question, because the opening left out how the fix works. The other failed answers that repeated what her message implies about `PAY-212`.

What does not separate the arms yet:

- Template and prompt cases: both arms passed every grader. With section order and the trailer checked by patterns, Claude without the skill gets them right, so the judge's earlier failures there were noise. The prompt case's notes dictate the content, so it needs a harder version.
- Rewrite: no arm passed the invented-claims grader, as in the runs before.

## 2026-10-13: the fixes

The reply skill now recommends an option, drafts the reply for it and gives the other option's reply in one line. It asks the user first only when it cannot recommend either option. It opens with the sender's request, with no label above it. The ask-first grader no longer asks for how the fix works, and the ticket grader accepts what the message itself implies about `PAY-212`. The date sentence is back to its earlier form.

| Case | With skill | Without |
|---|---|---|
| reply-decode-pl | 100% | 67% |
| write-design-notes-en | 100% | not run |

- Reply: the opening named Ania's request 3 against 0, a draft reply came in 3 against 3, and nothing was invented about the ticket 3 against 2.
- Design doc: no text kept the date of the re-check, against 3 of 3 with the added sentence.

The two runs above cost $2.11 at list price, and the run of the narrower date sentence $0.90.

## 2026-10-13: chat rule 10, questions that stand alone

The chat rules gained a tenth rule: a question to the user says what it is about, why it is needed, its options and what Claude will do without an answer. A new Polish case hands Claude its own notes, full of labels such as `F03` and "decyzja 2", and asks what the user must answer. With the rules the case scored 100%, without them 67%: 3 runs per arm, Sonnet as judge, $0.50 at list price.

The whole difference is the default. With the rules, 3 of 3 answers said what Claude would do without an answer, against 0 of 3. Both arms named each question's subject in plain words and gave its options. Without the rules, every answer still led each question with its label, as in "`F03`, limit uploadu", which the grader allows next to plain words.

What this does not show: the notes in the case explain each label, so Claude without the rules can copy those words. A case whose labels Claude coined earlier in the same session would test the rule harder.

## 2026-10-13: the review cases again, before the push

After the runs above, the review rules gained one sentence: when a project's review style and the user's How I write note disagree, the project's style wins in that project. The two review cases then ran again with the skill, 3 runs each.

- Review comments: 100%. The missing test was asked for in 3 of 3 runs, against 2 of 3 in the full run.
- Review in the user's voice: the judge failed comments whose question is phrased as a request, such as "Add one that expects 10.13?", although every comment ended with a question mark. The user's own style ends that way, so the grader is now a pattern that fails any comment not ending in "?". With it, both arms passed every grader in 3 of 3 runs. A style quoted in the request is enough for Claude without the skill, so this case does not test the real use: a note in the user's CLAUDE.md, which evals do not load. The "3 against 1" for questions in the full run above was measured with the old grader.

These checks cost $2.98 at list price.

## 2026-10-13: structure cases, before any change

This run is the baseline for the structure plan in `docs/research/structure-plan.md`: three new cases that test document type, splitting and headings, measured before `write` changes. The skill raised the three cases from 50% to 64% on average, but it scored lower than no skill on the ADR case, because it rewrote the ADR's fixed sections.

Setup: Claude Code 2.1.287, the default agent model Claude Opus 5.5, Sonnet as judge, 3 cases, 3 runs per arm, Write allowed but not Bash. Bash was blocked because the Docker credential store on this computer holds a symbolic link, so the skill skipped Vale, the word count and the facts check in both arms. The final runs cost $4.07.

| Case | With skill | Without | Difference |
|---|---|---|---|
| write-headings-carry-en | 100% | 58% | +42 |
| write-runbook-split-en | 50% | 25% | +25 |
| write-adr-one-decision-en | 42% | 67% | −25 |
| All cases | 64% | 50% | +14 |

The graders that matter for the plan, as runs passed out of 3, with the skill against without:

- The runbook keeps the migration history and the open questions out: 0 against 0. The skill put them under Details at the end of runbook.md in every run, so Details took in material for another document.
- The skill told the user where that material belongs: 0 against 1.
- The ADR has Context, Decision and Consequences in order: 0 against 3. The skill replaced the fixed sections with sentence headings, such as "Jobs live in Postgres because they must commit with their data", because its rule that headings say something does not know that an ADR has fixed sections.
- The ADR file holds one decision: 0 against 0. Both arms wrote both decisions into the one file the prompt named; two of three runs in each arm told the user that the notes hold two decisions.
- The design doc's headings alone tell the decision, the rejected options and the approval: 3 against 1. Generic headings such as "Overview": none in 3 runs against 2 runs with one.

Three graders changed before these numbers, after a first run showed they judged unfairly:

- `steps-kept` asked for four mitigation steps with commands, but the fourth step, escalation, has no command, so the judge failed complete runbooks. It now names the three commands and the escalation.
- `goals-first` looked for the words "Goal" and "Alternatives" in headings, and failed sentence headings such as "Why not one global limit or a limit per IP address". It is now an LLM grader that checks the order of the content.
- The ADR graders had no file to read, so the judge saw only Claude's final message. The prompt now names the file, `doc/adr/0007-job-system.md`, and the graders read it. A new regex grader fails the file when it also holds the retry policy.

What this run does not show:

- Three runs per arm is little, so one run moves a grader by 33 points.
- The ADR prompt names one file, which pushes both arms to write one file. The case tests whether Claude says that the notes hold two decisions, not whether it writes two files unasked.
- The same author wrote the cases, the graders and the plan.

## 2026-10-13: fixed sections for an ADR

The skill now treats the sections everyone expects in an ADR as a template, from the new `channels/doc-types.md`: Status, Context, Decision and Consequences keep their names, and the first sentence under each carries the claim. This fixed the ADR case, which went from 42% to 100% with the skill, and the two older template cases did not get worse.

Setup as in the baseline above: Sonnet as judge, 3 runs per arm, Write allowed but not Bash. The run cost $4.07.

| Case | With skill | Without | Baseline with skill |
|---|---|---|---|
| write-adr-one-decision-en | 100% | 50% | 42% |
| write-pr-template-en | 100% | 100% | not run |
| write-design-notes-en | 100% | 50% | not run |

What changed in the ADR case, as runs passed out of 3 with the skill, against the baseline:

- Context, Decision and Consequences in order: 3 against 0.
- The file holds one decision: 3 against 0. The skill wrote the queue decision to `doc/adr/0007-job-system.md` and drafted the retry policy as a second ADR in its report.
- Claude told the user that the notes hold two decisions: 3 against 2.

In one run Claude said it could not save the second ADR as a file, although Write was allowed; it showed the draft in its report instead. The ADR also added a reason the notes did not give, that a message broker cannot take part in a Postgres transaction. Neither is graded here.

## 2026-10-13: a control case for the ADR rule, and the claims an ADR adds

The ADR rule was written after reading runs of the case that measures it, so a new case checks it on input it has not seen. `write-adr-madr-template-en` gives the team's own MADR template, a common ADR format with the sections Context and Problem Statement, Considered Options and Decision Outcome. The repository's template won in 3 of 3 runs with the skill: no run fell back to the default Context, Decision and Status sections.

Setup as in the baseline above. The final runs cost $2.50.

| Case | With skill | Without |
|---|---|---|
| write-adr-madr-template-en | 100% | 67% |
| write-adr-one-decision-en | 78% | 67% |

Without the skill, all 3 MADR runs lost a fact from the notes, such as the 15-minute expiry of the presigned URLs.

Changes before these numbers:

- `doc-types.md` now lists Status after Decision, in the order of Nygard's post, which it cites. It had put Status second.
- The rule for a single named file now says to propose the second ADR with its file name and ask. In the run before, Claude said it could not save the second file, which was not true; no run says so now.
- `nygard-sections` is now a regex, and `status-present` is new, because the judge failed an ADR whose sections were all present and in order.
- `no-default-sections` in the MADR case allowed no `### Consequences`, which the MADR template itself has under Decision Outcome. It now forbids only bare Context, Decision and Status headings.

What the ADR case still shows:

- A new grader, `no-invented-claims`, failed in 3 of 3 runs in both arms. The ADRs state claims the notes do not give as plain fact, such as "A separate broker such as RabbitMQ cannot join a Postgres transaction" and "Job traffic adds to the load on that Postgres database". The skill's claim check should cut these or mark them as not verified, and it does not in an ADR. This is a gap in the claim check, outside the structure plan.
- One run with the skill left `## Status` empty, so the acceptance date was lost; `status-present` checks only the heading. The same run also lost why another broker was not wanted, which `why-kept` caught.

## 2026-10-13: runbooks and design docs in doc-types.md

`channels/doc-types.md` now covers runbooks and design docs as well as ADRs. A runbook keeps a fixed order, from what the alert means to escalation, and leaves out history and open design questions; a design doc keeps Ubl's order with headings that state conclusions. Material meant for another document no longer goes under Details: the skill names that document and its file in the report and asks. The runbook case went from 50% to 100% with the skill.

Setup as in the baseline above. The runs cost $8.45.

| Case | With skill | Without | With skill before this step |
|---|---|---|---|
| write-runbook-split-en | 100% | 42% | 50% |
| write-headings-carry-en | 100% | 75% | 100% |
| write-adr-one-decision-en | 83% | 56% | 78% |
| write-adr-madr-template-en | 100% | 78% | 100% |
| write-pr-template-en | 100% | 100% | 100% |

In the runbook case the migration history and the open questions stayed out of runbook.md in 3 of 3 runs with the skill and 0 of 3 without, and the skill named a design doc or an ADR for them in all 3.

The design doc case first scored 92%: one run used the heading "Alternatives considered", the label in the list of Ubl's sections, and its headings no longer said that the platform team must approve the Redis memory. The list now describes what each section holds instead of naming it, with an example of a heading that states a conclusion, and the case went back to 3 of 3. That fix rests on one run, so the full run with 5 runs per arm decides whether it holds.

The ADR case still fails `no-invented-claims` in every run of both arms; see the entry above.

## 2026-10-13: the full suite after the structure changes, 5 runs per arm

With the structure rules frozen, the whole suite ran once: 18 cases, 5 runs per arm, including the three held-out cases written before any run of them. The skill passed 93% of the checks against 65% without it. The held-out runbook and design doc gained 35 and 40 points, the held-out PR description shows no leak of the document rules, and no older case got worse by more than one run.

Setup: Claude Code 2.1.287, the default agent model Claude Opus 5.5, Sonnet as judge, 5 runs per arm, Write allowed but not Bash, so Vale, the word count and the facts check did not run in either arm. The run took 35 minutes and cost $39.19.

| Case | With skill | Without | Kind |
|---|---|---|---|
| write-runbook-pl | 90% | 55% | held-out |
| write-design-ops-mixed-en | 75% | 35% | held-out |
| write-pr-history-en | 93% | 93% | held-out |
| write-runbook-split-en | 90% | 40% | structure |
| write-headings-carry-en | 95% | 75% | structure |
| write-adr-one-decision-en | 83% | 63% | structure |
| write-adr-madr-template-en | 93% | 93% | structure |
| write-trigger-pl | 100% | 0% | older |
| write-explain-en | 100% | 47% | older |
| write-review-comments-en | 100% | 50% | older |
| write-design-notes-en | 100% | 50% | older |
| write-slack-pm-pl | 96% | 60% | older |
| write-pr-template-en | 100% | 95% | older |
| write-pr-en | 93% | 87% | older |
| write-review-voice-en | 100% | 100% | older |
| write-prompt-handoff-en | 100% | 100% | older |
| reply-decode-pl | 85% | 70% | older |
| write-rewrite-facts | 75% | 65% | older |
| All cases | 93% | 65% | |

What the held-out cases show, as runs passed out of 5 with the skill:

- The Polish runbook kept the history and the open question out in 5 of 5, and named a design doc or an ADR for them. Without the skill, the history stayed in 1 of 5 runs, and 2 of 5 dropped it without telling the user.
- The design doc with on-call steps mixed in left out all three on-call steps in 4 of 5 runs, and 4 of 5 files say that the steps go in a separate runbook. But 4 of 5 still named `thumbctl` in a short section on operations, and 2 of those 4 gave some of its commands; 1 run gave all three. The rule says what a design doc leaves out but not that a pointer must not repeat the commands, and this was not tuned after the run.
- The PR description used no document sections, such as Context or Goals, in 5 of 5, and opened with the final state, not the history, in 5 of 5.

Graders that failed with the skill in 3 or more of 5 runs:

- `no-invented-claims` in the ADR case and in `write-rewrite-facts`: 5 of 5 each. The skill states explanations the notes do not give as plain fact. This is the gap in the claim check named in the entries above.
- `no-invented-ticket` in `reply-decode-pl`: 3 of 5.
- `no-ops-steps` in the held-out design doc: 4 of 5, as above.

The older cases moved within one run of the last full run on 2026-10-13: for example `write-pr-en` lost one run of 5 on `ask-first`, and `write-review-comments-en` went from 92% to 100%. Three of five runs of `write-runbook-split-en` and four of five of `write-headings-carry-en` passed every grader, so the earlier 3-of-3 results there were partly luck.

What this run does not show:

- One author wrote the rules, the cases and the graders, the held-out ones included.
- Bash was off, so the steps that need a shell were not measured.
- The `ops-moved` grader of the held-out design doc reads only Claude's final message, so it passed runs whose file still held the commands; `no-ops-steps` reads the file.

## 2026-10-13: the claims graders, calibrated against labelled texts

The two `no-invented-claims` graders failed every run in both arms of the full run above, so they were checked before anything else. Each grader judged hand-labelled texts in `plugins/coldread/evals-calibration/`: clean texts, texts with an invented claim, and an added claim marked in the text as an assumption. With the old wording, the ADR grader failed a clean ADR in 1 of 3 runs and a marked claim in 2 of 3, and the rewrite grader failed the same clean text, word for word, in 5 of 6 runs. Both graders now judge the text sentence by sentence against a list of what is allowed, and every labelled text got its label in 3 of 3 runs in two rounds in a row, 48 judgements in all, with Sonnet as judge. Haiku failed a clean rewrite in 3 of 3 runs, so Sonnet stays the judge. The rewrite case now saves its text to `rewrite.md`, and its graders read only that file.

With the calibrated graders, 5 runs per arm, the two cases still fail the claims grader in 5 of 5 runs in both arms. The runs cost $4.17.

| Case | With skill | Without |
|---|---|---|
| write-adr-one-decision-en | 83% | 63% |
| write-rewrite-facts | 75% | 75% |

What the skill adds, from reading all 10 texts with the skill:

- In the ADR, 5 of 5 explain why RabbitMQ was rejected with a general fact about the tool: a broker cannot take part in a Postgres transaction. 5 of 5 add the consequence that job traffic loads the database, and 4 of 5 add a recommendation to revisit the decision if the load grows.
- In the rewrite, 3 of 5 turn a definition into a claim about this system, such as "the same item can arrive more than once" or "3 streams handled in parallel".
- In all 10 runs the report lists these additions and asks the user to confirm or cut them. None marks them in the text, although the claim check in `SKILL.md` asks for both.

Without the skill, 3 of 5 rewrites say the migration happened at the 2 June cutover, which the source does not say; no rewrite with the skill does. The binary grader hides this difference.

This corrects the earlier entries: the 5 of 5 failures there came partly from the graders, and the ADR claims are additions the report already lists, not claims passed off silently.

## 2026-10-13: the claim rule, measured with narrow graders

The claim check now asks for a mark in the text, such as "(to confirm)", on every claim about the user's system that has no source: an inferred consequence, an added recommendation, a definition applied to the system, or a completed detail such as a year. General facts about a named tool need no mark but go in the report. The maintainer chose this rule over marking everything or marking nothing.

Broad graders that judged "any new information" failed texts that a direct question to the same model passed, word for word, with no single sentence to blame: they flagged a text for mentioning a topic from their own list of examples, even as a question. So each case now has narrow graders, each asking about one kind of addition, calibrated twice on hand-labelled texts in `plugins/coldread/evals-calibration/`. The real rewrite and seven trimmed variants of it stayed unstable on `no-invented-design` and were dropped, so that grader is calibrated only on hand-written texts, and its only failing example is a text that invents a cause.

| Case | Check | With skill | Without |
|---|---|---|---|
| write-rewrite-facts | migration and cutover kept apart | 5 of 5 | 0 of 5 |
| write-rewrite-facts | no invented cause of duplicates | 5 of 5 | 2 of 5 |
| write-rewrite-facts | no invented design of the pipeline | 4 of 5 | 0 of 5 |
| write-adr-one-decision-en | no year added to "3 September" | 5 of 5 | 0 of 5 |
| write-adr-one-decision-en | recommendation to revisit marked or absent | 4 of 5 | 0 of 5 |
| write-pr-claims-en, held-out | no unmarked claim on locks, production or cost | 14 of 15 | 15 of 15 |

In the full run that followed, the rewrite's cause and design graders passed 4 of 5 without the skill, so these without-skill counts vary by up to 4 runs of 5.

The year rule was added after a run in which every ADR with the skill dated the decision "3 September 2026". The runs in this entry cost about $16, and the calibration rounds about $20.

What this does not show:

- The held-out PR case shows no gain: without the skill, Claude also kept to the notes. Its graders were also rewritten after its first run, because the broad grader failed texts the model itself judged clean, so it is not a blind test any more.
- The ADR grader for database load could not be calibrated. After the rule that a necessary consequence is a fact, "job traffic adds reads and writes to the database" passes and a claim about how much load fails; but on two real ADRs whose load sentence carried a mark, the judge split. That grader stays in the case as an indicator, and the 3 of 5 ADRs it failed before the change mark the amount of load and state only that queries exist.
- Narrow graders catch only the kinds of additions they name. A new kind of invented claim needs a new grader.

## 2026-10-13: the full suite after the claim rule, 5 runs per arm

The whole suite ran again after the claim rule: 19 cases, 5 runs per arm. The skill averaged 92% per case against 66% without it, against 93% and 65% in the full run before the rule; counted over all checks, 373 of 400 passed with the skill and 268 of 400 without. The run took 40 minutes and cost $42.72; setup as in that run.

| Case | With skill | Without | With skill, run before |
|---|---|---|---|
| write-adr-one-decision-en | 91% | 56% | 83% |
| write-rewrite-facts | 97% | 77% | 75% |
| write-pr-claims-en | 100% | 100% | new |
| write-trigger-pl | 60% | 0% | 100% |
| write-runbook-pl | 75% | 60% | 90% |
| write-headings-carry-en | 90% | 55% | 95% |
| write-review-comments-en | 95% | 50% | 100% |
| All cases | 92% | 66% | 93% |

The other 12 cases moved by at most one run of 5. The two cases that dropped are not explained by the claim rule:

- `write-trigger-pl` grades Claude's whole final message. In 2 of 5 runs Claude opened the message with a note that it could not save a file, and the judge read that note as the first sentences of the PR description, which itself opens with the fix and the ask. The grader should read a saved file, as the rewrite case now does.
- `write-runbook-pl` failed `design-moved` in 2 of 5 runs in which Claude named an ADR for the history in its report but kept one sentence in the runbook, that a worker reads the webhooks from a Kafka queue, because the runbook uses the word partition. Whether that sentence is history or what the on-call engineer needs is a judgment call.

## 2026-10-13: three fixes from a review of the branch

A review of the whole branch found three things in `SKILL.md`: a sentence about Details that read two ways, an example of a mark, "Job traffic adds load to the database (to confirm)", that contradicts the rule that what follows from the notes by necessity is sourced, and that rule itself, which only the graders stated. The sentence is now two, the example is "Job traffic slows the application's queries (to confirm)", and the rule is in the claim check.

The four cases these fixes touch ran again, 5 runs per arm, at about $11.

| Case | With skill | Without | With skill, full run |
|---|---|---|---|
| write-adr-one-decision-en | 93% | 56% | 91% |
| write-runbook-split-en | 90% | 45% | 90% |
| write-runbook-pl | 85% | 50% | 75% |
| write-pr-template-en | 95% | 100% | 100% |

The first run of `write-pr-template-en` scored 70% with the skill and 10% without, because the account's spend limit stopped 7 of its 10 runs; the table shows the rerun, with no errors.

## 2026-10-14: the trigger case reads a saved file

`write-trigger-pl` graded Claude's whole final message, so a note before the PR description, such as "I could not save a file", counted as its first sentences. The prompt now asks to save the description to `pr.md`, and `ask-first` reads only that file. Its wording also now says that a plain request for a review counts as the ask, because the judge passed and failed the same opening, "Proszę o review", in different runs. Calibrated on three texts, two from real runs, it matched all 18 judgements over two rounds; one of those labels changed after the first round, from fail to pass, because the grader asks what was fixed, not under which condition.

With 5 runs per arm, the case passed `ask-first` in 5 of 5 runs with the skill and 0 of 5 without, and the skill fired in 5 of 5. The runs cost $1.95.

## 2026-10-14: fixes from an independent review, not measured yet

Two reviewers with no context from the session read the branch: one the skill as a prompt, one the eval method and the numbers. The numbers in the tables and the README matched the raw results. The fixes below change the skill and the graders, and no eval has run since, so the tables above describe the branch before them.

In the skill:

- Vale's parenthesis rule flagged "(to confirm)", and the skill asked to fix Vale's warnings, so a model could delete the mark it was told to add. The rule now skips "(to confirm)" and "(do potwierdzenia)", checked with `lint.sh` in both languages, and the skill says never to remove a mark to satisfy a warning.
- In a review comment, a reply or a chat message, an unverified claim is now asked as a question instead of marked, so marks do not land in short texts written in the user's voice.
- A recommendation already labelled as one, which `channels/long-docs.md` asks for, needs no mark; the Polish mark is fixed as "(do potwierdzenia)"; the example of a necessary deduction no longer relies on one transaction implying one database, which a two-phase commit breaks.
- A runbook has no Details and an ADR may end with them; the report lists the other documents the skill proposes; an ADR's Status may be deprecated, as in Nygard's post; and with a single named file the ADR holds the decision the user asked about.

In the graders:

- `no-unmarked-load` is removed from the ADR case: it could not be calibrated, and the format allows no weight of 0. Its calibration texts stay in `evals-calibration/`.
- `no-added-year` fails only an unmarked year after a day and a month, so "2000 jobs" and a marked year pass.
- `design-moved` in both runbook cases and `ops-moved` read only Claude's reply, so they now ask only whether the reply says where the material belongs; regex graders check the files. `write-runbook-pl`'s history regex now matches the Polish "Kafce".
- `write-runbook-split-en/order` was a regex on heading words and failed sentence headings; it is now an LLM grader like the Polish one.
- Every grader that reads a file now fails a missing or empty file.
- The PR claims graders get one failing calibration text each for cost and for production; until now one text with a table lock failed all three. These texts have not been judged yet.

A run of the touched cases would confirm these fixes: the two runbook cases, the ADR case, `write-pr-claims-en` and `write-review-comments-en`, 5 runs per arm, about $12, plus the PR calibration texts, about $2.

## 2026-10-14: the review fixes, measured

The six cases the review fixes touch ran with 5 runs per arm, and the PR claims graders were calibrated on five texts. The runs cost $14.02.

| Case | With skill | Without | With skill before the fixes |
|---|---|---|---|
| write-adr-one-decision-en | 98% | 60% | 93% |
| write-runbook-split-en | 90% | 70% | 90% |
| write-review-voice-en | 100% | 100% | 100% |
| write-review-comments-en | 100% | 45% | 95% |
| write-runbook-pl | 65% | 60% | 85% |
| write-pr-claims-en | 88% | 96% | 100% |

The review voice case now fails any comment with a claim mark such as "(to confirm)", and no run with the skill had one, so asking instead of marking holds in the user's voice.

The two drops come from graders, not from the skill:

- `write-runbook-pl` failed `no-history` in 5 of 5 runs in both arms, because the review's fix to its regex, `Kaf[kc]`, matched every mention of the Kafka queue. Each runbook with the skill says that a worker reads the webhooks from a Kafka queue, which describes the system as it is, not its history. Kafka is now out of the pattern; the history is still caught by "3.8", "Black Friday", "v2" and "deduplik".
- `write-pr-claims-en` failed `no-unmarked-cost` in 2 of 5 runs with the skill: one text names no cost at all, and the other says "If the build blocks writes to orders, new orders could be held up", a condition. Calibration showed the same grader failing a text about production run time. All three PR claims graders now look for one kind of sentence each, ignore conditions and questions, and pass when that sentence is absent. They have not been calibrated in this form yet.
