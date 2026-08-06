# services ascii map

> 35 nodes

## Key Concepts

- **TargetType** (39 connections) — `server/schemas/shared/target_resolution.py`
- **handle_teach_command()** (18 connections) — `server/commands/teach_command.py`
- **teach_command.py** (14 connections) — `server/commands/teach_command.py`
- **test_teach_command.py** (13 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_spell_effects_support.py** (13 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **_target()** (7 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_handle_teach_command()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_target()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_process_stat_modify_rejects_non_player()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_process_stat_modify_success()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_process_create_object_missing_prototype()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_process_create_object_for_player()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_create_object_for_room_placeholder()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **Any** (2 connections)
- **test_handle_teach_command_no_spell_learning_service()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_player_not_found()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_target_resolution_failure()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_not_npc_target()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_learn_failure()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_success_with_corruption()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_build_stat_modifications_shorthand()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_build_stat_modifications_missing()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **Teach command handler for learning spells from NPC teachers.  This module handle** (1 connections) — `server/commands/teach_command.py`
- *... and 10 more nodes in this community*

## Relationships

- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (9 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (9 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (3 shared connections)
- [models player related](models_player_related.md) (3 shared connections)
- [party service game](party_service_game.md) (3 shared connections)
- [realtime real time](realtime_real_time.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [room renderer functions](room_renderer_functions.md) (2 shared connections)
- [commands position system](commands_position_system.md) (2 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (2 shared connections)
- [magic completion game](magic_completion_game.md) (2 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (2 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_teach_command.py`
- `server/tests/unit/game/magic/test_spell_effects_support.py`

## Audit Trail

- EXTRACTED: 161 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*