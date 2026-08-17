# npc_database.py

> 129 nodes

## Key Concepts

- **npc_database.py** (29 connections) — `server/npc_database.py`
- **database_config_helpers.py** (25 connections) — `server/database_config_helpers.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (23 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **patch** (20 connections)
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **fixtures/integration/__init__.py** (19 connections) — `server/tests/fixtures/integration/__init__.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **test_database_config_helpers_asyncpg_settings.py** (10 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **asyncio** (9 connections)
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSession** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 104 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (37 shared connections)
- [session_factory](session_factory.md) (11 shared connections)
- [ValidationError](ValidationError.md) (10 shared connections)
- [DatabaseManager](DatabaseManager.md) (8 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [rate_overrides.py](rate_overrides.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (3 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/tests/fixtures/integration/__init__.py`
- `server/tests/unit/infrastructure/test_npc_database.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 318 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*