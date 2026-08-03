# help content websocket

> 15 nodes

## Key Concepts

- **player_presence_utils.py** (16 connections) — `server/realtime/player_presence_utils.py`
- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **get_player_position()** (7 connections) — `server/realtime/player_presence_utils.py`
- **_get_name_from_user()** (5 connections) — `server/realtime/player_presence_utils.py`
- **_is_valid_name()** (4 connections) — `server/realtime/player_presence_utils.py`
- **_is_uuid_string()** (3 connections) — `server/realtime/player_presence_utils.py`
- **Player** (3 connections)
- **UUID** (3 connections)
- **Any** (1 connections)
- **Utility functions for player presence tracking.  This module provides helper fun** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a value is a valid non-empty string name.      Args:         name: Valu** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a string is a UUID format.      Args:         value: String to check** (1 connections) — `server/realtime/player_presence_utils.py`
- **Attempt to get player name from related User object.      Args:         player:** (1 connections) — `server/realtime/player_presence_utils.py`
- **Extract and validate player name, ensuring it's never a UUID.      Args:** (1 connections) — `server/realtime/player_presence_utils.py`
- **Get player position from stats.      Args:         player: The player object** (1 connections) — `server/realtime/player_presence_utils.py`

## Relationships

- [player presence tracker](player_presence_tracker.md) (6 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [grace period disconnect](grace_period_disconnect.md) (3 shared connections)
- [realtime player connection](realtime_player_connection.md) (3 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_utils.py`

## Audit Trail

- EXTRACTED: 62 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*