# Community 790

> 21 nodes

## Key Concepts

- **ascii_map_renderer.py** (16 connections) — `server/services/ascii_map_renderer.py`
- **test_ascii_map_renderer_grid.py** (7 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **test_ascii_map_symbols.py** (6 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **TestBuildGridPlayerMarker** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **TestRendererBinding** (4 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **renderer()** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **test_render_map_empty_and_connected_rooms()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **.test_player_marker_preserved_when_player_room_not_last_at_same_coords()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **ascii_map_symbols.py** (3 connections) — `server/services/ascii_map_symbols.py`
- **test_determine_map_style_and_symbols()** (2 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **.test_renderer_exposes_the_moved_tables()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **fixture** (1 connections)
- **ASCII map renderer for MythosMUD. This module provides server-side rendering of…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Symbol and colour tables for the ASCII map. Pure configuration, split out of…** (1 connections) — `server/services/ascii_map_symbols.py`
- **Unit tests for AsciiMapRenderer grid building. Guards against regressions in…** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **Return a fresh AsciiMapRenderer instance for each test.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **Tests for _build_grid player marker when multiple rooms share coordinates.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **Multiple rooms at same (x,y): cell keeps player marker even if player room is…** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **render_map covers empty map, styles, exits, and row rendering.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **Guards the symbol tables split out of `ascii_map_renderer.py` (#829). The…** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **`renderer.symbols` and friends must still resolve to the moved tables.** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`

## Relationships

- [Community 539](Community_539.md) (10 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 732](Community_732.md) (2 shared connections)
- [Community 334](Community_334.md) (1 shared connections)
- [Map & Admin Responses](Map_&_Admin_Responses.md) (1 shared connections)
- [Community 274](Community_274.md) (1 shared connections)
- [Community 797](Community_797.md) (1 shared connections)
- [Community 700](Community_700.md) (1 shared connections)
- [Community 991](Community_991.md) (1 shared connections)
- [Community 585](Community_585.md) (1 shared connections)
- [Community 1123](Community_1123.md) (1 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`
- `server/services/ascii_map_symbols.py`
- `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- `server/tests/unit/services/test_ascii_map_symbols.py`

## Audit Trail

- EXTRACTED: 39 (91%)
- INFERRED: 4 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*