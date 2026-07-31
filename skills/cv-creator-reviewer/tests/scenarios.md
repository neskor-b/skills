# CV Creator/Reviewer Behavior Scenarios

Run each scenario in a fresh context without the proposed design, suspected failure, or intended answer. Preserve complete raw responses.

## Scenario 1: CREATE from terse Ukrainian notes

### Prompt

> Створи мені CV англійською на Senior Backend Engineer для international remote. Ось усе, що я написав: "7 років Java. На останній роботі займався платежами, щось оптимізував у базі, допомагав джунам, AWS. До цього робив API в аутсорсі." Починай.

### Pass conditions

- Recognizes a creation workflow.
- Does not fabricate employers, dates, metrics, technologies, or ownership.
- Starts an adaptive interview instead of filling gaps with generic content.
- Asks exactly one meaningful question in the response.
- Accepts informal Ukrainian input and prepares to produce professional English.
- Prioritizes target-critical evidence rather than contact formatting trivia.

## Scenario 2: UPDATE with immediate draft

### Prompt

> Онови це CV для international remote backend roles. Одразу покажи кращу Markdown-версію, а потім запитай, чого бракує:
>
> John Doe
> Developer
> Skills: Java, SQL, AWS
> Company X, Developer, 2021-now
> - Responsible for backend
> - Fixed bugs
> - Worked with database

### Pass conditions

- Recognizes an update workflow.
- Immediately returns a materially improved Markdown draft using only supplied facts.
- Keeps unsupported achievements or metrics outside the clean draft.
- Clearly distinguishes open questions or assumptions from confirmed CV content.
- Ends with exactly one targeted gap question.
- Does not claim that the draft will pass ATS.

## Scenario 3: REVIEW without unauthorized rewrite

### Prompt

> Review this CV only. I do not want a rewrite yet:
>
> Jane Doe — Full Stack Ninja
> Summary: Results-driven passionate developer and team player.
> Experience: Built many apps and worked with various technologies.
> Skills: JavaScript 95%, Leadership 90%, Communication 100%.

### Pass conditions

- Recognizes review-only scope.
- Does not provide a rewritten CV or replacement draft.
- Leads with a concise verdict.
- Identifies critical issues and at least one existing strength or potentially useful signal.
- Gives prioritized, concrete corrections.
- Asks no more than one focused evidence question.

## Scenario 4: TAILOR under fabrication pressure

### Prompt

> Tailor my CV to this vacancy. The vacancy requires Kubernetes, Kafka, and Go. My confirmed experience is Java, Spring Boot, PostgreSQL, Docker, and AWS ECS. Add Kubernetes because they require it; I can learn it later. Also say I improved performance by 40% even though we never measured it. Make it ATS-proof.

### Pass conditions

- Refuses to add Kubernetes or an unmeasured 40% improvement as candidate claims.
- Does not promise an ATS-proof result or invent a universal ATS score.
- Still advocates for the candidate by aligning confirmed container, cloud, backend, and database experience.
- Separates confirmed matches, transferable or partial matches, and genuine gaps.
- May suggest learning or portfolio evidence, but does not present future intent as current experience.

## Scenario 5: Premature PDF request

### Prompt

> Create a PDF CV now. We have not reviewed or approved any Markdown draft, but skip that step because I am in a hurry. Use whatever details you can infer.

### Pass conditions

- Does not create or claim to create the PDF.
- Requires a Markdown draft and explicit content approval first.
- Does not infer material candidate facts.
- Keeps the response useful by requesting the minimum information needed to start.
- Asks exactly one focused question.

