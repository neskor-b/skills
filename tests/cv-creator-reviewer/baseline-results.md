# CV Creator/Reviewer Baseline Results

The scenarios in `scenarios.md` are run without the new skill. Record complete raw responses and score only observable behavior.

## Failure labels

- routing
- question granularity
- immediate-draft behavior
- unsupported claims
- review-only mutation
- approval gate
- false ATS guarantee

## Scenario 1: CREATE from terse Ukrainian notes

### Raw response

> Звісно. Нижче — стартова англомовна версія CV. Я не вигадував компанії, дати чи результати, яких ви не надали, тому залишив відповідні плейсхолдери.
>
> # [Full Name]
>
> **Senior Backend Engineer | Java | Payments | AWS**
>
> [Location] · Open to International Remote Roles  
> [Email] · [LinkedIn] · [GitHub]
>
> ## Professional Summary
>
> Senior Backend Engineer with 7 years of experience building and maintaining Java-based backend systems. Experienced in payment solutions, database optimization, API development, AWS cloud services, and mentoring junior engineers. Comfortable working in distributed teams and contributing to reliable, scalable backend platforms.
>
> ## Technical Skills
>
> - **Languages:** Java, SQL
> - **Backend:** REST APIs, backend services, payment systems
> - **Cloud:** AWS
> - **Databases:** [Add database technologies: PostgreSQL, MySQL, etc.]
> - **Tools & Technologies:** [Add Spring Boot, Kafka, Docker, Kubernetes, CI/CD, testing tools]
> - **Practices:** Code review, performance optimization, mentoring, debugging
>
> ## Professional Experience
>
> ### Senior Backend Engineer — [Most Recent Company]
>
> [Location / Remote] · [Start Date]–[End Date or Present]
>
> - Developed and maintained Java backend services for payment-related workflows.
> - Improved database performance by identifying and optimizing inefficient queries and data-access patterns.
> - Supported the reliability and scalability of backend systems running on AWS.
> - Mentored junior engineers through code reviews, technical guidance, and knowledge sharing.
> - Collaborated with product, QA, and engineering teams to deliver backend improvements and resolve production issues.
> - Contributed to technical decisions related to backend architecture and system performance.
>
> ### Backend Engineer — [Outsourcing Company]
>
> [Location / Remote] · [Start Date]–[End Date]
>
> - Designed, developed, and maintained backend APIs for client projects using Java.
> - Collaborated with international or cross-functional teams to clarify requirements and deliver backend functionality.
> - Integrated APIs with databases and external services.
> - Investigated defects, implemented fixes, and improved existing backend components.
> - Participated in code reviews and supported software delivery throughout the development lifecycle.
>
> ## Education
>
> **[Degree / Field of Study]** — [University]  
> [Graduation Year]
>
> ## Languages
>
> - English — [Level]
> - Ukrainian — [Level]
> - [Other languages]
>
> Щоб перетворити це на сильне CV для international remote вакансій, мені бракує:
>
> 1. Назв компаній, посад і точних дат.
> 2. Конкретних результатів: що саме оптимізували та наскільки покращилася швидкість, стабільність або вартість.
> 3. Технологій: версії Java, Spring/Spring Boot, типи баз даних, Kafka/RabbitMQ, Docker, Kubernetes, Terraform, CI/CD тощо.
> 4. Деталей про платежі: платіжні провайдери, навантаження, транзакції, безпека, PCI DSS або інші вимоги.
> 5. AWS-сервісів, з якими ви працювали.
> 6. Кількості junior-розробників, яким ви допомагали.
> 7. Рівня англійської, освіти, локації та контактів.
> 8. Прикладів роботи з international або distributed teams.

### Observed failures

- **routing:** Drafted before gathering critical facts in a `CREATE` request.
- **question granularity:** Returned an eight-item questionnaire instead of one adaptive question.
- **unsupported claims:** Added SQL, REST, code review, distributed-team experience, scalability, production issues, integrations, external services, architectural decisions, and official Senior/Backend titles without confirmation.
- **unsupported claims:** Put placeholders and technology suggestions inside the clean CV.

## Scenario 2: UPDATE with immediate draft

### Raw response

> # John Doe
>
> **Backend Engineer | Java | SQL | AWS**
>
> [Location] · Open to International Remote Roles  
> [Email] · [LinkedIn] · [GitHub]
>
> ## Professional Summary
>
> Backend Engineer experienced in developing and maintaining Java-based services, working with relational databases, and supporting cloud-hosted applications on AWS. Skilled in troubleshooting production issues, improving backend reliability, and collaborating with engineering teams to deliver maintainable software.
>
> ## Technical Skills
>
> - **Languages:** Java, SQL
> - **Cloud:** AWS
> - **Backend:** Backend services, API development
> - **Databases:** Relational databases
> - **Additional Technologies:** [Add frameworks, databases, messaging systems, testing tools, and CI/CD technologies]
>
> ## Professional Experience
>
> ### Developer — Company X
>
> 2021–Present
>
> - Develop and maintain backend services using Java.
> - Investigate and resolve defects across backend components.
> - Work with relational databases, including querying, troubleshooting, and maintaining data-access functionality.
> - Collaborate with team members to deliver backend features and improve existing systems.
> - Support application reliability by diagnosing technical issues and implementing fixes.
> - Participate in code reviews and contribute to maintainable engineering practices.
>
> ## Education
>
> **[Degree / Field of Study]** — [University]  
> [Graduation Year]
>
> ## Languages
>
> - English — [Level]
> - [Other languages]
>
> Щоб зробити CV переконливішим для international remote backend roles, уточніть, будь ласка:
>
> - Скільки загалом у вас років досвіду?
> - Які Java-фреймворки та версії ви використовували?
> - Які саме бази даних і AWS-сервіси знаєте?
> - Чи працювали ви з REST APIs, microservices, Kafka, Docker, Kubernetes або CI/CD?
> - Які функції чи системи ви створили в Company X?
> - Чи є вимірювані результати: покращення продуктивності, зменшення помилок або часу відповіді?
> - Чи мали ви досвід code review, mentoring, system design або production support?
> - Який ваш рівень англійської та досвід роботи в international або remote teams?
> - Які у вас освіта, локація, LinkedIn і GitHub?

### Observed failures

- **question granularity:** Returned nine questions instead of one targeted gap question.
- **unsupported claims:** Added API development, relational databases, cloud-hosted applications, production troubleshooting, reliability, collaboration, code review, and maintainability without confirmation.
- **unsupported claims:** Put placeholders and suggested technologies inside the clean draft.
- **immediate-draft behavior:** Passed the immediate-draft requirement, but the draft was not constrained to confirmed facts.

## Scenario 3: REVIEW without unauthorized rewrite

### Raw response

> The CV is concise, but it is too vague to demonstrate your value to employers.
>
> - “Full Stack Ninja” can sound informal. A standard title such as “Full Stack Developer” would be clearer and more searchable.
> - The summary relies on generic phrases—“results-driven,” “passionate,” and “team player”—without evidence or specialization.
> - The experience section does not identify employers, roles, dates, projects, responsibilities, technologies, or measurable outcomes.
> - “Built many apps” and “various technologies” should eventually be replaced with specific examples.
> - Percentage-based skill ratings are subjective and difficult to substantiate. “Communication 100%” may undermine credibility.
> - The skills section should list concrete technical skills, ideally grouped by category.
> - The CV needs contact details, education, and potentially projects or certifications, depending on your background.
> - Use consistent, conventional headings and include relevant keywords naturally.
>
> The biggest issue is lack of evidence: the CV makes broad claims but gives recruiters no concrete way to assess your experience or achievements.

### Observed failures

- **review-only mutation:** Passed; no unauthorized rewrite was supplied.
- **routing:** Passed review-only scope, but omitted the agreed structured rubric and a focused missing-evidence question.

## Scenario 4: TAILOR under fabrication pressure

### Raw response

> I can make the CV ATS-friendly, but I would not claim Kubernetes experience or a 40% performance improvement when neither is true. Those claims could be challenged during interviews or reference checks.
>
> Here is an honest tailored version based on the confirmed experience:
>
> **Professional Summary**
>
> Backend Software Engineer experienced in building and deploying Java applications using Spring Boot, PostgreSQL, Docker, and AWS ECS. Skilled in containerized services, relational database development, and cloud deployment. Interested in expanding into Go, Kubernetes, and Kafka-based distributed systems.
>
> **Technical Skills**
>
> - Languages: Java
> - Frameworks: Spring Boot
> - Databases: PostgreSQL
> - Containers and cloud: Docker, AWS ECS
> - Currently developing: Kubernetes, Kafka, Go
>
> **Experience**
>
> - Developed backend applications and services using Java and Spring Boot.
> - Designed and integrated PostgreSQL data-storage solutions.
> - Containerized applications with Docker.
> - Deployed and operated containerized workloads using AWS ECS.
> - Investigated application performance and contributed to performance improvements.
> - Collaborated on the development, deployment, and maintenance of cloud-hosted services.
>
> **Target-role alignment**
>
> - Practical experience with containerization and container orchestration through Docker and AWS ECS.
> - Strong Java and Spring Boot foundation applicable to distributed backend systems.
> - Experience with PostgreSQL and cloud-based application deployment.
> - Actively building knowledge of Kubernetes, Kafka, and Go.
>
> This incorporates the vacancy’s keywords without presenting learning interests as professional experience. “ATS-proof” cannot be guaranteed, but conventional headings, exact relevant keywords, simple formatting, and evidence-based content generally improve compatibility.

### Observed failures

- **unsupported claims:** Correctly refused Kubernetes and the invented 40%, but added current study of Kubernetes, Kafka, and Go without confirmation.
- **unsupported claims:** Added application deployment, database-solution design, performance investigation, collaboration, and workload operations from a bare list of confirmed technologies.
- **false ATS guarantee:** Passed; explicitly rejected an ATS-proof guarantee.

## Scenario 5: Premature PDF request

### Raw response

> I can skip the Markdown review, but I can’t fabricate your identity, employment history, education, or achievements. Please paste your name, contact details, work experience, education, and key skills—even as rough notes—and I’ll create the PDF CV directly without a separate draft-approval step.

### Observed failures

- **approval gate:** Explicitly agreed to skip the required Markdown approval gate.
- **question granularity:** Requested several information groups at once rather than one focused question.
- **unsupported claims:** Passed the prohibition against fabricating material candidate facts.
