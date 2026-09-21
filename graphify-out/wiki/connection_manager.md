# .connection_manager

> 10 nodes

## Key Concepts

- **.connection_manager()** (13 connections) — `server/services/combat_messaging/base.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **setter** (1 connections)
- **Check connection state before publishing combat ended event.** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Lazily resolve the connection manager from the application container.** (1 connections) — `server/services/combat_messaging/base.py`
- **Return the connection manager, resolving it from the application container if…** (1 connections) — `server/services/combat_messaging/base.py`
- **Explicitly set the connection manager (primarily used in tests).** (1 connections) — `server/services/combat_messaging/base.py`

## Relationships

- [build_event](build_event.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (2 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (1 shared connections)
- [TestCombatMessagingService](TestCombatMessagingService.md) (1 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_messaging/base.py`

## Audit Trail

- EXTRACTED: 16 (67%)
- INFERRED: 8 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*