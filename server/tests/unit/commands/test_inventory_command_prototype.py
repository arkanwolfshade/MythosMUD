"""Unit tests for inventory prototype registry helpers."""

from unittest.mock import MagicMock

from server.commands.inventory_command_prototype import (
    infer_equip_slot_from_prototype,
    prototype_from_registry,
    prototype_registry_from_request,
)
from server.game.items.prototype_registry import PrototypeRegistryError


def test_prototype_registry_from_request_missing_app():
    assert prototype_registry_from_request(MagicMock(app=None)) is None


def test_prototype_registry_from_request_returns_registry():
    registry = MagicMock()
    app = MagicMock()
    app.state.prototype_registry = registry
    request = MagicMock(app=app)
    assert prototype_registry_from_request(request) is registry


def test_prototype_from_registry_missing_get():
    assert prototype_from_registry(object(), "item-1") is None


def test_prototype_from_registry_returns_prototype():
    proto = MagicMock()
    registry = MagicMock()
    registry.get.return_value = proto
    assert prototype_from_registry(registry, "item-1") is proto


def test_prototype_from_registry_swallows_registry_error():
    registry = MagicMock()
    registry.get.side_effect = PrototypeRegistryError("missing")
    assert prototype_from_registry(registry, "item-1") is None


def test_infer_equip_slot_non_inventory_stack():
    request = MagicMock()
    assert infer_equip_slot_from_prototype(request, {"slot_type": "equipped"}) is None


def test_infer_equip_slot_no_registry():
    request = MagicMock(app=MagicMock(state=MagicMock(prototype_registry=None)))
    stack = {"slot_type": "inventory", "prototype_id": "sword-1"}
    assert infer_equip_slot_from_prototype(request, stack) is None


def test_infer_equip_slot_from_wear_slots():
    proto = MagicMock(wear_slots=["main_hand"])
    registry = MagicMock()
    registry.get.return_value = proto
    app = MagicMock()
    app.state.prototype_registry = registry
    request = MagicMock(app=app)
    stack = {"slot_type": "inventory", "item_id": "sword-1"}
    assert infer_equip_slot_from_prototype(request, stack) == "main_hand"


def test_infer_equip_slot_missing_prototype():
    registry = MagicMock()
    registry.get.return_value = None
    app = MagicMock()
    app.state.prototype_registry = registry
    request = MagicMock(app=app)
    stack = {"slot_type": "inventory", "prototype_id": "missing"}
    assert infer_equip_slot_from_prototype(request, stack) is None


def test_infer_equip_slot_empty_wear_slots():
    proto = MagicMock(wear_slots=[])
    registry = MagicMock()
    registry.get.return_value = proto
    app = MagicMock()
    app.state.prototype_registry = registry
    request = MagicMock(app=app)
    stack = {"slot_type": "inventory", "prototype_id": "ring-1"}
    assert infer_equip_slot_from_prototype(request, stack) is None


def test_prototype_registry_from_request_no_state():
    app = MagicMock(state=None)
    request = MagicMock(app=app)
    assert prototype_registry_from_request(request) is None


def test_infer_equip_slot_uses_item_id():
    proto = MagicMock(wear_slots=("off_hand",))
    registry = MagicMock()
    registry.get.return_value = proto
    app = MagicMock()
    app.state.prototype_registry = registry
    request = MagicMock(app=app)
    stack = {"slot_type": "inventory", "item_id": "shield-1"}
    assert infer_equip_slot_from_prototype(request, stack) == "off_hand"


def test_infer_equip_slot_non_string_wear_slot():
    proto = MagicMock(wear_slots=[42])
    registry = MagicMock()
    registry.get.return_value = proto
    app = MagicMock()
    app.state.prototype_registry = registry
    request = MagicMock(app=app)
    stack = {"slot_type": "inventory", "prototype_id": "odd-1"}
    slot = infer_equip_slot_from_prototype(request, stack)
    assert slot == "42"


def test_infer_equip_slot_invalid_prototype_id_type():
    request = MagicMock(app=MagicMock(state=MagicMock(prototype_registry=MagicMock())))
    stack = {"slot_type": "inventory", "prototype_id": 99}
    assert infer_equip_slot_from_prototype(request, stack) is None
