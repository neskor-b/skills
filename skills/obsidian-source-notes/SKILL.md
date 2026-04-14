---
name: obsidian-source-notes
description: Use when turning programming sources (books, articles, docs, courses) into linked Ukrainian notes in an Obsidian vault, routing ideas into source notes, concepts, maps, playbooks, code notes, and captures.
---

# Obsidian Source Notes

Use this skill to turn programming sources into linked Obsidian notes in `vault/`.

## Sub-skills

Do not re-implement Obsidian logic here. Use the relevant sub-skill for each case:

### `obsidian-markdown`

Use when writing or editing note content:
- Formatting wikilinks: `[[Note]]`, `[[Note|Display]]`, `[[Note#Heading]]`, `[[Note#^block-id]]`
- Adding or editing block IDs (`^block-id` anchors for definitions, claims, quotes, code)
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
- Listing tasks (`obsidian tasks daily todo`)
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
- `docs`
- `courses`

## Workflow

1. Inspect `vault/01-Sources/<source-type>/<source-slug>/` before writing.
2. Route each idea first:
   - `source-local`: bound to one source
   - `shared-evergreen`: reusable across sources
   - `topic-map`: broad topic with many links
   - `playbook`: procedure or checklist
   - `capture`: raw fragment that is not ready yet
3. Search narrowly before reading bodies:
   - current source folder
   - `vault/02-Concepts/`
   - `vault/04-Playbooks/`
   - `vault/03-Maps/` only for broad themes
4. Usually read only the best 3-7 matches. Rank by filename, aliases, frontmatter, existing links, and opening summary. Stop when confident; expand the search only if scope or naming still collides.
5. Update an existing note if it already covers the idea.
6. Write to the correct folder:
   - books: `02-Chapters/`, `03-Concepts/`, `04-Code/`
   - articles/docs/courses: `02-Notes/`, `03-Concepts/`, `04-Code/`
   - raw input: `05-Inbox/` or local `01-Inbox/`
7. Link only notes that improve navigation, provenance, or synthesis.

## Routing Guide

- `source-local` -> update or create a source-bound note in `01-Sources/<type>/<slug>/`
  - books: `02-Chapters/ch-XX-topic.md` for chapter-level ideas, `03-Concepts/concept-topic.md` for local concepts, `04-Code/code-topic.md` for code
  - articles/docs/courses: `02-Notes/note-topic.md` for source notes, `03-Concepts/concept-topic.md` for local concepts, `04-Code/code-topic.md` for code
- `shared-evergreen` -> update or create `vault/02-Concepts/concept-topic.md`
  - use when the idea is reusable across multiple sources or should survive without the original source context
- `topic-map` -> update or create `vault/03-Maps/topic-name.md`
  - use when the note mainly organizes many related notes rather than introducing a single atomic idea
- `playbook` -> update or create `vault/04-Playbooks/playbook-topic.md`
  - use when the output is a repeatable procedure, checklist, debugging flow, or decision process
- `capture` -> update or create `vault/05-Inbox/capture-topic.md` or local `01-Inbox/capture-topic.md`
  - use when the fragment is still too raw, ambiguous, or incomplete to normalize

## Promotion Rules

- Keep an idea local when it mainly depends on one source's wording, examples, or progression.
- Promote an idea to `vault/02-Concepts/` when it appears in multiple sources or becomes useful as a reusable explanation on its own.
- Promote an idea to `vault/04-Playbooks/` when the main value is an actionable sequence of steps or diagnostic checks.
- Update a map in `vault/03-Maps/` when a topic already has several related concepts, code notes, or playbooks that need navigation.
- Prefer extending an existing note with new source evidence and block references over creating a near-duplicate.

## Rules

- Keep the skill itself in English.
- Final note content must be in Ukrainian unless the user asks otherwise.
- One note equals one stable idea.
- Prefer updating over creating a duplicate.
- Keep source-bound material in the source folder.
- Move reusable synthesis to `vault/02-Concepts/`.
- Move procedures and checklists to `vault/04-Playbooks/`.
- Do not create standalone summary notes by default.
- Keep filenames short, lowercase, and predictable.
- Use these filename patterns: `ch-XX-topic.md`, `note-topic.md`, `concept-topic.md`, `code-topic.md`, `playbook-topic.md`, `capture-topic.md`.
- Prefer `chapter` notes for chapter-sized book or course sections; prefer `source` notes for smaller source fragments, articles, docs pages, or narrowly scoped excerpts.

## Metadata

Source-specific frontmatter fields (use `obsidian-markdown` for all general property rules):

- Source-bound notes: include `source_type`, `source_slug`, and `source_title`.
- Shared notes: include `scope` and `sources` when relevant.
- Playbooks: include `scope: playbook` and `sources` when relevant.

## Templates

Open the matching template before writing:

- [_templates/source-note.md](_templates/source-note.md)
- [_templates/chapter-note.md](_templates/chapter-note.md)
- [_templates/concept-note.md](_templates/concept-note.md)
- [_templates/code-note.md](_templates/code-note.md)
- [_templates/playbook-note.md](_templates/playbook-note.md)
- [_templates/capture-note.md](_templates/capture-note.md)

## Optional Prompt

- [_prompts/obsidian-session-prompt.md](_prompts/obsidian-session-prompt.md)
