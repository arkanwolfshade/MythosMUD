"""Arkham street-grid spec, derived from the canonical map plate (issue #829).

REVIEW THIS FILE, NOT THE GENERATED SQL.

This module is the human-reviewable representation of ``map.png``: every street,
its axis, its lattice line, and how far it runs. ``scripts/generate_arkham_grid.py``
consumes it and emits 481 rooms and ~1000 links. If the map is wrong, it is wrong
here, in one screen of text, rather than in a thousand tab-separated rows.

Run ``python scripts/arkham_grid_spec.py`` to print the derived city as ASCII and
compare it against the plate.

Lattice
-------
Streets sit on a lattice of ROWS (east-west lines, index 0 northernmost) and
COLS (north-south lines, index 0 westernmost). A street occupies one line and
spans a range of the perpendicular index, inclusive.

Coordinates are emitted at 2x scale so intersections land on even cells and
mid-block segments on odd ones. This is not cosmetic: ``AsciiMapRenderer`` does
``int(map_x)`` and then last-writer-wins on collision, so a fractional coordinate
would silently delete a room.
"""

from __future__ import annotations

from collections import Counter
from itertools import pairwise
from typing import NamedTuple

# --------------------------------------------------------------------------
# Lattice lines
# --------------------------------------------------------------------------

# East-west lines, north to south.
ROWS: dict[str, int] = {
    "apple": 0,  # Apple Lane - the north lane; carries the Innsmouth road
    "derby": 1,
    "curwen": 2,
    "hyde": 3,  # Whateley St. continues this line east of Independence Square
    "armitage": 4,
    "high_ln": 5,
    "water": 6,
    "bridge": 7,  # the Miskatonic: West / Garrison / Peabody bridge rooms only
    "river": 8,  # Aylesbury St. continues this line west
    "church": 9,
    "main": 10,
    "crane": 11,  # Crane St. (west) and Lich St. (mid-east) share this line
    "college": 12,
    "pickman": 13,
    "high_st": 14,
    "saltonstall": 15,
    "miskatonic": 16,
    "washington": 17,
}

# North-south lines, west to east. Several carry a different name north and
# south of the river - the plate labels them separately.
COLS: dict[str, int] = {
    "hill": 0,
    "boundary": 1,
    "west": 2,
    "brown": 3,
    "jenkin": 4,
    "gedney": 5,
    "garrison": 6,
    "parsonage": 7,
    "walnut": 8,
    "peabody": 9,
    "dyer": 10,  # Powder Mills St. south of the river; High Alley also sits here
    "federal": 11,  # French Hill St. south of the river
    "noyes": 12,  # Sentinel St. south of the river
    "halsey": 13,  # East St. south of the river
}

R = ROWS
C = COLS


class Street(NamedTuple):
    """One named street: a line on the lattice and the span it runs."""

    key: str  # id fragment, e.g. "derby" -> ..._room_derby_st_001
    name: str  # display name, e.g. "Derby Street"
    abbr: str  # id suffix: st | ln | ave
    axis: str  # "ew" or "ns"
    line: int  # ROWS[...] for ew, COLS[...] for ns
    start: int  # first crossing (inclusive), perpendicular index
    end: int  # last crossing (inclusive)


# --------------------------------------------------------------------------
# The streets
# --------------------------------------------------------------------------

STREETS: list[Street] = [
    # --- east-west, north of the Miskatonic -------------------------------
    Street("apple", "Apple Lane", "ln", "ew", R["apple"], C["west"], C["halsey"]),
    Street("derby", "Derby Street", "st", "ew", R["derby"], C["west"], C["halsey"]),
    Street("curwen", "Curwen Street", "st", "ew", R["curwen"], C["west"], C["halsey"]),
    Street("hyde", "Hyde Street", "st", "ew", R["hyde"], C["west"], C["peabody"]),
    Street("whateley", "Whateley Street", "st", "ew", R["hyde"], C["federal"], C["halsey"]),
    # Armitage runs one column further east than Hyde: Independence Square blocks
    # Hyde, but the square's southern edge is above Armitage, so it continues to
    # Dyer and gives High Alley its northern T-junction.
    Street("armitage", "Armitage Street", "st", "ew", R["armitage"], C["west"], C["dyer"]),
    Street("high_ln", "High Lane", "ln", "ew", R["high_ln"], C["west"], C["dyer"]),
    Street("water", "Water Street", "st", "ew", R["water"], C["west"], C["halsey"]),
    # --- east-west, south of the Miskatonic -------------------------------
    # The plate's "Aylesbury St." labels the western continuation of River Street,
    # which carries the road to Dunwich. Hill St. does not reach this far north, so
    # there is no junction out there to model - the road out IS the terminus room.
    Street("river", "River Street", "st", "ew", R["river"], C["boundary"], C["halsey"]),
    Street("church", "Church Street", "st", "ew", R["church"], C["boundary"], C["halsey"]),
    Street("main", "Main Street", "st", "ew", R["main"], C["hill"], C["halsey"]),
    Street("crane", "Crane Street", "st", "ew", R["crane"], C["boundary"], C["west"]),
    Street("lich", "Lich Street", "st", "ew", R["crane"], C["parsonage"], C["walnut"]),
    Street("college", "College Street", "st", "ew", R["college"], C["boundary"], C["halsey"]),
    Street("pickman", "Pickman Street", "st", "ew", R["pickman"], C["hill"], C["halsey"]),
    Street("high_st", "High Street", "st", "ew", R["high_st"], C["hill"], C["halsey"]),
    Street("saltonstall", "Saltonstall Street", "st", "ew", R["saltonstall"], C["hill"], C["halsey"]),
    Street("miskatonic", "Miskatonic Avenue", "ave", "ew", R["miskatonic"], C["hill"], C["halsey"]),
    Street("washington", "Washington Street", "st", "ew", R["washington"], C["hill"], C["halsey"]),
    # --- north-south, north of the Miskatonic -----------------------------
    Street("brown", "Brown Street", "st", "ns", C["brown"], R["apple"], R["water"]),
    Street("jenkin", "Jenkin Street", "st", "ns", C["jenkin"], R["apple"], R["water"]),
    Street("gedney", "Gedney Street", "st", "ns", C["gedney"], R["apple"], R["water"]),
    Street("dyer", "Dyer Street", "st", "ns", C["dyer"], R["derby"], R["curwen"]),
    Street("high_alley", "High Alley", "ln", "ns", C["dyer"], R["armitage"], R["high_ln"]),
    Street("federal", "Federal Street", "st", "ns", C["federal"], R["derby"], R["hyde"]),
    Street("noyes", "Noyes Street", "st", "ns", C["noyes"], R["derby"], R["hyde"]),
    Street("halsey", "Halsey Street", "st", "ns", C["halsey"], R["apple"], R["water"]),
    # --- north-south, crossing the river (the three bridges) --------------
    Street("west", "West Street", "st", "ns", C["west"], R["apple"], R["washington"]),
    Street("garrison", "Garrison Street", "st", "ns", C["garrison"], R["apple"], R["washington"]),
    Street("peabody", "Peabody Avenue", "ave", "ns", C["peabody"], R["apple"], R["washington"]),
    # --- north-south, south of the Miskatonic -----------------------------
    Street("hill", "Hill Street", "st", "ns", C["hill"], R["main"], R["washington"]),
    Street("boundary", "Boundary Street", "st", "ns", C["boundary"], R["river"], R["washington"]),
    # Parsonage is two streets sharing a name and a column: it starts at Derby
    # (the Sanatorium occupies the block north of it) and stops at Water, because
    # it is NOT one of the three bridges. It resumes on the south bank at River.
    Street("parsonage", "Parsonage Street", "st", "ns", C["parsonage"], R["derby"], R["water"]),
    Street("parsonage", "Parsonage Street", "st", "ns", C["parsonage"], R["river"], R["washington"]),
    Street("walnut", "Walnut Street", "st", "ns", C["walnut"], R["church"], R["washington"]),
    Street("powder", "Powder Mills Street", "st", "ns", C["dyer"], R["college"], R["washington"]),
    Street("frenchhill", "French Hill Street", "st", "ns", C["federal"], R["college"], R["washington"]),
    Street("sentinel", "Sentinel Street", "st", "ns", C["noyes"], R["college"], R["washington"]),
    Street("east", "East Street", "st", "ns", C["halsey"], R["river"], R["washington"]),
]

# The Sanatorium occupies the two blocks on Derby between Garrison and Peabody,
# entrance at Derby & Parsonage. Parsonage therefore does not run north of Derby.
SANITARIUM_DOOR = (C["parsonage"], R["derby"])

BRIDGE_COLS = (C["west"], C["garrison"], C["peabody"])

# How many city blocks lie between two adjacent crossings on a street.
#
# The default is the lattice distance: the lattice already encodes physical
# block spacing, so a street running four columns covers four blocks and gets
# four mid-block segment rooms.
#
# Overrides exist only where a street skips a column that does not exist in its
# half of the city, so the lattice distance overstates the real block count.
# Key: (street key, lower perpendicular index, higher perpendicular index).
BLOCKS: dict[tuple[str, int, int], int] = {
    # Walnut St. exists only south of the river. Every northern east-west street
    # therefore runs Parsonage -> Peabody as ONE block, not two.
    ("derby", C["parsonage"], C["peabody"]): 1,
    ("curwen", C["parsonage"], C["peabody"]): 1,
    ("hyde", C["parsonage"], C["peabody"]): 1,
    ("armitage", C["parsonage"], C["peabody"]): 1,
    ("high_ln", C["parsonage"], C["peabody"]): 1,
    ("water", C["parsonage"], C["peabody"]): 1,
    # Apple Lane past the Sanatorium. Parsonage does not reach this far north,
    # so the lattice says three; the plate - and the Sanatorium's two-block
    # frontage, which is the calibration for the whole map - says two.
    ("apple", C["garrison"], C["peabody"]): 2,
    # The Miskatonic occupies a whole lattice row of its own, so Water -> River is
    # two lattice steps. Each bridge is ONE room spanning the water, not two.
    ("west", R["water"], R["river"]): 1,
    ("garrison", R["water"], R["river"]): 1,
    ("peabody", R["water"], R["river"]): 1,
}


def blocks_between(street: Street, lo: int, hi: int) -> int:
    """City blocks between two adjacent crossings on ``street``."""
    return BLOCKS.get((street.key, lo, hi), hi - lo)


# --------------------------------------------------------------------------
# Sub-zone partition (regional)
# --------------------------------------------------------------------------


class Extra(NamedTuple):
    """A room that is not on the street lattice: a landmark, a road out, the station."""

    key: str
    name: str
    subzone: str
    environment: str
    x2: int  # 2x coordinate, hand-placed on a free cell
    y2: int
    attach_x2: int  # the room it hangs off
    attach_y2: int
    direction: str  # direction FROM the attach room TO this one


# Hand-placed, because ten rooms do not warrant a placement algorithm and because
# each one answers to the plate rather than to the lattice. Every cell here is
# checked for collision by test_arkham_grid_spec.py along with the street rooms.
EXTRAS: list[Extra] = [
    # --- roads out of town (decision 4) -----------------------------------
    Extra("road_to_dunwich", "The Dunwich Road", "rivertown", "outdoors",
          0, 16, 2, 16, "west"),
    Extra("road_to_boston", "The Boston Road", "lowersouthside", "outdoors",
          -2, 34, 0, 34, "west"),
    Extra("road_to_kingsport", "The Kingsport Road", "lowersouthside", "outdoors",
          18, 36, 18, 34, "south"),
    # --- the railway (decision 21) ----------------------------------------
    Extra("arkham_station", "Arkham Station", "rivertown", "indoors",
          8, 14, 8, 12, "south"),
    Extra("road_to_salem", "The Boston & Maine Line", "rivertown", "outdoors",
          6, 14, 8, 14, "west"),
    # --- outdoor landmarks, one room each in its own sub-zone (decision 3) --
    # The Island is reached by a river stair, not a bridge (decision 12).
    Extra("the_island", "The Island", "the_island", "outdoors",
          11, 14, 11, 12, "down"),
    Extra("independence_square", "Independence Square", "independence_square", "outdoors",
          20, 5, 20, 4, "south"),
    Extra("hangmans_hill", "Hangman's Hill", "hangmans_hill", "outdoors",
          -2, 20, 0, 20, "west"),
    Extra("wooded_graveyard", "The Wooded Graveyard", "wooded_graveyard", "outdoors",
          -2, 18, -2, 20, "north"),
    Extra("old_arkham_graveyard", "Old Arkham Graveyard", "old_arkham_graveyard", "outdoors",
          15, 21, 15, 22, "north"),
]

LANDMARK_SUBZONES = (
    "the_island",
    "independence_square",
    "hangmans_hill",
    "wooded_graveyard",
    "old_arkham_graveyard",
)


def subzone_at(col: int, row: int) -> str:
    """Which sub-zone a lattice position belongs to.

    Regional rather than per-street, so a long cross-town street changes
    sub-zone as it crosses the city - Derby runs through northside and uptown.
    """
    if row in (R["water"], R["bridge"], R["river"]):
        return "rivertown"
    if row < R["water"]:  # north of the Miskatonic
        return "uptown" if col > C["peabody"] else "northside"
    # south of the Miskatonic
    if col >= C["halsey"]:
        return "easttown"
    if col > C["peabody"]:
        return "frenchhill"
    if row <= R["crane"]:  # church, main, crane / lich
        return "campus" if col <= C["west"] else "downtown"
    if row == R["college"]:
        return "campus"
    if row == R["pickman"]:
        return "merchant"
    return "lowersouthside"


SUBZONE_LETTER = {
    "northside": "N",
    "uptown": "U",
    "rivertown": "R",
    "downtown": "D",
    "campus": "C",
    "merchant": "M",
    "frenchhill": "F",
    "easttown": "E",
    "lowersouthside": "L",
}


# --------------------------------------------------------------------------
# Derivation
# --------------------------------------------------------------------------


def crossings() -> dict[tuple[int, int], tuple[Street, Street]]:
    """Every lattice position (col, row) where an EW and an NS street meet."""
    ew = [s for s in STREETS if s.axis == "ew"]
    ns = [s for s in STREETS if s.axis == "ns"]
    out: dict[tuple[int, int], tuple[Street, Street]] = {}
    for a in ew:
        for b in ns:
            if a.start <= b.line <= a.end and b.start <= a.line <= b.end:
                out[(b.line, a.line)] = (a, b)
    return out


class Seg(NamedTuple):
    """One mid-block street room: a single city block of a named street."""

    street: Street
    x2: int  # 2x lattice coordinate
    y2: int
    lo: tuple[int, int]  # the crossing at the lower end (col, row)
    hi: tuple[int, int]  # the crossing at the higher end


def segments() -> list[Seg]:
    """Every city block of every street, one room each."""
    x = crossings()
    out: list[Seg] = []
    for s in STREETS:
        if s.axis == "ew":
            pts = sorted(c for c in range(s.start, s.end + 1) if (c, s.line) in x)
        else:
            pts = sorted(r for r in range(s.start, s.end + 1) if (s.line, r) in x)
        for a, b in pairwise(pts):
            n = blocks_between(s, a, b)
            span = 2 * (b - a)
            pos = [round(2 * a + (k + 1) * span / (n + 1)) for k in range(n)]
            if len(set(pos)) != n:
                raise ValueError(f"{s.key} {a}->{b}: {n} blocks do not fit in {span} cells")
            for p in pos:
                if s.axis == "ew":
                    out.append(Seg(s, p, 2 * s.line, (a, s.line), (b, s.line)))
                else:
                    out.append(Seg(s, 2 * s.line, p, (s.line, a), (s.line, b)))
    return out


def numbered_segments() -> dict[str, list[Seg]]:
    """Segments grouped by street key, ordered west-to-east / north-to-south.

    Streets split by the river (Parsonage) share a key, so numbering runs
    continuously across the gap - decision 25.
    """
    by_key: dict[str, list[Seg]] = {}
    for seg in segments():
        by_key.setdefault(seg.street.key, []).append(seg)
    for segs in by_key.values():
        ew = segs[0].street.axis == "ew"
        segs.sort(key=lambda s: (s.x2, s.y2) if ew else (s.y2, s.x2))
    return by_key


def _crossing_points(s: Street, x: dict[tuple[int, int], tuple[Street, Street]]) -> list[int]:
    if s.axis == "ew":
        return sorted(c for c in range(s.start, s.end + 1) if (c, s.line) in x)
    return sorted(r for r in range(s.start, s.end + 1) if (s.line, r) in x)


def render() -> str:
    """ASCII render of the derived lattice, for comparison against map.png.

    Letters are sub-zones. Digits on a horizontal run are the block count for
    that span - that is, how many mid-block rooms sit between those two
    crossings. A run of dashes with no digit is a single block.
    """
    x = crossings()
    max_col, max_row = max(COLS.values()), max(ROWS.values())
    w = 4
    grid = [[" "] * (w * (max_col + 1)) for _ in range(max_row + 1)]
    vert = [[" "] * (max_col + 1) for _ in range(max_row + 1)]

    for col, row in x:
        grid[row][col * w] = SUBZONE_LETTER[subzone_at(col, row)]

    for s in STREETS:
        pts = _crossing_points(s, x)
        for a, b in pairwise(pts):
            n = blocks_between(s, a, b)
            if s.axis == "ew":
                lo, hi = a * w, b * w
                for i in range(lo + 1, hi):
                    grid[s.line][i] = "-"
                if n != 1:
                    grid[s.line][(lo + hi) // 2] = str(n)
            else:
                for rr in range(a, b):
                    vert[rr][s.line] = "|"

    lines: list[str] = []
    for row in range(max_row + 1):
        rname = next(k for k, v in ROWS.items() if v == row)
        lines.append(f"{''.join(grid[row]).rstrip():<56} {rname}")
        if row < max_row:
            lines.append("".join(c + "   " for c in vert[row]).rstrip())
    header = " ".join(f"{k[:3]:<3}" for k in COLS)
    return f"cols: {header}\n\n" + "\n".join(lines)


def summary() -> str:
    x = crossings()
    seg = segments()
    per_sz: Counter[str] = Counter(subzone_at(c, r) for c, r in x)
    for s in seg:
        per_sz[subzone_at(s.x2 // 2, s.y2 // 2)] += 1

    for e in EXTRAS:
        per_sz[e.subzone] += 1

    cells: Counter[tuple[int, int]] = Counter()
    for col, row in x:
        cells[(2 * col, 2 * row)] += 1
    for s in seg:
        cells[(s.x2, s.y2)] += 1
    for e in EXTRAS:
        cells[(e.x2, e.y2)] += 1
    clashes = {k: v for k, v in cells.items() if v > 1}

    body = "\n".join(f"  {k:<22} {v}" for k, v in sorted(per_sz.items(), key=lambda i: -i[1]))
    out = (
        f"streets:       {len(STREETS)}\n"
        f"intersections: {len(x)}\n"
        f"segments:      {len(seg)}\n"
        f"extras:        {len(EXTRAS)}  (landmarks, roads out, the station)\n"
        f"TOTAL ROOMS:   {len(x) + len(seg) + len(EXTRAS)}\n\n"
        f"per sub-zone:\n{body}\n\n"
        f"coordinate collisions: {len(clashes)}"
    )
    if clashes:
        out += "\n" + "\n".join(f"  {k} x{v}" for k, v in sorted(clashes.items()))
    return out


if __name__ == "__main__":
    print(render())
    print()
    print(summary())
