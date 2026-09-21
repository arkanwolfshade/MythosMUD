# NPCMovementIntegration

> 37 nodes

## Key Concepts

- **NPCMovementIntegration** (50 connections) — `server/npc/movement_integration.py`
- **test_movement_integration.py** (29 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **.find_path_between_rooms()** (2 connections) — `server/npc/movement_integration.py`
- **.get_room_npcs()** (2 connections) — `server/npc/movement_integration.py`
- **.validate_npc_movement()** (2 connections) — `server/npc/movement_integration.py`
- **test_find_path_direct_connection()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_find_path_returns_none_without_connection()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_available_exits_empty_when_missing()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_destination_subzone_from_room_id()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_npc_room_returns_none()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_and_exits()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_empty_when_missing()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_objects_missing_destination()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_objects_missing_room()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_init_requires_persistence()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_is_npc_in_combat_true()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_blocked_in_combat()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_exception_returns_false()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_to_room_success()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_publish_movement_events()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_publish_movement_events_handles_publish_error()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_publish_movement_events_skips_without_bus()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_update_npc_instance_room_tracking()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_update_room_occupancy_skips_when_already_placed()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- *... and 12 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (8 shared connections)
- [.move_npc_to_room](move_npc_to_room.md) (6 shared connections)
- [._get_destination_subzone](_get_destination_subzone.md) (2 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (2 shared connections)
- [.get_npc_room](get_npc_room.md) (1 shared connections)
- [.get_available_exits](get_available_exits.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [persistence](persistence.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/npc/test_movement_integration.py`

## Audit Trail

- EXTRACTED: 83 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*