"""Unit tests for item component hooks."""

from unittest.mock import MagicMock

from server.game.items.component_hooks import initialize_components


def test_initialize_components_empty_prototype():
    prototype = MagicMock(effect_components=[])
    assert initialize_components(prototype) == {}


def test_initialize_components_records_prototype_components():
    prototype = MagicMock(prototype_id="p1", effect_components=["burn", "glow"])
    metadata = initialize_components(prototype)
    assert metadata["components"] == ["burn", "glow"]


def test_initialize_components_merges_overrides():
    prototype = MagicMock(prototype_id="p2", effect_components=["base"])
    overrides = {
        "metadata": {"color": "green"},
        "effect_components": ["override"],
    }
    metadata = initialize_components(prototype, overrides)
    assert metadata["components"] == ["base"]
    assert metadata["overrides"]["metadata"] == {"color": "green"}
    assert metadata["overrides"]["effect_components"] == ["override"]
