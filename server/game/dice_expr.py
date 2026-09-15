"""Shared damage_expr helpers for catalog dual-write and combat rolls.

Used by item and NPC catalog pipelines (ADR-026 / ADR-027).

Lossy rules for ``damage_expr_to_min_max``:
- Sum of terms ``NdM`` / ``NdM+K`` / ``NdM-K`` / bare integers (case-insensitive).
- Unknown alphabetic suffixes (e.g. ``+DB``) are ignored after a trailing ``+``/``-``.
- Min = sum(dice counts) + flat modifiers; max = sum(count * faces) + flats.
- Empty or unparseable expressions raise ``ValueError``.

``roll_damage_expr`` uses the same parse rules and rolls each die once.
"""

from __future__ import annotations

import random
import re
import secrets
from collections.abc import Callable

_DICE_TERM_RE = re.compile(r"^(\d+)\s*[dD]\s*(\d+)$")
_FLAT_TERM_RE = re.compile(r"^[+-]?\d+$")
_TRAILING_ALPHA = re.compile(r"[+-]\s*[A-Za-z_][A-Za-z0-9_]*\s*$")
_TERM_SPLIT_RE = re.compile(r"(?=[+-])")

_RollInt = Callable[[int, int], int]


def _strip_trailing_alpha(working: str) -> str:
    """Drop trailing +DB / -flavor suffixes until none remain."""
    while True:
        next_pass = _TRAILING_ALPHA.sub("", working).strip()
        if next_pass == working:
            return working
        working = next_pass


def _parse_terms(expr: str) -> list[str]:
    cleaned = expr.strip()
    if not cleaned:
        raise ValueError("damage_expr must be non-empty")

    working = _strip_trailing_alpha(cleaned)
    # Split on signed boundaries so ``1d10+1d4`` stays two dice terms, not flat +1.
    raw_terms = [part.strip() for part in _TERM_SPLIT_RE.split(working) if part.strip()]
    if not raw_terms:
        raise ValueError(f"unparseable damage_expr: {expr!r}")
    return raw_terms


def _term_minmax(term: str, expr: str) -> tuple[int, int]:
    """Return (min, max) contribution for one signed term."""
    dice = _DICE_TERM_RE.fullmatch(term.lstrip("+"))
    if dice is not None:
        count = int(dice.group(1))
        faces = int(dice.group(2))
        if count < 1 or faces < 1:
            raise ValueError(f"invalid dice term in damage_expr: {expr!r}")
        return count, count * faces
    if not _FLAT_TERM_RE.fullmatch(term):
        raise ValueError(f"unparseable damage_expr: {expr!r}")
    flat = int(term)
    return flat, flat


def _term_roll(term: str, expr: str, roll_int: _RollInt) -> int:
    """Return rolled contribution for one signed term."""
    dice = _DICE_TERM_RE.fullmatch(term.lstrip("+"))
    if dice is not None:
        count = int(dice.group(1))
        faces = int(dice.group(2))
        if count < 1 or faces < 1:
            raise ValueError(f"invalid dice term in damage_expr: {expr!r}")
        total = 0
        for _ in range(count):
            total += roll_int(1, faces)
        return total
    if not _FLAT_TERM_RE.fullmatch(term):
        raise ValueError(f"unparseable damage_expr: {expr!r}")
    return int(term)


def damage_expr_to_min_max(expr: str) -> tuple[int, int]:
    """Convert a dice expression to inclusive (min_damage, max_damage).

    Args:
        expr: Dice expression such as ``1d8+1`` or ``1d10+1d4``.

    Returns:
        Inclusive minimum and maximum damage before combat modifiers.

    Raises:
        ValueError: If ``expr`` is empty or yields no parseable terms.
    """
    raw_terms = _parse_terms(expr)
    min_total = 0
    max_total = 0
    for term in raw_terms:
        lo, hi = _term_minmax(term, expr)
        min_total += lo
        max_total += hi

    min_total = max(min_total, 0)
    return min_total, max(max_total, min_total)


def _secrets_roll(lo: int, hi: int) -> int:
    """Inclusive lo..hi using secrets (avoids Bandit/Codacy B311 on random)."""
    return lo + secrets.randbelow(hi - lo + 1)


def roll_damage_expr(expr: str, *, rng: random.Random | None = None) -> int:
    """Roll a dice expression once and return a non-negative integer.

    Args:
        expr: Dice expression such as ``1d8+1`` or ``1d10+1d4``.
        rng: Optional ``random.Random`` for deterministic tests.

    Returns:
        Rolled damage, floored at 0.

    Raises:
        ValueError: If ``expr`` is empty or yields no parseable terms.
    """
    roll_int: _RollInt = rng.randint if rng is not None else _secrets_roll

    total = 0
    for term in _parse_terms(expr):
        total += _term_roll(term, expr, roll_int)
    return max(total, 0)
