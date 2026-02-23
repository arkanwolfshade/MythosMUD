#!/usr/bin/env python3
"""Filter mythos_dev_public_dml.sql to keep only static/design data (exclude runtime tables)."""

import re

EXCLUDE_TABLES = {
    "aliases",
    "container_contents",
    "id_map_players",
    "id_map_users",
    "invites",
    "item_component_states",
    "item_instances",
    "lucidity_adjustment_log",
    "lucidity_cooldowns",
    "lucidity_exposure_state",
    "muting_rules",
    "player_effects",
    "player_inventories",
    "player_exploration",
    "player_lucidity",
    "player_skills",
    "player_spells",
    "players",
    "quest_instances",
    "skill_use_log",
    "users",
}

# Sequences that belong to excluded tables (remove their setval blocks)
EXCLUDE_SEQUENCES = {
    "item_component_states_id_seq1",
    "lucidity_adjustment_log_id_seq",
    "lucidity_cooldowns_id_seq",
    "lucidity_exposure_state_id_seq",
    "player_spells_id_seq1",
    "skill_use_log_id_seq",
}


def main() -> None:
    """Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back."""
    path = "data/export/mythos_dev_public_dml.sql"
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Table data block: -- Data for Name: tablename; Type: TABLE DATA
        m = re.match(r"^-- Data for Name: (\w+); Type: TABLE DATA", line)
        if m and m.group(1) in EXCLUDE_TABLES:
            i += 1
            while i < len(lines) and lines[i].strip() != r"\.":
                i += 1
            if i < len(lines):
                i += 1  # skip the \. line
            continue
        # SEQUENCE SET block: -- Name: seqname; Type: SEQUENCE SET
        m2 = re.match(r"^-- Name: (\w+); Type: SEQUENCE SET", line)
        if m2 and m2.group(1) in EXCLUDE_SEQUENCES:
            i += 1
            while i < len(lines) and not re.match(r"^SELECT pg_catalog\\.setval", lines[i]):
                i += 1
            if i < len(lines):
                i += 1  # skip setval line
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            continue
        out.append(line)
        i += 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.writelines(out)
    print("Done. Lines kept:", len(out))


if __name__ == "__main__":
    main()
