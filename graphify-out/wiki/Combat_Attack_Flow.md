# Combat Attack Flow

> 49 nodes

## Key Concepts

- **combat_attack.py** (17 connections) — `server/commands/combat_attack.py`
- **test_combat_attack.py** (12 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **run_handle_attack_command()** (9 connections) — `server/commands/combat_attack.py`
- **_resolve_combat_damage()** (8 connections) — `server/commands/combat_attack.py`
- **_validate_attack_player_and_room()** (7 connections) — `server/commands/combat_attack.py`
- **Any** (7 connections)
- **_execute_combat_action()** (7 connections) — `server/commands/combat_attack.py`
- **_validate_attack_preconditions()** (6 connections) — `server/commands/combat_attack.py`
- **Any** (6 connections)
- **_validate_attack_target_and_action()** (5 connections) — `server/commands/combat_attack.py`
- **_get_combat_action_context()** (5 connections) — `server/commands/combat_attack.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
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
- *... and 24 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (1 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/commands/combat_handler.py`
- `server/tests/unit/commands/test_combat_attack.py`

## Audit Trail

- EXTRACTED: 158 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*