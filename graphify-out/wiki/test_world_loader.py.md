# test_world_loader.py

> 16 nodes

## Key Concepts

- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **test_world_loader.py** (11 connections) — `server/tests/unit/test_world_loader.py`
- **generate_room_id()** (9 connections) — `server/world_loader.py`
- **TestGenerateRoomId** (6 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_basic()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_empty_components()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_special_characters()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_with_underscores()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **Unit tests for world loader utility functions. Tests room ID generation,…** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test validate_room_data() function.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() function.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() with basic components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() handles components with underscores.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() with empty components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() preserves special characters in components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Generate hierarchical room ID from components. Args: plane: Plane identifier…** (1 connections) — `server/world_loader.py`

## Relationships

- [validate_room_data](validate_room_data.md) (9 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [get_room_environment](get_room_environment.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 37 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*