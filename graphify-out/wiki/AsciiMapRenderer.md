# AsciiMapRenderer

> 18 nodes

## Key Concepts

- **AsciiMapRenderer** (54 connections) — `server/services/ascii_map_renderer.py`
- **TestVerticalExitCharBetween** (9 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_bidirectional_returns_pipe()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_no_exit_returns_none()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_north_and_one_way_south_assign_caret_and_v_by_target()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_north_returns_caret()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_north_uses_caret_bidirectional_uses_pipe()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_south_returns_v()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.__init__()** (2 connections) — `server/services/ascii_map_renderer.py`
- **Renders ASCII maps from room coordinate data. Supports multiple map styles…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Initialize the ASCII map renderer.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Tests for _vertical_exit_char_between (|, v, ^).** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Bidirectional vertical exit renders as a vertical bar.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way south exit renders as a lowercase 'v'.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way north exit renders as a caret.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **When there are no vertical exits, the helper returns None.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way North-only exit renders ^; bidirectional vertical exit renders |.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way north renders ^ and one-way south renders v; symbols match direction to…** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Relationships

- [Any](Any.md) (11 shared connections)
- [test_ascii_map_renderer_exits.py](test_ascii_map_renderer_exits.py.md) (8 shared connections)
- [test_ascii_map_renderer_grid.py](test_ascii_map_renderer_grid.py.md) (6 shared connections)
- [TestHorizontalExitCharBetween](TestHorizontalExitCharBetween.md) (5 shared connections)
- [TestResolveExitTarget](TestResolveExitTarget.md) (5 shared connections)
- [map_minimap.py](map_minimap.py.md) (3 shared connections)
- [._get_vertical_exit_char](_get_vertical_exit_char.md) (3 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)
- [._exit_is_bidirectional](_exit_is_bidirectional.md) (2 shared connections)
- [._render_empty_map](_render_empty_map.md) (1 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`
- `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Audit Trail

- EXTRACTED: 61 (88%)
- INFERRED: 8 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*