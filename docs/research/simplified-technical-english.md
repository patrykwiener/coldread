# What coldread takes from ASD-STE100, and what it leaves out

coldread takes one rule from ASD-STE100 practice. A rewrite keeps the strength of every claim and instruction, also when the user asks for Simplified Technical English. It leaves out the rest of the standard that a software text could use: its dictionary, its tense rule, its word limits and its rules for procedures. The reason is a measurement. Both versions of coldread were asked to rewrite six texts "in ASD-STE100", twice each. Model labellers who did not know which version wrote which text found that main kept every qualifier in 2 of 12 rewrites, and the version with the rule in 10 of 12. The parts left out either changed what texts say or found nothing to fix ([results, 2026-11-11](../results.md)).

A qualifier here is a word or clause that sets the strength or scope of a claim, such as "should", "only if", "likely" or "because".

## ASD-STE100 was built for maintenance procedures

ASD-STE100, Simplified Technical English (STE), is a controlled English that the European aerospace industry wrote for maintenance manuals, many of whose readers do not have English as their first language. The Aerospace, Security and Defence Industries Association of Europe (ASD) maintains it. Issue 9, of January 2025, has 53 writing rules in 9 sections and a dictionary of about 900 approved words, each with one meaning and one part of speech. A project adds its own technical nouns and verbs ([ASD-STE100](https://www.asd-ste100.org/)).

The rules that a software text could use are these:

- At most 20 words in a sentence of a procedure, and 25 in a description.
- One instruction per sentence, and the condition before the command.
- At most three nouns in a row.
- The active voice, the simple tenses only, and no phrasal verbs or semicolons.
- At most six sentences in a paragraph.

The dictionary does not approve "should", and its first replacement is "must". It does not approve "may" either, and offers "can" or "possibly". So "Personnel should wear protective clothing" becomes "Personnel must use protective clothing" (ASD-STE100 Issue 9, Part 2).

What is known about its effect:

- Two studies of aircraft maintenance procedures found that readers understood the STE versions better, mostly for complex procedures and for readers whose first language is not English. Reading time did not change ([Shubert et al., 1995](https://doi.org/10.2190/WG69-D74B-4DLL-2WBK) and [Chervak, Drury and Ouellette, 1996](https://doi.org/10.1177/154193129604000502)). Neither study tested prose such as a PR description.
- Phrasal verbs are hard for readers whose first language is not English, "even very advanced learners" (Thrush, 2001, Technical Communication 48).
- For text written by a model, one informal test asked Claude to explain code and counted 48 facts listed beforehand. Claude kept 47 of them with no style instruction, 43 when asked for "Simple Technical English" and 25 when asked for "ASD-STE100" ([Ghinda, 2026](https://allaboutcoding.ghinda.com/explain-to-me-in-simple-technical-english)).

I found no study of whether agents read prompts in STE better.

## A request for ASD-STE100 changes what a text says

In the baseline, the request changed meaning with each of the three tools tested: plain Claude, the asd-ste100 skill and coldread on main. It changed meaning most often with plain Claude and with coldread on main. "Ask finance whether duplicates already paid should be refunded or credited" became "must we give a refund or a credit?", and "the script stops and suggests `--no-pull`" became "tells you to use `--no-pull`". The [asd-ste100 skill](https://github.com/danyuchn/asd-ste100-skill) kept every qualifier in 9 of 12 rewrites. Its instructions say to keep modality, as in "may have failed" stays "may have failed".

coldread already asked rewrites to change how a text says things, not what it says, but nothing in the skill named the strength of a word. The new paragraph in step 2 of `SKILL.md` names it. It gives the pairs that go wrong, such as "should" and "must" or "suggests" and "tells you to". It keeps conditions, limits and reasons in place. It also tells the skill to follow a requested style's sentence rules, but to keep the original word where the style's word list would change a strength. With it, coldread went from 2 to 10 of 12 rewrites. On two held-out texts, which each version rewrote twice in the same run, it went from 0 to 3 of 4. The skill's description now names the style too, so a request for it reaches the skill. In the last run it started on 12 of 12 such requests, while the old description had started it on 23 of 28 over the two runs before. The case `write-rewrite-ste-en` keeps the rule in the write suite: with the skill, none of 5 rewrites of its note turned "should" into "must", and without it, 4 of 5 did.

## What coldread leaves out, and why

- **The dictionary and the tense rule.** They are what changed meaning in the baseline. The tense rule also removes "has shipped", which says that something is live now, where "shipped" does not.
- **Hard word limits.** The skill aims at about 20 words a sentence and Vale warns above 35. Rewrites that split "X, because Y" into two sentences often dropped "because", so the reason no longer read as the reason.
- **A script that counts qualifiers before and after a rewrite.** Of its 27 alarms, 6 were real. Of the 76 rewrites in the baseline, 35 changed meaning, and it caught 6 of them. Most changes swap words it does not count.
- **The asd-ste100 skill inside coldread.** It returns "the rewritten text, and nothing else", while coldread reports every fact it removed or added. Its linter, 2,688 lines of Python, parses Markdown itself, where coldread uses Vale. With both skills in one plugin, it took 4 of 6 STE requests even after write's description named the style, and none of 6 other requests.
- **STE's rules for procedures.** Four runbooks from coldread on main broke none of them. Two prompts for a new session, from the case `write-prompt-handoff-en`, had seven small breaks. In my reading, none of them could make an agent act out of order. Both conditions that came after their command followed a step that already stops and asks. The other breaks put two actions into one step or pointed to a warning further down.
- **Rules for readers whose first language is not English,** such as no figurative phrasal verbs and one meaning per word. They are not tested yet. A model judge cannot tell what such a reader finds hard, so they need a reading test with people from that group.

## Sources

- ASD-STE100 Simplified Technical English, Issue 9, 2025, <https://www.asd-ste100.org/>
- Shubert, S. K., Spyridakis, J. H., Holmback, H. K., and Coney, M. B. (1995). The comprehensibility of Simplified English in procedures. Journal of Technical Writing and Communication 25(4). <https://doi.org/10.2190/WG69-D74B-4DLL-2WBK>
- Chervak, S., Drury, C. G., and Ouellette, J. P. (1996). Simplified English for aircraft workcards. Proceedings of the Human Factors and Ergonomics Society Annual Meeting 40(5), 303–307. <https://doi.org/10.1177/154193129604000502>
- Thrush, E. A. (2001). Plain English? A study of plain English vocabulary and international audiences. Technical Communication 48, 289–296.
- Ghinda, L. (2026). Explain to me in Simple Technical English. <https://allaboutcoding.ghinda.com/explain-to-me-in-simple-technical-english>, data in <https://github.com/lucianghinda/llm-experiments>
- danyuchn/asd-ste100-skill: <https://github.com/danyuchn/asd-ste100-skill>
