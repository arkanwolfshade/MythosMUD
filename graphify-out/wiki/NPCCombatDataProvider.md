# NPCCombatDataProvider

> 121 nodes

## Key Concepts

- **NPCCombatDataProvider** (38 connections) — `server/services/npc_combat_data_provider.py`
- **combat_attack.py** (25 connections) — `server/commands/combat_attack.py`
- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **test_combat_attack.py** (20 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_npc_combat_data_provider.py** (18 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_counter.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **run_handle_attack_command()** (11 connections) — `server/commands/combat_attack.py`
- **asyncio** (11 connections)
- **_execute_phantom_combat_action()** (10 connections) — `server/commands/combat_attack.py`
- **_resolve_combat_damage()** (9 connections) — `server/commands/combat_attack.py`
- **game_tick_counter.py** (9 connections) — `server/app/game_tick_counter.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Any** (8 connections)
- **spawn_defaults.py** (8 connections) — `server/constants/spawn_defaults.py`
- **_execute_combat_action()** (7 connections) — `server/commands/combat_attack.py`
- **_validate_attack_player_and_room()** (7 connections) — `server/commands/combat_attack.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **asyncio** (7 connections)
- **_validate_attack_preconditions()** (6 connections) — `server/commands/combat_attack.py`
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 96 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (20 shared connections)
- [NATSError](NATSError.md) (15 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [CombatInstance](CombatInstance.md) (10 shared connections)
- [CombatService](CombatService.md) (9 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (8 shared connections)
- [reset_current_tick](reset_current_tick.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/commands/combat_attack.py`
- `server/constants/spawn_defaults.py`
- `server/services/combat_messaging_integration.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/tests/unit/commands/test_combat_attack.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 300 (94%)
- INFERRED: 19 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*