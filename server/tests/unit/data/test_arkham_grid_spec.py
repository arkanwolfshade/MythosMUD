"""Guards `scripts/arkham_grid_spec.py`, the reviewable representation of the Arkham
street plate (#829).

The spec module is the single input from which ~470 street rooms and ~1100 exit links
are generated. A mistake here is not a mistake in one room -- it is a mistake in the
whole city, replicated into three DML files. Two such mistakes were caught by hand
while authoring the spec and are pinned here so they cannot come back:

* Parsonage Street spanned the Miskatonic without being one of the three bridges,
  silently giving the city a fourth crossing.
* Mid-block rooms were emitted one per crossing-pair rather than one per block, which
  collapsed the Sanatorium's two-block frontage on Derby -- the calibration the whole
  map is scaled against -- into a single room.

The coordinate-collision test is the load-bearing one. `AsciiMapRenderer` plots by
`int(map_x)` and resolves a collision by last-writer-wins, so two rooms sharing a cell
do not raise: one of them simply stops existing on the map.

No database and no generated SQL are needed -- this exercises the spec module directly,
so it runs in milliseconds and fails at the point the mistake is made.
"""

from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from itertools import pairwise
from pathlib import Path
from typing import Protocol, cast

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[4]

# The sub-zone stable_ids that actually exist under zone `earth/arkhamcity`, plus the
# five single-room landmark sub-zones added by #829. `subzone_at` must never invent one.
_KNOWN_SUBZONES = frozenset(
    {
        "campus",
        "downtown",
        "easttown",
        "frenchhill",
        "lowersouthside",
        "merchant",
        "northside",
        "rivertown",
        "uptown",
        # the five single-room landmark sub-zones added by #829
        "hangmans_hill",
        "independence_square",
        "old_arkham_graveyard",
        "the_island",
        "wooded_graveyard",
    }
)


class _Street(Protocol):
    key: str
    name: str
    abbr: str
    axis: str
    line: int
    start: int
    end: int


class _Seg(Protocol):
    street: _Street
    x2: int
    y2: int
    lo: tuple[int, int]
    hi: tuple[int, int]


class _Extra(Protocol):
    key: str
    name: str
    subzone: str
    environment: str
    x2: int
    y2: int
    attach_x2: int
    attach_y2: int
    direction: str


class _SpecModule(Protocol):
    ROWS: dict[str, int]
    COLS: dict[str, int]
    STREETS: list[_Street]
    BLOCKS: dict[tuple[str, int, int], int]
    EXTRAS: list[_Extra]
    LANDMARK_SUBZONES: tuple[str, ...]
    SANITARIUM_DOOR: tuple[int, int]
    BRIDGE_COLS: tuple[int, ...]

    def crossings(self) -> dict[tuple[int, int], tuple[_Street, _Street]]: ...
    def segments(self) -> list[_Seg]: ...
    def numbered_segments(self) -> dict[str, list[_Seg]]: ...
    def subzone_at(self, col: int, row: int) -> str: ...
    def blocks_between(self, street: _Street, lo: int, hi: int) -> int: ...


class _Voice(Protocol):
    corner: str
    segments: tuple[str, ...]


class _VoicesModule(Protocol):
    VOICES: dict[str, _Voice]
    CORNER_TEMPLATES: tuple[str, ...]
    EXTRA_PROSE: dict[str, str]


def _load(name: str, relative: str) -> object:
    path = _REPO_ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader, f"cannot load {path}"
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def spec() -> _SpecModule:
    return cast(_SpecModule, _load("_arkham_grid_spec", "scripts/arkham_grid_spec.py"))


@pytest.fixture(scope="module")
def voices() -> _VoicesModule:
    return cast(_VoicesModule, _load("_arkham_street_voices", "scripts/arkham_street_voices.py"))


def _room_cells(spec: _SpecModule) -> list[tuple[tuple[int, int], str]]:
    """Every room's 2x coordinate, labelled, for collision reporting."""
    cells = [((2 * col, 2 * row), f"intersection {col},{row}") for col, row in spec.crossings()]
    cells += [((s.x2, s.y2), f"{s.street.key} segment") for s in spec.segments()]
    cells += [((e.x2, e.y2), f"extra {e.key}") for e in spec.EXTRAS]
    return cells


class TestCoordinates:
    def test_no_two_rooms_share_a_cell(self, spec: _SpecModule) -> None:
        """A shared cell silently deletes a room from the ASCII map rather than erroring."""
        counts: Counter[tuple[int, int]] = Counter(cell for cell, _ in _room_cells(spec))
        clashes = {cell: n for cell, n in counts.items() if n > 1}
        assert not clashes, f"coordinate collisions: {clashes}"

    def test_intersections_sit_on_even_cells(self, spec: _SpecModule) -> None:
        for col, row in spec.crossings():
            assert (2 * col) % 2 == 0 and (2 * row) % 2 == 0

    def test_every_segment_lies_between_its_own_crossings(self, spec: _SpecModule) -> None:
        """A segment must sit strictly between the two crossings it connects, on the
        street's own axis, or its exit directions will not match its geometry."""
        for s in spec.segments():
            lo_x, lo_y = 2 * s.lo[0], 2 * s.lo[1]
            hi_x, hi_y = 2 * s.hi[0], 2 * s.hi[1]
            if s.street.axis == "ew":
                assert s.y2 == lo_y == hi_y, f"{s.street.key} segment left its row"
                assert lo_x < s.x2 < hi_x, f"{s.street.key} segment outside {lo_x}..{hi_x}"
            else:
                assert s.x2 == lo_x == hi_x, f"{s.street.key} segment left its column"
                assert lo_y < s.y2 < hi_y, f"{s.street.key} segment outside {lo_y}..{hi_y}"


class TestRiver:
    def test_exactly_three_streets_cross_the_miskatonic(self, spec: _SpecModule) -> None:
        """Regression: Parsonage ran straight across the water as a fourth bridge."""
        water, river = spec.ROWS["water"], spec.ROWS["river"]
        crossers = {s.line for s in spec.STREETS if s.axis == "ns" and s.start <= water and s.end >= river}
        assert crossers == set(spec.BRIDGE_COLS), (
            f"streets crossing the river at columns {sorted(crossers)}, "
            f"expected exactly {sorted(spec.BRIDGE_COLS)} (West, Garrison, Peabody)"
        )

    def test_parsonage_is_split_by_the_river(self, spec: _SpecModule) -> None:
        runs = [s for s in spec.STREETS if s.key == "parsonage"]
        assert len(runs) == 2, "Parsonage must be two runs sharing a key, north and south"
        north, south = sorted(runs, key=lambda s: s.start)
        assert north.end == spec.ROWS["water"]
        assert south.start == spec.ROWS["river"]

    def test_no_street_room_sits_on_the_bridge_row_except_bridges(self, spec: _SpecModule) -> None:
        bridge_y = 2 * spec.ROWS["bridge"]
        on_row = {s.x2 for s in spec.segments() if s.y2 == bridge_y}
        assert on_row == {2 * c for c in spec.BRIDGE_COLS}


class TestSanitarium:
    def test_door_is_a_real_crossing(self, spec: _SpecModule) -> None:
        assert spec.SANITARIUM_DOOR in spec.crossings(), (
            "the Sanitarium entrance at Derby & Parsonage must be a real intersection room"
        )

    def test_frontage_is_two_blocks_on_both_derby_and_apple(self, spec: _SpecModule) -> None:
        """The user's calibration: the Sanatorium occupies two city blocks between
        Garrison and Peabody. Derby gets there via Parsonage; Apple Lane, which
        Parsonage never reaches, must still total two."""
        c = spec.COLS
        derby = next(s for s in spec.STREETS if s.key == "derby")
        apple = next(s for s in spec.STREETS if s.key == "apple")
        derby_blocks = spec.blocks_between(derby, c["garrison"], c["parsonage"]) + spec.blocks_between(
            derby, c["parsonage"], c["peabody"]
        )
        assert derby_blocks == 2, f"Derby Garrison->Peabody is {derby_blocks} blocks, expected 2"
        assert spec.blocks_between(apple, c["garrison"], c["peabody"]) == 2


class TestStreets:
    def test_every_street_forms_one_unbroken_chain(self, spec: _SpecModule) -> None:
        """Walking a street from end to end must never require leaving it."""
        x = spec.crossings()
        for s in spec.STREETS:
            pts = (
                [c for c in range(s.start, s.end + 1) if (c, s.line) in x]
                if s.axis == "ew"
                else [r for r in range(s.start, s.end + 1) if (s.line, r) in x]
            )
            assert len(pts) >= 2, f"{s.key} has fewer than two crossings: {pts}"
            assert pts[0] == s.start and pts[-1] == s.end, (
                f"{s.key} declares span {s.start}..{s.end} but crosses only {pts[0]}..{pts[-1]}"
            )

    def test_no_stale_block_overrides(self, spec: _SpecModule) -> None:
        """An override naming a span that is not an adjacent crossing pair does nothing
        and is silently ignored -- exactly how a map drifts from its spec."""
        x = spec.crossings()
        live: set[tuple[str, int, int]] = set()
        for s in spec.STREETS:
            pts = (
                sorted(c for c in range(s.start, s.end + 1) if (c, s.line) in x)
                if s.axis == "ew"
                else sorted(r for r in range(s.start, s.end + 1) if (s.line, r) in x)
            )
            live |= {(s.key, a, b) for a, b in pairwise(pts)}
        stale = set(spec.BLOCKS) - live
        assert not stale, f"BLOCKS overrides that match no adjacent crossing pair: {sorted(stale)}"

    def test_segment_numbering_runs_west_to_east_and_north_to_south(self, spec: _SpecModule) -> None:
        for key, segs in spec.numbered_segments().items():
            ew = segs[0].street.axis == "ew"
            ordered = sorted(segs, key=lambda s: (s.x2, s.y2) if ew else (s.y2, s.x2))
            assert segs == ordered, f"{key} segments are not in map order"

    def test_street_keys_are_unique_per_axis_line(self, spec: _SpecModule) -> None:
        """Two runs may share a key only if they share an axis and line (Parsonage)."""
        by_key: dict[str, list[_Street]] = {}
        for s in spec.STREETS:
            by_key.setdefault(s.key, []).append(s)
        for key, runs in by_key.items():
            assert len({(r.axis, r.line) for r in runs}) == 1, f"{key} is used for runs on different lattice lines"


class TestExtras:
    def test_every_extra_attaches_to_a_real_room(self, spec: _SpecModule) -> None:
        """A landmark hanging off a cell with no room in it is an orphan, and the
        isolation baseline in test_dml_room_graph.py may only shrink."""
        occupied = {cell for cell, _ in _room_cells(spec)}
        for e in spec.EXTRAS:
            assert (e.attach_x2, e.attach_y2) in occupied, (
                f"{e.key} attaches to empty cell ({e.attach_x2}, {e.attach_y2})"
            )

    def test_extras_do_not_attach_to_each_other_in_a_cycle(self, spec: _SpecModule) -> None:
        """Chained extras are fine (the graveyard hangs off Hangman's Hill); a cycle
        among them would mean none is reachable from the street grid."""
        by_cell = {(e.x2, e.y2): e for e in spec.EXTRAS}
        for e in spec.EXTRAS:
            seen: set[str] = {e.key}
            cur = e
            while (cur.attach_x2, cur.attach_y2) in by_cell:
                cur = by_cell[(cur.attach_x2, cur.attach_y2)]
                assert cur.key not in seen, f"extras form a cycle at {cur.key}"
                seen.add(cur.key)

    def test_extra_directions_are_supported(self, spec: _SpecModule) -> None:
        """Only n/s/e/w/up/down survive test_dml_room_graph.py's reciprocity check -
        a diagonal fails there as an unknown direction (decision 15)."""
        allowed = {"north", "south", "east", "west", "up", "down"}
        for e in spec.EXTRAS:
            assert e.direction in allowed, f"{e.key} uses unsupported direction {e.direction!r}"

    def test_each_landmark_subzone_has_exactly_one_room(self, spec: _SpecModule) -> None:
        counts: Counter[str] = Counter(e.subzone for e in spec.EXTRAS)
        for sz in spec.LANDMARK_SUBZONES:
            assert counts[sz] == 1, f"{sz} should hold exactly one room, has {counts[sz]}"

    def test_only_the_island_uses_a_vertical_exit(self, spec: _SpecModule) -> None:
        """The Island is reached by a river stair rather than a bridge (decision 12);
        nothing else in Arkham should be introducing up/down exits."""
        vertical = {e.key for e in spec.EXTRAS if e.direction in {"up", "down"}}
        assert vertical == {"the_island"}


class TestVoices:
    """`rooms.name` and `rooms.description` are both NOT NULL with minLength 1, so a
    street with no written voice is not a cosmetic gap - it stops the generator."""

    def test_every_street_has_a_voice(self, spec: _SpecModule, voices: _VoicesModule) -> None:
        street_keys = {s.key for s in spec.STREETS}
        assert street_keys - set(voices.VOICES) == set(), "streets with no written voice"
        assert set(voices.VOICES) - street_keys == set(), "voices for streets that do not exist"

    def test_every_extra_has_prose(self, spec: _SpecModule, voices: _VoicesModule) -> None:
        extra_keys = {e.key for e in spec.EXTRAS}
        assert extra_keys - set(voices.EXTRA_PROSE) == set(), "extras with no prose"
        assert set(voices.EXTRA_PROSE) - extra_keys == set(), "prose for extras that do not exist"

    def test_no_empty_prose(self, voices: _VoicesModule) -> None:
        for key, voice in voices.VOICES.items():
            assert voice.corner.strip(), f"{key} has an empty corner fragment"
            assert voice.segments, f"{key} has no segment variants"
            for text in voice.segments:
                assert len(text.strip()) >= 40, f"{key} has a suspiciously short variant"
        for key, text in voices.EXTRA_PROSE.items():
            assert len(text.strip()) >= 40, f"extra {key} has a suspiciously short description"

    def test_corner_templates_take_both_streets(self, voices: _VoicesModule) -> None:
        assert voices.CORNER_TEMPLATES, "no intersection templates"
        for template in voices.CORNER_TEMPLATES:
            assert "{a}" in template and "{b}" in template, f"template drops a street: {template!r}"

    def test_variants_are_distinct_within_a_street(self, voices: _VoicesModule) -> None:
        for key, voice in voices.VOICES.items():
            assert len(set(voice.segments)) == len(voice.segments), f"{key} repeats a variant"

    def test_long_streets_have_enough_variants(self, spec: _SpecModule, voices: _VoicesModule) -> None:
        """Descriptions cycle by position, so a street with many blocks and few
        variants reads as copy-paste. Room names disambiguate, but not past 5."""
        counts: Counter[str] = Counter(s.street.key for s in spec.segments())
        for key, n in counts.items():
            variants = len(voices.VOICES[key].segments)
            assert n / variants <= 5.0, (
                f"{key} has {n} blocks and only {variants} variants (each would appear {n / variants:.1f} times)"
            )


class TestSubZones:
    def test_every_room_lands_in_a_real_subzone(self, spec: _SpecModule) -> None:
        for col, row in spec.crossings():
            assert spec.subzone_at(col, row) in _KNOWN_SUBZONES
        for s in spec.segments():
            assert spec.subzone_at(s.x2 // 2, s.y2 // 2) in _KNOWN_SUBZONES

    def test_the_two_empty_subzones_finally_have_rooms(self, spec: _SpecModule) -> None:
        """`frenchhill` and `rivertown` have existed with zero rooms; #829 fills them."""
        occupied = {spec.subzone_at(col, row) for col, row in spec.crossings()}
        assert {"frenchhill", "rivertown"} <= occupied

    def test_the_river_corridor_is_rivertown(self, spec: _SpecModule) -> None:
        for row_name in ("water", "bridge", "river"):
            row = spec.ROWS[row_name]
            for col in spec.COLS.values():
                assert spec.subzone_at(col, row) == "rivertown"
