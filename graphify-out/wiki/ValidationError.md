# ValidationError

> 350 nodes · cohesion 0.01

## Key Concepts

- **NPCCombatIntegrationService** (100 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_integration_service.py** (60 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (47 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **NPCCombatUUIDMapping** (40 connections) — `server/services/npc_combat_uuid_mapping.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **asyncio** (25 connections)
- **test_npc_combat_integration_join.py** (24 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- **npc_combat_integration_validation_mixin.py** (22 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **test_npc_combat_handlers.py** (22 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_handlers.py** (16 connections) — `server/services/npc_combat_handlers.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **.__init__()** (13 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_lucidity.py** (13 connections) — `server/services/npc_combat_lucidity.py`
- **NPCCombatRewards** (13 connections) — `server/services/npc_combat_rewards.py`
- **spawn_defaults.py** (12 connections) — `server/constants/spawn_defaults.py`
- **CombatResultCtx** (12 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatIntegrationValidationMixin** (12 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatIntegrationCombatMixin** (11 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_uuid_mapping.py** (9 connections) — `server/services/npc_combat_uuid_mapping.py`
- **asyncio** (9 connections)
- **fixture** (8 connections)
- *... and 325 more nodes in this community*

## Relationships

- [Room](Room.md) (18 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (16 shared connections)
- [ground_channel.py](ground_channel.py.md) (15 shared connections)
- [PostgreSQL & SQL Audit Report](PostgreSQL_&_SQL_Audit_Report.md) (14 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (12 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (9 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (9 shared connections)
- [_complete_tutorial_with_rewards](_complete_tutorial_with_rewards.md) (7 shared connections)
- [look_container.py](look_container.py.md) (6 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (6 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (5 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (5 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/models/combat.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_lucidity.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_combat_status_segments.py`
- `server/tests/unit/services/test_npc_combat_handlers.py`
- `server/tests/unit/services/test_npc_combat_integration_join.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`
- `server/tests/unit/services/test_npc_combat_memory.py`
- `server/tests/unit/services/test_npc_combat_rewards.py`
- `server/tests/unit/services/test_npc_combat_uuid_mapping.py`

## Audit Trail

- EXTRACTED: 674 (89%)
- INFERRED: 86 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*