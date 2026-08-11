# React Node Upgrade Summary

> 44 nodes

## Key Concepts

- **validate_room_data()** (16 connections) — `server/world_loader.py`
- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **TestGetRoomEnvironment** (12 connections) — `server/tests/unit/test_world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_strict_validation_raises()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_exception_strict()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **Any** (4 connections)
- **.test_get_room_environment_from_room_data()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_from_subzone()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_from_zone()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_default()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_room_takes_priority()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_subzone_takes_priority_over_zone()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_subzone_none()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_zone_none()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_get_room_environment_empty_string_in_room_data()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_not_available()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_with_validator()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_creates_validator()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_with_errors()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validator_creation_fails()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_exception()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **SchemaValidator** (3 connections)
- **Test get_room_environment() function.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() returns room-specific environment.** (1 connections) — `server/tests/unit/test_world_loader.py`
- *... and 19 more nodes in this community*

## Relationships

- [Spell Registry Costs](Spell_Registry_Costs.md) (7 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (6 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (3 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 124 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*