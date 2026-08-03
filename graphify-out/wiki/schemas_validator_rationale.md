# schemas validator rationale

> 74 nodes

## Key Concepts

- **SchemaValidator** (27 connections) — `schemas/validator.py`
- **EmoteService** (21 connections) — `server/game/emote_service.py`
- **emote_service.py** (20 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (15 connections) — `server/tests/unit/game/test_emote_service.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
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
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **_EmoteLoadResult** (4 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **._async_load_emotes()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **._load_schema()** (3 connections) — `schemas/validator.py`
- **Path** (3 connections)
- *... and 49 more nodes in this community*

## Relationships

- [commands recovery lucidity](commands_recovery_lucidity.md) (6 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (6 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [commands position system](commands_position_system.md) (3 shared connections)
- [npc rationale extract](npc_rationale_extract.md) (3 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (2 shared connections)
- [chat game message](chat_game_message.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/game/emote_service.py`
- `server/tests/unit/game/test_emote_service.py`
- `tools/room_toolkit/room_validator/core/schema_validator.py`
- `tools/room_toolkit/room_validator/tests/test_schema_validator.py`

## Audit Trail

- EXTRACTED: 257 (94%)
- INFERRED: 15 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*