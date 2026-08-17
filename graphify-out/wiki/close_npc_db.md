# close_npc_db

> 12 nodes

## Key Concepts

- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **Shutdown core services.** (1 connections) — `server/container/bundles/core.py`
- **Close NPC database connections.** (1 connections) — `server/npc_database.py`
- **Test close_npc_db() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() disposes engine.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() handles closed event loop.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() handles case when engine is None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [asyncio](asyncio.md) (3 shared connections)
- [patch](patch.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [get_npc_engine](get_npc_engine.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*