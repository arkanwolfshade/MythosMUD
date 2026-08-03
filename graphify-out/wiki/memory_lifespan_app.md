# memory lifespan app

> 7 nodes

## Key Concepts

- **ensure_database_directory()** (7 connections) — `server/database_helpers.py`
- **test_ensure_database_directory_no_op_for_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_ensure_database_directory_creates_directory()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Ensure database directory exists (deprecated for PostgreSQL).      This function** (2 connections) — `server/database.py`
- **Ensure database directory exists.      DEPRECATED: PostgreSQL does not use file** (1 connections) — `server/database_helpers.py`
- **Test ensure_database_directory is no-op for PostgreSQL (returns None).** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test ensure_database_directory creates directory when path exists.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [lucidity npc combat](lucidity_npc_combat.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [command commands talk](command_commands_talk.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*