# CombatMessagingService

> 23 nodes

## Key Concepts

- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **CombatMessages** (5 connections)
- **test_combat_messaging_service.py** (4 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_error_message()** (2 connections) — `server/services/combat_messaging_service.py`
- **.__init__()** (2 connections) — `server/services/combat_messaging_service.py`
- **Any** (1 connections)
- **Base class with connection manager setup. Used by CombatMessagingIntegration.** (1 connections) — `server/services/combat_messaging/base.py`
- **Generate combat start messages for all room occupants. Args: attacker_name:…** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate combat end messages for all room occupants. Args: winner_name: Name of…** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate thematic error messages for combat actions. Args: error_type: Type of…** (1 connections) — `server/services/combat_messaging_service.py`
- **Validate NPC message templates against the schema. Args: messages_data: NPC…** (1 connections) — `server/services/combat_messaging_service.py`
- **Service for generating combat messages. This service creates thematic,…** (1 connections) — `server/services/combat_messaging_service.py`
- **Initialize the combat messaging service.** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate an attack message based on perspective and NPC configuration. Args:…** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate a death message for an NPC. Args: npc_name: Name of the NPC that died…** (1 connections) — `server/services/combat_messaging_service.py`
- **Unit tests for combat messaging service. Tests the CombatMessagingService class…** (1 connections) — `server/tests/unit/services/test_combat_messaging_service.py`

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [TestCombatMessagingService](TestCombatMessagingService.md) (4 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (3 shared connections)
- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [test_combat_schema.py](test_combat_schema.py.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 66 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*