# MythosTickScheduler

> 35 nodes

## Key Concepts

- **MythosTickScheduler** (30 connections) — `server/time/tick_scheduler.py`
- **test_tick_scheduler.py** (19 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **asyncio** (9 connections)
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._truncate_to_hour()** (5 connections) — `server/time/tick_scheduler.py`
- **fixture** (4 connections)
- **scheduler()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_emit_pending_ticks_initializes_last_hour()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_emit_pending_ticks_publishes_hours()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_sleep_until_next_hour_clamps_max()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_sleep_until_next_hour_clamps_min()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_sleep_until_next_hour_no_last_emitted()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_start_idempotent()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_start_registers_task()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_stop_cancels_task()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_truncate_to_hour()** (3 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **._sleep_until_next_hour()** (3 connections) — `server/time/tick_scheduler.py`
- **.start()** (3 connections) — `server/time/tick_scheduler.py`
- **datetime** (3 connections)
- **mock_chronicle()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **mock_task_registry()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **test_publish_tick_with_holidays()** (2 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- *... and 10 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [HolidayService](HolidayService.md) (3 shared connections)
- [.__post_init__](__post_init__.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 61 (79%)
- INFERRED: 16 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*