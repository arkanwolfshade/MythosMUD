# services passive lucidity

> 11 nodes

## Key Concepts

- **UUID** (6 connections)
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

## Relationships

- [room models instance](room_models_instance.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)

## Source Files

- `server/models/room.py`

## Audit Trail

- EXTRACTED: 28 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*