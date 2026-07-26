# MovementService

> 88 nodes · cohesion 0.03

## Key Concepts

- **MovementService** (43 connections) — `server/game/movement_service.py`
- **test_movement_service.py** (25 connections) — `server/tests/unit/game/test_movement_service.py`
- **UUID** (16 connections)
- **.move_player()** (14 connections) — `server/game/movement_service.py`
- **._validate_movement()** (9 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (8 connections) — `server/game/movement_service.py`
- **.get_player_room()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (6 connections) — `server/game/movement_service.py`
- **._validate_player_room_membership()** (6 connections) — `server/game/movement_service.py`
- **._check_combat_state()** (5 connections) — `server/game/movement_service.py`
- **._check_player_posture()** (5 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (5 connections) — `server/game/movement_service.py`
- **._extract_player_id()** (4 connections) — `server/game/movement_service.py`
- **.get_room_players()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._validate_exit()** (4 connections) — `server/game/movement_service.py`
- **.validate_player_location()** (4 connections) — `server/game/movement_service.py`
- **Any** (4 connections)
- **Room** (4 connections)
- **movement_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_empty_player_id()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 63 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (19 shared connections)
- [ValidationError](ValidationError.md) (10 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [__init__.py](__init__.py.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)
- [monitoring.py](monitoring.py.md) (2 shared connections)
- [FollowService](FollowService.md) (1 shared connections)
- [SpellRegistry](SpellRegistry.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 272 (94%)
- INFERRED: 18 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*