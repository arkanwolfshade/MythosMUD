# test_cache_service.py

> 15 nodes

## Key Concepts

- **clone_room_drops()** (13 connections) — `server/utils/room_renderer.py`
- **test_clone_room_drops()** (3 connections) — `server/tests/unit/utils/test_room_renderer_functions.py`
- **test_clone_room_drops_converts_to_dict()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_clone_room_drops_empty_list()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_clone_room_drops_multiple_drops()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_clone_room_drops_nested_structure()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_clone_room_drops_none()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_clone_room_drops_single_drop()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Test clone_room_drops returns empty list for None.** (2 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Test clone_room_drops() creates deep copy.** (1 connections) — `server/tests/unit/utils/test_room_renderer_functions.py`
- **Test clone_room_drops deep copies single drop.** (1 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Test clone_room_drops deep copies multiple drops.** (1 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Test clone_room_drops deep copies nested structures.** (1 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Test clone_room_drops converts mappings to dict.** (1 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Deep copy room drop payloads to shield callers from mutation.** (1 connections) — `server/utils/room_renderer.py`

## Relationships

- [The Toolkit](The_Toolkit.md) (7 shared connections)
- [GridLayoutManager.tsx](GridLayoutManager.tsx.md) (4 shared connections)
- [10 Concurrent Players Load Test](10_Concurrent_Players_Load_Test.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_room_renderer.py`
- `server/tests/unit/utils/test_room_renderer_functions.py`
- `server/utils/room_renderer.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*