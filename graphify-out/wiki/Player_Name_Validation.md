# Player Name Validation

> 158 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
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
- **.test_extract_player_name_user_exception()** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **._check_uuid_pattern_match()** (3 connections) — `server/realtime/player_name_utils.py`
- **.test_init()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_uuid_string_valid_uuid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_is_uuid_string_invalid_length()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 133 more nodes in this community*

## Relationships

- [look helpers commands](look_helpers_commands.md) (14 shared connections)
- [NATS Messaging](NATS_Messaging.md) (11 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 524 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*