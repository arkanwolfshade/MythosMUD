# npc_database.py

> 91 nodes

## Key Concepts

- **npc_database.py** (29 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (23 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **patch** (20 connections)
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **asyncio** (9 connections)
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSession** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_recreates_on_loop_change()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_raises_on_none_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_success()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 66 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (8 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (8 shared connections)
- [log_and_raise](log_and_raise.md) (5 shared connections)
- [database.py](database.py.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [instance.py](instance.py.md) (3 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (3 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (2 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 207 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*