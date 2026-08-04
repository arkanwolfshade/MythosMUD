# alias graph rationale

> 54 nodes

## Key Concepts

- **AliasGraph** (18 connections) — `server/utils/alias_graph.py`
- **alias_expansion.py** (17 connections) — `server/command_handler/alias_expansion.py`
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
- **test_alias_expansion.py** (13 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_graph.py** (9 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **alias_graph.py** (8 connections) — `server/utils/alias_graph.py`
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
- *... and 29 more nodes in this community*

## Relationships

- [command commands handler](command_commands_handler.md) (11 shared connections)
- [Loot Generation](Loot_Generation.md) (9 shared connections)
- [command validation commands](command_validation_commands.md) (4 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (3 shared connections)
- [task registry app](task_registry_app.md) (1 shared connections)
- [command validator validators](command_validator_validators.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`
- `server/tests/unit/utils/test_alias_graph.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 186 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*