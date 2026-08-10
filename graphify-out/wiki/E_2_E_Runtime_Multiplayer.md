# E 2 E Runtime Multiplayer

> 12 nodes

## Key Concepts

- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **TestCloseNpcDb** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **.test_close_npc_db_disposes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Shutdown core services.** (1 connections) — `server/container/bundles/core.py`
- **Close NPC database connections.** (1 connections) — `server/npc_database.py`
- **Test close_npc_db() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() disposes engine.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() handles closed event loop.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() handles case when engine is None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (2 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 34 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*