# npc_database.py

> 35 nodes

## Key Concepts

- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **init_npc_db()** (10 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (10 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **get_npc_database_path()** (9 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **TestNPCSessionMaker** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **_resolve_definition_id_from_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **reset_state()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_maker()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **async_sessionmaker** (2 connections)
- **AsyncSession** (2 connections)
- **AsyncEngine** (1 connections)
- **Path** (1 connections)
- **fixture** (1 connections)
- **Resolve NPC definition ID by name. Returns None if not found.** (1 connections) — `server/commands/npc_admin/instance.py`
- **NPC Database configuration for MythosMUD. This module provides database…** (1 connections) — `server/npc_database.py`
- **Get the NPC database engine, initializing if necessary. Returns: AsyncEngine |…** (1 connections) — `server/npc_database.py`
- **Get the NPC async session maker, initializing if necessary. Returns:…** (1 connections) — `server/npc_database.py`
- **Dependency to get NPC database session. Yields: AsyncSession: Database session…** (1 connections) — `server/npc_database.py`
- *... and 10 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (18 shared connections)
- [asyncio](asyncio.md) (14 shared connections)
- [patch](patch.md) (13 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [TestResetNPCDatabase](TestResetNPCDatabase.md) (2 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 126 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*