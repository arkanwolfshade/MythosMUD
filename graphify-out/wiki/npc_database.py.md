# npc_database.py

> 93 nodes

## Key Concepts

- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **patch** (20 connections)
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **init_npc_db()** (10 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (10 connections) — `server/npc_database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **get_npc_database_path()** (9 connections) — `server/npc_database.py`
- **asyncio** (9 connections)
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **TestCloseNpcDb** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSession** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEnsureNPCDatabaseDirectory** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_recreates_on_loop_change()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 68 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (21 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [EventBus](EventBus.md) (7 shared connections)
- [.get_instance](get_instance.md) (5 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (3 shared connections)
- [test_npc_admin_commands.py](test_npc_admin_commands.py.md) (3 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (3 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (2 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (2 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 220 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*