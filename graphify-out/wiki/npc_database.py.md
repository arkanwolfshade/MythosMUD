# npc_database.py

> 37 nodes

## Key Concepts

- **npc_database.py** (29 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (23 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
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
- **NPC Database configuration for MythosMUD. This module provides database…** (1 connections) — `server/npc_database.py`
- **Get the NPC database engine, initializing if necessary. Returns: AsyncEngine |…** (1 connections) — `server/npc_database.py`
- **Get the NPC async session maker, initializing if necessary. Returns:…** (1 connections) — `server/npc_database.py`
- **Dependency to get NPC database session. Yields: AsyncSession: Database session…** (1 connections) — `server/npc_database.py`
- *... and 12 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (14 shared connections)
- [patch](patch.md) (14 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [NPCDefinition](NPCDefinition.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (3 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (3 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (2 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 130 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*