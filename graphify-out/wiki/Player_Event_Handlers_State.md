# Player Event Handlers State

> 39 nodes

## Key Concepts

- **player_event_handlers_state.py** (28 connections) — `server/realtime/player_event_handlers_state.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **_dispatch_player_dp_updated_payload()** (11 connections) — `server/realtime/player_event_handlers_state.py`
- **_dispatch_player_dp_decay_payload()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **_maybe_attach_decay_posture_cross()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **_attach_dp_updated_posture_fields()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **ConnectionManager** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **BoundLogger** (5 connections)
- **_StatsPlayer** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_decay_previous_position_before_lying()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_dp_posture_from_stats()** (3 connections) — `server/realtime/player_event_handlers_state.py`
- **test_normalize_posture_enum_value()** (3 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **UUID** (2 connections)
- **.get_stats()** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Player** (1 connections)
- **PlayerEventHandlerUtils** (1 connections)
- **Protocol** (1 connections)
- **Player state update event handlers. This module handles player state updates…** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Build and send the player_dp_updated WebSocket payload.** (1 connections) — `server/realtime/player_event_handlers_state.py`
- *... and 14 more nodes in this community*

## Relationships

- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (13 shared connections)
- [Posture Notify](Posture_Notify.md) (9 shared connections)
- [Combat Events](Combat_Events.md) (7 shared connections)
- [Admin Setstat Support](Admin_Setstat_Support.md) (3 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Test Envelope](Test_Envelope.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_state.py`
- `server/realtime/posture_notify.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 92 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*