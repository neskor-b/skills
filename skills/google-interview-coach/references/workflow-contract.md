# Workflow Contract

## Narrow Empty-Sheet Preflight

Only when the prompt explicitly says the Sheet is empty and asks for the next action, propose a minimal schema (at least question and section-link fields) and wait for approval before entering the state machine. Record the approved schema as session state, begin normal `SETUP`, and carry that schema into `DISCOVER`; do not request a second schema approval. An empty Sheet first discovered during normal `DISCOVER` still requires one proposal and explicit approval.

## Session Setup

Reuse URLs already in the conversation; otherwise request the Google Sheet URL, Google Doc URL, and selection mode (uniform random or user-selected topic/question). Use Drive operations to locate files and inspect metadata or permissions, Sheet operations for spreadsheet structure and cells, and Doc operations for document structure and sections. Validate both URLs, file types, and read access. A wrong type, inaccessible file, or failed read stops the workflow with the exact correction needed. Record edit capability separately: read-only access still permits discovery, selection, the full interview, evaluation, cheat-sheet preparation, and preview; it blocks only mutations. Ask “Українська чи English?” and wait for the candidate’s selection before the first interview question.

## Schema and Document Discovery

Read headers, representative populated rows, formatting, formulas, validations, links, and inactive/archive signals to infer the Sheet schema. Preserve every observed convention. Inspect Doc heading hierarchy, section naming/formatting, and section-linking practice. If the Sheet is empty, use the schema already approved in preflight; otherwise propose a minimal schema (at least question and section-link fields) once and wait for approval. If targets or columns are ambiguous, ask one focused clarification; never guess.

## Question Resolution

In random mode, select uniformly from eligible non-empty question rows, excluding headers, helper rows, and inferred inactive records. In user-selected mode, find an exact or clear semantic match; present concise candidates for multiple plausible matches. For no match, interview first and defer a new row until the approved preview. Check existing links and Doc titles to prevent duplicate sections.

## Adaptive Interview

Ask one prompt at a time, beginning open-ended. Follow up realistically on definitions, mechanisms, trade-offs, edge cases, and practical application; request examples or code when useful. Continue until evidence covers important parts (often five to eight substantive prompts, never a fixed quota). Surface contradictions as questions, do not leak answers, and do not expose or edit the cheat sheet during the interview.

## Evidence-Based Evaluation

Tie the evaluation to the actual answers: correct points, partial explanations, incorrect claims or omissions, practical application, highest-priority gaps, and related topics. Distinguish factual mistakes, terminology issues, missing depth, and incomplete explanations.

## Complete Gap-Weighted Cheat Sheet

Keep a complete, self-contained overview of the whole topic—not merely a mistake list. Retain useful existing content; correct stale or inaccurate material. Cover mastered areas concisely, and expand evidenced gaps with mechanisms, examples or code, warnings, and a prominent personalized focus section. Include definition, core concepts/rules, nuances and trade-offs, common mistakes, related topics, and high-quality learning links for evidenced gaps.

## Preview Contract

Before showing the preview, capture bounded preservation witnesses for the exact planned mutation scope: target and neighboring Sheet values plus relevant formulas, validations, formatting, and row identities; and the target Doc section identity/content, section boundaries, nearby headings, and link anchor. Retain these concrete ranges/identifiers and fingerprints with the preview so the pre-write reread and post-write verification compare the same witnesses.

Show: the target question and exact Sheet row action; the Doc section title and create/update action; the proposed outline; personalized emphasis; and the specific section-link action. If edit access is absent, label the preview read-only and disclose that no write can occur until access changes. Wait for explicit confirmation of the current preview. A revision request is not approval: update the preview and its witnesses, then wait again. A decline is not approval: cancel the pending write and stop unless the user later requests another preview.

## Approved Write

Immediately before mutation, verify edit access and re-read the target Sheet row and Doc section against the exact approved preview and its preservation witnesses. If a concurrent change materially affects the target, proposed content, row action, section action, link action, or preservation assumptions, abort `WRITE`: make no mutation, invalidate the stale approval, rebase on the latest content, return to `PREVIEW`, and require fresh explicit approval. Never treat the prior approval as authorization for the rebased write.

When the approved snapshot is still current, update the exact existing section or create one using the current heading hierarchy, naming, formatting, and link convention; verify it is not a duplicate. Obtain or preserve a section-specific link, then mutate only the intended Sheet fields or add the deferred new row according to the inferred schema.

## Verification and Recovery

Do not claim completion from successful mutation responses. Re-read the exact created/updated Doc section and the exact Sheet row. Resolve or open the section-specific link stored in that row and prove that its document identity plus anchor/bookmark targets that exact section, not merely the Doc or a similarly titled section. Verify the approved content/action, confirm there is no duplicate section, and compare before/after preservation witnesses for unrelated cells, formulas, validations, formatting, neighboring rows, and unrelated Doc content. Report the row, fields, section, resolved link target, and preservation checks. If the link cannot be resolved to the exact section or any preservation check fails, report verification failure rather than success and preview any corrective mutation for approval.

On partial failure, state exactly which mutation succeeded and which failed. Re-read current state before retrying, reuse the exact already-created/updated section, and retry only the missing operation so no content or row is duplicated. The expected result of the already-approved successful mutation is not concurrent divergence: if there is no additional material change, the existing approval authorizes only the missing approved operation and no new approval is needed. If any additional concurrent change alters the missing operation or preservation assumptions, invalidate the approval and return to a revised preview.

## Common Mistakes

Do not write early; treat read-only as a reason to skip the interview; produce generic summaries; create duplicate rows or sections; request empty-Sheet schema approval twice; guess a schema or target; reuse stale approval after material changes; overwrite unrelated content; change conventions silently; accept a Doc-level link as a section link; or claim success without post-write reads.

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
