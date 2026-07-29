# Convert legacy string format exits

> 58 nodes

## Key Concepts

- **SchemaValidator** (51 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **TestSchemaValidator** (28 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.get_exit_flags()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **Test getting exit target from string format.** (4 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.is_one_way_exit()** (3 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.is_self_reference_exit()** (3 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.test_init_with_default_schema()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_init_with_custom_schema()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_init_schema_file_not_found()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_init_invalid_schema_file()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_validate_room_valid()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_validate_room_missing_required_field()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_validate_room_invalid_id_format()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_validate_room_empty_name()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_validate_room_with_file_path()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_normalize_exits_legacy_format()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_normalize_exits_new_format()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_validate_room_file_valid()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_validate_room_file_invalid_json()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_validate_room_database()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_validate_room_database_with_errors()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_get_exit_target_string_format()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_get_exit_target_object_format()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_get_exit_target_invalid_format()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.test_get_exit_flags_string_format()** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- *... and 33 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (7 shared connections)
- [PathValidator](PathValidator.md) (4 shared connections)
- [fixer](fixer.md) (3 shared connections)
- [test hierarchical schema](test_hierarchical_schema.md) (3 shared connections)
- [Any](Any.md) (1 shared connections)
- [Create a temporary directory for](Create_a_temporary_directory_for.md) (1 shared connections)
- [Integration tests for the main](Integration_tests_for_the_main.md) (1 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/schema_validator.py`
- `tools/room_toolkit/room_validator/tests/test_schema_validator.py`

## Audit Trail

- EXTRACTED: 138 (69%)
- INFERRED: 62 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*