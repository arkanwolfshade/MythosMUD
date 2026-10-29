"""
Shared inventory conventions.

Kept import-free so services, game code and the container wiring can all use it without import cycles.
"""

# slot_type of a stack the player carries in general inventory (pockets) until they equip it: equip then infers the
# slot from the item's prototype. Floor pickups, container transfers and granted items all arrive this way.
CARRIED_SLOT_TYPE: str = "inventory"
