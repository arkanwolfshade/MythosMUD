# combat services messaging

> 111 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **rest_countdown_task.py** (12 connections) — `server/commands/rest_countdown_task.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **Any** (7 connections)
- **UUID** (6 connections)
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Any** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_start()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_death()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- *... and 86 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (24 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (20 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (5 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (5 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (5 shared connections)
- [combat services turn](combat_services_turn.md) (4 shared connections)
- [realtime messaging message](realtime_messaging_message.md) (4 shared connections)
- [room websocket updates](room_websocket_updates.md) (4 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (4 shared connections)
- [message handler factory](message_handler_factory.md) (4 shared connections)
- [player respawn event](player_respawn_event.md) (4 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/envelope.py`
- `server/realtime/integration/room_event_handler.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 446 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*