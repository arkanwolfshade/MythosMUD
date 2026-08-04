# position player service

> 50 nodes

## Key Concepts

- **PlayerPositionService** (47 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_database_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_player_position_service_init()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_player_position_service_init_none_values()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_no_storage()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_creates_missing()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_updates_incorrect()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_keeps_correct()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_handles_errors()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_invalid_position()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_persistence()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_already_in_position()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_success()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_get_stats()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_get_stats_error()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_updates_connection_manager()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_updates_existing_connection_info()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_all_positions()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_no_manager()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_no_online_players()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_updates_by_display_name()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_handles_errors()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- *... and 25 more nodes in this community*

## Relationships

- [command admin setlucidity](command_admin_setlucidity.md) (11 shared connections)
- [commands whisper command](commands_whisper_command.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [party service game](party_service_game.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [rest grace period](rest_grace_period.md) (2 shared connections)

## Source Files

- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 168 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*