# server realtime player presence utils

> 25 nodes

## Key Concepts

- **extract_player_name()** (22 connections) — `server/realtime/player_presence_utils.py`
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
- **Get player position from stats. Args: player: The player object player_id: The…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a value is a valid non-empty string name. Args: name: Value to check…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a string is a UUID format. Args: value: String to check Returns: True…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Attempt to get player name from related User object. Args: player: The player…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Extract and validate player name, ensuring it's never a UUID. Args: player: The…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Unit tests for player_presence_utils.** (1 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server realtime player disconnect handlers](server_realtime_player_disconnect_handlers.md) (6 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (2 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (1 shared connections)
- [server realtime player connection setup](server_realtime_player_connection_setup.md) (1 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_presence_utils.py`

## Audit Trail

- EXTRACTED: 59 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*