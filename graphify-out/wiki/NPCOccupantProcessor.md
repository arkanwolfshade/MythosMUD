# NPCOccupantProcessor

> 6 nodes

## Key Concepts

- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **Any** (3 connections)
- **.separate_occupants_by_type()** (3 connections) — `server/realtime/room_occupant_manager.py`
- **UUID** (2 connections)
- **Get the list of occupants in a room.          Args:             room_id: The roo** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Separate occupants into players, NPCs, and all occupants lists.          Args:** (1 connections) — `server/realtime/room_occupant_manager.py`

## Relationships

- [world](world.md) (2 shared connections)
- [.get instance()](get_instance%28%29.md) (2 shared connections)

## Source Files

- `server/realtime/room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*