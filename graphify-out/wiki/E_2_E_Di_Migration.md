# E 2 E Di Migration

> 17 nodes

## Key Concepts

- **main()** (10 connections) — `data/local/mythos_mud_mapbuilder.py`
- **render_with_tcod()** (8 connections) — `data/local/mythos_mud_mapbuilder.py`
- **compute_bounds()** (7 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Any** (6 connections)
- **render_text()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **dump_ascii_to_file()** (6 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_load_tileset()** (4 connections) — `data/local/mythos_mud_mapbuilder.py`
- **example_validator()** (4 connections) — `data/local/mythos_mud_mapbuilder.py`
- **_handle_tcod_events()** (3 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Compute the bounding box of a grid.      Args:         grid: Dictionary mappi** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Load tileset for tcod rendering with fallback options.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Handle tcod events, return True if should exit.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Render a grid map using tcod (libtcodpy) library.      Creates a terminal wind** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Fallback textual renderer using simple printing or rich if available.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Write grid map to an ASCII text file.      Converts the grid to a text represe** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **A tiny example validator; replace with your own validator hook.** (1 connections) — `data/local/mythos_mud_mapbuilder.py`
- **Main entry point for the map builder tool.      Loads room data from JSON file** (1 connections) — `data/local/mythos_mud_mapbuilder.py`

## Relationships

- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (18 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`

## Audit Trail

- EXTRACTED: 60 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*