# .get_room_occupants

> 6 nodes

## Key Concepts

- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **.separate_occupants_by_type()** (3 connections) — `server/realtime/room_occupant_manager.py`
- **Any** (3 connections)
- **UUID** (2 connections)
- **Separate occupants into players, NPCs, and all occupants lists. Args:…** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Get the list of occupants in a room. Args: room_id: The room ID…** (1 connections) — `server/realtime/room_occupant_manager.py`

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (2 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (2 shared connections)

## Source Files

- `server/realtime/room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*