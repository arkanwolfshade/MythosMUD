"""The ASCII map draws exits that span more than one grid cell (#829).

A grid cell is not always a room. Arkham's blocks vary in length - a street may run
several lattice columns before the next cross street - so two rooms one step apart in
game can be several cells apart on the map. The renderer used to look only at `x + 1`,
so those exits drew nothing at all and the rooms appeared disconnected: the far side of
the map showed floating `+` and `.` marks with no lines between them.

This cannot be fixed in the data. A uniform lattice would need West->Garrison to be the
same distance everywhere, but north of the river Brown, Jenkin and Gedney sit between
them and south of the river nothing does, so no single spacing satisfies both. Spanning
exits are a permanent property of an honest map, and the renderer has to draw them.
"""

from __future__ import annotations

import re

from server.services.ascii_map_renderer import AsciiMapRenderer


def _plain(html: str) -> list[str]:
    """Strip the HTML spans so the assertions read like the map the player sees."""
    lines = [re.sub(r"<[^>]+>", "", line).rstrip() for line in html.split("\n")]
    return [line for line in lines if line.strip()]


def _room(room_id: str, x: int, y: int, exits: dict[str, str]) -> dict[str, object]:
    return {
        "id": room_id,
        "stable_id": room_id,
        "name": f"{room_id} Intersection",
        "map_x": x,
        "map_y": y,
        "map_style": "city",
        "exits": exits,
    }


class TestHorizontalBridging:
    def test_an_east_west_exit_spanning_three_cells_is_drawn(self) -> None:
        rooms = [
            _room("a", 0, 0, {"east": "b"}),
            _room("b", 3, 0, {"west": "a"}),
        ]
        rendered = _plain(
            AsciiMapRenderer().render_map(
                rooms, current_room_id="a", viewport_width=6, viewport_height=1, viewport_x=0, viewport_y=0
            )
        )
        assert rendered, "nothing rendered"
        row = rendered[0]
        assert "—" in row, f"no connector drawn across the gap: {row!r}"

    def test_adjacent_rooms_still_render_unchanged(self) -> None:
        """The bridge logic must not alter the ordinary one-cell case."""
        rooms = [
            _room("a", 0, 0, {"east": "b"}),
            _room("b", 1, 0, {"west": "a"}),
        ]
        row = _plain(
            AsciiMapRenderer().render_map(
                rooms, current_room_id="a", viewport_width=4, viewport_height=1, viewport_x=0, viewport_y=0
            )
        )[0]
        assert "—" in row

    def test_an_unconnected_gap_stays_blank(self) -> None:
        """Two rooms with no exit between them must NOT be joined by a line."""
        rooms = [
            _room("a", 0, 0, {}),
            _room("b", 3, 0, {}),
        ]
        row = _plain(
            AsciiMapRenderer().render_map(
                rooms, current_room_id="a", viewport_width=6, viewport_height=1, viewport_x=0, viewport_y=0
            )
        )[0]
        assert "—" not in row, f"drew a connector where there is no exit: {row!r}"


class TestVerticalBridging:
    def test_a_north_south_exit_spanning_three_cells_is_drawn(self) -> None:
        rooms = [
            _room("a", 0, 0, {"south": "b"}),
            _room("b", 0, 3, {"north": "a"}),
        ]
        rendered = _plain(
            AsciiMapRenderer().render_map(
                rooms, current_room_id="a", viewport_width=2, viewport_height=5, viewport_x=0, viewport_y=0
            )
        )
        assert any("|" in line for line in rendered), f"no connector down the gap: {rendered}"

    def test_an_unconnected_vertical_gap_stays_blank(self) -> None:
        rooms = [
            _room("a", 0, 0, {}),
            _room("b", 0, 3, {}),
        ]
        rendered = _plain(
            AsciiMapRenderer().render_map(
                rooms, current_room_id="a", viewport_width=2, viewport_height=5, viewport_x=0, viewport_y=0
            )
        )
        assert not any("|" in line for line in rendered), f"drew a connector with no exit: {rendered}"


class TestBridgeComputation:
    def test_only_interior_cells_are_bridged(self) -> None:
        """The endpoints are rooms; only the cells strictly between them are filled."""
        renderer = AsciiMapRenderer()
        exit_from: dict[tuple[int, int], dict[str, dict[str, object]]] = {
            (0, 0): {"east": {"target": (3, 0), "is_bidirectional": True}},
        }
        horizontal, vertical = renderer._build_exit_bridges(exit_from)  # pyright: ignore[reportPrivateUsage]
        assert horizontal == {(1, 0), (2, 0)}
        assert vertical == set()

    def test_adjacent_rooms_produce_no_bridge_cells(self) -> None:
        renderer = AsciiMapRenderer()
        exit_from: dict[tuple[int, int], dict[str, dict[str, object]]] = {
            (0, 0): {"east": {"target": (1, 0), "is_bidirectional": True}},
        }
        horizontal, vertical = renderer._build_exit_bridges(exit_from)  # pyright: ignore[reportPrivateUsage]
        assert horizontal == set()
        assert vertical == set()

    def test_a_diagonal_target_is_ignored(self) -> None:
        """Only axis-aligned spans can be drawn; a diagonal would fill the wrong cells."""
        renderer = AsciiMapRenderer()
        exit_from: dict[tuple[int, int], dict[str, dict[str, object]]] = {
            (0, 0): {"east": {"target": (3, 2), "is_bidirectional": True}},
        }
        horizontal, vertical = renderer._build_exit_bridges(exit_from)  # pyright: ignore[reportPrivateUsage]
        assert horizontal == set()
        assert vertical == set()

    def test_westward_and_northward_spans_are_bridged_too(self) -> None:
        """Spans are directional; the lower endpoint is not always the source."""
        renderer = AsciiMapRenderer()
        exit_from: dict[tuple[int, int], dict[str, dict[str, object]]] = {
            (5, 4): {
                "west": {"target": (2, 4), "is_bidirectional": True},
                "north": {"target": (5, 1), "is_bidirectional": True},
            },
        }
        horizontal, vertical = renderer._build_exit_bridges(exit_from)  # pyright: ignore[reportPrivateUsage]
        assert horizontal == {(3, 4), (4, 4)}
        assert vertical == {(5, 2), (5, 3)}


class TestDepartureMarkers:
    """The map must show that a room has a way out of the area being drawn.

    Standing at Derby & Parsonage, the Sanitarium is one step north - but its rooms
    belong to another sub-zone and are not in the map response, so no exit was drawn at
    all and the corner read as a dead end.
    """

    def _rendered(self, rooms: list[dict[str, object]], width: int = 4, height: int = 3) -> str:
        return "\n".join(
            _plain(
                AsciiMapRenderer().render_map(
                    rooms, current_room_id="a", viewport_width=width, viewport_height=height,
                    viewport_x=0, viewport_y=0,
                )
            )
        )

    def test_a_north_exit_out_of_the_area_is_marked(self) -> None:
        rooms = [
            {**_room("a", 0, 1, {"north": "earth_arkhamcity_sanitarium_room_foyer_entrance_001"})},
        ]
        assert "*" in self._rendered(rooms), "no marker for the exit leaving the area"

    def test_an_east_exit_out_of_the_area_is_marked(self) -> None:
        rooms = [{**_room("a", 0, 0, {"east": "somewhere_else"})}]
        assert "*" in self._rendered(rooms)

    def test_an_exit_to_a_loaded_room_is_not_marked(self) -> None:
        """An ordinary exit already draws a connector; it must not also show a marker."""
        rooms = [
            {**_room("a", 0, 0, {"east": "b"})},
            {**_room("b", 1, 0, {"west": "a"})},
        ]
        rendered = self._rendered(rooms)
        assert "—" in rendered
        assert "*" not in rendered, "a fully-drawn exit was also marked as leaving"

    def test_a_room_with_no_exits_is_not_marked(self) -> None:
        rooms = [{**_room("a", 0, 0, {})}]
        assert "*" not in self._rendered(rooms)
