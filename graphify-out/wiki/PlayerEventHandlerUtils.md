# PlayerEventHandlerUtils

> 43 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (41 connections) — `server/realtime/player_event_handlers_utils.py`
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
- **Extract occupant names from occupant information. Args: occupants_info: List of…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Add a valid name to the appropriate lists. Args: name: The name to validate and…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- *... and 18 more nodes in this community*

## Relationships

- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (5 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (5 shared connections)
- [player_event_handlers_respawn.py](player_event_handlers_respawn.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (2 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (2 shared connections)
- [test_player_event_handlers_state.py](test_player_event_handlers_state.py.md) (2 shared connections)
- [test_player_event_handlers_utils.py](test_player_event_handlers_utils.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 73 (83%)
- INFERRED: 15 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*