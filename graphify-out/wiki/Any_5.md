# Any

> 36 nodes

## Key Concepts

- **Any** (14 connections)
- **.extract_and_validate_player_name()** (8 connections) — `server/realtime/player_name_utils.py`
- **._validate_name_not_uuid()** (8 connections) — `server/realtime/player_name_utils.py`
- **UUID** (8 connections)
- **._try_fallback_name_sources()** (7 connections) — `server/realtime/player_name_utils.py`
- **._is_uuid_string()** (6 connections) — `server/realtime/player_name_utils.py`
- **._is_valid_name_string()** (6 connections) — `server/realtime/player_name_utils.py`
- **.extract_player_name()** (5 connections) — `server/realtime/player_name_utils.py`
- **._is_valid_name()** (5 connections) — `server/realtime/player_name_utils.py`
- **._log_uuid_validation_failure()** (5 connections) — `server/realtime/player_name_utils.py`
- **._try_player_username()** (5 connections) — `server/realtime/player_name_utils.py`
- **._try_user_object_name()** (5 connections) — `server/realtime/player_name_utils.py`
- **._validate_name_basic()** (5 connections) — `server/realtime/player_name_utils.py`
- **.validate_player_name_not_uuid()** (5 connections) — `server/realtime/player_name_utils.py`
- **._check_uuid_string_matches()** (4 connections) — `server/realtime/player_name_utils.py`
- **._extract_initial_player_name()** (4 connections) — `server/realtime/player_name_utils.py`
- **._get_name_from_user_object()** (4 connections) — `server/realtime/player_name_utils.py`
- **.is_valid_name_for_occupant()** (4 connections) — `server/realtime/player_name_utils.py`
- **._check_uuid_pattern_match()** (3 connections) — `server/realtime/player_name_utils.py`
- **Get name from user object (username or display_name). Args: user: The user…** (1 connections) — `server/realtime/player_name_utils.py`
- **Try to get name from related User object. Args: player: The player object…** (1 connections) — `server/realtime/player_name_utils.py`
- **Try to get player name from fallback sources (username, user object). Args:…** (1 connections) — `server/realtime/player_name_utils.py`
- **Perform basic validation on player name (not None, is string, not empty). Args:…** (1 connections) — `server/realtime/player_name_utils.py`
- **Check if player name matches UUID pattern. Args: player_name: The player name…** (1 connections) — `server/realtime/player_name_utils.py`
- **Check if player name matches any UUID string representation. Args: player_name:…** (1 connections) — `server/realtime/player_name_utils.py`
- *... and 11 more nodes in this community*

## Relationships

- [PlayerNameExtractor](PlayerNameExtractor.md) (17 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`

## Audit Trail

- EXTRACTED: 128 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*