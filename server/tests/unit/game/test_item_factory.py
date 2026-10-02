"""Unit tests for ItemFactory."""

from types import SimpleNamespace
from typing import cast
from unittest.mock import MagicMock, patch

import pytest

from server.game.items.item_factory import ItemFactory, ItemFactoryError
from server.game.items.prototype_registry import PrototypeRegistryError


@pytest.fixture
def factory() -> ItemFactory:
    registry = MagicMock()
    return ItemFactory(registry)


def test_create_instance_invalid_quantity(factory: ItemFactory) -> None:
    with pytest.raises(ItemFactoryError, match="positive integer"):
        factory.create_instance("proto-1", quantity=0)


def test_create_instance_prototype_not_found(factory: ItemFactory) -> None:
    factory._registry.get.side_effect = PrototypeRegistryError("missing")
    with pytest.raises(ItemFactoryError, match="not found"):
        factory.create_instance("missing-proto")


def test_create_instance_success(factory: ItemFactory) -> None:
    prototype = SimpleNamespace(
        prototype_id="proto-1",
        name="Lantern",
        wear_slots=["hand"],
        metadata={"weight": 1},
        flags=["light"],
    )
    factory._registry.get.return_value = prototype

    with patch("server.game.items.item_factory.initialize_components", return_value=None):
        instance = factory.create_instance("proto-1", quantity=2, origin={"source": "loot"})

    assert instance.prototype_id == "proto-1"
    assert instance.name == "Lantern"
    assert instance.quantity == 2
    assert instance.slot_type == "hand"
    assert instance.origin == {"source": "loot"}


def test_create_instance_with_overrides(factory: ItemFactory) -> None:
    prototype = SimpleNamespace(
        prototype_id="proto-2",
        name="Sword",
        wear_slots=[],
        metadata={},
        flags=["sharp"],
    )
    factory._registry.get.return_value = prototype

    with patch("server.game.items.item_factory.initialize_components", return_value={"components": ["blade"]}):
        instance = factory.create_instance(
            "proto-2",
            overrides={"name": "Rusty Sword", "flags": ["dull"], "metadata": {"rust": True}},
            slot_type="weapon",
        )

    assert instance.name == "Rusty Sword"
    assert instance.slot_type == "weapon"
    assert instance.flags == ["dull"]


def _factory_for(prototype: SimpleNamespace) -> ItemFactory:
    registry = MagicMock()
    registry.configure_mock(**{"get.return_value": prototype})
    return ItemFactory(registry)


def test_create_instance_builds_inner_container_from_prototype() -> None:
    prototype = SimpleNamespace(
        prototype_id="furniture.chest",
        name="Chest",
        wear_slots=[],
        metadata={"container": {"capacity_slots": 200, "lock_state": "locked", "allowed_roles": ["admin"]}},
        flags=[],
    )

    with patch("server.game.items.item_factory.initialize_components", return_value=None):
        instance = _factory_for(prototype).create_instance("furniture.chest")

    expected = {"capacity_slots": 200, "lock_state": "locked", "allowed_roles": ["admin"], "items": []}
    assert instance.inner_container == expected
    stack = instance.to_inventory_stack()
    assert stack["inner_container"] == expected
    # The stack gets its own copy: filling it must not leak back into the instance.
    inner = cast(dict[str, list[object]], stack["inner_container"])
    inner["items"].append({"item_id": "x"})
    assert instance.inner_container == expected


def test_create_instance_without_container_has_no_inner_container() -> None:
    prototype = SimpleNamespace(prototype_id="proto-3", name="Rock", wear_slots=[], metadata={}, flags=[])

    with patch("server.game.items.item_factory.initialize_components", return_value=None):
        instance = _factory_for(prototype).create_instance("proto-3")

    assert instance.inner_container is None
    assert "inner_container" not in instance.to_inventory_stack()
