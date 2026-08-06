# services service hallucination

> 23 nodes

## Key Concepts

- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **TestGetRoomEnvironment** (12 connections) — `server/tests/unit/test_world_loader.py`
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
- **Test get_room_environment() function.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() returns room-specific environment.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() returns subzone environment when room doesn't have o** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() returns zone environment when room and subzone don't** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() returns default 'outdoors' when no environment speci** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() prioritizes room environment over subzone and zone.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() prioritizes subzone environment over zone.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() handles None subzone_config.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() handles None zone_config.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test get_room_environment() treats empty string as no environment.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Determine room environment using inheritance chain.      Priority order:     1.** (1 connections) — `server/world_loader.py`

## Relationships

- [add used user](add_used_user.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 64 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*