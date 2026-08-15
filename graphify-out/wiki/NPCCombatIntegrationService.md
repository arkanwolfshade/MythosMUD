# NPCCombatIntegrationService

> 107 nodes

## Key Concepts

- **NPCCombatIntegrationService** (86 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **._complete_player_attack_on_npc_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **test_npc_combat_memory.py** (4 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.handle_npc_death()** (3 connections) — `server/services/npc_combat_handlers.py`
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_handlers.py`
- **.get_combat_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_messaging_integration()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_original_string_id()** (3 connections) — `server/services/npc_combat_integration_service.py`
- *... and 82 more nodes in this community*

## Relationships

- [test_npc_combat_integration_service.py](test_npc_combat_integration_service.py.md) (35 shared connections)
- [get_logger](get_logger.md) (24 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (7 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (5 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (4 shared connections)
- [TestNPCCombatLifecycle](TestNPCCombatLifecycle.md) (4 shared connections)
- [TestNPCCombatRewards](TestNPCCombatRewards.md) (4 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (3 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (3 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (3 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (3 shared connections)

## Source Files

- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_npc_combat_memory.py`

## Audit Trail

- EXTRACTED: 202 (76%)
- INFERRED: 65 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*