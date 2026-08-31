# movement_service.py

> 23 nodes

## Key Concepts

- **movement_service.py** (36 connections) — `server/game/movement_service.py`
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
- **test_validate_exit_target_missing_in_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **Room** (2 connections)
- **Movement validation helpers for MovementService. Cohesive validation and room-…** (1 connections) — `server/game/movement_helpers.py`
- **Validate player is in the from_room, auto-adding if database matches.** (1 connections) — `server/game/movement_helpers.py`
- **Validate that there's a valid exit from the room to the target room.** (1 connections) — `server/game/movement_helpers.py`
- **Extract and validate player ID from player object.** (1 connections) — `server/game/movement_helpers.py`
- **Check if player is in combat (blocks movement).** (1 connections) — `server/game/movement_helpers.py`
- **Check if player posture allows movement (only standing allowed).** (1 connections) — `server/game/movement_helpers.py`
- **Movement service for MythosMUD. This module provides the MovementService class…** (1 connections) — `server/game/movement_service.py`
- **Validate rooms, membership, and exit for movement.** (1 connections) — `server/game/movement_service.py`
- **Validate that a movement operation is allowed. Args: player_obj: The player…** (1 connections) — `server/game/movement_service.py`
- **Test validate_exit logs when target room missing from persistence.** (1 connections) — `server/tests/unit/game/test_movement_service.py`

## Relationships

- [test_movement_service.py](test_movement_service.py.md) (12 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [MovementService](MovementService.md) (7 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [threading.py](threading.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 98 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*