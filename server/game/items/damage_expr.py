"""Lossy damage_expr → (min_damage, max_damage) bridge for catalog generators.

Combat still consumes WeaponStats integers until Phase 3 (ADR-026). This module
re-exports the shared helper from ``server.game.dice_expr`` so existing item
imports keep working.
"""

from __future__ import annotations

from server.game.dice_expr import damage_expr_to_min_max

__all__ = ["damage_expr_to_min_max"]
