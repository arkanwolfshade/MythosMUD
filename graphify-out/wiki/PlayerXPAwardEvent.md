# PlayerXPAwardEvent

> 54 nodes

## Key Concepts

- **PlayerXPAwardEvent** (30 connections) — `server/services/player_combat_service.py`
- **event_serialization.py** (20 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (16 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **_convert_value_from_json()** (5 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **_init_kwargs_from_event_data()** (4 connections) — `server/events/event_serialization.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_convert_value_for_json()** (3 connections) — `server/events/event_serialization.py`
- **_copy_public_event_attrs()** (3 connections) — `server/events/event_serialization.py`
- **_event_class_from_payload()** (3 connections) — `server/events/event_serialization.py`
- **_register_event_class()** (3 connections) — `server/events/event_serialization.py`
- **._handle_player_xp_awarded()** (3 connections) — `server/realtime/event_handler.py`
- **.handle_player_xp_awarded()** (3 connections) — `server/realtime/player_event_handlers.py`
- **test_deserialize_missing_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- *... and 29 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (13 shared connections)
- [EventBus](EventBus.md) (13 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (10 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (2 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [emit_posture_change](emit_posture_change.md) (1 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 122 (88%)
- INFERRED: 17 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*