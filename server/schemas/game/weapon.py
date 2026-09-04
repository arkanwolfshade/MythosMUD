"""
Weapon stats schema for MythosMUD.

Re-exports WeaponStats from models for API consumers. Defined in models.game
to avoid circular imports (models -> schemas -> models).
"""

from ...models.game import WeaponStats

__all__ = ["WeaponStats"]
