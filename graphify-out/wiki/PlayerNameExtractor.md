# PlayerNameExtractor

> 162 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
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
- **.__init__()** (3 connections) — `server/realtime/player_name_utils.py`
- **.test_check_uuid_pattern_match_invalid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 137 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (8 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (3 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 272 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*