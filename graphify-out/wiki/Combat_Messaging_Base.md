# Combat Messaging Base

> 37 nodes · cohesion 0.07

## Key Concepts

- **CombatMessagingService** (19 connections) — `server/services/combat_messaging_service.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **HasConnectionManager** (7 connections) — `server/services/combat_messaging/base.py`
- **base.py** (6 connections) — `server/services/combat_messaging/base.py`
- **CombatMessages** (6 connections) — `server/services/combat_messaging_service.py`
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **.connection_manager()** (5 connections) — `server/services/combat_messaging/base.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **Any** (4 connections) — `server/services/combat_messaging/base.py`
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **test_combat_messaging_service.py** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.service()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **Any** (2 connections) — `server/services/combat_messaging_service.py`
- **.get_error_message()** (2 connections) — `server/services/combat_messaging_service.py`
- **.__init__()** (2 connections) — `server/services/combat_messaging_service.py`
- **Base integration with connection manager resolution.** (1 connections) — `server/services/combat_messaging/base.py`
- **Base for mixins that require connection_manager. Satisfies mypy attr-defined che** (1 connections) — `server/services/combat_messaging/base.py`
- **Base class with connection manager setup. Used by CombatMessagingIntegration.** (1 connections) — `server/services/combat_messaging/base.py`
- **Lazily resolve the connection manager from the application container.** (1 connections) — `server/services/combat_messaging/base.py`
- **Return the connection manager, resolving it from the application container if ne** (1 connections) — `server/services/combat_messaging/base.py`
- *... and 12 more nodes in this community*

## Relationships

- [[Standardized Error Responses]] (4 shared connections)
- [[Combat Messaging Tests]] (4 shared connections)
- [[Services Combat Messaging]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Combat Player Broadcasts]] (2 shared connections)
- [[Application DI Bundles]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)
- [[Combat Services Messaging]] (1 shared connections)
- [[Combat Schema Validation]] (1 shared connections)

## Source Files

- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 102 (90%)
- INFERRED: 11 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
