# Review comments on a pull request

Read this when the text is a review: comments on lines of a pull request and the summary that goes with them.

## The user's style comes first

If the user's instructions describe how they write review comments, as in a `## How I write` note, or the project's instructions set a review style, follow it: its length, its register, how a comment opens and ends, and what it never contains. When the two disagree, the project's style wins inside that project. The shape below is the default for everyone else. The rest of this file still applies: one problem per comment, only what the author must change or answer, and nice-to-haves kept out.

## The default shape

A comment holds one problem in at most three sentences: a label in the text's language, such as **Fix:** for a required change or **Question:** for something the author must answer, then what is wrong and why it matters, and the fix as a `suggestion` block when it is a code change. Comment only where the author must change or answer something. A nice-to-have, a future idea and your evidence stay in the report for the user. On a plan or a proposal, comment on its decisions, not on implementation detail.

The review summary has about three sentences: what is good, what must happen before merging, and a follow-up only if some work must happen after the merge. A nice-to-have is not such a follow-up.

A reply to a comment on the user's own pull request says what changed, or why nothing will, in one or two sentences. It does not thank the reviewer for the catch or explain the problem back to them.

## Point to code the author can find

Cite code by file and line, as in `importer/dates.py:27`. A bare `:279` next to the name of another file reads as a line of that file, so give the file every time the comment points somewhere new.

## The cold read

A comment is read next to the lines it is attached to, so the reader needs those lines too. Write one file with the summary first, then for each comment: the file and line, the quoted code lines it is attached to, and the comment. Add to the reader line that each comment is read next to its lines. The reader then checks every comment, not only the summary.
