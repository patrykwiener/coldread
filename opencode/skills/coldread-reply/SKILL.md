---
name: coldread-reply
description: Make sense of a message someone sent the user, then draft the user's reply - a comment on their pull request, a Slack or Teams message, an email, a ticket comment. Use when the user pastes or quotes such a message and asks what the sender means, what they want, or what to answer. Polish phrasings count the same, such as „o co mu chodzi", „co mam odpisać", „dostałem taką wiadomość", „odpisz mu".
argument-hint: "[the message, and what you need]"
---

# Read their message cold, then answer it

Here the user is the reader who was not in the session: someone wrote from inside their own work, and the user has to work out what they want. Do for the user what the cold reader does for a draft, then help with the answer.

What the user said: the text that came with the command that loaded this skill, if any.

## 1. Say what the sender asks

Open with one sentence: what the sender wants the user to do, decide or know, as in "Ania asks you to decide whether failed uploads stop retrying client errors in this pull request or in a separate ticket." If the message asks for nothing, say so: "Nothing to do: Ania only reports that the build passed."

## 2. Resolve the names

List every name in the message that the user may not know: labels, ticket numbers, internal names, abbreviations, and pointers such as "as discussed". The user's About me note, if they have one, tells you what they know already. Resolve each name from something you can check: the repository, the thread the user pasted, the pull request, or what anyone in the user's field knows. Name the source each time. A name you cannot resolve stays unresolved: say so, and say who or what would resolve it, such as "ask Ania" or "search the tracker for PAY-212". Never guess what a label stands for.

## 3. Name what the reply must settle

Say what the sender needs from the reply: a decision, a fact, an action or a confirmation. If the message can be read two ways, give both readings and what each one needs. When the reply needs a decision only the user can make, recommend the option you would pick and say why in one or two sentences, then draft the reply for that option, and give the other option's reply in one line. Ask the user before drafting only when you cannot recommend either option, such as when the choice turns on a fact only the user knows.

## 4. Draft the reply

Write the reply with the `coldread-write` skill, in the channel the message came from:

- The reader is the sender. Put into the reader line what the thread has already settled, so the reply does not repeat it.
- Reply in the language of the message, unless the user asks otherwise.
- When the user's instructions hold a note on how they write, such as a `## How I write` section, the reply follows it.
- The write skill's own limits apply, such as no cold read for a text under 40 words.

Never send or post the reply. Show it and stop: the user sends it.

## Output

Open with the sentence from step 1, with no heading or label before it. Then the names from step 2 and the point from step 3, then the draft and the write skill's report. Keep the first three short: the user wants the answer, not a lecture about the message.
