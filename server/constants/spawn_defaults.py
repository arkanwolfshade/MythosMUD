"""
Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.

Single source of truth so seeded players and respawn logic stay aligned.
"""

# Sanitarium Main Foyer — Dr. Morgan's room; tutorial exit and default death/lucidity respawn.
DEFAULT_RESPAWN_ROOM: str = "earth_arkhamcity_sanitarium_room_foyer_001"

# Second-floor Recovery Ward of the Sanitarium (ADR-028): where players wake after delirium or a sanitarium failover.
# Death still respawns at DEFAULT_RESPAWN_ROOM. The ward is reached by stairs from the Main Foyer, where Dr. Morgan
# runs the debrief.
RECOVERY_WARD_ROOM_ID: str = "earth_arkhamcity_sanitarium_room_recovery_ward_001"

# Tutorial instance exit destination (same as default respawn unless overridden per-template).
DEFAULT_EXIT_ROOM_ID: str = DEFAULT_RESPAWN_ROOM

# Death-state isolation room. ID shape: {plane}_{zone}_{sub_zone}_{stable_id}
LIMBO_ROOM_ID: str = "limbo_death_void_limbo_death_void"
