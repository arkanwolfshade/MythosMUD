# npc_database.py

> 40 nodes

## Key Concepts

- **npc_database.py** (31 connections) — `server/npc_database.py`
- **test_npc_database.py** (26 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (13 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **_build_npc_connect_args()** (9 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **_build_npc_pool_kwargs()** (7 connections) — `server/npc_database.py`
- **_resolve_npc_database_url()** (6 connections) — `server/npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **TestBuildNpcPoolKwargs** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **_resolve_definition_id_from_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **reset_state()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **_track_npc_engine_creation_loop()** (3 connections) — `server/npc_database.py`
- **.test_production_database_uses_configured_pool_settings()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_test_database_uses_nullpool()** (2 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **async_sessionmaker** (2 connections)
- **AsyncSession** (2 connections)
- **AsyncEngine** (1 connections)
- **fixture** (1 connections)
- **Resolve NPC definition ID by name. Returns None if not found.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Build connect_args for asyncpg: always a hung-transaction timeout, plus…** (1 connections) — `server/database_config_helpers.py`
- *... and 15 more nodes in this community*

## Relationships

- [patch](patch.md) (14 shared connections)
- [asyncio](asyncio.md) (12 shared connections)
- [NPCDefinition](NPCDefinition.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [get_npc_database_path](get_npc_database_path.md) (7 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [test_npc_definitions_api.py](test_npc_definitions_api.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (3 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 148 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*