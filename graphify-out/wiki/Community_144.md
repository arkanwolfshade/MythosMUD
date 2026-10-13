# Community 144

> 85 nodes

## Key Concepts

- **player_event_handlers_state.py** (32 connections) — `server/realtime/player_event_handlers_state.py`
- **emit_posture_change()** (31 connections) — `server/realtime/posture_notify.py`
- **posture_notify.py** (27 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (16 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **_dispatch_player_dp_updated_payload()** (12 connections) — `server/realtime/player_event_handlers_state.py`
- **attach_posture_self_message()** (12 connections) — `server/realtime/posture_notify.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **_dispatch_player_dp_decay_payload()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_maybe_attach_decay_posture_cross()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_attach_dp_updated_posture_fields()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_personal_posture_message()** (6 connections) — `server/realtime/posture_notify.py`
- **_StatsPlayer** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_decay_previous_position_before_lying()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_updated()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_broadcast_room_posture_change()** (4 connections) — `server/realtime/posture_notify.py`
- **BoundLogger** (4 connections)
- **PlayerDPUpdated** (4 connections)
- *... and 60 more nodes in this community*

## Relationships

- [Community 41](Community_41.md) (12 shared connections)
- [Community 136](Community_136.md) (8 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (8 shared connections)
- [Community 106](Community_106.md) (6 shared connections)
- [Community 281](Community_281.md) (5 shared connections)
- [Community 98](Community_98.md) (5 shared connections)
- [Community 76](Community_76.md) (4 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (4 shared connections)
- [Community 79](Community_79.md) (3 shared connections)
- [Community 395](Community_395.md) (3 shared connections)
- [Community 368](Community_368.md) (3 shared connections)
- [Community 902](Community_902.md) (3 shared connections)

## Source Files

- `server/realtime/player_event_handlers_state.py`
- `server/realtime/posture_notify.py`
- `server/services/position_messages.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 204 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*