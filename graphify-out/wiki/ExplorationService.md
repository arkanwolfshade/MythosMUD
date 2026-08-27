# ExplorationService

> 12 nodes

## Key Concepts

- **build_room_drop_summary()** (10 connections) — `server/utils/room_renderer.py`
- **test_build_room_drop_summary()** (3 connections) — `server/tests/unit/utils/test_room_renderer_functions.py`
- **test_build_room_drop_summary_empty()** (3 connections) — `server/tests/unit/utils/test_room_renderer_functions.py`
- **test_build_room_drop_summary_empty()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_build_room_drop_summary_multiple_drops()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_build_room_drop_summary_single_drop()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Test build_room_drop_summary() returns newline-separated summary.** (1 connections) — `server/tests/unit/utils/test_room_renderer_functions.py`
- **Test build_room_drop_summary() handles empty drops.** (1 connections) — `server/tests/unit/utils/test_room_renderer_functions.py`
- **Test build_room_drop_summary returns empty line for empty drops.** (1 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Test build_room_drop_summary formats single drop correctly.** (1 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Test build_room_drop_summary formats multiple drops correctly.** (1 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **Return a newline-separated textual summary of room drops.** (1 connections) — `server/utils/room_renderer.py`

## Relationships

- [The Toolkit](The_Toolkit.md) (5 shared connections)
- [GridLayoutManager.tsx](GridLayoutManager.tsx.md) (3 shared connections)
- [10 Concurrent Players Load Test](10_Concurrent_Players_Load_Test.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_room_renderer.py`
- `server/tests/unit/utils/test_room_renderer_functions.py`
- `server/utils/room_renderer.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*