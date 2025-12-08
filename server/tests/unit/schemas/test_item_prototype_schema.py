import pytest
from pydantic import ValidationError

from server.game.items.models import ItemPrototypeModel


def build_valid_payload(**overrides):
    payload = {
        "prototype_id": "artifact.miskatonic.codex",
        "name": "Codex of Whispered Secrets",
        "short_description": "a codex bound in eel-skin",
        "long_description": "Pages that shimmer with impossible glyphs.",
        "item_type": "artifact",
        "weight": 3.5,
        "base_value": 1200,
        "durability": 100,
        "flags": ["MAGICAL", "NO_DROP"],
        "wear_slots": ["off_hand"],
        "usage_restrictions": {"faction": ["miskatonic"]},
        "stacking_rules": {"max_stack": 1},
        "effect_components": ["component.Lucidity_whisper"],
        "metadata": {"lore": "Restricted Archive shelf A-17"},
        "tags": ["lore", "codex"],
    }
    payload.update(overrides)
    return payload


def test_valid_prototype_payload_passes_validation():
    payload = build_valid_payload()

    prototype = ItemPrototypeModel.model_validate(payload)

    assert prototype.prototype_id == payload["prototype_id"]
    assert "lore" in prototype.tags


@pytest.mark.parametrize("missing_field", ["prototype_id", "name", "item_type"])
def test_missing_required_field_raises_validation_error(missing_field):
    payload = build_valid_payload()
    payload.pop(missing_field)

    with pytest.raises(ValidationError):
        ItemPrototypeModel.model_validate(payload)


def test_flags_must_be_known_identifiers():
    payload = build_valid_payload(flags=["UNKNOWN_FLAG"])

    with pytest.raises(ValidationError):
        ItemPrototypeModel.model_validate(payload)


def test_weight_and_durability_constraints_enforced():
    payload = build_valid_payload(weight=-1, durability=-5)

    with pytest.raises(ValidationError):
        ItemPrototypeModel.model_validate(payload)


def test_effect_components_must_be_non_empty_strings():
    payload = build_valid_payload(effect_components=["", 7])

    with pytest.raises(ValidationError):
        ItemPrototypeModel.model_validate(payload)
