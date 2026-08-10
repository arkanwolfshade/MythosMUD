# Admin Set Stat Command

> 48 nodes

## Key Concepts

- **PathValidator** (25 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **TestValidatorComponents** (11 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **TestValidatorEdgeCases** (10 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.check_bidirectional_connections()** (6 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.test_full_validation_pipeline()** (6 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.build_graph()** (5 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **._get_exit_target()** (5 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **.test_room_with_nonexistent_exit_targets()** (5 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **test_validator_integration.py** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_path_validator_integration()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_empty_room_directory()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_room_with_malformed_json()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **.test_room_with_missing_required_fields()** (4 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
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
- *... and 23 more nodes in this community*

## Relationships

- [Room Definition Loader](Room_Definition_Loader.md) (8 shared connections)
- [Room Fixer Toolkit](Room_Fixer_Toolkit.md) (5 shared connections)
- [Room Schema Validator](Room_Schema_Validator.md) (5 shared connections)
- [Room Validation Reporter](Room_Validation_Reporter.md) (4 shared connections)
- [Logging Path Utilities](Logging_Path_Utilities.md) (4 shared connections)
- [Legacy Cleanup Summary](Legacy_Cleanup_Summary.md) (2 shared connections)
- [Migration Testing Strategy](Migration_Testing_Strategy.md) (2 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/path_validator.py`
- `tools/room_toolkit/room_validator/tests/test_validator_integration.py`

## Audit Trail

- EXTRACTED: 114 (77%)
- INFERRED: 34 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*