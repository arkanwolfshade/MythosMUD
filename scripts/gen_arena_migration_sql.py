#!/usr/bin/env python3
"""
Generate arena zone migration SQL for mythos_unit and mythos_e2e.

Reads arena data from gen_arena_dml (deterministic UUIDs and row content),
outputs INSERT ... ON CONFLICT (id) DO NOTHING for zones, subzones, rooms,
room_links, and zone_configurations. Writes one .sql file per schema under
data/db/migrations/.

Usage:
  python scripts/gen_arena_migration_sql.py

Output files:
  data/db/migrations/20260227_add_arena_zone_unit.sql
  data/db/migrations/20260227_add_arena_zone_e2e.sql
  data/db/migrations/20260227_add_arena_zone_dev.sql
"""

from __future__ import annotations

import sys
from pathlib import Path

from scripts.gen_arena_dml import (
    gen_room_links,
    gen_room_row,
    gen_subzone_row,
    gen_zone_config_row,
    gen_zone_row,
)

# Project root (parent of scripts/)
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def sql_escape(s: str) -> str:
    """Escape single quotes for SQL literal: ' -> ''."""
    return s.replace("'", "''")


def emit_zone_insert(schema: str) -> str:
    """Build INSERT SQL for the arena zone row in the target schema."""
    # id, stable_id, name, zone_type, environment, description, weather_patterns, special_rules
    row = gen_zone_row(schema)
    parts = row.split("\t")
    uid, stable_id, name, zone_type, env, desc, _weather, special = parts
    return (
        f"INSERT INTO {schema}.zones (\n"
        "    id, stable_id, name, zone_type, environment, description, weather_patterns, special_rules\n"
        ") VALUES (\n"
        f"    '{uid}'::uuid,\n"
        f"    '{sql_escape(stable_id)}',\n"
        f"    '{sql_escape(name)}',\n"
        f"    '{sql_escape(zone_type)}',\n"
        f"    '{sql_escape(env)}',\n"
        f"    '{sql_escape(desc)}',\n"
        "    '[]'::jsonb,\n"
        f"    '{sql_escape(special)}'::jsonb\n"
        ")\nON CONFLICT (id) DO NOTHING;\n"
    )


def emit_subzone_insert(schema: str) -> str:
    """Build INSERT SQL for the arena subzone row in the target schema."""
    row = gen_subzone_row(schema)
    parts = row.split("\t")
    uid, zone_id, stable_id, name, env, desc, special = parts
    return (
        f"INSERT INTO {schema}.subzones (\n"
        "    id, zone_id, stable_id, name, environment, description, special_rules\n"
        ") VALUES (\n"
        f"    '{uid}'::uuid,\n"
        f"    '{zone_id}'::uuid,\n"
        f"    '{sql_escape(stable_id)}',\n"
        f"    '{sql_escape(name)}',\n"
        f"    '{sql_escape(env)}',\n"
        f"    '{sql_escape(desc)}',\n"
        f"    '{sql_escape(special)}'::jsonb\n"
        ")\nON CONFLICT (id) DO NOTHING;\n"
    )


def emit_rooms_insert(schema: str) -> str:
    """Build batched INSERT SQL for all 121 arena room rows in the target schema."""
    # id, subzone_id, stable_id, name, description, attributes, map_x, map_y, map_origin_zone, map_symbol, map_style
    lines = [
        f"INSERT INTO {schema}.rooms (\n"
        "    id, subzone_id, stable_id, name, description, attributes, map_x, map_y, map_origin_zone, map_symbol, map_style\n"
        ") VALUES"
    ]
    rows = []
    for r in range(11):
        for c in range(11):
            row = gen_room_row(r, c, schema)
            parts = row.split("\t")
            uid, subzone_id, stable_id, name, desc, attrs = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
            # map_x, map_y, map_origin_zone, map_symbol, map_style -> NULL, NULL, false, NULL, NULL per COPY
            rows.append(
                f"    ('{uid}'::uuid, '{subzone_id}'::uuid, '{sql_escape(stable_id)}', "
                f"'{sql_escape(name)}', '{sql_escape(desc)}', '{sql_escape(attrs)}'::jsonb, "
                "NULL, NULL, false, NULL, NULL)"
            )
    lines.append(",\n".join(rows))
    lines.append("\nON CONFLICT (id) DO NOTHING;\n")
    return "\n".join(lines)


def emit_room_links_insert(schema: str) -> str:
    """Build batched INSERT SQL for arena room_links in the target schema."""
    link_lines = gen_room_links(schema)
    lines = [f"INSERT INTO {schema}.room_links (\n    id, from_room_id, to_room_id, direction, attributes\n) VALUES"]
    values = []
    for line in link_lines:
        parts = line.split("\t")
        link_id, from_id, to_id, direction, attrs = parts
        values.append(
            f"    ('{link_id}'::uuid, '{from_id}'::uuid, '{to_id}'::uuid, "
            f"'{sql_escape(direction)}', '{sql_escape(attrs)}'::jsonb)"
        )
    lines.append(",\n".join(values))
    lines.append("\nON CONFLICT (id) DO NOTHING;\n")
    return "\n".join(lines)


def emit_zone_config_insert(schema: str) -> str:
    """Build INSERT SQL for the arena zone_configurations row in the target schema."""
    row = gen_zone_config_row(schema)
    parts = row.split("\t")
    config_id, zone_id, subzone_id = parts
    return (
        f"INSERT INTO {schema}.zone_configurations (\n"
        "    id, zone_id, subzone_id\n"
        ") VALUES (\n"
        f"    '{config_id}'::uuid,\n"
        f"    '{zone_id}'::uuid,\n"
        f"    '{subzone_id}'::uuid\n"
        ")\nON CONFLICT (id) DO NOTHING;\n"
    )


def generate_migration(schema: str) -> str:
    """Assemble full arena migration SQL (zone, subzone, rooms, links, zone_config) for schema."""
    header = (
        f"-- Add arena zone (limbo/arena), subzone, 121 rooms, room_links, zone_config for {schema}.\n"
        "-- Idempotent: ON CONFLICT (id) DO NOTHING. Same UUIDs as mythos_dev.\n"
        "\n"
    )
    return (
        header
        + emit_zone_insert(schema)
        + "\n"
        + emit_subzone_insert(schema)
        + "\n"
        + emit_rooms_insert(schema)
        + "\n"
        + emit_room_links_insert(schema)
        + "\n"
        + emit_zone_config_insert(schema)
    )


def main() -> None:
    """Generate arena migration SQL files for unit, e2e, and dev schemas."""
    migrations_dir = ROOT / "data" / "db" / "migrations"
    migrations_dir.mkdir(parents=True, exist_ok=True)
    for schema in ("mythos_unit", "mythos_e2e", "mythos_dev"):
        sql = generate_migration(schema)
        out_path = migrations_dir / f"20260227_add_arena_zone_{schema.replace('mythos_', '')}.sql"
        out_path.write_text(sql, encoding="utf-8")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
