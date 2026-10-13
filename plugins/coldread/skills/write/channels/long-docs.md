# Long documents, sets of documents and decision documents

Read this when the text runs over about 1,500 words, when it is one of several documents that link to each other, or when it asks its readers to choose between options, such as an RFC or a proposal.

## The opening carries the budget

The budget covers the opening: what the document is for, what it asks of whom, and a reading path. A reading path says, for each kind of reader, which sections to read and in which order, as in "Approvers: sections 1 and 3. The team that builds it: section 4, then the test list." In a set, each document also says where it sits among the others and which one to read first. Otherwise readers ask the author in which order to read, and a document should answer that itself.

After the opening, a document with more than five sections gets a contents list.

## The body

- Keep paragraphs under about 120 words and table cells under about 40; `LongCell` flags longer cells. A table never replaces the explanation: say in a sentence before it what it shows and what follows from it.
- Link every reference to another part, such as "the decisions below", to that part.
- Do not count the document's own parts in the opening, as in "10 decisions": the number goes stale with the next edit. Name what the reader decides instead.
- Give every screen or page of an application its address or its menu path where it first appears.
- Keep each fact in one place. When two documents of a set state the same fact, keep it where it belongs and link to it from the other: for example, the decisions and their reasons in the RFC, and what is done and how in the plan.
- Keep the identifiers that others refer to: headings that other documents link to, decision numbers and test IDs. Rename a heading only together with every link to it.

## Decision documents

A document that asks its readers to choose suggests and leaves the choice to them. Give each decision:

- the question;
- the options, with what each gives, costs and risks;
- a recommendation, labelled as one, with its reason;
- the evidence that would change it.

Nothing reads as settled without a reason. Shortening tends to turn a recommendation into a statement of fact, such as "We use Postgres" for "We recommend Postgres, because the team runs it already". After every cut, check that each recommendation is still labelled and still has its reason.

## Rewriting a long document or a set

Copy every file you change to a temporary folder first. After the rewrite, run the facts check from step 4 with all documents of the set as new files: a value may move to another document, but it must not disappear. Run one cold read per document, and compare each reader's retelling with the points of that document.
