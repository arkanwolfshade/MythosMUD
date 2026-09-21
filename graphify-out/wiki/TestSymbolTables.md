# TestSymbolTables

> 12 nodes

## Key Concepts

- **TestSymbolTables** (7 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **parametrize** (4 connections)
- **.test_every_style_can_draw_a_room_and_the_player()** (3 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_every_style_can_draw_an_intersection()** (3 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_every_style_has_room_player_and_exit_colours()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_styles_match_the_colour_table()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_symbols_are_single_characters()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_the_player_is_distinct_from_every_room_symbol()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **`_get_room_symbol` falls back to "default", and the player marker is how you…** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **Arkham is 153 intersections; they must not fall back to the default glyph.** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **_determine_map_style only accepts a style present in `symbols`; a style with no…** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **The grid allocates one column per room; a wider glyph shifts the whole row.** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`

## Relationships

- [ascii_map_renderer.py](ascii_map_renderer.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_ascii_map_symbols.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*