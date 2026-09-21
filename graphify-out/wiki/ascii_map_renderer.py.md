# ascii_map_renderer.py

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

- [AsciiMapRenderer](AsciiMapRenderer.md) (11 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.render_map](render_map.md) (2 shared connections)
- [map_minimap.py](map_minimap.py.md) (1 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (1 shared connections)
- [TestDepartures](TestDepartures.md) (1 shared connections)
- [test_ascii_map_renderer_exits.py](test_ascii_map_renderer_exits.py.md) (1 shared connections)
- [ascii_map_exits.py](ascii_map_exits.py.md) (1 shared connections)
- [TestSymbolTables](TestSymbolTables.md) (1 shared connections)

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