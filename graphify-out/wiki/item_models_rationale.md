# item models rationale

> 108 nodes

## Key Concepts

- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **test_player_event_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **event_serialization.py** (12 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (6 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_convert_value_for_json()** (4 connections) — `server/events/event_serialization.py`
- **Any** (4 connections)
- **_convert_value_from_json()** (4 connections) — `server/events/event_serialization.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **Any** (3 connections)
- **._handle_player_xp_awarded()** (3 connections) — `server/realtime/event_handler.py`
- **.handle_player_xp_awarded()** (3 connections) — `server/realtime/player_event_handlers.py`
- **test_deserialize_unknown_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_deserialize_missing_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_non_base_event_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_event_handler_handle_player_xp_awarded()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **player_event_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- *... and 83 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (28 shared connections)
- [NATS Messaging](NATS_Messaging.md) (17 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (3 shared connections)
- [player death service](player_death_service.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [combat validator validators](combat_validator_validators.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 313 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*