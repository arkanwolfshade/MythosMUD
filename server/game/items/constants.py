"""Constants supporting item prototype validation.

These enumerations anchor the schema's guard rails to ensure prototype payloads
remain lore-compliant while keeping the validation surface explicit.
"""

# A stack with this flag never outlives the instance it was made for: dropped copies are destroyed
# when the instance is flushed instead of being sent to the owner's bank box.
INSTANCE_BOUND_FLAG = "INSTANCE_BOUND"

ALLOWED_FLAGS: set[str] = {
    "MAGICAL",
    "CURSED",
    "NO_DROP",
    "NO_SALE",
    "SOULBOUND",
    "GLOW",
    "QUEST_ITEM",
    "CONSUMABLE",
    INSTANCE_BOUND_FLAG,
}

ALLOWED_ITEM_TYPES: set[str] = {
    "consumable",
    "equipment",
    "artifact",
    "container",
    "quest",
    "environment",
    "currency",
    "weapon",
}

ALLOWED_WEAR_SLOTS: set[str] = {
    "head",
    "torso",
    "legs",
    "main_hand",
    "off_hand",
    "feet",
    "hands",
    "accessory",
    "ring",
    "amulet",
    "belt",
    "backpack",
}
