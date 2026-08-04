# commands recovery lucidity

> 85 nodes

## Key Concepts

- **SchemaValidator** (27 connections) — `schemas/validator.py`
- **emote_service.py** (20 connections) — `server/game/emote_service.py`
- **validate_room_data()** (16 connections) — `server/world_loader.py`
- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **TestGetRoomEnvironment** (12 connections) — `server/tests/unit/test_world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **_get_alias_validator()** (8 connections) — `server/alias_storage.py`
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
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **_EmoteLoadResult** (4 connections) — `server/game/emote_service.py`
- **.test_validate_room_data_strict_validation_raises()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_exception_strict()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **Any** (4 connections)
- **._load_schema()** (3 connections) — `schemas/validator.py`
- **Path** (3 connections)
- *... and 60 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (18 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (9 shared connections)
- [schemas validator rationale](schemas_validator_rationale.md) (8 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (6 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (4 shared connections)
- [commands party examples](commands_party_examples.md) (2 shared connections)
- [command commands handler](command_commands_handler.md) (1 shared connections)
- [rate lucidity services](rate_lucidity_services.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [room hierarchical schema](room_hierarchical_schema.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/alias_storage.py`
- `server/game/emote_service.py`
- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`
- `tools/room_toolkit/room_validator/core/schema_validator.py`

## Audit Trail

- EXTRACTED: 278 (93%)
- INFERRED: 20 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*