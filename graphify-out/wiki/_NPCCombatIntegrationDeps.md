# _NPCCombatIntegrationDeps

> 30 nodes

## Key Concepts

- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **combat_messaging_integration.py** (5 connections) — `server/services/combat_messaging_integration.py`
- **UUID** (5 connections)
- **.get_messaging_integration()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_npc_attack_on_player_started()** (3 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_messaging_integration()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **combat_messaging/__init__.py** (3 connections) — `server/services/combat_messaging/__init__.py`
- **Protocol** (1 connections)
- **Combat messaging integration with real-time messaging system. This package…** (1 connections) — `server/services/combat_messaging/__init__.py`
- **Combat messaging integration with real-time messaging system. Re-exports from…** (1 connections) — `server/services/combat_messaging_integration.py`
- **Integrates combat messaging with the real-time messaging system. This service…** (1 connections) — `server/services/combat_messaging/integration.py`
- **Structured logging / observability trail when NPC-initiated combat begins.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Process combat attack, starting new combat or continuing existing one.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Start a new combat and process initial attack.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Broadcast room occupants update to killer's room after NPC death. Swallows…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize…** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Return combat service dependency.** (1 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 5 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (10 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [get_current_tick](get_current_tick.md) (2 shared connections)
- [messaging_integration](messaging_integration.md) (1 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging_integration.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 99 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*