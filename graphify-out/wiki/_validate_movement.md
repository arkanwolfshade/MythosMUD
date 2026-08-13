# ._validate_movement

> 6 nodes

## Key Concepts

- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **Load fresh player from persistence for posture check when available.** (1 connections) — `server/game/movement_service.py`
- **Validate rooms, membership, and exit for movement.** (1 connections) — `server/game/movement_service.py`
- **Validate that a movement operation is allowed. Args: player_obj: The player…** (1 connections) — `server/game/movement_service.py`

## Relationships

- [MovementService](MovementService.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [._execute_move_locked](_execute_move_locked.md) (2 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*