# ._execute_move_locked

> 13 nodes

## Key Concepts

- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._record_move_validation_failure()** (4 connections) — `server/game/movement_service.py`
- **Resolve player by ID or name and return player object and resolved ID.** (1 connections) — `server/game/movement_service.py`
- **Update player location in database.** (1 connections) — `server/game/movement_service.py`
- **If player exited tutorial instance (moved to fixed exit room), clear and…** (1 connections) — `server/game/movement_service.py`
- **Record timing and monitor stats when movement validation fails.** (1 connections) — `server/game/movement_service.py`
- **Run movement logic while holding the service lock.** (1 connections) — `server/game/movement_service.py`
- **Initialize the movement service. Args: event_bus: Optional EventBus instance…** (1 connections) — `server/game/movement_service.py`

## Relationships

- [MovementService](MovementService.md) (11 shared connections)
- [._validate_movement](_validate_movement.md) (2 shared connections)
- [._get_rooms_for_movement](_get_rooms_for_movement.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*