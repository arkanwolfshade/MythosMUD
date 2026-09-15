"""Unit tests for ADR-026 item metadata Pydantic contracts."""

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
