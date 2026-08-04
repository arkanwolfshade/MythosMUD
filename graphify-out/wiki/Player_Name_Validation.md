# Player Name Validation

> 164 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Any** (14 connections)
- **player_name_utils.py** (13 connections) — `server/realtime/player_name_utils.py`
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
- **test_player_name_utils.py** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_player_name_user_exception()** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.__init__()** (3 connections) — `server/realtime/player_name_utils.py`
- **._check_uuid_pattern_match()** (3 connections) — `server/realtime/player_name_utils.py`
- *... and 139 more nodes in this community*

## Relationships

- [realtime monitoring performance](realtime_monitoring_performance.md) (5 shared connections)
- [logging processors structured](logging_processors_structured.md) (5 shared connections)
- [command utility models](command_utility_models.md) (5 shared connections)
- [player_event_handler_utils](player_event_handler_utils.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [event bus events](event_bus_events.md) (2 shared connections)
- [schedule services service](schedule_services_service.md) (2 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (2 shared connections)
- [player occupant processor](player_occupant_processor.md) (2 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 547 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*