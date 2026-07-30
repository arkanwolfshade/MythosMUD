# ensure database directory()

> 33 nodes

## Key Concepts

- **NPCMovementIntegration** (24 connections) — `server/npc/movement_integration.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **._get_room_objects()** (4 connections) — `server/npc/movement_integration.py`
- **._update_room_occupancy()** (4 connections) — `server/npc/movement_integration.py`
- **._update_npc_instance_room_tracking()** (4 connections) — `server/npc/movement_integration.py`
- **._get_destination_subzone()** (4 connections) — `server/npc/movement_integration.py`
- **._validate_room_ids()** (3 connections) — `server/npc/movement_integration.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/movement_integration.py`
- **.validate_subzone_boundary()** (3 connections) — `server/npc/movement_integration.py`
- **Room** (2 connections)
- **.get_npc_room()** (2 connections) — `server/npc/movement_integration.py`
- **.get_room_npcs()** (2 connections) — `server/npc/movement_integration.py`
- **.validate_npc_movement()** (2 connections) — `server/npc/movement_integration.py`
- **.get_available_exits()** (2 connections) — `server/npc/movement_integration.py`
- **.find_path_between_rooms()** (2 connections) — `server/npc/movement_integration.py`
- **Initialize the idle movement handler.          Args:             event_bus: O** (1 connections) — `server/npc/idle_movement.py`
- **Integration layer for NPC movement with existing game systems.      This class** (1 connections) — `server/npc/movement_integration.py`
- **Initialize NPC movement integration.          Args:             event_bus: Op** (1 connections) — `server/npc/movement_integration.py`
- **Validate room IDs for NPC movement.          Args:             npc_id: ID of** (1 connections) — `server/npc/movement_integration.py`
- **Return True if the NPC is currently in combat (blocks normal movement).** (1 connections) — `server/npc/movement_integration.py`
- **Get room objects and validate they exist.          Args:             npc_id:** (1 connections) — `server/npc/movement_integration.py`
- **Update room occupancy by removing NPC from source and adding to destination.** (1 connections) — `server/npc/movement_integration.py`
- **Update NPC instance room tracking for occupant queries.          Args:** (1 connections) — `server/npc/movement_integration.py`
- *... and 8 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (3 shared connections)
- [datetime](datetime.md) (2 shared connections)
- [get current tick()](get_current_tick%28%29.md) (2 shared connections)
- [Test check all command blocks](Test_check_all_command_blocks.md) (2 shared connections)
- [.get explored rooms()](get_explored_rooms%28%29.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [. get destination subzone()](_get_destination_subzone%28%29.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`

## Audit Trail

- EXTRACTED: 92 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*