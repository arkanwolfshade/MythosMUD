# test_passive_corruption_flux_rate_overrides.py

> 54 nodes · cohesion 0.06

## Key Concepts

- **AliasGraph** (22 connections) — `server/utils/alias_graph.py`
- **alias_expansion.py** (19 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_expansion.py** (17 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_graph.py** (11 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **alias_graph.py** (9 connections) — `server/utils/alias_graph.py`
- **asyncio** (5 connections)
- **asyncio** (5 connections)
- **test_alias_graph_build_graph()** (5 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_clear()** (5 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_detect_cycle_no_cycle()** (5 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_get_expansion_depth()** (5 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_alias_graph_is_safe_to_expand()** (5 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_check_alias_safety_cycle_detected()** (4 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_depth_too_deep()** (4 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_ok()** (4 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_depth_limit()** (4 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_alias_graph_init()** (4 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **test_handle_expanded_command_delegates()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **.build_graph()** (3 connections) — `server/utils/alias_graph.py`
- **.detect_cycle()** (3 connections) — `server/utils/alias_graph.py`
- **._extract_alias_references()** (3 connections) — `server/utils/alias_graph.py`
- **.__init__()** (3 connections) — `server/utils/alias_graph.py`
- *... and 29 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (13 shared connections)
- [look_container.py](look_container.py.md) (5 shared connections)
- [Room](Room.md) (5 shared connections)
- [QuestService](QuestService.md) (5 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (4 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (3 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (2 shared connections)
- [test_logging_file_categories.py](test_logging_file_categories.py.md) (1 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`
- `server/tests/unit/utils/test_alias_graph.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 112 (88%)
- INFERRED: 15 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*