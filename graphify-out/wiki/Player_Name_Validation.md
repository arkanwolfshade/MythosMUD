# Player Name Validation

> 35 nodes · cohesion 0.09

## Key Concepts

- **Any** (14 connections) — `server/realtime/player_name_utils.py`
- **.extract_and_validate_player_name()** (8 connections) — `server/realtime/player_name_utils.py`
- **._validate_name_not_uuid()** (8 connections) — `server/realtime/player_name_utils.py`
- **UUID** (8 connections) — `server/realtime/player_name_utils.py`
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
- **Validate that player name is not a UUID string.          Args:             playe** (2 connections) — `server/realtime/player_name_utils.py`
- **Get name from user object (username or display_name).          Args:** (1 connections) — `server/realtime/player_name_utils.py`
- **Try to get name from related User object.          Args:             player: The** (1 connections) — `server/realtime/player_name_utils.py`
- **Try to get player name from fallback sources (username, user object).          A** (1 connections) — `server/realtime/player_name_utils.py`
- **Perform basic validation on player name (not None, is string, not empty).** (1 connections) — `server/realtime/player_name_utils.py`
- **Check if player name matches UUID pattern.          Args:             player_nam** (1 connections) — `server/realtime/player_name_utils.py`
- *... and 10 more nodes in this community*

## Relationships

- [[Player Respawn Events]] (18 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`

## Audit Trail

- EXTRACTED: 128 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
