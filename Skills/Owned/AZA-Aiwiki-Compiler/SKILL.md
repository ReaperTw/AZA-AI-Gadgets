---
name: AZA-Aiwiki-Compiler
description: Compile and maintain the DriveSync AIWiki through Ingest, Query, Lint, and Ignore.
argument-hint: "ingest <path> | query <question> | lint | ignore <path> [reason]"
disable-model-invocation: true
---

# AZA-Aiwiki-Compiler

Maintain AIWiki as DriveSync's knowledge relation layer: reusable concepts, semantic relations, viewpoint changes, and provenance. Keep raw material in place; AIWiki is neither a backup nor a summary warehouse.

## Start

1. Locate `<DriveSyncRoot>` without assuming a drive letter. Prefer the current directory or its ancestors; otherwise find a `DriveSync` directory containing `AGENTS.md` and one complete supported layout:
   - Current: `<RulesRoot> = Others/Rules`; `<AIWikiRoot> = AIWiki`.
   - Backend: `<RulesRoot> = Backend/System/Rules`; `<AIWikiRoot> = Backend/AIWiki`.
   A layout is complete only when `<RulesRoot>` and `<AIWikiRoot>/AGENTS.md` both exist. If both layouts are complete and the requested path does not identify one, ask which is authoritative before writing.
2. Read `<DriveSyncRoot>/AGENTS.md`, follow its relevant pointers under `<RulesRoot>`, then read `<AIWikiRoot>/AGENTS.md`. Their current rules are authoritative; this Skill supplies the operation router, not a cached schema.
3. Read `<AIWikiRoot>/index.md` and `<AIWikiRoot>/ignore.md`. Read only the relevant concept, project, source, and original files after that.
4. Select the requested operation. Infer it from natural language when clear; ask only when the operation, layout, or source scope would materially change the result.

## Operations

### Ingest

Use for `$AZA-Aiwiki-Compiler ingest <source>` or a request to compile specified material.

- Resolve every source inside the user-authorized scope. Keep source files read-only and modify only `<AIWikiRoot>/**` unless the user explicitly expands scope.
- If a source exactly matches `<AIWikiRoot>/ignore.md`, report that it is excluded and make no knowledge pages for it.
- Search for an existing canonical concept first. Update it when the source adds a reusable fact, semantic relation, traceable user viewpoint, viewpoint change, or provenance.
- Create a concept only when it has long-term independent query value. A source that adds only a one-off summary may need no derived page.
- Keep source pages as thin registries: provenance, reliability and limits, plus pages using the source. Do not duplicate the source or concept summary there.
- Separate `來源事實`, optional traceable `使用者觀點`, and `AI 推論`. Use Obsidian `[[wikilinks]]` and link every knowledge page back to a source.
- Update `<AIWikiRoot>/index.md`, append the ingest event to `<AIWikiRoot>/log.md`, then run Lint.

### Query

Use for `$AZA-Aiwiki-Compiler query <question>` or a request to answer from AIWiki.

- Start at `<AIWikiRoot>/index.md`, follow only relevant concept and source links, and distinguish source facts, user viewpoints, and AI inference in the answer.
- State gaps or uncertainty instead of inventing support. Treat medical, financial, legal, and other changing claims as historical knowledge until verified against current reliable sources.
- Query is read-only by default. Compile reusable results back into AIWiki only after the user explicitly authorizes write-back; then treat it as Ingest and run Lint.

### Lint

Use for `$AZA-Aiwiki-Compiler lint` or after every write.

- Check broken wikilinks, duplicate or near-duplicate concepts, missing sources, classification errors, orphan pages, stale relations, conflicting or outdated claims, and repeated source text.
- Check actual links in maintained content. Ignore wikilink examples inside inline code or fenced code blocks, and do not apply knowledge-page schema or orphan checks to `<AIWikiRoot>/AGENTS.md`; still confirm links pointing to that file resolve.
- Confirm every maintained page is reachable from `<AIWikiRoot>/index.md` and every source registry has a valid used-by page.
- Exclude immutable research files from schema and illustrative-link checks as directed by `<AIWikiRoot>/AGENTS.md`; still verify they were not modified.
- Repair only `<AIWikiRoot>/**`. Record unresolved issues in an appended `<AIWikiRoot>/log.md` entry rather than guessing or altering raw sources.

### Ignore

Use for `$AZA-Aiwiki-Compiler ignore <source> [reason]` or when the user says material is only a memo and should stay out of AIWiki.

- Add the exact DriveSync-relative source path, reason, and date to `<AIWikiRoot>/ignore.md`; deduplicate existing entries.
- Preserve the original source. Remove its derived claims, backlinks, and registry entry. Delete a concept only when no remaining non-ignored source or reusable knowledge supports it.
- Remove deleted pages from `<AIWikiRoot>/index.md`, keep historical log meaning, repair stale historical wikilinks, append a correction entry to `<AIWikiRoot>/log.md`, then run Lint.

## Boundaries

- Do not scan `AIChats/`, personal history, or unrelated folders unless the user explicitly includes them.
- Do not treat folder names, ingest state, or Agent guesses as user viewpoints.
- Do not create hard links merely to avoid orphan pages.
- Do not run Git branch, commit, push, merge, or destructive history operations unless requested.

## Completion

Report the operation, sources used or excluded, changed files, Lint counts, unresolved limitations, and confirmation that raw sources stayed unchanged. For read-only Query, report that nothing was written.
