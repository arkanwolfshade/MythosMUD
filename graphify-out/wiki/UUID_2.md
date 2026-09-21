# UUID

> 22 nodes

## Key Concepts

- **UUID** (19 connections)
- **.move_player()** (8 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **._maybe_trigger_room_entry_hallucination()** (6 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **.get_player_room()** (4 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_added_player_room()** (4 connections) — `server/game/movement_service.py`
- **Exception** (1 connections)
- **Validate movement parameters. Returns False if validation fails (same room),…** (1 connections) — `server/game/movement_service.py`
- **Mark destination room as explored (non-blocking).** (1 connections) — `server/game/movement_service.py`
- **Handle movement errors with monitoring.** (1 connections) — `server/game/movement_service.py`
- **Log movement timing breakdown after a successful move.** (1 connections) — `server/game/movement_service.py`
- **Move a player from one room to another atomically. This operation ensures ACID…** (1 connections) — `server/game/movement_service.py`
- **Check the Uneasy tier's room-entry hallucination trigger after a successful…** (1 connections) — `server/game/movement_service.py`
- **Validate player and room IDs for add_player_to_room.** (1 connections) — `server/game/movement_service.py`
- **Update player current_room_id in persistence after room add.** (1 connections) — `server/game/movement_service.py`
- **Add a player to a room (for initial placement, teleportation, etc.). Args:…** (1 connections) — `server/game/movement_service.py`
- **Get the room ID where a player is currently located. Args: player_id: The ID of…** (1 connections) — `server/game/movement_service.py`

## Relationships

- [MovementService](MovementService.md) (14 shared connections)
- [._execute_move_locked](_execute_move_locked.md) (7 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (1 shared connections)
- [hallucinations.py](hallucinations.py.md) (1 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*