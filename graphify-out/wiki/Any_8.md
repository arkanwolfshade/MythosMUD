# Any

> 22 nodes

## Key Concepts

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
- **Validate a room file against the schema. Args: file_path: Path to the room JSON…** (1 connections) — `schemas/validator.py`
- **Validate all rooms in a database against the schema. Args: room_database:…** (1 connections) — `schemas/validator.py`
- **Validate a serialized alias bundle against the alias schema. Args: alias_data:…** (1 connections) — `schemas/validator.py`
- **Validate emote definition data against the emote schema. Args: emote_data:…** (1 connections) — `schemas/validator.py`
- **Extract target room ID from exit data, handling both formats. Args: exit_data:…** (1 connections) — `schemas/validator.py`
- **Extract flags from exit data, handling both formats. Args: exit_data: Exit data…** (1 connections) — `schemas/validator.py`
- **Initialize the schema validator. Args: schema_path: Path to the JSON schema…** (1 connections) — `schemas/validator.py`
- **Load and cache the JSON schema.** (1 connections) — `schemas/validator.py`
- **Validate a JSON document against the loaded schema. Args: data: Data to…** (1 connections) — `schemas/validator.py`
- **Validate a single room against the schema. Args: room_data: Room data to…** (1 connections) — `schemas/validator.py`

## Relationships

- [get_logger](get_logger.md) (11 shared connections)

## Source Files

- `schemas/validator.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*