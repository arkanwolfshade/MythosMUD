# CombatMessagingService

> 43 nodes

## Key Concepts

- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging/base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging_service.py** (9 connections) — `server/services/combat_messaging_service.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **HasConnectionManager** (6 connections) — `server/services/combat_messaging/base.py`
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **CombatMessages** (5 connections)
- **test_combat_messaging_service.py** (5 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **combat_messaging/__init__.py** (3 connections) — `server/services/combat_messaging/__init__.py`
- **.get_error_message()** (2 connections) — `server/services/combat_messaging_service.py`
- **.__init__()** (2 connections) — `server/services/combat_messaging_service.py`
- **Any** (1 connections)
- **Base integration with connection manager resolution.** (1 connections) — `server/services/combat_messaging/base.py`
- **Base for mixins that require connection_manager. Satisfies mypy attr-defined…** (1 connections) — `server/services/combat_messaging/base.py`
- *... and 18 more nodes in this community*

## Relationships

- [build_event](build_event.md) (20 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [.connection_manager](connection_manager.md) (4 shared connections)
- [TestCombatMessagingService](TestCombatMessagingService.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [test_combat_schema.py](test_combat_schema.py.md) (2 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (1 shared connections)
- [messaging_integration](messaging_integration.md) (1 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 105 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*