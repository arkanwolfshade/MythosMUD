# emote_service.py

> 44 nodes

## Key Concepts

- **emote_service.py** (21 connections) — `server/game/emote_service.py`
- **EmoteService** (20 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (16 connections) — `server/tests/unit/game/test_emote_service.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **schemas/validator.py** (7 connections) — `schemas/validator.py`
- **EmoteDefinition** (6 connections) — `server/game/emote_service.py`
- **._async_load_emotes()** (4 connections) — `server/game/emote_service.py`
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **_EmoteLoadResult** (3 connections) — `server/game/emote_service.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **test_format_emote_messages_unknown_raises()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **TypedDict** (3 connections)
- **_EmoteRowData** (2 connections) — `server/game/emote_service.py`
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **test_emote_service_init_loads_via_mock()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_format_emote_messages()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_is_emote_alias_and_get_definition()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_list_available_emotes()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (5 shared connections)
- [SchemaValidator](SchemaValidator.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [command_input.py](command_input.py.md) (3 shared connections)
- [alias_storage.py](alias_storage.py.md) (3 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [handle_emote_command](handle_emote_command.md) (2 shared connections)
- [chat_service.py](chat_service.py.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [validate_room_data](validate_room_data.md) (1 shared connections)
- [RoomLoader](RoomLoader.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/game/emote_service.py`
- `server/tests/unit/game/test_emote_service.py`

## Audit Trail

- EXTRACTED: 94 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*