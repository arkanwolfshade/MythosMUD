# MythosTickScheduler

> 47 nodes

## Key Concepts

- **MythosTickScheduler** (30 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **test_tick_scheduler.py** (19 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (16 connections) — `server/time/tick_scheduler.py`
- **asyncio** (9 connections)
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
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
- **.get_instance()** (3 connections) — `server/time/time_service.py`
- *... and 22 more nodes in this community*

## Relationships

- [datetime](datetime.md) (17 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [TaskRegistry](TaskRegistry.md) (4 shared connections)
- [test_time_bundle.py](test_time_bundle.py.md) (4 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 112 (85%)
- INFERRED: 19 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*