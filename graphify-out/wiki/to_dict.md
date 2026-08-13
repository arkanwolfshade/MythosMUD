# .to_dict

> 17 nodes

## Key Concepts

- **.to_dict()** (8 connections) — `server/models/room.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **Any** (3 connections)
- **Get list of player IDs currently in the room. Returns: List of player IDs in…** (1 connections) — `server/models/room.py`
- **Get list of object IDs currently in the room. Returns: List of object IDs in…** (1 connections) — `server/models/room.py`
- **Get list of NPC IDs currently in the room. Returns: List of NPC IDs in the room** (1 connections) — `server/models/room.py`
- **Get the total number of occupants in the room. Returns: Total count of players,…** (1 connections) — `server/models/room.py`
- **Check if the room has no occupants. Returns: True if the room is empty, False…** (1 connections) — `server/models/room.py`
- **Get list of containers in this room. Returns: List of container data…** (1 connections) — `server/models/room.py`
- **Convert the room to a dictionary representation. Returns: Dictionary containing…** (1 connections) — `server/models/room.py`
- **Initialize a Room from JSON data. Args: room_data: Dictionary containing room…** (1 connections) — `server/models/room.py`

## Relationships

- [Room](Room.md) (8 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/models/room.py`

## Audit Trail

- EXTRACTED: 27 (90%)
- INFERRED: 3 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*