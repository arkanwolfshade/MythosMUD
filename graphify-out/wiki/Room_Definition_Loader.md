# Room Definition Loader

> 93 nodes

## Key Concepts

- **RoomLoader** (56 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **TestRoomLoader** (19 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.load_room_data()** (11 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **TestValidatorEdgeCases** (10 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **Path** (8 connections)
- **._load_referenced_intersections()** (7 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.build_room_database()** (6 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.discover_room_files()** (5 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._validate_or_update_room_id()** (5 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.test_room_with_nonexistent_exit_targets()** (5 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.discover_config_files()** (4 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.test_build_room_database_empty_directory()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_build_room_database_with_errors()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_empty_room_directory()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_room_with_malformed_json()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_room_with_missing_required_fields()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.__init__()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.parse_room_filename()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.generate_room_id()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._validate_room_structure()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._extract_location_from_path()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._validate_required_fields()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._add_location_fields()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._check_intersection_references_rooms()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._add_intersection_to_database()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- *... and 68 more nodes in this community*

## Relationships

- [Room Fixer Toolkit](Room_Fixer_Toolkit.md) (8 shared connections)
- [Logging Path Utilities](Logging_Path_Utilities.md) (7 shared connections)
- [Admin Set Stat Command](Admin_Set_Stat_Command.md) (5 shared connections)
- [Migration Testing Strategy](Migration_Testing_Strategy.md) (2 shared connections)
- [Room Validation Reporter](Room_Validation_Reporter.md) (1 shared connections)
- [Room Schema Validator](Room_Schema_Validator.md) (1 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/room_loader.py`
- `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- `tools/room_toolkit/room_validator/tests/test_validator_integration.py`

## Audit Trail

- EXTRACTED: 233 (80%)
- INFERRED: 57 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*