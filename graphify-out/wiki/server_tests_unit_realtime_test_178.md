# server tests unit realtime test

> 12 nodes

## Key Concepts

- **asyncio** (22 connections)
- **test_get_current_lucidity_not_found()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_delirium_respawn_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_delirium_respawn_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_respawn_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_handle_player_delirium_respawned_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_send_respawn_event_with_retry_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **Test get_player_data_for_respawn() successfully retrieves player data.** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **Test send_respawn_event_with_retry() successfully sends event.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **Test get_current_lucidity() returns default when record not found.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **Test get_player_data_for_delirium_respawn() returns None when connection…** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **Test handle_player_delirium_respawned() handles errors.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (22 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*