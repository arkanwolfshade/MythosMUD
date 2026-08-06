# websocket helpers realtime

> 81 nodes

## Key Concepts

- **SchemaValidator** (28 connections) — `schemas/validator.py`
- **EmoteService** (21 connections) — `server/game/emote_service.py`
- **emote_service.py** (20 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (15 connections) — `server/tests/unit/game/test_emote_service.py`
- **command_input.py** (14 connections) — `server/command_handler/command_input.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **_is_predefined_emote()** (8 connections) — `server/command_handler/command_input.py`
- **schema_validator.py** (8 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections)
- **EmoteDefinition** (7 connections) — `server/game/emote_service.py`
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **.format_emote_messages()** (5 connections) — `server/game/emote_service.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_room_file()** (4 connections) — `schemas/validator.py`
- **.validate_room_database()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- **_AliasValidatorCache** (4 connections) — `server/alias_storage.py`
- **_get_alias_validator()** (4 connections) — `server/alias_storage.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **_EmoteLoadResult** (4 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- *... and 56 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (9 shared connections)
- [add used user](add_used_user.md) (6 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (6 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (4 shared connections)
- [npc idle movement](npc_idle_movement.md) (3 shared connections)
- [player model models](player_model_models.md) (2 shared connections)
- [command validator validators](command_validator_validators.md) (2 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (2 shared connections)
- [chat game message](chat_game_message.md) (2 shared connections)

## Source Files

- `schemas/validator.py`
- `server/alias_storage.py`
- `server/command_handler/command_input.py`
- `server/game/emote_service.py`
- `server/tests/unit/game/test_emote_service.py`
- `tools/room_toolkit/room_validator/core/schema_validator.py`

## Audit Trail

- EXTRACTED: 287 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*