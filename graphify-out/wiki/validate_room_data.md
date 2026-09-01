# validate_room_data

> 36 nodes

## Key Concepts

- **validate_room_data()** (17 connections) — `server/world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **test_world_loader.py** (11 connections) — `server/tests/unit/test_world_loader.py`
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
- **SchemaValidator** (1 connections)
- **Unit tests for world loader utility functions. Tests room ID generation,…** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() function.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() returns empty list when validation not available.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() with provided validator.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() creates validator when not provided.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() returns validation errors.** (1 connections) — `server/tests/unit/test_world_loader.py`
- *... and 11 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [get_room_environment](get_room_environment.md) (3 shared connections)
- [SchemaValidator](SchemaValidator.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 67 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*