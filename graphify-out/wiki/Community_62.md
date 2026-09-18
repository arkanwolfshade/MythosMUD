# Community 62

> 114 nodes

## Key Concepts

- **build_event()** (90 connections) — `server/realtime/envelope.py`
- **envelope.py** (32 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **.connection_manager()** (13 connections) — `server/services/combat_messaging/base.py`
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
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_combat_target_switch()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_death()** (5 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- *... and 89 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (13 shared connections)
- [Community 184](Community_184.md) (9 shared connections)
- [Community 281](Community_281.md) (5 shared connections)
- [Community 306](Community_306.md) (5 shared connections)
- [Community 70](Community_70.md) (5 shared connections)
- [Community 82](Community_82.md) (4 shared connections)
- [Community 123](Community_123.md) (4 shared connections)
- [Community 890](Community_890.md) (4 shared connections)
- [Realtime Message Handlers](Realtime_Message_Handlers.md) (4 shared connections)
- [Community 463](Community_463.md) (4 shared connections)
- [Community 200](Community_200.md) (4 shared connections)
- [Community 254](Community_254.md) (3 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/websocket_handler_commands.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 287 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*