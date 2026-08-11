# Combat Messaging Base

> 27 nodes

## Key Concepts

- **time_event_consumer.py** (24 connections) — `server/time/time_event_consumer.py`
- **MythosTimeEventConsumer** (23 connections) — `server/time/time_event_consumer.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **MythosHourTickEvent** (12 connections) — `server/events/event_types.py`
- **.__init__()** (8 connections) — `server/time/time_event_consumer.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **._handle_tick()** (6 connections) — `server/time/time_event_consumer.py`
- **_HolidayLoadResult** (5 connections) — `server/services/holiday_service.py`
- **Any** (5 connections)
- **._serialize_holiday()** (4 connections) — `server/time/time_event_consumer.py`
- **._serialize_schedule()** (4 connections) — `server/time/time_event_consumer.py`
- **.describe_state()** (3 connections) — `server/time/time_event_consumer.py`
- **.get_current_mythos_datetime()** (3 connections) — `server/time/time_service.py`
- **.format_clock()** (3 connections) — `server/time/time_service.py`
- **Event fired when the accelerated Mythos clock rolls over to a new hour.** (1 connections) — `server/events/event_types.py`
- **TypedDict** (1 connections)
- **Time event consumer for processing game time events.  This module provides the T** (1 connections) — `server/time/time_event_consumer.py`
- **Bridges hour tick events into downstream systems such as NPC schedules and room** (1 connections) — `server/time/time_event_consumer.py`
- **Dispatch hour tick events to each dependent subsystem.** (1 connections) — `server/time/time_event_consumer.py`
- **Helper for admin diagnostics.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a holiday entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Serialize a schedule entry for the SSE payload.** (1 connections) — `server/time/time_event_consumer.py`
- **Create the SSE payload consumed by the client HUD.** (1 connections) — `server/time/time_event_consumer.py`
- **Protocol** (1 connections)
- **Minimal chronicle contract required by downstream systems.      The canonical My** (1 connections) — `server/time/time_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [Spell Effects Tests](Spell_Effects_Tests.md) (9 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (5 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (5 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (5 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (3 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/services/holiday_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 112 (84%)
- INFERRED: 21 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*