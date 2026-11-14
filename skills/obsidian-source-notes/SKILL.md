---
name: obsidian-source-notes
description: Use when turning books, articles, papers, documentation, courses, talks, excerpts, or raw fragments into linked Obsidian source notes, concepts, arguments, code examples, maps, or playbooks. Defaults to Ukrainian notes. Not for documenting repository architecture or general vault administration.
---

# Obsidian Source Notes

Turn source material into traceable, connected notes. Preserve source-specific explanations while developing reusable concepts, arguments, and procedures. Support programming and nontechnical material through one workflow.

Keep these instructions in English. Write notes in Ukrainian unless the user requests another language; preserve code, identifiers, source titles, and verbatim quotations accurately.

## Use the official Obsidian skills

Delegate format and tool mechanics to the skills from [obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills). Load the relevant skill before using its capability, rather than copying its manual here or loading every skill for every request.

| Skill | When and how to use it here |
| --- | --- |
| `obsidian-markdown` | For every note: properties, wikilinks, aliases, block references, embeds, callouts, footnotes, math and Mermaid. Use its references when needed. |
| `obsidian-cli` | For a running Obsidian vault: search, read, backlinks, properties, tasks and note operations. Use its rename/move commands when changing note paths so Obsidian can update links. Check availability and command output, not just exit status. |
| `defuddle` | For HTML articles and documentation: extract clean Markdown and available metadata before summarizing. Fetch raw Markdown directly; use an appropriate reader for PDFs or other formats. Preserve the original URL and location. |
| `knap` | For structured JSON/CSV imports, repeated template rendering, and Defuddle-to-note pipelines. Inspect its syntax and validate/render with real data. Preview batch paths and check collisions before writing. |
| `obsidian-bases` | For requested or useful library views: sources by type, concepts by source, reading status, or inbox review. Reuse an existing Base first; filter using actual properties. |
| `json-canvas` | For requested visual maps of source notes, concepts, arguments, or procedures. Reference existing notes as file nodes, label meaningful relationships, and validate IDs, edges and paths. |
| `obsidian-headless` | Only when the user requests Sync or Publish without the desktop app. It is not a note editing API. Follow its authorization, preview and credential handling guidance. |

Use these capabilities wherever they contribute to the requested result; ordinary note creation does not require a new Base, Canvas, batch pipeline, sync, or publication. A Markdown topic map and a Canvas are complementary: choose based on the requested artifact rather than generating both automatically.

If a required skill or executable is missing, say which capability is unavailable. Continue with supported tools when they can satisfy the request faithfully. Direct filesystem reading/writing is suitable for local notes without a running desktop; use `obsidian-markdown` and preserve links. Do not substitute Headless for missing CLI note commands, silently install tools, or claim unavailable commands ran.

## Resolve context before writing

- Identify the selected vault and its real filesystem root; do not infer it from the active Obsidian window when a different vault was requested. Ask only if the target remains ambiguous.
- Inspect existing instructions, folders, naming, properties and nearby notes. `vault/` below denotes the vault root, not a mandatory literal subfolder. Reuse the actual layout; never reorganize an existing vault merely to fit these defaults.
- Resolve `_templates/...` relative to this skill's directory, not the vault or current directory. Open the matching bundled template before drafting. Vault links and destinations are relative to the selected vault root.
- Inspect the source folder if known. Normalize `source_type`, `source_slug`, and `source_title` from evidence. Supported types include `books`, `articles`, `essays`, `papers`, `docs`, `courses`, `talks`, `interviews`, and `notes`.
- For fragments without stable source identity, create a capture. Retain any known URL, title or locator; leave unknown metadata empty rather than inventing it.

## Workflow

1. Read the supplied material or extract it through the matching tool. Keep a source locator: URL, page, chapter, section, timestamp, or documentation version when available. Distinguish source claims, exact quotations, paraphrase, and your own synthesis.
2. Classify each stable idea using the routing table. One note holds one stable idea; a source or chapter note may organize the ideas of that source segment. Do not split every paragraph or create standalone summaries by default.
3. Search narrowly before reading full notes: current source folder, shared concepts, relevant playbooks, and maps for broader themes. Use filenames, aliases, frontmatter, links and opening summaries to rank matches. Usually inspect the best 3–7; expand only when identity or scope still collides.
4. Extend an existing note when it already represents the idea. Preserve its block IDs, meaningful content, metadata, links and user edits. Check backlinks before a necessary rename or move.
5. Open the matching template and adapt it to the material. Keep relevant sections only; remove instructional placeholders, example links and empty scaffolding. For programming material, include practical rules, explained code, tradeoffs or diagnostic checks where supported. For other material, use appropriate evidence and examples.
6. Write the note in the existing layout or use the defaults below. Add links that improve navigation, provenance or synthesis. Link real targets and existing block IDs; do not leave fictional example targets in output.
7. Promote reusable ideas and update an existing map or view when it improves the requested result. Create supporting artifacts only when useful to the task. Verify the changed files and report what was created or updated, including any source-access limitations.

## Structured imports

For JSON/CSV batches, inspect representative records and map fields to the existing note schema before rendering. Choose a stable source ID, URL or established slug as record identity; do not use row order as identity on reruns. Compare intended destinations with existing notes and within the batch. Update only the imported fields or sections intended by the task, preserving user additions and `created`; do not blindly overwrite a whole existing note with rendered output. Preview and validate a representative render before the batch. If no reliable identity exists, report ambiguous matches rather than merging unrelated records.

Without a running desktop, a necessary rename or move must also update affected vault links and be verified; defer the rename if link preservation cannot be established. Ordinary content updates can keep the original paths.

## Routing and default layout

Use the vault's existing conventions first. When starting a new library, these paths provide consistent defaults:

| Role | Destination under vault root | Template |
| --- | --- | --- |
| Source segment or excerpt | `01-Sources/<type>/<slug>/02-Notes/note-topic.md` | [_templates/source-note.md](_templates/source-note.md) |
| Chapter or substantial course module | `01-Sources/<type>/<slug>/02-Chapters/ch-XX-topic.md` | [_templates/chapter-note.md](_templates/chapter-note.md) |
| Source-local concept | `01-Sources/<type>/<slug>/03-Concepts/concept-topic.md` | [_templates/concept-note.md](_templates/concept-note.md) |
| Source-local argument, model or causal explanation | `01-Sources/<type>/<slug>/04-Arguments/argument-topic.md` | [_templates/argument-note.md](_templates/argument-note.md) |
| Source-local code example | `01-Sources/<type>/<slug>/04-Code/code-topic.md` | [_templates/code-note.md](_templates/code-note.md) |
| Shared concept | `02-Concepts/concept-topic.md` | [_templates/concept-note.md](_templates/concept-note.md) |
| Shared argument or model | `02-Concepts/argument-topic.md` | [_templates/argument-note.md](_templates/argument-note.md) |
| Topic map and synthesis | `03-Maps/map-topic.md` | [_templates/map-note.md](_templates/map-note.md) |
| Procedure, checklist or debugging flow | `04-Playbooks/playbook-topic.md` | [_templates/playbook-note.md](_templates/playbook-note.md) |
| Raw or ambiguous input | `05-Inbox/capture-topic.md` or existing source-local `01-Inbox/` | [_templates/capture-note.md](_templates/capture-note.md) |

Books and chapter-based courses normally use `02-Chapters/`; articles, docs and other short sources normally use `02-Notes/`. Existing page-based courses may use `02-Notes/`: preserve that convention. `04-Arguments/` and `04-Code/` can coexist, but create only the folders needed. Keep filenames short, lowercase and predictable; preserve established filenames instead of renaming for cosmetic consistency.

## Promotion and domain choices

- Keep wording, progression, evidence and code tied to a particular source in that source's folder.
- Promote a concept when it explains a reusable idea independently, even if initially encountered in one source. Preserve links back to supporting source passages.
- Use an argument note when the reasoning chain, mechanism, claim or model matters more than a definition. Record assumptions, evidence, limits and counterarguments; do not present a contested source claim as established fact.
- Use a code note when an implementation example merits its own explanation. Preserve its language, provenance and relationship to concepts; distinguish copied code from adapted examples and do not claim execution without running it.
- Promote an actionable sequence or diagnostic flow into a playbook. Include when to use it, steps, success signals and common failure modes.
- Use maps to connect several existing concepts, arguments, code notes and playbooks. Prefer extending a useful existing map to creating a competing one.
- A capture may later produce several note types. Preserve the original fragment and its provenance when developing it; do not discard raw input automatically.

## Metadata and verification

Follow the existing vault schema and `obsidian-markdown`. Templates are starting structures, not requirements to populate unknown data.

- Source-bound notes: `source_type`, `source_slug`, `source_title`, and known source locator in `source` or the context section.
- Shared concepts and arguments: `scope: shared`, with `sources` links to supporting local notes or passages. Source-local concepts and arguments use `scope: local`.
- Arguments: `claim_status` when useful, such as `working`, `supported` or `contested`.
- Maps: `scope: map`; playbooks: `scope: playbook`; captures: `scope: inbox`.
- Code notes: retain source metadata; record language/version in context when relevant. Preserve code syntax rather than translating identifiers.
- Preserve `created` on updates; use known dates, not invented publication dates.

Before completion, check changed frontmatter, note paths, wikilinks and block references, source fidelity and absence of template examples. Validate `.canvas` JSON and graph references, `.base` YAML and property/formula references, and Knap output when those artifacts were created. Inspect rendering in Obsidian when available; otherwise report filesystem validation without claiming UI verification. Report unavailable sources or unexecuted code explicitly when they affect the result.
