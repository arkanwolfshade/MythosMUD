# test alias graph

> 38 nodes

## Key Concepts

- **AliasGraph** (18 connections) — `server/utils/alias_graph.py`
- **alias_expansion.py** (16 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_graph.py** (9 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **handle_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (6 connections) — `server/command_handler/alias_expansion.py`
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
- **.get_expansion_depth()** (2 connections) — `server/utils/alias_graph.py`
- **.clear()** (2 connections) — `server/utils/alias_graph.py`
- **Alias Expansion Logic for MythosMUD.  This module handles alias resolution, expa** (1 connections) — `server/command_handler/alias_expansion.py`
- **Check if an alias is safe to expand.      Builds an alias dependency graph and c** (1 connections) — `server/command_handler/alias_expansion.py`
- **Handle command processing with alias expansion and loop detection.      This fun** (1 connections) — `server/command_handler/alias_expansion.py`
- **Unit tests for alias_graph utilities.  Tests the AliasGraph class.** (1 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **Test AliasGraph initialization.** (1 connections) — `server/tests/unit/utils/test_alias_graph.py`
- *... and 13 more nodes in this community*

## Relationships

- [CommandExecutionRequest](CommandExecutionRequest.md) (5 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (4 shared connections)
- [test magic commands](test_magic_commands.md) (2 shared connections)
- [ContainerDataCore](ContainerDataCore.md) (2 shared connections)
- [test movement service](test_movement_service.md) (2 shared connections)
- [AuthSlice](AuthSlice.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [APIRouter](APIRouter.md) (1 shared connections)
- [Validate an expanded command for](Validate_an_expanded_command_for.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/utils/test_alias_graph.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 114 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*