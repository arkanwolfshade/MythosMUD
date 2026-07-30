# connection statistics

> 62 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **Any** (14 connections)
- **UUID** (8 connections)
- **._validate_name_not_uuid()** (8 connections) — `server/realtime/player_name_utils.py`
- **.extract_and_validate_player_name()** (8 connections) — `server/realtime/player_name_utils.py`
- **._try_fallback_name_sources()** (7 connections) — `server/realtime/player_name_utils.py`
- **._is_uuid_string()** (6 connections) — `server/realtime/player_name_utils.py`
- **._is_valid_name_string()** (6 connections) — `server/realtime/player_name_utils.py`
- **._is_valid_name()** (5 connections) — `server/realtime/player_name_utils.py`
- **._try_player_username()** (5 connections) — `server/realtime/player_name_utils.py`
- **._try_user_object_name()** (5 connections) — `server/realtime/player_name_utils.py`
- **._validate_name_basic()** (5 connections) — `server/realtime/player_name_utils.py`
- **._log_uuid_validation_failure()** (5 connections) — `server/realtime/player_name_utils.py`
- **.extract_player_name()** (5 connections) — `server/realtime/player_name_utils.py`
- **.validate_player_name_not_uuid()** (5 connections) — `server/realtime/player_name_utils.py`
- **._extract_initial_player_name()** (4 connections) — `server/realtime/player_name_utils.py`
- **._get_name_from_user_object()** (4 connections) — `server/realtime/player_name_utils.py`
- **._check_uuid_string_matches()** (4 connections) — `server/realtime/player_name_utils.py`
- **.is_valid_name_for_occupant()** (4 connections) — `server/realtime/player_name_utils.py`
- **.__init__()** (3 connections) — `server/realtime/player_name_utils.py`
- **._check_uuid_pattern_match()** (3 connections) — `server/realtime/player_name_utils.py`
- **.test_init()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_valid_name_none()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_get_name_from_user_object_username()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_get_name_from_user_object_display_name()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 37 more nodes in this community*

## Relationships

- [PlayerNameExtractor](PlayerNameExtractor.md) (61 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (6 shared connections)
- [world](world.md) (6 shared connections)
- [.get instance()](get_instance%28%29.md) (4 shared connections)
- [login grace period](login_grace_period.md) (4 shared connections)
- [test combat persistence handler](test_combat_persistence_handler.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [NPCEventHandler](NPCEventHandler.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 274 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*