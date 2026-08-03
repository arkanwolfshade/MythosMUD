# alias graph rationale

> 51 nodes

## Key Concepts

- **AliasGraph** (18 connections) — `server/utils/alias_graph.py`
- **alias_expansion.py** (17 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_expansion.py** (13 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **CommandExecutionRequest** (9 connections)
- **test_alias_graph.py** (9 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_init()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_build_graph()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_detect_cycle_no_cycle()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_is_safe_to_expand()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_get_expansion_depth()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_clear()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **.__init__()** (3 connections) — `server/utils/alias_graph.py`
- **.build_graph()** (3 connections) — `server/utils/alias_graph.py`
- **._extract_alias_references()** (3 connections) — `server/utils/alias_graph.py`
- **.detect_cycle()** (3 connections) — `server/utils/alias_graph.py`
- **.is_safe_to_expand()** (3 connections) — `server/utils/alias_graph.py`
- **Any** (2 connections)
- **CommandExecutionRequest** (2 connections)
- **test_check_alias_safety_cycle_detected()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_depth_too_deep()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_ok()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_too_long()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- *... and 26 more nodes in this community*

## Relationships

- [command validation commands](command_validation_commands.md) (7 shared connections)
- [command commands handler](command_commands_handler.md) (6 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [commands position system](commands_position_system.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [commands command validation](commands_command_validation.md) (2 shared connections)
- [command validator validators](command_validator_validators.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`
- `server/tests/unit/utils/test_alias_graph.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 164 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*