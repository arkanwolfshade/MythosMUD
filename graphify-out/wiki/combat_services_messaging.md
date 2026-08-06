# combat services messaging

> 110 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **HasConnectionManager** (7 connections) — `server/services/combat_messaging/base.py`
- **Any** (7 connections)
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Any** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_start()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_death()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_end()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_error()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_target_switch()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- *... and 85 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (11 shared connections)
- [profession models rationale](profession_models_rationale.md) (8 shared connections)
- [command commands aliases](command_commands_aliases.md) (8 shared connections)
- [commands communication support](commands_communication_support.md) (7 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (6 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (5 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (5 shared connections)
- [npc service services](npc_service_services.md) (4 shared connections)
- [instance game manager](instance_game_manager.md) (4 shared connections)
- [services chat logger](services_chat_logger.md) (4 shared connections)
- [command models moderation](command_models_moderation.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 456 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*