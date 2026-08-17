# CombatMessagingService

> 31 nodes

## Key Concepts

- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **CombatMessages** (5 connections)
- **test_combat_messaging_service.py** (5 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.service()** (4 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **Any** (3 connections)
- **.get_error_message()** (2 connections) — `server/services/combat_messaging_service.py`
- **.__init__()** (2 connections) — `server/services/combat_messaging_service.py`
- **Any** (1 connections)
- **fixture** (1 connections)
- **Base class with connection manager setup. Used by CombatMessagingIntegration.** (1 connections) — `server/services/combat_messaging/base.py`
- **Lazily resolve the connection manager from the application container.** (1 connections) — `server/services/combat_messaging/base.py`
- **Generate combat start messages for all room occupants. Args: attacker_name:…** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate combat end messages for all room occupants. Args: winner_name: Name of…** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate thematic error messages for combat actions. Args: error_type: Type of…** (1 connections) — `server/services/combat_messaging_service.py`
- **Validate NPC message templates against the schema. Args: messages_data: NPC…** (1 connections) — `server/services/combat_messaging_service.py`
- **Service for generating combat messages. This service creates thematic,…** (1 connections) — `server/services/combat_messaging_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [TestCombatMessagingService](TestCombatMessagingService.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [.connection_manager](connection_manager.md) (3 shared connections)
- [CombatMessagingIntegration](CombatMessagingIntegration.md) (1 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [combat_schema.py](combat_schema.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 50 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*