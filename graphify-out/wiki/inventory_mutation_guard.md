# inventory mutation guard

> 72 nodes

## Key Concepts

- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **UUID** (12 connections)
- **Any** (10 connections)
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_left()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **._prepare_room_data()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._send_room_name_message()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._log_occupants_info()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.query_room_occupants_snapshot()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_room_state_event()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_entered_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.subscribe_player_to_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.build_room_occupants_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **._process_player_entered_event()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.unsubscribe_player_from_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_left_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **mock_utils()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **player_room_event_handler()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- *... and 47 more nodes in this community*

## Relationships

- [Player Name Validation](Player_Name_Validation.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (3 shared connections)
- [player occupant processor](player_occupant_processor.md) (2 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 237 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*