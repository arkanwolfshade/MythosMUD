"""Generate the Arkham street grid as pg_dump COPY-block rows (#829).

One-shot. Reads `arkham_grid_spec` (the map) and `arkham_street_voices` (the prose)
and emits tab-separated rows for `rooms`, `room_links`, `subzones` and
`zone_configurations`, ready to splice into the seed.

The seed remains the source of truth after this runs -- this script is kept as
a historical record of how the city was derived, beside the other one-shot
migration scripts in this directory. It is not a maintained pipeline; hand-edit
the seed afterwards like any other room.

UUIDs are deterministic v5 so re-running this script reproduces the same ids for
the same input, not because two files must stay byte-identical -- since #811 there
is a single schema-agnostic seed (data/db/seed.sql), not one per environment.
Namespace and key formats are copied from `scripts/static_data/generate_sql.mjs`
and verified against existing seed rows -- note that `subzones` uses a single
colon and `zone_configurations` a double one.

    python scripts/generate_arkham_grid.py --out build/arkham/

Emits rooms.tsv, room_links.tsv, subzones.tsv, zone_configurations.tsv and a
summary on stdout.

group: id/name builders below are intentionally many small single-purpose
functions (one per stable-id/UUID/name shape) rather than one large function --
that decomposition is the point, not fragmentation.
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from itertools import pairwise
from pathlib import Path
from typing import NamedTuple

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))


# Reason: this file is a standalone script (`python scripts/generate_arkham_grid.py`, see the
# module docstring), not a package member -- a relative import fails with no parent package,
# and scripts/ has no __init__.py for a `scripts.arkham_grid_spec` absolute import to resolve.
# sys.path.insert above already makes the bare name resolve correctly at runtime; this is the
# same tradeoff `noqa: E402` documents for the same reason.
import arkham_grid_spec as S  # noqa: E402  # pyright: ignore[reportImplicitRelativeImport]
import arkham_street_voices as V  # noqa: E402  # pyright: ignore[reportImplicitRelativeImport]

# --------------------------------------------------------------------------
# Identity
# --------------------------------------------------------------------------

NAMESPACE = uuid.UUID("c8e7f86d-b1c9-4074-8b2e-9f3c6c8a9f2a")
ZONE_STABLE = "earth/arkhamcity"
ZONE_UUID = "4f286c89-fe32-5c6b-98d7-79bdc83ae183"
PLANE_ZONE = "earth_arkhamcity"


def room_uuid(stable_id: str) -> str:
    return str(uuid.uuid5(NAMESPACE, f"rooms:{stable_id}"))


def link_uuid(from_stable_id: str, direction: str) -> str:
    return str(uuid.uuid5(NAMESPACE, f"room_links:{from_stable_id}:{direction}"))


def subzone_uuid(subzone: str) -> str:
    return str(uuid.uuid5(NAMESPACE, f"subzones:{ZONE_STABLE}:{subzone}"))


def zone_config_uuid(subzone: str) -> str:
    # NOTE the double colon - this differs from the subzones key above.
    return str(uuid.uuid5(NAMESPACE, f"zone_configurations:{ZONE_STABLE}::{subzone}"))


# --------------------------------------------------------------------------
# Fixed points the grid must honour
# --------------------------------------------------------------------------

# The Sanitarium's only door. Its interior is untouched by #829; only the street
# it opens onto changes, from Derby & Garrison to Derby & Parsonage.
SANITARIUM_ENTRANCE = "earth_arkhamcity_sanitarium_room_foyer_entrance_001"

# Arkham's one link to another zone. Regenerating this exact stable_id keeps its
# UUID, so both causeway links survive with no edit on the Innsmouth side.
INNSMOUTH_ATTACH = "earth_arkhamcity_northside_room_apple_ln_003"
INNSMOUTH_CAUSEWAY = "earth_innsmouth_waterfront_room_causeway_001"

# The one Arkham room outside the Sanitarium that is a building interior rather than
# a street: `indoors`, and one of only two `rest_location` rooms in the world. #829
# replaces Arkham's STREETS, not its interiors, so this survives the rebuild and is
# simply re-attached to the new Curwen Street. It's the MUD's inn (rest_location) -- present
# in data/db/seed.sql for all three environments since #811 (a stale mythos_unit-only omission
# from before the DML collapse was fixed alongside it).
BOARDING_HOUSE = "earth_arkhamcity_downtown_room_curwen_boarding_house_001"
# North of the Curwen Street block between Garrison and Parsonage - the commercial
# heart, which suits "squeezed between two storefronts".
BOARDING_HOUSE_CELL = (13, 3)
BOARDING_HOUSE_ATTACH = (13, 4)

# Short room-id fragments for the landmark sub-zones, so we do not emit
# `..._the_island_room_the_island_001`.
LANDMARK_ROOM_KEY = {
    "the_island": "island",
    "independence_square": "square",
    "hangmans_hill": "summit",
    "wooded_graveyard": "graveyard",
    "old_arkham_graveyard": "graveyard",
}

NEW_SUBZONES: dict[str, tuple[str, str, dict[str, float]]] = {
    "hangmans_hill": (
        "Hangman's Hill",
        "The bare rise west of Arkham where the gallows stood until 1789. Nothing has "
        "grown on the summit since, and the town below makes a pattern from up here that "
        "it does not make from within.",
        {"combat_modifier": 1.2, "exploration_bonus": 1.1, "npc_spawn_modifier": 1.6,
         "lucidity_drain_rate": 1.5},
    ),
    "wooded_graveyard": (
        "The Wooded Graveyard",
        "Old stones lean among close-grown trees on Hangman's Hill's northern slope. The "
        "wood has taken the ground back so thoroughly that the paths survive only as "
        "absences between the trunks.",
        {"combat_modifier": 1.1, "exploration_bonus": 1.2, "npc_spawn_modifier": 1.4,
         "lucidity_drain_rate": 1.0, "corruption_rate": 0.05},
    ),
    "old_arkham_graveyard": (
        "Old Arkham Graveyard",
        "The town's first burying ground, walled in iron and crowded with slate markers "
        "whose winged skulls have weathered to blank ovals. The ground inside the railings "
        "is noticeably higher than the street outside them.",
        {"combat_modifier": 1.0, "exploration_bonus": 1.2, "npc_spawn_modifier": 1.3,
         "lucidity_drain_rate": 0.8, "corruption_rate": 0.05},
    ),
    "independence_square": (
        "Independence Square",
        "A civic square of gravel walks and clipped limes with a bandstand at its centre. "
        "It is the one open space in Arkham that feels entirely safe, which the older "
        "residents consider worth remarking on.",
        {"combat_modifier": 0.7, "exploration_bonus": 1.2, "npc_spawn_modifier": 0.6,
         "lucidity_drain_rate": 0.0},
    ),
    "the_island": (
        "The Island",
        "A low wooded island in the Miskatonic, reached by a stone stair down the northern "
        "embankment. The trees are older than anything on either bank and the river divides "
        "around them without hurry.",
        {"combat_modifier": 1.0, "exploration_bonus": 1.5, "npc_spawn_modifier": 0.8,
         "lucidity_drain_rate": 1.2},
    ),
}


class Room(NamedTuple):
    stable_id: str
    subzone: str
    name: str
    description: str
    environment: str
    map_x: int
    map_y: int
    map_symbol: str


class Link(NamedTuple):
    from_id: str
    to_id: str
    direction: str


OPPOSITE = {"north": "south", "south": "north", "east": "west", "west": "east",
            "up": "down", "down": "up"}


# --------------------------------------------------------------------------
# Naming
# --------------------------------------------------------------------------


def _street_at(col: int, row: int, axis: str) -> S.Street:
    """The street of the given axis passing through a crossing."""
    ew, ns = S.crossings()[(col, row)]
    return ew if axis == "ew" else ns


def intersection_stable_id(col: int, row: int) -> str:
    ew, ns = S.crossings()[(col, row)]
    a, b = sorted((ew.key, ns.key))
    return f"{PLANE_ZONE}_{S.subzone_at(col, row)}_intersection_{a}_{b}"


def intersection_name(col: int, row: int) -> str:
    ew, ns = S.crossings()[(col, row)]
    return f"{ew.name} and {ns.name} Intersection"


def intersection_description(col: int, row: int) -> str:
    ew, ns = S.crossings()[(col, row)]
    template = V.CORNER_TEMPLATES[(col * 7 + row * 3) % len(V.CORNER_TEMPLATES)]
    text = template.format(a=V.VOICES[ew.key].corner, b=V.VOICES[ns.key].corner)
    # Corner fragments are lowercase noun phrases, so a template that opens with one
    # would start the sentence in lowercase.
    return text[0].upper() + text[1:]


def segment_name(seg: S.Seg, index_in_span: int, span_size: int) -> str:
    """Name a block by the nearer of the two crossings that bound it.

    Names are not unique - the middle blocks of a four-block span share one - but
    they do not need to be, and the cycled descriptions keep adjacent rooms distinct.
    """
    lo_cross = _other_street_name(seg, seg.lo)
    hi_cross = _other_street_name(seg, seg.hi)
    if span_size == 1 or index_in_span == 0:
        return f"{seg.street.name} - Near {lo_cross}"
    if index_in_span == span_size - 1:
        return f"{seg.street.name} - Near {hi_cross}"
    return f"{seg.street.name} - Between {lo_cross} and {hi_cross}"


def _other_street_name(seg: S.Seg, crossing: tuple[int, int]) -> str:
    ew, ns = S.crossings()[crossing]
    return ns.name if seg.street.axis == "ew" else ew.name


# --------------------------------------------------------------------------
# Rooms
# --------------------------------------------------------------------------


def build_rooms() -> list[Room]:
    rooms: list[Room] = []

    for (col, row) in sorted(S.crossings()):
        rooms.append(
            Room(
                stable_id=intersection_stable_id(col, row),
                subzone=S.subzone_at(col, row),
                name=intersection_name(col, row),
                description=intersection_description(col, row),
                environment="intersection",
                map_x=2 * col,
                map_y=2 * row,
                map_symbol="+",
            )
        )

    # Segments, numbered continuously per street key, west-to-east / north-to-south.
    spans: dict[tuple[str, tuple[int, int], tuple[int, int]], list[S.Seg]] = {}
    for seg in S.segments():
        spans.setdefault((seg.street.key, seg.lo, seg.hi), []).append(seg)

    for key, segs in S.numbered_segments().items():
        voice = V.VOICES[key]
        for n, seg in enumerate(segs, start=1):
            span = spans[(seg.street.key, seg.lo, seg.hi)]
            idx = span.index(seg)
            horizontal = seg.street.axis == "ew"
            rooms.append(
                Room(
                    stable_id=f"{PLANE_ZONE}_{S.subzone_at(seg.x2 // 2, seg.y2 // 2)}"
                    f"_room_{key}_{seg.street.abbr}_{n:03d}",
                    subzone=S.subzone_at(seg.x2 // 2, seg.y2 // 2),
                    name=segment_name(seg, idx, len(span)),
                    description=voice.segments[(n - 1) % len(voice.segments)],
                    environment="street_paved",
                    map_x=seg.x2,
                    map_y=seg.y2,
                    map_symbol="-" if horizontal else "|",
                )
            )

    for e in S.EXTRAS:
        frag = LANDMARK_ROOM_KEY.get(e.key, e.key)
        rooms.append(
            Room(
                stable_id=f"{PLANE_ZONE}_{e.subzone}_room_{frag}_001",
                subzone=e.subzone,
                name=e.name,
                description=V.EXTRA_PROSE[e.key],
                environment=e.environment,
                map_x=e.x2,
                map_y=e.y2,
                map_symbol="#",
            )
        )

    return rooms


# --------------------------------------------------------------------------
# Links
# --------------------------------------------------------------------------


def build_links(rooms: list[Room]) -> list[Link]:
    by_cell = {(r.map_x, r.map_y): r for r in rooms}
    links: list[Link] = []

    def join(a: Room, b: Room, direction: str) -> None:
        links.append(Link(a.stable_id, b.stable_id, direction))
        links.append(Link(b.stable_id, a.stable_id, OPPOSITE[direction]))

    # Walk each street end to end, joining consecutive rooms along its line.
    for street in S.STREETS:
        pts = S._crossing_points(street, S.crossings())
        cells: list[tuple[int, int]] = []
        for a, b in pairwise(pts):
            lo = (2 * a, 2 * street.line) if street.axis == "ew" else (2 * street.line, 2 * a)
            cells.append(lo)
            span = [
                s for s in S.segments()
                if s.street.key == street.key
                and s.lo == ((a, street.line) if street.axis == "ew" else (street.line, a))
                and s.hi == ((b, street.line) if street.axis == "ew" else (street.line, b))
            ]
            cells += [(s.x2, s.y2) for s in sorted(span, key=lambda s: (s.x2, s.y2))]
        last = pts[-1]
        cells.append((2 * last, 2 * street.line) if street.axis == "ew"
                     else (2 * street.line, 2 * last))

        forward = "east" if street.axis == "ew" else "south"
        for c1, c2 in pairwise(cells):
            join(by_cell[c1], by_cell[c2], forward)

    # Landmarks, roads out, the station.
    for e in S.EXTRAS:
        join(by_cell[(e.attach_x2, e.attach_y2)], by_cell[(e.x2, e.y2)], e.direction)

    # The Sanitarium's door moves to Derby & Parsonage (decision 6).
    door_col, door_row = S.SANITARIUM_DOOR
    door = by_cell[(2 * door_col, 2 * door_row)]
    links.append(Link(SANITARIUM_ENTRANCE, door.stable_id, "south"))
    links.append(Link(door.stable_id, SANITARIUM_ENTRANCE, "north"))

    # Arkham's only cross-zone walk. The splice deletes every link touching a replaced
    # street room, which includes this pair, so both directions are re-emitted here.
    # `apple_ln_003` keeps its stable_id and therefore its v5 UUID, and link UUIDs are
    # v5 of (from_stable_id, direction), so the re-emitted rows are byte-identical to
    # the deleted ones - the Innsmouth side of the world is unchanged.
    if INNSMOUTH_ATTACH not in {r.stable_id for r in rooms}:
        raise SystemExit(
            f"{INNSMOUTH_ATTACH} is no longer generated - the walk to "
            f"{INNSMOUTH_CAUSEWAY} would break and Innsmouth become unreachable"
        )
    links.append(Link(INNSMOUTH_ATTACH, INNSMOUTH_CAUSEWAY, "north"))
    links.append(Link(INNSMOUTH_CAUSEWAY, INNSMOUTH_ATTACH, "south"))

    # The surviving boarding house, re-attached to the rebuilt Curwen Street.
    # Its own row stays in dev/e2e (and stays absent from unit); only these links
    # and its coordinates are new.
    street = by_cell[BOARDING_HOUSE_ATTACH]
    links.append(Link(street.stable_id, BOARDING_HOUSE, "north"))
    links.append(Link(BOARDING_HOUSE, street.stable_id, "south"))

    return links


# --------------------------------------------------------------------------
# Emission
# --------------------------------------------------------------------------


def _tsv(*fields: str) -> str:
    return "\t".join(fields)


def rooms_tsv(rooms: list[Room]) -> str:
    lines = []
    for r in rooms:
        attributes = json.dumps({"environment": r.environment}, separators=(", ", ": "))
        lines.append(
            _tsv(
                room_uuid(r.stable_id), subzone_uuid(r.subzone), r.stable_id, r.name,
                r.description, attributes, f"{r.map_x:.2f}", f"{r.map_y:.2f}",
                "f", r.map_symbol, "city",
            )
        )
    return "\n".join(lines)


def links_tsv(links: list[Link]) -> str:
    return "\n".join(
        _tsv(link_uuid(x.from_id, x.direction), room_uuid(x.from_id), room_uuid(x.to_id),
             x.direction, "{}")
        for x in links
    )


def subzones_tsv() -> str:
    lines = []
    for stable, (name, description, rules) in NEW_SUBZONES.items():
        lines.append(
            _tsv(subzone_uuid(stable), ZONE_UUID, stable, name, "outdoors", description,
                 json.dumps(rules, separators=(", ", ": ")))
        )
    return "\n".join(lines)


def zone_configurations_tsv() -> str:
    return "\n".join(
        _tsv(zone_config_uuid(s), ZONE_UUID, subzone_uuid(s)) for s in NEW_SUBZONES
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("build/arkham"))
    args = parser.parse_args()

    rooms = build_rooms()
    links = build_links(rooms)

    ids = [r.stable_id for r in rooms]
    if len(set(ids)) != len(ids):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        raise SystemExit(f"duplicate stable_ids: {dupes}")

    seen: set[tuple[str, str]] = set()
    for link in links:
        if (link.from_id, link.direction) in seen:
            raise SystemExit(f"duplicate (from, direction): {link.from_id} {link.direction}")
        seen.add((link.from_id, link.direction))

    # The preserved boarding house occupies a cell too, so it must not land on a
    # generated room - the ASCII renderer would drop one of them without erroring.
    occupied = {(r.map_x, r.map_y) for r in rooms}
    if BOARDING_HOUSE_CELL in occupied:
        raise SystemExit(f"boarding house cell {BOARDING_HOUSE_CELL} collides with a street room")
    if BOARDING_HOUSE_ATTACH not in occupied:
        raise SystemExit(f"boarding house attach cell {BOARDING_HOUSE_ATTACH} has no room")

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "rooms.tsv").write_text(rooms_tsv(rooms) + "\n", encoding="utf-8", newline="\n")
    (args.out / "room_links.tsv").write_text(links_tsv(links) + "\n", encoding="utf-8", newline="\n")
    (args.out / "subzones.tsv").write_text(subzones_tsv() + "\n", encoding="utf-8", newline="\n")
    (args.out / "zone_configurations.tsv").write_text(
        zone_configurations_tsv() + "\n", encoding="utf-8", newline="\n"
    )

    # Coordinate patch for rooms that survive the rebuild but had no coordinates.
    # Every Arkham room must end up non-NULL, or _needs_coordinate_generation fires a
    # zone-wide BFS that overwrites everything authored here (maps.py:112-122).
    (args.out / "preserved_coords.tsv").write_text(
        _tsv(BOARDING_HOUSE, f"{BOARDING_HOUSE_CELL[0]:.2f}",
             f"{BOARDING_HOUSE_CELL[1]:.2f}", "#", "city") + "\n",
        encoding="utf-8", newline="\n",
    )

    print(f"rooms            {len(rooms)}")
    print(f"room_links       {len(links)}")
    print(f"new subzones     {len(NEW_SUBZONES)}")
    print(f"preserved        1  ({BOARDING_HOUSE.rsplit('_room_', 1)[-1]})")
    print(f"written to       {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
