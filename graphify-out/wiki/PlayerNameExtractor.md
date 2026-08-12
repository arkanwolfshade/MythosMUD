# PlayerNameExtractor

> 28 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **test_player_name_utils.py** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.__init__()** (3 connections) — `server/realtime/player_name_utils.py`
- **.test_check_uuid_pattern_match_valid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_and_validate_player_name_fallback_username()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_get_name_from_user_object_getattr_fallback()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_get_name_from_user_object_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_init()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_uuid_string_valid_uuid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_for_occupant_valid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_fallback_name_sources_invalid_current_username_fallback()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_name_basic_whitespace_only()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_name_not_uuid_uuid_pattern()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_player_name_not_uuid_uuid_string()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Utility class for extracting and validating player names. CRITICAL: NEVER uses…** (1 connections) — `server/realtime/player_name_utils.py`
- **Initialize the player name extractor.** (1 connections) — `server/realtime/player_name_utils.py`
- **Tests for player name extraction and validation utilities. As documented in…** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _get_name_from_user_object with getattr fallback.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test PlayerNameExtractor initialization.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _get_name_from_user_object when no name available.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _try_fallback_name_sources with username fallback.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _is_uuid_string with valid UUID.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _validate_name_basic with whitespace only.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _check_uuid_pattern_match with valid UUID pattern.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _validate_name_not_uuid with UUID pattern.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 3 more nodes in this community*

## Relationships

- [TestPlayerNameExtractor](TestPlayerNameExtractor.md) (30 shared connections)
- [Any](Any.md) (17 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (12 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (2 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (2 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (2 shared connections)
- [.test_check_uuid_string_matches_no_match](test_check_uuid_string_matches_no_match.md) (1 shared connections)
- [.test_extract_and_validate_player_name_invalid_uuid](test_extract_and_validate_player_name_invalid_uuid.md) (1 shared connections)
- [.test_extract_and_validate_player_name_none](test_extract_and_validate_player_name_none.md) (1 shared connections)
- [.test_extract_and_validate_player_name_success](test_extract_and_validate_player_name_success.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 151 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*