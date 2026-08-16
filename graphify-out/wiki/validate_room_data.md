# validate_room_data

> 24 nodes

## Key Concepts

- **validate_room_data()** (17 connections) — `server/world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **patch** (8 connections)
- **.test_validate_room_data_creates_validator()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_strict_validation_raises()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_exception()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_exception_strict()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_not_available()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validator_creation_fails()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_with_errors()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_with_validator()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **SchemaValidator** (1 connections)
- **Create a schema validator with the specified schema. Args: schema_name: Name of…** (1 connections) — `schemas/validator.py`
- **Test validate_room_data() function.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() returns empty list when validation not available.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() with provided validator.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() creates validator when not provided.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() returns validation errors.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() raises exception in strict mode with errors.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() returns empty list when validator creation fails.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() handles validation exception.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() raises in strict mode when validation exception…** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Validate room data against schema if validation is available. Args: room_data:…** (1 connections) — `server/world_loader.py`

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [SchemaValidator](SchemaValidator.md) (4 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [EmoteService](EmoteService.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (1 shared connections)
- [get_room_environment](get_room_environment.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 50 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*