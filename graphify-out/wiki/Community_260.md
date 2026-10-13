# Community 260

> 61 nodes

## Key Concepts

- **CoordinateGenerator** (31 connections) — `server/services/coordinate_generator.py`
- **test_coordinate_generator.py** (23 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **._generate_for_subzone()** (8 connections) — `server/services/coordinate_generator.py`
- **Any** (8 connections)
- **._load_rooms_data()** (7 connections) — `server/services/coordinate_generator.py`
- **.generate_coordinates_for_zone()** (6 connections) — `server/services/coordinate_generator.py`
- **asyncio** (6 connections)
- **._build_adjacency_list()** (5 connections) — `server/services/coordinate_generator.py`
- **._assign_coordinates_bfs()** (4 connections) — `server/services/coordinate_generator.py`
- **._find_origin_room()** (4 connections) — `server/services/coordinate_generator.py`
- **._rooms_query_and_pattern()** (4 connections) — `server/services/coordinate_generator.py`
- **._attach_room_exits()** (3 connections) — `server/services/coordinate_generator.py`
- **._detect_coordinate_conflicts()** (3 connections) — `server/services/coordinate_generator.py`
- **._get_next_coordinates()** (3 connections) — `server/services/coordinate_generator.py`
- **.__init__()** (3 connections) — `server/services/coordinate_generator.py`
- **._reverse_direction()** (3 connections) — `server/services/coordinate_generator.py`
- **._room_dict_from_row()** (3 connections) — `server/services/coordinate_generator.py`
- **._store_coordinates()** (3 connections) — `server/services/coordinate_generator.py`
- **generator()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_assign_coordinates_bfs_displaces_up_down_exits()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_assign_coordinates_bfs_reaches_disconnected_components()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_assign_coordinates_bfs_resolves_collisions()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_room_dict_from_row_carries_environment_columns()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_room_dict_from_row_inherited_environment_is_none()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_store_coordinates_noop_on_empty()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- *... and 36 more nodes in this community*

## Relationships

- [Map & Admin Responses](Map_&_Admin_Responses.md) (4 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)

## Source Files

- `server/services/coordinate_generator.py`
- `server/tests/unit/services/test_coordinate_generator.py`

## Audit Trail

- EXTRACTED: 94 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*