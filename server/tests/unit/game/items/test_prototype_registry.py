"""Unit tests for PrototypeRegistry."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry, PrototypeRegistryError

VALID_PROTOTYPE = {
    "prototype_id": "test.item.one",
    "name": "Test Item",
    "short_description": "a test item",
    "long_description": "A test item for unit tests.",
    "item_type": "equipment",
    "weight": 1.0,
    "base_value": 10,
    "flags": [],
    "wear_slots": [],
    "usage_restrictions": {},
    "stacking_rules": {"max_stack": 1},
    "effect_components": [],
    "metadata": {},
    "tags": ["test", "gear"],
}


def _make_prototype(prototype_id: str = "test.item.one", **overrides: object) -> ItemPrototypeModel:
    payload = {**VALID_PROTOTYPE, "prototype_id": prototype_id, **overrides}
    return ItemPrototypeModel.model_validate(payload)


def test_get_returns_prototype() -> None:
    proto = _make_prototype()
    registry = PrototypeRegistry(prototypes={proto.prototype_id: proto}, invalid_entries=[])
    assert registry.get("test.item.one") is proto


def test_get_missing_raises() -> None:
    registry = PrototypeRegistry(prototypes={}, invalid_entries=[])
    with pytest.raises(PrototypeRegistryError, match="not found"):
        registry.get("missing")


def test_find_by_tag() -> None:
    proto_a = _make_prototype("a", tags=["weapon", "melee"])
    proto_b = _make_prototype("b", tags=["armor"])
    registry = PrototypeRegistry(
        prototypes={proto_a.prototype_id: proto_a, proto_b.prototype_id: proto_b},
        invalid_entries=[],
    )
    found = registry.find_by_tag("weapon")
    assert len(found) == 1
    assert found[0].prototype_id == "a"


def test_all_returns_values() -> None:
    proto = _make_prototype()
    registry = PrototypeRegistry(prototypes={proto.prototype_id: proto}, invalid_entries=[])
    assert list(registry.all()) == [proto]


def test_invalid_entries_returns_copy() -> None:
    invalid = [{"prototype_id": "bad", "errors": []}]
    registry = PrototypeRegistry(prototypes={}, invalid_entries=invalid)
    result = registry.invalid_entries()
    assert result == invalid
    result.append({"extra": True})
    assert len(registry.invalid_entries()) == 1


def test_load_from_path_missing_directory(tmp_path: Path) -> None:
    missing = tmp_path / "nope"
    with patch("server.game.items.prototype_registry.get_monitoring_dashboard") as dash_cls:
        dash = MagicMock()
        dash_cls.return_value = dash
        with pytest.raises(PrototypeRegistryError, match="not found"):
            PrototypeRegistry.load_from_path(missing)
        dash.record_registry_failure.assert_called_once()


def test_load_from_path_valid_json(tmp_path: Path) -> None:
    (tmp_path / "item.json").write_text(json.dumps(VALID_PROTOTYPE), encoding="utf-8")
    with patch("server.game.items.prototype_registry.get_monitoring_dashboard") as dash_cls:
        dash = MagicMock()
        dash_cls.return_value = dash
        registry = PrototypeRegistry.load_from_path(tmp_path)
    assert registry.get("test.item.one").name == "Test Item"


def test_load_from_path_invalid_json(tmp_path: Path) -> None:
    (tmp_path / "broken.json").write_text("{not json", encoding="utf-8")
    with patch("server.game.items.prototype_registry.get_monitoring_dashboard") as dash_cls:
        dash = MagicMock()
        dash_cls.return_value = dash
        registry = PrototypeRegistry.load_from_path(tmp_path)
    assert registry.invalid_entries() == []
    dash.record_registry_failure.assert_called()


def test_load_from_path_validation_error(tmp_path: Path) -> None:
    bad = {**VALID_PROTOTYPE, "item_type": "not_a_real_type"}
    (tmp_path / "bad.json").write_text(json.dumps(bad), encoding="utf-8")
    with patch("server.game.items.prototype_registry.get_monitoring_dashboard") as dash_cls:
        dash = MagicMock()
        dash_cls.return_value = dash
        registry = PrototypeRegistry.load_from_path(tmp_path)
    assert len(registry.invalid_entries()) == 1


def test_load_from_path_durability_anomaly(tmp_path: Path) -> None:
    payload = {
        **VALID_PROTOTYPE,
        "prototype_id": "durability.missing",
        "effect_components": ["component.durability"],
        "durability": None,
    }
    (tmp_path / "durability.json").write_text(json.dumps(payload), encoding="utf-8")
    with patch("server.game.items.prototype_registry.get_monitoring_dashboard") as dash_cls:
        dash = MagicMock()
        dash_cls.return_value = dash
        registry = PrototypeRegistry.load_from_path(tmp_path)
    assert registry.get("durability.missing") is not None
    dash.record_durability_anomaly.assert_called_once()
