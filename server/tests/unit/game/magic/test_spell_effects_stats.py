"""Unit tests for spell_effects_stats helpers."""

from server.game.magic.spell_effects_stats import apply_stat_modifications


def test_apply_stat_modifications_basic() -> None:
    stats = {"strength": 50}
    updated, changes, modified = apply_stat_modifications(
        stats, {"strength": 10}, mastery_modifier=1.0, spell_id="spell_1"
    )
    assert updated["strength"] == 60
    assert changes["strength"] == 10
    assert modified == ["strength (+10)"]


def test_apply_stat_modifications_clamps_to_bounds() -> None:
    stats = {"dexterity": 95}
    updated, _, _ = apply_stat_modifications(stats, {"dexterity": 20}, 1.0, "s")
    assert updated["dexterity"] == 100


def test_apply_stat_modifications_skips_invalid_stat() -> None:
    stats = {"strength": 50}
    updated, changes, modified = apply_stat_modifications(stats, {"invalid_stat": 5}, 1.0, "s")
    assert updated["strength"] == 50
    assert changes == {}
    assert modified == []


def test_apply_stat_modifications_string_coercion() -> None:
    stats = {"power": 40}
    updated, changes, _ = apply_stat_modifications(stats, {"power": "5"}, 2.0, "s")
    assert updated["power"] == 50
    assert changes["power"] == 10


def test_apply_stat_modifications_bad_string_skipped() -> None:
    stats = {"luck": 50}
    updated, changes, _ = apply_stat_modifications(stats, {"luck": "not-a-number"}, 1.0, "s")
    assert updated["luck"] == 50
    assert changes == {}
