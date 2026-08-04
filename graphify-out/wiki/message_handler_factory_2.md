# message handler factory

> 54 nodes

## Key Concepts

- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **mock_utils()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **player_state_event_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_player_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_no_get_stats()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **mock_logger()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_player_state_event_handler_init()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_success()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_no_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_no_death_location()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_invalid_player_id()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_error_handling()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_decay_success()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_decay_no_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- *... and 29 more nodes in this community*

## Relationships

- [room look commands](room_look_commands.md) (7 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (7 shared connections)
- [item models rationale](item_models_rationale.md) (6 shared connections)
- [player_event_handler_utils](player_event_handler_utils.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [schedule services service](schedule_services_service.md) (2 shared connections)
- [event bus events](event_bus_events.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 136 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*