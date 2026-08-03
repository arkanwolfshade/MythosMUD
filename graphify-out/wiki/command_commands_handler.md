# command commands handler

> 124 nodes

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **Any** (14 connections)
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **CommandExecutionRequest** (11 connections)
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (10 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **test_grace_period_blocking.py** (8 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler_unified.py`
- **check_alias_safety()** (6 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (6 connections) — `server/command_handler/alias_expansion.py`
- *... and 99 more nodes in this community*

## Relationships

- [commands admin mute](commands_admin_mute.md) (19 shared connections)
- [command validation commands](command_validation_commands.md) (15 shared connections)
- [game weapon player](game_weapon_player.md) (15 shared connections)
- [command inventory factories](command_inventory_factories.md) (9 shared connections)
- [command commands validation](command_commands_validation.md) (8 shared connections)
- [request context realtime](request_context_realtime.md) (6 shared connections)
- [npc rationale extract](npc_rationale_extract.md) (6 shared connections)
- [command commands handler](command_commands_handler.md) (6 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (5 shared connections)
- [commands command validation](commands_command_validation.md) (5 shared connections)
- [manager room npcs](manager_room_npcs.md) (5 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (4 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 553 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*