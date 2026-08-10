# Player Position Service

> 51 nodes

## Key Concepts

- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_as_app_with_state()** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_player()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_current_room()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_non_npc()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_dead_npc()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_persistence_on_app()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_failure_message()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_combat_command_handler_requires_async_persistence()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_extract_combat_command_data_string_type()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_extract_combat_command_data_enum_value()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_validate_target_name_empty()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_validate_target_name_present()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_room_forbids_combat_true()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_room_forbids_combat_false_no_attrs()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_validate_combat_action()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_validate_combat_action_empty_name()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_handle_flee_command_delegates()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_handle_taunt_command_delegates()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 26 more nodes in this community*

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (12 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (7 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (6 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (5 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (2 shared connections)

## Source Files

- `server/tests/unit/commands/test_combat_handler.py`

## Audit Trail

- EXTRACTED: 181 (92%)
- INFERRED: 15 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*