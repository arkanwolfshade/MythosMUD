"""Unit tests for lossy damage_expr → min/max bridge re-export (ADR-026)."""

from server.game.items.damage_expr import damage_expr_to_min_max


def test_items_damage_expr_reexports_shared_helper() -> None:
    assert damage_expr_to_min_max("1d4+1") == (2, 5)
