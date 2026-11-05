"""The MP rules (ADR-029 step 6b): pure functions of a player's stats."""

from __future__ import annotations

from server.models.player_mp import after_gaining, after_spending, max_mp_of, mp_of, set_to


def test_mp_of_defaults_to_zero_and_coerces() -> None:
    assert mp_of({}) == 0
    assert mp_of({"magic_points": "7"}) == 7
    assert mp_of({"magic_points": 3.9}) == 3  # a row an older build saved as a fraction


def test_max_mp_is_the_stored_value_else_from_power() -> None:
    assert max_mp_of({"max_magic_points": 12, "power": 80}) == 12
    assert max_mp_of({"power": 80}) == 16  # ceil(80 * 0.2)
    assert max_mp_of({}) == 10  # the default POW of 50


def test_spending_never_goes_below_zero() -> None:
    assert after_spending({"magic_points": 10}, 3).new_mp == 7
    assert after_spending({"magic_points": 2}, 5).new_mp == 0


def test_gaining_keeps_whole_mp_and_caps_at_max() -> None:
    stats = {"magic_points": 2, "max_magic_points": 10}
    change = after_gaining(stats, 1.8)
    assert (change.old_mp, change.new_mp, change.max_mp, change.gained) == (2, 3, 10, 1)
    assert after_gaining(stats, 50).new_mp == 10


def test_gaining_leaves_mp_an_admin_set_above_the_max() -> None:
    change = after_gaining({"magic_points": 15, "max_magic_points": 10}, 5)
    assert (change.new_mp, change.gained) == (15, 0)


def test_set_to_may_exceed_the_max() -> None:
    assert set_to({"magic_points": 1, "max_magic_points": 10}, 15).new_mp == 15
