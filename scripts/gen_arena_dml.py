"""Generate arena zone, subzone, 121 rooms, and room_links for DML. Deterministic UUIDs."""

from __future__ import annotations

import uuid

NS = uuid.NAMESPACE_DNS
ZONE_UUID = uuid.uuid5(NS, "mythosmud.limbo/arena.zone")
SUBZONE_UUID = uuid.uuid5(NS, "mythosmud.limbo/arena.arena.subzone")
ROOMS: dict[tuple[int, int], uuid.UUID] = {}
for r in range(11):
    for c in range(11):
        ROOMS[(r, c)] = uuid.uuid5(NS, f"mythosmud.limbo_arena_arena_arena.{r}.{c}")


def room_stable_id(row: int, col: int) -> str:
    """Return the stable_id for an arena room at grid position (row, col)."""
    return f"limbo_arena_arena_arena_{row}_{col}"


def gen_zone_row(_schema: str) -> str:
    """Return a tab-separated zone row for the limbo/arena zone (id through special_rules)."""
    # id, stable_id, name, zone_type, environment, description, weather_patterns, special_rules
    return (
        f"{ZONE_UUID}\tlimbo/arena\tarena\tarena\tindoors\t"
        "A gladiator ring suspended in limbo: eleven by eleven cells of sand and shadow, "
        "where combatants are sent from the tutorial or from death. The crowd is unseen but ever watching.\t"
        "[]\t"
        '{"combat_modifier": 1.2, "exploration_bonus": 0, "npc_spawn_modifier": 1, "lucidity_drain_rate": 0}'
    )


def gen_subzone_row(_schema: str) -> str:
    """Return a tab-separated subzone row for the arena subzone under limbo/arena."""
    return (
        f"{SUBZONE_UUID}\t{ZONE_UUID}\tarena\tarena\tindoors\t"
        "The arena grid: eleven by eleven cells, north/south/east/west. "
        "Center (5,5) is the entrance and respawn point.\t{}"
    )


def gen_room_row(row: int, col: int, _schema: str) -> str:
    """Return a tab-separated room row for the arena cell at (row, col)."""
    stable_id = room_stable_id(row, col)
    name = f"Arena cell ({row},{col})" if (row, col) != (5, 5) else "Arena entrance (center)"
    desc = (
        "The heart of the gladiator ring. Sand and shadow stretch to the edges; "
        "exits lead north, south, east, and west into the grid."
        if (row, col) == (5, 5)
        else f"Arena cell at grid position ({row},{col}). Exits lead to adjacent cells."
    )
    room_id = ROOMS[(row, col)]
    return f'{room_id}\t{SUBZONE_UUID}\t{stable_id}\t{name}\t{desc}\t{{"environment": "arena"}}\t\\N\t\\N\tf\t\\N\t\\N'


def gen_room_link_id(from_r: int, from_c: int, direction: str) -> uuid.UUID:
    """Return a deterministic UUID for a room link from (from_r, from_c) in the given direction."""
    return uuid.uuid5(NS, f"mythosmud.arena.link.{room_stable_id(from_r, from_c)}.{direction}")


def gen_room_links(_schema: str) -> list[str]:
    """Return tab-separated room_links rows for the 11x11 arena grid (id, from_room_id, to_room_id, direction, attributes)."""
    lines = []
    # direction -> (dr, dc)
    delta = {"north": (-1, 0), "south": (1, 0), "east": (0, 1), "west": (0, -1)}
    for row in range(11):
        for col in range(11):
            from_uid = ROOMS[(row, col)]
            for direction, (dr, dc) in delta.items():
                nr, nc = row + dr, col + dc
                if 0 <= nr <= 10 and 0 <= nc <= 10:
                    to_uid = ROOMS[(nr, nc)]
                    link_id = gen_room_link_id(row, col, direction)
                    lines.append(f"{link_id}\t{from_uid}\t{to_uid}\t{direction}\t{{}}")
    return lines


def gen_zone_config_row(_schema: str) -> str:
    """Return a tab-separated zone_config row linking the arena zone and subzone."""
    config_id = uuid.uuid5(NS, "mythosmud.limbo/arena.zone_config")
    return f"{config_id}\t{ZONE_UUID}\t{SUBZONE_UUID}"


def main() -> None:
    """Print sample arena DML (zone, subzone, rooms, room_links, zone_config) to stdout."""
    schema = "mythos_dev"
    print("-- ZONE ROW")
    print(gen_zone_row(schema))
    print()
    print("-- SUBZONE ROW")
    print(gen_subzone_row(schema))
    print()
    print("-- ROOM ROWS (first 3)")
    for row in range(2):
        for col in range(2):
            print(gen_room_row(row, col, schema))
    print("...")
    print("-- ROOM (5,5)")
    print(gen_room_row(5, 5, schema))
    print()
    print("-- ROOM_LINKS (first 5)")
    for room_link_line in gen_room_links(schema)[:5]:
        print(room_link_line)
    print("... total", len(gen_room_links(schema)))
    print()
    print("-- ZONE_CONFIG ROW")
    print(gen_zone_config_row(schema))


def all_room_rows(schema: str) -> list[str]:
    """Return tab-separated room rows for all 121 arena grid cells (0,0) through (10,10)."""
    return [gen_room_row(row, col, schema) for row in range(11) for col in range(11)]


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "rooms":
        for row_str in all_room_rows("mythos_dev"):
            print(row_str)
    elif len(sys.argv) > 1 and sys.argv[1] == "links":
        for link_row in gen_room_links("mythos_dev"):
            print(link_row)
    else:
        main()
