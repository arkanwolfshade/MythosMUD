# alias graph rationale

> 30 nodes

## Key Concepts

- **AliasGraph** (18 connections) — `server/utils/alias_graph.py`
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
- **.get_expansion_depth()** (2 connections) — `server/utils/alias_graph.py`
- **.clear()** (2 connections) — `server/utils/alias_graph.py`
- **Unit tests for alias_graph utilities.  Tests the AliasGraph class.** (1 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **Test AliasGraph initialization.** (1 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **Test AliasGraph.build_graph() builds dependency graph.** (1 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **Test AliasGraph.detect_cycle() returns None when no cycle.** (1 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **Test AliasGraph.is_safe_to_expand() returns True when safe.** (1 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **Test AliasGraph.get_expansion_depth() returns depth.** (1 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **Test AliasGraph.clear() clears the graph.** (1 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **Graph-based circular dependency detection for alias expansion.      Uses depth-f** (1 connections) — `server/utils/alias_graph.py`
- **Initialize alias graph analyzer.          Args:             alias_storage: Stora** (1 connections) — `server/utils/alias_graph.py`
- **Build dependency graph for a player's aliases.          Creates a directed graph** (1 connections) — `server/utils/alias_graph.py`
- *... and 5 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [command commands handler](command_commands_handler.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_alias_graph.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*