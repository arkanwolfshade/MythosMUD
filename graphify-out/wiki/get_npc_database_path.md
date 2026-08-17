# get_npc_database_path

> 9 nodes

## Key Concepts

- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_raises_for_non_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_returns_none_for_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Path** (1 connections)
- **Get the NPC database file path. DEPRECATED: PostgreSQL does not use file paths.…** (1 connections) — `server/npc_database.py`
- **Test get_npc_database_path() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_database_path() returns None for PostgreSQL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_database_path() raises for non-PostgreSQL URLs.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [npc_database.py](npc_database.py.md) (4 shared connections)
- [patch](patch.md) (3 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 17 (89%)
- INFERRED: 2 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*