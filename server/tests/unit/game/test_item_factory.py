import json
from pathlib import Path

import pytest

from server.game.items import ItemFactory, ItemFactoryError, PrototypeRegistry


def write_prototype(directory: Path, filename: str, payload: dict) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / filename).write_text(json.dumps(payload, indent=2), encoding="utf-8")


@pytest.fixture()
def prototype_directory(tmp_path: Path) -> Path:
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
        "usage_restrictions": {},
        "stacking_rules": {"max_stack": 1},
        "effect_components": ["component.sanity_whisper"],
        "metadata": {"lore": "Restricted Archive shelf A-17"},
        "tags": ["lore", "codex"],
    }
    write_prototype(tmp_path, "artifact_codex.json", payload)
    return tmp_path


def build_factory(directory: Path) -> ItemFactory:
    registry = PrototypeRegistry.load_from_path(directory)
    return ItemFactory(registry)


def test_factory_creates_instance_with_overrides(prototype_directory: Path):
    factory = build_factory(prototype_directory)

    instance = factory.create_instance(
        "artifact.miskatonic.codex",
        quantity=2,
        overrides={
            "name": "Codex of Forbidden Dreams",
            "metadata": {"edition": "expurgated"},
            "flags": ["MAGICAL"],
        },
        origin={"source": "admin_spawn"},
        slot_type="backpack",
    )

    assert instance.prototype_id == "artifact.miskatonic.codex"
    assert instance.name == "Codex of Forbidden Dreams"
    assert instance.quantity == 2
    assert instance.slot_type == "backpack"
    assert instance.flags == ["MAGICAL"]
    assert instance.metadata["edition"] == "expurgated"
    assert instance.origin["source"] == "admin_spawn"
    assert instance.metadata["components"] == ["component.sanity_whisper"]
    assert "item_instance_id" in instance.to_inventory_stack()


def test_factory_respects_default_slot_from_prototype(prototype_directory: Path):
    factory = build_factory(prototype_directory)
    instance = factory.create_instance("artifact.miskatonic.codex")

    assert instance.slot_type == "off_hand"


def test_factory_rejects_invalid_quantity(prototype_directory: Path):
    factory = build_factory(prototype_directory)

    with pytest.raises(ItemFactoryError):
        factory.create_instance("artifact.miskatonic.codex", quantity=0)


def test_factory_raises_for_missing_prototype(tmp_path: Path):
    factory = build_factory(tmp_path)

    with pytest.raises(ItemFactoryError):
        factory.create_instance("artifact.unknown")
