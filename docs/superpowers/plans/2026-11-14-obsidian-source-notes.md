# Obsidian Source Notes Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for inline implementation.

**Goal:** Replace the two source-library skills with obsidian-source-notes, preserving shared and domain-specific capabilities.

**Architecture:** One source-to-notes workflow with eight note templates. Delegate format and tool mechanics to the seven official Obsidian skills, loaded only when relevant.

**Spec:** User-approved design in this chat: unified Ukrainian source notes, arguments, maps, code and playbooks; preserve existing vault structure; integrate obsidianmd/obsidian-skills.

## Constraints and review focus

- Skill instructions in English; notes in Ukrainian unless requested otherwise.
- Resolve bundled template paths relative to the skill; vault paths relative to the selected vault.
- Preserve existing notes, conventions and links; no invented source identity or evidence.
- Both chapter-based courses and page-based documentation must route correctly.
- Missing CLI or optional dependencies must not be reported as successful execution.
- Ordinary note creation must not trigger Sync, Publish or unrelated artifacts.

## Tasks

- [x] Create unified entrypoint and merge eight templates, retaining arguments, maps, code, practical rules, provenance and captures.
- [x] Update UI metadata and README to the official upstream and seven dependency roles; retain lockfile hashes of installed dependencies.
- [x] Validate frontmatter, resource links, legacy references and behavioral routing; remove old skill directories after replacement exists.

## Validation evidence

Independent scenario evaluation covered web extraction, course/code/argument routing, existing layout, structured imports/Bases, Canvas and desktop-free editing. Follow-up clarified stable batch identity and preserving links during offline renames. Bundled validator passed; resource and YAML checks are run separately. Existing installed global copies are outside this repository and are not changed.
