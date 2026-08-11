# NATS Message Broker

> 111 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_disconnect_handlers.py** (27 connections) — `server/realtime/player_disconnect_handlers.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **UUID** (7 connections)
- **UUID** (4 connections)
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_start_grace_period_reconnection_cancels()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Any** (3 connections)
- **_session_ids_past_age_off()** (3 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_start_grace_period_creates_task()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 86 more nodes in this community*

## Relationships

- [Rescue Service Tests](Rescue_Service_Tests.md) (12 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (9 shared connections)
- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (7 shared connections)
- [API Type Guards](API_Type_Guards.md) (6 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (3 shared connections)
- [Look Player Command](Look_Player_Command.md) (3 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (3 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (2 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 417 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*