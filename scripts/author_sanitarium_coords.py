"""Give the Sanitarium's interior rooms map coordinates (#829).

Not cosmetic. `_needs_coordinate_generation` (server/api/maps.py:112-122) triggers a
zone-wide BFS rewrite if *any* room in `earth_arkhamcity` lacks coordinates, and that
BFS would overwrite the 481 street coordinates authored from the plate. The Sanitarium
is the only part of Arkham left with NULLs, so it has to be filled for the street grid
to survive its first map request.

The interior is laid out by walking its own exit graph from the entrance, using the
same direction deltas the server generator uses (north = -y, south = +y, east = +x,
west = -x). It is then translated into a region well clear of the street lattice, so
the two never share a cell when the ASCII renderer plots a whole zone at once.

Three wrinkles the street grid does not have:

* `up`/`down` move nothing in the server's convention, so the tutorial bedroom would
  land on top of the foyer. Vertical links get a deliberate offset instead.
* Four rooms are deliberately isolated (an elevator, a kitchen, an accessible toilet,
  a secret entrance) and cannot be reached by walking. They are parked on free cells.
* The graph is not planar, so a naive BFS can still collide. Collisions are detected
  and nudged rather than ignored - the renderer resolves a shared cell by dropping a
  room silently.
* Rooms occupy ADJACENT cells. The minimap viewport is counted in cells, so any extra
  spacing between rooms directly reduces how much of the building fits on screen.

    python scripts/author_sanitarium_coords.py [--check]
"""

from __future__ import annotations

import argparse
import re
from collections import deque
from pathlib import Path

ENVS = ("dev", "unit", "e2e")
DML = "data/db/mythos_{env}_dml.sql"

SUBZONE = "_sanitarium_"
ENTRANCE = "earth_arkhamcity_sanitarium_room_foyer_entrance_001"

# Far clear of the street lattice, which spans roughly x in [-2, 26], y in [0, 36].
ORIGIN_X, ORIGIN_Y = 100, 0

# ONE cell per room. This must stay 1.
#
# The minimap viewport is measured in CELLS, not rooms: `_auto_center_viewport` centres on
# `player_x - viewport_width // 2` and the default minimap `size` is 5. Spacing rooms two
# cells apart therefore shrinks a 5x5 minimap from 5 rooms per axis to 3, which is what
# made the Sanitarium render as a stub of itself.
#
# A 2x lattice was tried here to stop interior exits passing over other rooms. It did not
# work - the same six crossings occur at either spacing, because they come from the room
# graph itself (a corridor and its side rooms share a direction), not from packing. So it
# bought nothing and cost the minimap two thirds of its range.
STEP = 1

DELTA = {
    "north": (0, -STEP),
    "south": (0, STEP),
    "east": (STEP, 0),
    "west": (-STEP, 0),
    # `up`/`down` do not move in the server's BFS, which would stack rooms on one cell.
    # They get TWO rows rather than one so a stacked room lands clear of the row that a
    # corridor's own side rooms occupy. At one row the tutorial bedroom took a side room's
    # square, and the nudge-on-collision then pushed five rooms east in a cascade, leaving
    # each of their corridor exits spanning two cells. Vertical exits are never drawn on
    # the ASCII map, so the longer span here costs nothing visually.
    "up": (0, -2 * STEP),
    "down": (0, 2 * STEP),
}


def parse_block(text: str, table: str) -> tuple[int, int, list[list[str]]]:
    m = re.search(rf"^COPY [\w.]+\.{table} \([^)]*\) FROM stdin;\n", text, re.M)
    if not m:
        raise SystemExit(f"no COPY block for {table}")
    end = text.index("\n\\.", m.end())
    rows = [ln.split("\t") for ln in text[m.end() : end + 1].rstrip("\n").split("\n")]
    return m.end(), end + 1, rows


def assign(rooms: list[list[str]], links: list[list[str]]) -> dict[str, tuple[int, int]]:
    """Walk the Sanitarium's own exit graph and hand every room a unique cell."""
    by_uuid = {r[0]: r[2] for r in rooms}
    interior = {r[0] for r in rooms if SUBZONE in r[2]}
    adjacency: dict[str, list[tuple[str, str]]] = {u: [] for u in interior}
    for link in links:
        if link[1] in interior and link[2] in interior:
            adjacency[link[1]].append((link[3], link[2]))

    start = next(u for u, s in by_uuid.items() if s == ENTRANCE)
    placed: dict[str, tuple[int, int]] = {start: (0, 0)}
    taken: set[tuple[int, int]] = {(0, 0)}

    queue = deque([start])
    while queue:
        cur = queue.popleft()
        cx, cy = placed[cur]
        for direction, nxt in sorted(adjacency[cur]):
            if nxt in placed:
                continue
            dx, dy = DELTA.get(direction, (1, 0))
            cell = (cx + dx, cy + dy)
            # Non-planar graph: nudge east until the square is free rather than
            # letting two rooms share one and lose one to the renderer.
            while cell in taken:
                cell = (cell[0] + STEP, cell[1])
            placed[nxt] = cell
            taken.add(cell)
            queue.append(nxt)

    # The four deliberately isolated rooms are unreachable by walking; park them in a
    # row below the mapped interior so they still carry non-NULL coordinates.
    orphan_y = max(y for _, y in placed.values()) + STEP * 2
    for i, uuid_ in enumerate(sorted(interior - set(placed))):
        placed[uuid_] = (i * STEP * 2, orphan_y)

    return {u: (ORIGIN_X + x, ORIGIN_Y + y) for u, (x, y) in placed.items()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    for env in ENVS:
        path = Path(DML.format(env=env))
        text = path.read_bytes().decode("utf-8")
        start, end, rooms = parse_block(text, "rooms")
        _, _, links = parse_block(text, "room_links")

        coords = assign(rooms, links)
        if len(set(coords.values())) != len(coords):
            raise SystemExit("sanitarium coordinate collision")

        filled = 0
        for row in rooms:
            if row[0] in coords:
                x, y = coords[row[0]]
                row[6], row[7] = f"{x}.00", f"{y}.00"
                # map_symbol is left NULL on purpose: AsciiMapRenderer auto-assigns a
                # symbol from the room's environment when none is stored, and an explicit
                # '#' on every room overrides that with a wall of identical marks.
                row[10] = "interior"
                filled += 1

        nulls = [r[2] for r in rooms if r[6] == "\\N" and r[2].startswith("earth_arkhamcity_")]
        payload = "\n".join("\t".join(r) for r in rooms) + "\n"
        if not args.check:
            path.write_bytes((text[:start] + payload + text[end:]).encode("utf-8"))
        print(f"{env:<5} filled {filled} sanitarium rooms; arkham rooms still NULL: {len(nulls)}")
        if nulls:
            print("   ", nulls[:5])

    print("(dry run)" if args.check else "written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
