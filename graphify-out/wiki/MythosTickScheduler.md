# MythosTickScheduler

> 41 nodes

## Key Concepts

- **MythosTickScheduler** (30 connections) — `server/time/tick_scheduler.py`
- **test_tick_scheduler.py** (19 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (16 connections) — `server/time/tick_scheduler.py`
- **asyncio** (9 connections)
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._truncate_to_hour()** (5 connections) — `server/time/tick_scheduler.py`
- **MythosCalendarComponents** (4 connections) — `server/time/time_service.py`
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
- *... and 16 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [MythosChronicle](MythosChronicle.md) (5 shared connections)
- [TaskRegistry](TaskRegistry.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [.initialize](initialize.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 83 (84%)
- INFERRED: 16 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*