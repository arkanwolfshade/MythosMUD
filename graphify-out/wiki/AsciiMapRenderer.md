# AsciiMapRenderer

> 81 nodes · cohesion 0.04

## Key Concepts

- **AsciiMapRenderer** (52 connections) — `server/services/ascii_map_renderer.py`
- **Any** (14 connections)
- **.render_map()** (10 connections) — `server/services/ascii_map_renderer.py`
- **TestVerticalExitCharBetween** (9 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **._build_grid()** (6 connections) — `server/services/ascii_map_renderer.py`
- **._build_exit_lookup()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._determine_map_style()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._exit_is_bidirectional()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_exit_entries_for_room()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_horizontal_exit_char()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_vertical_exit_char()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._render_exit_row()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._render_room_row()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._resolve_exit_target()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_room_symbol()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._horizontal_exit_char_between()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._vertical_exit_char_between()** (4 connections) — `server/services/ascii_map_renderer.py`
- **TestGetHorizontalExitCharViewportBounds** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **._auto_center_viewport()** (3 connections) — `server/services/ascii_map_renderer.py`
- **._get_reverse_direction()** (3 connections) — `server/services/ascii_map_renderer.py`
- **._render_empty_map()** (3 connections) — `server/services/ascii_map_renderer.py`
- **renderer()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_returns_entries_for_valid_exits()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_skips_exit_with_missing_target()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_returns_none_when_next_x_at_or_past_viewport_right()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- *... and 56 more nodes in this community*

## Relationships

- [map_minimap.py](map_minimap.py.md) (24 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`
- `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- `server/tests/unit/services/test_ascii_map_renderer_grid.py`

## Audit Trail

- EXTRACTED: 252 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*