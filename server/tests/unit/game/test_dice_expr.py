"""Unit tests for shared damage_expr helpers (ADR-026 / ADR-027)."""

from __future__ import annotations

import random

import pytest

from server.game.dice_expr import damage_expr_to_min_max, roll_damage_expr


@pytest.mark.parametrize(
    ("expr", "expected"),
    [
        ("1d8", (1, 8)),
        ("1d8+1", (2, 9)),
        ("2d6", (2, 12)),
        ("1d10+1d4", (2, 14)),
        ("1D3+1", (2, 4)),
        ("1d6+DB", (1, 6)),
        ("  1d4-1  ", (0, 3)),
    ],
)
def test_damage_expr_to_min_max(expr: str, expected: tuple[int, int]) -> None:
    assert damage_expr_to_min_max(expr) == expected


def test_damage_expr_rejects_empty() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        _ = damage_expr_to_min_max("   ")


def test_damage_expr_rejects_unparseable() -> None:
    with pytest.raises(ValueError, match="unparseable"):
        _ = damage_expr_to_min_max("DB only")


def test_roll_damage_expr_deterministic() -> None:
    rng = random.Random(0)
    assert roll_damage_expr("1d1+2", rng=rng) == 3


def test_roll_damage_expr_within_bounds() -> None:
    lo, hi = damage_expr_to_min_max("2d6+1")
    rng = random.Random(42)
    for _ in range(40):
        rolled = roll_damage_expr("2d6+1", rng=rng)
        assert lo <= rolled <= hi


def test_roll_damage_expr_rejects_empty() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        _ = roll_damage_expr("")
