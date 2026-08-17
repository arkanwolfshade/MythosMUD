# server commands combat handler combatcommandhandler

> 121 nodes

## Key Concepts

- **npc_combat_integration_service.py** (53 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatIntegrationService** (49 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **npc_combat_handlers.py** (16 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **CombatResultCtx** (12 connections) — `server/services/npc_combat_handlers.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **NPCCombatIntegrationValidationMixin** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **npc_combat_rewards.py** (10 connections) — `server/services/npc_combat_rewards.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_lifecycle.py** (8 connections) — `server/services/npc_combat_lifecycle.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_memory.py** (7 connections) — `server/services/npc_combat_memory.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **.handle_combat_result()** (5 connections) — `server/services/npc_combat_handlers.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_lifecycle.py** (5 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **test_npc_combat_rewards.py** (5 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **._complete_player_attack_on_npc_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- *... and 96 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (23 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (18 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (13 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (10 shared connections)
- [server services npc combat integration](server_services_npc_combat_integration.md) (8 shared connections)
- [server services npc combat data](server_services_npc_combat_data.md) (7 shared connections)
- [server services npc combat grace](server_services_npc_combat_grace.md) (6 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (6 shared connections)
- [npccombatlucidity](npccombatlucidity.md) (6 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (5 shared connections)
- [server game mechanics gamemechanicsservice](server_game_mechanics_gamemechanicsservice.md) (5 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (5 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/services/combat_messaging_integration.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`
- `server/tests/unit/services/test_npc_combat_memory.py`
- `server/tests/unit/services/test_npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 293 (90%)
- INFERRED: 33 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*