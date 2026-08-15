# combat_attack.py

> 41 nodes

## Key Concepts

- **combat_attack.py** (17 connections) — `server/commands/combat_attack.py`
- **test_combat_attack.py** (12 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **run_handle_attack_command()** (9 connections) — `server/commands/combat_attack.py`
- **_resolve_combat_damage()** (8 connections) — `server/commands/combat_attack.py`
- **asyncio** (8 connections)
- **_execute_combat_action()** (7 connections) — `server/commands/combat_attack.py`
- **_validate_attack_player_and_room()** (7 connections) — `server/commands/combat_attack.py`
- **Any** (7 connections)
- **_validate_attack_preconditions()** (6 connections) — `server/commands/combat_attack.py`
- **_get_combat_action_context()** (5 connections) — `server/commands/combat_attack.py`
- **_validate_attack_target_and_action()** (5 connections) — `server/commands/combat_attack.py`
- **test_execute_combat_action_failure_message()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_get_combat_action_context_missing_player()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_blocked_by_rest()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_success_path()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_incapacitated()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_missing_target()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_no_combat_zone()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_target_and_action_invalid()** (4 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **mock_handler()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_resolve_combat_damage_unarmed_fallback()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **fixture** (1 connections)
- **Attack command flow: validation and execution. Extracted from combat.py to…** (1 connections) — `server/commands/combat_attack.py`
- **Resolve damage from equipped weapon or fall back to config unarmed damage.** (1 connections) — `server/commands/combat_attack.py`
- **Execute combat action using the proper combat service.** (1 connections) — `server/commands/combat_attack.py`
- *... and 16 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (3 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (1 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/tests/unit/commands/test_combat_attack.py`

## Audit Trail

- EXTRACTED: 80 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*