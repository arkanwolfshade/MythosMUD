# commands logout helpers

> 39 nodes

## Key Concepts

- **NPCMovementIntegration** (24 connections) — `server/npc/movement_integration.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
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
- *... and 14 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (4 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [config models player](config_models_player.md) (2 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (1 shared connections)
- [health models rationale](health_models_rationale.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 107 (89%)
- INFERRED: 13 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*