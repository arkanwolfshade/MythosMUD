# 🟡 HIGH PRIORITY ISSUES

> 11 nodes

## Key Concepts

- **UUID** (6 connections)
- **.player_entered()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.has_player()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **Add a player to the room without triggering an event. This method is used for…** (1 connections) — `server/models/room.py`
- **Remove a player from the room without triggering an event. This method is used…** (1 connections) — `server/models/room.py`
- **Remove a player from the room and trigger event. Args: player_id: The ID of the…** (1 connections) — `server/models/room.py`
- **Check if a player is in the room. Args: player_id: The ID of the player to…** (1 connections) — `server/models/room.py`
- **Add a player to the room and trigger event. Args: player_id: The ID of the…** (1 connections) — `server/models/room.py`

## Relationships

- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)

## Source Files

- `server/models/room.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*