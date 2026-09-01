# time_event_consumer.py

> 26 nodes

## Key Concepts

- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
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
- **asyncio** (1 connections)
- **fixture** (1 connections)
- **Event fired when the accelerated Mythos clock rolls over to a new hour.** (1 connections) — `server/events/event_types.py`
- **Broadcast a game event to all connected players. Args: event_type: The type of…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Unit tests for MythosTimeEventConsumer hour tick handling.** (1 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **Time event consumer for processing game time events. This module provides the…** (1 connections) — `server/time/time_event_consumer.py`
- **Helper for admin diagnostics.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a holiday entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a schedule entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Create the SSE payload consumed by the client HUD.** (1 connections) — `server/time/time_event_consumer.py`
- **Bridges hour tick events into downstream systems such as NPC schedules and room…** (1 connections) — `server/time/time_event_consumer.py`
- *... and 1 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [HolidayService](HolidayService.md) (6 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [time.py](time.py.md) (4 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (4 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [pydantic.md](pydantic.md.md) (2 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [._bind_event_type](_bind_event_type.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 78 (85%)
- INFERRED: 14 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*