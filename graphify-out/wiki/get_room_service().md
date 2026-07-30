# get room service()

> 32 nodes

## Key Concepts

- **SchemaValidator** (27 connections) — `schemas/validator.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **schema_validator.py** (8 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections)
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_room_file()** (4 connections) — `schemas/validator.py`
- **.validate_room_database()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- **._load_schema()** (3 connections) — `schemas/validator.py`
- **Path** (3 connections)
- **.get_exit_target()** (3 connections) — `schemas/validator.py`
- **.get_exit_flags()** (3 connections) — `schemas/validator.py`
- **.is_room_id_valid()** (2 connections) — `schemas/validator.py`
- **Shared schema validator for room definition files.  This module provides JSON sc** (1 connections) — `schemas/validator.py`
- **Validates room definitions against JSON schema.      This validator can be used** (1 connections) — `schemas/validator.py`
- **Initialize the schema validator.          Args:             schema_path: Path to** (1 connections) — `schemas/validator.py`
- **Load and cache the JSON schema.** (1 connections) — `schemas/validator.py`
- **Validate a JSON document against the loaded schema.          Args:             d** (1 connections) — `schemas/validator.py`
- **Validate a single room against the schema.          Args:             room_data:** (1 connections) — `schemas/validator.py`
- **Validate a room file against the schema.          Args:             file_path: P** (1 connections) — `schemas/validator.py`
- **Validate all rooms in a database against the schema.          Args:** (1 connections) — `schemas/validator.py`
- *... and 7 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (6 shared connections)
- [AuthSlice](AuthSlice.md) (6 shared connections)
- [Any](Any.md) (4 shared connections)
- [Convert legacy string format exits](Convert_legacy_string_format_exits.md) (4 shared connections)
- [PlayerIdCarrier](PlayerIdCarrier.md) (2 shared connections)
- [fixer](fixer.md) (2 shared connections)
- [test alias storage](test_alias_storage.md) (1 shared connections)
- [test hierarchical schema](test_hierarchical_schema.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `tools/room_toolkit/room_validator/core/schema_validator.py`

## Audit Trail

- EXTRACTED: 111 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*