# NPC Movement Integration

> 29 nodes · cohesion 0.09

## Key Concepts

- **NPCMovementIntegration** (24 connections) — `server/npc/movement_integration.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **._get_destination_subzone()** (4 connections) — `server/npc/movement_integration.py`
- **._get_room_objects()** (4 connections) — `server/npc/movement_integration.py`
- **._update_npc_instance_room_tracking()** (4 connections) — `server/npc/movement_integration.py`
- **._update_room_occupancy()** (4 connections) — `server/npc/movement_integration.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/movement_integration.py`
- **._validate_room_ids()** (3 connections) — `server/npc/movement_integration.py`
- **.validate_subzone_boundary()** (3 connections) — `server/npc/movement_integration.py`
- **.find_path_between_rooms()** (2 connections) — `server/npc/movement_integration.py`
- **.get_available_exits()** (2 connections) — `server/npc/movement_integration.py`
- **.get_npc_room()** (2 connections) — `server/npc/movement_integration.py`
- **.get_room_npcs()** (2 connections) — `server/npc/movement_integration.py`
- **.validate_npc_movement()** (2 connections) — `server/npc/movement_integration.py`
- **Room** (2 connections)
- **Get room objects and validate they exist.          Args:             npc_id:** (1 connections) — `server/npc/movement_integration.py`
- **Update room occupancy by removing NPC from source and adding to destination.** (1 connections) — `server/npc/movement_integration.py`
- **Update NPC instance room tracking for occupant queries.          Args:** (1 connections) — `server/npc/movement_integration.py`
- **Move an NPC to a different room with full integration.          This method pr** (1 connections) — `server/npc/movement_integration.py`
- **Get the current room ID for an NPC.          Args:             npc_id: ID of** (1 connections) — `server/npc/movement_integration.py`
- **Get list of NPC IDs in a room.          Args:             room_id: ID of the** (1 connections) — `server/npc/movement_integration.py`
- **Validate that an NPC can move between rooms.          Args:             npc_i** (1 connections) — `server/npc/movement_integration.py`
- **Integration layer for NPC movement with existing game systems.      This class** (1 connections) — `server/npc/movement_integration.py`
- **Get available exits from a room.          Args:             room_id: ID of th** (1 connections) — `server/npc/movement_integration.py`
- **Find a path between two rooms.          This is a simple implementation that c** (1 connections) — `server/npc/movement_integration.py`
- *... and 4 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)

## Source Files

- `server/npc/movement_integration.py`

## Audit Trail

- EXTRACTED: 80 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*