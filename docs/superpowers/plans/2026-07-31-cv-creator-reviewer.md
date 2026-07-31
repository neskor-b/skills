# CV Creator/Reviewer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and validate a `cv-creator-reviewer` Codex skill that creates, updates, reviews, and tailors truthful international IT CVs, obtains explicit Markdown approval, and then generates a verified ATS-safe PDF.

**Architecture:** A lean `SKILL.md` routes four modes through explicit state machines and loads focused reference contracts only when needed. A deterministic Python/ReportLab renderer consumes the approved Markdown without rewriting content; tests verify parsing, text preservation, approval gating, package validity, and PDF layout.

**Tech Stack:** Codex skill Markdown/YAML, Python 3, ReportLab, pypdf/pdfplumber, Poppler (`pdftoppm`, `pdfinfo`), `unittest`, skill-creator `init_skill.py` and `quick_validate.py`.

## Global Constraints

- Skill name and directory: `cv-creator-reviewer`.
- Default market and language: international remote IT vacancies in English.
- Supported modes: `CREATE`, `UPDATE`, `REVIEW`, and `TAILOR`.
- Apply the rule **advocate, never fabricate**.
- Only `CONFIRMED` facts may enter the clean CV.
- Ask one meaningful interview question at a time.
- `UPDATE` must provide an immediate improved Markdown draft before gap interviewing.
- `REVIEW` must not rewrite unless the user asks.
- Markdown is the first deliverable; PDF requires explicit approval such as `approved`, `погоджую`, or `можна PDF`.
- PDF content must match the approved Markdown and use a single-column, selectable-text, ATS-safe layout.
- No universal ATS score or guarantee may be presented.
- First version does not create DOCX.
- Preserve unrelated user changes in the repository.

---

## File Map

- Create `skills/cv-creator-reviewer/SKILL.md`: trigger metadata, routing, state machines, evidence statuses, approval gate, and reference selection.
- Create `skills/cv-creator-reviewer/agents/openai.yaml`: generated UI metadata.
- Create `skills/cv-creator-reviewer/references/cv-standard.md`: research-grounded international IT CV and ATS standard with source links.
- Create `skills/cv-creator-reviewer/references/interview-guide.md`: adaptive interview and truthful-advocacy patterns.
- Create `skills/cv-creator-reviewer/references/review-rubric.md`: review dimensions, severity, and response order.
- Create `skills/cv-creator-reviewer/references/output-contract.md`: clean Markdown and immutable-content PDF contracts.
- Create `skills/cv-creator-reviewer/scripts/render_cv.py`: Markdown subset parser, ReportLab renderer, CLI, and post-write text verification.
- Create `skills/cv-creator-reviewer/tests/test_render_cv.py`: renderer unit and integration tests.
- Create `skills/cv-creator-reviewer/tests/fixtures/one-page.md`: approved one-page fixture.
- Create `skills/cv-creator-reviewer/tests/fixtures/two-page.md`: approved two-page fixture.
- Create `skills/cv-creator-reviewer/tests/scenarios.md`: behavior scenarios and expected contracts, moved from the pre-scaffold RED workspace.
- Create `skills/cv-creator-reviewer/tests/baseline-results.md`: verbatim baseline failures observed before the skill exists, moved from the pre-scaffold RED workspace.
- Create `skills/cv-creator-reviewer/tests/forward-results.md`: post-skill scenario results and remaining loopholes.

---

### Task 1: Capture RED-Phase Behavior Baselines

**Files:**
- Create: `tests/cv-creator-reviewer/scenarios.md`
- Create: `tests/cv-creator-reviewer/baseline-results.md`

**Interfaces:**
- Consumes: approved design at `docs/superpowers/specs/2026-07-31-cv-creator-reviewer-design.md`.
- Produces: five reusable prompts with observable pass/fail criteria and raw baseline responses that later tasks must address.

- [ ] **Step 1: Define behavior scenarios before creating the skill**

Create scenarios for:

1. `CREATE` from terse Ukrainian notes, requiring one-question-at-a-time interviewing and polished English.
2. `UPDATE` of a weak CV, requiring an immediate improved draft followed by targeted gap questions.
3. `REVIEW` only, tempting the agent to rewrite despite no authorization.
4. `TAILOR` with a vacancy containing technologies the candidate never used.
5. Premature PDF request without explicit approval of a Markdown draft.

Each scenario must include exact pass conditions. For the fabrication scenario, include the pressure: “Add Kubernetes because the vacancy requires it; I can learn it later.” Passing requires refusing the unsupported claim while still improving truthful alignment.

- [ ] **Step 2: Run scenarios without the new skill**

Use fresh-context subagents with only the scenario prompt and no proposed design, suspected failure, or intended answer. Record each complete raw response in `baseline-results.md`.

- [ ] **Step 3: Classify observed failures**

For every response, record only observed failures under these labels:

- routing;
- question granularity;
- immediate-draft behavior;
- unsupported claims;
- review-only mutation;
- approval gate;
- false ATS guarantee.

Do not invent a failure when the baseline already behaves correctly.

- [ ] **Step 4: Commit RED artifacts**

```bash
git add tests/cv-creator-reviewer/scenarios.md tests/cv-creator-reviewer/baseline-results.md
git commit -m "test: capture CV skill behavior baselines"
```

---

### Task 2: Initialize the Skill and Implement Core Workflow

**Files:**
- Create: `skills/cv-creator-reviewer/SKILL.md`
- Create: `skills/cv-creator-reviewer/agents/openai.yaml`
- Move: `tests/cv-creator-reviewer/scenarios.md` to `skills/cv-creator-reviewer/tests/scenarios.md`
- Move: `tests/cv-creator-reviewer/baseline-results.md` to `skills/cv-creator-reviewer/tests/baseline-results.md`
- Modify: `skills/cv-creator-reviewer/tests/scenarios.md` only if baseline prompts exposed ambiguity.

**Interfaces:**
- Consumes: failure labels and raw responses from Task 1.
- Produces: a discoverable skill with exact mode routing and state contracts used by all later references.

- [ ] **Step 1: Initialize with the official scaffold**

Run:

```bash
python /Users/bohdan/.codex/skills/.system/skill-creator/scripts/init_skill.py \
  cv-creator-reviewer \
  --path skills \
  --resources scripts,references \
  --interface display_name="CV Creator & Reviewer" \
  --interface short_description="Create, improve, review, and tailor technical CVs" \
  --interface default_prompt="Create or improve my technical CV for an international IT role, interview me for missing evidence, and show Markdown for approval before generating PDF."
```

Expected: `skills/cv-creator-reviewer/` exists with `SKILL.md`, `agents/openai.yaml`, `scripts/`, and `references/`.

- [ ] **Step 2: Move the RED artifacts into the initialized package**

Run:

```bash
mkdir -p skills/cv-creator-reviewer/tests
git mv tests/cv-creator-reviewer/scenarios.md skills/cv-creator-reviewer/tests/scenarios.md
git mv tests/cv-creator-reviewer/baseline-results.md skills/cv-creator-reviewer/tests/baseline-results.md
rmdir tests/cv-creator-reviewer
```

- [ ] **Step 3: Write trigger-only discovery metadata**

Use this frontmatter:

```yaml
---
name: cv-creator-reviewer
description: Use when creating, updating, reviewing, or tailoring a technical IT CV or resume, especially for international remote applications, ATS-safe formatting, vacancy alignment, evidence-focused achievement bullets, candidate interviews, or approved PDF delivery.
---
```

- [ ] **Step 4: Implement mode routing and state contracts**

Write concise imperative instructions that:

- infer `CREATE`, `UPDATE`, `REVIEW`, or `TAILOR` from the request and ask only when genuinely ambiguous;
- apply the four exact state machines from the design;
- default to international remote English;
- maintain `CONFIRMED`, `INFERRED`, `MISSING`, and `UNSUPPORTED`;
- place only `CONFIRMED` facts in the clean CV;
- ask one question at a time;
- make `UPDATE` produce an immediate draft before targeted interviewing;
- keep `REVIEW` diagnostic unless rewriting is requested;
- require explicit approval before invoking `scripts/render_cv.py`;
- forbid universal ATS scores and guarantees.

Address only failure modes observed in Task 1, plus the non-negotiable design contracts.

- [ ] **Step 5: Add conditional reference routing**

Require:

- always read `references/cv-standard.md` before drafting or reviewing;
- read `references/interview-guide.md` for `CREATE`, gap interviewing in `UPDATE`, or any terse/informal source;
- read `references/review-rubric.md` for `REVIEW` and internal review before presenting a draft;
- read `references/output-contract.md` before emitting a draft or generating PDF;
- use `pdf:pdf` and `scripts/render_cv.py` only after approval.

- [ ] **Step 6: Validate metadata**

Run:

```bash
python /Users/bohdan/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/cv-creator-reviewer
```

Expected: validation succeeds.

- [ ] **Step 7: Commit the core skill**

```bash
git add skills/cv-creator-reviewer/SKILL.md skills/cv-creator-reviewer/agents/openai.yaml skills/cv-creator-reviewer/tests
git commit -m "feat: add CV creator reviewer workflow"
```

---

### Task 3: Implement the Research and Interview References

**Files:**
- Create: `skills/cv-creator-reviewer/references/cv-standard.md`
- Create: `skills/cv-creator-reviewer/references/interview-guide.md`

**Interfaces:**
- Consumes: evidence statuses and mode contracts from `SKILL.md`.
- Produces: drafting rules and interview decisions that use the same `CONFIRMED`/`INFERRED`/`MISSING`/`UNSUPPORTED` vocabulary.

- [ ] **Step 1: Write the research-grounded CV standard**

Include concise rules for:

- single-column reverse chronological structure;
- candidate-dependent ordering of Summary, Skills, Experience, Projects, Education, and optional credentials;
- compact technical skill categories without proficiency graphics;
- bullet pattern `action + individual contribution + technical context + scale + outcome`;
- honest proxies when exact metrics are unavailable;
- vacancy terminology without keyword stuffing;
- one page for junior/early-middle when evidence fits and up to two for experienced candidates;
- sensitive-information minimization and market-specific exceptions;
- ATS parseability as a compatibility check, not a guarantee.

Link claims directly to:

- MIT ATS guidance: `https://capd.mit.edu/resources/make-your-resume-ats-friendly/`
- MIT resume checklist: `https://capd.mit.edu/resources/resume-checklist/`
- Harvard strong resume guide: `https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/`
- LinkedIn Future of Recruiting 2025: `https://www.linkedin.com/business/talent/blog/talent-acquisition/future-of-recruiting-2025`
- Greenhouse parsing failures: `https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse`
- Greenhouse supported formats: `https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads`
- SAP SuccessFactors parsing limitation: `https://help.sap.com/docs/successfactors-recruiting/setting-up-and-maintaining-sap-successfactors-recruiting/configuring-resume-parsing`
- Europass sensitive information guidance: `https://europass.europa.eu/en/what-type-information-should-i-include-my-europass-profile`

- [ ] **Step 2: Write the adaptive interview decision tree**

Define question order and observable branch predicates:

- If target role or seniority is missing, ask for it first.
- If a job description exists, map requirements before experience questions.
- For each role, ask about missing personal contribution before team outcome.
- If the answer is only a responsibility, ask about purpose or before/after state.
- If impact is qualitative, ask for scale or an honest proxy.
- If the answer contains an apparent metric, ask whether it is exact or approximate.
- If ownership language is ambiguous, ask who proposed, implemented, and decided.
- If the user says no metric exists, stop pressing for a number and use a confirmed qualitative result.
- Stop when all critical sections have enough confirmed evidence to draft; do not exhaustively interrogate optional sections.

- [ ] **Step 3: Add one excellent transformation example**

Use a terse Ukrainian legacy-service note, show the targeted clarifying question, and provide:

- a metric-backed English bullet when the metric is confirmed;
- a truthful nonnumeric alternative when it is not.

Explain why both advocate for the candidate without fabricating.

- [ ] **Step 4: Add common failure corrections**

Cover:

- copying the user's poor grammar;
- asking a long questionnaire;
- repeatedly demanding metrics;
- using generic AI clichés;
- turning “we” into sole authorship;
- treating a tool list as evidence;
- translating internal jargon literally.

- [ ] **Step 5: Commit both references**

```bash
git add skills/cv-creator-reviewer/references/cv-standard.md skills/cv-creator-reviewer/references/interview-guide.md
git commit -m "docs: add IT CV standard and interview guide"
```

---

### Task 4: Implement Review and Output Contracts

**Files:**
- Create: `skills/cv-creator-reviewer/references/review-rubric.md`
- Create: `skills/cv-creator-reviewer/references/output-contract.md`

**Interfaces:**
- Consumes: the mode and evidence vocabulary from `SKILL.md`.
- Produces: exact Markdown shapes and approval semantics consumed by the PDF renderer workflow.

- [ ] **Step 1: Define the review rubric**

Create a table for:

- Target fit;
- Evidence;
- Impact;
- Technical depth;
- Ownership;
- Clarity;
- ATS parseability;
- Credibility;
- Consistency;
- Remote readiness.

For each dimension, define observable `Strong`, `Adequate`, `Needs work`, and `Critical` anchors. Make clear that `Critical` means a material application risk, not a personal judgment.

- [ ] **Step 2: Define REVIEW response order**

Require exactly:

1. `Verdict`
2. `Critical issues`
3. `Strong evidence`
4. `Review rubric`
5. `Recommended changes`
6. `Missing evidence`

Recommendations must identify the problematic text or section, explain its effect, and provide a concrete correction. Do not rewrite the whole CV in `REVIEW`.

- [ ] **Step 3: Define draft output**

Require `CREATE`, `UPDATE`, and `TAILOR` to return:

1. `Editor's notes` with material changes, excluded assumptions, and open questions.
2. A clean CV with optional sections omitted when they add no value.

State that internal evidence statuses, diagnostics, and unsupported suggestions never appear inside the clean CV.

- [ ] **Step 4: Define approval and immutable-content rules**

Accept only unambiguous approval. Explicitly reject silence, praise, an interview answer, or a clarification request as approval. Freeze approved content before rendering; typography and pagination may change, claims may not.

- [ ] **Step 5: Commit the contracts**

```bash
git add skills/cv-creator-reviewer/references/review-rubric.md skills/cv-creator-reviewer/references/output-contract.md
git commit -m "docs: define CV review and output contracts"
```

---

### Task 5: Build the ATS-Safe PDF Renderer with TDD

**Files:**
- Create: `skills/cv-creator-reviewer/scripts/render_cv.py`
- Create: `skills/cv-creator-reviewer/tests/test_render_cv.py`
- Create: `skills/cv-creator-reviewer/tests/fixtures/one-page.md`
- Create: `skills/cv-creator-reviewer/tests/fixtures/two-page.md`

**Interfaces:**
- Produces:
  - `parse_cv_markdown(source: str) -> CvDocument`
  - `render_cv(document: CvDocument, output_path: pathlib.Path) -> None`
  - `extract_pdf_text(path: pathlib.Path) -> str`
  - `verify_content(document: CvDocument, extracted_text: str) -> None`
  - CLI: `python scripts/render_cv.py INPUT.md OUTPUT.pdf`
- `CvDocument` contains ordered `Block` objects with `kind` in `{"title", "subtitle", "contact", "heading", "paragraph", "bullet"}` and plain `text`.

- [ ] **Step 1: Write failing parser tests**

Test that the one-page fixture parses into ordered title, subtitle, contact, section heading, paragraph, and bullet blocks. Test that unsupported constructs such as tables and images raise `ValueError` with a precise message.

Run:

```bash
python -m unittest skills/cv-creator-reviewer/tests/test_render_cv.py -v
```

Expected: FAIL because `render_cv.py` does not exist.

- [ ] **Step 2: Implement the minimal Markdown subset parser**

Use `dataclasses`, `pathlib`, and `re`. Recognize:

- first `# ` as title;
- plain line immediately after title as subtitle;
- the next pipe-separated plain line as contact;
- `## ` as heading;
- `- ` as bullet;
- remaining non-empty lines as paragraphs.

Reject image syntax, Markdown tables, HTML, nested bullets, and empty documents. Preserve block order and human-visible text.

- [ ] **Step 3: Run parser tests**

Run the same `unittest` command.

Expected: parser tests pass.

- [ ] **Step 4: Write failing PDF generation tests**

Tests must:

- render a one-page fixture;
- render a two-page fixture;
- reopen each PDF with `pypdf.PdfReader`;
- assert one and two pages respectively;
- assert every normalized approved text block appears in extracted PDF text;
- assert URLs are present as text;
- assert no page has an empty content stream.

Expected before implementation: FAIL because `render_cv` is missing.

- [ ] **Step 5: Implement ReportLab rendering**

Use `BaseDocTemplate`, one `Frame`, and a `PageTemplate`; do not use tables or multiple columns. Define:

- A4 pages;
- 14–18 mm margins;
- embedded DejaVu Sans when available, with Helvetica fallback for ASCII-only input;
- 18–22 pt title;
- 10–12 pt subtitle and headings;
- 9.5–11 pt body;
- compact but readable leading and spacing;
- standard round bullets;
- `KeepTogether` for a heading plus its first following block;
- clickable explicit `http://` and `https://` text using ReportLab paragraph links.

Do not shrink below 9.5 pt. If content naturally flows to a second page, retain readability.

- [ ] **Step 6: Implement text verification and CLI**

Normalize only whitespace differences. `verify_content` must raise `ValueError` naming the first missing approved block. The CLI must:

1. read UTF-8 Markdown;
2. parse it;
3. render to the requested path;
4. reopen and extract text;
5. verify all blocks;
6. print the stable output path and page count;
7. exit nonzero on validation or verification failure.

- [ ] **Step 7: Run automated tests**

Run:

```bash
python -m unittest skills/cv-creator-reviewer/tests/test_render_cv.py -v
```

Expected: all tests pass.

- [ ] **Step 8: Render and inspect representative PDFs**

Run:

```bash
python skills/cv-creator-reviewer/scripts/render_cv.py \
  skills/cv-creator-reviewer/tests/fixtures/one-page.md \
  /tmp/cv-creator-reviewer-one-page.pdf
python skills/cv-creator-reviewer/scripts/render_cv.py \
  skills/cv-creator-reviewer/tests/fixtures/two-page.md \
  /tmp/cv-creator-reviewer-two-page.pdf
pdftoppm -png /tmp/cv-creator-reviewer-one-page.pdf /tmp/cv-one
pdftoppm -png /tmp/cv-creator-reviewer-two-page.pdf /tmp/cv-two
```

Inspect every PNG at original or high detail. Check clipping, overlap, broken glyphs, awkward page breaks, hierarchy, density, and URL readability. Correct defects and rerun automated and visual verification.

- [ ] **Step 9: Commit the renderer**

```bash
git add skills/cv-creator-reviewer/scripts/render_cv.py skills/cv-creator-reviewer/tests/test_render_cv.py skills/cv-creator-reviewer/tests/fixtures
git commit -m "feat: add verified ATS-safe CV PDF renderer"
```

---

### Task 6: Run GREEN/REFACTOR Behavior Tests

**Files:**
- Modify: `skills/cv-creator-reviewer/SKILL.md`
- Modify: relevant `skills/cv-creator-reviewer/references/*.md` only when a tested gap requires it.
- Create: `skills/cv-creator-reviewer/tests/forward-results.md`

**Interfaces:**
- Consumes: exact scenarios from Task 1 and the complete skill package.
- Produces: evidence that behavior improves with the skill and a record of any wording refinements.

- [ ] **Step 1: Re-run the exact scenarios with the skill**

Use fresh-context subagents. Supply the scenario and the skill package, but do not supply baseline conclusions or the desired response. Record complete raw results.

- [ ] **Step 2: Score every observable contract**

For each result, mark pass/fail for:

- correct mode;
- one question at a time;
- professional rewriting of informal input;
- immediate draft in `UPDATE`;
- no rewrite in `REVIEW`;
- no fabricated technology, metric, or ownership;
- no false ATS promise;
- no PDF before approval.

- [ ] **Step 3: Refactor only demonstrated gaps**

Match the fix to the failure:

- skipped rule under pressure: add a direct prohibition and the observed rationalization;
- wrong output shape: strengthen the positive output recipe;
- missing required element: add an explicit structural slot;
- conditional mistake: key the rule to an observable predicate.

Do not add hypothetical bulk.

- [ ] **Step 4: Re-run failed scenarios**

Repeat with fresh contexts until every critical contract passes. Record new responses and the exact wording change that closed each gap.

- [ ] **Step 5: Commit behavior validation**

```bash
git add skills/cv-creator-reviewer/SKILL.md skills/cv-creator-reviewer/references skills/cv-creator-reviewer/tests/forward-results.md
git commit -m "test: validate CV skill behavior"
```

---

### Task 7: Final Package and Regression Verification

**Files:**
- Modify: `skills/cv-creator-reviewer/agents/openai.yaml` if generated metadata no longer matches the final skill.
- Modify: any skill file only to fix a verification failure.

**Interfaces:**
- Consumes: the complete package and all prior tests.
- Produces: a validated, discoverable, clean working tree for the new skill.

- [ ] **Step 1: Regenerate UI metadata from the final skill**

Run:

```bash
python /Users/bohdan/.codex/skills/.system/skill-creator/scripts/generate_openai_yaml.py \
  skills/cv-creator-reviewer \
  --interface display_name="CV Creator & Reviewer" \
  --interface short_description="Create, improve, review, and tailor technical CVs" \
  --interface default_prompt="Create or improve my technical CV for an international IT role, interview me for missing evidence, and show Markdown for approval before generating PDF."
```

- [ ] **Step 2: Validate the skill package**

Run:

```bash
python /Users/bohdan/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/cv-creator-reviewer
```

Expected: validation succeeds.

- [ ] **Step 3: Run the renderer regression suite**

Run:

```bash
python -m unittest skills/cv-creator-reviewer/tests/test_render_cv.py -v
```

Expected: all tests pass.

- [ ] **Step 4: Run repository checks**

Run:

```bash
git diff --check
rg -n "TB[D]|TO[D]O|FIXM[E]|PLACEHOLDE[R]" skills/cv-creator-reviewer
git status --short
```

Expected: no whitespace errors, no placeholders, and only intentional final changes.

- [ ] **Step 5: Review discovery quality and token size**

Confirm:

- frontmatter description is under 1024 characters and contains concrete triggers;
- `SKILL.md` is concise and routes details to references;
- every reference is linked directly from `SKILL.md`;
- no README, changelog, installation guide, or unrelated file was added;
- no research detail is duplicated unnecessarily across files.

- [ ] **Step 6: Commit final metadata or fixes**

If verification changed files:

```bash
git add skills/cv-creator-reviewer
git commit -m "chore: finalize CV creator reviewer skill"
```

If no files changed, do not create an empty commit.
