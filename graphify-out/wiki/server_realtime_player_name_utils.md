# server realtime player name utils

> 28 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **test_player_name_utils.py** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.__init__()** (3 connections) — `server/realtime/player_name_utils.py`
- **.test_extract_and_validate_player_name_invalid_uuid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_and_validate_player_name_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_get_name_from_user_object_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_init()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_for_occupant_invalid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_log_uuid_validation_failure_critical()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_log_uuid_validation_failure_warning_string()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_user_object_name_exception_handling()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_try_user_object_name_user_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_name_not_uuid_matches_player_id()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_validate_name_not_uuid_uuid_pattern()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Utility class for extracting and validating player names. CRITICAL: NEVER uses…** (1 connections) — `server/realtime/player_name_utils.py`
- **Initialize the player name extractor.** (1 connections) — `server/realtime/player_name_utils.py`
- **Tests for player name extraction and validation utilities. As documented in…** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test PlayerNameExtractor initialization.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _get_name_from_user_object when no name available.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _try_user_object_name when user is None.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _try_user_object_name with exception handling.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _log_uuid_validation_failure with critical error.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _log_uuid_validation_failure with UUID string warning.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _validate_name_not_uuid with UUID pattern.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Test _validate_name_not_uuid with name matching player ID.** (1 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 3 more nodes in this community*

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (61 shared connections)
- [server realtime player name utils](server_realtime_player_name_utils.md) (17 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (11 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (10 shared connections)
- [occupantsnap](occupantsnap.md) (2 shared connections)
- [server realtime npc occupant processor](server_realtime_npc_occupant_processor.md) (1 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 119 (91%)
- INFERRED: 12 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*