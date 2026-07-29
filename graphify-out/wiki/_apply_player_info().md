# . apply player info()

> 27 nodes

## Key Concepts

- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **Player** (8 connections)
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **._get_player_for_position_change()** (5 connections) — `server/services/player_position_service.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (5 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (5 connections) — `server/services/player_position_service.py`
- **.save_player()** (4 connections) — `server/services/player_position_service.py`
- **._initial_response()** (4 connections) — `server/services/player_position_service.py`
- **.get_player_by_name()** (3 connections) — `server/services/player_position_service.py`
- **.ensure_default_aliases()** (3 connections) — `server/services/player_position_service.py`
- **._validate_position()** (3 connections) — `server/services/player_position_service.py`
- **.get_online_player_by_display_name()** (2 connections) — `server/services/player_position_service.py`
- **TypedDict** (1 connections)
- **Result payload for a posture transition attempt.** (1 connections) — `server/services/player_position_service.py`
- **Ensure the expected aliases exist for position commands.** (1 connections) — `server/services/player_position_service.py`
- **Validate and normalize position.** (1 connections) — `server/services/player_position_service.py`
- **Get player for position change.          Returns:             Tuple of (player,** (1 connections) — `server/services/player_position_service.py`
- **Copy player identity fields into the position-change response.** (1 connections) — `server/services/player_position_service.py`
- **Load player stats, returning {} when loading fails.** (1 connections) — `server/services/player_position_service.py`
- **Get current position from player stats.** (1 connections) — `server/services/player_position_service.py`
- **Update player position in persistence.** (1 connections) — `server/services/player_position_service.py`
- **Build the default unsuccessful position-change payload.** (1 connections) — `server/services/player_position_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [PlayerPositionService](PlayerPositionService.md) (10 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`

## Audit Trail

- EXTRACTED: 86 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*