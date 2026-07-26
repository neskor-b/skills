# Google Interview Coach Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reusable Codex skill that runs adaptive interviews from an existing Google Sheet and, after approval, maintains a complete but gap-weighted cheat-sheet section in an existing Google Doc.

**Architecture:** Create one orchestration skill that delegates Google file operations to the installed Google Drive, Google Sheets, and Google Docs skills. Keep the trigger and core state machine in `SKILL.md`; place the detailed interview, evaluation, preview, mutation, and recovery contracts in one directly linked reference.

**Tech Stack:** Codex skills (`SKILL.md`), YAML UI metadata, Markdown reference documentation, the `skill-creator` initialization and validation scripts, and forward-tests with fresh subagents.

## Global Constraints

- Create the skill under `skills/google-interview-coach/`.
- Infer and preserve the existing Google Sheet and Google Doc structures on every run.
- Ask for Ukrainian or English, both Google URLs, and random or user-selected mode at session start.
- Conduct an adaptive interview before creating or updating any cheat sheet.
- Produce a complete topic cheat sheet while giving extra depth and learning links to gaps revealed by the interview.
- Show a short preview and require explicit approval before any Google file mutation.
- Re-read before writing and verify both resources after writing.
- Do not store personal Google URLs inside the skill.
- Do not add unrelated repository documentation.

---

### Task 1: Baseline Forward-Test

**Files:**
- Create: `/tmp/google-interview-coach-baseline.md`
- Read: `docs/superpowers/specs/2026-07-26-google-interview-coach-design.md`

**Interfaces:**
- Consumes: the approved design specification.
- Produces: a baseline trace identifying behaviors that generic agents omit without the skill.

- [ ] **Step 1: Define the baseline scenario**

Use a fresh subagent without access to the new skill:

```text
You have connected Google Drive, Google Sheets, and Google Docs tools. A user says:
"Проведи технічну співбесіду за моєю таблицею: https://docs.google.com/spreadsheets/d/example.
Шпаргалки зберігаються розділами тут: https://docs.google.com/document/d/example.
Після цього онови матеріали."

Describe exactly how you would proceed, including the dialogue, when you read or write files,
how you handle a missing topic, and what you put in the cheat sheet. Do not perform live writes.
```

- [ ] **Step 2: Run the baseline**

Dispatch the scenario to a fresh subagent without mentioning the planned skill or expected behavior.

Expected: the response omits or weakens at least one critical contract such as language selection, adaptive evidence collection, schema preservation, full-but-gap-weighted cheat-sheet content, preview approval, or post-write verification.

- [ ] **Step 3: Record the observed failures**

Write `/tmp/google-interview-coach-baseline.md` with:

```markdown
# Baseline

## Scenario
The exact fresh-context prompt from Step 1.

## Observed omissions
- Quote each omitted, reordered, or contradicted behavior from the subagent trace.

## Wording to teach
- For each omission, state the smallest positive output or ordering contract that would correct it.
```

- [ ] **Step 4: Confirm RED**

Read the trace and verify that it records actual observed behavior rather than hypothetical risks.

### Task 2: Scaffold and Author the Skill

**Files:**
- Create: `skills/google-interview-coach/SKILL.md`
- Create: `skills/google-interview-coach/agents/openai.yaml`
- Create: `skills/google-interview-coach/references/workflow-contract.md`
- Read: `/Users/bohdan/.codex/skills/.system/skill-creator/references/openai_yaml.md`
- Read: `/tmp/google-interview-coach-baseline.md`

**Interfaces:**
- Consumes: baseline omissions and the approved design.
- Produces: `$google-interview-coach`, with `references/workflow-contract.md` directly linked from `SKILL.md`.

- [ ] **Step 1: Read UI metadata rules**

Read `openai_yaml.md` completely and use only supported fields.

- [ ] **Step 2: Initialize the skill**

Run:

```bash
/Users/bohdan/.codex/skills/.system/skill-creator/scripts/init_skill.py google-interview-coach \
  --path /Users/bohdan/Desktop/skills/skills \
  --resources references \
  --interface 'display_name=Google Interview Coach' \
  --interface 'short_description=Run adaptive interviews from Google Sheets and maintain focused Google Docs cheat sheets' \
  --interface 'default_prompt=Use $google-interview-coach to interview me from my Google Sheet and update my Google Doc cheat sheet after review.'
```

Expected: a new skill folder with `SKILL.md`, `agents/openai.yaml`, and `references/`.

- [ ] **Step 3: Write the minimal trigger and state machine**

Replace the generated `SKILL.md` with a concise document containing:

```yaml
---
name: google-interview-coach
description: Use when conducting a technical interview from questions in a Google Sheet and maintaining linked topic cheat-sheet sections in a Google Doc, including random or user-selected topics, adaptive questioning, answer analysis, and approved synchronization.
---
```

The body must:

- require `google-drive:google-drive`, `google-drive:google-sheets`, and `google-drive:google-docs`;
- require reading `references/workflow-contract.md` before starting;
- define the ordered states `SETUP -> DISCOVER -> SELECT -> INTERVIEW -> EVALUATE -> PREVIEW -> APPROVE -> WRITE -> VERIFY`;
- state that no write occurs before `APPROVE`;
- state that the interview precedes cheat-sheet generation;
- address every observed baseline omission using positive output contracts.

- [ ] **Step 4: Write the workflow contract**

Create `references/workflow-contract.md` with these explicit sections:

1. `Session Setup`: language, URLs, access validation, selection mode.
2. `Schema and Document Discovery`: inference, preservation, empty-table proposal, ambiguity handling.
3. `Question Resolution`: uniform random selection, exact/semantic matching, duplicate prevention, deferred new-row creation.
4. `Adaptive Interview`: one prompt at a time, open-ended start, evidence coverage, realistic follow-ups, no answer leakage.
5. `Evidence-Based Evaluation`: correct, partial, incorrect, practical application, priorities, related topics.
6. `Complete Gap-Weighted Cheat Sheet`: full coverage, concise mastered areas, expanded gaps, examples, warnings, quality learning links.
7. `Preview Contract`: row action, section action, outline, personalized emphasis, link action.
8. `Approved Write`: re-read, update/create section, section link, precise row mutation.
9. `Verification and Recovery`: post-write reads, concurrent edits, partial failure, safe retry.
10. `Common Mistakes`: writing early, generic summaries, duplicate rows/sections, guessing schema, claiming unverified success.

Include one compact end-to-end example showing the agent's opening prompts and preview shape, without real URLs or private data.

- [ ] **Step 5: Inspect generated metadata**

Run:

```bash
sed -n '1,160p' skills/google-interview-coach/agents/openai.yaml
```

Expected: only the generated `interface` fields, with `$google-interview-coach` preserved literally in `default_prompt`.

- [ ] **Step 6: Check concise packaging**

Run:

```bash
wc -l -w skills/google-interview-coach/SKILL.md \
  skills/google-interview-coach/references/workflow-contract.md
```

Expected: `SKILL.md` remains below 500 words and the reference is directly discoverable from it.

### Task 3: Validate Behavior and Packaging

**Files:**
- Test: `skills/google-interview-coach/SKILL.md`
- Test: `skills/google-interview-coach/references/workflow-contract.md`
- Test: `skills/google-interview-coach/agents/openai.yaml`

**Interfaces:**
- Consumes: the authored `$google-interview-coach` skill.
- Produces: evidence that the skill is structurally valid and changes agent behavior as intended.

- [ ] **Step 1: Run structural validation**

Run:

```bash
/Users/bohdan/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/bohdan/Desktop/skills/skills/google-interview-coach
```

Expected: validation succeeds.

- [ ] **Step 2: Run repository hygiene checks**

Run:

```bash
git diff --check
rg -n 'TBD|TODO|FIXME|example\.com|spreadsheets/d/example|document/d/example' \
  skills/google-interview-coach
```

Expected: `git diff --check` succeeds and the search returns no placeholders or baseline example URLs.

- [ ] **Step 3: Run the GREEN forward-test**

Dispatch a fresh subagent with:

```text
Use $google-interview-coach at
/Users/bohdan/Desktop/skills/skills/google-interview-coach to respond to this request:

"Проведи технічну співбесіду за моєю Google-таблицею та після неї онови розділ
шпаргалки в Google Doc."

There are no live URLs in this test. Demonstrate the next correct conversational action and
then summarize the later state transitions. Do not invent URLs and do not perform writes.
```

Expected: it first asks the required setup questions, keeps interview before evaluation and cheat-sheet generation, and places preview approval before all writes.

- [ ] **Step 4: Run edge-case forward-tests**

Use fresh contexts for:

```text
Use $google-interview-coach. The Sheet is empty. Show the next action only.
```

Expected: propose a schema and wait for approval.

```text
Use $google-interview-coach. The interview is complete, and I answered most points correctly
but missed two edge cases. Describe the cheat-sheet content and next action.
```

Expected: complete topic coverage, expanded treatment of the two gaps, and preview before writing.

```text
Use $google-interview-coach. The Doc update succeeded, but the Sheet link update failed.
Describe recovery.
```

Expected: report exact partial state and retry only the missing Sheet operation without duplicating the Doc section.

- [ ] **Step 5: Compare RED and GREEN**

Confirm that each omission in `/tmp/google-interview-coach-baseline.md` is explicitly corrected in the GREEN traces. If a failure remains, tighten the smallest relevant contract and repeat Steps 1–4.

- [ ] **Step 6: Commit the skill**

Run:

```bash
git add skills/google-interview-coach
git commit -m "Add Google interview coach skill"
```

Expected: one commit containing only the new skill files.

### Task 4: Final Verification and Repository Handoff

**Files:**
- Test: `skills/google-interview-coach/`
- Modify: `README.md`

**Interfaces:**
- Consumes: the validated skill.
- Produces: repository discovery metadata and a final clean verification report.

- [ ] **Step 1: Add the skill to the repository index**

Add one row to `README.md` under `Local Skills`:

```markdown
| `google-interview-coach` | Runs adaptive interviews from Google Sheets and maintains linked Google Docs cheat sheets | `google-drive`, `google-sheets`, `google-docs` |
```

Add a short note under `Required External Skills` explaining that the Google Drive plugin must be connected for live use.

- [ ] **Step 2: Re-run all non-live checks**

Run:

```bash
/Users/bohdan/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/bohdan/Desktop/skills/skills/google-interview-coach
git diff --check
git status --short
```

Expected: validation succeeds, no whitespace errors appear, and only the intended README change remains uncommitted.

- [ ] **Step 3: Commit repository discovery metadata**

Run:

```bash
git add README.md
git commit -m "Document Google interview coach skill"
```

- [ ] **Step 4: Verify committed state**

Run:

```bash
git status --short
git log -3 --oneline
```

Expected: clean status and commits for the design, skill, and repository index.
