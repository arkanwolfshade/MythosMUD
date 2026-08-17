# server tests unit services test

> 12 nodes

## Key Concepts

- **test_ascii_map_renderer_grid.py** (8 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **TestBuildGridPlayerMarker** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **renderer()** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **test_render_map_empty_and_connected_rooms()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **.test_player_marker_preserved_when_player_room_not_last_at_same_coords()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **test_determine_map_style_and_symbols()** (2 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **fixture** (1 connections)
- **Unit tests for AsciiMapRenderer grid building. Guards against regressions in…** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **Return a fresh AsciiMapRenderer instance for each test.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **Tests for _build_grid player marker when multiple rooms share coordinates.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **Multiple rooms at same (x,y): cell keeps player marker even if player room is…** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **render_map covers empty map, styles, exits, and row rendering.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`

## Relationships

- [server services ascii map renderer](server_services_ascii_map_renderer.md) (7 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_ascii_map_renderer_grid.py`

## Audit Trail

- EXTRACTED: 15 (79%)
- INFERRED: 4 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*