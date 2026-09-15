"""Direct tests for `server/services/ascii_map_exits.py`.

The exit-geometry helpers were extracted out of `AsciiMapRenderer` to get that module
back under its line limit, and the renderer keeps thin methods delegating to them so the
names referenced by `docs/testing/map-regression-tests.md` still resolve.

That split creates a failure nothing else would catch: someone edits one side and not the
other, and the renderer quietly stops agreeing with the module it delegates to. The
delegation tests below pin the two together.

`REVERSE_DIRECTIONS` gets its own attention because the existing renderer test only spot
checks north/south and east/west. A transposed diagonal - "northeast": "southeast" - is
invisible to a spot check but silently breaks bidirectional-exit detection, which is what
decides whether the map draws an arrow or a line.
"""

from __future__ import annotations

import pytest

from server.services import ascii_map_exits
from server.services.ascii_map_renderer import AsciiMapRenderer


class TestReverseDirections:
    def test_every_direction_is_its_own_inverse(self) -> None:
        """reverse(reverse(d)) == d for every entry - catches a transposed pair."""
        for direction, opposite in ascii_map_exits.REVERSE_DIRECTIONS.items():
            assert ascii_map_exits.reverse_direction(opposite) == direction

    def test_all_engine_directions_are_covered(self) -> None:
        """Every direction the command parser accepts needs an opposite, or exits in that
        direction can never be detected as bidirectional."""
        for direction in (
            "north",
            "south",
            "east",
            "west",
            "up",
            "down",
            "northeast",
            "northwest",
            "southeast",
            "southwest",
        ):
            assert ascii_map_exits.reverse_direction(direction), f"{direction} has no opposite"

    def test_unknown_direction_yields_empty_string(self) -> None:
        assert ascii_map_exits.reverse_direction("widdershins") == ""

    def test_direction_lookup_is_case_insensitive(self) -> None:
        assert ascii_map_exits.reverse_direction("NORTH") == "south"


class TestExitCharacters:
    @pytest.mark.parametrize(
        ("east", "west_back", "expected"),
        [
            ({"target": (1, 0)}, {"target": (0, 0)}, "—"),  # bidirectional
            ({"target": (1, 0)}, None, ">"),  # one-way east
            (None, {"target": (0, 0)}, "<"),  # one-way west
            (None, None, None),  # no exit
        ],
    )
    def test_horizontal_characters(
        self, east: dict[str, object] | None, west_back: dict[str, object] | None, expected: str | None
    ) -> None:
        assert ascii_map_exits.horizontal_exit_char_between(east, west_back, 1, 0, 0) == expected

    @pytest.mark.parametrize(
        ("south", "north_back", "expected"),
        [
            ({"target": (0, 1)}, {"target": (0, 0)}, "|"),
            ({"target": (0, 1)}, None, "v"),
            (None, {"target": (0, 0)}, "^"),
            (None, None, None),
        ],
    )
    def test_vertical_characters(
        self, south: dict[str, object] | None, north_back: dict[str, object] | None, expected: str | None
    ) -> None:
        assert ascii_map_exits.vertical_exit_char_between(south, north_back, 1, 0, 0) == expected

    def test_an_exit_pointing_somewhere_else_is_not_drawn(self) -> None:
        """The target must be the neighbouring cell; an exit to a third room draws nothing."""
        assert ascii_map_exits.horizontal_exit_char_between({"target": (9, 9)}, None, 1, 0, 0) is None
        assert ascii_map_exits.vertical_exit_char_between({"target": (9, 9)}, None, 1, 0, 0) is None


class TestRendererDelegation:
    """The renderer's methods must stay equivalent to the functions they delegate to."""

    def test_reverse_direction_delegates(self) -> None:
        renderer = AsciiMapRenderer()
        for direction in ascii_map_exits.REVERSE_DIRECTIONS:
            assert renderer._get_reverse_direction(direction) == ascii_map_exits.reverse_direction(  # pyright: ignore[reportPrivateUsage]
                direction
            )

    def test_horizontal_char_delegates(self) -> None:
        renderer = AsciiMapRenderer()
        east: dict[str, object] = {"target": (1, 0)}
        west_back: dict[str, object] = {"target": (0, 0)}
        assert renderer._horizontal_exit_char_between(  # pyright: ignore[reportPrivateUsage]
            east, west_back, 1, 0, 0
        ) == ascii_map_exits.horizontal_exit_char_between(east, west_back, 1, 0, 0)

    def test_vertical_char_delegates(self) -> None:
        renderer = AsciiMapRenderer()
        south: dict[str, object] = {"target": (0, 1)}
        north_back: dict[str, object] = {"target": (0, 0)}
        assert renderer._vertical_exit_char_between(  # pyright: ignore[reportPrivateUsage]
            south, north_back, 1, 0, 0
        ) == ascii_map_exits.vertical_exit_char_between(south, north_back, 1, 0, 0)

    def test_bridges_delegate(self) -> None:
        renderer = AsciiMapRenderer()
        exit_from: dict[tuple[int, int], dict[str, dict[str, object]]] = {
            (0, 0): {"east": {"target": (4, 0), "is_bidirectional": True}},
        }
        assert renderer._build_exit_bridges(exit_from) == ascii_map_exits.build_exit_bridges(  # pyright: ignore[reportPrivateUsage]
            exit_from
        )


class TestDepartures:
    """Exits that leave the loaded area.

    A map request is scoped to one sub-zone, so the room on the far side of the
    Sanitarium door is simply not in the response. `_resolve_exit_target` cannot place it
    and drops the exit, which left Derby & Parsonage looking like a plain street corner
    with no way into the building.
    """

    @staticmethod
    def _room(room_id: str, x: int, y: int, exits: dict[str, str]) -> dict[str, object]:
        return {"id": room_id, "stable_id": room_id, "map_x": x, "map_y": y, "exits": exits}

    def test_an_exit_to_an_unloaded_room_is_a_departure(self) -> None:
        rooms = [
            self._room("corner", 0, 0, {"north": "sanitarium_entrance", "east": "next"}),
            self._room("next", 1, 0, {"west": "corner"}),
        ]
        assert ascii_map_exits.build_departures(rooms) == {(0, 0): frozenset({"north"})}

    def test_exits_within_the_loaded_set_are_not_departures(self) -> None:
        rooms = [
            self._room("a", 0, 0, {"east": "b"}),
            self._room("b", 1, 0, {"west": "a"}),
        ]
        assert ascii_map_exits.build_departures(rooms) == {}

    def test_a_room_can_depart_in_several_directions(self) -> None:
        rooms = [self._room("a", 0, 0, {"north": "elsewhere", "south": "also_elsewhere"})]
        assert ascii_map_exits.build_departures(rooms) == {(0, 0): frozenset({"north", "south"})}

    def test_rooms_without_coordinates_are_skipped(self) -> None:
        """They cannot be plotted, so there is nowhere to draw the marker."""
        rooms: list[dict[str, object]] = [
            {"id": "a", "stable_id": "a", "map_x": None, "map_y": None, "exits": {"north": "elsewhere"}}
        ]
        assert ascii_map_exits.build_departures(rooms) == {}

    def test_null_exits_are_not_departures(self) -> None:
        rooms: list[dict[str, object]] = [
            {"id": "a", "stable_id": "a", "map_x": 0, "map_y": 0, "exits": {"north": None}}
        ]
        assert ascii_map_exits.build_departures(rooms) == {}
