"""
NPC Configuration for MythosMUD.

This module defines configuration settings for NPC lifecycle management,
spawning, respawning, and population control.

As documented in the Necronomicon, the timing of manifestations is critical
to maintaining the delicate balance between our world and the outer darkness.
These configuration parameters control when and how NPCs materialize in
the game world.

AI Agent: Configuration module for NPC lifecycle and spawning behavior.
         Provides centralized settings for maintenance intervals, respawn delays,
         and spawn checking frequencies.
"""

from typing import Any


class NPCMaintenanceConfig:
    """
    Configuration for NPC lifecycle maintenance.

    This class centralizes all timing and frequency parameters for NPC
    lifecycle operations, respawning, and periodic spawn checks.
    """

    # How often to run NPC maintenance (in game ticks)
    # 60 ticks = 1 minute (assuming 1 second per tick)
    MAINTENANCE_INTERVAL_TICKS: int = 60

    # How often to re-roll optional NPC spawns (in seconds)
    # This controls how frequently we check if optional NPCs should spawn
    SPAWN_REROLL_INTERVAL: float = 600.0  # Every 10 minutes

    # Respawn delay overrides per NPC type (in seconds)
    # These values override the default respawn delay for specific NPC types
    RESPAWN_DELAYS: dict[str, float] = {
        "quest_giver": 600.0,  # 10 minutes - important NPCs respawn quickly
        "shopkeeper": 300.0,  # 5 minutes (default) - essential services
        "passive_mob": 180.0,  # 3 minutes - common creatures respawn faster
        "aggressive_mob": 300.0,  # 5 minutes - balanced respawn rate
    }

    # Minimum interval between spawn checks per NPC definition (in seconds)
    # This prevents spam spawning of the same NPC type
    MIN_SPAWN_CHECK_INTERVAL: float = 300.0  # 5 minutes between checks

    # Default values (also defined in lifecycle_manager.py, documented here for reference)
    # These are the baseline values used by the lifecycle manager
    DEFAULT_RESPAWN_DELAY: float = 300.0  # 5 minutes
    DEATH_SUPPRESSION_DURATION: float = 30.0  # 30 seconds after death
    MAX_RESPAWN_ATTEMPTS: int = 3  # Maximum attempts before giving up
    CLEANUP_INTERVAL: float = 3600.0  # 1 hour - cleanup old lifecycle records

    @classmethod
    def get_respawn_delay(cls, npc_type: str) -> float:
        """
        Get the respawn delay for a specific NPC type.

        Args:
            npc_type: Type of NPC (quest_giver, shopkeeper, passive_mob, etc.)

        Returns:
            Respawn delay in seconds for this NPC type
        """
        return cls.RESPAWN_DELAYS.get(npc_type, cls.DEFAULT_RESPAWN_DELAY)

    @classmethod
    def should_run_maintenance(cls, tick_count: int) -> bool:
        """
        Check if NPC maintenance should run on this tick.

        Args:
            tick_count: Current game tick number

        Returns:
            True if maintenance should run on this tick
        """
        return tick_count % cls.MAINTENANCE_INTERVAL_TICKS == 0

    @classmethod
    def get_config_summary(cls) -> dict[str, Any]:
        """
        Get a summary of all NPC configuration values.

        Returns:
            Dictionary containing all configuration parameters
        """
        return {
            "maintenance_interval_ticks": cls.MAINTENANCE_INTERVAL_TICKS,
            "spawn_reroll_interval": cls.SPAWN_REROLL_INTERVAL,
            "respawn_delays": cls.RESPAWN_DELAYS.copy(),
            "min_spawn_check_interval": cls.MIN_SPAWN_CHECK_INTERVAL,
            "default_respawn_delay": cls.DEFAULT_RESPAWN_DELAY,
            "death_suppression_duration": cls.DEATH_SUPPRESSION_DURATION,
            "max_respawn_attempts": cls.MAX_RESPAWN_ATTEMPTS,
            "cleanup_interval": cls.CLEANUP_INTERVAL,
        }
