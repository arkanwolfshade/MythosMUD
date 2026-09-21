# NPCCombatIntegrationService

> 402 nodes

## Key Concepts

- **NPCCombatIntegrationService** (86 connections) — `server/services/npc_combat_integration_service.py`
- **PlayerCombatService** (77 connections) — `server/services/player_combat_service.py`
- **npc_combat_integration_service.py** (53 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (46 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **NPCCombatUUIDMapping** (38 connections) — `server/services/npc_combat_uuid_mapping.py`
- **test_player_combat_service.py** (36 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **asyncio** (25 connections)
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **asyncio** (22 connections)
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **npc_combat_handlers.py** (16 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **npc_combat_grace.py** (15 connections) — `server/services/npc_combat_grace.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **CombatResultCtx** (12 connections) — `server/services/npc_combat_handlers.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatIntegrationValidationMixin** (11 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **npc_combat_rewards.py** (10 connections) — `server/services/npc_combat_rewards.py`
- *... and 377 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (51 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (12 shared connections)
- [CombatService](CombatService.md) (12 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (9 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (8 shared connections)
- [event_types.py](event_types.py.md) (7 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (5 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [mock_async_persistence](mock_async_persistence.md) (5 shared connections)
- [test_npc_combat_integration_service_npc_aggro.py](test_npc_combat_integration_service_npc_aggro.py.md) (4 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/config/__init__.py`
- `server/container/bundles/combat.py`
- `server/services/combat_messaging_integration.py`
- `server/services/npc_combat_grace.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_npc_combat_grace.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`
- `server/tests/unit/services/test_npc_combat_memory.py`
- `server/tests/unit/services/test_npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 745 (87%)
- INFERRED: 115 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*