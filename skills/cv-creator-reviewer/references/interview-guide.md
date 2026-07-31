# Adaptive CV Interview Guide

## Interview contract

Ask exactly one meaningful question per turn. Make the next question depend on the previous answer. Do not repeat information already present and do not make the candidate complete a long questionnaire.

Accept answers in the candidate's own words and language. Extract facts, recognize hidden value, and rewrite professionally; never require the candidate to formulate polished English bullets.

Stop when critical sections contain enough confirmed evidence to produce or revise a strong draft. Do not exhaustively interrogate optional sections.

## Question priority

Use the first applicable branch:

1. If target role or seniority is missing, ask for it.
2. If chronology, employer, or official role is missing for material experience, ask for that fact.
3. If a job description exists but has not been mapped, extract its requirements before asking about experience.
4. If an experience entry lacks the candidate's personal contribution, ask what they personally proposed, implemented, decided, owned, or reviewed.
5. If the answer is only a responsibility, ask what problem it addressed or what changed afterward.
6. If an outcome is qualitative, ask about scale or one honest proxy.
7. If a metric appears, ask whether it is exact or approximate when that distinction is unclear.
8. If ownership language is ambiguous, ask who proposed the approach, who implemented it, and who made the final decision—but ask only the single most important ownership distinction first.
9. If a critical technical skill lacks evidence, ask where and how it was applied.
10. Ask about contact details, education, languages, or optional material only when the core evidence is sufficient or the target role makes it material.

When the candidate says no metric exists, stop pressing for a number. Use a confirmed qualitative result or proxy.

## Experience evidence

For each relevant role, gather only what is needed from:

- company, official title, and dates;
- product, domain, users, and system scale;
- individual responsibility and ownership;
- technologies actually used;
- technical challenge, approach, and trade-offs;
- reliability, latency, throughput, cost, delivery, security, quality, or business result;
- mentoring, review, cross-team collaboration, and distributed-work evidence.

Do not infer one category from another. A technology list does not prove architecture, deployment, production operation, collaboration, or measurable impact.

## Truthful advocacy

Translate informal input into the strongest supported professional meaning:

- “допомагав джунам” may signal mentoring, code review, onboarding, or technical guidance; ask which occurred.
- “щось оптимізував у базі” may signal query tuning, indexing, schema changes, caching, or data-access redesign; ask what changed.
- “займався платежами” may signal provider integration, transaction flows, reconciliation, fraud, compliance, or reliability; ask for the actual responsibility.
- “робив API” may signal design, implementation, integration, performance, documentation, or ownership; ask for the most material contribution.

Use verbs that match the confirmed ownership:

- `led`, `owned`, `architected`, or `spearheaded` only for leadership or decision ownership;
- `designed` only for actual design responsibility;
- `implemented`, `developed`, or `built` for direct creation;
- `contributed to`, `supported`, or `collaborated on` for partial contribution.

## Transformation example

Informal input:

> На старому платіжному сервісі все падало. Трохи переписав і додав тести.

Ask:

> What part did you personally change, and what confirmed reliability result followed—for example fewer incidents, safer releases, or adoption by other teams?

If the candidate confirms ownership and exact incident counts:

> Stabilized a legacy payment service by refactoring failure-prone components and adding integration coverage, reducing recurring production incidents from 5–6 per month to fewer than one.

If no numeric metric exists but the qualitative result is confirmed:

> Improved the reliability of a legacy payment service by refactoring failure-prone components and adding integration coverage for critical transaction flows.

Both versions advocate for the candidate. Only the first may contain the confirmed numbers.

## Common mistakes

| Mistake | Correction |
| --- | --- |
| Copy the candidate's grammar into the CV | Extract the facts and rewrite in professional English. |
| Return a long intake questionnaire | Ask one highest-value question and branch from the answer. |
| Demand a metric repeatedly | Accept a confirmed qualitative result or proxy. |
| Add generic “results-driven” language | Show the result or omit the claim. |
| Turn “we” into sole authorship | Clarify the candidate's individual contribution. |
| Treat a skill list as proof of work | Ask where and how the skill was used. |
| Translate internal jargon literally | Translate it into standard market terminology after confirming meaning. |
| Offer a menu of fashionable technologies | Ask an open evidence question without seeding unsupported answers. |

