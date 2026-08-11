# Tailwind UI Migration Plan

> 197 nodes

## Key Concepts

- **BaseEvent** (75 connections) — `server/events/event_types.py`
- **event_types.py** (74 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (68 connections) — `server/events/event_types.py`
- **test_event_bus.py** (45 connections) — `server/tests/unit/events/test_event_bus.py`
- **event_bus.py** (29 connections) — `server/events/event_bus.py`
- **MockEventClass** (29 connections) — `server/tests/unit/events/test_event_bus.py`
- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **event_serialization.py** (15 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **serialize_event()** (14 connections) — `server/events/event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **._subscribe_to_events()** (14 connections) — `server/npc/event_reaction_system.py`
- **tick_scheduler.py** (14 connections) — `server/time/tick_scheduler.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **test_follow_flow.py** (13 connections) — `server/tests/integration/test_follow_flow.py`
- **__init__.py** (11 connections) — `server/events/__init__.py`
- **NPCSpoke** (11 connections) — `server/events/event_types.py`
- **NPCListened** (11 connections) — `server/events/event_types.py`
- **communication_integration.py** (11 connections) — `server/npc/communication_integration.py`
- **distributed_event_bus.py** (10 connections) — `server/events/distributed_event_bus.py`
- **ObjectAddedToRoom** (9 connections) — `server/events/event_types.py`
- **ObjectRemovedFromRoom** (9 connections) — `server/events/event_types.py`
- **NPCTookDamage** (8 connections) — `server/events/event_types.py`
- **test_nats_event_bridge.py** (7 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **Any** (6 connections)
- *... and 172 more nodes in this community*

## Relationships

- [Realtime Service Bundle](Realtime_Service_Bundle.md) (43 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (28 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (21 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (19 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (15 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (14 shared connections)
- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (9 shared connections)
- [Game Chat Moderation](Game_Chat_Moderation.md) (9 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (7 shared connections)
- [Lucidity Database Models](Lucidity_Database_Models.md) (7 shared connections)
- [Health Check Models](Health_Check_Models.md) (6 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 778 (88%)
- INFERRED: 103 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*