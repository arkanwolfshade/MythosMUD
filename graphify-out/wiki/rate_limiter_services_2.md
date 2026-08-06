# rate limiter services

> 35 nodes

## Key Concepts

- **MythosTickScheduler** (29 connections) — `server/time/tick_scheduler.py`
- **test_tick_scheduler.py** (17 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._truncate_to_hour()** (5 connections) — `server/time/tick_scheduler.py`
- **.start()** (3 connections) — `server/time/tick_scheduler.py`
- **._sleep_until_next_hour()** (3 connections) — `server/time/tick_scheduler.py`
- **datetime** (3 connections)
- **scheduler()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_truncate_to_hour()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_start_registers_task()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_start_idempotent()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_stop_cancels_task()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_emit_pending_ticks_publishes_hours()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_emit_pending_ticks_initializes_last_hour()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_sleep_until_next_hour_no_last_emitted()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_sleep_until_next_hour_clamps_min()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_sleep_until_next_hour_clamps_max()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_publish_tick_with_holidays()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **.stop()** (2 connections) — `server/time/tick_scheduler.py`
- **mock_chronicle()** (1 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **mock_event_bus()** (1 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **mock_task_registry()** (1 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- *... and 10 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [follow service game](follow_service_game.md) (2 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [command service commands](command_service_commands.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [schemas items item](schemas_items_item.md) (1 shared connections)
- [event connection helpers](event_connection_helpers.md) (1 shared connections)

## Source Files

- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 113 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*