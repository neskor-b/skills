# CV Creator/Reviewer Skill Design

## Purpose

Create a personal Codex skill for technical CVs in IT. The skill must create, update, review, and tailor CVs while acting as a truthful advocate for the candidate. It must transform short, informal, or poorly structured input into strong professional English without inventing experience, technologies, ownership, or metrics.

The default target is international remote IT vacancies in English. The user may override the language, market, role, seniority, and output length.

## Evidence Base

The skill's guidance will be grounded in current recommendations from MIT Career Advising, Harvard career services, LinkedIn skills-first hiring research, official Greenhouse and SAP SuccessFactors parsing documentation, Europass privacy guidance, and current software-engineering resume guidance.

The resulting standard must preserve these conclusions:

- Optimize for both quick human scanning and reliable text parsing.
- Treat ATS compatibility as parseability and truthful vacancy alignment, not a universal score or guaranteed pass.
- Prefer a single-column reverse-chronological structure with standard section names.
- Emphasize demonstrated skills, individual contribution, technical depth, scale, and outcomes.
- Tailor terminology and ordering to a vacancy only when supported by candidate evidence.
- Use AI as an interviewer and professional editor, never as a source of fabricated facts.
- Avoid unnecessary sensitive personal information and account for regional differences.

## Scope

The skill supports four modes:

- `CREATE`: build a CV from supplied information through an adaptive interview.
- `UPDATE`: audit an existing CV and immediately produce a stronger Markdown draft, then interview for missing or weak evidence and revise it.
- `REVIEW`: diagnose and prioritize issues without rewriting unless the user asks.
- `TAILOR`: adapt a confirmed CV to a specific vacancy without inventing qualifications.

Supported first-version outputs:

1. Structured text or Markdown for user validation.
2. ATS-safe PDF only after explicit approval of the Markdown content.

DOCX output is outside the first-version scope.

## Defaults and Intake

Defaults:

- Market: international remote.
- Language: English.
- Format: ATS-safe reverse chronological CV.
- Length: one page for junior and early-middle candidates when evidence fits; up to two pages for experienced middle, senior, staff, or management candidates.
- Delivery gate: Markdown first; PDF only after explicit approval.

At intake, determine:

- requested mode;
- target role and seniority;
- language and geographic market;
- presence of a job description;
- preferred or necessary length;
- available sources such as an existing CV, notes, LinkedIn, GitHub, portfolio, or project descriptions.

## State Machine

### CREATE

`INTAKE -> EVIDENCE_INVENTORY -> INTERVIEW -> DRAFT -> INTERNAL_REVIEW -> USER_REVIEW -> APPROVAL -> PDF_RENDER -> VERIFY`

Collect supplied facts, identify critical gaps, conduct an adaptive interview, create a Markdown CV, review it against the rubric, and show it to the user. Generate PDF only after explicit approval.

### UPDATE

`INTAKE -> PARSE -> AUDIT -> IMMEDIATE_DRAFT -> GAP_INTERVIEW -> REVISE -> USER_REVIEW -> APPROVAL -> PDF_RENDER -> VERIFY`

Audit the existing CV and immediately provide an improved Markdown draft. Keep assumptions and missing evidence outside the clean CV. Interview only for gaps or claims whose strength materially depends on clarification, then revise the draft.

### REVIEW

`INTAKE -> PARSE -> RUBRIC_REVIEW -> REPORT`

Return, in order:

1. Overall verdict.
2. Critical issues.
3. Strong evidence.
4. Rubric assessment.
5. Concrete recommended changes.
6. Questions that could uncover missing evidence.

Do not rewrite in this mode unless requested.

### TAILOR

`INTAKE -> REQUIREMENT_MAP -> EVIDENCE_MATCH -> DRAFT -> USER_REVIEW -> APPROVAL -> PDF_RENDER -> VERIFY`

Separate vacancy requirements into confirmed matches, partial matches, gaps, and unsupported claims. Change ordering, emphasis, terminology, and selection of content, but never disguise a genuine gap or add an unsupported qualification.

## Evidence Inventory

Track material facts using these statuses:

- `CONFIRMED`: directly supplied or explicitly confirmed by the user.
- `INFERRED`: plausible but awaiting confirmation.
- `MISSING`: necessary information is absent.
- `UNSUPPORTED`: must not appear as a candidate claim.

Only `CONFIRMED` facts may enter the clean CV. Present `INFERRED` material only as a clearly marked proposal or confirmation question outside the CV.

When sources conflict, stop work on the affected fragment, show the competing versions, and ask one focused question. Do not silently choose.

## Adaptive Interview

Ask one meaningful question at a time. Do not require the user to complete a long questionnaire and do not ask for facts already unambiguously available.

Cover, as relevant:

1. Target role, seniority, vacancy, market, and language.
2. Contact information and professional links.
3. Professional positioning.
4. Each work experience:
   - company, role, and dates;
   - product, domain, and scale;
   - individual responsibility;
   - key work and technologies;
   - technical decisions and trade-offs;
   - results and metrics;
   - collaboration, leadership, and ownership.
5. Selected projects, open source, GitHub, and portfolio.
6. Education, certifications, publications, talks, and awards.
7. Languages, work authorization, location, or time zone only when relevant.
8. Gaps and contradictions.
9. Final confirmation of material facts.

When the user describes only a responsibility, ask about purpose, before/after state, scale, adoption, reliability, performance, delivery, cost, security, or business impact. If exact metrics do not exist, seek an honest proxy such as teams served, production adoption, manual work removed, ownership scope, or incident class eliminated.

## Truthful Advocacy

Apply the principle: **advocate, never fabricate**.

The user may provide terse, informal, ungrammatical, Ukrainian-language, or poorly structured input. The skill must:

1. Extract facts from it.
2. Recognize hidden ownership, complexity, scale, initiative, leadership, and impact.
3. Ask only clarifications that can materially strengthen or validate a claim.
4. Convert the answer into professional English CV language.
5. Use current international IT terminology.
6. Remove repetition, weak phrasing, irrelevant detail, and uncertain tone.
7. Select the strongest truthful interpretation.

The skill must not:

- add a technology because it appears in a vacancy;
- convert team participation into sole authorship;
- inflate seniority or ownership;
- alter official dates;
- conceal gaps with false entries;
- convert approximate outcomes into precise metrics;
- invent projects, certifications, education, employers, or achievements.

Choose verbs that match actual ownership. Translate technical activity into system, product, team, or business value without requiring the user to write polished bullets.

## CV Content Standard

Use only sections that add value. The default section set is:

1. Name and target professional role.
2. Email, phone, location or time zone.
3. LinkedIn and relevant GitHub, portfolio, or personal site.
4. Optional Professional Summary.
5. Technical Skills grouped by useful categories.
6. Professional Experience in reverse chronological order.
7. Optional Selected Projects.
8. Education.
9. Optional certifications, publications, talks, or awards.

Move Education or Projects upward for junior candidates when they provide stronger evidence. Give certifications more prominence for roles where they are meaningful. Omit Professional Summary when it merely repeats the rest of the CV.

Technical Skills must be compact, truthful, vacancy-relevant, and supported by Experience or Projects where possible. Do not use ratings, progress bars, stars, or arbitrary proficiency percentages. Demonstrate soft skills through evidence rather than unsupported labels.

Each experience bullet should, where evidence permits, contain:

`accurate action verb + individual action + technical context + scale + outcome`

Prefer concise bullets that remain readable during quick scanning. Avoid personal pronouns, clichés, vague adjectives, keyword stuffing, unexplained internal jargon, and repeated AI-like sentence patterns.

## Review Rubric

Assess:

| Criterion | Meaning |
| --- | --- |
| Target fit | Alignment with role, seniority, market, and vacancy |
| Evidence | Skills supported by concrete experience |
| Impact | Outcomes, scale, metrics, or honest proxies |
| Technical depth | Architecture, complexity, tooling, and trade-offs |
| Ownership | Individual contribution, initiative, and leadership |
| Clarity | Concision, precision, organization, and scanability |
| ATS parseability | Standard sections, linear reading order, safe formatting |
| Credibility | Truthfulness and absence of contradictions |
| Consistency | Dates, titles, tense, terminology, and formatting |
| Remote readiness | English communication and distributed-work signals where relevant |

Use qualitative ratings:

- `Strong`
- `Adequate`
- `Needs work`
- `Critical`

A numeric score may be used only as an internal consistency aid. Never present it as a probability of passing ATS or securing an interview.

## Markdown Output Contract

For `REVIEW`, return:

```markdown
# CV Review

## Verdict
...

## Critical issues
...

## Strong evidence
...

## Review rubric
...

## Recommended changes
...

## Missing evidence
...
```

For `CREATE`, `UPDATE`, and `TAILOR`, return:

1. Concise editor's notes covering material changes, excluded assumptions, and open questions.
2. A clean Markdown CV without internal statuses, diagnostics, or unsupported suggestions.

```markdown
## Editor's notes
...

---

# Candidate Name
Target Role

Contact | LinkedIn | GitHub

## Professional Summary
...

## Technical Skills
...

## Professional Experience
...

## Selected Projects
...

## Education
...
```

Omit optional sections when they do not add value.

Explicit approval includes unambiguous statements such as `approved`, `погоджую`, or `можна PDF`. Silence, answers to interview questions, partial praise, or requests for clarification are not approval.

## PDF Contract

Treat the approved Markdown as immutable content input. The renderer may adjust typography, spacing, line breaks, and pagination but must not silently rewrite claims.

PDF workflow:

`APPROVED_MARKDOWN -> NORMALIZE -> GENERATE -> EXTRACT_TEXT -> CONTENT_COMPARE -> RENDER_PNG -> VISUAL_INSPECTION -> FIX_AND_REPEAT -> DELIVER`

The PDF must use:

- one column;
- standard section names;
- selectable text;
- an embedded readable font;
- consistent dates, spacing, and hierarchy;
- clickable textual URLs;
- sufficient contrast;
- no tables, photographs, icons replacing text, skill bars, text boxes, decorative columns, or infographic elements.

Use one or two pages according to evidence density. Do not reduce text to an unreadable size merely to fit one page.

Before delivery, verify:

- all approved names, contacts, employers, roles, dates, and sections are present;
- extracted text follows the correct reading order;
- no approved content was lost or changed;
- no clipped text, overlaps, broken glyphs, or blank pages exist;
- page density and transitions are visually balanced;
- the PDF opens successfully and contains selectable text.

Do not deliver a PDF that fails content or visual verification.

## Error Handling

- Insufficient facts: continue the interview instead of generating generic filler.
- Contradictory dates or claims: show the conflict and request confirmation.
- Missing vacancy: create a strong base CV for the target role.
- Unavailable URL: request pasted content or another source.
- Missing PDF dependency: identify the exact dependency and retain the approved Markdown as a complete interim artifact.
- Failed PDF verification: repair and repeat both text and visual checks before delivery.

## Skill Package

```text
skills/cv-creator-reviewer/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── cv-standard.md
│   ├── interview-guide.md
│   ├── review-rubric.md
│   └── output-contract.md
└── scripts/
    └── render_cv.py
```

Responsibilities:

- `SKILL.md`: triggers, mode routing, state machine, approval gates, truthfulness rules, and reference routing.
- `references/cv-standard.md`: research-grounded IT CV, ATS, privacy, market, and content standard.
- `references/interview-guide.md`: adaptive interview branches and methods for extracting strong evidence from informal input.
- `references/review-rubric.md`: review criteria, severity, and recommendation rules.
- `references/output-contract.md`: Markdown and PDF structure, content rules, and approval semantics.
- `scripts/render_cv.py`: deterministic PDF generation from approved Markdown.
- `agents/openai.yaml`: UI metadata generated from the completed skill.

## Validation Strategy

Skill authoring must follow RED-GREEN-REFACTOR with baseline and forward tests. Validate at least:

1. Creation from terse, poorly written notes.
2. Update of a weak existing IT CV.
3. Tailoring to a vacancy without keyword stuffing.
4. Resistance to requests to fabricate a metric, technology, or level of ownership.
5. Review-only behavior without unauthorized rewriting.
6. Refusal to generate PDF before explicit approval.
7. One-page and two-page PDF generation.
8. Preservation of approved content during rendering.
9. Correct handling of contradictory dates and unavailable sources.
10. Useful behavior when no vacancy is supplied.

Also run the skill package validator, execute the PDF script directly on representative fixtures, extract PDF text, render every page to PNG, and visually inspect the latest output.

## Success Criteria

The skill is successful when it:

- reliably chooses the requested mode;
- interviews adaptively and one question at a time;
- turns informal candidate input into strong professional English;
- finds and surfaces evidence of technical impact and ownership;
- never places unconfirmed facts in the clean CV;
- produces actionable reviews without false ATS guarantees;
- delivers clean Markdown before any PDF;
- requires explicit approval for PDF;
- generates an ATS-safe, visually polished PDF whose text matches the approved Markdown;
- passes package validation and realistic behavior tests.
