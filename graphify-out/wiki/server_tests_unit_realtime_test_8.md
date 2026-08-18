# server tests unit realtime test

> 9 nodes

## Key Concepts

- **asyncio** (4 connections)
- **test_get_player_info_invalid_player_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- **test_get_player_info_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- **test_get_player_info_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- **test_get_player_info_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- **Test get_player_info() returns None for invalid player_id.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- **Test get_player_info() returns None when player not found.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- **Test get_player_info() successfully retrieves player info.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- **Test get_player_info() returns None when connection manager not available.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils.py`

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (4 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_event_handlers_utils.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*