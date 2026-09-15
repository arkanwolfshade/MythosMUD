"""Unit tests for NPC attack damage resolution (ADR-027 Phase 3)."""

from __future__ import annotations

import random
from uuid import UUID

from server.game.npcs.attack_damage import armor_points_from_base_stats, resolve_npc_attack_damage
from server.models.combat import CombatParticipant, CombatParticipantType


def test_resolve_prefers_damage_expr() -> None:
    stats: dict[str, object] = {
        "attacks": [{"damage_expr": "1d1+2", "min_damage": 9, "max_damage": 9}],
    }
    rng = random.Random(0)
    assert resolve_npc_attack_damage(stats, {"attack_damage": 99}, rng=rng) == 3


def test_resolve_falls_back_to_min_max_without_expr() -> None:
    stats: dict[str, object] = {"attacks": [{"min_damage": 4, "max_damage": 4}]}
    assert resolve_npc_attack_damage(stats, {"attack_damage": 1}) == 4


def test_resolve_falls_back_to_behavior_attack_damage() -> None:
    assert resolve_npc_attack_damage({}, {"attack_damage": 7}) == 7


def test_armor_points_from_base_stats() -> None:
    assert armor_points_from_base_stats({"armor": {"armor_points": 2}}) == 2
    assert armor_points_from_base_stats({}) == 0


def test_apply_damage_subtracts_armor_points() -> None:
    target = CombatParticipant(
        participant_id=UUID("00000000-0000-4000-8000-0000000000a1"),
        participant_type=CombatParticipantType.NPC,
        name="Cellar Shambler",
        current_dp=10,
        max_dp=10,
        dexterity=40,
        armor_points=1,
    )
    old_dp, died, _ = target.apply_damage(5)
    assert old_dp == 10
    assert target.current_dp == 6
    assert died is False
