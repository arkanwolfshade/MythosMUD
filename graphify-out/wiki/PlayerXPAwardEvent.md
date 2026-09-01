# PlayerXPAwardEvent

> 71 nodes

## Key Concepts

- **PlayerXPAwardEvent** (27 connections) — `server/events/event_types.py`
- **event_serialization.py** (20 connections) — `server/events/event_serialization.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **test_nats_event_bridge.py** (10 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **_register_event_types()** (6 connections) — `server/events/event_serialization.py`
- **_convert_value_from_json()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_handle_nats_message_injects_remote_origin()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_publish_adds_origin_and_calls_nats()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **_init_kwargs_from_event_data()** (4 connections) — `server/events/event_serialization.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **._subject_for_event()** (4 connections) — `server/events/nats_event_bridge.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **test_handle_nats_message_bad_payload_logs_warning()** (4 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- *... and 46 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (17 shared connections)
- [event_types.py](event_types.py.md) (13 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (7 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (2 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 152 (88%)
- INFERRED: 20 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*