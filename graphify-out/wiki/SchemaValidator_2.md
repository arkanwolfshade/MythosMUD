# SchemaValidator

> 30 nodes

## Key Concepts

- **SchemaValidator** (21 connections) — `schemas/validator.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **schemas/validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections)
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- **.validate_room_database()** (4 connections) — `schemas/validator.py`
- **.validate_room_file()** (4 connections) — `schemas/validator.py`
- **.get_exit_flags()** (3 connections) — `schemas/validator.py`
- **.get_exit_target()** (3 connections) — `schemas/validator.py`
- **._load_schema()** (3 connections) — `schemas/validator.py`
- **Path** (3 connections)
- **.is_room_id_valid()** (2 connections) — `schemas/validator.py`
- **Shared schema validator for room definition files. This module provides JSON…** (1 connections) — `schemas/validator.py`
- **Validate a room file against the schema. Args: file_path: Path to the room JSON…** (1 connections) — `schemas/validator.py`
- **Validate all rooms in a database against the schema. Args: room_database:…** (1 connections) — `schemas/validator.py`
- **Validate a serialized alias bundle against the alias schema. Args: alias_data:…** (1 connections) — `schemas/validator.py`
- **Validate emote definition data against the emote schema. Args: emote_data:…** (1 connections) — `schemas/validator.py`
- **Extract target room ID from exit data, handling both formats. Args: exit_data:…** (1 connections) — `schemas/validator.py`
- **Extract flags from exit data, handling both formats. Args: exit_data: Exit data…** (1 connections) — `schemas/validator.py`
- **Check if a room ID follows the unified naming schema. Args: room_id: Room ID to…** (1 connections) — `schemas/validator.py`
- **Create a schema validator with the specified schema. Args: schema_name: Name of…** (1 connections) — `schemas/validator.py`
- *... and 5 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (5 shared connections)
- [EmoteService](EmoteService.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [RoomLoader](RoomLoader.md) (2 shared connections)
- [validate_room_data](validate_room_data.md) (2 shared connections)
- [SchemaValidator](SchemaValidator.md) (1 shared connections)

## Source Files

- `schemas/validator.py`

## Audit Trail

- EXTRACTED: 58 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*