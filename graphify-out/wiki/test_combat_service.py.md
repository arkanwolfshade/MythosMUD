# test_combat_service.py

> 84 nodes

## Key Concepts

- **test_combat_service.py** (37 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (28 connections) — `server/tests/unit/services/test_combat_service.py`
- **CombatResult** (26 connections) — `server/models/combat.py`
- **asyncio** (17 connections)
- **_make_combat_instance()** (15 connections) — `server/tests/unit/services/test_combat_service.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_make_participant()** (12 connections) — `server/tests/unit/services/test_combat_service.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (7 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (7 connections) — `server/tests/unit/services/test_combat_service.py`
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_register_combat_state_tracks_participants()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_get_combat_by_participant_returns_active_combat()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_start_combat_happy_path()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_sync_npc_participant_dp_after_spell_damage()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- *... and 59 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [get_config](get_config.md) (8 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [combat_service.py](combat_service.py.md) (2 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (1 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (1 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [TestCombatMessagingService](TestCombatMessagingService.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 205 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*