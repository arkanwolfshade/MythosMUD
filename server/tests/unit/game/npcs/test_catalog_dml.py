"""Unit tests for NPC catalog DML emitter (ADR-027 Phase 2)."""

from __future__ import annotations

from typing import cast

from server.game.npcs.catalog_dml import prepare_npc_definition, render_migration


def _sample_row() -> dict[str, object]:
    return {
        "name": "Mist Hound",
        "description": "A lean hound of fog and teeth.",
        "hostility": "aggressive",
        "base_stats": {
            "determination_points": 10,
            "max_dp": 10,
            "xp_value": 20,
            "dexterity": 60,
            "catalog": {
                "namespace": "era_classic",
                "canonical_id": "era_classic.npc.mist_hound",
                "era": "1920s",
                "source_key": "synthetic_core_01",
            },
            "attacks": [{"name": "bite", "damage_expr": "1d6+1", "skill": "brawl"}],
            "armor": {"armor_points": 0, "coverage": "none"},
        },
    }


def test_prepare_forces_arena_inert_and_dual_write() -> None:
    prepared = prepare_npc_definition(_sample_row())
    assert prepared["sub_zone_id"] == "arena"
    assert prepared["room_id"] is None
    assert prepared["required_npc"] is False
    assert prepared["max_population"] == 0
    assert prepared["spawn_probability"] == 0.0
    assert prepared["npc_type"] == "aggressive_mob"
    base_stats = cast(dict[str, object], prepared["base_stats"])
    attacks_raw = base_stats["attacks"]
    assert isinstance(attacks_raw, list)
    attacks = cast(list[object], attacks_raw)
    first_raw = attacks[0]
    assert isinstance(first_raw, dict)
    first = cast(dict[str, object], first_raw)
    assert first["min_damage"] == 2
    assert first["max_damage"] == 7
    behavior = cast(dict[str, object], prepared["behavior_config"])
    assert behavior["attack_damage"] == 4


def test_render_migration_uses_name_sub_zone_conflict() -> None:
    sql = render_migration("mythos_unit", [_sample_row()], header="-- test\n")
    assert "ON CONFLICT (name, sub_zone_id) DO UPDATE SET" in sql
    assert "INSERT INTO mythos_unit.npc_definitions" in sql
    assert "'arena'" in sql
