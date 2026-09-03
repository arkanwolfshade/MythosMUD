# Test Combat Handler

> 88 nodes

## Key Concepts

- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **test_combat_handler.py** (40 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **TargetResolutionResult** (35 connections) — `server/schemas/shared/target_resolution.py`
- **_handler_with_persistence()** (22 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **asyncio** (14 connections)
- **target_resolution.py** (13 connections) — `server/schemas/shared/target_resolution.py`
- **_as_app_with_state()** (9 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_current_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_player()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_accepts_live_phantom()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_dead_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_dissipated_phantom()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_non_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppStatePersistence** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **._validate_combat_target_match()** (5 connections) — `server/commands/combat_handler.py`
- **test_get_player_and_room_no_persistence_on_app()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_failure_message()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_handle_flee_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_handle_taunt_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_validate_combat_action()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_validate_combat_action_empty_name()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 63 more nodes in this community*

## Relationships

- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (20 shared connections)
- [Test Target Resolution Service](Test_Target_Resolution_Service.md) (17 shared connections)
- [Combat Handler](Combat_Handler.md) (8 shared connections)
- [Combat Flee](Combat_Flee.md) (6 shared connections)
- [Test Follow Commands](Test_Follow_Commands.md) (5 shared connections)
- [Combat Taunt](Combat_Taunt.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Combat Loader](Combat_Loader.md) (4 shared connections)
- [Test Spell](Test_Spell.md) (3 shared connections)
- [Test Combat Attack](Test_Combat_Attack.md) (3 shared connections)
- [Test Rest Command](Test_Rest_Command.md) (2 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 231 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*