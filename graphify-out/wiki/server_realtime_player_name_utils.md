# server realtime player name utils

> 155 nodes

## Key Concepts

- **PlayerNameExtractor** (98 connections) — `server/realtime/player_name_utils.py`
- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
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
- **.test_extract_player_name_user_exception()** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **test_player_name_utils.py** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **._check_uuid_pattern_match()** (3 connections) — `server/realtime/player_name_utils.py`
- **.test_check_uuid_pattern_match_invalid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_check_uuid_pattern_match_valid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 130 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (5 shared connections)
- [server realtime npc occupant processor](server_realtime_npc_occupant_processor.md) (3 shared connections)
- [server realtime event handler py](server_realtime_event_handler_py.md) (2 shared connections)
- [server realtime player event handlers](server_realtime_player_event_handlers.md) (2 shared connections)
- [server realtime player occupant processor](server_realtime_player_occupant_processor.md) (2 shared connections)
- [server realtime player name utils](server_realtime_player_name_utils.md) (1 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 267 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*