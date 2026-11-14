---
name: repo-architecture-analyzer
description: >
  Analyze any code repository and produce a structured architecture report: every entity
  (class, component, service, model, hook, controller, module, util, type) with its
  responsibility, public API, and dependency links. Use this skill when asked to understand,
  document, or map the architecture of a codebase — regardless of language or framework.
  Output is a structured data model (not yet formatted for any tool), ready to be consumed
  by a rendering skill such as repo-to-obsidian.
---

# Repo Architecture Analyzer

Analyzes a code repository and extracts a complete, structured architecture model:
all entities, their responsibilities, their public APIs, and the dependency graph between them.

This skill produces **analysis output only** — it does not write final notes or files.
Its output is consumed by an orchestrator skill (e.g., `repo-to-obsidian`).

---

## Phase 1 — Project Identification

Before touching individual files, understand the project at a high level.

1. Read `package.json` / `pyproject.toml` / `pom.xml` / `go.mod` / `Cargo.toml` (whichever exists)
   to identify: language, framework, major dependencies, project name.
2. Read `README.md` if present — extract the one-paragraph description of what the app does.
3. List the top-level directory structure (max 2 levels deep).
4. Identify the **architectural style**: layered MVC, feature-sliced, hexagonal, component-driven,
   microservice, monolith, library, CLI tool, etc.
5. Identify the **source root**: `src/`, `app/`, `lib/`, `packages/`, or repo root.

Record this as the **Project Summary**:

```
name: <project name>
language: <primary language>
framework: <framework or "none">
style: <architectural style>
source_root: <path>
description: <one paragraph>
```

---

## Phase 2 — Entity Discovery

Walk the source tree and identify every file that defines an architectural entity.

**Include:**

- Files that export/define classes, components, services, controllers, repositories,
  models/schemas, stores, hooks/composables, middleware, guards, pipes, resolvers,
  route handlers, utility modules, DI modules, configuration objects

**Skip:**

- Test files (`*.test.*`, `*.spec.*`, `__tests__/`, `test/`)
- Generated files (`dist/`, `build/`, `.cache/`, `*.generated.*`, `*.pb.*`)
- Lock files, environment files (`.env`), raw config files that define no logic
- Third-party vendored code (`vendor/`, `node_modules/`)

For each file found, record:

```
file: <relative path from repo root>
entities: [list of entity names defined in this file]
```

A single file can define multiple entities (e.g., a file with multiple exported classes).
Treat each as a separate entity with the same source file.

---

## Phase 3 — Entity Analysis

For every entity discovered, extract:

### Entity Record

```
name: <ExactExportedName>
type: <class|component|service|model|hook|controller|repository|store|module|util|type|middleware|config>
file: <relative path>
responsibility: <one sentence — what this entity does and why it exists>
design_pattern: <optional — Repository, Singleton, Observer, Factory, Strategy, Facade…>
public_api:
  - name: <methodName or propName>
    signature: <full signature if available>
    description: <one line>
internal_dependencies:
  - name: <OtherEntityName>
    reason: <why it is used — one line>
notes: <optional — edge cases, TODOs, unclear parts>
```

**Rules for responsibility:**

- Write one sentence in active voice: "Manages user authentication state and exposes login/logout actions."
- If responsibility is genuinely unclear from static analysis, write: "Responsibility unclear — review manually."
- Do not repeat the entity name in the sentence.

**Rules for internal_dependencies:**

- List only entities defined **in this repo** — not third-party libraries.
- Extract from: import statements, constructor parameters, class fields, `inject()` calls,
  `provide/inject`, `useSelector`, `useStore`, decorators (`@Inject`, `@Autowired`).
- If a dependency is used but not defined in this repo, omit it.

---

## Phase 4 — Dependency Graph

After all entities are analyzed, build the complete bidirectional dependency graph.

For each entity A that depends on entity B:

- A has B in `internal_dependencies`
- B must have A in its `dependents` list (computed, not extracted)

Compute `dependents` for every entity by inverting the `internal_dependencies` map.

Then identify **dependency clusters**: groups of 2–6 entities that are tightly coupled
(many edges between them). These are the most architecturally significant areas.

```
clusters:
  - name: <ClusterName>
    entities: [EntityA, EntityB, EntityC]
    description: <what they do together>
```

---

## Phase 5 — Architecture Summary

Produce a final summary of the entire analysis:

```
project: <Project Summary from Phase 1>

layers:
  - name: <LayerName>         # e.g. "Presentation", "Business Logic", "Data Access"
    entities: [...]
    description: <one line>

data_flow:
  <Describe in 3–5 steps how a typical request/action flows through the system.
   Use entity names. Example: "1. User action triggers [[AuthComponent]], which calls
   [[AuthService]]. 2. AuthService validates credentials via [[UserRepository]]…">

entry_points:
  - <EntityName> — <why it is an entry point>

clusters: <from Phase 4>

total_entities: <count>
```

---

## Language-Specific Extraction Rules

### TypeScript / JavaScript

- **React**: components are functions/classes returning JSX; hooks start with `use`
- **Vue**: `defineComponent`, `<script setup>`, composables
- **Angular**: detect by decorators — `@Component`, `@Injectable`, `@NgModule`,
  `@Controller`, `@Pipe`, `@Guard`, `@Interceptor`
- **NestJS**: `@Injectable()` → service, `@Controller()` → controller,
  `@Module()` → module, `@Entity()` → model
- **Zustand/Redux**: store slices and selectors are `store` type entities
- Extract imports from `import { X } from './path'` and `require('./path')`

### Python

- **Django**: `models.Model` subclasses → model; `View`/`APIView` subclasses → controller;
  `Serializer` subclasses → model; `Manager` subclasses → repository
- **FastAPI**: router functions → controller; Pydantic models → model;
  `Depends()` providers → service
- Extract imports from `from module import X` and `import module`

### Java / Kotlin

- Detect entity type from annotations: `@Service`, `@Repository`, `@Controller`,
  `@RestController`, `@Component`, `@Entity`, `@ViewModel`
- Extract dependencies from constructor parameters and `@Autowired` fields

### Go

- Group by package. Each package with exported types/functions is an entity.
- Interfaces are `type` entities; structs with methods are `service` or `model` entities.

### Other languages

Apply the same principles: find the primary abstraction unit, extract its name,
responsibility, public surface, and import-based dependencies.

---

## Output Format

Return the complete analysis as a structured report in this order:

1. **Project Summary**
2. **Entity List** — all entities with full records
3. **Dependency Graph** — adjacency list (A → [B, C], B → [D], …)
4. **Dependency Clusters**
5. **Architecture Summary** including data flow and layers

This output is passed directly to the rendering skill. Keep it complete and accurate —
downstream note generation depends on the correctness of dependency links.
