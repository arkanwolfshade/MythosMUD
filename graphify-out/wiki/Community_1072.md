# Community 1072

> 13 nodes

## Key Concepts

- **.to_dict()** (8 connections) — `server/models/room.py`
- **.get_containers()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **Any** (3 connections)
- **Get list of object IDs currently in the room. Returns: List of object IDs in…** (1 connections) — `server/models/room.py`
- **Get list of NPC IDs currently in the room. Returns: List of NPC IDs in the room** (1 connections) — `server/models/room.py`
- **Get the total number of occupants in the room. Returns: Total count of players,…** (1 connections) — `server/models/room.py`
- **Check if the room has no occupants. Returns: True if the room is empty, False…** (1 connections) — `server/models/room.py`
- **Get list of containers in this room. Returns: List of container data…** (1 connections) — `server/models/room.py`
- **Convert the room to a dictionary representation. Returns: Dictionary containing…** (1 connections) — `server/models/room.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Community 45](Community_45.md) (1 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (1 shared connections)

## Source Files

- `server/models/room.py`

## Audit Trail

- EXTRACTED: 21 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*