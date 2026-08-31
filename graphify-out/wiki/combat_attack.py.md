# combat_attack.py

> 49 nodes

## Key Concepts

- **combat_attack.py** (25 connections) — `server/commands/combat_attack.py`
- **test_combat_attack.py** (20 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **run_handle_attack_command()** (11 connections) — `server/commands/combat_attack.py`
- **asyncio** (11 connections)
- **_execute_phantom_combat_action()** (10 connections) — `server/commands/combat_attack.py`
- **_resolve_combat_damage()** (9 connections) — `server/commands/combat_attack.py`
- **Any** (8 connections)
- **_execute_combat_action()** (7 connections) — `server/commands/combat_attack.py`
- **_validate_attack_player_and_room()** (7 connections) — `server/commands/combat_attack.py`
- **_validate_attack_preconditions()** (6 connections) — `server/commands/combat_attack.py`
- **_get_combat_action_context()** (5 connections) — `server/commands/combat_attack.py`
- **_validate_attack_target_and_action()** (5 connections) — `server/commands/combat_attack.py`
- **test_execute_phantom_combat_action_success()** (5 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_routes_phantom_target()** (5 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_execute_combat_action_failure_message()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_execute_phantom_combat_action_already_dissipated()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_get_combat_action_context_missing_player()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_blocked_by_rest()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_success_path()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_incapacitated()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_missing_target()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_no_combat_zone()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_target_and_action_invalid()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **mock_handler()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_resolve_combat_damage_unarmed_fallback()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- *... and 24 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (5 shared connections)
- [CombatParticipantType](CombatParticipantType.md) (3 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [models/combat.py](models-combat.py.md) (2 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/tests/unit/commands/test_combat_attack.py`

## Audit Trail

- EXTRACTED: 114 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*