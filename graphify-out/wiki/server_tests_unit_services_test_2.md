# server tests unit services test

> 10 nodes

## Key Concepts

- **TestHorizontalExitCharBetween** (7 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_bidirectional_returns_em_dash()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_no_exit_returns_none()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_east_returns_gt()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_west_returns_lt()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Tests for _horizontal_exit_char_between (em dash, >, <).** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Bidirectional horizontal exit between two rooms uses an em dash.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way east exit renders as a greater-than sign.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way west exit renders as a less-than sign.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **When there are no horizontal exits, the helper returns None.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`

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