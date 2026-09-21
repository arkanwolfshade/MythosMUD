# TestCombatMessagingService

> 85 nodes

## Key Concepts

- **TestCombatMessagingService** (21 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **asyncio** (16 connections)
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **CombatBroadcastMixin** (11 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_combat_attack()** (7 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_combat_target_switch()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessages** (5 connections)
- **._send_attacker_personal_combat_message()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **._send_attacker_personal_message_if_needed()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.service()** (4 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **Any** (4 connections)
- **test_combat_messaging_service.py** (4 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **._build_combat_attack_messages()** (3 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.test_get_attack_message_attacker_perspective()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_custom_action_type()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- *... and 60 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [AppConfig](AppConfig.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (1 shared connections)
- [messaging_integration](messaging_integration.md) (1 shared connections)
- [test_messaging_integration_init_no_connection_manager](test_messaging_integration_init_no_connection_manager.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 138 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*