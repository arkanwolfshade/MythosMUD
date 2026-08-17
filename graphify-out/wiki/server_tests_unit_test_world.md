# server tests unit test world

> 22 nodes

## Key Concepts

- **validate_room_data()** (17 connections) — `server/world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
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

- [server tests unit test world](server_tests_unit_test_world.md) (3 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (2 shared connections)
- [schemas validator](schemas_validator.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 41 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*