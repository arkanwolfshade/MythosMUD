# Server Services (80)

> 18 nodes

## Key Concepts

- **.change_position()** (10 connections) — `server/services/player_position_service.py`
- **Any** (7 connections)
- **._get_player_for_position_change()** (5 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (5 connections) — `server/services/player_position_service.py`
- **._extract_player_info()** (4 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (4 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (4 connections) — `server/services/player_position_service.py`
- **.__init__()** (3 connections) — `server/services/player_position_service.py`
- **.ensure_default_aliases()** (3 connections) — `server/services/player_position_service.py`
- **._validate_position()** (3 connections) — `server/services/player_position_service.py`
- **Ensure the expected aliases exist for position commands.** (1 connections) — `server/services/player_position_service.py`
- **Validate and normalize position.** (1 connections) — `server/services/player_position_service.py`
- **Get player for position change.          Returns:             Tuple of (player,** (1 connections) — `server/services/player_position_service.py`
- **Extract player information for response.** (1 connections) — `server/services/player_position_service.py`
- **Get current position from player stats.** (1 connections) — `server/services/player_position_service.py`
- **Update player position in persistence.** (1 connections) — `server/services/player_position_service.py`
- **Mutate persistence and in-memory tracking to reflect the requested position.** (1 connections) — `server/services/player_position_service.py`
- **Mirror posture changes into the live connection manager.** (1 connections) — `server/services/player_position_service.py`

## Relationships

- [Server Services (98)](Server_Services_%2898%29.md) (9 shared connections)
- [Server Persistence](Server_Persistence.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`

## Audit Trail

- EXTRACTED: 54 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*