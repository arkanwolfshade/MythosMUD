"""Inventory serialization contract tests."""

from __future__ import annotations

import json
from typing import Any

import pytest

from server.models.player import Player
from server.schemas.inventory_schema import (
    InventorySchemaValidationError,
    validate_inventory_items,
    validate_inventory_payload,
)


def build_player(player_id: str = "inventory-player", user_id: str = "inventory-user") -> Player:
    """Create a minimal Player entity suitable for inventory testing."""
    return Player(player_id=player_id, user_id=user_id, name="Test Investigator")


def into_payload(items: list[dict[str, Any]], equipped: dict[str, dict[str, Any]] | None = None) -> dict[str, Any]:
    """Assemble a canonical payload for schema validation."""
    return {"inventory": items, "equipped": equipped or {}, "version": 1}


def test_empty_inventory_round_trip(empty_inventory: list[dict[str, Any]]):
    player = build_player("inventory-empty")
    player.set_inventory(empty_inventory)

    assert player.inventory == "[]"
    assert player.get_inventory() == empty_inventory

    validate_inventory_items(empty_inventory)
    validate_inventory_payload(into_payload(empty_inventory))


def test_partial_inventory_serializes_to_json(
    partial_inventory: list[dict[str, Any]],
):
    player = build_player("inventory-partial")
    player.set_inventory(partial_inventory)

    serialized = json.loads(player.inventory)  # type: ignore[arg-type]
    assert serialized == partial_inventory

    round_tripped = player.get_inventory()
    assert round_tripped == partial_inventory

    validate_inventory_items(partial_inventory)
    validate_inventory_payload(into_payload(partial_inventory))


def test_full_inventory_obeys_slot_limit(full_inventory: list[dict[str, Any]]):
    assert len(full_inventory) == 20

    player = build_player("inventory-full")
    player.set_inventory(full_inventory)
    decoded = player.get_inventory()

    assert decoded == full_inventory
    validate_inventory_items(full_inventory)


def test_equipped_payload_requires_single_quantity(partial_inventory: list[dict[str, Any]]):
    equipped = {
        "left_hand": {
            **partial_inventory[1],
            "quantity": 1,
        }
    }

    validate_inventory_payload(into_payload(partial_inventory, equipped))

    bad_equipped = {"left_hand": {**partial_inventory[1], "quantity": 2}}
    with pytest.raises(InventorySchemaValidationError):
        validate_inventory_payload(into_payload(partial_inventory, bad_equipped))
