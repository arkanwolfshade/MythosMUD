# Zone Coordinate Generator

> 29 nodes

## Key Concepts

- **CoordinateGenerator** (20 connections) — `server/services/coordinate_generator.py`
- **Any** (8 connections)
- **._generate_for_subzone()** (8 connections) — `server/services/coordinate_generator.py`
- **._load_rooms_data()** (7 connections) — `server/services/coordinate_generator.py`
- **.generate_coordinates_for_zone()** (6 connections) — `server/services/coordinate_generator.py`
- **._build_adjacency_list()** (5 connections) — `server/services/coordinate_generator.py`
- **._assign_coordinates_bfs()** (5 connections) — `server/services/coordinate_generator.py`
- **._find_origin_room()** (4 connections) — `server/services/coordinate_generator.py`
- **.__init__()** (3 connections) — `server/services/coordinate_generator.py`
- **._rooms_query_and_pattern()** (3 connections) — `server/services/coordinate_generator.py`
- **._room_dict_from_row()** (3 connections) — `server/services/coordinate_generator.py`
- **._attach_room_exits()** (3 connections) — `server/services/coordinate_generator.py`
- **._detect_coordinate_conflicts()** (3 connections) — `server/services/coordinate_generator.py`
- **._get_next_coordinates()** (3 connections) — `server/services/coordinate_generator.py`
- **._reverse_direction()** (3 connections) — `server/services/coordinate_generator.py`
- **._store_coordinates()** (3 connections) — `server/services/coordinate_generator.py`
- **AsyncSession** (1 connections)
- **Generates map coordinates for rooms using hierarchical grouping and directional** (1 connections) — `server/services/coordinate_generator.py`
- **Initialize coordinate generator.          Args:             session: Database se** (1 connections) — `server/services/coordinate_generator.py`
- **Generate coordinates for all rooms in a zone/subzone.          Args:** (1 connections) — `server/services/coordinate_generator.py`
- **Load rooms and their exits from database.          Args:             plane: Plan** (1 connections) — `server/services/coordinate_generator.py`
- **Find the origin room (map_origin_zone=true, or first room).** (1 connections) — `server/services/coordinate_generator.py`
- **Build adjacency list from room exits.** (1 connections) — `server/services/coordinate_generator.py`
- **Assign coordinates using BFS starting from origin.** (1 connections) — `server/services/coordinate_generator.py`
- **Detect conflicts (multiple rooms at same x,y coordinates).** (1 connections) — `server/services/coordinate_generator.py`
- *... and 4 more nodes in this community*

## Relationships

- [Container Persistence Ops](Container_Persistence_Ops.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (1 shared connections)

## Source Files

- `server/services/coordinate_generator.py`

## Audit Trail

- EXTRACTED: 99 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*