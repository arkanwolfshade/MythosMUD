# PlayerStateEventHandler

> 68 nodes

## Key Concepts

- **PlayerStateEventHandler** (36 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_state.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerXPAwardEvent** (25 connections) — `server/events/event_types.py`
- **asyncio** (21 connections)
- **player_state_event_handler()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_error_handling()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_includes_posture_message_on_posture_change()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_no_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_no_get_stats()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_not_found()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_success()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_error_handling()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_no_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_player_no_current_room_id()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_player_not_found()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_success()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **mock_utils()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_invalid_player_id()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_no_death_location()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_success()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- *... and 43 more nodes in this community*

## Relationships

- [PlayerDPUpdated](PlayerDPUpdated.md) (14 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (11 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (2 shared connections)
- [combat_service.py](combat_service.py.md) (2 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)
- [._bind_event_type](_bind_event_type.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 128 (78%)
- INFERRED: 36 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*