# UUID

> 13 nodes

## Key Concepts

- **UUID** (6 connections)
- **_ensure_player_in_room_occupancy()** (6 connections) — `server/realtime/websocket_helpers.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **Add a player to the room and trigger event.          Args:             player_id** (1 connections) — `server/models/room.py`
- **Add a player to the room without triggering an event.          This method is us** (1 connections) — `server/models/room.py`
- **Remove a player from the room without triggering an event.          This method** (1 connections) — `server/models/room.py`
- **Remove a player from the room and trigger event.          Args:             play** (1 connections) — `server/models/room.py`
- **Check if a player is in the room.          Args:             player_id: The ID o** (1 connections) — `server/models/room.py`
- **If the room tracks occupancy, register the player when missing.** (1 connections) — `server/realtime/websocket_helpers.py`

## Relationships

- [spawn defaults](spawn_defaults.md) (6 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)

## Source Files

- `server/models/room.py`
- `server/realtime/websocket_helpers.py`

## Audit Trail

- EXTRACTED: 33 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*