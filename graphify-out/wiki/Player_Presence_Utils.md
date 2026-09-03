# Player Presence Utils

> 27 nodes

## Key Concepts

- **player_presence_utils.py** (18 connections) — `server/realtime/player_presence_utils.py`
- **test_player_presence_utils.py** (18 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **extract_player_name()** (17 connections) — `server/realtime/player_presence_utils.py`
- **get_player_position()** (8 connections) — `server/realtime/player_presence_utils.py`
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

- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (5 shared connections)
- [Player Connection Setup](Player_Connection_Setup.md) (3 shared connections)
- [Test Player Disconnect Handlers](Test_Player_Disconnect_Handlers.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)
- [Test Combat Persistence Handler Persistence](Test_Combat_Persistence_Handler_Persistence.md) (1 shared connections)
- [Test Rest And Grace Period](Test_Rest_And_Grace_Period.md) (1 shared connections)
- [Test Player Presence Tracker](Test_Player_Presence_Tracker.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_presence_utils.py`

## Audit Trail

- EXTRACTED: 64 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*