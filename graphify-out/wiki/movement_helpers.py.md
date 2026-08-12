# movement_helpers.py

> 19 nodes

## Key Concepts

- **movement_helpers.py** (16 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (8 connections) — `server/game/movement_helpers.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **check_combat_state()** (7 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (7 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (6 connections) — `server/game/movement_helpers.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **Room** (2 connections)
- **Movement validation helpers for MovementService. Cohesive validation and room-…** (1 connections) — `server/game/movement_helpers.py`
- **Validate player is in the from_room, auto-adding if database matches.** (1 connections) — `server/game/movement_helpers.py`
- **Validate that there's a valid exit from the room to the target room.** (1 connections) — `server/game/movement_helpers.py`
- **Extract and validate player ID from player object.** (1 connections) — `server/game/movement_helpers.py`
- **Check if player is in combat (blocks movement).** (1 connections) — `server/game/movement_helpers.py`
- **Check if player posture allows movement (only standing allowed).** (1 connections) — `server/game/movement_helpers.py`
- **Validate rooms, membership, and exit for movement.** (1 connections) — `server/game/movement_service.py`
- **Validate that a movement operation is allowed. Args: player_obj: The player…** (1 connections) — `server/game/movement_service.py`

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [MovementService](MovementService.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 84 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*