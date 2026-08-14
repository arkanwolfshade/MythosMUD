# movement_helpers.py

> 27 nodes

## Key Concepts

- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **test_check_player_posture_blocks_sitting()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_exit_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_exit_no_exits()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_exit_target_missing_in_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **Room** (2 connections)
- **Movement validation helpers for MovementService. Cohesive validation and room-…** (1 connections) — `server/game/movement_helpers.py`
- **Validate player is in the from_room, auto-adding if database matches.** (1 connections) — `server/game/movement_helpers.py`
- **Validate that there's a valid exit from the room to the target room.** (1 connections) — `server/game/movement_helpers.py`
- **Extract and validate player ID from player object.** (1 connections) — `server/game/movement_helpers.py`
- **Check if player is in combat (blocks movement).** (1 connections) — `server/game/movement_helpers.py`
- **Check if player posture allows movement (only standing allowed).** (1 connections) — `server/game/movement_helpers.py`
- **Validate rooms, membership, and exit for movement.** (1 connections) — `server/game/movement_service.py`
- **Validate that a movement operation is allowed. Args: player_obj: The player…** (1 connections) — `server/game/movement_service.py`
- **Test check_player_posture blocks non-standing posture.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test validate_exit returns False when room has no exits.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_movement_service.py](test_movement_service.py.md) (11 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [MovementService](MovementService.md) (5 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 74 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*