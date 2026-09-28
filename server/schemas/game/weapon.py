"""
Weapon stats schema for MythosMUD.

Re-exports WeaponStats from models for API consumers. Defined in models.game
to avoid circular imports (models -> schemas -> models).
"""

from collections.abc import Mapping

from ...models.game import WeaponStats

__all__ = ["WeaponStats", "weapon_stats_from_metadata"]

# Hoisted rather than read per call: the field set is fixed at class creation, and pylint
# does not recognise pydantic's class-level model_fields as a mapping (unsupported-membership-test).
_WEAPON_STATS_KEYS: frozenset[str] = frozenset(WeaponStats.model_fields.keys())


def weapon_stats_from_metadata(weapon: Mapping[str, object]) -> WeaponStats:
    """
    Project an ADR-026 ``metadata.weapon`` dict onto the narrow WeaponStats contract.

    ``metadata.weapon`` is validated by WeaponMetadata (server.game.items.metadata_models),
    which carries the rich CoC fields -- ``damage_expr``, ``attacks``, ``range``, ``ammo``,
    ``skill``, ``skill_bonus`` -- alongside the legacy integers. WeaponStats is the narrower
    wire contract the client mirrors, and it sets ``extra="forbid"``, so feeding it a whole
    prototype metadata dict raises ValidationError on every single weapon in the catalog.
    Dropping the keys WeaponStats does not model is what the callers always meant; doing it
    here keeps that projection in one place instead of at each boundary.

    Args:
        weapon: Raw ``metadata.weapon`` mapping from an item prototype.

    Returns:
        WeaponStats: The modelled subset of the mapping.

    Raises:
        ValidationError: If the modelled subset itself is invalid (e.g. missing min/max damage).
    """
    known = {key: value for key, value in weapon.items() if key in _WEAPON_STATS_KEYS}
    return WeaponStats.model_validate(known)
