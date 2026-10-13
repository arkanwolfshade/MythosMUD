# Core Bundle & DB Init

> 389 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **database_config_helpers.py** (22 connections) — `server/database_config_helpers.py`
- **fixtures/integration/__init__.py** (22 connections) — `server/tests/fixtures/integration/__init__.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **reset_database()** (18 connections) — `server/database.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **._initialize_database()** (14 connections) — `server/database.py`
- **asyncio** (14 connections)
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **asyncio** (12 connections)
- **CoreBundle** (11 connections) — `server/container/bundles/core.py`
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **init_db()** (10 connections) — `server/database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **get_engine()** (9 connections) — `server/database.py`
- *... and 364 more nodes in this community*

## Relationships

- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (49 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (26 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (21 shared connections)
- [Community 637](Community_637.md) (10 shared connections)
- [Community 339](Community_339.md) (8 shared connections)
- [Community 264](Community_264.md) (6 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (6 shared connections)
- [Community 74](Community_74.md) (5 shared connections)
- [Community 870](Community_870.md) (4 shared connections)
- [Community 161](Community_161.md) (3 shared connections)
- [Community 338](Community_338.md) (3 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (2 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/tests/fixtures/integration/__init__.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 833 (87%)
- INFERRED: 121 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*