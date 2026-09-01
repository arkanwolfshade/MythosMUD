# PlayerRoomEventHandler

> 63 nodes

## Key Concepts

- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **UUID** (15 connections)
- **_as_map()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_entered()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **_snapshot_payload()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **OccupantsUpdateFn** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **RoomConnectionManager** (9 connections) — `server/realtime/player_event_handlers_room.py`
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
- **Protocol** (6 connections)
- **_NamedRoom** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **_as_occupant_snap()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._send_room_name_message()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_entered()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_left()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.broadcast_player_entered_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 38 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (15 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (11 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (5 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 143 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*