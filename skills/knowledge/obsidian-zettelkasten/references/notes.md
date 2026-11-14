# Note conventions

## Default new-vault layout

```text
notes/          Permanent thoughts and drafts
maps/           Navigation notes and learning routes
sources/        Optional reusable source records
attachments/    Images and other attachments
_system/        Vault agreements and accepted style evidence
```

Create directories when they have content or an approved setup needs them. Existing conventions take precedence. Do not prebuild frontend/backend/embedded/management trees. Subjects may overlap through links and maps.

Use readable thought titles as filenames without numeric prefixes. Avoid filesystem-invalid characters and ambiguous duplicate basenames. Use aliases for retrieval and paths in wikilinks where necessary.

## Minimal properties

| Property | Meaning |
| --- | --- |
| `id` | Unique UUID generated once per note; check collisions and preserve through revisions/renames. |
| `type` | `permanent` for thoughts, `navigation` for maps, `source` for reusable source records. |
| `status` | `draft` or `permanent` for thoughts; omit on other roles unless locally useful. |

`type: permanent` names the thought-note role even with `status: draft`. Permanent means integrated and usable, not immutable. Avoid difficulty, confidence, mastery and topic metadata without a concrete use. Keep style evidence in the system profile, not mandatory extra properties.

IDs are not Obsidian link resolution: wikilinks use filenames/paths. Inspect backlinks before renames, preserve aliases/block IDs, update affected links and verify. Prefer CLI rename/move when available. With filesystem operations, verify vault-wide affected links or defer renaming.

## Flexible thought outline

One note develops one sufficiently complete thought. Its title expresses a claim, mechanism, distinction or genuine question. Include essential conditions in the claim itself. Adapt headings to the user's language and remove unused sections.

```markdown
---
id: <new unique UUID>
type: permanent
status: permanent
---

# A title expressing the thought

The central idea, including essential conditions.

Explain how or why it works in language the user understands.

## Example
Code, scenario, diagram or observation when useful.

## Limits
Assumptions, exceptions, counterexamples or tradeoffs when material.

## Connections
- [[Existing note]] — explain the relationship.

## Sources
Specific URL/title and locator/version when available;
or identified personal observation or synthesis.
```

Never emit placeholders or fictitious links into real notes. Do not demand an external source for an original thought. Keep unknown provenance explicit. A citation to an unread page is not verification. Verify material model-proposed claims or retain uncertainty in a draft. Do not require code or exercises everywhere.

### Example thought

Illustrative Ukrainian content; omit graph links here because no real target vault exists. Add the actual schema/ID and verified links when writing to a vault. This example is not user style evidence.

````markdown
# Поверхнева копія зберігає спільні вкладені об’єкти

Коли я копіюю об’єкт через spread, новим стає зовнішній контейнер.
Вкладений об’єкт може залишитися тим самим для обох контейнерів.

```javascript
const original = { settings: { theme: "light" } };
const copy = { ...original };
copy.settings.theme = "dark";
console.log(original.settings.theme); // "dark"
```

Тому перед зміною вкладених даних я маю з’ясувати, чи не
використовує їх інша частина програми. Сам факт копіювання
зовнішнього об’єкта незалежності цих даних не гарантує.

## Джерело
[MDN — Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
````

A management note follows the same idea structure but may need a contextual scenario, competing interpretations and evidence limits rather than code. Transfer writing preferences without forcing technical metaphors.

## Drafts and revision

Use `status: draft`, preserving the user's partial explanation and a concrete unresolved question or needed test. Known errors must be identified as rejected explanations, not presented as true. AI editing alone does not require draft status.

Promote after relevant questions are resolved and the usable formulation agreed. Propose the change before writing; retain ID/path and remove resolved warnings. Promotion does not establish mastery or make a note a qualifying style reference.

Correct factual mistakes; enrich the same idea in place; separate independently useful thoughts. For conflicting sources, retain both positions, conditions and the unresolved issue. Keep edit history in Git where available; retain old explanations in prose only when educationally useful. Do not initialize Git or commit automatically.

## Navigation and graph use

Navigation notes provide a framing question/purpose, selected real links and explained reading routes. Create as clusters or useful routes emerge. Several maps can reference the same thought. Preserve direct thought-to-thought links. Avoid a compulsory universal home node or artificial backlinks: Obsidian already exposes incoming references.

Built-in graph edges represent links, not semantic/causal inference. Node size reflects incoming references, not quality. Use local graph depth to explore neighboring chains; global filters/groups for overview. Do not promise semantic edge labels or automatically discovered relationships.

Offer filters for `_system/`, sources and navigation if these obscure thought connections. Use existing paths/properties rather than creating topic tags just for graph colors. No `.obsidian` changes or plugin installation by default. Canvas/Mermaid may explain selected relationships without replacing the note network.

## Optional source record

A `type: source` note holds title, actual locator, material version/context and useful questions or related thoughts. Create when a source is reused or worth revisiting; one thought can simply cite its source inline. No obligatory source file per URL or full copied texts.

Example content for `sources/MDN — Memory management.md`:

```markdown
# MDN — Memory management

Посилання: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management

## Навіщо повернутися
Уточнити різницю між непотрібним програмі та недосяжним об’єктом.
```

Add real thought links when available. Distinguish quotations, paraphrase and user synthesis.

## Historical scope

This is a digital learning adaptation, not an exact reconstruction of Luhmann's numbering. Stable addressing, branching thoughts, cross-references and entry points inform it. Style calibration and recall exercises are additions for this skill.

Background, not required reading for ordinary authoring: [Luhmann's 1981 account](https://ckrybus.com/static/papers/luhmann1981.pdf), [archive description](https://niklas-luhmann-archiv.de/nachlass/zettelkasten), [Schmidt's study](https://sociologica.unibo.it/article/download/8350/8270?inline=1).
