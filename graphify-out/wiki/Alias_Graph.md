# Alias Graph

> 51 nodes

## Key Concepts

- **AliasGraph** (18 connections) — `server/utils/alias_graph.py`
- **alias_expansion.py** (17 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_expansion.py** (14 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (9 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_graph.py** (9 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **check_alias_safety()** (8 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **asyncio** (5 connections)
- **test_check_alias_safety_cycle_detected()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_depth_too_deep()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_ok()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_delegates()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_depth_limit()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_alias_graph_build_graph()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_clear()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_detect_cycle_no_cycle()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_get_expansion_depth()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_init()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_is_safe_to_expand()** (3 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **.build_graph()** (3 connections) — `server/utils/alias_graph.py`
- **.detect_cycle()** (3 connections) — `server/utils/alias_graph.py`
- **._extract_alias_references()** (3 connections) — `server/utils/alias_graph.py`
- **.__init__()** (3 connections) — `server/utils/alias_graph.py`
- **.is_safe_to_expand()** (3 connections) — `server/utils/alias_graph.py`
- **test_validate_expanded_command_invalid_content()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- *... and 26 more nodes in this community*

## Relationships

- [Alias Storage](Alias_Storage.md) (4 shared connections)
- [Test Command Input](Test_Command_Input.md) (4 shared connections)
- [Test Command Validator](Test_Command_Validator.md) (3 shared connections)
- [Processing](Processing.md) (2 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Container Service Helpers](Container_Service_Helpers.md) (1 shared connections)
- [Test Request Context](Test_Request_Context.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`
- `server/tests/unit/utils/test_alias_graph.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 94 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*