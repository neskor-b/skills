# Workflow Contract

## Session Setup

Reuse URLs already in the conversation; otherwise request the Google Sheet URL, Google Doc URL, and selection mode (uniform random or user-selected topic/question). Validate both URLs, file types, and read access. Ask “Українська чи English?” and wait for the candidate’s selection before the first interview question. For an explicitly known empty Sheet, first propose the schema and wait for its approval; complete language setup before interviewing. Before a final write, verify edit access; read-only access permits interview and preview only.

## Schema and Document Discovery

Read headers, representative populated rows, formatting, formulas, validations, links, and inactive/archive signals to infer the Sheet schema. Preserve every observed convention. Inspect Doc heading hierarchy, section naming/formatting, and section-linking practice. If the Sheet is empty, propose a minimal approved schema (at least question and section-link fields) and wait. If targets or columns are ambiguous, ask one focused clarification; never guess.

## Question Resolution

In random mode, select uniformly from eligible non-empty question rows, excluding headers, helper rows, and inferred inactive records. In user-selected mode, find an exact or clear semantic match; present concise candidates for multiple plausible matches. For no match, interview first and defer a new row until the approved preview. Check existing links and Doc titles to prevent duplicate sections.

## Adaptive Interview

Ask one prompt at a time, beginning open-ended. Follow up realistically on definitions, mechanisms, trade-offs, edge cases, and practical application; request examples or code when useful. Continue until evidence covers important parts (often five to eight substantive prompts, never a fixed quota). Surface contradictions as questions, do not leak answers, and do not expose or edit the cheat sheet during the interview.

## Evidence-Based Evaluation

Tie the evaluation to the actual answers: correct points, partial explanations, incorrect claims or omissions, practical application, highest-priority gaps, and related topics. Distinguish factual mistakes, terminology issues, missing depth, and incomplete explanations.

## Complete Gap-Weighted Cheat Sheet

Keep a complete, self-contained overview of the whole topic—not merely a mistake list. Retain useful existing content; correct stale or inaccurate material. Cover mastered areas concisely, and expand evidenced gaps with mechanisms, examples or code, warnings, and a prominent personalized focus section. Include definition, core concepts/rules, nuances and trade-offs, common mistakes, related topics, and high-quality learning links for evidenced gaps.

## Preview Contract

Before any mutation, show: the target question and exact Sheet row action; the Doc section title and create/update action; the proposed outline; personalized emphasis; and the specific section-link action. Wait for explicit confirmation. A request to revise the preview, or a previous general request to update, is not approval.

## Approved Write

After approval, re-read the target Sheet row and Doc section. Update the exact existing section or create one using the current heading hierarchy, naming, formatting, and link convention; verify it is not a duplicate. Obtain or preserve a section-specific link, then mutate only the intended Sheet fields or add the deferred new row according to the inferred schema.

## Verification and Recovery

Re-read both resources after writing and report what was verified. If concurrent edits change the proposed outcome, rebase and show a revised preview. On partial failure, state which mutation succeeded, do not duplicate content or rows, and offer a safe retry/completion step. Stop with a precise correction for invalid URLs, inaccessible files, wrong types, or no edit access.

## Common Mistakes

Do not write early; produce generic summaries; create duplicate rows or sections; guess a schema or target; overwrite unrelated content; change conventions silently; or claim success without post-write reads.

## Compact Example

Opening: “Українська чи English?” After the choice: “Please share the Sheet and Doc links, then choose random selection or a topic.” Once discovery succeeds: “Explain how dependency injection improves testability.” Follow-ups probe lifecycle, trade-offs, and a production example without supplying answers.

Preview shape:

```text
Sheet: row 12 — update assessment fields; preserve existing link format.
Doc: “Dependency Injection” — update existing section.
Outline: core idea; mechanisms; trade-offs; example; common pitfalls; focus plan; learning links.
Personalization: expand lifecycle and test-double gaps; keep fundamentals concise.
Link: preserve row 12’s section-specific link.
Write these changes? (explicit confirmation required)
```
