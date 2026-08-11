# LRU Cache Manager

> 166 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
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
- *... and 141 more nodes in this community*

## Relationships

- [Character Creation E2E](Character_Creation_E2E.md) (14 shared connections)
- [API Type Guards](API_Type_Guards.md) (12 shared connections)
- [Services Combat Initialization](Services_Combat_Initialization.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (1 shared connections)
- [Container System Architecture](Container_System_Architecture.md) (1 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (1 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (1 shared connections)
- [Archive Lucidity System](Archive_Lucidity_System.md) (1 shared connections)
- [Warning Fixes Session](Warning_Fixes_Session.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 564 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*