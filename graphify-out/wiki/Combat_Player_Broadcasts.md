# Combat Player Broadcasts

> 130 nodes · cohesion 0.02

## Key Concepts

- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **send_game_event()** (28 connections) — `server/realtime/connection_manager_api.py`
- **admin_setstat_command.py** (27 connections) — `server/commands/admin_setstat_command.py`
- **envelope.py** (25 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (25 connections) — `server/tests/unit/realtime/test_envelope.py`
- **event_handlers.py** (21 connections) — `server/realtime/event_handlers.py`
- **container_websocket_events.py** (16 connections) — `server/services/container_websocket_events.py`
- **message_broadcaster.py** (15 connections) — `server/realtime/messaging/message_broadcaster.py`
- **connection_manager_api.py** (15 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **resolve_connection_manager()** (12 connections) — `server/realtime/connection_manager_utils.py`
- **broadcast_game_event()** (10 connections) — `server/realtime/connection_manager_api.py`
- **_apply_stat_change_and_build_result()** (8 connections) — `server/commands/admin_setstat_command.py`
- **spell_costs.py** (7 connections) — `server/game/magic/spell_costs.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **_send_combat_participant_updates()** (7 connections) — `server/realtime/event_handlers.py`
- **ConnectionManager** (7 connections) — `server/realtime/event_handlers.py`
- **_build_set_stat_error_response()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_calculate_stat_warnings()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_log_admin_set_stat()** (6 connections) — `server/commands/admin_setstat_command.py`
- **send_room_event()** (6 connections) — `server/realtime/connection_manager_api.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **UUIDEncoder** (6 connections) — `server/realtime/envelope.py`
- **_publish_npc_died_to_event_bus()** (6 connections) — `server/realtime/event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- *... and 105 more nodes in this community*

## Relationships

- [[NPC Admin API]] (25 shared connections)
- [[Room Occupant Events]] (22 shared connections)
- [[Admin Set Stat Command]] (12 shared connections)
- [[Player Respawn Events]] (10 shared connections)
- [[WebSocket Message Handlers]] (9 shared connections)
- [[Combat Services Messaging]] (8 shared connections)
- [[Message Broadcaster Core]] (8 shared connections)
- [[Look Command Helpers]] (8 shared connections)
- [[Admin Teleport Commands]] (7 shared connections)
- [[Container Open Events]] (7 shared connections)
- [[Alias Expansion Logic]] (6 shared connections)
- [[Game Tick Processing]] (6 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/game/magic/spell_costs.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`
- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`
- `server/realtime/npc_event_handlers.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 605 (98%)
- INFERRED: 15 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
