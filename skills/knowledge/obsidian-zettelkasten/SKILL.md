---
name: obsidian-zettelkasten
description: Use when developing a personal Zettelkasten in Obsidian for learning, revisiting ideas, or connecting knowledge across engineering, management, and other subjects. Applies to guided understanding, permanent notes, drafts, and navigation notes; not source-by-source chapter summaries or codebase documentation.
---

# Obsidian Zettelkasten

Develop connected thoughts the user can understand and use. Organize around ideas and questions, not source outlines. A useful thought need not be an original discovery. Support any subject, including nonengineering topics.

Keep skill instructions in English. Follow the vault/user's note language; propose Ukrainian for a new vault. Preserve identifiers and exact quotations.

## Use existing Obsidian skills

Delegate mechanics to the same capability set as `obsidian-source-notes`, from [obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills). Load only applicable skills before using their capabilities.

| Skill | Use here |
| --- | --- |
| `obsidian-markdown` | Every note: properties, wikilinks, aliases, block references, embeds, callouts, footnotes, math and Mermaid. |
| `obsidian-cli` | Running vault search, reading, backlinks, properties, tasks and note operations. Prefer rename/move commands for link updates; inspect output as well as exit status. |
| `defuddle` | Read HTML sources as clean Markdown and retain metadata/locators. Read raw Markdown directly; use appropriate readers for PDFs and other formats. |
| `knap` | Structured JSON/CSV imports or repeated template rendering when useful. Inspect syntax, preview destinations/collisions, use stable record identity and preserve user edits on reruns. |
| `obsidian-bases` | Requested or useful draft, unresolved-question, source and review views. Reuse existing Bases and actual properties. |
| `json-canvas` | Requested visual maps of real notes and relationships. Validate node/edge IDs and file paths; label relationships. |
| `obsidian-headless` | Explicitly requested Sync/Publish without the desktop only. Never substitute it for a missing note-editing API. |

If a required skill/tool is unavailable, explain the missing capability and continue through supported tools when faithful. Local filesystem editing is valid without a running desktop; use `obsidian-markdown` and preserve links. Do not silently install dependencies or claim unavailable commands ran. Ordinary note work does not require Bases, Canvas, imports, Sync or Publish.

## Resolve context

Identify the intended vault root; read its instructions, representative notes, maps, naming and properties. Ask only when the target is ambiguous. Read existing style evidence; do not assume memory across sessions. Adapt to conventions without reorganizing the vault.

Read [note conventions](references/notes.md) before note creation, revision or vault setup; [workflows](references/workflows.md) for learning sessions and review; [style calibration](references/style-calibration.md) when selecting a mode or recording style evidence. Resolve bundled paths relative to this skill.

## Mode and approval contract

**Guided mode is the default.** Obtain the user's own explanation before composing a note. Compare it with source evidence, correct misunderstandings and preserve their explanatory logic and useful wording. Discuss a central misconception before finalizing its replacement explanation. If they cannot explain yet, help investigate; do not manufacture their understanding.

**Direct mode is gated.** Require at least 10 distinct accepted notes based on the user's own explanations, sufficient style coverage, and an accepted trial note. Generated notes do not count. Propose the first trial after the other conditions are met. Select 3–5 relevant accepted human-grounded references; return to guided work when coverage is insufficient.

**Both modes require a short proposal before writing.** List candidate thoughts, create/update/draft actions, reasons, intended connections and substantive corrections. Include supporting map/source/profile changes. Wait for discussion and approval of this concrete list. Produce full texts and write only the approved scope afterward. Further notes or materially different changes return to the proposal. Existing explicit approval of the same concrete changes remains valid.

## Note quality and completion

- Search for the idea before creating it. Extend existing thoughts where appropriate; split only independently useful ideas.
- Keep explanations self-contained. Add examples, limits and retrieval questions when useful; remove empty sections.
- Distinguish sourced claims, observations, interpretations and hypotheses. Keep known locators and material version/experimental context; never invent provenance or treat model output as verified evidence.
- Explain meaningful direct links. Create navigation notes as useful clusters or routes emerge. No compulsory parents, fixed subject taxonomy or link quota.
- Link only existing targets or targets created in the same approved operation. Preserve IDs, user contributions, aliases and block references.
- Graph size reflects incoming references, not truth or mastery. Edges show links, not causality; explain relationships in text.
- Verify changed files, schema, new ID uniqueness, link targets and affected backlinks. IDs do not make filename-based links rename-safe; defer a rename if link preservation cannot be verified.
- Report changes, remaining questions and source-access limitations. Saving a note does not establish understanding.

## Boundaries

Use `obsidian-source-notes` for source-structured reading records; use this skill for the personal idea network. Do not import its chapter layout or automatically mirror notes between vaults. Repository entity/API documentation belongs to repository documentation skills. Graph/plugin configuration changes are separate proposed work, not automatic setup.
