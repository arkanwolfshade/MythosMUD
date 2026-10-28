"""Unit tests for ADR-026 item metadata Pydantic contracts."""

import pytest
from pydantic import ValidationError

from server.constants.containers import MAX_CONTAINER_CAPACITY_SLOTS
from server.game.items.metadata_models import ItemMetadata, WeaponMetadata


def test_item_metadata_accepts_legacy_weapon_ints() -> None:
    meta = ItemMetadata.model_validate(
        {
            "weapon": {
                "min_damage": 1,
                "max_damage": 4,
                "modifier": 0,
                "damage_types": ["slashing"],
                "magical": False,
            },
            "lore_note": "allowed open key",
        }
    )
    assert meta.weapon is not None
    assert meta.weapon.min_damage == 1
    assert meta.weapon.max_damage == 4


def test_item_metadata_accepts_rich_dual_write_weapon() -> None:
    weapon = WeaponMetadata.model_validate(
        {
            "min_damage": 2,
            "max_damage": 9,
            "modifier": 0,
            "damage_types": ["slashing"],
            "magical": False,
            "damage_expr": "1d8+1",
            "attacks": 1,
            "skill": "sword",
        }
    )
    meta = ItemMetadata.model_validate(
        {
            "weapon": weapon.model_dump(exclude_none=True),
            "catalog": {"namespace": "era_classic", "source_key": "synthetic_a"},
            "armor": {"armor_points": 1, "coverage": "torso"},
        }
    )
    assert meta.catalog is not None
    assert meta.catalog.namespace == "era_classic"
    assert meta.armor is not None
    assert meta.armor.armor_points == 1


def test_item_metadata_container_defaults_and_cap() -> None:
    meta = ItemMetadata.model_validate({"container": {"capacity_slots": MAX_CONTAINER_CAPACITY_SLOTS}})
    assert meta.container is not None
    assert meta.container.capacity_slots == MAX_CONTAINER_CAPACITY_SLOTS
    assert meta.container.lock_state == "unlocked"
    assert meta.container.allowed_roles == []


@pytest.mark.parametrize(
    "container",
    [
        {"capacity_slots": MAX_CONTAINER_CAPACITY_SLOTS + 1},
        {"capacity_slots": 0},
        {"capacity_slots": 10, "lock_state": "ajar"},
        {"capcity_slots": 10},  # typo'd key must not be silently ignored
    ],
)
def test_item_metadata_container_rejects_invalid(container: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        _ = ItemMetadata.model_validate({"container": container})


def test_item_metadata_accepts_lucidity_recovery() -> None:
    meta = ItemMetadata.model_validate(
        {"lucidity_recovery": {"cooldown_key": "folk_tonic", "lcd_delta": 3, "cooldown_minutes": 30}}
    )
    assert meta.lucidity_recovery is not None
    assert meta.lucidity_recovery.cooldown_key == "folk_tonic"
    assert meta.lucidity_recovery.lcd_delta == 3
    assert meta.lucidity_recovery.cooldown_minutes == 30


@pytest.mark.parametrize(
    "payload",
    [
        {"lcd_delta": 3, "cooldown_minutes": 30},
        {"cooldown_key": "", "lcd_delta": 3, "cooldown_minutes": 30},
        {"cooldown_key": "folk_tonic", "lcd_delta": 0, "cooldown_minutes": 30},
        {"cooldown_key": "folk_tonic", "lcd_delta": 3, "cooldown_minutes": 0},
        {"cooldown_key": "folk_tonic", "lcd_delta": 3, "cooldown_minutes": 30, "typo": 1},
    ],
)
def test_item_metadata_rejects_bad_lucidity_recovery(payload: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        _ = ItemMetadata.model_validate({"lucidity_recovery": payload})
