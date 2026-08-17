# .connection_manager

> 29 nodes

## Key Concepts

- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (5 connections)
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **.get_messaging_integration()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Any** (3 connections)
- **setter** (1 connections)
- **Protocol** (1 connections)
- **Check connection state before publishing combat ended event.** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Lazily resolve the connection manager from the application container.** (1 connections) — `server/services/combat_messaging/base.py`
- **Return the connection manager, resolving it from the application container if…** (1 connections) — `server/services/combat_messaging/base.py`
- **Explicitly set the connection manager (primarily used in tests).** (1 connections) — `server/services/combat_messaging/base.py`
- **Process combat attack, starting new combat or continuing existing one.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Start a new combat and process initial attack.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Broadcast room occupants update to killer's room after NPC death. Swallows…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return combat service dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 4 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (8 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (7 shared connections)
- [CombatMessagingService](CombatMessagingService.md) (4 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [.get_instance](get_instance.md) (2 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)
- [get_current_tick](get_current_tick.md) (2 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (1 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (1 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (1 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/npc_combat_integration_combat_mixin.py`

## Audit Trail

- EXTRACTED: 58 (82%)
- INFERRED: 13 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*