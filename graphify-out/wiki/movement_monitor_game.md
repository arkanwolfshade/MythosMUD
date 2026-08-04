# movement monitor game

> 83 nodes

## Key Concepts

- **test_combat_service.py** (37 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (28 connections) — `server/tests/unit/services/test_combat_service.py`
- **CombatResult** (23 connections) — `server/models/combat.py`
- **_make_combat_instance()** (15 connections) — `server/tests/unit/services/test_combat_service.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_make_participant()** (12 connections) — `server/tests/unit/services/test_combat_service.py`
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
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_sync_npc_participant_dp_after_spell_damage()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_register_combat_state_tracks_participants()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **.get_messaging_integration()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 58 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (18 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (8 shared connections)
- [services combat sync](services_combat_sync.md) (5 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [command factories exploration](command_factories_exploration.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [command models moderation](command_models_moderation.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 328 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*