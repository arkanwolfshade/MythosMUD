# ._execute_move_locked

> 18 nodes

## Key Concepts

- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._record_move_validation_failure()** (4 connections) — `server/game/movement_service.py`
- **Room** (2 connections)
- **Resolve player by ID or name and return player object and resolved ID.** (1 connections) — `server/game/movement_service.py`
- **Get and validate rooms for movement.** (1 connections) — `server/game/movement_service.py`
- **Execute the atomic room transfer.** (1 connections) — `server/game/movement_service.py`
- **Update player location in database.** (1 connections) — `server/game/movement_service.py`
- **If player exited tutorial instance (moved to fixed exit room), clear and…** (1 connections) — `server/game/movement_service.py`
- **Record timing and monitor stats when movement validation fails.** (1 connections) — `server/game/movement_service.py`
- **Run movement logic while holding the service lock.** (1 connections) — `server/game/movement_service.py`
- **Initialize the movement service. Args: event_bus: Optional EventBus instance…** (1 connections) — `server/game/movement_service.py`

## Relationships

- [MovementService](MovementService.md) (10 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*