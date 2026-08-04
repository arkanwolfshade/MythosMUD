# commands logout helpers

> 44 nodes

## Key Concepts

- **NPCMovementIntegration** (50 connections) — `server/npc/movement_integration.py`
- **test_movement_integration.py** (29 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **._get_destination_subzone()** (4 connections) — `server/npc/movement_integration.py`
- **.validate_subzone_boundary()** (3 connections) — `server/npc/movement_integration.py`
- **.get_npc_room()** (2 connections) — `server/npc/movement_integration.py`
- **.get_room_npcs()** (2 connections) — `server/npc/movement_integration.py`
- **.validate_npc_movement()** (2 connections) — `server/npc/movement_integration.py`
- **.get_available_exits()** (2 connections) — `server/npc/movement_integration.py`
- **.find_path_between_rooms()** (2 connections) — `server/npc/movement_integration.py`
- **test_init_requires_persistence()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_validate_room_ids_rejects_empty_or_same()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_to_room_success()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_blocked_in_combat()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_objects_missing_room()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_validate_npc_movement()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_and_exits()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_find_path_direct_connection()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_validate_subzone_boundary()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_publish_movement_events()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_npc_room_returns_none()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_objects_missing_destination()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_update_room_occupancy_skips_when_already_placed()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_exception_returns_false()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_publish_movement_events_skips_without_bus()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_publish_movement_events_handles_publish_error()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- *... and 19 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (2 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)
- [idle movement npc](idle_movement_npc.md) (1 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (1 shared connections)

## Source Files

- `server/npc/movement_integration.py`
- `server/tests/unit/npc/test_movement_integration.py`

## Audit Trail

- EXTRACTED: 154 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*