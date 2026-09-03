# Test Room Service

> 11 nodes

## Key Concepts

- **room_service()** (5 connections) — `server/tests/unit/game/test_room_service.py`
- **fixture** (5 connections)
- **room_service_with_cache()** (4 connections) — `server/tests/unit/game/test_room_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **mock_room_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **sample_room_dict()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Create a mock room cache service.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Create a RoomService instance.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Create a RoomService instance with cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Create a sample room dictionary.** (1 connections) — `server/tests/unit/game/test_room_service.py`

## Relationships

- [Test Room Service](Test_Room_Service.md) (5 shared connections)
- [Room Service](Room_Service.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 15 (83%)
- INFERRED: 3 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*