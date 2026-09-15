"""Guards the symbol tables split out of `ascii_map_renderer.py` (#829).

The tables were moved into their own module purely to keep the renderer under its length
limit, and `AsciiMapRenderer.__init__` binds them to the same attribute names it always
used. That kind of extraction fails quietly: if a table were dropped or a key renamed, the
renderer would not raise - `_get_room_symbol` falls back through `.get(...)` and every
room would silently render as a blank or the wrong glyph.
"""

from __future__ import annotations

import pytest

from server.services import ascii_map_symbols
from server.services.ascii_map_renderer import AsciiMapRenderer

_STYLES = ("world", "city", "interior")


class TestRendererBinding:
    """`renderer.symbols` and friends must still resolve to the moved tables."""

    def test_renderer_exposes_the_moved_tables(self) -> None:
        renderer = AsciiMapRenderer()
        assert renderer.symbols == ascii_map_symbols.SYMBOLS
        assert renderer.exit_symbols == ascii_map_symbols.EXIT_SYMBOLS
        assert renderer.style_colors == ascii_map_symbols.STYLE_COLORS


class TestSymbolTables:
    @pytest.mark.parametrize("style", _STYLES)
    def test_every_style_can_draw_a_room_and_the_player(self, style: str) -> None:
        """`_get_room_symbol` falls back to "default", and the player marker is how you
        find yourself on the map - a style missing either renders unusably."""
        assert ascii_map_symbols.SYMBOLS[style].get("default")
        assert ascii_map_symbols.SYMBOLS[style].get("player")

    @pytest.mark.parametrize("style", _STYLES)
    def test_every_style_can_draw_an_intersection(self, style: str) -> None:
        """Arkham is 153 intersections; they must not fall back to the default glyph."""
        assert ascii_map_symbols.SYMBOLS[style].get("intersection")

    @pytest.mark.parametrize("style", _STYLES)
    def test_the_player_is_distinct_from_every_room_symbol(self, style: str) -> None:
        table = ascii_map_symbols.SYMBOLS[style]
        player = table["player"]
        others = {key: value for key, value in table.items() if key != "player"}
        clashes = [key for key, value in others.items() if value == player]
        assert not clashes, f"{style}: player marker is indistinguishable from {clashes}"

    def test_styles_match_the_colour_table(self) -> None:
        """_determine_map_style only accepts a style present in `symbols`; a style with no
        colours would render unstyled spans."""
        assert set(ascii_map_symbols.SYMBOLS) == set(ascii_map_symbols.STYLE_COLORS)

    @pytest.mark.parametrize("style", _STYLES)
    def test_every_style_has_room_player_and_exit_colours(self, style: str) -> None:
        assert set(ascii_map_symbols.STYLE_COLORS[style]) >= {"room", "player", "exit"}

    def test_symbols_are_single_characters(self) -> None:
        """The grid allocates one column per room; a wider glyph shifts the whole row."""
        for style, table in ascii_map_symbols.SYMBOLS.items():
            for key, value in table.items():
                assert len(value) == 1, f"{style}.{key} is {len(value)} characters: {value!r}"
