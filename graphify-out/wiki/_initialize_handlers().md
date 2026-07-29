# . initialize handlers()

> 116 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **UUID** (12 connections)
- **Any** (10 connections)
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **.__init__()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_left()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **Any** (7 connections)
- **._prepare_room_data()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **UUID** (6 connections)
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._send_room_name_message()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._log_occupants_info()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.query_room_occupants_snapshot()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_room_state_event()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_player_info()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.process_dict_occupant()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.broadcast_player_entered_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 91 more nodes in this community*

## Relationships

- [Any](Any.md) (19 shared connections)
- [UUID](UUID.md) (6 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (4 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (4 shared connections)
- [disconnect grace period](disconnect_grace_period.md) (4 shared connections)
- [test player event handlers respawn](test_player_event_handlers_respawn.md) (2 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (2 shared connections)
- [test player event handlers utils](test_player_event_handlers_utils.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [TypedDict](TypedDict.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 383 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*