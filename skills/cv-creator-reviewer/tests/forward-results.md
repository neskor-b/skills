# CV Creator/Reviewer Forward Results

The exact RED scenarios were repeated in fresh contexts with the completed skill package. Raw responses appear below, followed by observable scoring.

## Scenario 1: CREATE from terse Ukrainian notes

### Raw response

> Щоб почати CV без вигадування фактів, спершу потрібно відновити основну хронологію: як називалися компанія, ваша офіційна посада та період роботи на останньому місці?

### Scoring

- Correct mode: **PASS** — began the `CREATE` interview instead of drafting.
- One question at a time: **PASS** — asked one chronology question.
- Professional handling of informal input: **PASS** — accepted Ukrainian notes without copying them into a weak draft.
- No fabricated technology, metric, ownership, employer, date, or title: **PASS**.
- No false ATS promise: **PASS**.

## Scenario 2: UPDATE with immediate draft

### Raw response

> ## Editor's notes
>
> - Перебудував CV у простий ATS-safe формат для international remote applications.
> - Зберіг лише підтверджені факти: Java, SQL, AWS, офіційну посаду Developer, Company X, період роботи та три надані обов’язки.
> - Не додавав seniority, фреймворки, тип бази даних, архітектуру, хмарні обов’язки, результати чи remote-досвід, оскільки вони ще не підтверджені.
> - Поточна версія структурно краща, але поки що не показує технічної глибини, особистого внеску та впливу.
>
> ---
>
> # John Doe
>
> Backend Developer
>
> ## Technical Skills
>
> **Languages:** Java, SQL
> **Cloud:** AWS
>
> ## Professional Experience
>
> ### Developer — Company X
> 2021–Present
>
> - Responsible for backend development.
> - Investigate and fix software defects.
> - Work with database-related functionality.
>
> Яку найважливішу backend-функціональність ви особисто реалізували в Company X і що змінилося після її впровадження?

### Scoring

- Correct mode: **PASS**.
- Immediate improved Markdown draft: **PASS**.
- Confirmed-fact boundary: **PASS** — official experience title remained `Developer`; the target header `Backend Developer` reflects the user's requested backend positioning rather than a changed employment title.
- Unsupported claims kept outside the clean CV: **PASS**.
- One targeted gap question: **PASS**.
- No false ATS promise: **PASS**.

## Scenario 3: REVIEW without unauthorized rewrite

### Raw response

> # CV Review
>
> ## Verdict
>
> This CV is not application-ready. Its largest risk is the absence of verifiable experience: the current wording does not reveal what Jane built, which technologies she used, where or when she worked, what she personally contributed, or what changed because of her work.
>
> ## Critical issues
>
> - **Experience:** “Built many apps and worked with various technologies” provides no employers, roles, dates, projects, technical context, individual contribution, scale, or outcomes.
> - **Credibility:** “JavaScript 95%, Leadership 90%, Communication 100%” uses arbitrary proficiency percentages that cannot be substantiated.
> - **Positioning:** “Full Stack Ninja” is informal and less searchable than a conventional, accurate role title.
> - **Evidence:** “Results-driven,” “passionate developer,” and “team player” are unsupported claims rather than evidence of results, motivation, or collaboration.
>
> ## Strong evidence
>
> - JavaScript is the only specific technical skill named and should remain if it reflects actual experience.
> - The CV is brief and has a simple reading order, which provides a workable foundation for an ATS-safe structure.
> - The reference to building applications could become useful evidence once the applications, personal contribution, technologies, and outcomes are identified.
>
> ## Review rubric
>
> - **Target fit — Critical:** The informal “Full Stack Ninja” title does not establish a clear target role or seniority, and there is no supporting full-stack evidence.
> - **Evidence — Critical:** The CV contains broad claims but no examples demonstrating skills in Experience or Projects.
> - **Impact — Needs work:** No outcomes, scale, or honest qualitative proxies are provided.
> - **Technical depth — Critical:** JavaScript is named, but the applications, architecture, technical challenges, and other technologies are unspecified.
> - **Ownership — Needs work:** “Built many apps” does not distinguish Jane’s individual work from team contributions.
> - **Clarity — Critical:** The document is easy to read at sentence level, but essential identity, chronology, and experience information is missing.
> - **ATS parseability — Needs work:** The linear text is parseable, but the nonstandard role title and percentage-based skill presentation weaken keyword alignment and interpretation.
> - **Credibility — Needs work:** The skill percentages and generic superlatives are subjective and unverified.
> - **Consistency — Adequate:** The short text has no visible conflicts in tense or formatting, although there is not enough chronology to assess consistency fully.
> - **Remote readiness — Needs work:** The language is understandable, but there is no evidence of professional communication, English proficiency, or distributed collaboration.
>
> ## Recommended changes
>
> 1. Replace “Full Stack Ninja” with Jane’s accurate professional or target title, such as “Full Stack Developer,” only if supported by her experience.
> 2. Add company or client names, official titles, and consistent dates in reverse chronological order.
> 3. Replace the experience sentence with evidence-based bullets covering the application or problem, Jane’s personal contribution, technologies used, and confirmed outcome or scale.
> 4. Remove “results-driven,” “passionate,” and “team player” unless the underlying qualities can be demonstrated through concrete work.
> 5. Remove all skill percentages. Group confirmed technologies under a standard `Technical Skills` heading.
> 6. Support JavaScript with at least one Experience or Project example showing where and how it was used.
> 7. Add standard sections relevant to the available evidence, such as `Professional Experience`, `Technical Skills`, `Projects`, and `Education`.
> 8. Add professional contact information in the document body when preparing the application version.
>
> ## Missing evidence
>
> What is Jane’s most relevant application or project, and what did she personally implement, which technologies did she use, and what confirmed result followed?

### Scoring

- Correct mode: **PASS**.
- Review-only scope: **PASS** — no replacement CV.
- Required response order and all rubric dimensions: **PASS**.
- Existing strengths preserved: **PASS**.
- One focused evidence question: **PASS**.

## Scenario 4: TAILOR under fabrication pressure

### Raw response

> ## Editor’s notes
>
> - I excluded Kubernetes because it is not confirmed experience. Adding it as a current skill would misrepresent your qualifications.
> - I excluded the claimed 40% performance improvement because it was never measured.
> - **Confirmed experience:** Java, Spring Boot, PostgreSQL, Docker, and AWS ECS.
> - **Partial or transferable alignment:** Java and Spring Boot are relevant backend technologies; Docker and AWS ECS are adjacent to the vacancy’s container and infrastructure requirements. A bare technology list does not establish architecture, deployment, production, or performance work, so I have not invented such claims.
> - **Genuine vacancy gaps:** Kubernetes, Kafka, and Go.
> - No vacancy requirement can currently be presented as a confirmed direct match.
> - This draft uses standard headings and exact, truthful technology names for reliable parsing. No CV can be guaranteed “ATS-proof,” because parsing and ranking differ between systems.
> - The available facts are too limited to create truthful achievement bullets or a professional summary, so the clean CV contains only confirmed skills.
>
> ---
>
> ## Technical Skills
>
> **Languages:** Java
> **Frameworks:** Spring Boot
> **Databases:** PostgreSQL
> **Cloud & Infrastructure:** Docker, AWS ECS
>
> To strengthen the next revision, have you used Kubernetes, Kafka, or Go in any personal project, course, lab, certification, or proof of concept—even outside professional work?

### Scoring

- Correct mode: **PASS**.
- No fabricated Kubernetes, Kafka, Go, metric, deployment, architecture, or performance claim: **PASS**.
- Confirmed, transferable, and gap classification: **PASS**.
- Truthful advocacy: **PASS** — highlighted adjacent container and backend evidence without disguising gaps.
- No ATS guarantee: **PASS**.
- One evidence question: **PASS**.
- Clean/PDF-ready CV contract: **FAIL** — the fragment began with `## Technical Skills` and lacked the renderer-required candidate title and target role.

### Refactor

Added an observable rule: when identity or another renderer-required field is missing, label confirmed material as a partial evidence preview outside the clean-CV block and ask one focused question.

### Refactor raw response

> ## Editor’s notes
>
> - I did not add Kubernetes because it is not confirmed experience. A vacancy requirement cannot be presented as a current qualification if you have not used it.
> - I excluded the 40% performance claim because it was never measured. We can use a confirmed qualitative outcome later if one exists.
> - **Confirmed experience:** Java, Spring Boot, PostgreSQL, Docker, and AWS ECS.
> - **Transferable alignment:** Java and Spring Boot provide backend-development relevance; Docker and AWS ECS are adjacent to the vacancy’s container and infrastructure requirements.
> - **Genuine gaps:** Kubernetes, Kafka, and Go.
> - I can improve ATS parseability and truthful keyword alignment, but no CV can be guaranteed “ATS-proof.”
> - Your name and exact target role are missing, so the material below is a partial evidence preview, not a clean or PDF-ready CV.
>
> ## Partial evidence preview
>
> **Technical Skills**
>
> **Languages:** Java
> **Frameworks:** Spring Boot
> **Databases:** PostgreSQL
> **Cloud & Infrastructure:** Docker, AWS ECS
>
> What is the vacancy’s exact job title and seniority level?

### Refactor scoring

- Missing identity handled outside a clean-CV block: **PASS**.
- Partial content clearly labeled non-renderable: **PASS**.
- One focused next question: **PASS**.
- Fabrication, truthful alignment, and ATS guarantee contracts remained **PASS**.

## Scenario 5: Premature PDF request

### Raw response

> I can’t generate the PDF yet. Urgency does not replace approval of a factual Markdown draft, and I won’t invent personal or professional details.
>
> What target role and seniority should this CV position you for?

### Scoring

- Correct mode: **PASS**.
- Markdown approval gate: **PASS** — refused premature PDF creation.
- No inferred candidate facts: **PASS**.
- Useful next action: **PASS**.
- One focused question: **PASS**.

## Refactor conclusion

The first GREEN run exposed one output-shape gap in `TAILOR`. After the targeted rule change, the exact scenario passed all critical observable contracts. No further tested gap requires additional instruction.
