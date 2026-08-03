# npc idle movement

> 6 nodes

## Key Concepts

- **get_engine()** (9 connections) — `server/database_helpers.py`
- **test_get_engine_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Get the database engine, initializing if necessary.      Returns:         AsyncE** (1 connections) — `server/database_helpers.py`
- **Test get_engine returns engine from DatabaseManager.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_engine raises ValidationError when database cannot be initialized.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (3 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [command commands talk](command_commands_talk.md) (1 shared connections)
- [commands inventory put](commands_inventory_put.md) (1 shared connections)
- [room persistence loader](room_persistence_loader.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*