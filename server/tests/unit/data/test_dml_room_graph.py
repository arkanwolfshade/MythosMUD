"""Guards the `rooms` / `room_links` seed data in `data/db/mythos_{dev,unit,e2e}_dml.sql` against
the class of authoring mistake behind #823: one-way exits, a reciprocal that points at the wrong
room, and duplicate `(from_room_id, direction)` rows that silently collide under the DDL's own
`UNIQUE (from_room_id, direction)` constraint.

No database is needed -- this parses the `COPY ... FROM stdin` blocks directly out of the
`pg_dump`-formatted DML files (real tab separators, `\\N` for NULL, terminated by a bare `\\.`
line), so it runs in milliseconds under `make test` and catches the mistake at the point it's
actually made: in the text file, before it ever reaches a database.

`_KNOWN_ISOLATED_ROOMS` is a baseline, same discipline as `.basedpyright/baseline.json`: it may
only shrink as rooms are wired up (see #824), never grow to paper over a new orphan.
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

# The one room (and its two links) that mythos_unit_dml.sql intentionally omits relative to
# dev/e2e -- a smaller unit-test fixture set, not an authoring gap (see PR-B/#824 investigation).
_UNIT_EXCLUDED_ROOM_STABLE_ID = "earth_arkhamcity_downtown_room_curwen_boarding_house_001"

RoomRow = tuple[str, ...]
LinkRow = tuple[str, ...]

_COPY_RE = re.compile(r"^COPY [\w.]+\.(\w+) \(")


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


def _dml_path(environment: str) -> Path:
    return get_project_root() / "data" / "db" / f"mythos_{environment}_dml.sql"


def _load(environment: str) -> tuple[list[RoomRow], list[LinkRow]]:
    text = _dml_path(environment).read_text(encoding="utf-8")
    blocks = _parse_copy_blocks(text)
    return blocks["rooms"], blocks["room_links"]


_ENVIRONMENTS = ("dev", "unit", "e2e")


def _stable_id_by_room_id(rooms: list[RoomRow]) -> dict[str, str]:
    return {row[0]: row[2] for row in rooms}


def test_every_dml_file_parses_and_is_nonempty() -> None:
    for env in _ENVIRONMENTS:
        rooms, links = _load(env)
        assert len(rooms) > 100, f"{env}: suspiciously few rooms parsed ({len(rooms)})"
        assert len(links) > 100, f"{env}: suspiciously few room_links parsed ({len(links)})"


def test_no_duplicate_from_room_direction() -> None:
    """Mirrors the DDL's own `UNIQUE (from_room_id, direction)` constraint at the text level."""
    for env in _ENVIRONMENTS:
        _, links = _load(env)
        seen: dict[tuple[str, str], str] = {}
        for row in links:
            _link_id, from_room_id, _to_room_id, direction, *_ = row
            key = (from_room_id, direction)
            assert key not in seen, (
                f"{env}: duplicate room_links row for from_room_id={from_room_id} direction={direction} "
                f"(ids {seen[key]} and {row[0]})"
            )
            seen[key] = row[0]


def test_no_dangling_room_link_references() -> None:
    for env in _ENVIRONMENTS:
        rooms, links = _load(env)
        room_ids = {row[0] for row in rooms}
        for _link_id, from_room_id, to_room_id, _direction, *_ in links:
            assert from_room_id in room_ids, f"{env}: room_links {_link_id} from_room_id {from_room_id} not a room"
            assert to_room_id in room_ids, f"{env}: room_links {_link_id} to_room_id {to_room_id} not a room"


def test_every_room_link_has_an_exact_reciprocal() -> None:
    """The #823 bug class: a one-way exit, or a reciprocal that points at the wrong room."""
    for env in _ENVIRONMENTS:
        rooms, links = _load(env)
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
                problems.append(
                    f"{from_name} --{direction}--> {to_name} has no reciprocal ({to_name} --{opposite}--> ???)"
                )
            elif back_target != from_room_id:
                back_name = stable_id.get(back_target, back_target)
                reciprocal = f"{to_name} --{opposite}--> {back_name} points elsewhere"
                problems.append(f"{from_name} --{direction}--> {to_name}, but the reciprocal {reciprocal}")
        assert not problems, f"{env}: {len(problems)} broken reciprocal(s):\n" + "\n".join(problems)


def test_no_isolated_rooms_beyond_the_known_baseline() -> None:
    for env in _ENVIRONMENTS:
        rooms, links = _load(env)
        connected: set[str] = set()
        for _link_id, from_room_id, to_room_id, _direction, *_ in links:
            connected.add(from_room_id)
            connected.add(to_room_id)
        stable_id = _stable_id_by_room_id(rooms)
        isolated = {stable_id[room_id] for room_id in stable_id if room_id not in connected}
        unexpected = isolated - _KNOWN_ISOLATED_ROOMS
        assert not unexpected, f"{env}: newly isolated room(s), not in the baseline allowlist: {sorted(unexpected)}"
        shrunk = _KNOWN_ISOLATED_ROOMS - isolated
        if shrunk:
            # Not a failure -- a room getting wired up is progress. Surfaced so the baseline gets
            # trimmed (mirrors the basedpyright baseline's "may only shrink" discipline).
            print(f"{env}: baseline room(s) no longer isolated, remove from _KNOWN_ISOLATED_ROOMS: {sorted(shrunk)}")


def test_dev_and_e2e_rooms_and_links_are_byte_identical() -> None:
    dev_rooms, dev_links = _load("dev")
    e2e_rooms, e2e_links = _load("e2e")
    assert dev_rooms == e2e_rooms, "mythos_dev_dml.sql and mythos_e2e_dml.sql rooms blocks have diverged"
    assert dev_links == e2e_links, "mythos_dev_dml.sql and mythos_e2e_dml.sql room_links blocks have diverged"


def test_unit_rooms_match_dev_except_the_known_exclusion() -> None:
    dev_rooms, _ = _load("dev")
    unit_rooms, _ = _load("unit")
    dev_stable_ids = {row[2] for row in dev_rooms}
    unit_stable_ids = {row[2] for row in unit_rooms}

    missing_from_unit = dev_stable_ids - unit_stable_ids
    assert missing_from_unit == {_UNIT_EXCLUDED_ROOM_STABLE_ID}, (
        f"mythos_unit_dml.sql is missing dev rooms beyond the known exclusion: "
        f"{missing_from_unit - {_UNIT_EXCLUDED_ROOM_STABLE_ID}}"
    )
    extra_in_unit = unit_stable_ids - dev_stable_ids
    assert not extra_in_unit, f"mythos_unit_dml.sql has rooms dev/e2e lack: {extra_in_unit}"


def test_unit_room_links_diff_from_dev_is_limited_to_the_known_exclusion() -> None:
    dev_rooms, dev_links = _load("dev")
    unit_rooms, unit_links = _load("unit")
    dev_stable_id = _stable_id_by_room_id(dev_rooms)
    unit_stable_id = _stable_id_by_room_id(unit_rooms)

    def touches_excluded_room(link: LinkRow, stable_id: dict[str, str]) -> bool:
        _link_id, from_room_id, to_room_id, *_ = link
        return _UNIT_EXCLUDED_ROOM_STABLE_ID in (stable_id.get(from_room_id), stable_id.get(to_room_id))

    dev_only = [link for link in dev_links if link not in unit_links]
    unexpected_dev_only = [link for link in dev_only if not touches_excluded_room(link, dev_stable_id)]
    assert not unexpected_dev_only, (
        f"mythos_dev_dml.sql has room_links unit lacks, beyond the known exclusion's own links: {unexpected_dev_only}"
    )

    unit_only = [link for link in unit_links if link not in dev_links]
    unexpected_unit_only = [link for link in unit_only if not touches_excluded_room(link, unit_stable_id)]
    assert not unexpected_unit_only, f"mythos_unit_dml.sql has room_links dev/e2e lack: {unexpected_unit_only}"
