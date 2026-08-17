# test_schedule_room_occupants_update_does_not_leak_coro_when_register_fails

> 2 nodes

## Key Concepts

- **test_schedule_room_occupants_update_does_not_leak_coro_when_register_fails()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **register_task RuntimeError must close the occupants coroutine (startup…** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`

## Relationships

- [asyncio](asyncio.md) (1 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 3 (75%)
- INFERRED: 1 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*