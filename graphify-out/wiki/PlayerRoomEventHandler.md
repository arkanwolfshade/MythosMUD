# PlayerRoomEventHandler

> 50 nodes

## Key Concepts

- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **UUID** (15 connections)
- **_as_map()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_entered()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **_snapshot_payload()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **JsonMap** (9 connections)
- **.handle_player_left()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **._prepare_room_data()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_room_state_event()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **._log_occupants_info()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.query_room_occupants_snapshot()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **_as_occupant_snap()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._send_room_name_message()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_entered_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_left_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.build_room_occupants_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **._process_player_entered_event()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.subscribe_player_to_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.unsubscribe_player_from_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **OccupantSnap** (4 connections)
- *... and 25 more nodes in this community*

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (22 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 118 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*