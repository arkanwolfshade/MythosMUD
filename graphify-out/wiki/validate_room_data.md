# validate_room_data

> 45 nodes

## Key Concepts

- **validate_room_data()** (15 connections) — `server/world_loader.py`
- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **TestGetRoomEnvironment** (12 connections) — `server/tests/unit/test_world_loader.py`
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
- **.test_get_room_environment_default()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_empty_string_in_room_data()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_from_room_data()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_from_subzone()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_from_zone()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_room_takes_priority()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_subzone_none()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_subzone_takes_priority_over_zone()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_zone_none()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **Any** (2 connections)
- **SchemaValidator** (1 connections)
- **Test get_room_environment() treats empty string as no environment.** (1 connections) — `server/tests/unit/test_world_loader.py`
- *... and 20 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [SchemaValidator](SchemaValidator.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 74 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*