# CombatMessagingService

> 74 nodes

## Key Concepts

- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **.connection_manager()** (13 connections) — `server/services/combat_messaging/base.py`
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
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_combat_target_switch()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_death()** (5 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **CombatMessages** (5 connections)
- **test_combat_messaging_service.py** (5 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.send_dp_decay_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._send_mortally_wounded_personal_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- *... and 49 more nodes in this community*

## Relationships

- [build_event](build_event.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [TestCombatMessagingService](TestCombatMessagingService.md) (4 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (2 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (2 shared connections)
- [messaging_integration](messaging_integration.md) (1 shared connections)
- [test_messaging_integration_init_no_connection_manager](test_messaging_integration_init_no_connection_manager.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 145 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*