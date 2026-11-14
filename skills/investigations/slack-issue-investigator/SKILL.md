---
name: slack-issue-investigator
description: Use when the user explicitly asks to search Slack for prior discussions related to a current technical problem, especially when the right keywords are unclear and local code context can help formulate the search.
---

# Slack Issue Investigator

## Overview

Use this skill when the user explicitly wants Slack searched for prior discussion of a current technical problem.

This is an investigation workflow, not a single search query. Start with the local problem context, search Slack broadly across all accessible conversations, narrow based on evidence, then return a traceable report and a recommended solution.

Keep the skill company-agnostic. Do not assume any specific channel taxonomy, team structure, product naming, or org-specific workflow.

## When to Use

Use this skill only when the user clearly asks for Slack investigation, for example:

- `search Slack for this`
- `search Slack for this issue`
- `look through Slack for similar problems`
- `check whether anyone asked about this in Slack`

Strong signals:

- The user is debugging something non-obvious
- The right search terms are unclear
- Local code context may reveal better search terms than the user's description
- Prior internal discussion is likely more useful than public documentation

## When Not to Use

Do not use this skill when:

- The user is asking for ordinary debugging but did not ask to search Slack
- The task is to summarize a known channel rather than investigate a problem
- The task is to send, draft, or reply in Slack
- The available Slack tools cannot search or read the needed scope

If Slack access is unavailable or too limited for the request, say so quickly and explain the limitation.

## Workflow

### 1. Confirm explicit intent

Use this skill only on an explicit Slack-search request. Do not auto-trigger it for generic bug reports.

### 2. Harvest local context first

Read the smallest useful slice of local context before searching Slack:

- The user's description of the problem
- Nearby file names
- Relevant symbols, functions, classes, components, services, or modules
- Error strings
- Stack traces
- Logs
- Failing tests

Do not scan the whole repository unless the problem is still unclear after reading the most relevant files.

### 3. Expand the search space

Generate multiple Slack searches rather than one literal query. Use a mix of:

- Exact error text
- Symbol names
- File or module names
- Feature names
- Symptom-based wording
- Synonyms suggested by the code or error output
- Combined queries such as `symbol + symptom` or `feature + failure`

If the first query is too narrow, broaden it. If it is too noisy, narrow it.

### 4. Start wide

Search across all accessible Slack conversations first. Do not assume you already know the right channel.

If the available Slack tools support channel discovery, inspect the accessible channel set early so you can form better hypotheses about where deeper discussion is likely to live.

Use the first pass to discover:

- Better terminology
- Recurring channels
- Candidate threads
- People or teams discussing the same area

### 5. Narrow intentionally

After the wide pass, narrow the search using the strongest signals:

- Repeated technical terms
- Messages highly similar to the current problem
- Threads with deeper discussion
- Threads that contain evidence of a working fix

Prefer a few strong threads over many shallow matches.

### 6. Read candidate threads in full

For the best matches, read enough thread context to answer:

- What was the actual problem
- What solutions were proposed
- What was tried
- What seems to have worked
- Whether anyone confirmed the outcome

Do not present a thread as solved unless the thread itself shows convincing confirmation.

### 7. Synthesize findings

Group the results into:

- Strong matches
- Partial matches
- Rejected leads
- Repeated patterns
- Conflicting advice

If the Slack evidence is weak, say so instead of forcing a strong conclusion.

### 8. Recommend a solution

End with a best-effort recommendation grounded in:

- Facts from Slack
- Facts from local code or error output
- Clearly labeled inference when you go beyond the evidence

## Output Format

Return a report with these sections:

1. `Problem framing`
2. `Local clues extracted from code`
3. `Search strategy used`
4. `Relevant channels and why`
5. `Relevant threads/messages`
6. `Discarded leads`
7. `What Slack evidence suggests`
8. `Recommended solution`
9. `Confidence and open questions`

The report should help the user understand both the answer and how you arrived at it.

## Facts vs Inference

Always distinguish between:

- Facts directly stated in Slack
- Facts directly observed in code, logs, tests, or stack traces
- Inferences made from those facts
- The final recommendation

Use language that makes the boundary clear. Good phrases:

- `Slack evidence shows...`
- `In the local code, I found...`
- `My inference is...`
- `My recommended next step is...`

## Search Quality Rules

- Start broad, then narrow
- Prefer high-signal threads over large result dumps
- Show what was discarded, not only what was kept
- If direct matches fail, fall back to symptoms and related terminology
- Use the local codebase to improve query quality when the user's wording is vague

## Failure Modes

### Limited Slack access

If the available Slack tools cannot search private channels, DMs, or the expected scope, say exactly that and continue with the accessible scope.

### Weak local context

If the problem description is vague and the local code does not provide strong clues, say that the search quality is limited by weak starting signals.

### Noisy first pass

If the first search returns too many weak matches, tighten the query around symbols, exact strings, or feature-specific combinations.

### No direct matches

If no direct matches appear, search for:

- The broader feature area
- The symptom without the exact error
- Related symbol names
- Neighboring terminology found in the code

### Stale advice

If a thread looks old or partially contradicted by newer evidence, call that out before recommending the approach.

## Common Mistakes

- Treating the first matching message as the answer
- Searching only one guessed channel
- Ignoring local code context that could improve the query
- Blending confirmed Slack facts with speculation
- Returning links without explaining relevance

## Minimal Response Standard

Even when results are weak, return:

- What you searched for
- Where you searched
- What looked promising
- What was discarded
- Your current best recommendation
