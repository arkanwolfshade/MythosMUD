---
name: mythosmud-llm-wiki
description: >-
  Maintain MythosMUD permanent memory in the Obsidian LLM wiki under
  data/MythosMUD-Obsidian (Karpathy pattern: raw / wiki / schema). Use when
  ingesting sources, filing durable answers, linting the wiki, syncing graphify
  into the vault, or when the user mentions Obsidian, LLM wiki, or project
  memory.
---

# MythosMUD LLM Wiki (Obsidian)

## Vault location

`data/MythosMUD-Obsidian/`

Schema (read first): `data/MythosMUD-Obsidian/AGENTS.md`

Catalog: `data/MythosMUD-Obsidian/index.md`

Log: `data/MythosMUD-Obsidian/log.md`

Pattern reference:
[Karpathy llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

## When to use this skill

- User drops or points at a source to **ingest**
- Answer should **persist** beyond the chat (design, lore, decisions)
- User asks to **lint** / health-check the wiki
- After code-graph updates: **sync graphify** into the vault
- User mentions Obsidian vault, permanent memory, or LLM wiki

## Non-goals

- Do not use the vault as a substitute for live `graphify query` / jCodemunch
  when answering "how does this code work right now?"
- Do not run `graphify export obsidian` into the curated vault (too many nodes).
  Use `graphify export wiki` + sync script instead.
- Never edit `raw/` sources (except regenerating `raw/graphify/` via the script).

## Workflows

### Ingest

1. Confirm source path under `raw/` (or copy a new clip into `raw/clips/` /
   `raw/sources/` first; do not alter existing raw files).
2. Follow vault `AGENTS.md` → Operations → Ingest.
3. Update `index.md` and append `log.md`.
4. Summarize pages touched for the user.

### Query (durable)

1. Read `index.md`, then relevant `wiki/` pages.
2. Answer with citations (`[[wikilinks]]` / raw paths).
3. File reusable answers under `wiki/queries/` or `wiki/comparisons/`.
4. Log the query.

### Lint

1. Scan for orphans, contradictions, missing concept pages, stale claims.
2. Propose a short fix list; apply mechanical fixes; ask before large rewrites.
3. Log the lint pass.

### Graphify sync

From repo root (PowerShell):

```powershell
./scripts/sync_obsidian_graphify.ps1
```

Then optionally promote high-signal findings into `wiki/code/` pages.

## Division of labor

| Need                   | Where                                           |
| ---------------------- | ----------------------------------------------- |
| Permanent memory       | This vault                                      |
| Live code graph        | `graphify` CLI + `graphify-out/`                |
| Symbol edit navigation | jCodemunch                                      |
| Formal ADRs            | `docs/architecture/decisions/` (+ wiki summary) |
