# build_event

> 106 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **envelope.py** (32 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **log_room_broadcast_result()** (12 connections) — `server/services/combat_messaging/base.py`
- **combat_messaging/base.py** (12 connections) — `server/services/combat_messaging/base.py`
- **CombatBroadcastMixin** (11 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **PlayerBroadcastMixin** (10 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_broadcasts.py** (10 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **player_broadcasts.py** (10 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_combat_attack()** (7 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (7 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **HasConnectionManager** (6 connections) — `server/services/combat_messaging/base.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **.broadcast_combat_target_switch()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_death()** (5 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **._send_follow_request_to_target()** (4 connections) — `server/game/follow_service.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.send_dp_decay_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- *... and 81 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (11 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (6 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [.connection_manager](connection_manager.md) (4 shared connections)
- [admin_teleport_utils.py](admin_teleport_utils.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (4 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (4 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/realtime/envelope.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 303 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*