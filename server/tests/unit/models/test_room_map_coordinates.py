"""`Room` carries map coordinates end to end (#829).

`GET /api/rooms/list` documented that it returned `map_x` / `map_y` and returned `null`
for both, every time. Three independent breaks stacked: `get_rooms_with_exits()` did not
select the columns, `Room.to_dict()` had no keys for them, and the client never copied
them into node data. Because `RoomData` sets `extra="allow"`, nothing raised - the
coordinates were simply always absent, which is why the React Flow map and the room
editor laid every zone out on a naive grid while the ASCII map rendered correctly from
the same columns.

These tests pin the middle link: whatever the query hands `Room`, coordinates survive
into `to_dict()`. The `Decimal` case is the one that actually occurs - `map_x` is
`numeric(10,2)`, which the driver returns as `Decimal`, not `float`.
"""

from __future__ import annotations

from decimal import Decimal

import pytest

from server.models.room import Room, _as_float  # pyright: ignore[reportPrivateUsage]


def _room(**overrides: object) -> Room:
    data: dict[str, object] = {
        "id": "earth_arkhamcity_northside_intersection_derby_garrison",
        "name": "Derby Street and Garrison Street Intersection",
        "description": "A crossing.",
        "plane": "earth",
        "zone": "arkhamcity",
        "sub_zone": "northside",
        "exits": {},
    }
    data.update(overrides)
    return Room(data)


class TestAsFloat:
    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (Decimal("12.00"), 12.0),  # what asyncpg returns for numeric(10,2)
            (Decimal("-2.50"), -2.5),  # coordinates west of origin are negative
            (12, 12.0),
            (12.5, 12.5),
            ("12.00", 12.0),  # JSON payloads round-trip as strings
            (None, None),
            ("", None),
            ("not a number", None),
        ],
    )
    def test_coerces_every_shape_the_column_arrives_in(self, value: object, expected: float | None) -> None:
        assert _as_float(value) == expected

    def test_booleans_are_not_coordinates(self) -> None:
        """bool is a subclass of int, so a naive isinstance check would make True == 1.0."""
        assert _as_float(True) is None
        assert _as_float(False) is None


class TestRoomCoordinates:
    def test_coordinates_survive_into_to_dict(self) -> None:
        room = _room(map_x=Decimal("12.00"), map_y=Decimal("-2.50"))
        payload = room.to_dict()
        assert payload["map_x"] == 12.0
        assert payload["map_y"] == -2.5

    def test_to_dict_always_has_the_keys(self) -> None:
        """The client distinguishes "no coordinates" from "not sent"; the keys must exist
        even when the values are null, or a positioned room is indistinguishable from an
        unpositioned one."""
        payload = _room().to_dict()
        assert "map_x" in payload
        assert "map_y" in payload
        assert payload["map_x"] is None
        assert payload["map_y"] is None

    def test_a_room_at_the_origin_is_not_treated_as_missing(self) -> None:
        """(0, 0) is a real cell. Truthiness checks on coordinates are a classic bug."""
        payload = _room(map_x=Decimal("0.00"), map_y=Decimal("0.00")).to_dict()
        assert payload["map_x"] == 0.0
        assert payload["map_y"] == 0.0

    def test_partial_coordinates_do_not_invent_the_other_axis(self) -> None:
        payload = _room(map_x=Decimal("5.00")).to_dict()
        assert payload["map_x"] == 5.0
        assert payload["map_y"] is None
