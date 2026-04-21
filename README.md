# Local Obsidian Skills

This repository contains my local skills for working with Obsidian and repository documentation.

## Local Skills

| Skill | Purpose | External dependencies |
| --- | --- | --- |
| `obsidian-source-notes` | Turns programming sources into linked notes for Obsidian | `obsidian-markdown`, `obsidian-cli`, `obsidian-bases` |
| `repo-architecture-analyzer` | Analyzes a repository architecture and builds a structured entity model | None |
| `repo-to-obsidian` | Generates a linked Obsidian vault from a code repository | `repo-architecture-analyzer` (local), `obsidian-markdown` |

## Required External Skills

Some local skills directly reference skills from [`kepano/obsidian-skills`](https://github.com/kepano/obsidian-skills/tree/main), so those dependencies need to be installed separately.

| Skill | Used by | Repository |
| --- | --- | --- |
| `obsidian-markdown` | `obsidian-source-notes`, `repo-to-obsidian` | <https://github.com/kepano/obsidian-skills/tree/main/skills/obsidian-markdown> |
| `obsidian-cli` | `obsidian-source-notes` | <https://github.com/kepano/obsidian-skills/tree/main/skills/obsidian-cli> |
| `obsidian-bases` | `obsidian-source-notes` | <https://github.com/kepano/obsidian-skills/tree/main/skills/obsidian-bases> |

`skills-lock.json` in this repository also shows that the installed external skills come from `git@github.com:kepano/obsidian-skills.git`.

## Installation

Use the [`vercel-labs/skills`](https://github.com/vercel-labs/skills) CLI to install skills from this repository and its external dependencies.

### 1. Install the local skills from this repository

From the repository root, you can install selected local skills via the current directory path:

```bash
npx skills add . \
  --agent codex \
  --skill obsidian-source-notes \
  --skill repo-architecture-analyzer \
  --skill repo-to-obsidian
```

If you want to see what this repository exposes before installing anything:

```bash
npx skills add . --list
```

### 2. Inspect the upstream skills

```bash
npx skills add kepano/obsidian-skills --list
```

### 3. Install the required external skills

For Codex, install the skills that this repository depends on:

```bash
npx skills add kepano/obsidian-skills \
  --agent codex \
  --skill obsidian-markdown \
  --skill obsidian-cli \
  --skill obsidian-bases
```

If you want those skills available across all projects, add `--global`:

```bash
npx skills add kepano/obsidian-skills \
  --agent codex \
  --global \
  --skill obsidian-markdown \
  --skill obsidian-cli \
  --skill obsidian-bases
```

### 4. Install the optional skills recorded in `skills-lock.json`

`skills-lock.json` also contains `defuddle` and `json-canvas`. They are not required by the current local skills, but you can install them from the same upstream repository:

```bash
npx skills add kepano/obsidian-skills \
  --agent codex \
  --skill defuddle \
  --skill json-canvas
```

### Notes on `vercel-labs/skills`

- `npx skills add <owner>/<repo>` accepts GitHub shorthand, full Git URLs, and local paths.
- Use `--list` to preview available skills without installing anything.
- By default, installation is project-scoped; `--global` installs to your user-level agent directory.
- Use `--copy` if you prefer copied files over symlinks.

## Notes

- `repo-to-obsidian` also depends on the local `repo-architecture-analyzer` skill, which is already included in this repository.
- `skills-lock.json` also contains `defuddle` and `json-canvas` from the same repository, but the current local skills do not directly depend on them.
