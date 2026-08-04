# fixtures mock helpers

> 20 nodes

## Key Concepts

- **alias_expansion.py** (17 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_expansion.py** (13 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **Any** (2 connections)
- **CommandExecutionRequest** (2 connections)
- **test_check_alias_safety_cycle_detected()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_depth_too_deep()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_ok()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_too_long()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_invalid_content()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_ok()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_depth_limit()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_delegates()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **Alias Expansion Logic for MythosMUD.  This module handles alias resolution, expa** (1 connections) — `server/command_handler/alias_expansion.py`
- **Check if an alias is safe to expand.      Builds an alias dependency graph and c** (1 connections) — `server/command_handler/alias_expansion.py`
- **Validate an expanded command for length and content.      Args:         expanded** (1 connections) — `server/command_handler/alias_expansion.py`
- **Handle command processing with alias expansion and loop detection.      This fun** (1 connections) — `server/command_handler/alias_expansion.py`
- **Unit tests for alias_expansion module.** (1 connections) — `server/tests/unit/commands/test_alias_expansion.py`

## Relationships

- [command commands handler](command_commands_handler.md) (6 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (4 shared connections)
- [alias graph rationale](alias_graph_rationale.md) (3 shared connections)
- [command validator validators](command_validator_validators.md) (3 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [command validation commands](command_validation_commands.md) (2 shared connections)
- [commands whisper command](commands_whisper_command.md) (1 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [request context realtime](request_context_realtime.md) (1 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`

## Audit Trail

- EXTRACTED: 84 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*