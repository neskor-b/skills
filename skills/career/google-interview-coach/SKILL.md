---
name: google-interview-coach
description: Use when conducting a technical interview from questions in a Google Sheet and maintaining linked topic cheat-sheet sections in a Google Doc, including random or user-selected topics, adaptive questioning, answer analysis, and approved synchronization.
---

# Google Interview Coach

Before starting, read [the workflow contract](references/workflow-contract.md) completely; it is authoritative for discovery, interviewing, approval, writes, verification, and recovery. Route operations by resource: use `google-drive:google-drive` to locate files and inspect Drive metadata or permissions, `google-drive:google-sheets` for Sheet structure and cell reads/writes, and `google-drive:google-docs` for Doc structure and section reads/writes.

Before the state machine, apply one narrowly bounded preflight: only when the prompt explicitly says the Sheet is empty and asks for the next action, propose a minimal schema and await approval. Carry an approved preflight schema into `DISCOVER`; do not propose or approve it again. After approval, begin normal `SETUP`. Otherwise, enter `SETUP` immediately.

Follow these states in order: `SETUP -> DISCOVER -> SELECT -> INTERVIEW -> EVALUATE -> PREVIEW -> APPROVE -> WRITE -> VERIFY`.

## State contracts

- **SETUP:** Reuse any supplied URLs, collect missing Sheet/Doc URLs and selection mode, validate file types and read access, and separately record edit capability. A read failure is fatal; missing edit access blocks only mutation, not discovery, interview, evaluation, or preview. Ask “Українська чи English?” and wait for a choice before the first interview question.
- **DISCOVER:** Infer the Sheet and Doc conventions from their actual structures. Preserve headers, column order, formulas, validations, links, formatting, heading hierarchy, naming, and section-linking convention. Ask one focused clarification for ambiguity. For an empty Sheet, reuse an approved preflight schema or propose a schema once and await approval.
- **SELECT:** Randomly select uniformly from eligible non-empty question rows, or exact/semantic-match a user topic. Resolve multiple matches with the user. Do not create a missing-topic row yet, and prevent duplicate Doc sections.
- **INTERVIEW:** Interview before generating any cheat sheet. Ask one open-ended prompt at a time, then realistic evidence-seeking follow-ups without leaking answers or showing/editing the cheat sheet.
- **EVALUATE:** Ground correct, partial, incorrect, practical, priority-gap, and related-topic findings in the candidate’s answers.
- **PREVIEW:** Capture bounded pre-write preservation witnesses for the target Sheet/Doc scope. Show the target Sheet row action, Doc section action, outline, personalized emphasis, and section-link action.
- **APPROVE:** Wait for explicit confirmation after that concrete preview. No write occurs before `APPROVE`; a revision request returns to a revised preview, while a decline cancels the pending write. Neither is approval. Without edit access, stop only before mutation, disclose the read-only state, and request access.
- **WRITE:** Re-read the target row and section against the approved preview. Any material concurrent change aborts `WRITE`, invalidates the stale approval, and returns to a revised `PREVIEW` for fresh explicit approval. Otherwise update/create the non-duplicate Doc section, preserve/create its established section link, and mutate only the precise Sheet row fields.
- **VERIFY:** Re-read the exact row and Doc section, resolve the Sheet’s section-specific link, and prove it targets the exact created/updated section. Compare preservation witnesses to prove unrelated Sheet and Doc data remained unchanged; never infer success from mutation responses alone. Use the contract’s partial-failure recovery rules.

The cheat sheet is a complete, self-contained topic overview: concise for mastered material and deeper on evidenced gaps, with concepts, examples, warnings, related topics, personalized focus, and high-quality learning links for gaps.
