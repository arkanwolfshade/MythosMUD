"""Unit tests for item catalog DML emission (ADR-026 Phase 2)."""

from server.game.items.catalog_dml import apply_weapon_dual_write, prepare_prototype, render_migration
from server.game.items.metadata_models import ItemMetadata


def test_apply_weapon_dual_write_fills_min_max_from_expr() -> None:
    metadata: dict[str, object] = {"weapon": {"damage_expr": "1d4+1", "skill": "knife"}}
    apply_weapon_dual_write(metadata)
    weapon = metadata["weapon"]
    assert isinstance(weapon, dict)
    assert weapon["min_damage"] == 2
    assert weapon["max_damage"] == 5


def test_apply_weapon_dual_write_strips_db_and_shotgun_bands() -> None:
    metadata: dict[str, object] = {"weapon": {"damage_expr": "4d6/2d6/1d6"}}
    apply_weapon_dual_write(metadata)
    weapon = metadata["weapon"]
    assert isinstance(weapon, dict)
    assert weapon["min_damage"] == 4
    assert weapon["max_damage"] == 24


def test_render_migration_includes_on_conflict_and_dual_write() -> None:
    raw: dict[str, object] = {
        "prototype_id": "era_classic.weapon.synthetic_knife",
        "name": "Field Knife",
        "short_description": "A plain steel field knife.",
        "long_description": "Synthetic catalog row for generator tests.",
        "item_type": "equipment",
        "weight": 0.5,
        "base_value": 12,
        "flags": [],
        "wear_slots": ["main_hand"],
        "usage_restrictions": {},
        "stacking_rules": {},
        "effect_components": [],
        "metadata": {
            "weapon": {"damage_expr": "1d4+1", "attacks": 1, "skill": "knife"},
            "catalog": {"namespace": "era_classic", "source_key": "synthetic_a"},
        },
        "tags": ["era_classic", "weapon"],
    }
    sql = render_migration(
        "mythos_unit",
        [raw],
        header="-- Generated item catalog DML (test).",
    )
    assert "ON CONFLICT (prototype_id) DO UPDATE SET" in sql
    assert "mythos_unit.item_prototypes" in sql
    assert '"min_damage":2' in sql.replace(" ", "")
    assert '"max_damage":5' in sql.replace(" ", "")
    model = prepare_prototype(raw)
    assert model.metadata["weapon"]["min_damage"] == 2


def test_prepare_prototype_accepts_tome_metadata() -> None:
    raw: dict[str, object] = {
        "prototype_id": "era_classic.tome.arkham_restricted_ledger",
        "name": "Arkham Restricted Ledger",
        "short_description": "A university ledger of restricted loans.",
        "long_description": "Synthetic tome row for catalog DML tests.",
        "item_type": "artifact",
        "weight": 1.2,
        "base_value": 40,
        "flags": [],
        "wear_slots": [],
        "usage_restrictions": {},
        "stacking_rules": {"max_stack": 1},
        "effect_components": [],
        "metadata": {
            "tome": {
                "sanity_loss_expr": "1d4",
                "mythos_gain": 2,
                "study_hours": 8,
                "spells": [],
            },
            "catalog": {"namespace": "era_classic", "source_key": "core_tome_01"},
        },
        "tags": ["era_classic", "tome"],
    }
    model = prepare_prototype(raw)
    assert model.item_type == "artifact"
    meta = ItemMetadata.model_validate(model.metadata)
    assert meta.tome is not None
    assert meta.tome.mythos_gain == 2


def test_prepare_prototype_accepts_equipment_skill_bonuses() -> None:
    raw: dict[str, object] = {
        "prototype_id": "era_classic.equipment.pocket_loupe",
        "name": "Pocket Loupe",
        "short_description": "A three-lens pocket magnifier.",
        "long_description": "Synthetic equipment row for catalog DML tests.",
        "item_type": "equipment",
        "weight": 0.1,
        "base_value": 2,
        "flags": [],
        "wear_slots": [],
        "usage_restrictions": {},
        "stacking_rules": {"max_stack": 1},
        "effect_components": [],
        "metadata": {
            "equipment": {
                "skill_bonuses": [{"skill": "spot_hidden", "bonus": 10}],
                "notes": "Fine detail work.",
            },
            "catalog": {"namespace": "era_classic", "source_key": "core_eq_05"},
        },
        "tags": ["era_classic", "equipment"],
    }
    model = prepare_prototype(raw)
    meta = ItemMetadata.model_validate(model.metadata)
    assert meta.equipment is not None
    assert meta.equipment.skill_bonuses is not None
    assert meta.equipment.skill_bonuses[0].skill == "spot_hidden"
    assert meta.equipment.skill_bonuses[0].bonus == 10
