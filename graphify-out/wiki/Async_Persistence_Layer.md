# Async Persistence Layer

> 87 nodes

## Key Concepts

- **BaseEvent** (75 connections) — `server/events/event_types.py`
- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **event_serialization.py** (15 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **serialize_event()** (14 connections) — `server/events/event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **DistributedEventBus** (12 connections) — `server/events/distributed_event_bus.py`
- **distributed_event_bus.py** (10 connections) — `server/events/distributed_event_bus.py`
- **test_nats_event_bridge.py** (7 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **Any** (6 connections)
- **_register_event_types()** (6 connections) — `server/events/event_serialization.py`
- **._handle_event()** (6 connections) — `server/npc/event_reaction_system.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **Any** (5 connections)
- **.should_trigger()** (5 connections) — `server/npc/event_reaction_system.py`
- **.execute()** (5 connections) — `server/npc/event_reaction_system.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **.set_nats_service()** (4 connections) — `server/events/distributed_event_bus.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **_convert_value_for_json()** (4 connections) — `server/events/event_serialization.py`
- *... and 62 more nodes in this community*

## Relationships

- [Commands Look Item](Commands_Look_Item.md) (21 shared connections)
- [Client Event Store](Client_Event_Store.md) (18 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (13 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (12 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (8 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (3 shared connections)
- [Lucidity Database Models](Lucidity_Database_Models.md) (2 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (2 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (2 shared connections)
- [Holiday Persistence Models](Holiday_Persistence_Models.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/npc/event_reaction_system.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 347 (93%)
- INFERRED: 27 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*