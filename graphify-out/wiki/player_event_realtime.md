# player event realtime

> 53 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **Any** (7 connections)
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_info()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.process_dict_occupant()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.__init__()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.normalize_player_id()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **._extract_name_from_occupant()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.extract_occupant_names()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.build_occupants_snapshot_data()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.normalize_event_ids()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.add_valid_name_to_lists()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.count_occupants_by_type()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.is_player_disconnecting()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.is_player_in_grace_period()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **mock_utils()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **mock_utils()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **player_event_handler_utils()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_string_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- *... and 28 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (14 shared connections)
- [player respawn event](player_respawn_event.md) (8 shared connections)
- [player room realtime](player_room_realtime.md) (3 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (2 shared connections)
- [realtime real time](realtime_real_time.md) (2 shared connections)
- [player event handlers](player_event_handlers.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 165 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*