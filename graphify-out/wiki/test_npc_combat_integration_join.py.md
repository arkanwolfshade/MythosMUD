# test_npc_combat_integration_join.py

> 55 nodes

## Key Concepts

- **test_npc_combat_integration_join.py** (24 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- **test_combat_attack.py** (23 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **AlreadyEngagedError** (13 connections) — `server/services/combat_types.py`
- **asyncio** (13 connections)
- **_participant()** (8 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- **test_attacking_an_npc_already_in_combat_joins_the_fight()** (8 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- **_fight()** (7 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- **test_attack_on_another_foe_is_refused_before_first_engagement_side_effects()** (7 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- **test_engaged_player_cannot_queue_an_attack_on_a_foe_outside_their_fight()** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- **test_execute_combat_action_reports_the_foe_when_already_engaged()** (5 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_execute_phantom_combat_action_success()** (5 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_routes_phantom_target()** (5 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_get_engaged_foe_name_reports_the_current_foe_only_for_other_targets()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- **asyncio** (5 connections)
- **test_execute_attack_on_npc_goes_through_the_normal_attack_path()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_execute_combat_action_failure_message()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_execute_phantom_combat_action_already_dissipated()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_get_combat_action_context_missing_player()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_blocked_by_rest()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_success_path()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_incapacitated()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_missing_target()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_no_combat_zone()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_target_and_action_invalid()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **integration_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- *... and 30 more nodes in this community*

## Relationships

- [NpcDisposition](NpcDisposition.md) (19 shared connections)
- [CombatService](CombatService.md) (11 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [TargetType](TargetType.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [combat_assist.py](combat_assist.py.md) (1 shared connections)

## Source Files

- `server/services/combat_types.py`
- `server/tests/unit/commands/test_combat_attack.py`
- `server/tests/unit/services/test_npc_combat_integration_join.py`

## Audit Trail

- EXTRACTED: 121 (91%)
- INFERRED: 12 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*