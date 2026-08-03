# command commands talk

> 13 nodes

## Key Concepts

- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- **_reset_database_url_state()** (5 connections) — `server/database.py`
- **_get_database_url_state()** (4 connections) — `server/database.py`
- **test_reset_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **reset_db()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Get database URL state for testing.      This is a public function to access the** (1 connections) — `server/database.py`
- **Reset database URL state for testing.      This is a public function to reset th** (1 connections) — `server/database.py`
- **Database utility functions.  This module provides module-level utility functions** (1 connections) — `server/database_helpers.py`
- **Reset database state for testing.      This function resets the DatabaseManager** (1 connections) — `server/database_helpers.py`
- **# NOTE: NPC models are NOT imported here - they belong to the NPC database** (1 connections) — `server/database_helpers.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test reset_database resets DatabaseManager singleton and module state.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (11 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (6 shared connections)
- [world models rationale](world_models_rationale.md) (3 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [commands inventory put](commands_inventory_put.md) (1 shared connections)
- [memory lifespan app](memory_lifespan_app.md) (1 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [npc idle movement](npc_idle_movement.md) (1 shared connections)
- [room persistence loader](room_persistence_loader.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*