# Cursor Plans Postgresql

> 8 nodes · cohesion 0.25

## Key Concepts

- **test_async_persistence_room_cache.py** (32 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_table_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_process_exit_rows_missing_stable_id()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_warmup_room_cache()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Unit tests for async persistence layer: load_room_cache_async, query_rooms, warm** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _process_exit_rows handles missing stable_id.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test warmup_room_cache calls _ensure_room_cache_loaded.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async handles table not found error.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Relationships

- [Event Bus Serialization](Event_Bus_Serialization.md) (2 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)
- [Game Enums](Game_Enums.md) (1 shared connections)
- [Npc Idle Movement](Npc_Idle_Movement.md) (1 shared connections)
- [E 2 E Scenarios Lucidity](E_2_E_Scenarios_Lucidity.md) (1 shared connections)
- [E 2 E Execution Protocol](E_2_E_Execution_Protocol.md) (1 shared connections)
- [Dependencies Infrastructure](Dependencies_Infrastructure.md) (1 shared connections)
- [E 2 E Session Sharing](E_2_E_Session_Sharing.md) (1 shared connections)
- [Value Distribution](Value_Distribution.md) (1 shared connections)
- [Structured Logging Combat](Structured_Logging_Combat.md) (1 shared connections)
- [Cursor Plans Mud](Cursor_Plans_Mud.md) (1 shared connections)
- [Investigations Sessions Combat](Investigations_Sessions_Combat.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*