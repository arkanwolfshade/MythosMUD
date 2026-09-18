# Community 838

> 19 nodes

## Key Concepts

- **TestSymbolTables** (7 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **test_ascii_map_symbols.py** (6 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **TestRendererBinding** (4 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **parametrize** (4 connections)
- **.test_every_style_can_draw_a_room_and_the_player()** (3 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_every_style_can_draw_an_intersection()** (3 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **ascii_map_symbols.py** (3 connections) — `server/services/ascii_map_symbols.py`
- **.test_renderer_exposes_the_moved_tables()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_every_style_has_room_player_and_exit_colours()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_styles_match_the_colour_table()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_symbols_are_single_characters()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **.test_the_player_is_distinct_from_every_room_symbol()** (2 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **Symbol and colour tables for the ASCII map. Pure configuration, split out of…** (1 connections) — `server/services/ascii_map_symbols.py`
- **Guards the symbol tables split out of `ascii_map_renderer.py` (#829). The…** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **`renderer.symbols` and friends must still resolve to the moved tables.** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **`_get_room_symbol` falls back to "default", and the player marker is how you…** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **Arkham is 153 intersections; they must not fall back to the default glyph.** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **_determine_map_style only accepts a style present in `symbols`; a style with no…** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`
- **The grid allocates one column per room; a wider glyph shifts the whole row.** (1 connections) — `server/tests/unit/services/test_ascii_map_symbols.py`

## Relationships

- [Community 534](Community_534.md) (3 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)

## Source Files

- `server/services/ascii_map_symbols.py`
- `server/tests/unit/services/test_ascii_map_symbols.py`

## Audit Trail

- EXTRACTED: 25 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*