# PlayerNameExtractor

> 40 nodes

## Key Concepts

- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_init()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_uuid_string_invalid_dash_count()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_uuid_string()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_string_valid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_player_username_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_get_name_from_user_object_username()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_get_name_from_user_object_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_user_object_name_user_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_user_object_name_exception_handling()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_fallback_name_sources_invalid_current_username_fallback()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_name_basic_valid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_check_uuid_pattern_match_invalid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_log_uuid_validation_failure_warning_pattern()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_name_not_uuid_matches_player_id()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_and_validate_player_name_success()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_and_validate_player_name_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_player_name_from_player()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_player_name_not_uuid_uuid_string()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_for_occupant_valid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test suite for PlayerNameExtractor class.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test PlayerNameExtractor initialization.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _is_uuid_string with invalid dash count.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _is_valid_name with UUID string.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _is_valid_name_string with valid string.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 15 more nodes in this community*

## Relationships

- [container websocket events](container_websocket_events.md) (34 shared connections)
- [Test should echo to sender](Test_should_echo_to_sender.md) (5 shared connections)
- [Test send messages to players](Test_send_messages_to_players.md) (4 shared connections)
- [Test get applicable rules() returns](Test_get_applicable_rules%28%29_returns.md) (3 shared connections)
- [test_alias_hash_different_name](test_alias_hash_different_name.md) (1 shared connections)
- [test_alias_hash_same_name_and_command](test_alias_hash_same_name_and_command.md) (1 shared connections)
- [Test evaluate condition() returns False](Test_evaluate_condition%28%29_returns_False.md) (1 shared connections)
- [test_select_exit_empty_dict](test_select_exit_empty_dict.md) (1 shared connections)
- [idle_movement_handler](idle_movement_handler.md) (1 shared connections)
- [test_should_idle_move_true_when_not_in_combat_and_probability_succeeds](test_should_idle_move_true_when_not_in_combat_and_probability_succeeds.md) (1 shared connections)
- [Chat WebSocket event carries speaker](Chat_WebSocket_event_carries_speaker.md) (1 shared connections)
- [Test convert ids to uuids](Test_convert_ids_to_uuids.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 138 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*