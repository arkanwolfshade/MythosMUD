# PlayerDPUpdated

> 150 nodes

## Key Concepts

- **PlayerDPUpdated** (41 connections) — `server/events/event_types.py`
- **PlayerStateEventHandler** (37 connections) — `server/realtime/player_event_handlers_state.py`
- **player_event_handlers_state.py** (36 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_state.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_player_event_handlers.py** (32 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **PlayerXPAwardEvent** (28 connections) — `server/events/event_types.py`
- **asyncio** (21 connections)
- **asyncio** (15 connections)
- **_dispatch_player_dp_updated_payload()** (13 connections) — `server/realtime/player_event_handlers_state.py`
- **_dispatch_player_dp_decay_payload()** (9 connections) — `server/realtime/player_event_handlers_state.py`
- **_maybe_attach_decay_posture_cross()** (9 connections) — `server/realtime/player_event_handlers_state.py`
- **_attach_dp_updated_posture_fields()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **fixture** (8 connections)
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **test_handle_player_xp_awarded_error_handling()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **player_state_event_handler()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_died_invalid_player_id()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_error_handling()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_includes_posture_message_on_posture_change()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_no_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_no_get_stats()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_not_found()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_success()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_no_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- *... and 125 more nodes in this community*

## Relationships

- [build_event](build_event.md) (13 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (11 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (7 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (5 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (5 shared connections)
- [CombatPersistenceHandler](CombatPersistenceHandler.md) (4 shared connections)
- [event_handler.py](event_handler.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (4 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (4 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 306 (84%)
- INFERRED: 58 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*