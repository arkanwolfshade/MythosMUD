# player_event_handlers_state.py

> 56 nodes

## Key Concepts

- **player_event_handlers_state.py** (32 connections) — `server/realtime/player_event_handlers_state.py`
- **emit_posture_change()** (27 connections) — `server/realtime/posture_notify.py`
- **posture_notify.py** (22 connections) — `server/realtime/posture_notify.py`
- **_dispatch_player_dp_updated_payload()** (13 connections) — `server/realtime/player_event_handlers_state.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (12 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **_dispatch_player_dp_decay_payload()** (9 connections) — `server/realtime/player_event_handlers_state.py`
- **_maybe_attach_decay_posture_cross()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_attach_dp_updated_posture_fields()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **ConnectionManager** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_personal_posture_message()** (5 connections) — `server/realtime/posture_notify.py`
- **BoundLogger** (5 connections)
- **_StatsPlayer** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_decay_previous_position_before_lying()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_broadcast_room_posture_change()** (4 connections) — `server/realtime/posture_notify.py`
- **UUID** (4 connections)
- **asyncio** (4 connections)
- **_dp_posture_from_stats()** (3 connections) — `server/realtime/player_event_handlers_state.py`
- **.send_personal_message()** (3 connections) — `server/realtime/posture_notify.py`
- **test_emit_posture_change_attach_only_returns_message()** (3 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- *... and 31 more nodes in this community*

## Relationships

- [PlayerEnteredRoom](PlayerEnteredRoom.md) (13 shared connections)
- [build_event](build_event.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [PlayerStateEventHandler](PlayerStateEventHandler.md) (6 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (6 shared connections)
- [format_room_posture_message](format_room_posture_message.md) (6 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [follow_movement.py](follow_movement.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (2 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_state.py`
- `server/realtime/posture_notify.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 159 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*