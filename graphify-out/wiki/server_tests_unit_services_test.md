# server tests unit services test

> 10 nodes

## Key Concepts

- **TestResolveExitTarget** (7 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_returns_coords_and_bidirectional_when_target_has_reverse_exit()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_returns_coords_and_not_bidirectional_when_no_reverse()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_returns_none_when_target_room_has_no_coords()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_returns_none_when_target_room_missing()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Room without a reverse exit is not considered bidirectional.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **If the target room ID does not exist, the helper returns None.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **If the target room lacks map coordinates, the helper returns None.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Tests for _resolve_exit_target.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Room with a reverse exit is treated as bidirectional and returns its…** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Relationships

- [server services ascii map renderer](server_services_ascii_map_renderer.md) (5 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Audit Trail

- EXTRACTED: 14 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*