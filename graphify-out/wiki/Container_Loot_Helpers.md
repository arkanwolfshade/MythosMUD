# Container Loot Helpers

> 93 nodes

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **close_db()** (9 connections) — `server/database_helpers.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **get_database_url()** (6 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
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
- **AsyncEngine** (3 connections)
- *... and 68 more nodes in this community*

## Relationships

- [Spell Registry Costs](Spell_Registry_Costs.md) (13 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (12 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (9 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (6 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (4 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (2 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Combat Services Messaging](Combat_Services_Messaging.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 320 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*