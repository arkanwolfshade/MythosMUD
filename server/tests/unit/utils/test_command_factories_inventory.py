import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import (
    DropCommand,
    EquipCommand,
    GetCommand,
    InventoryCommand,
    PickupCommand,
    PutCommand,
    UnequipCommand,
)
from server.utils.command_factories_inventory import InventoryCommandFactory


def test_inventory_command_accepts_no_args() -> None:
    """Inventory requires zero arguments."""
    command = InventoryCommandFactory.create_inventory_command([])
    assert isinstance(command, InventoryCommand)


def test_inventory_command_rejects_extra_args() -> None:
    """Inventory should fail when unexpected arguments are provided."""
    with pytest.raises(MythosValidationError):
        InventoryCommandFactory.create_inventory_command(["extra"])


@pytest.mark.parametrize(
    ("args", "expected_index", "expected_quantity", "expected_search_term"),
    [
        (["3", "2"], 3, 2, None),
        (["silver", "sword", "5"], None, 5, "silver sword"),
    ],
)
def test_pickup_command_parses_index_or_name(
    args: list[str], expected_index: int | None, expected_quantity: int | None, expected_search_term: str | None
) -> None:
    """Pickup supports numeric or name selectors plus optional quantity."""
    command = InventoryCommandFactory.create_pickup_command(args)
    assert isinstance(command, PickupCommand)
    assert command.index == expected_index
    assert command.quantity == expected_quantity
    assert command.search_term == expected_search_term


@pytest.mark.parametrize(
    "args",
    [
        [],
        ["0"],
        ["1", "0"],
    ],
)
def test_pickup_command_validation_errors(args: list[str]) -> None:
    """Pickup rejects empty args, non-positive index, and non-positive quantity."""
    with pytest.raises(MythosValidationError):
        InventoryCommandFactory.create_pickup_command(args)


def test_drop_command_accepts_index_and_optional_quantity() -> None:
    command = InventoryCommandFactory.create_drop_command(["4", "2"])
    assert isinstance(command, DropCommand)
    assert command.index == 4
    assert command.quantity == 2


@pytest.mark.parametrize(
    "args",
    [
        [],
        ["not-a-number"],
        ["1", "not-a-number"],
    ],
)
def test_drop_command_validation_errors(args: list[str]) -> None:
    with pytest.raises(MythosValidationError):
        InventoryCommandFactory.create_drop_command(args)


def test_put_command_parses_item_container_and_quantity() -> None:
    command = InventoryCommandFactory.create_put_command(["gem", "in", "bag", "3"])
    assert isinstance(command, PutCommand)
    assert command.item == "gem"
    assert command.container == "bag"
    assert command.quantity == 3


def test_put_command_rejects_missing_parts() -> None:
    with pytest.raises(MythosValidationError):
        InventoryCommandFactory.create_put_command(["only-item"])


def test_get_command_parses_item_container_and_quantity() -> None:
    command = InventoryCommandFactory.create_get_command(["potion", "from", "satchel", "2"])
    assert isinstance(command, GetCommand)
    assert command.item == "potion"
    assert command.container == "satchel"
    assert command.quantity == 2


def test_get_command_rejects_missing_parts() -> None:
    with pytest.raises(MythosValidationError):
        InventoryCommandFactory.create_get_command([])


def test_equip_command_accepts_numeric_index_and_slot() -> None:
    command = InventoryCommandFactory.create_equip_command(["2", "Head"])
    assert isinstance(command, EquipCommand)
    assert command.index == 2
    assert command.search_term is None
    assert command.target_slot == "head"


def test_equip_command_accepts_name_and_infers_slot() -> None:
    command = InventoryCommandFactory.create_equip_command(["silver", "helm", "head"])
    assert isinstance(command, EquipCommand)
    assert command.index is None
    assert command.search_term == "silver helm"
    assert command.target_slot == "head"


def test_equip_command_rejects_non_positive_index() -> None:
    with pytest.raises(MythosValidationError):
        InventoryCommandFactory.create_equip_command(["0"])


def test_unequip_command_accepts_known_slot() -> None:
    command = InventoryCommandFactory.create_unequip_command(["Head"])
    assert isinstance(command, UnequipCommand)
    assert command.slot == "head"
    assert command.search_term is None


def test_unequip_command_accepts_item_name() -> None:
    command = InventoryCommandFactory.create_unequip_command(["ancient", "ring"])
    assert isinstance(command, UnequipCommand)
    assert command.slot is None
    assert command.search_term == "ancient ring"
