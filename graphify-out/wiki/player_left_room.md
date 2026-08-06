# player left room

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

- [player model models](player_model_models.md) (7 shared connections)
- [command validation commands](command_validation_commands.md) (6 shared connections)
- [alias graph rationale](alias_graph_rationale.md) (3 shared connections)
- [command validator validators](command_validator_validators.md) (3 shared connections)
- [combat attack handler](combat_attack_handler.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)
- [task registry app](task_registry_app.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`

## Audit Trail

- EXTRACTED: 84 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*