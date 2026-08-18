# RoomOccupantManager

> 10 nodes

## Key Concepts

- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **.separate_occupants_by_type()** (3 connections) — `server/realtime/room_occupant_manager.py`
- **Any** (3 connections)
- **UUID** (2 connections)
- **Separate occupants into players, NPCs, and all occupants lists. Args:…** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Manages room occupant queries and processing. Handles both players and NPCs,…** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Initialize the room occupant manager. Args: connection_manager:…** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Get the list of occupants in a room. Args: room_id: The room ID…** (1 connections) — `server/realtime/room_occupant_manager.py`

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (9 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (6 shared connections)
- [test_room_occupant_manager.py](test_room_occupant_manager.py.md) (3 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (2 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (2 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 25 (69%)
- INFERRED: 11 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*