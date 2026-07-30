# AuthSlice

> 60 nodes

## Key Concepts

- **validate_room_data()** (16 connections) — `server/world_loader.py`
- **world_loader.py** (14 connections) — `server/world_loader.py`
- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **TestGetRoomEnvironment** (12 connections) — `server/tests/unit/test_world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **test_world_loader.py** (10 connections) — `server/tests/unit/test_world_loader.py`
- **generate_room_id()** (9 connections) — `server/world_loader.py`
- **TestGenerateRoomId** (7 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_strict_validation_raises()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **.test_validate_room_data_validation_exception_strict()** (4 connections) — `server/tests/unit/test_world_loader.py`
- **Any** (4 connections)
- **.test_generate_room_id_basic()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_with_underscores()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_empty_components()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_special_characters()** (3 connections) — `server/tests/unit/test_world_loader.py`
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
- *... and 35 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (10 shared connections)
- [get room service()](get_room_service%28%29.md) (6 shared connections)
- [world](world.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (2 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 183 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*