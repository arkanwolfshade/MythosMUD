# . is npc in combat()

> 39 nodes

## Key Concepts

- **NPCMovementIntegration** (24 connections) — `server/npc/movement_integration.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._get_room_objects()** (4 connections) — `server/npc/movement_integration.py`
- **._update_room_occupancy()** (4 connections) — `server/npc/movement_integration.py`
- **._update_npc_instance_room_tracking()** (4 connections) — `server/npc/movement_integration.py`
- **._publish_movement_events()** (4 connections) — `server/npc/movement_integration.py`
- **._validate_room_ids()** (3 connections) — `server/npc/movement_integration.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/movement_integration.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/npc_base.py`
- **._move_simple()** (3 connections) — `server/npc/npc_base.py`
- **Room** (2 connections)
- **.get_npc_room()** (2 connections) — `server/npc/movement_integration.py`
- **.get_room_npcs()** (2 connections) — `server/npc/movement_integration.py`
- **.validate_npc_movement()** (2 connections) — `server/npc/movement_integration.py`
- **.get_available_exits()** (2 connections) — `server/npc/movement_integration.py`
- **.find_path_between_rooms()** (2 connections) — `server/npc/movement_integration.py`
- **Initialize the idle movement handler.          Args:             event_bus: O** (1 connections) — `server/npc/idle_movement.py`
- **Integration layer for NPC movement with existing game systems.      This class** (1 connections) — `server/npc/movement_integration.py`
- **Validate room IDs for NPC movement.          Args:             npc_id: ID of** (1 connections) — `server/npc/movement_integration.py`
- **Return True if the NPC is currently in combat (blocks normal movement).** (1 connections) — `server/npc/movement_integration.py`
- **Get room objects and validate they exist.          Args:             npc_id:** (1 connections) — `server/npc/movement_integration.py`
- *... and 14 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (9 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [cfg float()](cfg_float%28%29.md) (2 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [. get destination subzone()](_get_destination_subzone%28%29.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (1 shared connections)
- [. repr ()](_repr_%28%29.md) (1 shared connections)
- [.get instance()](get_instance%28%29.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 107 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*