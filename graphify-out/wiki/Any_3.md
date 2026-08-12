# Any

> 17 nodes

## Key Concepts

- **Any** (10 connections)
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_left()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_entered_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_left_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **._process_player_entered_event()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.unsubscribe_player_from_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **Broadcast player entered message to room occupants. Args: message: The player…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Initialize room event handler. Args: connection_manager: ConnectionManager…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Process player entered event and return player name and normalized IDs. Args:…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Handle player entering a room with enhanced synchronization. Args: event: The…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Unsubscribe a player from a room. Args: player_id: The player's ID (UUID or…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Log player movement for AI processing. Args: player_id: The player's ID…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Broadcast player left message to room occupants. Args: message: The player left…** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Handle player leaving a room with enhanced synchronization. Args: event: The…** (1 connections) — `server/realtime/player_event_handlers_room.py`

## Relationships

- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (17 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*