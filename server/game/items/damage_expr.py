"""Lossy damage_expr → (min_damage, max_damage) bridge for catalog generators.

Combat still consumes WeaponStats integers until Phase 3 (ADR-026). This helper
exists so private SQL generators can dual-write min/max without changing
``server/game/weapons.py``.

Lossy rules:
- Sum of terms ``NdM`` / ``NdM+K`` / ``NdM-K`` / bare integers (case-insensitive).
- Unknown alphabetic suffixes (e.g. ``+DB``) are ignored after a trailing ``+``/``-``.
- Min = sum(dice counts) + flat modifiers; max = sum(count * faces) + flats.
- Empty or unparseable expressions raise ``ValueError``.
"""

from __future__ import annotations

import re

_DICE_TERM_RE = re.compile(r"^(\d+)\s*[dD]\s*(\d+)$")
_FLAT_TERM_RE = re.compile(r"^[+-]?\d+$")
_TRAILING_ALPHA = re.compile(r"[+-]\s*[A-Za-z_][A-Za-z0-9_]*\s*$")
_TERM_SPLIT_RE = re.compile(r"(?=[+-])")


def damage_expr_to_min_max(expr: str) -> tuple[int, int]:
    """Convert a dice expression to inclusive (min_damage, max_damage).

    Args:
        expr: Dice expression such as ``1d8+1`` or ``1d10+1d4``.

    Returns:
        Inclusive minimum and maximum damage before combat modifiers.

    Raises:
        ValueError: If ``expr`` is empty or yields no parseable terms.
    """
    cleaned = expr.strip()
    if not cleaned:
        raise ValueError("damage_expr must be non-empty")

    working = cleaned
    while True:
        next_pass = _TRAILING_ALPHA.sub("", working).strip()
        if next_pass == working:
            break
        working = next_pass

    # Split on signed boundaries so ``1d10+1d4`` stays two dice terms, not flat +1.
    raw_terms = [part.strip() for part in _TERM_SPLIT_RE.split(working) if part.strip()]
    if not raw_terms:
        raise ValueError(f"unparseable damage_expr: {expr!r}")

    min_total = 0
    max_total = 0
    for term in raw_terms:
        dice = _DICE_TERM_RE.fullmatch(term.lstrip("+"))
        if dice is not None:
            count = int(dice.group(1))
            faces = int(dice.group(2))
            if count < 1 or faces < 1:
                raise ValueError(f"invalid dice term in damage_expr: {expr!r}")
            min_total += count
            max_total += count * faces
            continue

        if not _FLAT_TERM_RE.fullmatch(term):
            raise ValueError(f"unparseable damage_expr: {expr!r}")
        flat = int(term)
        min_total += flat
        max_total += flat

    min_total = max(min_total, 0)
    max_total = max(max_total, min_total)
    return min_total, max_total
