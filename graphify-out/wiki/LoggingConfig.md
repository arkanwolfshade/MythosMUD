# LoggingConfig

> 31 nodes · cohesion 0.08

## Key Concepts

- **player_position_service.py** (18 connections) — `server/services/player_position_service.py`
- **PositionPlayer** (13 connections) — `server/services/player_position_service.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **._get_player_for_position_change()** (4 connections) — `server/services/player_position_service.py`
- **._initial_response()** (4 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (4 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (4 connections) — `server/services/player_position_service.py`
- **._validate_position()** (4 connections) — `server/services/player_position_service.py`
- **.ensure_default_aliases()** (3 connections) — `server/services/player_position_service.py`
- **position_messages.py** (3 connections) — `server/services/position_messages.py`
- **.get_stats()** (1 connections) — `server/services/player_position_service.py`
- **.set_stats()** (1 connections) — `server/services/player_position_service.py`
- **TypedDict** (1 connections)
- **Player posture coordination service for MythosMUD. As noted in the Pnakotic…** (1 connections) — `server/services/player_position_service.py`
- **Validate and normalize position.** (1 connections) — `server/services/player_position_service.py`
- **Get player for position change. Returns: Tuple of (player, response_dict) if…** (1 connections) — `server/services/player_position_service.py`
- **Copy player identity fields into the position-change response.** (1 connections) — `server/services/player_position_service.py`
- **Load player stats, returning {} when loading fails.** (1 connections) — `server/services/player_position_service.py`
- **Get current position from player stats.** (1 connections) — `server/services/player_position_service.py`
- **Update player position in persistence.** (1 connections) — `server/services/player_position_service.py`
- **Build the default unsuccessful position-change payload.** (1 connections) — `server/services/player_position_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [RoomDataCache](RoomDataCache.md) (12 shared connections)
- [PlayerCombatState](PlayerCombatState.md) (6 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (1 shared connections)
- [.initialize](initialize.md) (1 shared connections)
- [_CombatServiceDeps](_CombatServiceDeps.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`
- `server/services/position_messages.py`

## Audit Trail

- EXTRACTED: 67 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*