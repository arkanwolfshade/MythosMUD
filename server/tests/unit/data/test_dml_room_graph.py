"""Guards the `rooms` / `room_links` seed data in `data/db/seed.sql` against the class of
authoring mistake behind #823: one-way exits, a reciprocal that points at the wrong room, and
duplicate `(from_room_id, direction)` rows that silently collide under the DDL's own
`UNIQUE (from_room_id, direction)` constraint.

No database is needed -- this parses the `COPY ... FROM stdin` blocks directly out of the
`pg_dump`-formatted seed file (real tab separators, `\\N` for NULL, terminated by a bare `\\.`
line), so it runs in milliseconds under `make test` and catches the mistake at the point it's
actually made: in the text file, before it ever reaches a database.

`_KNOWN_ISOLATED_ROOMS` is a baseline, same discipline as `.basedpyright/baseline.json`: it may
only shrink as rooms are wired up (see #824), never grow to paper over a new orphan.

Since #811, `data/db/seed.sql` is the single schema-agnostic seed source loaded into all three
environments (mythos_dev / mythos_unit / mythos_e2e) -- there is no longer a per-environment
file to diverge, so the cross-environment comparison tests this module used to carry (byte-
identical dev/e2e, unit-matches-dev-except-the-Inn) no longer apply and were removed.
"""

from __future__ import annotations

import re
from pathlib import Path

from server.utils.project_paths import get_project_root

_OPPOSITE = {"north": "south", "south": "north", "east": "west", "west": "east", "up": "down", "down": "up"}

# Pre-existing, fully isolated (zero room_links) rooms, unrelated to #823's broken-reciprocal bug.
# Each is an administrative/instanced stub: an elevator, a secret entrance, or a single-room plane
# anchor reached by a mechanic other than walking. This list may only shrink -- adding a room here
# to silence a new orphan defeats the guard. (The Innsmouth Waterfront Pier was on this list until
# #824 wired it into the map; it is intentionally absent now. #829 removed five more: four Arkham
# intersections that the street-grid rebuild replaced outright, and derby_halsey, which the rebuild
# finally connected. Only the four sanitarium stubs and two single-room plane anchors remain.)
_KNOWN_ISOLATED_ROOMS = frozenset(
    {
        "earth_arkhamcity_sanitarium_room_accessible_toilet_001",
        "earth_arkhamcity_sanitarium_room_elevator_001",
        "earth_arkhamcity_sanitarium_room_kitchen_001",
        "earth_arkhamcity_sanitarium_room_secret_entrance_001",
        "limbo_death_void",
        "yeng_katmandu_palace_palace_ground_001",
    }
)

RoomRow = tuple[str, ...]
LinkRow = tuple[str, ...]

_COPY_RE = re.compile(r"^COPY (\w+) \(")


def _parse_copy_blocks(text: str) -> dict[str, list[tuple[str, ...]]]:
    """Return every `COPY <schema>.<table> (...) FROM stdin; ... \\.` block, keyed by table name."""
    blocks: dict[str, list[tuple[str, ...]]] = {}
    table: str | None = None
    rows: list[tuple[str, ...]] = []
    for line in text.split("\n"):
        if table is not None:
            if line == "\\.":
                blocks[table] = rows
                table = None
                rows = []
                continue
            rows.append(tuple(line.split("\t")))
            continue
        match = _COPY_RE.match(line)
        if match:
            table = match.group(1)
            rows = []
    return blocks


def _dml_path() -> Path:
    return get_project_root() / "data" / "db" / "seed.sql"


def _load() -> tuple[list[RoomRow], list[LinkRow]]:
    text = _dml_path().read_text(encoding="utf-8")
    blocks = _parse_copy_blocks(text)
    return blocks["rooms"], blocks["room_links"]


def _stable_id_by_room_id(rooms: list[RoomRow]) -> dict[str, str]:
    return {row[0]: row[2] for row in rooms}


def test_dml_file_parses_and_is_nonempty() -> None:
    rooms, links = _load()
    assert len(rooms) > 100, f"suspiciously few rooms parsed ({len(rooms)})"
    assert len(links) > 100, f"suspiciously few room_links parsed ({len(links)})"


def test_no_duplicate_from_room_direction() -> None:
    """Mirrors the DDL's own `UNIQUE (from_room_id, direction)` constraint at the text level."""
    _, links = _load()
    seen: dict[tuple[str, str], str] = {}
    for row in links:
        _link_id, from_room_id, _to_room_id, direction, *_ = row
        key = (from_room_id, direction)
        assert key not in seen, (
            f"duplicate room_links row for from_room_id={from_room_id} direction={direction} "
            f"(ids {seen[key]} and {row[0]})"
        )
        seen[key] = row[0]


def test_no_dangling_room_link_references() -> None:
    rooms, links = _load()
    room_ids = {row[0] for row in rooms}
    for _link_id, from_room_id, to_room_id, _direction, *_ in links:
        assert from_room_id in room_ids, f"room_links {_link_id} from_room_id {from_room_id} not a room"
        assert to_room_id in room_ids, f"room_links {_link_id} to_room_id {to_room_id} not a room"


def test_every_room_link_has_an_exact_reciprocal() -> None:
    """The #823 bug class: a one-way exit, or a reciprocal that points at the wrong room."""
    rooms, links = _load()
    stable_id = _stable_id_by_room_id(rooms)
    by_from_direction = {(row[1], row[3]): row[2] for row in links}
    problems: list[str] = []
    for _link_id, from_room_id, to_room_id, direction, *_ in links:
        opposite = _OPPOSITE.get(direction)
        if opposite is None:
            problems.append(f"unknown direction {direction!r} on link from {stable_id.get(from_room_id)}")
            continue
        back_target = by_from_direction.get((to_room_id, opposite))
        from_name = stable_id.get(from_room_id, from_room_id)
        to_name = stable_id.get(to_room_id, to_room_id)
        if back_target is None:
            problems.append(f"{from_name} --{direction}--> {to_name} has no reciprocal ({to_name} --{opposite}--> ???)")
        elif back_target != from_room_id:
            back_name = stable_id.get(back_target, back_target)
            reciprocal = f"{to_name} --{opposite}--> {back_name} points elsewhere"
            problems.append(f"{from_name} --{direction}--> {to_name}, but the reciprocal {reciprocal}")
    assert not problems, f"{len(problems)} broken reciprocal(s):\n" + "\n".join(problems)


def test_no_isolated_rooms_beyond_the_known_baseline() -> None:
    rooms, links = _load()
    connected: set[str] = set()
    for _link_id, from_room_id, to_room_id, _direction, *_ in links:
        connected.add(from_room_id)
        connected.add(to_room_id)
    stable_id = _stable_id_by_room_id(rooms)
    isolated = {stable_id[room_id] for room_id in stable_id if room_id not in connected}
    unexpected = isolated - _KNOWN_ISOLATED_ROOMS
    assert not unexpected, f"newly isolated room(s), not in the baseline allowlist: {sorted(unexpected)}"
    shrunk = _KNOWN_ISOLATED_ROOMS - isolated
    if shrunk:
        # Not a failure -- a room getting wired up is progress. Surfaced so the baseline gets
        # trimmed (mirrors the basedpyright baseline's "may only shrink" discipline).
        print(f"baseline room(s) no longer isolated, remove from _KNOWN_ISOLATED_ROOMS: {sorted(shrunk)}")
