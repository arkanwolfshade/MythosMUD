# NPCMovementIntegration

> 31 nodes

## Key Concepts

- **NPCMovementIntegration** (24 connections) — `server/npc/movement_integration.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **._get_destination_subzone()** (4 connections) — `server/npc/movement_integration.py`
- **._get_room_objects()** (4 connections) — `server/npc/movement_integration.py`
- **._publish_movement_events()** (4 connections) — `server/npc/movement_integration.py`
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
- **Get room objects and validate they exist. Args: npc_id: ID of the NPC…** (1 connections) — `server/npc/movement_integration.py`
- **Update room occupancy by removing NPC from source and adding to destination.…** (1 connections) — `server/npc/movement_integration.py`
- **Update NPC instance room tracking for occupant queries. Args: npc_id: ID of the…** (1 connections) — `server/npc/movement_integration.py`
- **Move an NPC to a different room with full integration. This method provides…** (1 connections) — `server/npc/movement_integration.py`
- **Publish NPC movement events. Args: npc_id: ID of the NPC from_room_id: Source…** (1 connections) — `server/npc/movement_integration.py`
- **Get the current room ID for an NPC. Args: npc_id: ID of the NPC Returns:…** (1 connections) — `server/npc/movement_integration.py`
- **Get list of NPC IDs in a room. Args: room_id: ID of the room Returns:…** (1 connections) — `server/npc/movement_integration.py`
- **Validate that an NPC can move between rooms. Args: npc_id: ID of the NPC…** (1 connections) — `server/npc/movement_integration.py`
- **Integration layer for NPC movement with existing game systems. This class…** (1 connections) — `server/npc/movement_integration.py`
- *... and 6 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (1 shared connections)

## Source Files

- `server/npc/movement_integration.py`

## Audit Trail

- EXTRACTED: 48 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*