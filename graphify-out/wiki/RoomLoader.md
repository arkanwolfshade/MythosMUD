# RoomLoader

> 116 nodes

## Key Concepts

- **RoomLoader** (58 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **PathValidator** (27 connections) — `tools/room_toolkit/room_validator/core/path_validator.py`
- **room_validator/validator.py** (22 connections) — `tools/room_toolkit/room_validator/validator.py`
- **RoomFixer** (20 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **TestRoomLoader** (19 connections) — `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- **main()** (19 connections) — `tools/room_toolkit/room_validator/validator.py`
- **temp_dir()** (12 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **TestValidatorComponents** (11 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **core/__init__.py** (11 connections) — `tools/room_toolkit/room_validator/core/__init__.py`
- **_initialize_validator_components()** (9 connections) — `tools/room_toolkit/room_validator/validator.py`
- **test_validator_integration.py** (9 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **TestValidatorEdgeCases** (8 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **schema_validator.py** (8 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **_validate_config_files()** (7 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_validate_room_connectivity()** (7 connections) — `tools/room_toolkit/room_validator/validator.py`
- **Any** (7 connections)
- **.test_full_validation_pipeline()** (6 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **_apply_automatic_fixes()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_generate_minimap()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_load_and_filter_rooms()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **_report_results()** (6 connections) — `tools/room_toolkit/room_validator/validator.py`
- **reporter.py** (6 connections) — `tools/room_toolkit/room_validator/core/reporter.py`
- **room_loader.py** (6 connections) — `tools/room_toolkit/room_validator/core/room_loader.py`
- **.test_room_with_nonexistent_exit_targets()** (5 connections) — `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- **_collect_parsing_errors()** (5 connections) — `tools/room_toolkit/room_validator/validator.py`
- *... and 91 more nodes in this community*

## Relationships

- [.load_room_data](load_room_data.md) (18 shared connections)
- [Path](Path.md) (13 shared connections)
- [Reporter](Reporter.md) (12 shared connections)
- [SchemaValidator](SchemaValidator.md) (12 shared connections)
- [.check_bidirectional_connections](check_bidirectional_connections.md) (9 shared connections)
- [TestValidatorIntegration](TestValidatorIntegration.md) (7 shared connections)
- [TestPathValidator](TestPathValidator.md) (3 shared connections)
- [MinimapRenderer](MinimapRenderer.md) (3 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (2 shared connections)
- [room_validator/tests/conftest.py](room_validator-tests-conftest.py.md) (1 shared connections)
- [alias_schema.json](alias_schema.json.md) (1 shared connections)

## Source Files

- `.claude/rules/click.md`
- `server/tests/unit/structured_logging/test_logging_utilities.py`
- `tools/room_toolkit/room_validator/core/__init__.py`
- `tools/room_toolkit/room_validator/core/fixer.py`
- `tools/room_toolkit/room_validator/core/path_validator.py`
- `tools/room_toolkit/room_validator/core/reporter.py`
- `tools/room_toolkit/room_validator/core/room_loader.py`
- `tools/room_toolkit/room_validator/core/schema_validator.py`
- `tools/room_toolkit/room_validator/tests/test_room_loader.py`
- `tools/room_toolkit/room_validator/tests/test_validator_integration.py`
- `tools/room_toolkit/room_validator/validator.py`

## Audit Trail

- EXTRACTED: 237 (86%)
- INFERRED: 40 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*