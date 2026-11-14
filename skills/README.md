# Authored Skills

Group first-party skills by purpose:

```text
skills/
├── knowledge/
│   ├── obsidian-source-notes/
│   └── obsidian-zettelkasten/
├── engineering/
│   ├── repo-architecture-analyzer/
│   ├── repo-to-obsidian/
│   └── documentation-writer/
├── career/
│   ├── cv-creator-reviewer/
│   └── google-interview-coach/
└── investigations/
    └── slack-issue-investigator/
```

- `knowledge`: reading, source notes and knowledge workflows.
- `engineering`: repository analysis, architecture and software documentation.
- `career`: CVs, interviews and professional preparation.
- `investigations`: issue investigation and evidence gathering.

Add each skill under `skills/<category>/<skill-name>/`. Choose the category by its primary purpose, rather than the application used for its output. Create a new category when its purpose does not fit the existing ones.

Each skill folder contains `SKILL.md` with `name` and `description` in YAML frontmatter, plus its own templates, references, scripts or assets as needed. Category folders are organizational containers and do not contain `SKILL.md`. Keep skill names unchanged when moving categories, and resolve bundled resources relative to each skill folder.
