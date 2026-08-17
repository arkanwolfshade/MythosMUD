# .change_position

> 26 nodes

## Key Concepts

- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **Player** (8 connections)
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **._get_player_for_position_change()** (4 connections) — `server/services/player_position_service.py`
- **._initial_response()** (4 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (4 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (4 connections) — `server/services/player_position_service.py`
- **.ensure_default_aliases()** (3 connections) — `server/services/player_position_service.py`
- **._validate_position()** (3 connections) — `server/services/player_position_service.py`
- **.get_player_by_name()** (3 connections) — `server/services/player_position_service.py`
- **TypedDict** (1 connections)
- **Validate and normalize position.** (1 connections) — `server/services/player_position_service.py`
- **Get player for position change. Returns: Tuple of (player, response_dict) if…** (1 connections) — `server/services/player_position_service.py`
- **Copy player identity fields into the position-change response.** (1 connections) — `server/services/player_position_service.py`
- **Load player stats, returning {} when loading fails.** (1 connections) — `server/services/player_position_service.py`
- **Get current position from player stats.** (1 connections) — `server/services/player_position_service.py`
- **Update player position in persistence.** (1 connections) — `server/services/player_position_service.py`
- **Build the default unsuccessful position-change payload.** (1 connections) — `server/services/player_position_service.py`
- **Mutate persistence and in-memory tracking to reflect the requested position.** (1 connections) — `server/services/player_position_service.py`
- **Mirror posture changes into the live connection manager.** (1 connections) — `server/services/player_position_service.py`
- **Result payload for a posture transition attempt.** (1 connections) — `server/services/player_position_service.py`
- **Look up a player by name.** (1 connections) — `server/services/player_position_service.py`
- *... and 1 more nodes in this community*

## Relationships

- [build_event](build_event.md) (12 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*