# PlayerStateEventHandler

> 66 nodes

## Key Concepts

- **PlayerStateEventHandler** (36 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_state.py** (36 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
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
- **.handle_player_dp_updated()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **mock_utils()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_invalid_player_id()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_no_death_location()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_success()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- *... and 41 more nodes in this community*

## Relationships

- [PlayerEnteredRoom](PlayerEnteredRoom.md) (19 shared connections)
- [player_event_handlers_state.py](player_event_handlers_state.py.md) (6 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (5 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 110 (74%)
- INFERRED: 38 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*