# TestExitBridges

> 6 nodes

## Key Concepts

- **TestExitBridges** (4 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_a_misaligned_vertical_target_is_ignored()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_a_non_tuple_target_is_ignored()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **Guard branches in `build_exit_bridges` and its per-axis helpers.** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **`exit_from` values normally carry a `(x, y)` target; malformed data (a bare…** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **A `south`/`north` exit is expected to keep x fixed; `_vertical_bridge_cells`…** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`

## Relationships

- [AsciiMapRenderer](AsciiMapRenderer.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_ascii_map_exits.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*