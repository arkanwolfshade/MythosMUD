# PlayerDPUpdated

> 143 nodes

## Key Concepts

- **PlayerDPUpdated** (38 connections) — `server/events/event_types.py`
- **PlayerStateEventHandler** (36 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_state.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **player_event_handlers_state.py** (31 connections) — `server/realtime/player_event_handlers_state.py`
- **emit_posture_change()** (27 connections) — `server/realtime/posture_notify.py`
- **PlayerXPAwardEvent** (25 connections) — `server/events/event_types.py`
- **posture_notify.py** (22 connections) — `server/realtime/posture_notify.py`
- **asyncio** (21 connections)
- **_dispatch_player_dp_updated_payload()** (13 connections) — `server/realtime/player_event_handlers_state.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (11 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **_dispatch_player_dp_decay_payload()** (9 connections) — `server/realtime/player_event_handlers_state.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **_maybe_attach_decay_posture_cross()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_attach_dp_updated_posture_fields()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **ConnectionManager** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_personal_posture_message()** (5 connections) — `server/realtime/posture_notify.py`
- **player_state_event_handler()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_error_handling()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_includes_posture_message_on_posture_change()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- *... and 118 more nodes in this community*

## Relationships

- [event_handler.py](event_handler.py.md) (15 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (10 shared connections)
- [build_event](build_event.md) (10 shared connections)
- [event_types.py](event_types.py.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (6 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [magic_healing_events.py](magic_healing_events.py.md) (3 shared connections)
- [CombatPersistenceHandler](CombatPersistenceHandler.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/posture_notify.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 322 (88%)
- INFERRED: 46 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*