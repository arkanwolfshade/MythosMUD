# NPCCombatDataProvider

> 123 nodes

## Key Concepts

- **NPCCombatDataProvider** (43 connections) — `server/services/npc_combat_data_provider.py`
- **combat_attack.py** (25 connections) — `server/commands/combat_attack.py`
- **test_npc_combat_data_provider.py** (20 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_combat_attack.py** (19 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_counter.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **target_resolution.py** (12 connections) — `server/schemas/shared/target_resolution.py`
- **run_handle_attack_command()** (11 connections) — `server/commands/combat_attack.py`
- **asyncio** (11 connections)
- **_execute_phantom_combat_action()** (10 connections) — `server/commands/combat_attack.py`
- **_resolve_combat_damage()** (9 connections) — `server/commands/combat_attack.py`
- **.get_npc_combat_data()** (9 connections) — `server/services/npc_combat_data_provider.py`
- **game_tick_counter.py** (9 connections) — `server/app/game_tick_counter.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Any** (8 connections)
- **asyncio** (8 connections)
- **_execute_combat_action()** (7 connections) — `server/commands/combat_attack.py`
- **_validate_attack_player_and_room()** (7 connections) — `server/commands/combat_attack.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_validate_attack_preconditions()** (6 connections) — `server/commands/combat_attack.py`
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Any** (6 connections)
- **_get_combat_action_context()** (5 connections) — `server/commands/combat_attack.py`
- *... and 98 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (28 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (12 shared connections)
- [TargetType](TargetType.md) (6 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (5 shared connections)
- [reset_current_tick](reset_current_tick.md) (4 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (3 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/commands/combat_attack.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/commands/test_combat_attack.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 275 (93%)
- INFERRED: 20 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*