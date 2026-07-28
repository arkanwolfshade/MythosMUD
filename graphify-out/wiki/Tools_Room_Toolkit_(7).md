# Tools Room Toolkit (7)

> 36 nodes

## Key Concepts

- **PathValidator** (25 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **TestValidatorComponents** (11 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.check_bidirectional_connections()** (6 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.test_full_validation_pipeline()** (6 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.build_graph()** (5 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._get_exit_target()** (5 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.test_path_validator_integration()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **._is_one_way_exit()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._get_room_zone()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._get_opposite_direction()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.find_dead_ends()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.find_self_references()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.generate_minimap_graph()** (3 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.test_room_loader_integration()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_schema_validator_integration()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_reporter_integration()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.__init__()** (2 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.find_unreachable_rooms()** (2 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Validates room connectivity using graph traversal algorithms.      Implements th** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Initialize the path validator.          Args:             schema_validator: Opti** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Build adjacency graph from room database.          Args:             room_databa** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Get target room ID from exit data.** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Check if exit is marked as one-way.** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Extract zone and sub_zone from room data.          Args:             room_id: Ro** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **Check for bidirectional connections between rooms, accounting for zone transitio** (1 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- *... and 11 more nodes in this community*

## Relationships

- [Tools Room Toolkit (6)](Tools_Room_Toolkit_%286%29.md) (5 shared connections)
- [Tools Room Toolkit](Tools_Room_Toolkit.md) (5 shared connections)
- [Tools Room Toolkit (3)](Tools_Room_Toolkit_%283%29.md) (4 shared connections)
- [Tools Room Toolkit (2)](Tools_Room_Toolkit_%282%29.md) (3 shared connections)
- [Tools Room Toolkit (11)](Tools_Room_Toolkit_%2811%29.md) (2 shared connections)
- [Tools Room Toolkit (13)](Tools_Room_Toolkit_%2813%29.md) (2 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/path_validator.py`
- `tools/room_toolkit/room_validator/tests/test_validator_integration.py`

## Audit Trail

- EXTRACTED: 90 (81%)
- INFERRED: 21 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*