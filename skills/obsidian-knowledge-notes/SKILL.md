---
name: obsidian-knowledge-notes
description: Use when turning books, articles, papers, course notes, excerpts, or raw fragments into linked Ukrainian notes in an Obsidian vault, routing ideas into source notes, concepts, arguments, maps, playbooks, and captures.
---

# Obsidian Knowledge Notes

Use this skill to turn source material and raw note fragments into linked Obsidian notes in `vault/`.

Resolve every relative path mentioned in this skill relative to this skill directory, meaning the directory that contains this `SKILL.md`, not relative to the current workspace or the Obsidian vault.

## Sub-skills

Do not re-implement Obsidian logic here. Use the relevant sub-skill for each case:

### `obsidian-markdown`

Use when writing or editing note content:
- Formatting wikilinks: `[[Note]]`, `[[Note|Display]]`, `[[Note#Heading]]`, `[[Note#^block-id]]`
- Adding or editing block IDs (`^block-id` anchors for definitions, claims, quotes, evidence)
- Writing frontmatter / properties (title, tags, aliases, cssclasses, custom fields)
- Adding callouts (`> [!note]`, `> [!warning]`, etc.)
- Embedding notes, images, or PDFs (`![[embed]]`)
- Adding inline tags (`#tag`, `#nested/tag`)
- Writing LaTeX math (`$formula$`, `$$block$$`)
- Writing Mermaid diagrams
- Adding Obsidian comments (`%%hidden%%`)
- Adding footnotes

### `obsidian-cli`

Use when interacting with the vault from the terminal:
- Reading note content (`obsidian read file="..."`)
- Creating new notes (`obsidian create name="..."`)
- Appending content to a note (`obsidian append file="..."`)
- Searching vault content (`obsidian search query="..."`)
- Reading or appending to the daily note (`obsidian daily:read`, `obsidian daily:append`)
- Setting or updating note properties (`obsidian property:set`)
- Listing tags or backlinks (`obsidian tags`, `obsidian backlinks`)

### `obsidian-bases`

Use when building database views over notes:
- Creating `.base` files
- Defining `filters` to query notes by tag, folder, or property
- Defining `formulas` to compute values (dates, conditionals, arithmetic)
- Configuring `views` (table, cards, list, map)
- Adding `summaries` (Sum, Average, Count, etc.)
- Embedding a base into a note (`![[File.base]]`)

Supported source types:

- `books`
- `articles`
- `essays`
- `papers`
- `courses`
- `talks`
- `interviews`
- `notes`

If the user only provides a quote, fragment, or rough note without stable source metadata, treat it as a `capture` first and promote it later only when the structure becomes clear.

## Workflow

Before writing, resolve all relative paths in this skill against this skill directory, meaning the directory that contains this `SKILL.md`. `_templates/...` paths refer to files inside the skill folder, not inside the Obsidian vault, and you must open the matching template file before writing notes.

1. Inspect `vault/01-Sources/<source-type>/<source-slug>/` before writing when the material belongs to a known source.
2. Normalize source identity if possible:
   - `source_type`
   - `source_slug`
   - `source_title`
3. Route each idea first:
   - `source-local`: bound to one source, section, or excerpt
   - `shared-evergreen`: reusable across sources
   - `argument`: a claim, model, causal chain, or explanatory frame that deserves its own note
   - `topic-map`: a note whose main job is navigation and synthesis
   - `playbook`: a reusable procedure, checklist, or decision process
   - `capture`: raw material that is not ready yet
4. Search narrowly before reading bodies:
   - current source folder
   - `vault/02-Concepts/`
   - `vault/03-Maps/`
   - `vault/04-Playbooks/`
5. Usually read only the best 3-7 matches. Rank by filename, aliases, frontmatter, existing links, and opening summary. Stop when confident; expand the search only if scope or naming still collides.
6. Update an existing note if it already covers the idea.
7. Write to the correct folder:
   - books/courses: `02-Chapters/`, `03-Concepts/`, `04-Arguments/`
   - articles/essays/papers/talks/interviews/notes: `02-Notes/`, `03-Concepts/`, `04-Arguments/`
   - reusable global notes: `vault/02-Concepts/`
   - maps: `vault/03-Maps/`
   - playbooks: `vault/04-Playbooks/`
   - raw input: `vault/05-Inbox/` or local `01-Inbox/`
8. Link only notes that improve navigation, provenance, or synthesis.

## Routing Guide

- `source-local` -> update or create a source-bound note in `01-Sources/<type>/<slug>/`
  - books/courses: `02-Chapters/ch-XX-topic.md` for chapter-level ideas, `03-Concepts/concept-topic.md` for local concepts, `04-Arguments/argument-topic.md` for local arguments or models
  - articles/essays/papers/talks/interviews/notes: `02-Notes/note-topic.md` for source notes, `03-Concepts/concept-topic.md` for local concepts, `04-Arguments/argument-topic.md` for local arguments or models
- `shared-evergreen` -> update or create `vault/02-Concepts/concept-topic.md`
  - use when the idea is reusable across multiple sources or should survive without the original source context
- `argument` -> update or create `vault/02-Concepts/argument-topic.md`
  - use when the main value is the structure of a claim, model, mechanism, or line of reasoning rather than a plain definition
- `topic-map` -> update or create `vault/03-Maps/map-topic.md`
  - use when the note mainly organizes several concepts, arguments, or source notes instead of introducing one atomic idea
- `playbook` -> update or create `vault/04-Playbooks/playbook-topic.md`
  - use when the output is a repeatable procedure, checklist, reading workflow, or decision process
- `capture` -> update or create `vault/05-Inbox/capture-topic.md` or local `01-Inbox/capture-topic.md`
  - use when the fragment is still too raw, ambiguous, or incomplete to normalize

## Promotion Rules

- Keep an idea local when it mainly depends on one source's wording, sequence, examples, or evidence.
- Promote an idea to `vault/02-Concepts/` when it becomes a reusable explanation on its own.
- Promote an idea to `vault/02-Concepts/argument-topic.md` when the reasoning chain, model, or claim is worth comparing across multiple sources.
- Update a map in `vault/03-Maps/` when a topic already has several related concepts, arguments, or playbooks that need navigation.
- Promote an idea to `vault/04-Playbooks/` when the main value is an actionable sequence of steps or recurring process.
- Prefer extending an existing note with new source evidence and block references over creating a near-duplicate.

## Rules

- Keep the skill itself in English.
- Final note content must be in Ukrainian unless the user asks otherwise.
- One note equals one stable idea.
- Prefer updating over creating a duplicate.
- Keep source-bound material in the source folder.
- Move reusable synthesis to `vault/02-Concepts/`.
- Use standalone `argument` notes for claims, models, and causal explanations that need their own structure.
- Move procedures and checklists to `vault/04-Playbooks/`.
- Do not create standalone summary notes by default.
- If source metadata is missing, do not invent it. Store the fragment as a `capture` first.
- Keep filenames short, lowercase, and predictable.
- Use these filename patterns: `ch-XX-topic.md`, `note-topic.md`, `concept-topic.md`, `argument-topic.md`, `map-topic.md`, `playbook-topic.md`, `capture-topic.md`.
- Prefer `chapter` notes for book or course sections and `source` notes for smaller source fragments or standalone excerpts.

## Metadata

Source-specific frontmatter fields (use `obsidian-markdown` for all general property rules):

- Source-bound notes: include `source_type`, `source_slug`, and `source_title`.
- Shared concept or argument notes: include `scope` and `sources` when relevant.
- Argument notes: include `claim_status` when useful, for example `working`, `supported`, or `contested`.
- Map notes: include `scope: map`.
- Playbooks: include `scope: playbook` and `sources` when relevant.

## Templates

Rule: `_templates/...` paths in this skill always refer to files inside this skill folder, never to `vault/_templates/...`.

Open the matching template file from this skill directory before writing any note.

Example: `_templates/chapter-note.md` resolves to the file at `./_templates/chapter-note.md` relative to this `SKILL.md`, not `vault/_templates/chapter-note.md`.

- [_templates/source-note.md](_templates/source-note.md)
- [_templates/chapter-note.md](_templates/chapter-note.md)
- [_templates/concept-note.md](_templates/concept-note.md)
- [_templates/argument-note.md](_templates/argument-note.md)
- [_templates/map-note.md](_templates/map-note.md)
- [_templates/playbook-note.md](_templates/playbook-note.md)
- [_templates/capture-note.md](_templates/capture-note.md)
