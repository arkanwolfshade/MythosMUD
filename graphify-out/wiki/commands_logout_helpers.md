# commands logout helpers

> 61 nodes

## Key Concepts

- **NPCMovementIntegration** (50 connections) — `server/npc/movement_integration.py`
- **test_movement_integration.py** (29 connections) — `server/tests/unit/npc/test_movement_integration.py`
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
- **test_init_requires_persistence()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_validate_room_ids_rejects_empty_or_same()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_to_room_success()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_blocked_in_combat()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_objects_missing_room()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_validate_npc_movement()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_and_exits()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- *... and 36 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (8 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [idle movement npc](idle_movement_npc.md) (2 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)
- [schedule services service](schedule_services_service.md) (1 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (1 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/npc/test_movement_integration.py`

## Audit Trail

- EXTRACTED: 199 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*