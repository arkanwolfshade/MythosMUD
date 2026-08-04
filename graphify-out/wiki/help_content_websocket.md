# help content websocket

> 27 nodes

## Key Concepts

- **extract_player_name()** (22 connections) — `server/realtime/player_presence_utils.py`
- **test_player_presence_utils.py** (18 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **player_presence_utils.py** (17 connections) — `server/realtime/player_presence_utils.py`
- **get_player_position()** (11 connections) — `server/realtime/player_presence_utils.py`
- **_is_valid_name()** (6 connections) — `server/realtime/player_presence_utils.py`
- **_is_uuid_string()** (5 connections) — `server/realtime/player_presence_utils.py`
- **_get_name_from_user()** (5 connections) — `server/realtime/player_presence_utils.py`
- **Player** (3 connections)
- **UUID** (3 connections)
- **test_extract_player_name_user_access_error()** (3 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_get_player_position_stats_error()** (3 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_is_valid_name()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_is_uuid_string()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_extract_player_name_from_player_name()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_extract_player_name_from_user()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_extract_player_name_placeholder()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_extract_player_name_rejects_uuid_string()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_get_player_position_default()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_get_player_position_from_stats()** (2 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **Any** (1 connections)
- **Utility functions for player presence tracking.  This module provides helper fun** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a value is a valid non-empty string name.      Args:         name: Valu** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a string is a UUID format.      Args:         value: String to check** (1 connections) — `server/realtime/player_presence_utils.py`
- **Attempt to get player name from related User object.      Args:         player:** (1 connections) — `server/realtime/player_presence_utils.py`
- **Extract and validate player name, ensuring it's never a UUID.      Args:** (1 connections) — `server/realtime/player_presence_utils.py`
- *... and 2 more nodes in this community*

## Relationships

- [player presence tracker](player_presence_tracker.md) (8 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (7 shared connections)
- [Database Config](Database_Config.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_presence_utils.py`

## Audit Trail

- EXTRACTED: 117 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*