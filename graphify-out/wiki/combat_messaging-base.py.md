# combat_messaging/base.py

> 58 nodes

## Key Concepts

- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **log_room_broadcast_result()** (12 connections) — `server/services/combat_messaging/base.py`
- **combat_messaging/base.py** (12 connections) — `server/services/combat_messaging/base.py`
- **CombatBroadcastMixin** (11 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **PlayerBroadcastMixin** (10 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_broadcasts.py** (10 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **player_broadcasts.py** (10 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_combat_attack()** (7 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (7 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **HasConnectionManager** (6 connections) — `server/services/combat_messaging/base.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_combat_target_switch()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_death()** (5 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.send_dp_decay_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._send_mortally_wounded_personal_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Any** (4 connections)
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **._build_combat_attack_messages()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_mortally_wounded_messages()** (3 connections) — `server/services/combat_messaging/player_broadcasts.py`
- *... and 33 more nodes in this community*

## Relationships

- [build_event](build_event.md) (10 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (5 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [CombatMessagingService](CombatMessagingService.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 119 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*