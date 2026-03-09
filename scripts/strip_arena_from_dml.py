#!/usr/bin/env python3
"""
Remove arena zone/subzone/rooms/room_links/zone_config from mythos_unit_dml.sql and mythos_e2e_dml.sql.

Arena data is now applied via data/db/migrations/20260227_add_arena_zone_*.sql.
Run from project root. Modifies files in place.
"""

from __future__ import annotations

import sys
import uuid
from pathlib import Path

from scripts.gen_arena_dml import ROOMS, SUBZONE_UUID, ZONE_UUID

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


NS = uuid.NAMESPACE_DNS
ARENA_ROOM_IDS = {str(ROOMS[(r, c)]) for r in range(11) for c in range(11)}
ZONE_CONFIG_UUID = str(uuid.uuid5(NS, "mythosmud.limbo/arena.zone_config"))


def is_arena_zone_line(line: str) -> bool:
    """Return True when a zones COPY row is the arena zone."""
    return line.startswith(str(ZONE_UUID) + "\t")


def is_arena_subzone_line(line: str) -> bool:
    """Return True when a subzones COPY row is the arena subzone."""
    return line.startswith(str(SUBZONE_UUID) + "\t")


def is_arena_room_line(line: str) -> bool:
    """Return True when a rooms COPY row belongs to the arena subzone."""
    parts = line.split("\t")
    return len(parts) >= 2 and parts[1] == str(SUBZONE_UUID)


def is_arena_room_link_line(line: str) -> bool:
    """Return True when a room_links COPY row links two arena rooms."""
    parts = line.split("\t")
    if len(parts) < 4:
        return False
    from_id, to_id = parts[1], parts[2]
    return from_id in ARENA_ROOM_IDS and to_id in ARENA_ROOM_IDS


def is_arena_zone_config_line(line: str) -> bool:
    """Return True when a zone_configurations COPY row matches arena zone config."""
    return line.startswith(ZONE_CONFIG_UUID + "\t")


def get_copy_section(line: str) -> str | None:
    """Return the active COPY section name, or None if line is not a COPY header."""
    if "COPY " not in line or " FROM stdin;" not in line:
        return None
    if "room_links" in line:
        return "room_links"
    if "zone_configurations" in line:
        return "zone_configurations"
    if "subzones" in line:
        return "subzones"
    if "rooms" in line:
        return "rooms"
    if "zones" in line:
        return "zones"
    return None


def should_skip_line(section: str | None, line: str) -> bool:
    """Return True when a data row belongs to arena records in the active COPY section."""
    if section == "zones":
        return is_arena_zone_line(line)
    if section == "subzones":
        return is_arena_subzone_line(line)
    if section == "rooms":
        return is_arena_room_line(line)
    if section == "room_links":
        return is_arena_room_link_line(line)
    if section == "zone_configurations":
        return is_arena_zone_config_line(line)
    return False


def strip_arena_from_file(path: Path) -> None:
    """Remove arena records from COPY sections in a DML file, in place."""
    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()
    out = []
    section: str | None = None
    for line in lines:
        copy_section = get_copy_section(line)
        if copy_section is not None:
            section = copy_section
            out.append(line)
            continue
        if line.strip() == "\\.":
            section = None
            out.append(line)
            continue
        if should_skip_line(section, line):
            continue
        out.append(line)
    with path.open("w", encoding="utf-8") as f:
        f.writelines(out)
    print(f"Stripped arena from {path}")


def main() -> None:
    """Strip arena rows from mythos_unit and mythos_e2e DML files."""
    for name in ("mythos_unit_dml.sql", "mythos_e2e_dml.sql"):
        path = ROOT / "data" / "db" / name
        if not path.exists():
            print(f"Skip (not found): {path}")
            continue
        strip_arena_from_file(path)


if __name__ == "__main__":
    main()
