"""Unit tests for item prototype Pydantic models."""

import pytest
from pydantic import ValidationError

from server.game.items.constants import ALLOWED_FLAGS, ALLOWED_ITEM_TYPES, ALLOWED_WEAR_SLOTS
from server.game.items.models import ItemPrototypeModel


def _valid_payload(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "prototype_id": "test_lantern",
        "name": "Brass Lantern",
        "short_description": "A tarnished brass lantern.",
        "long_description": "A tarnished brass lantern that flickers with unsettling light.",
        "item_type": next(iter(ALLOWED_ITEM_TYPES)),
        "weight": 1.0,
        "base_value": 10,
    }
    base.update(overrides)
    return base


def test_item_prototype_valid_minimal() -> None:
    model = ItemPrototypeModel.model_validate(_valid_payload())
    assert model.prototype_id == "test_lantern"


def test_item_prototype_rejects_invalid_item_type() -> None:
    with pytest.raises(ValidationError, match="item_type"):
        ItemPrototypeModel.model_validate(_valid_payload(item_type="forbidden_type"))


def test_item_prototype_rejects_invalid_flags() -> None:
    with pytest.raises(ValidationError, match="Invalid flags"):
        ItemPrototypeModel.model_validate(_valid_payload(flags=["not_a_real_flag"]))


def test_item_prototype_accepts_valid_flags() -> None:
    flag = next(iter(ALLOWED_FLAGS))
    model = ItemPrototypeModel.model_validate(_valid_payload(flags=[flag]))
    assert model.flags == [flag]


def test_item_prototype_rejects_invalid_wear_slots() -> None:
    with pytest.raises(ValidationError, match="Invalid wear slots"):
        ItemPrototypeModel.model_validate(_valid_payload(wear_slots=["invalid_slot"]))


def test_item_prototype_accepts_valid_wear_slots() -> None:
    slot = next(iter(ALLOWED_WEAR_SLOTS))
    model = ItemPrototypeModel.model_validate(_valid_payload(wear_slots=[slot]))
    assert model.wear_slots == [slot]


def test_item_prototype_rejects_empty_effect_components() -> None:
    with pytest.raises(ValidationError, match="effect_components"):
        ItemPrototypeModel.model_validate(_valid_payload(effect_components=["   "]))


def test_item_prototype_normalizes_effect_components_and_tags() -> None:
    model = ItemPrototypeModel.model_validate(
        _valid_payload(effect_components=["  glow  "], tags=["  mythos ", "", "artifact"])
    )
    assert model.effect_components == ["glow"]
    assert model.tags == ["mythos", "artifact"]
