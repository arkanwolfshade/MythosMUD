# get health service()

> 69 nodes

## Key Concepts

- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatDataProvider** (29 connections) — `server/services/npc_combat_data_provider.py`
- **CombatResult** (23 connections) — `server/models/combat.py`
- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- **npc_combat_integration_combat_mixin.py** (15 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCCombatIntegrationCombatMixin** (11 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_make_participant()** (10 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_combat_instance()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (6 connections)
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **UUID** (5 connections)
- **.get_npc_combat_data()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- *... and 44 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (30 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (11 shared connections)
- [world](world.md) (9 shared connections)
- [combat](combat.md) (8 shared connections)
- [. init ()](_init_%28%29.md) (8 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [test exploration service](test_exploration_service.md) (3 shared connections)
- [get current tick()](get_current_tick%28%29.md) (3 shared connections)
- [src/**/*.spec](src-__-_.spec.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [add hashed password column](add_hashed_password_column.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_combat_service.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 333 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*