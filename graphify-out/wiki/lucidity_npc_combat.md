# lucidity npc combat

> 18 nodes

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **test_get_database_path_unsupported_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_empty_string_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_postgresql_returns_none()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_none_url_uses_manager()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_uses_database_manager_when_no_test_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_uses_test_url_when_available()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_uses_module_attribute_fallback()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Get the database file path.      DEPRECATED: PostgreSQL does not use file paths.** (1 connections) — `server/database_helpers.py`
- **Unit tests for database_helpers module.  Tests module-level utility functions fo** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_path returns None for PostgreSQL URLs.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_path raises ValidationError for unsupported URL schemes.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_path uses DatabaseManager when URL state is None.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_path falls back to DatabaseManager when no test URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_path raises ValidationError when URL is empty string.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_path uses test URL from get_test_database_url when available.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_path falls back to module _database_url attribute.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [manager subject services](manager_subject_services.md) (11 shared connections)
- [command commands talk](command_commands_talk.md) (6 shared connections)
- [command inventory models](command_inventory_models.md) (5 shared connections)
- [room persistence loader](room_persistence_loader.md) (5 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [memory lifespan app](memory_lifespan_app.md) (4 shared connections)
- [commands inventory put](commands_inventory_put.md) (4 shared connections)
- [npc idle movement](npc_idle_movement.md) (3 shared connections)
- [game models enums](game_models_enums.md) (3 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 92 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*