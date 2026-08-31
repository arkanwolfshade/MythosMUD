# MythosTimeEventConsumer

> 26 nodes

## Key Concepts

- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **._init_temporal_services()** (10 connections) — `server/container/bundles/time.py`
- **test_time_event_consumer.py** (9 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **.initialize()** (6 connections) — `server/container/bundles/time.py`
- **._handle_tick()** (5 connections) — `server/time/time_event_consumer.py`
- **test_handle_tick_updates_room_and_broadcasts()** (4 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._serialize_holiday()** (4 connections) — `server/time/time_event_consumer.py`
- **._serialize_schedule()** (4 connections) — `server/time/time_event_consumer.py`
- **Any** (4 connections)
- **test_describe_state()** (3 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **tick_event()** (3 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **.describe_state()** (3 connections) — `server/time/time_event_consumer.py`
- **asyncio** (1 connections)
- **fixture** (1 connections)
- **Construct holiday_service, schedule_service, and mythos_tick_scheduler.…** (1 connections) — `server/container/bundles/time.py`
- **Initialize the Temporal context: holiday/schedule/tick-scheduler, then the…** (1 connections) — `server/container/bundles/time.py`
- **Event fired when the accelerated Mythos clock rolls over to a new hour.** (1 connections) — `server/events/event_types.py`
- **Unit tests for MythosTimeEventConsumer hour tick handling.** (1 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **Helper for admin diagnostics.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a holiday entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a schedule entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Create the SSE payload consumed by the client HUD.** (1 connections) — `server/time/time_event_consumer.py`
- **Bridges hour tick events into downstream systems such as NPC schedules and room…** (1 connections) — `server/time/time_event_consumer.py`
- *... and 1 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [HolidayService](HolidayService.md) (4 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (4 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (3 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/events/event_types.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 62 (83%)
- INFERRED: 13 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*