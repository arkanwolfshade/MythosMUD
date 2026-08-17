# get_room_service

> 14 nodes

## Key Concepts

- **get_room_service()** (11 connections) — `server/dependencies.py`
- **TestGetRoomService** (5 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetRoomService** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_room_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_room_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_room_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_room_service_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Get a RoomService instance with dependency injection. This function provides a…** (1 connections) — `server/dependencies.py`
- **Tests for get_room_service dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_room_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_room_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_room_service() function.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_room_service() returns room service from container.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_room_service() raises error when service not initialized.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_dependencies.py](test_dependencies.py.md) (2 shared connections)
- [RoomService](RoomService.md) (2 shared connections)
- [get_container](get_container.md) (1 shared connections)
- [Request](Request.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 23 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*