"""Shared inventory fixtures for MythosMUD tests."""

from __future__ import annotations

import pytest


@pytest.fixture
def empty_inventory() -> list[dict[str, object]]:
    """Represent an unburdened investigator with no items equipped or stored."""
    return []


@pytest.fixture
def partial_inventory() -> list[dict[str, object]]:
    """Provide a small cross-section of eldritch gear without hitting capacity limits."""
    return [
        {
            "item_id": "sigil_elder_sign",
            "item_name": "Elder Sign Token",
            "slot_type": "backpack",
            "quantity": 1,
            "metadata": {"protection": "outer_god", "attuned": False},
        },
        {
            "item_id": "lantern_battered",
            "item_name": "Battered Lantern",
            "slot_type": "left_hand",
            "quantity": 1,
            "metadata": {"fuel_level": 0.35, "last_refilled_by": "Prof. Armitage"},
        },
        {
            "item_id": "tonic_laudanum",
            "item_name": "Laudanum Tonic",
            "slot_type": "backpack",
            "quantity": 3,
            "metadata": {"dose_size_ml": 10, "apothecary": "Ma's Apotheca"},
        },
    ]


@pytest.fixture
def full_inventory() -> list[dict[str, object]]:
    """Generate a packed inventory reaching the canonical 20-slot cap."""
    payload: list[dict[str, object]] = []
    for index in range(20):
        payload.append(
            {
                "item_id": f"specimen_{index:02}",
                "item_name": f"Labeled Specimen #{index:02}",
                "slot_type": "backpack",
                "quantity": 1,
                "metadata": {"provenance": "Miskatonic Vault", "catalog_id": f"VAULT-{index:02}"},
            }
        )
    return payload
