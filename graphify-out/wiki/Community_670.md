# Community 670

> 25 nodes

## Key Concepts

- **test_player_presence_utils.py** (18 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **extract_player_name()** (13 connections) — `server/realtime/player_presence_utils.py`
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
- **Get player position from stats. Args: player: The player object player_id: The…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a value is a valid non-empty string name. Args: name: Value to check…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a string is a UUID format. Args: value: String to check Returns: True…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Attempt to get player name from related User object. Args: player: The player…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Extract and validate player name, ensuring it's never a UUID. Args: player: The…** (1 connections) — `server/realtime/player_presence_utils.py`
- **Unit tests for player_presence_utils.** (1 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (3 shared connections)
- [Community 170](Community_170.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_presence_utils.py`

## Audit Trail

- EXTRACTED: 49 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*