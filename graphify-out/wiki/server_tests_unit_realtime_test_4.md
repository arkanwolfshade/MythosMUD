# server tests unit realtime test

> 33 nodes

## Key Concepts

- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_check_uuid_string_matches_lowercase()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_check_uuid_string_matches_no_match()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_and_validate_player_name_fallback_user_object()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_and_validate_player_name_fallback_username()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_initial_player_name_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_initial_player_name_with_getattr()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_initial_player_name_with_name_attr()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_get_name_from_user_object_display_name()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_get_name_from_user_object_username()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_uuid_string_invalid_dash_count()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_uuid_string_valid_uuid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_uuid_string()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_player_username_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_user_object_name_no_user_attr()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_user_object_name_with_user()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_name_not_uuid_valid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_player_name_not_uuid_uuid_string()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _get_name_from_user_object with username.** (2 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _try_user_object_name with user attribute.** (2 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test extract_and_validate_player_name with username fallback.** (2 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _extract_initial_player_name with getattr fallback.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _extract_initial_player_name when name is None.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test suite for PlayerNameExtractor class.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _try_player_username when username is None.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 8 more nodes in this community*

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (31 shared connections)
- [server realtime player name utils](server_realtime_player_name_utils.md) (30 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 95 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*