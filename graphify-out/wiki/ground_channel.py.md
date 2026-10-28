# ground_channel.py

> 80 nodes · cohesion 0.04

## Key Concepts

- **NPCCombatDataProvider** (44 connections) — `server/services/npc_combat_data_provider.py`
- **test_npc_combat_data_provider.py** (21 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **_NPCCombatIntegrationDeps** (19 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.join_player_to_combat()** (10 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (10 connections)
- **.get_npc_combat_data()** (9 connections) — `server/services/npc_combat_data_provider.py`
- **.join_existing_combat_for_mixin()** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._process_combat_attack()** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **asyncio** (8 connections)
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_player_combat_data()** (6 connections) — `server/services/npc_combat_data_provider.py`
- **Any** (6 connections)
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._resolve_npc_behavior_snapshot()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **.get_messaging_integration()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_npc_disposition()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.join_existing_combat_for_mixin()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_npc_definition()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_npc_instance()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **._resolve_npc_combat_stats()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.join_player_to_combat()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 55 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (15 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (11 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (10 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (4 shared connections)
- [PostgreSQL & SQL Audit Report](PostgreSQL_&_SQL_Audit_Report.md) (2 shared connections)
- [FollowService](FollowService.md) (2 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [saveMapChanges.ts](saveMapChanges.ts.md) (1 shared connections)
- [security.ts](security.ts.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 169 (91%)
- INFERRED: 17 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*