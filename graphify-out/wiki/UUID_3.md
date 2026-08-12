# UUID

> 20 nodes

## Key Concepts

- **UUID** (18 connections)
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **.move_player()** (7 connections) — `server/game/movement_service.py`
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (5 connections) — `server/game/movement_service.py`
- **.get_player_room()** (4 connections) — `server/game/movement_service.py`
- **._persist_added_player_room()** (4 connections) — `server/game/movement_service.py`
- **Exception** (1 connections)
- **Validate movement parameters. Returns False if validation fails (same room),…** (1 connections) — `server/game/movement_service.py`
- **Handle movement errors with monitoring.** (1 connections) — `server/game/movement_service.py`
- **Move a player from one room to another atomically. This operation ensures ACID…** (1 connections) — `server/game/movement_service.py`
- **Validate player and room IDs for add_player_to_room.** (1 connections) — `server/game/movement_service.py`
- **Update player current_room_id in persistence after room add.** (1 connections) — `server/game/movement_service.py`
- **Add a player to a room (for initial placement, teleportation, etc.). Args:…** (1 connections) — `server/game/movement_service.py`
- **Validate parameters for remove_player_from_room operation.** (1 connections) — `server/game/movement_service.py`
- **Remove a player from a room (for logout, teleportation, etc.). Args: player_id:…** (1 connections) — `server/game/movement_service.py`
- **Get the room ID where a player is currently located. Args: player_id: The ID of…** (1 connections) — `server/game/movement_service.py`

## Relationships

- [MovementService](MovementService.md) (17 shared connections)
- [log_and_raise](log_and_raise.md) (7 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [movement_helpers.py](movement_helpers.py.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 76 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*