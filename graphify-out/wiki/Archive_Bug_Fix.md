# Archive Bug Fix

> 167 nodes

## Key Concepts

- **ConnectionManager** (166 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **Any** (40 connections)
- **.check_connection_health()** (6 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **.canonical_room_id()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (5 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (5 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **._broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (5 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (5 connections) — `server/realtime/connection_manager.py`
- **RespawnPlayerStatsPayload** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 142 more nodes in this community*

## Relationships

- [Playwright E2E Specs](Playwright_E2E_Specs.md) (40 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (16 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (13 shared connections)
- [Follow Service Tests](Follow_Service_Tests.md) (12 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (6 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (5 shared connections)
- [Cursor Skills Overdrive](Cursor_Skills_Overdrive.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Command Alias Model](Command_Alias_Model.md) (4 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (4 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (4 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 609 (95%)
- INFERRED: 31 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*