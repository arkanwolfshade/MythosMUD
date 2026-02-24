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


def _skip_table_data_block(lines: list[str], start: int) -> int:
    """Skip a TABLE DATA block (COPY ... \\.). Return index after the block."""
    i = start + 1
    while i < len(lines) and lines[i].strip() != r"\.":
        i += 1
    if i < len(lines):
        i += 1  # skip the \. line
    return i


def _skip_sequence_set_block(lines: list[str], start: int) -> int:
    """Skip a SEQUENCE SET block (setval + trailing blank lines). Return index after the block."""
    i = start + 1
    while i < len(lines) and not re.match(r"^SELECT pg_catalog\\.setval", lines[i]):
        i += 1
    if i < len(lines):
        i += 1  # skip setval line
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    return i


def _filter_lines(lines: list[str]) -> list[str]:
    """Filter out TABLE DATA and SEQUENCE SET blocks for excluded tables/sequences."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^-- Data for Name: (\w+); Type: TABLE DATA", line)
        if m and m.group(1) in EXCLUDE_TABLES:
            i = _skip_table_data_block(lines, i)
            continue
        m2 = re.match(r"^-- Name: (\w+); Type: SEQUENCE SET", line)
        if m2 and m2.group(1) in EXCLUDE_SEQUENCES:
            i = _skip_sequence_set_block(lines, i)
            continue
        out.append(line)
        i += 1
    return out


def main() -> None:
    """Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back."""
    path = "data/export/mythos_dev_public_dml.sql"
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    out = _filter_lines(lines)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.writelines(out)
    print("Done. Lines kept:", len(out))


if __name__ == "__main__":
    main()
