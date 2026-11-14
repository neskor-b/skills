# Local Agent Skills

This repository contains local skills for knowledge management, repository analysis and documentation, and Google Workspace interview coaching.

## Local Skills

| Category | Skill | Purpose |
| --- | --- | --- |
| Knowledge | [obsidian-zettelkasten](skills/knowledge/obsidian-zettelkasten/SKILL.md) | Develops a personal idea network through guided learning and calibrated direct authoring |
| Knowledge | [obsidian-source-notes](skills/knowledge/obsidian-source-notes/SKILL.md) | Turns sources into linked Ukrainian notes, arguments, code, maps and playbooks |
| Engineering | [repo-architecture-analyzer](skills/engineering/repo-architecture-analyzer/SKILL.md) | Analyzes repository architecture and builds a structured entity model |
| Engineering | [repo-to-obsidian](skills/engineering/repo-to-obsidian/SKILL.md) | Generates a linked Obsidian vault from a code repository |
| Engineering | [documentation-writer](skills/engineering/documentation-writer/SKILL.md) | Writes software documentation using Diátaxis |
| Career | [cv-creator-reviewer](skills/career/cv-creator-reviewer/SKILL.md) | Creates, reviews and tailors technical CVs |
| Career | [google-interview-coach](skills/career/google-interview-coach/SKILL.md) | Runs adaptive interviews with Google Sheets and Docs |
| Investigations | [slack-issue-investigator](skills/investigations/slack-issue-investigator/SKILL.md) | Investigates issues using Slack context |

Skills are grouped by purpose under `skills/<category>/<skill-name>/`. See [the directory guide](skills/README.md) when adding a skill. Names used for invocation stay unchanged.

## External Dependencies

`obsidian-source-notes` and `obsidian-zettelkasten` delegate format and tool mechanics to the official [obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills) package rather than duplicating them. Load only the skills relevant to the current task.

| Skill | Role in source notes |
| --- | --- |
| `obsidian-markdown` | Note formatting, properties, links, embeds and block references; also used by `repo-to-obsidian` |
| `obsidian-cli` | Search and operate on a running vault; direct file editing remains available without the desktop |
| `defuddle` | Extract readable web sources and metadata |
| `knap` | Render structured JSON/CSV imports and batches through templates |
| `obsidian-bases` | Source, concept and inbox review views |
| `json-canvas` | Visual maps connecting actual notes |
| `obsidian-headless` | Explicitly requested Sync/Publish workflows only |

Install the Obsidian package for full capability. Executables are needed only for the corresponding task. The skills live upstream under `plugins/obsidian/skills/`.

For live use of `google-interview-coach`, connect the Google Drive plugin.

`skills-lock.json` records the existing installed dependencies and their hashes. Its historical `kepano/obsidian-skills` source URLs are retained until those dependencies are actually updated; they do not attest to an installation of the newer official package.

## Installation

Use the [`vercel-labs/skills`](https://github.com/vercel-labs/skills) CLI to install skills from this repository and its external dependencies.

### Local skills from this repository

From the repository root:

```bash
npx skills add .
```

### Required external skills

```bash
npx skills add https://github.com/obsidianmd/obsidian-skills
```

Both knowledge skills use the seven capabilities listed above, loading only what a task needs. Headless is for explicitly requested Sync/Publish only; it is not required for local note work. Select the skills needed for your workflow.

## Notes

- `repo-to-obsidian` also depends on the local `repo-architecture-analyzer` skill, which is already included in this repository.
- Installing skills is separate from enabling CLI tools, Sync, or Publish; ordinary source-note work does not activate remote services.
