"""Constants supporting item prototype validation.

These enumerations anchor the schema's guard rails to ensure prototype payloads
remain lore-compliant while keeping the validation surface explicit.
"""

ALLOWED_FLAGS: set[str] = {
    "MAGICAL",
    "CURSED",
    "NO_DROP",
    "NO_SALE",
    "SOULBOUND",
    "GLOW",
    "QUEST_ITEM",
    "CONSUMABLE",
}

ALLOWED_ITEM_TYPES: set[str] = {
    "consumable",
    "equipment",
    "artifact",
    "container",
    "quest",
    "environment",
    "currency",
}

ALLOWED_WEAR_SLOTS: set[str] = {
    "HEAD",
    "TORSO",
    "LEGS",
    "MAIN_HAND",
    "OFF_HAND",
    "FEET",
    "HANDS",
    "ACCESSORY",
    "RING",
    "AMULET",
    "BELT",
}
