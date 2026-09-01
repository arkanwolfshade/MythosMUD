# NPCMovementIntegration

> 62 nodes

## Key Concepts

- **NPCMovementIntegration** (50 connections) — `server/npc/movement_integration.py`
- **test_movement_integration.py** (30 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
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
- **persistence()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_find_path_direct_connection()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_find_path_returns_none_without_connection()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_available_exits_empty_when_missing()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_destination_subzone_from_room_id()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_npc_room_returns_none()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_and_exits()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_empty_when_missing()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- *... and 37 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (7 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (1 shared connections)
- [idle_movement.py](idle_movement.py.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/npc/test_movement_integration.py`

## Audit Trail

- EXTRACTED: 109 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*