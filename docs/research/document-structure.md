# How coldread should decide, check and split document structure

The `write` skill should pick the document type before it picks sections, because Diátaxis and Google's writing course both tie structure to what the reader is trying to do (learn, do a task, look something up, understand), and ADR and design-doc authors add a fixed section order for deciding ([Diátaxis](https://diataxis.fr/compass/), [Google Tech Writing](https://developers.google.com/tech-writing/one/documents), [Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)). Today the brief records the reader, the Must and the points but not the type, no step plans more than one file, and the cold reader judges points rather than the outline, so nothing stops a runbook from absorbing design rationale. Material should go into a set of documents when it serves more than one type, more than one reader group, or more than one decision ([Diátaxis](https://diataxis.fr/map/), [GOV.UK](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/), [adr.github.io](https://adr.github.io/)). Structure can be checked cheaply: retell the document from its headings alone, outline it paragraph by paragraph and compare the outline with the brief, and ask readers to paraphrase each section ([GOV.UK](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/), [Miami University](https://miamioh.edu/howe-center/hwc/writing-resources/handouts/writing-process/reverse-outlining.html), [digital.gov](https://digital.gov/guides/plain-language/test/paraphrase-testing)). The Recommendations section turns this into four changes to `SKILL.md` and a sketch of a planning command.

## Document types and when to use each

Diátaxis, a documentation framework by Daniele Procida, sorts documentation by two questions: does the content serve action or cognition (doing versus understanding), and does it serve acquisition or application (learning versus working) ([compass](https://diataxis.fr/compass/)). The answers give four types:

- A **tutorial** is "an experience that takes place under the guidance of a tutor" and is "always learning-oriented"; its purpose "is not to help the user get something done, but to help them learn" ([tutorials](https://diataxis.fr/tutorials/)).
- A **how-to guide** gives "directions that guide the reader through a problem or towards a result" and is "goal-oriented". It contains "no digression, explanation, teaching", and links to reference instead of copying it. Its title names the task, as in "How to integrate application performance monitoring" ([how-to guides](https://diataxis.fr/how-to-guides/)).
- **Reference** is "technical descriptions of the machinery and how to operate it", and its structure "should mirror the structure of the product" ([reference](https://diataxis.fr/reference/)).
- **Explanation** is "a discursive treatment of a subject, that permits reflection". It "tends to absorb other things", such as instructions; you should be able to put "about" in front of each title ([explanation](https://diataxis.fr/explanation/)).

Diátaxis names the main failure: "When these distinctions are allowed to blur, the different kinds of documentation bleed into each other" ([map](https://diataxis.fr/map/)). It also warns against building the structure first: "do not create empty structures for tutorials/howto guides/reference/explanation with nothing in them" ([how to use Diátaxis](https://diataxis.fr/how-to-use-diataxis/)).

Engineering teams add decision documents and operational documents, which Diátaxis does not cover:

- An **ADR** (architecture decision record) in Michael Nygard's original post has Title, Context, Status, Decision and Consequences; "The whole document should be one or two pages long", because "Large documents are never kept up to date" ([Nygard, 2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)). The ADR GitHub organisation defines an ADR as a record that "captures a single AD and its rationale" ([adr.github.io](https://adr.github.io/)).
- A **design doc** at Google, as described by Malte Ubl, usually has context and scope, goals and non-goals, the design, alternatives considered, and cross-cutting concerns such as security and privacy. Ubl puts the sweet spot "around 10-20ish pages", says that beyond that "it might make sense to split up the problem into more manageable sub problems", and allows a "1-3 page 'mini design doc'". A doc that says "This is how we are going to implement it" without trade-offs is "really [an] implementation manual" and may not be needed ([Ubl](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- An **IETF RFC** has a fixed order: title, abstract, status, table of contents, body starting with an introduction, IANA and security considerations, references. The abstract must be "a concise and comprehensive overview of the purpose and contents of the entire document" ([RFC 7322](https://www.rfc-editor.org/rfc/rfc7322.html)). I found no primary source for a team RFC format.
- A **runbook**, which Google SRE calls a playbook, contains "high-level instructions on how to respond to automated alerts": the severity and impact of the alert, debugging suggestions and actions to mitigate and resolve it ([SRE workbook](https://sre.google/workbook/on-call/)). The SRE book reports that a playbook "produces roughly a 3x improvement in MTTR" (mean time to repair) compared with "winging it" ([SRE book](https://sre.google/sre-book/introduction/)).
- A **README**, in the Write the Docs guide, has project name and description, features, installation, contribute, support and licence ([Write the Docs](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)).

The table maps each type to what the reader needs and what usually goes wrong. "Typical failure" comes from the source where one is named, and from my inference where marked.

| Type | Reader's need | Sections in order | Typical failure |
|---|---|---|---|
| Tutorial | Learn by doing | Steps of one guided lesson | Turns into a how-to with no learning arc (inference) |
| How-to guide | Reach a goal now | Goal title, steps, links to reference | Explanation creeps in |
| Reference | Look up a fact | Mirrors the product's structure | Organised by the author's history (inference) |
| Explanation | Understand why | "About X" sections | Absorbs instructions |
| ADR | Know one decision and why | Title, Context, Decision, Status, Consequences | Grows past two pages or holds two decisions |
| Design doc | Agree on a design | Context, goals and non-goals, design, alternatives, cross-cutting | Implementation manual with no trade-offs |
| Runbook | Fix an alert under stress | Alert, severity and impact, diagnosis, mitigation, resolution | Out of date, or mixes design history in (inference) |
| README | Decide to use, then start | Description, example, install, contribute, support, licence | Long install detail instead of links (inference) |

## Deciding structure before drafting

Four techniques from the sources decide the structure before any sentence exists.

**Outline first, and review the draft against the outline.** Google's course recommends "a structured, high-level outline" to "group topics and determine where more detail is needed", and to "Limit each step of your outline to describing a concept or completing a specific task". After the first draft, "you can review it against your outline and introduction to make sure you haven't missed anything" ([Google, large docs](https://developers.google.com/tech-writing/two/large-docs)). Digital.gov suggests starting from the headings: "Start writing by developing the headings, structuring them to your audience's concerns. This approach can reveal major groupings of information" ([digital.gov, headings](https://digital.gov/guides/plain-language/design/headings)). coldread's Points list is already an outline of claims; it is not yet an outline of sections.

**Put the bottom line first.** BLUF (bottom line up front) comes from US Army Regulation 25-50, which requires "putting the main point at the beginning of the correspondence (bottom line up front)" and writing that is "understood by the reader in a single rapid reading" (AR 25-50, 10 October 2020, para 1-38; I read [a copy hosted by the State of Maine](https://www.maine.gov/dvem/policies/documents/AR%2025-50%20(10%20October%202020).pdf), not the Army Publishing Directorate original). The inverted pyramid, a news-writing order, says the same at every level: "The story should start with the main point. Each heading or subheading should be descriptive. The first sentence of every paragraph should be the most important" ([NN/g](https://www.nngroup.com/articles/inverted-pyramid/)). GOV.UK calls this frontloading and adds that content should then "taper down to smaller and smaller details" ([GOV.UK](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/)). coldread already applies this to the opening, but not to each section and each paragraph.

**Disclose progressively.** Progressive disclosure means showing what most readers need first and deferring the rest. NN/g defines it for interfaces and gives two rules: show upfront everything users frequently need, and keep the first level focused; designs with more than two levels "typically have low usability" ([NN/g](https://www.nngroup.com/articles/progressive-disclosure/)). For documents, Google recommends introducing "new terminology and concepts near the instructions that rely on them" and starting "with simple examples" ([Google, large docs](https://developers.google.com/tech-writing/two/large-docs)). My inference: coldread's main part plus Details is already two levels, so Details should not nest further.

**One purpose per document.** GOV.UK says "Before you start writing, identify a user need. Publish only what's needed to meet that user need and nothing more" ([GOV.UK, user needs](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/meet-user-needs/)), and "if there are different needs for each user group, they would each need their own user need" ([GOV.UK, identify user needs](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/)). Information Mapping, a structured-writing method by Robert Horn "in use in industry since 1972", gives each unit of information a label as "an advance organizer" for the reader ([Information Mapping](https://informationmapping.com/blogs/news/fun-facts-about-information-mapping)). Secondary sources say the method sorts content into six information types (procedure, process, concept, structure, principle, fact), but the official page cited here does not list them, and the official support page that does returned 403, so treat the six types as unverified. Digital.gov puts the same rule at section level: "Limit each paragraph or section to one topic" ([digital.gov, clear and short](https://digital.gov/guides/plain-language/writing/clear-short)). Google adds that the introduction states what the document covers, what it expects readers to know, and what it does not cover ([Google, large docs](https://developers.google.com/tech-writing/two/large-docs)).

## Splitting material into a set of documents

Information architecture, here meaning how content is divided into documents and linked, has one primary rule across the sources: one place per need and per fact. Write the Docs lists "Eliminate content overlap between separate sources" (Unique), "Content should be ordered to cover prerequisite concepts first" (Cumulative), "Within each publication, cover concepts in full, or not at all" (Complete), and "Provide addresses to readers that link directly to content at a granular level" (Addressable) ([Write the Docs, principles](https://www.writethedocs.org/guide/writing/docs-principles/)). Diátaxis adds that, without a clear architecture, writers "often try to structure their work around features of a product" ([map](https://diataxis.fr/map/)).

What goes where then follows from type. A runbook links to the design doc for "why", and the design doc links to ADRs for each decision, because a how-to guide must not explain ([how-to guides](https://diataxis.fr/how-to-guides/)) and an ADR holds one decision ([adr.github.io](https://adr.github.io/)).

Six signals, each tied to its source, say a document should split:

1. **It serves two Diátaxis types.** The compass gives two different answers for different parts of the text ([compass](https://diataxis.fr/compass/)).
2. **It serves two reader groups with different needs.** Each group needs its own user need ([GOV.UK](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/)).
3. **It records more than one decision.** One ADR per decision ([adr.github.io](https://adr.github.io/)).
4. **It exceeds the type's length.** Over two pages for an ADR ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)), or well over about 20 pages for a design doc ([Ubl](https://www.industrialempathy.com/posts/design-docs-at-google/)).
5. **Its readers are new to the subject.** Google says how-to guides, overviews and conceptual guides "often work better as shorter documents" for newcomers, while reference pages and in-depth tutorials can be longer ([Google, large docs](https://developers.google.com/tech-writing/two/large-docs)).
6. **It has more than about four new chunks at one level.** Information Mapping's blog states that "readers can best retain no more than five to nine pieces of information in short-term memory", but gives no source for it ([Information Mapping](https://informationmapping.com/blogs/news/fun-facts-about-information-mapping)); the number goes back to Miller (1956). Cowan's review of that research says Miller's seven "was meant more as a rough estimate and a rhetorical device than as a real capacity limit" and finds "a single, central capacity limit averaging about four chunks" ([Cowan, 2001](https://pubmed.ncbi.nlm.nih.gov/11515286/)). So coldread's four-point limit has a primary source, but it is about short-term memory in lab tasks, not about documents: using it for the number of points or sections is an inference.

## Validating structure

Three checks from the sources test structure rather than sentences.

**The headings-only test.** NN/g describes the layer-cake pattern, where readers fix "mostly on the page's headings and subheadings", and calls it the most effective way to scan apart from reading every word; it works when each heading is "descriptive of all topics in the section, and only topics in the section" ([NN/g, 2019](https://www.nngroup.com/articles/layer-cake-pattern-scanning/)). NN/g also advises that "if users see only the first 2 words, they should still get the gist" ([NN/g, F-pattern](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)). Microsoft says to "Think of headings as an outline" and to skip second-level headings when a section has fewer than two distinct topics ([Microsoft](https://learn.microsoft.com/en-us/style-guide/scannable-content/headings)); Google says "Don't skip levels of the heading hierarchy" ([Google style](https://developers.google.com/style/headings)). GOV.UK adds the reverse check: headings should be "removable – the content should still make sense with the headings removed", and should not be generic, such as "Introduction" ([GOV.UK](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/)). The stakes are measured: in NN/g's 1997 study, "79 percent of our test users always scanned any new page", and a scannable version of a site scored 47% better usability ([NN/g, 1997](https://www.nngroup.com/articles/how-users-read-on-the-web/)); a 2008 log study found that users read "about 20% of the text on the average page" ([NN/g, 2008](https://www.nngroup.com/articles/how-little-do-users-read/)).

**The reverse outline.** A reverse outline is an outline built from a finished draft, by writing down the main point of each paragraph. Miami University's Howe Writing Center pulls "the first and last sentences of each body paragraph" into "a skeletal version of your paper", then checks whether each one works toward the thesis and whether the order holds ([Miami University](https://miamioh.edu/howe-center/hwc/writing-resources/handouts/writing-process/reverse-outlining.html)). Google's advice to review the draft "against your outline and introduction" is the same check from the other side ([Google, large docs](https://developers.google.com/tech-writing/two/large-docs)).

**Paraphrase per section.** Digital.gov's paraphrase test asks readers, "Each time the participant reaches the end of a section", to say "in their own words what that section means"; wherever they misunderstood, "the content has a problem" ([digital.gov](https://digital.gov/guides/plain-language/test/paraphrase-testing)). coldread's cold reader retells the whole text once; the source does it section by section.

The following ways to automate these checks are my inference; no source above describes an LLM or a script doing them.

- **Headings-only retelling.** A script extracts every heading line and the first sentence under each, as in `grep -nE '^#{1,6} ' file.md` plus the next non-empty line. A fresh subagent gets only that skeleton and the reader line, and retells the argument and the ask. The skill then compares that retelling with the Must and the Points, just as step 6 does for the full text. A miss means the headings do not carry the argument.
- **Type-mixing detection.** The same subagent, or the cold reader in an extra section, labels each section with one Diátaxis type or a decision type, using the compass questions. Two labels in one document, or a label that differs from the type in the brief, flag a split or a move. Cheap regex hints can precede it: numbered imperative steps (`^\d+\. [A-Z][a-z]+ `) in a text typed as explanation or design doc, or "because", "we chose", "alternatively" inside a runbook's step list.
- **Heading-to-content match.** For each section, a reader gets the body without its heading and writes a heading; the script compares it with the real one. This tests NN/g's "all topics in the section, and only topics in the section". A Vale rule can flag generic headings such as `Overview`, `Introduction`, `Background`, `Misc` and `Notes`, which GOV.UK names as unhelpful.
- **Order check.** For a typed document, a regex asserts the required sections appear in the required order, like the existing `section-order.md` grader does for a PR template.

## Measuring it in evals

coldread's evals are folders with a `prompt.md` (frontmatter plus the user's request) and `graders/*.md`, each of type `regex` on a saved file, `llm` with a PASS and FAIL rule, or `tool_used` to check the skill fired; for example `write-pr-template-en/graders/section-order.md` asserts heading order with one multiline regex. Three cases would cover type, split and headings.

### `write-runbook-split-en`: the skill keeps design rationale out of a runbook

Prompt: "Write the on-call doc for the export queue backlog alert and save it to runbook.md. Reader: an on-call backend engineer paged at night." The notes mix the alert threshold, four mitigation steps, the history of why the queue moved from Redis to Postgres, and two open design questions.

- `skill-fired.md`: `tool_used`, as in the existing cases.
- `order.md`: `regex`, `match: contains`, pattern `'^## .*(?:[Ss]everity|[Ii]mpact)[\s\S]*^## .*(?:[Mm]itigat|[Ff]ix|[Rr]esolv)'` with `flags: m`.
- `no-history.md`: `regex`, `match: not_contains` on runbook.md, pattern `'Redis'`, because the migration story belongs elsewhere.
- `split-offered.md`: `llm` on the transcript: PASS if Claude's report proposes moving the migration history and the open questions to a design doc or ADR, or wrote them to a second file; FAIL if they are in runbook.md or silently dropped.

### `write-headings-carry-en`: a design doc's headings alone tell the argument

Prompt: a design doc for adding a per-tenant rate limit, saved to design.md, with notes giving the decision, two rejected options and one approval needed.

- `no-generic-headings.md`: `regex`, `match: not_contains`, pattern `'^#{2,3} (?:Overview|Introduction|Background|Details?|Misc|Notes|Summary)\s*$'`, `flags: m`. Details stays allowed if the case wants it; drop it from the pattern then.
- `headings-retell.md`: `llm`. The grader text tells the model to read only the lines that start with `#`: PASS if from those alone it can state the chosen limit design, that two options were rejected, and what needs approval; FAIL otherwise.
- `design-sections.md`: `regex`, `match: contains`, checks that goals or non-goals appear before alternatives, following Ubl's order.

### `write-adr-one-decision-en`: two decisions become two ADRs

Prompt: "Write an ADR for these decisions and save it in doc/adr/", with notes holding two independent decisions, such as the queue backend and the retry policy.

- `two-files.md`: `llm` on the transcript, or a `regex` on a file listing if the runner exposes one: PASS if Claude wrote two ADR files or proposed two before writing; FAIL if one file records both decisions.
- `nygard-order.md`: `regex`, `match: contains`, pattern `'^#+ .*Context[\s\S]*^#+ .*Decision[\s\S]*^#+ .*Consequences'`, `flags: m`, on the first ADR file. This needs a fixed file name in the prompt, such as `doc/adr/0007-queue-backend.md`.
- `status-present.md`: `regex` for `'(?im)^#+ *Status|^Status:'`.

## Recommendations

Each recommendation lists the sources it rests on, then separates what the sources say from what I infer.

1. **Add a `Type` line to the brief in step 1**, before Points: one of tutorial, how-to, reference, explanation, ADR, design doc, runbook, README, or a channel type such as PR description. Each non-channel type names its required sections and order, from the table above, in a new `channels/doc-types.md`. A repository template still wins. *Sources:* [Diátaxis compass](https://diataxis.fr/compass/), [Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), [Ubl](https://www.industrialempathy.com/posts/design-docs-at-google/), [SRE workbook](https://sre.google/workbook/on-call/), [Write the Docs](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/). *Sources say:* types have distinct needs and section sets. *Inference:* making the type an explicit brief line is what stops the drift.
2. **Add an `Outline` line to the brief:** the planned headings, each a statement, in order, with the point it carries. Show it to the user with the brief. *Sources:* [Google, large docs](https://developers.google.com/tech-writing/two/large-docs), [digital.gov, headings](https://digital.gov/guides/plain-language/design/headings). *Sources say:* outline first, develop headings first, review the draft against the outline. *Inference:* for texts under about 200 words, such as Slack messages, the outline adds nothing and should be skipped.
3. **Replace "more than four points → propose a split" with the six split signals** in section 4, and say in the proposal which signal fired and what the second document would be. *Sources:* as listed per signal. *Sources say:* each signal on its own. *Inference:* combining them into one rule, and applying Cowan's limit of about four chunks to points and sections.
4. **Add a structure check to step 6, before the full cold read:** run the headings-only retelling on the extracted skeleton, compare it with the Outline and the Must, and ask the cold reader to label each section's type in a new section of its report. Fix a mismatch like a blocker. *Sources:* [NN/g layer cake](https://www.nngroup.com/articles/layer-cake-pattern-scanning/), [GOV.UK clear structure](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/), [Miami University](https://miamioh.edu/howe-center/hwc/writing-resources/handouts/writing-process/reverse-outlining.html), [digital.gov paraphrase testing](https://digital.gov/guides/plain-language/test/paraphrase-testing). *Sources say:* readers scan headings, headings must match their sections, outline and paraphrase checks find structural faults. *Inference:* that an LLM reader on a skeleton is a fair stand-in for a human scanner; the evals in section 6 would test that.

**A sketch of a doc-set planning command**, `/coldread:plan-docs`, which is inference built on the sources above. It takes the user's notes and the intended readers, and writes no prose. It outputs:

1. one row per reader group and its need, in GOV.UK's "As a… I need to… So that…" form ([GOV.UK](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/));
2. one row per proposed file: path, type, reader, Must, outline, and which notes go there;
3. a fact map that assigns each number and decision in the notes to exactly one file, which `facts.sh` can later check across the set ([Write the Docs, Unique](https://www.writethedocs.org/guide/writing/docs-principles/));
4. the reading path that `long-docs.md` already asks for.

The user approves the plan, and then `write` runs once per file with that file's row as its brief. Diátaxis's warning against empty structures suggests the plan should list only files that already have content in the notes ([how to use Diátaxis](https://diataxis.fr/how-to-use-diataxis/)).

## Verification

On 2026-10-13 a second pass re-read 42 quoted sentences against their pages: Diátaxis (compass, map, how-to guides), Nygard, adr.github.io, Ubl, GOV.UK (two pages), Google Technical Writing Two, NN/g (layer cake, 1997, 2008, progressive disclosure), Microsoft headings, Write the Docs principles, digital.gov paraphrase testing, Miami University, the SRE book and AR 25-50. All matched word for word except Information Mapping, corrected above: its page does not list the six types and gives no source for "five to nine".

## Sources

All accessed 2026-10-13.

- Diátaxis, home: https://diataxis.fr/
- Diátaxis, compass: https://diataxis.fr/compass/
- Diátaxis, tutorials: https://diataxis.fr/tutorials/
- Diátaxis, how-to guides: https://diataxis.fr/how-to-guides/
- Diátaxis, reference: https://diataxis.fr/reference/
- Diátaxis, explanation: https://diataxis.fr/explanation/
- Diátaxis, map: https://diataxis.fr/map/
- Diátaxis, how to use Diátaxis: https://diataxis.fr/how-to-use-diataxis/
- Google Technical Writing One, documents: https://developers.google.com/tech-writing/one/documents
- Google Technical Writing Two, organizing large documents: https://developers.google.com/tech-writing/two/large-docs
- Google developer documentation style guide, headings: https://developers.google.com/style/headings
- Microsoft Writing Style Guide, scannable content: https://learn.microsoft.com/en-us/style-guide/scannable-content/
- Microsoft Writing Style Guide, headings: https://learn.microsoft.com/en-us/style-guide/scannable-content/headings
- NN/g, F-shaped pattern: https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/
- NN/g, layer-cake pattern: https://www.nngroup.com/articles/layer-cake-pattern-scanning/
- NN/g, inverted pyramid: https://www.nngroup.com/articles/inverted-pyramid/
- NN/g, progressive disclosure: https://www.nngroup.com/articles/progressive-disclosure/
- NN/g, how users read on the web (1997): https://www.nngroup.com/articles/how-users-read-on-the-web/
- NN/g, how little do users read (2008): https://www.nngroup.com/articles/how-little-do-users-read/
- digital.gov, plain language principles: https://digital.gov/guides/plain-language/principles
- digital.gov, headings: https://digital.gov/guides/plain-language/design/headings
- digital.gov, clear and short: https://digital.gov/guides/plain-language/writing/clear-short
- digital.gov, paraphrase testing: https://digital.gov/guides/plain-language/test/paraphrase-testing
- GOV.UK, create a clear structure: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/
- GOV.UK, meet user needs: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/meet-user-needs/
- GOV.UK, identify user needs: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/
- Write the Docs, beginner's guide: https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/
- Write the Docs, documentation principles: https://www.writethedocs.org/guide/writing/docs-principles/
- Information Mapping International, fun facts (blog post, 9 November 2020): https://informationmapping.com/blogs/news/fun-facts-about-information-mapping
- Nelson Cowan, "The magical number 4 in short-term memory", Behavioral and Brain Sciences 24(1), 2001, abstract on PubMed: https://pubmed.ncbi.nlm.nih.gov/11515286/
- Michael Nygard, Documenting Architecture Decisions (2011): https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- ADR GitHub organisation: https://adr.github.io/
- Malte Ubl, Design Docs at Google: https://www.industrialempathy.com/posts/design-docs-at-google/
- RFC 7322, RFC Style Guide: https://www.rfc-editor.org/rfc/rfc7322.html
- Google SRE book, introduction: https://sre.google/sre-book/introduction/
- Google SRE workbook, on-call: https://sre.google/workbook/on-call/
- AR 25-50, Preparing and Managing Correspondence, 10 October 2020 (copy hosted by the State of Maine): https://www.maine.gov/dvem/policies/documents/AR%2025-50%20(10%20October%202020).pdf
- Miami University Howe Writing Center, reverse outlining: https://miamioh.edu/howe-center/hwc/writing-resources/handouts/writing-process/reverse-outlining.html

### Tried but not verified

- **Diátaxis "complex hierarchies" page** (`https://diataxis.fr/complex-hierarchies/`): returns 404, and no current page on the site covers landing pages or two-dimensional hierarchies, so this document makes no claim about them.
- **AR 25-50 on armypubs.army.mil**: I did not reach the Army Publishing Directorate original; the quotes come from the State of Maine copy listed above, and match its paragraph 1–38 a and b word for word.
- **plainlanguage.gov "Organize" guidelines**: the URL redirects to digital.gov, whose current pages I used instead; the archived original was not checked.
- **GOV.UK "organise and group content"** page: linked from the planning page but returned no readable content.
- **Google SRE book, "Being On-Call" chapter**: contains no playbook guidance; the playbook claims come from the introduction and the workbook instead.
- **Information Mapping's six information types and its principles**: the official blog post names chunking, labelling, consistency and integrated graphics, but not the six types; the official support page that lists the types returned 403. The six types appear here only as unverified.
