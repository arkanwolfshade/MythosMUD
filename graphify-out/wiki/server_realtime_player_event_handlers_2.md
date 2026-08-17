# server realtime player event handlers

> 47 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (32 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_player_event_handlers_utils_grace_period.py** (10 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **Any** (7 connections)
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
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
- **BoundLogger** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (4 shared connections)
- [server realtime player event handlers](server_realtime_player_event_handlers.md) (2 shared connections)
- [server realtime player name utils](server_realtime_player_name_utils.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 73 (88%)
- INFERRED: 10 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*