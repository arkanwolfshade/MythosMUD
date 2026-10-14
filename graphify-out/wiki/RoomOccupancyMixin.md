# RoomOccupancyMixin

> 19 nodes

## Key Concepts

- **RoomOccupancyMixin** (12 connections) — `server/game/movement_room_occupancy.py`
- **UUID** (7 connections)
- **.add_player_to_room()** (6 connections) — `server/game/movement_room_occupancy.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_room_occupancy.py`
- **._validate_add_player_ids()** (5 connections) — `server/game/movement_room_occupancy.py`
- **._validate_remove_player_params()** (5 connections) — `server/game/movement_room_occupancy.py`
- **.get_player_room()** (4 connections) — `server/game/movement_room_occupancy.py`
- **._persist_added_player_room()** (4 connections) — `server/game/movement_room_occupancy.py`
- **.get_room_players()** (3 connections) — `server/game/movement_room_occupancy.py`
- **.validate_player_location()** (3 connections) — `server/game/movement_room_occupancy.py`
- **Validate parameters for remove_player_from_room operation.** (1 connections) — `server/game/movement_room_occupancy.py`
- **Remove a player from a room (for logout, teleportation, etc.). Args: player_id:…** (1 connections) — `server/game/movement_room_occupancy.py`
- **Get the room ID where a player is currently located. Args: player_id: The ID of…** (1 connections) — `server/game/movement_room_occupancy.py`
- **Get all players currently in a room. Args: room_id: The ID of the room to check…** (1 connections) — `server/game/movement_room_occupancy.py`
- **Validate that a player is in the specified room. Args: player_id: The ID of the…** (1 connections) — `server/game/movement_room_occupancy.py`
- **Room occupancy API; the host (MovementService) provides _persistence, _lock and…** (1 connections) — `server/game/movement_room_occupancy.py`
- **Validate player and room IDs for add_player_to_room.** (1 connections) — `server/game/movement_room_occupancy.py`
- **Update player current_room_id in persistence after room add.** (1 connections) — `server/game/movement_room_occupancy.py`
- **Add a player to a room (for initial placement, teleportation, etc.). Args:…** (1 connections) — `server/game/movement_room_occupancy.py`

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [MovementService](MovementService.md) (1 shared connections)

## Source Files

- `server/game/movement_room_occupancy.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*