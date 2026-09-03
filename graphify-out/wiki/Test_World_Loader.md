# Test World Loader

> 12 nodes

## Key Concepts

- **generate_room_id()** (7 connections) — `server/world_loader.py`
- **TestGenerateRoomId** (6 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_basic()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_empty_components()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_special_characters()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_with_underscores()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() function.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() with basic components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() handles components with underscores.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() with empty components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() preserves special characters in components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Generate hierarchical room ID from components. Args: plane: Plane identifier…** (1 connections) — `server/world_loader.py`

## Relationships

- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*