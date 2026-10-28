"""Shared weapon prototype metadata fixtures.

The real shape of ``metadata.weapon`` as stored in the item catalog, for tests that need
to prove the WeaponStats projection copes with the full ADR-026 payload rather than a
hand-trimmed subset. Shared so the two call sites' tests assert against one shape.
"""

# Verbatim from data/item_catalog/catalog/pack_dark_ages_uniques.json, plus the legacy
# min_damage/max_damage/modifier integers that server.game.items.catalog_dml dual-writes
# from damage_expr ("1d4") when loading the catalog into the database.
SLING_PROTOTYPE_WEAPON: dict[str, object] = {
    "range": "60 yards",
    "skill": "fighting_sling",
    "attacks": 1,
    "magical": False,
    "modifier": 0,
    "max_damage": 4,
    "min_damage": 1,
    "damage_expr": "1d4",
    "damage_types": ["bludgeoning"],
}
