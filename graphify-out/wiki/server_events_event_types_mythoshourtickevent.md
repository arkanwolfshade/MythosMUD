# server events event types mythoshourtickevent

> 23 nodes

## Key Concepts

- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **test_time_event_consumer.py** (9 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **._handle_tick()** (5 connections) — `server/time/time_event_consumer.py`
- **test_handle_tick_updates_room_and_broadcasts()** (4 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._serialize_holiday()** (4 connections) — `server/time/time_event_consumer.py`
- **._serialize_schedule()** (4 connections) — `server/time/time_event_consumer.py`
- **Any** (4 connections)
- **test_describe_state()** (3 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **tick_event()** (3 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **.describe_state()** (3 connections) — `server/time/time_event_consumer.py`
- **.__post_init__()** (2 connections) — `server/events/event_types.py`
- **asyncio** (1 connections)
- **fixture** (1 connections)
- **Event fired when the accelerated Mythos clock rolls over to a new hour.** (1 connections) — `server/events/event_types.py`
- **Unit tests for MythosTimeEventConsumer hour tick handling.** (1 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **Helper for admin diagnostics.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a holiday entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a schedule entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Create the SSE payload consumed by the client HUD.** (1 connections) — `server/time/time_event_consumer.py`
- **Bridges hour tick events into downstream systems such as NPC schedules and room…** (1 connections) — `server/time/time_event_consumer.py`
- **Dispatch hour tick events to each dependent subsystem.** (1 connections) — `server/time/time_event_consumer.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [scripts validate calendar load and](scripts_validate_calendar_load_and.md) (3 shared connections)
- [server tests unit time test](server_tests_unit_time_test.md) (2 shared connections)
- [server events event bus](server_events_event_bus.md) (2 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [holidayresolver](holidayresolver.md) (1 shared connections)
- [moduletype](moduletype.md) (1 shared connections)
- [leveluphook](leveluphook.md) (1 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (1 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [maprooms](maprooms.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 47 (76%)
- INFERRED: 15 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*