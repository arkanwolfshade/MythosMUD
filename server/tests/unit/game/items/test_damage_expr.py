"""Unit tests for lossy damage_expr → min/max bridge (ADR-026)."""

import pytest

from server.game.items.damage_expr import damage_expr_to_min_max


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
