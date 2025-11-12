import json
from pathlib import Path

import pytest

from server.game.items.prototype_registry import PrototypeRegistry, PrototypeRegistryError


def write_prototype(directory: Path, name: str, payload: dict) -> Path:
    file_path = directory / f"{name}.json"
    file_path.write_text(json.dumps(payload, indent=2))
    return file_path


@pytest.fixture()
def valid_payload():
    return {
        "prototype_id": "artifact.miskatonic.codex",
        "name": "Codex of Whispered Secrets",
        "short_description": "a codex bound in eel-skin",
        "long_description": "Pages that shimmer with impossible glyphs.",
        "item_type": "artifact",
        "weight": 3.5,
        "base_value": 1200,
        "durability": 100,
        "flags": ["MAGICAL", "NO_DROP"],
        "wear_slots": ["OFF_HAND"],
        "usage_restrictions": {"faction": ["miskatonic"]},
        "stacking_rules": {"max_stack": 1},
        "effect_components": ["component.sanity_whisper"],
        "metadata": {"lore": "Restricted Archive shelf A-17"},
        "tags": ["lore", "codex"],
    }


def test_registry_loads_valid_prototypes(tmp_path: Path, valid_payload: dict):
    write_prototype(tmp_path, "artifact_codex", valid_payload)
    registry = PrototypeRegistry.load_from_path(tmp_path)

    result = registry.get("artifact.miskatonic.codex")

    assert result.prototype_id == "artifact.miskatonic.codex"
    assert result.name == "Codex of Whispered Secrets"


def test_registry_skips_invalid_prototypes_and_logs_warning(tmp_path: Path, caplog):
    valid = {
        "prototype_id": "weapon.eldritch.dagger",
        "name": "Eldritch Dagger",
        "short_description": "a dagger humming with void-light",
        "long_description": "Its edge never dulls.",
        "item_type": "equipment",
        "weight": 1.2,
        "base_value": 450,
        "durability": 50,
        "flags": ["MAGICAL"],
        "wear_slots": ["MAIN_HAND"],
        "usage_restrictions": {},
        "stacking_rules": {"max_stack": 1},
        "effect_components": ["component.void_edge"],
        "metadata": {},
        "tags": ["weapon", "eldritch"],
    }
    invalid = {**valid, "prototype_id": ""}  # invalid due to empty identifier
    write_prototype(tmp_path, "valid_dagger", valid)
    write_prototype(tmp_path, "invalid_dagger", invalid)

    with caplog.at_level("WARNING"):
        registry = PrototypeRegistry.load_from_path(tmp_path)

    assert registry.get("weapon.eldritch.dagger").name == "Eldritch Dagger"
    assert any("invalid prototype payload" in record.message for record in caplog.records)
    assert registry.invalid_entries()[0]["prototype_id"] == "invalid_dagger"


def test_registry_get_raises_for_missing_prototype(tmp_path: Path, valid_payload: dict):
    write_prototype(tmp_path, "artifact_codex", valid_payload)
    registry = PrototypeRegistry.load_from_path(tmp_path)

    with pytest.raises(PrototypeRegistryError):
        registry.get("missing.prototype")


def test_registry_find_by_tag_returns_matching_prototypes(tmp_path: Path, valid_payload: dict):
    lore_payload = valid_payload
    weapon_payload = {
        **valid_payload,
        "prototype_id": "weapon.eldritch.dagger",
        "name": "Eldritch Dagger",
        "item_type": "equipment",
        "tags": ["weapon"],
        "wear_slots": ["MAIN_HAND"],
    }
    write_prototype(tmp_path, "artifact_codex", lore_payload)
    write_prototype(tmp_path, "weapon_dagger", weapon_payload)
    registry = PrototypeRegistry.load_from_path(tmp_path)

    lore_prototypes = registry.find_by_tag("lore")
    weapon_prototypes = registry.find_by_tag("weapon")

    assert [prototype.prototype_id for prototype in lore_prototypes] == ["artifact.miskatonic.codex"]
    assert [prototype.prototype_id for prototype in weapon_prototypes] == ["weapon.eldritch.dagger"]
