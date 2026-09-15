"""Exit geometry for the ASCII map.

Extracted from `ascii_map_renderer.py` to satisfy the module-length limit, following the
same split as `async_persistence_room_loader.py`. This half answers one question - which
character, if any, joins two cells - and holds no renderer state, so every function here
is pure.

`AsciiMapRenderer` keeps thin methods delegating to these, because the method names are
referenced by `docs/testing/map-regression-tests.md` and by the existing renderer tests.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import cast

# These mirror the shapes AsciiMapRenderer builds, but as Mapping rather than dict.
# Mapping is covariant in its value type, so the renderer's concrete dict form is
# assignable here without this module restating the loose value type the project bans.
# Nothing here needs more: values are only compared for equality or isinstance-checked.
ExitInfo = Mapping[str, object]
ExitLookup = Mapping[tuple[int, int], Mapping[str, ExitInfo]]
Grid = Mapping[tuple[int, int], Mapping[str, object] | str]

# Opposite of each direction, for deciding whether an exit is bidirectional.
REVERSE_DIRECTIONS: dict[str, str] = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
    "northeast": "southwest",
    "northwest": "southeast",
    "southeast": "northwest",
    "southwest": "northeast",
    "up": "down",
    "down": "up",
    "in": "out",
    "out": "in",
}


def reverse_direction(direction: str) -> str:
    """Opposite of `direction`, or "" when it has none."""
    return REVERSE_DIRECTIONS.get(direction.lower(), "")


def horizontal_exit_char_between(
    east_exit: ExitInfo | None,
    west_exit_back: ExitInfo | None,
    next_x: int,
    y: int,
    x: int,
) -> str | None:
    """Return the horizontal exit character (—, >, or <) given east/west exit state, or None."""
    if east_exit and east_exit.get("target") == (next_x, y):
        if west_exit_back and west_exit_back.get("target") == (x, y):
            return "—"  # em dash, bidirectional
        return ">"
    if west_exit_back and west_exit_back.get("target") == (x, y):
        return "<"
    return None


def vertical_exit_char_between(
    south_exit: ExitInfo | None,
    north_exit_back: ExitInfo | None,
    next_y: int,
    x: int,
    y: int,
) -> str | None:
    """Return the vertical exit character (|, v, or ^) given south/north exit state, or None."""
    if south_exit and south_exit.get("target") == (x, next_y):
        if north_exit_back and north_exit_back.get("target") == (x, y):
            return "|"  # bidirectional
        return "v"
    if north_exit_back and north_exit_back.get("target") == (x, y):
        return "^"
    return None


def get_horizontal_exit_char(
    x: int,
    y: int,
    exit_from: ExitLookup,
    grid: Grid,
    viewport_x: int,
    viewport_width: int,
) -> str | None:
    """Exit character shown immediately after the room at (x, y), or None."""
    next_x = x + 1
    if next_x >= viewport_x + viewport_width:
        return None
    if not isinstance(grid.get((next_x, y)), dict):
        return None
    room_exits = exit_from.get((x, y), {})
    next_exits = exit_from.get((next_x, y), {})
    return horizontal_exit_char_between(room_exits.get("east"), next_exits.get("west"), next_x, y, x)


def get_vertical_exit_char(
    x: int,
    y: int,
    exit_from: ExitLookup,
    grid: Grid,
    viewport_y: int,
    viewport_height: int,
) -> str | None:
    """Exit character shown on the row between (x, y) and the room below it, or None."""
    next_y = y + 1
    if next_y >= viewport_y + viewport_height:
        return None
    if not isinstance(grid.get((x, next_y), " "), dict):
        return None
    room_exits = exit_from.get((x, y), {})
    next_exits = exit_from.get((x, next_y), {})
    return vertical_exit_char_between(room_exits.get("south"), next_exits.get("north"), next_y, x, y)


def build_departures(
    rooms: Sequence[Mapping[str, object]],
) -> dict[tuple[int, int], frozenset[str]]:
    """Directions in which each room has an exit leading OUT of the loaded area.

    A map request is scoped to one sub-zone, so the Sanitarium's rooms are simply absent
    when you are standing on Derby Street. `_resolve_exit_target` cannot place such an
    exit and drops it, which means the one way into the building is invisible on the map
    - the player sees a plain street corner with no hint there is a door.

    These are the exits worth marking: the target exists in the world, it is just not on
    this sheet of paper.
    """
    known: set[str] = set()
    positions: dict[str, tuple[int, int]] = {}
    for room in rooms:
        room_id = str(room.get("id") or room.get("stable_id") or "")
        if not room_id:
            continue
        known.add(room_id)
        map_x, map_y = room.get("map_x"), room.get("map_y")
        if isinstance(map_x, int | float) and isinstance(map_y, int | float):
            positions[room_id] = (int(map_x), int(map_y))

    departures: dict[tuple[int, int], set[str]] = {}
    for room in rooms:
        room_id = str(room.get("id") or room.get("stable_id") or "")
        cell = positions.get(room_id)
        if cell is None:
            continue
        exits = room.get("exits")
        if not isinstance(exits, Mapping):
            continue
        for direction, target in cast(Mapping[str, object], exits).items():
            if direction not in REVERSE_DIRECTIONS:
                continue
            target_id = str(target) if target else ""
            if target_id and target_id not in known:
                departures.setdefault(cell, set()).add(direction)
    return {cell: frozenset(dirs) for cell, dirs in departures.items()}


def build_exit_bridges(
    exit_from: ExitLookup,
) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
    """Cells lying strictly between two rooms joined by a single exit.

    A grid cell is not always a room. A city block can be longer than one cell - in
    Arkham a street may run several columns before the next cross street - so two
    connected rooms are not necessarily neighbours on the grid. Without filling the
    cells between them the map draws nothing at all there, and rooms that are a single
    step apart in game appear disconnected.

    Returns (horizontal, vertical) cell sets, for east/west and north/south spans.
    """
    horizontal: set[tuple[int, int]] = set()
    vertical: set[tuple[int, int]] = set()
    for (x, y), exits in exit_from.items():
        for direction, info in exits.items():
            target = info.get("target")
            if not isinstance(target, tuple):
                continue
            target_x, target_y = cast(tuple[int, int], target)
            if direction in ("east", "west") and target_y == y and abs(target_x - x) > 1:
                step = 1 if target_x > x else -1
                horizontal.update((cx, y) for cx in range(x + step, target_x, step))
            elif direction in ("north", "south") and target_x == x and abs(target_y - y) > 1:
                step = 1 if target_y > y else -1
                vertical.update((x, cy) for cy in range(y + step, target_y, step))
    return horizontal, vertical
