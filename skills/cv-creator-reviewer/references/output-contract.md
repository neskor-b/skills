# CV Output Contract

## Draft delivery

For `CREATE`, `UPDATE`, and `TAILOR`, return two distinct parts:

1. Concise editor's notes.
2. A clean Markdown CV.

Use editor's notes for:

- material editorial decisions;
- confirmed strengths surfaced from informal input;
- assumptions or suggested claims deliberately excluded;
- remaining evidence gaps;
- vacancy gaps that must not be disguised.

Never put evidence statuses, diagnostics, placeholders, questions, or unsupported suggestions inside the clean CV.

## Clean Markdown shape

Use the applicable subset:

```markdown
## Editor's notes

- ...

---

# Candidate Name
Target Role

email@example.com | +00 000 000 000 | Location
LinkedIn URL | GitHub URL | Portfolio URL

## Professional Summary

...

## Technical Skills

**Languages:** ...
**Frameworks:** ...

## Professional Experience

### Official Role — Company
Location or Remote | Mon YYYY–Present

- ...

## Selected Projects

### Project Name
URL

- ...

## Education

**Degree — Institution** | Year

## Certifications

- ...
```

Omit optional sections and empty contact fields. Do not print placeholder brackets.

Use official titles in experience entries. A clarified market-facing title may appear only when explicitly confirmed and must not misrepresent seniority.

## Approval gate

Treat the current Markdown as approved only after an unambiguous statement such as:

- `approved`;
- `погоджую`;
- `можна PDF`;
- another explicit statement that the shown content is final and PDF generation may begin.

These are not approval:

- silence or absence of objections;
- praise such as “looks good” when PDF was not requested;
- an answer to an interview question;
- a request for changes or clarification;
- urgency or an instruction to skip review;
- approval of an earlier draft after a material revision.

After any material content change, obtain approval of the revised Markdown.

## Immutable PDF input

Freeze the clean approved Markdown as the content source. Rendering may change:

- typography;
- spacing;
- line wrapping;
- page breaks;
- link presentation without changing visible link text.

Rendering must not change:

- claims or wording;
- names, titles, employers, dates, or metrics;
- section selection or order;
- technologies or qualifications.

Use `scripts/render_cv.py INPUT.md OUTPUT.pdf` only after approval. Pass the clean CV, not editor's notes.

## PDF presentation

Require:

- A4, one column, selectable text;
- standard section hierarchy;
- embedded readable font;
- consistent spacing and dates;
- sufficient contrast;
- clickable textual URLs;
- ordinary bullets;
- one or two readable pages based on evidence density.

Reject:

- tables and multiple columns;
- photos, icons that replace text, and infographic elements;
- text boxes, skill bars, and proficiency charts;
- important content in headers or footers;
- image-only output;
- body text below 9.5 pt merely to force one page.

## Verification

Before delivery:

1. Reopen the PDF.
2. Extract its text.
3. Confirm every approved visible text block is present in the correct order, allowing only whitespace normalization.
4. Confirm names, contacts, employers, roles, dates, metrics, and URLs.
5. Render every page to PNG.
6. Inspect for clipped text, overlaps, broken glyphs, blank pages, awkward section splits, weak hierarchy, excessive density, and unreadable URLs.
7. Correct defects and repeat text and visual checks.

Do not deliver the PDF until both content and visual verification pass.

## Failure handling

- Missing critical facts: continue the interview rather than add filler.
- Contradictory facts: present the conflict and request confirmation.
- No vacancy: create a strong base CV for the target role.
- Unavailable source URL: request pasted content or another source.
- Missing PDF dependency: name it precisely and retain the approved Markdown as the complete interim result.
- Failed text or visual verification: repair and rerun; do not hand off the defective PDF.

