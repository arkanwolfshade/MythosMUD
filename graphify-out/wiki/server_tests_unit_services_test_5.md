# server tests unit services test

> 6 nodes

## Key Concepts

- **TestGetExitEntriesForRoom** (5 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_returns_entries_for_valid_exits()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_skips_exit_with_missing_target()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Tests for _get_exit_entries_for_room.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Valid exits for a room produce one entry with correct direction and coordinates.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Exits whose targets are missing are skipped when building exit entries.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Relationships

- [server services ascii map renderer](server_services_ascii_map_renderer.md) (3 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*