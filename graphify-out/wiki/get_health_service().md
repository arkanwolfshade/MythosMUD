# get health service()

> 43 nodes

## Key Concepts

- **CombatResult** (23 connections) — `server/models/combat.py`
- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
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
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **.get_messaging_integration()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_npc_attack_on_player_started()** (3 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **Result of a combat action.** (1 connections) — `server/models/combat.py`
- **Protocol** (1 connections)
- *... and 18 more nodes in this community*

## Relationships

- [test combat attack handler](test_combat_attack_handler.md) (15 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (14 shared connections)
- [close db()](close_db%28%29.md) (7 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 190 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*