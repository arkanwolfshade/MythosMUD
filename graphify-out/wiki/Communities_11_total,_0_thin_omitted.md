# Communities (11 total, 0 thin omitted)

> 24 nodes · cohesion 0.14

## Key Concepts

- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **test_time_event_consumer.py** (8 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **._handle_tick()** (5 connections) — `server/time/time_event_consumer.py`
- **test_handle_tick_updates_room_and_broadcasts()** (4 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._serialize_holiday()** (4 connections) — `server/time/time_event_consumer.py`
- **._serialize_schedule()** (4 connections) — `server/time/time_event_consumer.py`
- **Any** (4 connections)
- **test_describe_state()** (3 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **tick_event()** (3 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **.describe_state()** (3 connections) — `server/time/time_event_consumer.py`
- **Event fired when the accelerated Mythos clock rolls over to a new hour.** (1 connections) — `server/events/event_types.py`
- **asyncio** (1 connections)
- **fixture** (1 connections)
- **Unit tests for MythosTimeEventConsumer hour tick handling.** (1 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **Time event consumer for processing game time events. This module provides the…** (1 connections) — `server/time/time_event_consumer.py`
- **Helper for admin diagnostics.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a holiday entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a schedule entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Create the SSE payload consumed by the client HUD.** (1 connections) — `server/time/time_event_consumer.py`
- **Bridges hour tick events into downstream systems such as NPC schedules and room…** (1 connections) — `server/time/time_event_consumer.py`
- **Dispatch hour tick events to each dependent subsystem.** (1 connections) — `server/time/time_event_consumer.py`

## Relationships

- [OccupantFormatter](OccupantFormatter.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [EventHandler](EventHandler.md) (3 shared connections)
- [BaseEvent](BaseEvent.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (2 shared connections)
- [test_admin_teleport_commands.py](test_admin_teleport_commands.py.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 69 (84%)
- INFERRED: 13 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*