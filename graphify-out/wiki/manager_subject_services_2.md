# manager subject services

> 93 nodes

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **close_db()** (9 connections) — `server/database_helpers.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (7 connections) — `server/database_helpers.py`
- **get_test_database_url()** (6 connections) — `server/database_config_helpers.py`
- **get_database_url()** (6 connections) — `server/database_helpers.py`
- **_reset_database_url_state()** (5 connections) — `server/database.py`
- **test_get_engine_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **_get_database_url_state()** (4 connections) — `server/database.py`
- **AsyncSession** (4 connections)
- **test_reset_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_unsupported_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_empty_string_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_engine_initialization_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- *... and 68 more nodes in this community*

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (13 shared connections)
- [command inventory models](command_inventory_models.md) (10 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (9 shared connections)
- [combat npc services](combat_npc_services.md) (5 shared connections)
- [world models rationale](world_models_rationale.md) (4 shared connections)
- [game models enums](game_models_enums.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [conftest mock rationale](conftest_mock_rationale.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 327 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*