# PlayerRoomEventHandler

> 25 nodes

## Key Concepts

- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **UUID** (12 connections)
- **.send_occupants_snapshot_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **._prepare_room_data()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_room_state_event()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._log_occupants_info()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.query_room_occupants_snapshot()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._send_room_name_message()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.build_room_occupants_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.subscribe_player_to_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **Subscribe player to room for receiving broadcasts. Args: player_id: The…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Send room name as a message to the Game Info panel. Args: player_id_uuid: The…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Prepare room data for client, removing occupant fields. Args: room: The room…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Send full room update to a player. Args: player_id: The player's ID (UUID or…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Handles room-related player events (entered, left, occupants).** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Log occupants snapshot preparation and sending. Args: player_id_uuid: The…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Build room occupants message for sending to player. Args: room_id: The room ID…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Query room occupants snapshot for a player. Args: player_id_uuid: The player's…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Send occupants snapshot to a player. CRITICAL: This method MUST include NPCs…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Send single authoritative room_state (room metadata + occupants) to a player.…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Build authoritative room_state event for a room (same as…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Send room updates and occupants snapshot to entering player. Args: player_id:…** (1 connections) — `server/realtime/player_event_handlers_room.py`

## Relationships

- [Any](Any.md) (17 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (2 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 66 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*