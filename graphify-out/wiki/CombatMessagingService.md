# CombatMessagingService

> 68 nodes

## Key Concepts

- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging/base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **HasConnectionManager** (7 connections) — `server/services/combat_messaging/base.py`
- **Any** (7 connections)
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessages** (5 connections)
- **Any** (5 connections)
- **.broadcast_combat_death()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_end()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_error()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_start()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_target_switch()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_death()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.broadcast_player_respawn()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.send_dp_decay_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- *... and 43 more nodes in this community*

## Relationships

- [build_event](build_event.md) (15 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [TestCombatMessagingService](TestCombatMessagingService.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 131 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*