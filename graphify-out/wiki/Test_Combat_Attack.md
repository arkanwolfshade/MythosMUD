# Test Combat Attack

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

- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (5 shared connections)
- [Test Magic Service](Test_Magic_Service.md) (3 shared connections)
- [Test Weapons](Test_Weapons.md) (3 shared connections)
- [Test Combat Handler](Test_Combat_Handler.md) (3 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (3 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (2 shared connections)
- [Test Config Init](Test_Config_Init.md) (2 shared connections)
- [Test Npc Combat Integration Class](Test_Npc_Combat_Integration_Class.md) (2 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Combat Handler](Combat_Handler.md) (1 shared connections)
- [Combat Integration Base](Combat_Integration_Base.md) (1 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/tests/unit/commands/test_combat_attack.py`

## Audit Trail

- EXTRACTED: 114 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*