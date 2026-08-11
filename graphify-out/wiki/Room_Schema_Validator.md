# Room Schema Validator

> 83 nodes

## Key Concepts

- **SchemaValidator** (51 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **TestSchemaValidator** (28 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
- **.validate()** (6 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.validate_room()** (5 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **Path** (5 connections)
- **.__init__()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.validate_room_file()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.get_exit_flags()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.validate_subzone_config()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.validate_zone_config()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **._load_schema()** (3 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.validate_room_database()** (3 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.is_one_way_exit()** (3 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.is_self_reference_exit()** (3 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **test_schema_validator.py** (3 connections) — `tools/room_toolkit/room_validator/tests/test_schema_validator.py`
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
- *... and 58 more nodes in this community*

## Relationships

- [Async Persistence Types](Async_Persistence_Types.md) (4 shared connections)
- [Admin Set Stat Command](Admin_Set_Stat_Command.md) (4 shared connections)
- [Hierarchical Schema Tests](Hierarchical_Schema_Tests.md) (3 shared connections)
- [Inventory Command Factories](Inventory_Command_Factories.md) (2 shared connections)
- [Room Fixer Toolkit](Room_Fixer_Toolkit.md) (1 shared connections)
- [Room Definition Loader](Room_Definition_Loader.md) (1 shared connections)
- [Migration Testing Strategy](Migration_Testing_Strategy.md) (1 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/schema_validator.py`
- `tools/room_toolkit/room_validator/rules/base_rule.py`
- `tools/room_toolkit/room_validator/tests/test_schema_validator.py`

## Audit Trail

- EXTRACTED: 181 (72%)
- INFERRED: 69 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*