# Google Interview Coach Skill Design

## Goal

Create a reusable Codex skill that conducts an adaptive technical interview based on questions stored in an existing Google Sheet, evaluates the user's answers, and maintains a personalized topic cheat sheet as a section in an existing Google Doc.

The skill must use the connected Google Drive, Google Sheets, and Google Docs capabilities. It must preserve and extend the existing structures of the Sheet and Doc rather than imposing a new schema.

## Inputs and Session Start

At the beginning of each new interview session, ask for:

1. The conversation language: Ukrainian or English.
2. The Google Sheet URL.
3. The Google Doc URL.
4. The selection mode:
   - choose a random question from the Sheet;
   - let the user provide a question or topic.

Reuse URLs already provided in the current conversation, but do not store personal URLs inside the skill.

Validate that both resources are accessible before continuing. Verify edit access before attempting the final write.

## Existing Structure as the Authority

Infer the Sheet schema from its headers, formatting, formulas, links, and representative populated rows on every run. Preserve:

- column meanings and order;
- value and link formats;
- formulas and validation rules;
- row formatting and conventions;
- the existing method for linking a question to a Doc section.

Infer the Google Doc's organization and section-linking convention from existing content. New cheat-sheet sections must follow the same heading hierarchy, formatting, naming, and linking convention.

Do not guess when multiple columns or document targets are plausible. Ask one focused clarification instead.

If the Sheet has no usable schema because it is empty, propose a minimal schema and wait for explicit approval before creating it. The proposal should include at least a question field and a cheat-sheet-section link field, plus any additional fields that are clearly useful and approved by the user.

## Question Selection

### Random mode

Select uniformly from non-empty question rows. Do not select headers, helper rows, archived rows, or other records that the inferred schema marks as inactive.

### User-selected mode

Search the Sheet for an exact or semantically equivalent question or topic.

- Exact or clear semantic match: reuse the existing row.
- Multiple plausible matches: show concise candidates and ask the user to choose.
- No match: conduct the interview, then prepare a new row that follows the inferred schema.

Do not add the new row before the interview and preview are complete.

## Interview Behavior

Conduct the interview as a realistic interviewer:

- ask one question at a time;
- begin with an open-ended question;
- adapt follow-ups to the user's answers;
- probe definitions, mechanisms, trade-offs, edge cases, and practical application;
- request examples or code when relevant;
- point out contradictions through follow-up questions without revealing the correct answer prematurely;
- avoid exposing or editing the cheat sheet during the interview.

The interview has no fixed question count. Continue until there is enough evidence to assess the important parts of the topic. Five to eight substantive questions is a typical range, not a limit.

## Evaluation

After the interview, produce an evidence-based analysis tied to the user's actual answers:

- correct points;
- partially correct points;
- incorrect statements or omissions;
- ability to apply the knowledge in practice;
- highest-priority learning gaps;
- related topics worth studying or interviewing next.

Clearly distinguish factual mistakes from incomplete explanations, terminology issues, and missing depth.

## Personalized Cheat Sheet

Create or update the cheat sheet only after the interview and evaluation are complete.

The cheat sheet must remain a complete, self-contained overview of the whole topic. It is not limited to mistakes. Include, when relevant:

- a concise definition and core idea;
- essential concepts, rules, and mechanisms;
- important nuances, trade-offs, and common mistakes;
- practical examples or code;
- related topics;
- a prominent section describing what the user should focus on;
- high-quality learning links for the gaps found during the interview.

Personalize depth rather than coverage:

- cover well-understood material concisely;
- give more explanation, examples, warnings, and learning resources to weak or missed areas;
- retain useful existing content;
- correct inaccuracies and stale material;
- update the personalized emphasis based on the latest interview;
- never create a duplicate section for the same question.

When a linked section already exists, update that exact section. When no valid section exists, prepare a new section that follows the Doc's current structure.

## Preview and Write Approval

Before changing either Google file, show a short preview containing:

- the target question and Sheet row action;
- the target Doc section title and whether it will be created or updated;
- the proposed cheat-sheet outline;
- the main personalized additions or emphasis;
- the link action that will be applied to the Sheet.

Wait for explicit user confirmation. A request to revise the preview is not approval to write.

After approval:

1. Re-read the target Sheet row and Doc section to detect intervening changes.
2. Update or create the Doc section.
3. Obtain or preserve the section-specific link using the document's existing convention.
4. Update or add the Sheet row and link without altering unrelated cells.
5. Re-read both resources and verify the result.

## Failure Handling and Consistency

- Invalid URL, inaccessible file, or wrong file type: stop and explain the exact correction needed.
- Read access without edit access: allow the interview and preview, but do not claim the files were updated.
- Ambiguous schema or target: ask a focused question before writing.
- Broken or missing section link: prepare a corrected/new target and disclose it in the preview.
- Concurrent changes detected before writing: rebase the proposed change on the latest content and show a revised preview if the outcome materially changes.
- Partial write failure: state exactly which mutation succeeded, avoid duplicating content on retry, and offer a safe completion step.

Never rebuild the Sheet, reorganize the Doc, overwrite unrelated content, or silently change formatting conventions.

## Verification Scenarios

Forward-test the skill against at least these scenarios:

1. Random selection from a populated Sheet.
2. User-selected topic with an exact existing match.
3. User-selected topic with several similar matches.
4. New topic absent from the Sheet.
5. Existing and valid cheat-sheet section.
6. Missing or broken section link.
7. Empty Sheet requiring a proposed schema.
8. Ambiguous inferred schema.
9. User requests preview revisions or declines the write.
10. Failure after the Doc update but before the Sheet update.

Success means the skill conducts an adaptive interview, grounds its evaluation in the answers, produces a complete but gap-weighted cheat sheet, obtains approval before mutation, preserves existing structures, and verifies the final cross-link.

## Skill Packaging

Create one orchestrating skill in `skills/` with:

- a concise `SKILL.md`;
- `agents/openai.yaml`;
- only the supporting references required to keep the main instructions concise.

The skill should explicitly require the connected Google Drive, Google Sheets, and Google Docs sub-skills rather than duplicate their operational instructions.
