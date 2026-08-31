# extract_player_name

> 27 nodes

## Key Concepts

- **extract_player_name()** (22 connections) — `server/realtime/player_presence_utils.py`
- **player_presence_utils.py** (18 connections) — `server/realtime/player_presence_utils.py`
- **test_player_presence_utils.py** (18 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **get_player_position()** (10 connections) — `server/realtime/player_presence_utils.py`
- **_is_valid_name()** (6 connections) — `server/realtime/player_presence_utils.py`
- **_is_uuid_string()** (5 connections) — `server/realtime/player_presence_utils.py`
- **_get_name_from_user()** (4 connections) — `server/realtime/player_presence_utils.py`
- **test_extract_player_name_user_access_error()** (3 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_get_player_position_stats_error()** (3 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **Player** (3 connections)
- **UUID** (3 connections)
- **test_extract_player_name_from_player_name()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_extract_player_name_from_user()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_extract_player_name_placeholder()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_extract_player_name_rejects_uuid_string()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_get_player_position_default()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_get_player_position_from_stats()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_is_uuid_string()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_is_valid_name()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **Any** (1 connections)
- **Utility functions for player presence tracking. This module provides helper…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Get player position from stats. Args: player: The player object player_id: The…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a value is a valid non-empty string name. Args: name: Value to check…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a string is a UUID format. Args: value: String to check Returns: True…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Attempt to get player name from related User object. Args: player: The player…** (1 connections) — `server/realtime/player_presence_utils.py`
- *... and 2 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (6 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (3 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (3 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_presence_utils.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*