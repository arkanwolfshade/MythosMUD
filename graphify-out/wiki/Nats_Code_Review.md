# Nats Code Review

> 8 nodes

## Key Concepts

- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **TestResetNPCDatabase** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_reset_npc_database_resets_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Reset NPC database state for testing.      This function resets all global NPC d** (1 connections) — `server/npc_database.py`
- **Reset NPC database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test reset_npc_database() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test reset_npc_database() resets all global state.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [Realtime Errors Error](Realtime_Errors_Error.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 18 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*