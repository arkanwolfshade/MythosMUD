# SchemaValidator

> 84 nodes · cohesion 0.03

## Key Concepts

- **SchemaValidator** (29 connections) — `schemas/validator.py`
- **emote_service.py** (19 connections) — `server/game/emote_service.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **.get_player_aliases()** (8 connections) — `server/alias_storage.py`
- **_get_alias_validator()** (8 connections) — `server/alias_storage.py`
- **schema_validator.py** (8 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections)
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **._get_alias_file_path()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **._load_alias_data()** (6 connections) — `server/alias_storage.py`
- **._save_alias_data()** (6 connections) — `server/alias_storage.py`
- **Path** (5 connections)
- **EmoteDefinition** (5 connections) — `server/game/emote_service.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- **.validate_room_database()** (4 connections) — `schemas/validator.py`
- **.validate_room_file()** (4 connections) — `schemas/validator.py`
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- *... and 59 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (22 shared connections)
- [validate_room_data](validate_room_data.md) (6 shared connections)
- [Alias](Alias.md) (5 shared connections)
- [EmoteService](EmoteService.md) (4 shared connections)
- [SchemaValidator](SchemaValidator.md) (4 shared connections)
- [test_alias_storage.py](test_alias_storage.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [get_asyncpg_server_settings_for_database_url](get_asyncpg_server_settings_for_database_url.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [PathValidator](PathValidator.md) (2 shared connections)
- [command_input.py](command_input.py.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/alias_storage.py`
- `server/game/emote_service.py`
- `server/tests/unit/test_alias_storage.py`
- `tools/room_toolkit/room_validator/core/schema_validator.py`

## Audit Trail

- EXTRACTED: 277 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*