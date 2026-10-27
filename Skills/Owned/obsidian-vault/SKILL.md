---
name: obsidian-vault
description: Search, create, and organize notes in the current Obsidian vault with wikilinks and hierarchical index notes. Use when the user wants to find, create, or organize notes in Obsidian.
---

# Obsidian Vault

## Vault location

The active Vault is `C:\Drivesync\MainVault` on this device. Other devices may use a different path — locate the Vault via the project `AGENTS.md` before assuming this path.

The Vault is hierarchical, not flat: `Home.md` is the human entry point, and every top-level area has an `_index.md` that routes navigation.

## Routing

1. Read the Vault-root `AGENTS.md` and the project `AGENTS.md` for the active task; they are authoritative for routing and rules.
2. Start navigation at `Home.md`, then follow the relevant top-level `_index.md` (Inbox, Writing, Academic, Mindset, Records, Library, Backend) and its sub-indexes to the target area.
3. Use the `_index.md` structure to decide where a note belongs before creating or moving anything.

## Naming and linking

- **Title case** for note names.
- Use Obsidian `[[wikilinks]]` syntax: `[[Note Title]]`.
- Notes link to dependencies or related notes at the bottom.
- Index notes aggregate a topic; list `[[wikilinks]]`, do not duplicate content.

## Workflows

### Search for notes

```powershell
# Search by filename
rg --files "C:\Drivesync\MainVault" | rg -i "keyword"

# Search by content
rg -l -i "keyword" "C:\Drivesync\MainVault" -g "*.md"
```

Or use Grep/Glob tools directly on the Vault path.

### Create a new note

1. Read the relevant `_index.md` to confirm the destination area.
2. Use **Title Case** for the filename.
3. Write the content as a unit of learning or a structured note (per Vault rules).
4. Add `[[wikilinks]]` to related notes at the bottom.
5. If part of a numbered sequence, use the hierarchical numbering scheme.

### Find related notes

Search for `[[Note Title]]` across the Vault to find backlinks:

```powershell
rg -l -F "[[Note Title]]" "C:\Drivesync\MainVault" -g "*.md"
```

### Find index notes

```powershell
rg --files "C:\Drivesync\MainVault" | rg "_index\.md$"
```

## Boundaries

- File classification, moves, empty-note cleanup, and drive maintenance: defer to `Backend/System/Rules/DriveSync_File_Maintenance.md` — never move or delete without explicit user request.
- AIChats access and quoting personal history: defer to `Backend/System/Rules/AIChats_Knowledge.md`.
- SOUL access: defer to the Vault-root `AGENTS.md` gating — read `SOUL.md` only when the user explicitly asks or the task involves personal context.
- Do not claim the Vault is flat; route through `Home.md` and `_index.md` files.
