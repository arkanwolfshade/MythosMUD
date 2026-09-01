# SchemaValidator

> 71 nodes

## Key Concepts

- **SchemaValidator** (21 connections) — `schemas/validator.py`
- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (18 connections) — `server/tests/unit/game/test_emote_service.py`
- **emote_service.py** (16 connections) — `server/game/emote_service.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **schemas/validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections)
- **EmoteDefinition** (6 connections) — `server/game/emote_service.py`
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- **.validate_room_database()** (4 connections) — `schemas/validator.py`
- **.validate_room_file()** (4 connections) — `schemas/validator.py`
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **test_load_emotes_handles_missing_table_gracefully()** (4 connections) — `server/tests/unit/game/test_emote_service.py`
- **.get_exit_flags()** (3 connections) — `schemas/validator.py`
- **.get_exit_target()** (3 connections) — `schemas/validator.py`
- **._load_schema()** (3 connections) — `schemas/validator.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.load_emotes()** (3 connections) — `server/game/emote_service.py`
- *... and 46 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [alias_storage.py](alias_storage.py.md) (5 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [RoomLoader](RoomLoader.md) (2 shared connections)
- [validate_room_data](validate_room_data.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [SchemaValidator](SchemaValidator.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/game/emote_service.py`
- `server/tests/unit/game/test_emote_service.py`

## Audit Trail

- EXTRACTED: 132 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*