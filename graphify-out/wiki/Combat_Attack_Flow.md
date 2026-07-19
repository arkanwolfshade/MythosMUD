# Combat Attack Flow

> 39 nodes · cohesion 0.07

## Key Concepts

- **combat_attack.py** (13 connections) — `server/commands/combat_attack.py`
- **test_combat_attack.py** (12 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **Any** (8 connections) — `server/commands/combat_attack.py`
- **_resolve_combat_damage()** (7 connections) — `server/commands/combat_attack.py`
- **run_handle_attack_command()** (7 connections) — `server/commands/combat_attack.py`
- **_validate_attack_preconditions()** (7 connections) — `server/commands/combat_attack.py`
- **_execute_combat_action()** (6 connections) — `server/commands/combat_attack.py`
- **_get_combat_action_context()** (4 connections) — `server/commands/combat_attack.py`
- **_validate_attack_player_and_room()** (4 connections) — `server/commands/combat_attack.py`
- **_validate_attack_target_and_action()** (4 connections) — `server/commands/combat_attack.py`
- **mock_handler()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_execute_combat_action_failure_message()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_get_combat_action_context_missing_player()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_resolve_combat_damage_unarmed_fallback()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_blocked_by_rest()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_success_path()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_incapacitated()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_missing_target()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_no_combat_zone()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_target_and_action_invalid()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **Attack command flow: validation and execution.  Extracted from combat.py to redu** (1 connections) — `server/commands/combat_attack.py`
- **Resolve damage from equipped weapon or fall back to config unarmed damage.** (1 connections) — `server/commands/combat_attack.py`
- **Execute combat action using the proper combat service.** (1 connections) — `server/commands/combat_attack.py`
- **Handle attack commands (attack, punch, kick, etc.).** (1 connections) — `server/commands/combat_attack.py`
- **Validate target name, load player/room, check DP and no_combat.     Returns (pla** (1 connections) — `server/commands/combat_attack.py`
- *... and 14 more nodes in this community*

## Relationships

- [[NPC Admin API]] (3 shared connections)
- [[NPC Services Bundle]] (3 shared connections)
- [[Weapon Resolution Helpers]] (2 shared connections)
- [[Combat Command Handler]] (2 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/tests/unit/commands/test_combat_attack.py`

## Audit Trail

- EXTRACTED: 109 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
