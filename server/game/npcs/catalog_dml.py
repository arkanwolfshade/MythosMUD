"""Emit idempotent npc_definitions DML from catalog JSON (ADR-027 Phase 2).

Forces arena + inert spawn placement. Dual-writes attack ``damage_expr`` into
legacy min/max and ``behavior_config.attack_damage``.
"""

from __future__ import annotations

import json
import re
from collections.abc import Mapping, MutableMapping, Sequence
from typing import cast

from server.game.dice_expr import damage_expr_to_min_max
from server.game.npcs.base_stats_models import NpcBaseStats

_ARENA_SUB_ZONE = "arena"
_DATA_COLUMNS: tuple[str, ...] = (
    "name",
    "description",
    "npc_type",
    "sub_zone_id",
    "room_id",
    "required_npc",
    "max_population",
    "spawn_probability",
    "base_stats",
    "behavior_config",
    "ai_integration_stub",
)


def sql_escape(value: str) -> str:
    """Escape a string for a single-quoted SQL literal."""
    return value.replace("'", "''")


def _normalize_damage_expr(expr: str) -> str:
    """Strip DB/flavor suffixes and range bands for legacy min/max."""
    cleaned = expr.strip()
    cleaned = re.sub(r"(?i)\+?\s*half\s*DB\b", "", cleaned)
    cleaned = re.sub(r"(?i)\+?\s*1/2\s*DB\b", "", cleaned)
    cleaned = re.sub(r"(?i)\+?\s*DB\b", "", cleaned)
    cleaned = re.sub(r"(?i)\+?\s*(burn|stun)\b", "", cleaned)
    if "/" in cleaned:
        cleaned = cleaned.split("/", 1)[0]
    return cleaned.strip(" +").strip()


def apply_attack_dual_write(base_stats: MutableMapping[str, object]) -> None:
    """Fill attack min/max from damage_expr when absent."""
    attacks_raw = base_stats.get("attacks")
    if not isinstance(attacks_raw, list):
        return
    for entry_obj in cast(list[object], attacks_raw):
        if not isinstance(entry_obj, dict):
            continue
        attack = cast(MutableMapping[str, object], entry_obj)
        expr = attack.get("damage_expr")
        if not isinstance(expr, str) or not expr.strip():
            continue
        if attack.get("min_damage") is not None and attack.get("max_damage") is not None:
            continue
        min_damage, max_damage = damage_expr_to_min_max(_normalize_damage_expr(expr))
        if attack.get("min_damage") is None:
            attack["min_damage"] = min_damage
        if attack.get("max_damage") is None:
            attack["max_damage"] = max_damage


def _hostility_to_npc_type(raw: Mapping[str, object]) -> str:
    npc_type = raw.get("npc_type")
    if isinstance(npc_type, str) and npc_type in {"aggressive_mob", "passive_mob"}:
        return npc_type
    hostility = raw.get("hostility")
    if isinstance(hostility, str) and hostility.strip().lower() in {"aggressive", "hostile"}:
        return "aggressive_mob"
    return "passive_mob"


def _first_attack_damage(base_stats: Mapping[str, object]) -> int:
    attacks_raw = base_stats.get("attacks")
    if not isinstance(attacks_raw, list) or not attacks_raw:
        return 1
    first_obj = cast(list[object], attacks_raw)[0]
    if not isinstance(first_obj, dict):
        return 1
    first = cast(dict[str, object], first_obj)
    lo = first.get("min_damage")
    hi = first.get("max_damage")
    if isinstance(lo, int) and isinstance(hi, int):
        return max(1, (lo + hi) // 2)
    if isinstance(lo, int):
        return max(1, lo)
    return 1


def _ensure_behavior_config(
    raw: Mapping[str, object],
    base_stats: Mapping[str, object],
    npc_type: str,
) -> dict[str, object]:
    behavior_raw = raw.get("behavior_config")
    behavior: dict[str, object] = {}
    if isinstance(behavior_raw, dict):
        behavior = {str(k): v for k, v in cast(dict[object, object], behavior_raw).items()}
    if "attack_damage" not in behavior:
        behavior["attack_damage"] = _first_attack_damage(base_stats)
    if "aggression_level" not in behavior:
        behavior["aggression_level"] = "aggressive" if npc_type == "aggressive_mob" else "passive"
    return behavior


def prepare_npc_definition(raw: Mapping[str, object]) -> dict[str, object]:
    """Validate catalog row, dual-write attacks, force arena/inert placement."""
    base_raw = raw.get("base_stats")
    if not isinstance(base_raw, dict):
        raise ValueError("catalog row requires base_stats object")
    base_stats: dict[str, object] = {str(k): v for k, v in cast(dict[object, object], base_raw).items()}
    apply_attack_dual_write(base_stats)
    _ = NpcBaseStats.model_validate(base_stats)

    name = raw.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("catalog row requires non-empty name")
    description = raw.get("description")
    if description is not None and not isinstance(description, str):
        raise ValueError("description must be a string when present")

    npc_type = _hostility_to_npc_type(raw)
    behavior = _ensure_behavior_config(raw, base_stats, npc_type)
    ai_raw = raw.get("ai_integration_stub")
    ai_stub: dict[str, object] = {}
    if isinstance(ai_raw, dict):
        ai_stub = {str(k): v for k, v in cast(dict[object, object], ai_raw).items()}

    return {
        "name": name.strip(),
        "description": description,
        "npc_type": npc_type,
        "sub_zone_id": _ARENA_SUB_ZONE,
        "room_id": None,
        "required_npc": False,
        "max_population": 0,
        "spawn_probability": 0.0,
        "base_stats": base_stats,
        "behavior_config": behavior,
        "ai_integration_stub": ai_stub,
    }


def _sql_literal(value: object, *, as_json_text: bool = False) -> str:
    if value is None:
        return "NULL"
    if as_json_text:
        dumped = json.dumps(value, separators=(",", ":"), ensure_ascii=True)
        return f"'{sql_escape(dumped)}'"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, int):
        return str(value)
    return f"'{sql_escape(str(value))}'"


def render_npc_insert(schema: str, row: Mapping[str, object]) -> str:
    """Render one idempotent INSERT for npc_definitions."""
    values = [
        _sql_literal(row["name"]),
        _sql_literal(row["description"]),
        _sql_literal(row["npc_type"]),
        _sql_literal(row["sub_zone_id"]),
        _sql_literal(row["room_id"]),
        _sql_literal(row["required_npc"]),
        _sql_literal(row["max_population"]),
        _sql_literal(row["spawn_probability"]),
        _sql_literal(row["base_stats"], as_json_text=True),
        _sql_literal(row["behavior_config"], as_json_text=True),
        _sql_literal(row["ai_integration_stub"], as_json_text=True),
        "NOW()",
        "NOW()",
    ]
    update_cols = [c for c in _DATA_COLUMNS if c not in {"name", "sub_zone_id"}]
    updates = ",\n    ".join(f"{col} = EXCLUDED.{col}" for col in update_cols)
    updates += ",\n    updated_at = NOW()"
    col_sql = ",\n    ".join([*_DATA_COLUMNS, "created_at", "updated_at"])
    val_sql = ",\n    ".join(values)
    return (
        f"INSERT INTO {schema}.npc_definitions (\n"
        f"    {col_sql}\n"
        ") VALUES (\n"
        f"    {val_sql}\n"
        ")\n"
        "ON CONFLICT (name, sub_zone_id) DO UPDATE SET\n"
        f"    {updates};\n"
    )


def render_migration(
    schema: str,
    rows: Sequence[Mapping[str, object]],
    *,
    header: str,
) -> str:
    """Render a full migration SQL file body for one schema."""
    blocks = [header.rstrip() + "\n"]
    for raw in rows:
        prepared = prepare_npc_definition(raw)
        blocks.append(render_npc_insert(schema, prepared))
    return "\n".join(blocks).rstrip() + "\n"
