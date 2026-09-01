# npc_database.py

> 41 nodes

## Key Concepts

- **npc_database.py** (29 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (23 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **_resolve_definition_id_from_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **reset_state()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_maker()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_reset_npc_database_resets_state()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSessionMaker** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestResetNPCDatabase** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **async_sessionmaker** (2 connections)
- **AsyncSession** (2 connections)
- **AsyncEngine** (1 connections)
- **Path** (1 connections)
- **fixture** (1 connections)
- **Resolve NPC definition ID by name. Returns None if not found.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Build connect_args for asyncpg: always a hung-transaction timeout, plus…** (1 connections) — `server/database_config_helpers.py`
- *... and 16 more nodes in this community*

## Relationships

- [patch](patch.md) (25 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [TestEnsureNPCDatabaseDirectory](TestEnsureNPCDatabaseDirectory.md) (3 shared connections)
- [test_npc_definitions_api.py](test_npc_definitions_api.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (3 shared connections)
- [NPCStartupService](NPCStartupService.md) (3 shared connections)
- [get_config](get_config.md) (3 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 140 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*