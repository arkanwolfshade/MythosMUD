# Room Definition Loader

> 80 nodes · cohesion 0.04

## Key Concepts

- **RoomLoader** (51 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **TestRoomLoader** (19 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **Path** (16 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.load_room_data()** (11 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._load_referenced_intersections()** (7 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.build_room_database()** (6 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.discover_room_files()** (5 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._validate_or_update_room_id()** (5 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.discover_config_files()** (4 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.test_build_room_database_with_errors()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_init_with_custom_path()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_init_with_default_path()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_load_room_data_invalid_json()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_load_room_data_missing_required_fields()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_load_room_data_not_dict()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_load_room_data_valid()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **._add_intersection_to_database()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._add_location_fields()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._check_intersection_references_rooms()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.count_config_subzones()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._extract_location_from_path()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.generate_room_id()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.__init__()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.load_config_file()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.parse_room_filename()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- *... and 55 more nodes in this community*

## Relationships

- [[Room Fixer Toolkit]] (9 shared connections)
- [[Room Validator Toolkit]] (3 shared connections)
- [[Room File Fixer]] (1 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/room_loader.py`
- `tools/room_toolkit/room_validator/tests/test_room_loader.py`

## Audit Trail

- EXTRACTED: 254 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
