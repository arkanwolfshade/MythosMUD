# attack combat commands

> 35 nodes

## Key Concepts

- **test_combat_attack.py** (12 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **run_handle_attack_command()** (9 connections) — `server/commands/combat_attack.py`
- **_validate_attack_player_and_room()** (7 connections) — `server/commands/combat_attack.py`
- **Any** (7 connections)
- **_execute_combat_action()** (7 connections) — `server/commands/combat_attack.py`
- **_validate_attack_preconditions()** (6 connections) — `server/commands/combat_attack.py`
- **_validate_attack_target_and_action()** (5 connections) — `server/commands/combat_attack.py`
- **_get_combat_action_context()** (5 connections) — `server/commands/combat_attack.py`
- **test_validate_attack_player_and_room_missing_target()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_incapacitated()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_player_and_room_no_combat_zone()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_validate_attack_target_and_action_invalid()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_get_combat_action_context_missing_player()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_resolve_combat_damage_unarmed_fallback()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_execute_combat_action_failure_message()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_blocked_by_rest()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_run_handle_attack_command_success_path()** (3 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **mock_handler()** (2 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **Validate target name, load player/room, check DP and no_combat.     Returns (pla** (1 connections) — `server/commands/combat_attack.py`
- **Resolve combat target and validate action; return (target_match, npc_instance, N** (1 connections) — `server/commands/combat_attack.py`
- **Run all attack pre-checks; return (player, room_id, target_match, npc_instance,** (1 connections) — `server/commands/combat_attack.py`
- **Load player and resolve NPC instance/name for combat action.     Returns (player** (1 connections) — `server/commands/combat_attack.py`
- **Execute combat action using the proper combat service.** (1 connections) — `server/commands/combat_attack.py`
- **Handle attack commands (attack, punch, kick, etc.).** (1 connections) — `server/commands/combat_attack.py`
- **Unit tests for server.commands.combat_attack (attack preconditions and execution** (1 connections) — `server/tests/unit/commands/test_combat_attack.py`
- *... and 10 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (10 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [combat commands handler](combat_commands_handler.md) (1 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/tests/unit/commands/test_combat_attack.py`

## Audit Trail

- EXTRACTED: 104 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*