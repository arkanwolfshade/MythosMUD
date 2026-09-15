"""Unit tests for NPC base_stats Pydantic contracts and public JSON Schema."""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast

import pytest
from jsonschema import validate as jsonschema_validate
from pydantic import ValidationError

from server.game.npcs.base_stats_models import NpcBaseStats

_REPO_ROOT = Path(__file__).resolve().parents[5]
_FIXTURE = _REPO_ROOT / "schemas" / "npcs" / "fixtures" / "synthetic_rich_base_stats.json"
_SCHEMA = _REPO_ROOT / "schemas" / "npcs" / "npc_base_stats.schema.json"


def _loads_json_value(text: str) -> object:
    # Reason: SERIALIZATION_BOUNDARY - json.loads is typed Any upstream.
    # Appropriate because: callers immediately isinstance-guard and rebuild a typed dict[str, object].
    return json.loads(text)  # pyright: ignore[reportAny]


def _load_json_object(path: Path) -> dict[str, object]:
    payload = _loads_json_value(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"expected JSON object in {path}")
    return {str(key): value for key, value in cast(dict[object, object], payload).items()}


def test_npc_base_stats_model_accepts_rich_fixture() -> None:
    payload = _load_json_object(_FIXTURE)
    stats = NpcBaseStats.model_validate(payload)
    assert stats.max_dp == 12
    assert stats.catalog is not None
    assert stats.catalog.namespace == "era_classic"
    assert stats.attacks is not None
    assert stats.attacks[0].damage_expr == "1d6+1"
    assert stats.armor is not None
    assert stats.armor.armor_points == 1


def test_npc_base_stats_json_schema_accepts_rich_fixture() -> None:
    schema = _load_json_object(_SCHEMA)
    payload = _load_json_object(_FIXTURE)
    jsonschema_validate(instance=payload, schema=schema)


def test_npc_base_stats_rejects_missing_required() -> None:
    with pytest.raises(ValidationError):
        _ = NpcBaseStats.model_validate({"determination_points": 1, "max_dp": 1})
