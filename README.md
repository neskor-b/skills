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

For installation instructions, see the upstream repository: <https://github.com/kepano/obsidian-skills>.

## Notes

- `repo-to-obsidian` also depends on the local `repo-architecture-analyzer` skill, which is already included in this repository.
- `skills-lock.json` also contains `defuddle` and `json-canvas` from the same repository, but the current local skills do not directly depend on them.
