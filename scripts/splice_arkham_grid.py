"""Splice the generated Arkham street grid into the three DML seed files (#829).

One-shot, idempotent-by-refusal: it will not run twice, because the second run
finds the new rooms already present and stops.

What it does to each of `mythos_{dev,unit,e2e}_dml.sql`:

* `rooms`        - removes the 80 replaced Arkham street rooms, appends the 481 new
                   ones, and gives the surviving boarding house its coordinates.
* `room_links`   - removes every link touching a replaced room, appends the new set.
* `subzones`     - appends the five landmark sub-zones.
* `zone_configurations` - appends their NPC-config mappings.
* `npc_definitions` / `npc_spawn_rules` - rehouses the seven NPCs whose rooms went.

Two invariants from `server/tests/unit/data/test_dml_room_graph.py` shape all of this:

1. The dev and e2e rooms/links blocks must stay BYTE-IDENTICAL, so rows are appended
   in generated order and never re-sorted.
2. The unit file must differ from dev by exactly one room -
   `earth_arkhamcity_downtown_room_curwen_boarding_house_001` - and its links. That
   room is a building interior and a `rest_location`, so #829 keeps it and re-attaches
   it; unit simply continues to omit it and its two links.

    python scripts/splice_arkham_grid.py --generated build/arkham
    python scripts/splice_arkham_grid.py --generated build/arkham --check
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

from generate_arkham_grid import BOARDING_HOUSE  # noqa: E402

ENVS = ("dev", "unit", "e2e")
DML = Path("data/db/mythos_{env}_dml.sql")

# NPCs whose rooms are replaced. (npc id, new sub_zone_id, new room stable_id)
NPC_REHOMING: dict[str, tuple[str, str]] = {
    "51": ("merchant", "earth_arkhamcity_merchant_intersection_peabody_pickman"),
    "52": ("frenchhill", "earth_arkhamcity_frenchhill_intersection_frenchhill_pickman"),
    "53": ("campus", "earth_arkhamcity_campus_intersection_college_garrison"),
    "55": ("campus", "earth_arkhamcity_campus_room_college_st_002"),
    "57": ("independence_square", "earth_arkhamcity_independence_square_room_square_001"),
    "58": ("downtown", "earth_arkhamcity_downtown_room_lich_st_001"),
    "60": ("hangmans_hill", "earth_arkhamcity_hangmans_hill_room_summit_001"),
}


def is_replaced_street_room(stable_id: str) -> bool:
    """True for the Arkham rooms #829 replaces: streets only, never interiors."""
    return (
        stable_id.startswith("earth_arkhamcity_")
        and "_sanitarium_" not in stable_id
        and stable_id != BOARDING_HOUSE
    )


def block_bounds(text: str, table: str) -> tuple[int, int]:
    """Character offsets of a COPY block's body (between the header and the `\\.`)."""
    m = re.search(rf"^COPY [\w.]+\.{table} \([^)]*\) FROM stdin;\n", text, re.M)
    if not m:
        raise SystemExit(f"no COPY block for {table}")
    end = text.index("\n\\.", m.end())
    return m.end(), end + 1


def body(text: str, table: str) -> list[list[str]]:
    start, end = block_bounds(text, table)
    return [line.split("\t") for line in text[start:end].rstrip("\n").split("\n")]


def replace_body(text: str, table: str, rows: list[list[str]]) -> str:
    start, end = block_bounds(text, table)
    payload = "\n".join("\t".join(r) for r in rows) + "\n"
    return text[:start] + payload + text[end:]


def load_generated(out: Path) -> tuple[list[list[str]], list[list[str]], list[list[str]], list[list[str]], list[str]]:
    def tsv(name: str) -> list[list[str]]:
        return [ln.split("\t") for ln in (out / name).read_text(encoding="utf-8").splitlines() if ln]

    return (
        tsv("rooms.tsv"),
        tsv("room_links.tsv"),
        tsv("subzones.tsv"),
        tsv("zone_configurations.tsv"),
        tsv("preserved_coords.tsv")[0],
    )


def splice(env: str, out: Path, check: bool) -> str:
    path = Path(DML.as_posix().format(env=env))
    # Bytes, not read_text: these files are LF-only and must stay that way on Windows.
    text = path.read_bytes().decode("utf-8")
    new_rooms, new_links, new_subzones, new_configs, preserved = load_generated(out)

    if any(r[2] in text for r in new_rooms[:1]):
        raise SystemExit(f"{path} already contains generated rooms - refusing to splice twice")

    rooms = body(text, "rooms")
    links = body(text, "room_links")

    dropped_uuids = {r[0] for r in rooms if is_replaced_street_room(r[2])}
    kept_rooms = [r for r in rooms if r[0] not in dropped_uuids]
    kept_links = [x for x in links if x[1] not in dropped_uuids and x[2] not in dropped_uuids]

    # The boarding house is present in dev/e2e and deliberately absent from unit.
    # Where it is present, give it coordinates; where it is absent, its two links
    # must be dropped too, or unit gains links to a room it does not have.
    bh_uuid = _uuid_of(BOARDING_HOUSE)
    bh_present = any(r[2] == BOARDING_HOUSE for r in kept_rooms)
    add_rooms = list(new_rooms)
    if bh_present:
        add_links = list(new_links)
        for r in kept_rooms:
            if r[2] == BOARDING_HOUSE:
                r[6], r[7], r[9], r[10] = preserved[1], preserved[2], preserved[3], preserved[4]
    else:
        add_links = [x for x in new_links if bh_uuid not in (x[1], x[2])]

    text = replace_body(text, "rooms", kept_rooms + add_rooms)
    text = replace_body(text, "room_links", kept_links + add_links)
    text = replace_body(text, "subzones", body(text, "subzones") + new_subzones)
    text = replace_body(
        text, "zone_configurations", body(text, "zone_configurations") + new_configs
    )

    npcs = body(text, "npc_definitions")
    for row in npcs:
        if row[0] in NPC_REHOMING:
            row[4], row[5] = NPC_REHOMING[row[0]]
    text = replace_body(text, "npc_definitions", npcs)

    rules = body(text, "npc_spawn_rules")
    for row in rules:
        if row[1] in NPC_REHOMING:
            row[2] = NPC_REHOMING[row[1]][0]
    text = replace_body(text, "npc_spawn_rules", rules)

    if not check:
        path.write_bytes(text.encode("utf-8"))

    return (
        f"{env:<5} rooms {len(rooms)} -> {len(kept_rooms) + len(add_rooms)}"
        f"  (dropped {len(dropped_uuids)}, added {len(add_rooms)})"
        f"   links {len(links)} -> {len(kept_links) + len(add_links)}"
    )


def _uuid_of(stable_id: str) -> str:
    from generate_arkham_grid import room_uuid

    return room_uuid(stable_id)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generated", type=Path, default=Path("build/arkham"))
    parser.add_argument("--check", action="store_true", help="report without writing")
    args = parser.parse_args()

    for env in ENVS:
        print(splice(env, args.generated, args.check))
    print("(dry run - nothing written)" if args.check else "written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
