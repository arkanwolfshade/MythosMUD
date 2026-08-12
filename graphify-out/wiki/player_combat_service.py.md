# player_combat_service.py

> 70 nodes

## Key Concepts

- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **PlayerXPAwardEvent** (32 connections) — `server/services/player_combat_service.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **PlayerDiedEvent** (16 connections) — `server/events/event_types.py`
- **event_serialization.py** (15 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (14 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (9 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **Any** (6 connections)
- **Protocol** (6 connections)
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_convert_value_for_json()** (4 connections) — `server/events/event_serialization.py`
- **_convert_value_from_json()** (4 connections) — `server/events/event_serialization.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_register_event_class()** (3 connections) — `server/events/event_serialization.py`
- *... and 45 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (47 shared connections)
- [test_player_event_handlers_state.py](test_player_event_handlers_state.py.md) (8 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (7 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (7 shared connections)
- [build_event](build_event.md) (7 shared connections)
- [PlayerStateEventHandler](PlayerStateEventHandler.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (4 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (4 shared connections)
- [NATSEventBusBridge](NATSEventBusBridge.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 317 (95%)
- INFERRED: 18 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*