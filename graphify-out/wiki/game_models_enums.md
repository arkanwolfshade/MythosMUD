# game models enums

> 6 nodes

## Key Concepts

- **get_database_url()** (6 connections) — `server/database_helpers.py`
- **test_get_database_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Get the database URL, initializing if necessary.      Returns:         str | Non** (1 connections) — `server/database_helpers.py`
- **Test get_database_url returns URL from DatabaseManager.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_url returns None when not configured.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (3 shared connections)
- [command commands talk](command_commands_talk.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*