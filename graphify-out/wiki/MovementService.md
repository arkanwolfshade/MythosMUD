# MovementService

> 62 nodes

## Key Concepts

- **MovementService** (47 connections) — `server/game/movement_service.py`
- **UUID** (18 connections)
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **.move_player()** (7 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **.get_player_room()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_added_player_room()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [PlayerCombatService](PlayerCombatService.md) (11 shared connections)
- [log_and_raise](log_and_raise.md) (9 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [SpellEffects](SpellEffects.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [follow_movement.py](follow_movement.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 139 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*