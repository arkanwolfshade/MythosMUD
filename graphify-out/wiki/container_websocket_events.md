# container websocket events

> 32 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **test_player_name_utils.py** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_player_name_user_exception()** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.__init__()** (3 connections) — `server/realtime/player_name_utils.py`
- **.test_is_uuid_string_invalid_length()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_uuid_string_valid_format()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_valid_string()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_empty_string()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_initial_player_name_with_getattr()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_user_object_name_with_user()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_name_basic_whitespace_only()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_check_uuid_string_matches_lowercase()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_name_not_uuid_uuid_pattern()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_and_validate_player_name_invalid_uuid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_player_name_not_uuid_valid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Utility class for extracting and validating player names.      CRITICAL: NEVER u** (1 connections) — `server/realtime/player_name_utils.py`
- **Initialize the player name extractor.** (1 connections) — `server/realtime/player_name_utils.py`
- **Tests for player name extraction and validation utilities.  As documented in "Id** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _is_uuid_string with invalid length.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _is_uuid_string with valid format variations.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _is_valid_name with valid string.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _is_valid_name with empty string.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _is_valid_name with None.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _extract_initial_player_name with getattr fallback.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 7 more nodes in this community*

## Relationships

- [PlayerNameExtractor](PlayerNameExtractor.md) (34 shared connections)
- [connection statistics](connection_statistics.md) (17 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (10 shared connections)
- [login grace period](login_grace_period.md) (8 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [Test should echo to sender](Test_should_echo_to_sender.md) (5 shared connections)
- [Test send messages to players](Test_send_messages_to_players.md) (4 shared connections)
- [Test get applicable rules() returns](Test_get_applicable_rules%28%29_returns.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [connection manager api](connection_manager_api.md) (1 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [test_alias_hash_different_name](test_alias_hash_different_name.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 159 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*