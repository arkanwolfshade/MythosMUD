# server tests unit test world

> 14 nodes

## Key Concepts

- **test_world_loader.py** (11 connections) — `server/tests/unit/test_world_loader.py`
- **generate_room_id()** (9 connections) — `server/world_loader.py`
- **TestGenerateRoomId** (6 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_basic()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_empty_components()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_special_characters()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **.test_generate_room_id_with_underscores()** (3 connections) — `server/tests/unit/test_world_loader.py`
- **Unit tests for world loader utility functions. Tests room ID generation,…** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() function.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() with basic components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() handles components with underscores.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() with empty components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Test generate_room_id() preserves special characters in components.** (1 connections) — `server/tests/unit/test_world_loader.py`
- **Generate hierarchical room ID from components. Args: plane: Plane identifier…** (1 connections) — `server/world_loader.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server tests unit test world](server_tests_unit_test_world.md) (4 shared connections)
- [server async persistence room loader](server_async_persistence_room_loader.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*