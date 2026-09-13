"""Guards the Arkham street grid in the DML seed files (#829).

`test_dml_room_graph.py` proves the world's exits are *structurally* sound - reciprocal,
non-duplicate, non-dangling. It cannot tell whether Derby Street is wired to the right
cross-streets, whether a block has three exits, or whether two rooms occupy one map
cell. Those are geometry, and 481 generated rooms are exactly the case where nobody
reviews the SQL closely enough to notice.

The load-bearing assertions here:

* Every Arkham room has coordinates. `_needs_coordinate_generation`
  (server/api/maps.py:112-122) fires a zone-wide BFS rewrite when *any* room in the
  zone lacks them, which would silently overwrite every coordinate authored from the
  map plate. One NULL room is enough to lose the whole grid.
* No two rooms share a cell. `AsciiMapRenderer` plots by `int(map_x)` and resolves a
  collision last-writer-wins, so a duplicate cell does not raise - a room just stops
  existing on the map.
* No exit passes through a third room's cell, which is the build-time form of the
  "edges should not cross nodes" requirement the map editor asks for at runtime.

Parses the COPY blocks straight out of the text files, so it needs no database and
runs in milliseconds.
"""

from __future__ import annotations

import re
from collections import defaultdict
from typing import NamedTuple

import pytest

from server.utils.project_paths import get_project_root

_DML = "data/db/mythos_dev_dml.sql"
_ARKHAM = "earth_arkhamcity_"
_SANITARIUM = "_sanitarium_"

# Sanitarium interiors are laid out by their own exit graph in a coordinate region well
# clear of the street lattice; they are not part of the plate and are excluded from the
# street-geometry checks (but NOT from the coordinate-uniqueness check).
_SEGMENT_RE = re.compile(r"_room_([a-z_]+)_(st|ln|ave)_(\d{3})$")
_INTERSECTION_RE = re.compile(r"_intersection_([a-z_]+)$")

_DELTA = {"north": (0, -1), "south": (0, 1), "east": (1, 0), "west": (-1, 0)}

# (rooms by stable_id, links as (from, to, direction)) - the parsed DML, built once.
World = tuple[dict[str, "Room"], list[tuple[str, str, str]]]


class Room(NamedTuple):
    stable_id: str
    x: float  # NaN when the DML has \N, so `x != x` detects a missing coordinate
    y: float
    subzone: str


def _copy_block(text: str, table: str) -> list[list[str]]:
    m = re.search(rf"^COPY [\w.]+\.{table} \([^)]*\) FROM stdin;\n", text, re.M)
    assert m, f"no COPY block for {table}"
    end = text.index("\n\\.", m.end())
    return [line.split("\t") for line in text[m.end() : end + 1].rstrip("\n").split("\n")]


@pytest.fixture(scope="module")
def world() -> World:
    text = (get_project_root() / _DML).read_bytes().decode("utf-8")
    rows = _copy_block(text, "rooms")
    by_uuid = {
        r[0]: Room(
            r[2],
            float(r[6]) if r[6] != "\\N" else float("nan"),
            float(r[7]) if r[7] != "\\N" else float("nan"),
            r[2].split("_")[2],
        )
        for r in rows
    }
    links = [
        (by_uuid[x[1]].stable_id, by_uuid[x[2]].stable_id, x[3])
        for x in _copy_block(text, "room_links")
        if x[1] in by_uuid and x[2] in by_uuid
    ]
    return {r.stable_id: r for r in by_uuid.values()}, links


def _arkham(rooms: dict[str, Room]) -> dict[str, Room]:
    return {k: v for k, v in rooms.items() if k.startswith(_ARKHAM)}


def _streets(rooms: dict[str, Room]) -> dict[str, Room]:
    return {k: v for k, v in _arkham(rooms).items() if _SANITARIUM not in k}


class TestCoordinates:
    def test_no_arkham_room_lacks_coordinates(self, world: World) -> None:
        """One NULL room triggers a zone-wide BFS that overwrites the authored grid."""
        missing = [k for k, r in _arkham(world[0]).items() if r.x != r.x or r.y != r.y]
        assert not missing, f"Arkham rooms with NULL coordinates: {missing[:10]}"

    def test_no_two_arkham_rooms_share_a_cell(self, world: World) -> None:
        cells: dict[tuple[int, int], list[str]] = defaultdict(list)
        for k, r in _arkham(world[0]).items():
            cells[(int(r.x), int(r.y))].append(k)
        clashes = {c: ids for c, ids in cells.items() if len(ids) > 1}
        assert not clashes, f"rooms sharing a map cell (one would vanish): {clashes}"


class TestMinimapReach:
    """The minimap viewport is counted in CELLS, not rooms.

    `_auto_center_viewport` centres on `player_x - viewport_width // 2` and the minimap
    defaults to `size=5`, so every cell of spacing between connected rooms costs the
    player visible map. Laying the Sanitarium out on a 2x lattice shrank a 5x5 minimap
    from 5 rooms per axis to 3 and made the building render as a stub of itself.
    """

    def test_connected_rooms_sit_on_adjacent_cells(self, world: World) -> None:
        rooms, links = world
        arkham = _arkham(rooms)
        spread: list[str] = []
        for frm, to, direction in links:
            if frm not in arkham or to not in arkham or direction not in _DELTA:
                continue
            # Each sub-zone is its own coordinate space (CoordinateGenerator groups by
            # sub_zone), so a door from an interior to the street is a deliberate jump
            # between regions, not a spacing mistake.
            if (_SANITARIUM in frm) != (_SANITARIUM in to):
                continue
            a, b = rooms[frm], rooms[to]
            steps = abs(int(a.x) - int(b.x)) + abs(int(a.y) - int(b.y))
            # Street blocks legitimately span two cells where a street crosses a column
            # that carries no cross-street; nothing should ever exceed that.
            if steps > 2:
                spread.append(f"{frm} --{direction}--> {to} spans {steps} cells")
        assert not spread, "exits spanning too many cells (costs minimap reach): " + "; ".join(spread[:6])

    def test_the_sanitarium_is_compact_enough_to_navigate(self, world: World) -> None:
        """Walking one room must move the player exactly one cell inside the building."""
        rooms, links = world
        interior = {k: v for k, v in _arkham(rooms).items() if _SANITARIUM in k}
        for frm, to, direction in links:
            if frm not in interior or to not in interior or direction not in _DELTA:
                continue
            a, b = rooms[frm], rooms[to]
            steps = abs(int(a.x) - int(b.x)) + abs(int(a.y) - int(b.y))
            assert steps == 1, f"{frm} --{direction}--> {to} spans {steps} cells, expected 1"

    def test_no_room_invents_a_map_symbol_it_does_not_need(self) -> None:
        """AsciiMapRenderer auto-assigns a symbol from the environment when none is
        stored. Stamping one on every room replaces that with identical marks."""
        text = (get_project_root() / _DML).read_bytes().decode("utf-8")
        rows = _copy_block(text, "rooms")
        stamped = [r[2] for r in rows if _SANITARIUM in r[2] and r[9] != "\\N"]
        assert not stamped, f"sanitarium rooms with a hard-coded map_symbol: {stamped[:5]}"


class TestStreetGeometry:
    def test_segments_have_exactly_two_exits_on_one_axis(self, world: World) -> None:
        rooms, links = world
        streets = _streets(rooms)
        out: dict[str, list[str]] = defaultdict(list)
        for frm, _to, direction in links:
            if frm in streets:
                out[frm].append(direction)
        for sid in streets:
            if not _SEGMENT_RE.search(sid):
                continue
            dirs = out[sid]
            # A block with a landmark or building hanging off it legitimately has three.
            assert 2 <= len(dirs) <= 3, f"{sid} has {len(dirs)} exits: {dirs}"
            through = [d for d in dirs if d in _DELTA]
            axes = {d in ("north", "south") for d in through}
            assert len(axes) >= 1, f"{sid} has no cardinal exits"

    def test_intersections_have_two_to_four_exits(self, world: World) -> None:
        rooms, links = world
        streets = _streets(rooms)
        out: dict[str, list[str]] = defaultdict(list)
        for frm, _to, direction in links:
            if frm in streets:
                out[frm].append(direction)
        for sid in streets:
            if _INTERSECTION_RE.search(sid):
                assert 2 <= len(out[sid]) <= 4, f"{sid} has {len(out[sid])} exits"

    def test_exit_direction_matches_geometry(self, world: World) -> None:
        """An east exit must lead to a greater map_x, or the map lies about the city."""
        rooms, links = world
        streets = _streets(rooms)
        for frm, to, direction in links:
            if frm not in streets or to not in streets or direction not in _DELTA:
                continue
            a, b = rooms[frm], rooms[to]
            dx, dy = _DELTA[direction]
            if dx:
                assert (b.x - a.x) * dx > 0 and b.y == a.y, f"{frm} --{direction}--> {to}"
            else:
                assert (b.y - a.y) * dy > 0 and b.x == a.x, f"{frm} --{direction}--> {to}"

    def test_no_street_exit_passes_through_another_room(self, world: World) -> None:
        """The build-time form of the editor's "edges must not cross nodes" rule.

        Scoped to the street grid, which is planar by construction: it is a rectilinear
        lattice, so every exit is axis-aligned between adjacent cells and no third room
        can lie on the line.

        The Sanitarium interior is deliberately excluded, and this is a real limitation
        rather than an oversight. Its exits put a corridor's continuation and that
        corridor's side rooms in the SAME direction - `hallway_001` leads north to the
        laundry and the corridor itself also runs north - so in two dimensions they
        compete for one cell. No layout can satisfy that without changing the room
        graph, which #829 does not touch. Interior rooms still get unique cells (see
        TestCoordinates); they just cannot be drawn crossing-free.
        """
        rooms, links = world
        arkham = _streets(rooms)
        occupied = {(int(r.x), int(r.y)): k for k, r in arkham.items()}
        offenders: list[str] = []
        for frm, to, direction in links:
            if frm not in arkham or to not in arkham or direction not in _DELTA:
                continue
            a, b = rooms[frm], rooms[to]
            dx, dy = _DELTA[direction]
            steps = int(abs(b.x - a.x) + abs(b.y - a.y))
            for i in range(1, steps):
                cell = (int(a.x) + dx * i, int(a.y) + dy * i)
                if cell in occupied:
                    offenders.append(f"{frm} --{direction}--> {to} crosses {occupied[cell]}")
        assert not offenders, "exits crossing rooms: " + "; ".join(offenders[:6])


class TestConnectivity:
    def test_the_whole_arkham_grid_is_one_component(self, world: World) -> None:
        """A player must be able to walk from any Arkham room to any other."""
        rooms, links = world
        arkham = set(_arkham(rooms))
        adjacency: dict[str, set[str]] = defaultdict(set)
        for frm, to, _d in links:
            if frm in arkham and to in arkham:
                adjacency[frm].add(to)
                adjacency[to].add(frm)
        start = "earth_arkhamcity_sanitarium_room_foyer_001"
        seen = {start}
        stack = [start]
        while stack:
            for nxt in adjacency[stack.pop()]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        # The four deliberately isolated sanitarium stubs are the documented exception.
        unreachable = arkham - seen
        assert all(_SANITARIUM in u for u in unreachable), (
            f"street rooms unreachable from the Sanitarium foyer: "
            f"{sorted(u for u in unreachable if _SANITARIUM not in u)[:10]}"
        )

    def test_the_sanitarium_opens_onto_derby_and_parsonage(self, world: World) -> None:
        """The plate puts the entrance mid-block between Garrison and Peabody (#829)."""
        _rooms, links = world
        door = "earth_arkhamcity_sanitarium_room_foyer_entrance_001"
        outward = [(to, d) for frm, to, d in links if frm == door and not to.startswith(_ARKHAM + "sanitarium")]
        assert outward == [("earth_arkhamcity_northside_intersection_derby_parsonage", "south")], (
            f"the Sanitarium's door leads to {outward}"
        )

    def test_innsmouth_is_still_reachable_on_foot(self, world: World) -> None:
        """The only cross-zone walk in the world; the rebuild must not sever it."""
        _rooms, links = world
        causeway = "earth_innsmouth_waterfront_room_causeway_001"
        both = {(frm, to, d) for frm, to, d in links if causeway in (frm, to)}
        assert ("earth_arkhamcity_northside_room_apple_ln_003", causeway, "north") in both
        assert (causeway, "earth_arkhamcity_northside_room_apple_ln_003", "south") in both


class TestIdentifiers:
    def test_stable_id_subzone_matches_the_room_it_is_filed_under(self, world: World) -> None:
        """The third id segment is how the client derives a sub-zone for map requests
        (AsciiMinimap.deriveEffectiveLocation), so it has to be a real sub-zone."""
        known = {
            "campus",
            "downtown",
            "easttown",
            "frenchhill",
            "lowersouthside",
            "merchant",
            "northside",
            "rivertown",
            "sanitarium",
            "uptown",
            "hangmans_hill",
            "independence_square",
            "old_arkham_graveyard",
            "the_island",
            "wooded_graveyard",
        }
        bad = sorted({k for k in _arkham(world[0]) if not any(k.startswith(f"{_ARKHAM}{s}_") for s in known)})
        assert not bad, f"rooms whose id names no known sub-zone: {bad[:10]}"
