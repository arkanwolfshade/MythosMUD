# PlayerDPUpdated

> 104 nodes

## Key Concepts

- **PlayerDPUpdated** (38 connections) — `server/events/event_types.py`
- **PlayerStateEventHandler** (36 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_state.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **player_event_handlers_state.py** (31 connections) — `server/realtime/player_event_handlers_state.py`
- **PlayerXPAwardEvent** (25 connections) — `server/events/event_types.py`
- **asyncio** (21 connections)
- **_dispatch_player_dp_updated_payload()** (13 connections) — `server/realtime/player_event_handlers_state.py`
- **_dispatch_player_dp_decay_payload()** (9 connections) — `server/realtime/player_event_handlers_state.py`
- **_maybe_attach_decay_posture_cross()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_attach_dp_updated_posture_fields()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **ConnectionManager** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_hp_sync.py`
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
- *... and 79 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (20 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [emit_posture_change](emit_posture_change.md) (7 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (5 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (5 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [PlayerEventHandler](PlayerEventHandler.md) (4 shared connections)
- [Spell](Spell.md) (3 shared connections)
- [CombatPersistenceHandler](CombatPersistenceHandler.md) (3 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_hp_sync.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 230 (83%)
- INFERRED: 46 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*