# .__init__

> 8 nodes

## Key Concepts

- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **.separate_occupants_by_type()** (3 connections) — `server/realtime/room_occupant_manager.py`
- **Any** (3 connections)
- **UUID** (2 connections)
- **Separate occupants into players, NPCs, and all occupants lists. Args:…** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Initialize the room occupant manager. Args: connection_manager:…** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Get the list of occupants in a room. Args: room_id: The room ID…** (1 connections) — `server/realtime/room_occupant_manager.py`

## Relationships

- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [RoomIDUtils](RoomIDUtils.md) (1 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (1 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (1 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)

## Source Files

- `server/realtime/room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*