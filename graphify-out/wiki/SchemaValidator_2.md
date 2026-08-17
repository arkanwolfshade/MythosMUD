# SchemaValidator

> 26 nodes

## Key Concepts

- **SchemaValidator** (21 connections) — `schemas/validator.py`
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
- **Validate a room file against the schema. Args: file_path: Path to the room JSON…** (1 connections) — `schemas/validator.py`
- **Validate all rooms in a database against the schema. Args: room_database:…** (1 connections) — `schemas/validator.py`
- **Validate a serialized alias bundle against the alias schema. Args: alias_data:…** (1 connections) — `schemas/validator.py`
- **Validate emote definition data against the emote schema. Args: emote_data:…** (1 connections) — `schemas/validator.py`
- **Extract target room ID from exit data, handling both formats. Args: exit_data:…** (1 connections) — `schemas/validator.py`
- **Extract flags from exit data, handling both formats. Args: exit_data: Exit data…** (1 connections) — `schemas/validator.py`
- **Check if a room ID follows the unified naming schema. Args: room_id: Room ID to…** (1 connections) — `schemas/validator.py`
- **Validates room definitions against JSON schema. This validator can be used by…** (1 connections) — `schemas/validator.py`
- **Initialize the schema validator. Args: schema_path: Path to the JSON schema…** (1 connections) — `schemas/validator.py`
- **Load and cache the JSON schema.** (1 connections) — `schemas/validator.py`
- **Validate a JSON document against the loaded schema. Args: data: Data to…** (1 connections) — `schemas/validator.py`
- *... and 1 more nodes in this community*

## Relationships

- [emote_service.py](emote_service.py.md) (4 shared connections)
- [alias_storage.py](alias_storage.py.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [RoomLoader](RoomLoader.md) (1 shared connections)
- [validate_room_data](validate_room_data.md) (1 shared connections)
- [SchemaValidator](SchemaValidator.md) (1 shared connections)

## Source Files

- `schemas/validator.py`

## Audit Trail

- EXTRACTED: 45 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*