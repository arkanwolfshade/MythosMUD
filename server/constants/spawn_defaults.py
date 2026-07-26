"""
Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.

Single source of truth so seeded players and respawn logic stay aligned.
"""

# Sanitarium Main Foyer — Dr. Morgan's room; tutorial exit and default death/lucidity respawn.
DEFAULT_RESPAWN_ROOM: str = "earth_arkhamcity_sanitarium_room_foyer_001"

# Tutorial instance exit destination (same as default respawn unless overridden per-template).
DEFAULT_EXIT_ROOM_ID: str = DEFAULT_RESPAWN_ROOM
