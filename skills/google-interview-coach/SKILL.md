---
name: google-interview-coach
description: Use when conducting a technical interview from questions in a Google Sheet and maintaining linked topic cheat-sheet sections in a Google Doc, including random or user-selected topics, adaptive questioning, answer analysis, and approved synchronization.
---

# Google Interview Coach

Use `google-drive:google-drive`, `google-drive:google-sheets`, and `google-drive:google-docs` for every resource operation. Before starting, read [the workflow contract](references/workflow-contract.md) completely; it is authoritative for discovery, interviewing, approval, writes, and recovery.

Before the state machine, apply one narrowly bounded preflight: only when the prompt explicitly says the Sheet is empty and asks for the next action, propose a minimal schema and await approval. After approval, begin normal `SETUP`. Otherwise, enter `SETUP` immediately.

Follow these states in order: `SETUP -> DISCOVER -> SELECT -> INTERVIEW -> EVALUATE -> PREVIEW -> APPROVE -> WRITE -> VERIFY`.

## State contracts

- **SETUP:** Reuse any supplied URLs, collect missing Sheet/Doc URLs and selection mode, validate access, and confirm edit access before a possible write. Ask “Українська чи English?” and wait for a choice before the first interview question.
- **DISCOVER:** Infer the Sheet and Doc conventions from their actual structures. Preserve headers, column order, formulas, validations, links, formatting, heading hierarchy, naming, and section-linking convention. Ask one focused clarification for ambiguity; propose an empty-Sheet schema and await approval.
- **SELECT:** Randomly select uniformly from eligible non-empty question rows, or exact/semantic-match a user topic. Resolve multiple matches with the user. Do not create a missing-topic row yet, and prevent duplicate Doc sections.
- **INTERVIEW:** Interview before generating any cheat sheet. Ask one open-ended prompt at a time, then realistic evidence-seeking follow-ups without leaking answers or showing/editing the cheat sheet.
- **EVALUATE:** Ground correct, partial, incorrect, practical, priority-gap, and related-topic findings in the candidate’s answers.
- **PREVIEW:** Show the target Sheet row action, Doc section action, outline, personalized emphasis, and section-link action.
- **APPROVE:** Wait for explicit confirmation after that concrete preview. No write occurs before `APPROVE`; revisions or earlier requests are not approval.
- **WRITE:** Re-read the target row and section, then update/create the non-duplicate Doc section, preserve/create its established section link, and mutate only the precise Sheet row fields.
- **VERIFY:** Re-read both resources, report verified results, and use the contract’s concurrent-edit and partial-failure recovery rules.

The cheat sheet is a complete, self-contained topic overview: concise for mastered material and deeper on evidenced gaps, with concepts, examples, warnings, related topics, personalized focus, and high-quality learning links for gaps.
