# server tests unit realtime test

> 51 nodes

## Key Concepts

- **test_player_event_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **asyncio** (15 connections)
- **fixture** (8 connections)
- **player_event_handler()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_dp_updated_delegates_to_state_handler()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_dp_updated_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_entered_delegates_to_room_handler()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_entered_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_entered_no_send_occupants_update()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_left_delegates_to_room_handler()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_left_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_xp_awarded_delegates_to_state_handler()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_xp_awarded_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_chat_logger()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_message_builder()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_name_extractor()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_occupant_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_room_sync_service()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **mock_task_registry()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_delirium_respawned_delegates_to_respawn_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_died_delegates_to_state_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_dp_decay_delegates_to_state_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_respawned_delegates_to_respawn_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_send_occupants_snapshot_to_player_delegates_to_room_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- *... and 26 more nodes in this community*

## Relationships

- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (6 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (4 shared connections)
- [server events event types playerleftroom](server_events_event_types_playerleftroom.md) (3 shared connections)
- [chatlogger](chatlogger.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_event_handlers.py`

## Audit Trail

- EXTRACTED: 81 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*