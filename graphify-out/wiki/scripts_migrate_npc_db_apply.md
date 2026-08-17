# scripts migrate npc db apply

> 8 nodes

## Key Concepts

- **apply_migration()** (4 connections) — `scripts/migrate_npc_db.py`
- **check_schema()** (4 connections) — `scripts/migrate_npc_db.py`
- **main()** (4 connections) — `scripts/migrate_npc_db.py`
- **migrate_npc_db.py** (3 connections) — `scripts/migrate_npc_db.py`
- **Path** (2 connections)
- **Cursor** (1 connections)
- **Check current schema of npc_spawn_rules table** (1 connections) — `scripts/migrate_npc_db.py`
- **Apply the migration to rename columns** (1 connections) — `scripts/migrate_npc_db.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/migrate_npc_db.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*