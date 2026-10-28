# logger.ts

> 98 nodes · cohesion 0.03

## Key Concepts

- **RoomLoader** (58 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **TestRoomLoader** (19 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **temp_dir()** (12 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **.load_room_data()** (11 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **Path** (8 connections)
- **TestValidatorEdgeCases** (8 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **._load_referenced_intersections()** (7 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.build_room_database()** (6 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.discover_room_files()** (5 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._validate_or_update_room_id()** (5 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.test_room_with_nonexistent_exit_targets()** (5 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.discover_config_files()** (4 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.load_config_file()** (4 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._validate_required_fields()** (4 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._validate_room_structure()** (4 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **test_room_loader.py** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_build_room_database_empty_directory()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_build_room_database_with_errors()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **.test_empty_room_directory()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_room_with_malformed_json()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_room_with_missing_required_fields()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **._add_intersection_to_database()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._add_location_fields()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **._check_intersection_references_rooms()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.count_config_subzones()** (3 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- *... and 73 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (13 shared connections)
- [Mypy Remediation](Mypy_Remediation.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (3 shared connections)
- [test_status_commands.py](test_status_commands.py.md) (2 shared connections)
- [SessionManager](SessionManager.md) (1 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_logging_utilities.py`
- `tools/room_toolkit/room_validator/core/room_loader.py`
- `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- `tools/room_toolkit/room_validator/tests/test_validator_integration.py`

## Audit Trail

- EXTRACTED: 148 (89%)
- INFERRED: 19 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*