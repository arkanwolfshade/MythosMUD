# server tests unit test world

> 36 nodes

## Key Concepts

- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **TestGetRoomEnvironment** (11 connections) — `server/tests/unit/test_world_loader.py`
- **test_world_loader.py** (11 connections) — `server/tests/unit/test_world_loader.py`
- **generate_room_id()** (9 connections) — `server/world_loader.py`
- **TestGenerateRoomId** (6 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_basic()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_empty_components()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_special_characters()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_with_underscores()** (3 connections) — `server/tests/unit/test_world_loader.py`
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
- **Test get_room_environment() returns subzone environment when room doesn't have…** (2 connections) — `server/tests/unit/test_world_loader.py`
- **Unit tests for world loader utility functions. Tests room ID generation,…** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() treats empty string as no environment.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() function.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() with basic components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() handles components with underscores.** (1 connections) — `server/tests/unit/test_world_loader.py`
- *... and 11 more nodes in this community*

## Relationships

- [schemas validator](schemas_validator.md) (3 shared connections)
- [server tests unit test world](server_tests_unit_test_world.md) (3 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [server async persistence room loader](server_async_persistence_room_loader.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*