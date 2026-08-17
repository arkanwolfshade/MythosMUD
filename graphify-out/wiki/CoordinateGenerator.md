# CoordinateGenerator

> 47 nodes

## Key Concepts

- **CoordinateGenerator** (24 connections) — `server/services/coordinate_generator.py`
- **test_coordinate_generator.py** (18 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **._generate_for_subzone()** (8 connections) — `server/services/coordinate_generator.py`
- **Any** (8 connections)
- **._load_rooms_data()** (7 connections) — `server/services/coordinate_generator.py`
- **.generate_coordinates_for_zone()** (6 connections) — `server/services/coordinate_generator.py`
- **._assign_coordinates_bfs()** (5 connections) — `server/services/coordinate_generator.py`
- **._build_adjacency_list()** (5 connections) — `server/services/coordinate_generator.py`
- **asyncio** (5 connections)
- **._find_origin_room()** (4 connections) — `server/services/coordinate_generator.py`
- **._attach_room_exits()** (3 connections) — `server/services/coordinate_generator.py`
- **._detect_coordinate_conflicts()** (3 connections) — `server/services/coordinate_generator.py`
- **._get_next_coordinates()** (3 connections) — `server/services/coordinate_generator.py`
- **.__init__()** (3 connections) — `server/services/coordinate_generator.py`
- **._reverse_direction()** (3 connections) — `server/services/coordinate_generator.py`
- **._room_dict_from_row()** (3 connections) — `server/services/coordinate_generator.py`
- **._rooms_query_and_pattern()** (3 connections) — `server/services/coordinate_generator.py`
- **._store_coordinates()** (3 connections) — `server/services/coordinate_generator.py`
- **generator()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_store_coordinates_noop_on_empty()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_store_coordinates_persists_values()** (3 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_generate_coordinates_for_zone_empty_data()** (2 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_generate_coordinates_for_zone_stores_results()** (2 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_generate_for_subzone_positions_linked_rooms()** (2 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- **test_assign_coordinates_bfs()** (1 connections) — `server/tests/unit/services/test_coordinate_generator.py`
- *... and 22 more nodes in this community*

## Relationships

- [ExplorationService](ExplorationService.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [deque](deque.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/coordinate_generator.py`
- `server/tests/unit/services/test_coordinate_generator.py`

## Audit Trail

- EXTRACTED: 76 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*