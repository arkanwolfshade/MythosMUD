# Realtime Errors Error

> 30 nodes

## Key Concepts

- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **_initialize_npc_database()** (11 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (9 connections) — `server/npc_database.py`
- **TestNPCSession** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSessionMaker** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_raises_on_none_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **.test_get_npc_session_maker()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_yields_session()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_rollback_on_error()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_inits_db_for_unit_test()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Initialize NPC database engine and session maker from configuration.      CRITIC** (1 connections) — `server/npc_database.py`
- **Get the NPC async session maker, initializing if necessary.      Returns:** (1 connections) — `server/npc_database.py`
- **Dependency to get NPC database session.      Yields:         AsyncSession: Datab** (1 connections) — `server/npc_database.py`
- **Initialize NPC database connection and verify configuration.      NOTE: DDL (tab** (1 connections) — `server/npc_database.py`
- **Unit tests for NPC database initialization and session management.  Tests NPC da** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC session maker functions.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session_maker() returns session maker.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC session management.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() yields session.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 5 more nodes in this community*

## Relationships

- [Room Service Tests](Room_Service_Tests.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (7 shared connections)
- [Coverage Disconnect Grace](Coverage_Disconnect_Grace.md) (5 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (5 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (3 shared connections)
- [Nats Code Review](Nats_Code_Review.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (2 shared connections)
- [Death Delirium UI Modals](Death_Delirium_UI_Modals.md) (2 shared connections)
- [Test Refactoring Deliverables](Test_Refactoring_Deliverables.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 122 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*