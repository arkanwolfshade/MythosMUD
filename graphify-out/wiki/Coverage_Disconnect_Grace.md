# Coverage Disconnect Grace

> 6 nodes

## Key Concepts

- **TestEnsureNPCDatabaseDirectory** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_ensure_npc_database_directory_no_op_for_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_ensure_npc_database_directory_creates_directory()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test ensure_npc_database_directory() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test ensure_npc_database_directory() is no-op for PostgreSQL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test ensure_npc_database_directory() creates directory if needed.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [Combat Schema Validation](Combat_Schema_Validation.md) (3 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*