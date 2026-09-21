# get_npc_database_path

> 17 nodes

## Key Concepts

- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEnsureNPCDatabaseDirectory** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_ensure_npc_database_directory_creates_directory()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_ensure_npc_database_directory_no_op_for_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_raises_for_non_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_returns_none_for_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Path** (1 connections)
- **Get the NPC database file path. DEPRECATED: PostgreSQL does not use file paths.…** (1 connections) — `server/npc_database.py`
- **Ensure NPC database directory exists. DEPRECATED: PostgreSQL does not use file…** (1 connections) — `server/npc_database.py`
- **Test get_npc_database_path() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_database_path() returns None for PostgreSQL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_database_path() raises for non-PostgreSQL URLs.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test ensure_npc_database_directory() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test ensure_npc_database_directory() is no-op for PostgreSQL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test ensure_npc_database_directory() creates directory if needed.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [npc_database.py](npc_database.py.md) (7 shared connections)
- [patch](patch.md) (4 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 30 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*