# AliasGraph

> 53 nodes

## Key Concepts

- **AliasGraph** (18 connections) — `server/utils/alias_graph.py`
- **alias_expansion.py** (17 connections) — `server/command_handler/alias_expansion.py`
- **command_handler/__init__.py** (14 connections) — `server/command_handler/__init__.py`
- **test_alias_expansion.py** (14 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_graph.py** (9 connections) — `server/tests/unit/utils/test_alias_graph.py`
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
- *... and 28 more nodes in this community*

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (11 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [processing.py](processing.py.md) (4 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (1 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`
- `server/tests/unit/utils/test_alias_graph.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 110 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*