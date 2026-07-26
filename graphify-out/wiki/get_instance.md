# .get_instance

> 347 nodes · cohesion 0.01

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **database.py** (75 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **._initialize_database()** (17 connections) — `server/database.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **init_db()** (11 connections) — `server/database.py`
- **set_test_database_url()** (10 connections) — `server/database_config_helpers.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **close_db()** (9 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **get_engine()** (8 connections) — `server/database.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- *... and 322 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (45 shared connections)
- [DatabaseError](DatabaseError.md) (35 shared connections)
- [get_async_session](get_async_session.md) (13 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [exceptions.py](exceptions.py.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (6 shared connections)
- [__init__.py](__init__.py.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [User](User.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [dependencies.py](dependencies.py.md) (4 shared connections)
- [get_asyncpg_server_settings_for_database_url](get_asyncpg_server_settings_for_database_url.md) (4 shared connections)

## Source Files

- `scripts/load_seed_using_project_db.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 1396 (96%)
- INFERRED: 60 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*