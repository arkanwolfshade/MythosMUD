# commands communication support

> 50 nodes

## Key Concepts

- **test_player_event_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **player_event_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_entered_delegates_to_room_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_entered_no_send_occupants_update()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_left_delegates_to_room_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_xp_awarded_delegates_to_state_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_dp_updated_delegates_to_state_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_entered_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_left_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_xp_awarded_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_dp_updated_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_room_sync_service()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_chat_logger()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_task_registry()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_message_builder()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_name_extractor()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_occupant_manager()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_player_event_handler_init()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_send_occupants_snapshot_to_player_delegates_to_room_handler()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_send_occupants_snapshot_to_player_string_id()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_died_delegates_to_state_handler()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_dp_decay_delegates_to_state_handler()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_respawned_delegates_to_respawn_handler()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_delirium_respawned_delegates_to_respawn_handler()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- *... and 25 more nodes in this community*

## Relationships

- [inventory mutation guard](inventory_mutation_guard.md) (7 shared connections)
- [Error Conversion](Error_Conversion.md) (7 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_event_handlers.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*