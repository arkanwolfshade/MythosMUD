"""The DP rules (ADR-029 step 6a): pure functions of a player's stats, shared by the ORM Player and the registry."""

from __future__ import annotations

import pytest

from server.models.game import PositionState
from server.models.player_dp import damaged, decayed, effective_damage, healed, restored, set_to


@pytest.mark.parametrize(
    ("stats", "amount", "damage_type", "expected"),
    [
        ({"cold_resistance": 50}, 40, "cold", 20),  # halved
        ({"cold_resistance": 50}, 40, "water", 20),  # water counts as cold
        ({"cold_resistance": 99}, 1, "cold", 1),  # at least 1 gets through
        ({"cold_resistance": 250}, 40, "cold", 1),  # clamped to 100%, still at least 1
        ({"cold_resistance": "bad"}, 40, "cold", 40),
        ({"cold_resistance": 50}, 40, "physical", 40),  # only cold-type damage is resisted
        ({}, 0, "cold", 0),
        ({}, -5, "physical", 0),
    ],
)
def test_effective_damage(stats: dict[str, object], amount: int, damage_type: str, expected: int) -> None:
    assert effective_damage(stats, amount, damage_type) == expected


def test_damage_never_goes_below_zero_and_defaults_a_missing_dp_to_20() -> None:
    assert damaged({"current_dp": 3}, 10).new_dp == 0
    change = damaged({}, 5)
    assert (change.old_dp, change.new_dp, dict(change.changes)) == (20, 15, {"current_dp": 15})


def test_heal_caps_at_max_dp_with_the_body_fallback() -> None:
    assert healed({"current_dp": 10, "max_dp": 20}, 50).new_dp == 20
    assert healed({"current_dp": 10, "constitution": 60, "size": 40}, 50).new_dp == 20  # (60+40)/5
    assert healed({"current_dp": 5, "max_dp": 0}, 50).new_dp == 20  # never a 0 max


def test_set_to_changes_posture_and_reports_thresholds() -> None:
    wounded = set_to({"current_dp": 5}, -3)
    assert wounded.changes == {"current_dp": -3, "position": PositionState.LYING}
    assert wounded.became_mortally_wounded and not wounded.became_dead

    dead = set_to({"current_dp": -3}, -10)
    assert dead.became_dead and not dead.became_mortally_wounded

    revived = set_to({"current_dp": -3}, 4)
    assert revived.changes == {"current_dp": 4, "position": PositionState.STANDING}

    healthy = set_to({"current_dp": 10}, 8)
    assert healthy.changes == {"current_dp": 8}


def test_decay_bleeds_to_minus_ten_and_lays_the_player_down() -> None:
    first = decayed({"current_dp": 0, "position": PositionState.SITTING})
    assert first.changes == {"current_dp": -1, "position": PositionState.LYING}

    lying = decayed({"current_dp": -9, "position": PositionState.LYING}, 3)
    assert lying.changes == {"current_dp": -10} and lying.became_dead


def test_restored_is_full_dp_and_standing() -> None:
    change = restored({"current_dp": -10, "max_dp": 30, "position": PositionState.LYING})
    assert (change.old_dp, change.new_dp) == (-10, 30)
    assert change.changes == {"current_dp": 30, "position": PositionState.STANDING}
