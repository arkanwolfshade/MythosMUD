# Services Combat Initialization

> 49 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **Any** (7 connections)
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **.get_player_info()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.process_dict_occupant()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.__init__()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.normalize_player_id()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **._extract_name_from_occupant()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.extract_occupant_names()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.build_occupants_snapshot_data()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.normalize_event_ids()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.add_valid_name_to_lists()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.count_occupants_by_type()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.is_player_disconnecting()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.is_player_in_grace_period()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **player_event_handler_utils()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_string_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **mock_name_extractor()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **mock_logger()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- *... and 24 more nodes in this community*

## Relationships

- [Character Creation E2E](Character_Creation_E2E.md) (8 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (5 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (3 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (3 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Container System Architecture](Container_System_Architecture.md) (2 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (2 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (2 shared connections)
- [Archive Lucidity System](Archive_Lucidity_System.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 155 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*