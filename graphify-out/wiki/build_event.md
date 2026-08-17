# build_event

> 87 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **rest_countdown_task.py** (13 connections) — `server/commands/rest_countdown_task.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **Any** (7 connections)
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **UUID** (6 connections)
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Any** (5 connections)
- **Any** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **.broadcast_combat_death()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_end()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_error()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_start()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_target_switch()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_death()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- *... and 62 more nodes in this community*

## Relationships

- [test_envelope.py](test_envelope.py.md) (20 shared connections)
- [CombatMessagingService](CombatMessagingService.md) (20 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (10 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [test_admin_commands_helpers.py](test_admin_commands_helpers.py.md) (4 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (4 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (4 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (4 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (3 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (3 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/envelope.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 258 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*