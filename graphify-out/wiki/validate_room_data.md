# validate_room_data

> 63 nodes

## Key Concepts

- **validate_room_data()** (17 connections) — `server/world_loader.py`
- **world_loader.py** (14 connections) — `server/world_loader.py`
- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **TestGetRoomEnvironment** (11 connections) — `server/tests/unit/test_world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **test_world_loader.py** (11 connections) — `server/tests/unit/test_world_loader.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **generate_room_id()** (9 connections) — `server/world_loader.py`
- **patch** (8 connections)
- **TestGenerateRoomId** (6 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_creates_validator()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_strict_validation_raises()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_exception()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_exception_strict()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_not_available()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validator_creation_fails()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_with_errors()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_with_validator()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_basic()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_empty_components()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_special_characters()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_with_underscores()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_default()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_empty_string_in_room_data()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_from_room_data()** (3 connections) — `server/tests/unit/test_world_loader.py`
- *... and 38 more nodes in this community*

## Relationships

- [SchemaValidator](SchemaValidator.md) (6 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [EmoteService](EmoteService.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 116 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*