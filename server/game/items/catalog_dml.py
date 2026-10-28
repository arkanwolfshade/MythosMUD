"""Emit idempotent item_prototypes DML from catalog JSON (ADR-026 Phase 2).

Dual-writes ``damage_expr`` into legacy ``min_damage`` / ``max_damage`` when missing.
Does not change combat consumers.
"""

from __future__ import annotations

import json
import re
from collections.abc import Mapping, MutableMapping, Sequence
from typing import cast

from server.game.items.damage_expr import damage_expr_to_min_max
from server.game.items.metadata_models import ItemMetadata
from server.game.items.models import ItemPrototypeModel

# Columns upserted from catalog rows (created_at is insert-only).
_DATA_COLUMNS: tuple[str, ...] = (
    "prototype_id",
    "name",
    "short_description",
    "long_description",
    "item_type",
    "weight",
    "base_value",
    "durability",
    "flags",
    "wear_slots",
    "stacking_rules",
    "usage_restrictions",
    "effect_components",
    "metadata",
    "tags",
)


def sql_escape(value: str) -> str:
    """Escape a string for a single-quoted SQL literal."""
    return value.replace("'", "''")


def _ensure_weapon_defaults(weapon: MutableMapping[str, object]) -> None:
    """Fill legacy WeaponStats keys when dual-writing from damage_expr."""
    _ = weapon.setdefault("modifier", 0)
    _ = weapon.setdefault("damage_types", [])
    _ = weapon.setdefault("magical", False)


def apply_weapon_dual_write(metadata: MutableMapping[str, object]) -> None:
    """Fill WeaponStats integers from damage_expr when min/max are absent."""
    weapon_obj = metadata.get("weapon")
    if not isinstance(weapon_obj, dict):
        return
    weapon = cast(MutableMapping[str, object], weapon_obj)
    expr = weapon.get("damage_expr")
    if not isinstance(expr, str) or not expr.strip():
        return
    if weapon.get("min_damage") is not None and weapon.get("max_damage") is not None:
        return
    min_damage, max_damage = damage_expr_to_min_max(_normalize_damage_expr(expr))
    if weapon.get("min_damage") is None:
        weapon["min_damage"] = min_damage
    if weapon.get("max_damage") is None:
        weapon["max_damage"] = max_damage
    _ensure_weapon_defaults(weapon)


def _normalize_damage_expr(expr: str) -> str:
    """Strip DB/flavor suffixes and shotgun range bands for legacy min/max."""
    cleaned = expr.strip()
    cleaned = re.sub(r"(?i)\+?\s*half\s*DB\b", "", cleaned)
    cleaned = re.sub(r"(?i)\+?\s*1/2\s*DB\b", "", cleaned)
    cleaned = re.sub(r"(?i)\+?\s*DB\b", "", cleaned)
    cleaned = re.sub(r"(?i)\+?\s*(burn|stun)\b", "", cleaned)
    if "/" in cleaned:
        cleaned = cleaned.split("/", 1)[0]
    return cleaned.strip(" +").strip()


def prepare_prototype(raw: Mapping[str, object]) -> ItemPrototypeModel:
    """Validate a catalog row and apply dual-write bridge fields."""
    payload = dict(raw)
    metadata_raw = payload.get("metadata")
    if isinstance(metadata_raw, dict):
        metadata = dict(cast(Mapping[str, object], metadata_raw))
        apply_weapon_dual_write(metadata)
        _ = ItemMetadata.model_validate(metadata)
        payload["metadata"] = metadata
    return ItemPrototypeModel.model_validate(payload)


def _sql_literal(value: object, *, as_jsonb: bool) -> str:
    if value is None:
        return "NULL"
    if as_jsonb:
        dumped = json.dumps(value, separators=(",", ":"), ensure_ascii=True)
        return f"'{sql_escape(dumped)}'::jsonb"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        return str(value)
    return f"'{sql_escape(str(value))}'"


def _prototype_value_literals(model: ItemPrototypeModel) -> list[str]:
    """SQL literals for _DATA_COLUMNS in order."""
    return [
        _sql_literal(model.prototype_id, as_jsonb=False),
        _sql_literal(model.name, as_jsonb=False),
        _sql_literal(model.short_description, as_jsonb=False),
        _sql_literal(model.long_description, as_jsonb=False),
        _sql_literal(model.item_type, as_jsonb=False),
        _sql_literal(model.weight, as_jsonb=False),
        _sql_literal(model.base_value, as_jsonb=False),
        _sql_literal(model.durability, as_jsonb=False),
        _sql_literal(model.flags, as_jsonb=True),
        _sql_literal(model.wear_slots, as_jsonb=True),
        _sql_literal(cast(object, model.stacking_rules), as_jsonb=True),
        _sql_literal(cast(object, model.usage_restrictions), as_jsonb=True),
        _sql_literal(model.effect_components, as_jsonb=True),
        _sql_literal(cast(object, model.metadata), as_jsonb=True),
        _sql_literal(model.tags, as_jsonb=True),
    ]


def render_prototype_insert(schema: str, model: ItemPrototypeModel) -> str:
    """Render one idempotent INSERT for item_prototypes."""
    columns = [*_DATA_COLUMNS, "created_at"]
    values = [*_prototype_value_literals(model), "NOW()"]
    updates = ",\n    ".join(f"{col} = EXCLUDED.{col}" for col in _DATA_COLUMNS[1:])
    col_sql = ",\n    ".join(columns)
    val_sql = ",\n    ".join(values)
    return (
        f"INSERT INTO {schema}.item_prototypes (\n"
        f"    {col_sql}\n"
        ") VALUES (\n"
        f"    {val_sql}\n"
        ")\n"
        "ON CONFLICT (prototype_id) DO UPDATE SET\n"
        f"    {updates};\n"
    )


def render_migration(
    schema: str,
    prototypes: Sequence[Mapping[str, object]],
    *,
    header: str,
) -> str:
    """Render a full migration SQL file body for one schema."""
    blocks = [header.rstrip() + "\n"]
    for raw in prototypes:
        model = prepare_prototype(raw)
        blocks.append(render_prototype_insert(schema, model))
    return "\n".join(blocks).rstrip() + "\n"
