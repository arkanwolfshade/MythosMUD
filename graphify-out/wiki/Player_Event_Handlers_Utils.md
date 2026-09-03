# Player Event Handlers Utils

> 42 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (28 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_player_event_handlers_utils_grace_period.py** (10 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **Any** (7 connections)
- **UUID** (6 connections)
- **.get_player_info()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.process_dict_occupant()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.build_occupants_snapshot_data()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **._extract_name_from_occupant()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.extract_occupant_names()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.__init__()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.normalize_player_id()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.add_valid_name_to_lists()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.count_occupants_by_type()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.is_player_disconnecting()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.is_player_in_grace_period()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.normalize_event_ids()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **mock_logger()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **mock_name_extractor()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_string_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **fixture** (2 connections)
- **Test is_player_in_grace_period() returns False when player is not in grace…** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **Extract occupant names from occupant information. Args: occupants_info: List of…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- *... and 17 more nodes in this community*

## Relationships

- [Player Event Handlers Room](Player_Event_Handlers_Room.md) (3 shared connections)
- [Conftest](Conftest.md) (3 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (3 shared connections)
- [Test Player Event Handlers Utils](Test_Player_Event_Handlers_Utils.md) (2 shared connections)
- [Test Player Name Utils](Test_Player_Name_Utils.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 69 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*