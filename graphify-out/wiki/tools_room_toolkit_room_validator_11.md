# tools room toolkit room validator

> 18 nodes

## Key Concepts

- **.check_bidirectional_connections()** (6 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.build_graph()** (5 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._get_exit_target()** (5 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.find_dead_ends()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.find_self_references()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.generate_minimap_graph()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._get_opposite_direction()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._get_room_zone()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._is_one_way_exit()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Get the opposite direction for bidirectional checking.** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Find rooms with no exits (dead ends). Args: room_database: Dictionary mapping…** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Find rooms that reference themselves in exits. Args: room_database: Dictionary…** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Generate minimap graph data for visualization. Args: room_database: Dictionary…** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Build adjacency graph from room database. Args: room_database: Dictionary…** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Get target room ID from exit data.** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Check if exit is marked as one-way.** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Extract zone and sub_zone from room data. Args: room_id: Room identifier…** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Check for bidirectional connections between rooms, accounting for zone…** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`

## Relationships

- [claude rules click](claude_rules_click.md) (9 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/path_validator.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*