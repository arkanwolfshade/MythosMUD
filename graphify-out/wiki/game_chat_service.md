# game chat service

> 36 nodes

## Key Concepts

- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **Player** (8 connections)
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **SupportsPlayerPersistence** (6 connections) — `server/services/player_position_service.py`
- **._get_player_for_position_change()** (6 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (6 connections) — `server/services/player_position_service.py`
- **.save_player()** (5 connections) — `server/services/player_position_service.py`
- **SupportsConnectionManager** (5 connections) — `server/services/player_position_service.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (5 connections) — `server/services/player_position_service.py`
- **.get_player_by_name()** (4 connections) — `server/services/player_position_service.py`
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **._initial_response()** (4 connections) — `server/services/player_position_service.py`
- **.get_online_player_by_display_name()** (3 connections) — `server/services/player_position_service.py`
- **.ensure_default_aliases()** (3 connections) — `server/services/player_position_service.py`
- **._validate_position()** (3 connections) — `server/services/player_position_service.py`
- **Protocol** (2 connections)
- **TypedDict** (1 connections)
- **Result payload for a posture transition attempt.** (1 connections) — `server/services/player_position_service.py`
- **Persistence surface required for posture updates.** (1 connections) — `server/services/player_position_service.py`
- **Look up a player by name.** (1 connections) — `server/services/player_position_service.py`
- **Persist player posture and related state.** (1 connections) — `server/services/player_position_service.py`
- **Live presence surface used to mirror posture into online player records.** (1 connections) — `server/services/player_position_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [position player service](position_player_service.md) (11 shared connections)
- [commands admin mute](commands_admin_mute.md) (4 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [command input commands](command_input_commands.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`

## Audit Trail

- EXTRACTED: 111 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*