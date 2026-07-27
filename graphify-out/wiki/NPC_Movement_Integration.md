# NPC Movement Integration

> 59 nodes · cohesion 0.04

## Key Concepts

- **NPCMovementIntegration** (28 connections) — `server/npc/movement_integration.py`
- **CommunicationIntegrationProtocol** (10 connections) — `server/npc/npc_protocols.py`
- **CombatIntegrationProtocol** (8 connections) — `server/npc/npc_protocols.py`
- **BehaviorEngine** (7 connections) — `server/npc/npc_base.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **NPCDefinition** (6 connections) — `server/npc/npc_base.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **._get_destination_subzone()** (4 connections) — `server/npc/movement_integration.py`
- **._get_room_objects()** (4 connections) — `server/npc/movement_integration.py`
- **._publish_movement_events()** (4 connections) — `server/npc/movement_integration.py`
- **._update_npc_instance_room_tracking()** (4 connections) — `server/npc/movement_integration.py`
- **._update_room_occupancy()** (4 connections) — `server/npc/movement_integration.py`
- **npc_protocols.py** (4 connections) — `server/npc/npc_protocols.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/movement_integration.py`
- **._validate_room_ids()** (3 connections) — `server/npc/movement_integration.py`
- **.validate_subzone_boundary()** (3 connections) — `server/npc/movement_integration.py`
- **.from_dict()** (3 connections) — `server/npc/npc_base.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **.find_path_between_rooms()** (2 connections) — `server/npc/movement_integration.py`
- **.get_available_exits()** (2 connections) — `server/npc/movement_integration.py`
- **.get_npc_room()** (2 connections) — `server/npc/movement_integration.py`
- **.get_room_npcs()** (2 connections) — `server/npc/movement_integration.py`
- **.validate_npc_movement()** (2 connections) — `server/npc/movement_integration.py`
- **.handle_npc_death()** (2 connections) — `server/npc/npc_protocols.py`
- *... and 34 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (7 shared connections)
- [[Aggressive Mob NPC]] (6 shared connections)
- [[NPC Death Lifecycle]] (6 shared connections)
- [[Npc Behavior Engine]] (2 shared connections)
- [[Player Combat XP]] (2 shared connections)
- [[Npc Config Parsing]] (1 shared connections)
- [[Chat NATS Publisher]] (1 shared connections)
- [[NPC Services Bundle]] (1 shared connections)
- [[NPC Occupant Verification]] (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_protocols.py`

## Audit Trail

- EXTRACTED: 143 (86%)
- INFERRED: 24 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
