# Local Agent Skills

This repository contains local skills for knowledge management, repository analysis and documentation, and Google Workspace interview coaching.

## Local Skills

| Skill | Purpose | External dependencies |
| --- | --- | --- |
| `obsidian-source-notes` | Turns general and programming sources into linked Ukrainian notes, arguments, code, maps and playbooks | Official Obsidian skills, selected by task (see below) |
| `repo-architecture-analyzer` | Analyzes a repository architecture and builds a structured entity model | None |
| `repo-to-obsidian` | Generates a linked Obsidian vault from a code repository | `repo-architecture-analyzer` (local), `obsidian-markdown` |
| `google-interview-coach` | Runs adaptive interviews from Google Sheets and maintains linked Google Docs cheat sheets | `google-drive`, `google-sheets`, `google-docs` |

## External Dependencies

`obsidian-source-notes` delegates format and tool mechanics to the official [obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills) package rather than duplicating them. Load only the skills relevant to the current task.

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

Select the seven skills listed above for the full source-to-notes workflow.

## Notes

- `repo-to-obsidian` also depends on the local `repo-architecture-analyzer` skill, which is already included in this repository.
- Installing skills is separate from enabling CLI tools, Sync, or Publish; ordinary source-note work does not activate remote services.
