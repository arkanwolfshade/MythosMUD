"""
NPC Startup Service for MythosMUD.

This module provides automatic NPC spawning during server startup to populate
the world with static NPCs based on existing NPC definitions.

As documented in the Cultes des Goules, proper initialization of the dimensional
entities is essential for maintaining the integrity of the world's fabric.
"""

import random
from typing import Any

from ..logging.enhanced_logging_config import get_logger
from ..npc_database import get_npc_session
from ..services.npc_instance_service import get_npc_instance_service
from ..services.npc_service import npc_service

logger = get_logger(__name__)


class NPCStartupService:
    """
    Service for automatic NPC spawning during server startup.

    This service extends the existing NPC subsystem by providing automatic
    population of the world with NPCs when the server starts.
    """

    def __init__(self):
        """Initialize the NPC startup service."""
        logger.info("NPCStartupService initialized")

    async def spawn_npcs_on_startup(self) -> dict[str, Any]:
        """
        Spawn NPCs during server startup.

        This method handles the automatic spawning of NPCs when the server
        starts, including required NPCs and optional NPCs based on configuration.

        Returns:
            Dictionary with startup spawning results
        """
        logger.info("Starting NPC startup spawning process")

        # AI Agent: Explicit type annotation to help mypy understand dict structure
        startup_results: dict[str, Any] = {
            "total_attempted": 0,
            "total_spawned": 0,
            "required_spawned": 0,
            "optional_spawned": 0,
            "failed_spawns": 0,
            "errors": [],
            "spawned_npcs": [],
        }

        try:
            # Get NPC instance service
            npc_instance_service = get_npc_instance_service()

            # Load NPC definitions from database
            async for npc_session in get_npc_session():
                try:
                    # Get all NPC definitions
                    definitions = await npc_service.get_npc_definitions(npc_session)
                    logger.info("Found NPC definitions for startup spawning", count=len(definitions))

                    # Separate required and optional NPCs
                    required_npcs = [d for d in definitions if d.required_npc]
                    optional_npcs = [d for d in definitions if not d.required_npc]

                    logger.info(
                        "NPCs categorized for spawning",
                        required_count=len(required_npcs),
                        optional_count=len(optional_npcs),
                    )

                    # Spawn required NPCs first
                    required_results = await self._spawn_required_npcs(required_npcs, npc_instance_service)
                    startup_results["required_spawned"] = required_results["spawned"]
                    startup_results["total_attempted"] += required_results["attempted"]
                    startup_results["total_spawned"] += required_results["spawned"]
                    startup_results["failed_spawns"] += required_results["failed"]
                    startup_results["errors"].extend(required_results["errors"])
                    startup_results["spawned_npcs"].extend(required_results["spawned_npcs"])

                    # Spawn optional NPCs based on probability
                    optional_results = await self._spawn_optional_npcs(optional_npcs, npc_instance_service)
                    startup_results["optional_spawned"] = optional_results["spawned"]
                    startup_results["total_attempted"] += optional_results["attempted"]
                    startup_results["total_spawned"] += optional_results["spawned"]
                    startup_results["failed_spawns"] += optional_results["failed"]
                    startup_results["errors"].extend(optional_results["errors"])
                    startup_results["spawned_npcs"].extend(optional_results["spawned_npcs"])

                except Exception as e:
                    error_msg = f"Error during startup spawning: {str(e)}"
                    logger.error(error_msg)
                    startup_results["errors"].append(error_msg)
                    startup_results["failed_spawns"] += 1

            logger.info(
                "NPC startup spawning completed",
                total_attempted=startup_results["total_attempted"],
                total_spawned=startup_results["total_spawned"],
                required_spawned=startup_results["required_spawned"],
                optional_spawned=startup_results["optional_spawned"],
                failed_spawns=startup_results["failed_spawns"],
                errors=len(startup_results["errors"]),
            )

            return startup_results

        except Exception as e:
            error_msg = f"Critical error in startup spawning: {str(e)}"
            logger.error(error_msg)
            startup_results["errors"].append(error_msg)
            return startup_results

    async def _spawn_required_npcs(self, required_npcs: list, npc_instance_service) -> dict[str, Any]:
        """
        Spawn all required NPCs.

        Args:
            required_npcs: List of required NPC definitions
            npc_instance_service: NPC instance service for spawning

        Returns:
            Dictionary with spawning results
        """
        # AI Agent: Explicit type annotation to help mypy understand dict structure
        results: dict[str, Any] = {"attempted": 0, "spawned": 0, "failed": 0, "errors": [], "spawned_npcs": []}

        logger.info("Spawning required NPCs", count=len(required_npcs))

        for npc_def in required_npcs:
            results["attempted"] += 1

            try:
                # Determine spawn room
                spawn_room = self._determine_spawn_room(npc_def)
                if not spawn_room:
                    error_msg = f"No valid spawn room found for required NPC {npc_def.name}"
                    logger.error(error_msg)
                    results["errors"].append(error_msg)
                    results["failed"] += 1
                    continue

                # Spawn the NPC
                spawn_result = await npc_instance_service.spawn_npc_instance(
                    definition_id=npc_def.id, room_id=spawn_room, reason="startup_required"
                )

                if spawn_result["success"]:
                    results["spawned"] += 1
                    results["spawned_npcs"].append(
                        {
                            "npc_id": spawn_result["npc_id"],
                            "name": spawn_result["definition_name"],
                            "room_id": spawn_result["room_id"],
                            "definition_id": npc_def.id,
                        }
                    )
                    logger.info("Spawned required NPC", npc_name=npc_def.name, spawn_room=spawn_room)
                else:
                    error_msg = (
                        f"Failed to spawn required NPC {npc_def.name}: {spawn_result.get('message', 'Unknown error')}"
                    )
                    logger.error(error_msg)
                    results["errors"].append(error_msg)
                    results["failed"] += 1

            except Exception as e:
                error_msg = f"Error spawning required NPC {npc_def.name}: {str(e)}"
                logger.error(error_msg)
                results["errors"].append(error_msg)
                results["failed"] += 1

        logger.info("Required NPC spawning completed", spawned=results["spawned"], attempted=results["attempted"])
        return results

    async def _spawn_optional_npcs(self, optional_npcs: list, npc_instance_service) -> dict[str, Any]:
        """
        Spawn optional NPCs based on spawn probability.

        Args:
            optional_npcs: List of optional NPC definitions
            npc_instance_service: NPC instance service for spawning

        Returns:
            Dictionary with spawning results
        """
        # AI Agent: Explicit type annotation to help mypy understand dict structure
        results: dict[str, Any] = {"attempted": 0, "spawned": 0, "failed": 0, "errors": [], "spawned_npcs": []}

        logger.info("Evaluating optional NPCs for spawning", count=len(optional_npcs))

        for npc_def in optional_npcs:
            # Check spawn probability
            spawn_probability = getattr(npc_def, "spawn_probability", 1.0)
            if random.random() > spawn_probability:
                logger.debug("Skipping optional NPC", npc_name=npc_def.name, probability=spawn_probability)
                continue

            results["attempted"] += 1

            try:
                # Determine spawn room
                spawn_room = self._determine_spawn_room(npc_def)
                if not spawn_room:
                    logger.debug("No valid spawn room found for optional NPC", npc_name=npc_def.name)
                    continue

                # Check population limits (this would need to be implemented in the population controller)
                # For now, we'll skip this check and let the spawning service handle it

                # Spawn the NPC
                spawn_result = await npc_instance_service.spawn_npc_instance(
                    definition_id=npc_def.id, room_id=spawn_room, reason="startup_optional"
                )

                if spawn_result["success"]:
                    results["spawned"] += 1
                    results["spawned_npcs"].append(
                        {
                            "npc_id": spawn_result["npc_id"],
                            "name": spawn_result["definition_name"],
                            "room_id": spawn_result["room_id"],
                            "definition_id": npc_def.id,
                        }
                    )
                    logger.info("Spawned optional NPC", npc_name=npc_def.name, spawn_room=spawn_room)
                else:
                    logger.warning(
                        f"Failed to spawn optional NPC {npc_def.name}: {spawn_result.get('message', 'Unknown error')}"
                    )
                    results["failed"] += 1

            except Exception as e:
                error_msg = f"Error spawning optional NPC {npc_def.name}: {str(e)}"
                logger.warning(error_msg)  # Use warning for optional NPCs
                results["errors"].append(error_msg)
                results["failed"] += 1

        logger.info("Optional NPC spawning completed", spawned=results["spawned"], attempted=results["attempted"])
        return results

    def _determine_spawn_room(self, npc_def) -> str | None:
        """
        Determine the appropriate room for spawning an NPC.

        Args:
            npc_def: NPC definition

        Returns:
            Room ID where the NPC should spawn, or None if no valid room found
        """
        try:
            from ..persistence import get_persistence

            persistence = get_persistence()
            if not persistence:
                logger.error("Persistence layer not available for room validation")
                return None

            # If NPC has a specific room_id, verify it exists
            if hasattr(npc_def, "room_id") and npc_def.room_id:
                room_id = npc_def.room_id
                room = persistence.get_room(room_id)
                if room:
                    logger.debug("Using specific room for NPC", npc_name=npc_def.name, room_id=room_id)
                    return room_id
                else:
                    logger.warning(
                        "NPC room_id not found in database",
                        npc_name=npc_def.name,
                        room_id=room_id,
                        definition_id=npc_def.id,
                    )
                    # Try fallback to sub-zone default

            # If NPC has a sub_zone_id, try to find a valid room in that sub-zone
            if hasattr(npc_def, "sub_zone_id") and npc_def.sub_zone_id:
                default_room = self._get_default_room_for_sub_zone(npc_def.sub_zone_id)
                if default_room:
                    room = persistence.get_room(default_room)
                    if room:
                        logger.debug(
                            "Using default room for NPC in sub-zone",
                            npc_name=npc_def.name,
                            sub_zone_id=npc_def.sub_zone_id,
                            room_id=default_room,
                        )
                        return default_room
                    else:
                        logger.warning(
                            "Default room for sub-zone not found in database",
                            npc_name=npc_def.name,
                            sub_zone_id=npc_def.sub_zone_id,
                            room_id=default_room,
                        )

            # Fallback to a default starting room
            fallback_room_id = "earth_arkhamcity_northside_intersection_derby_high"
            room = persistence.get_room(fallback_room_id)
            if room:
                logger.debug("Using fallback room for NPC", npc_name=npc_def.name, room_id=fallback_room_id)
                return fallback_room_id
            else:
                logger.error(
                    "Fallback room not found in database",
                    npc_name=npc_def.name,
                    room_id=fallback_room_id,
                )
                return None

        except Exception as e:
            logger.error("Error determining spawn room for NPC", npc_name=npc_def.name, error=str(e))
            return None

    def _get_default_room_for_sub_zone(self, sub_zone_id: str) -> str | None:
        """
        Get a default room for a given sub-zone.

        Args:
            sub_zone_id: Sub-zone identifier

        Returns:
            Default room ID for the sub-zone, or None if not found
        """
        # This is a simplified implementation
        # In a full implementation, this would query the room database or use configuration

        default_rooms = {
            "sanitarium": "earth_arkhamcity_sanitarium_room_foyer_001",
            "downtown": "earth_arkhamcity_downtown_intersection_derby_garrison",
            "northside": "earth_arkhamcity_northside_intersection_derby_high",
            "southside": "earth_arkhamcity_southside_intersection_derby_garrison",
            # Add more sub-zone mappings as needed
        }

        return default_rooms.get(sub_zone_id.lower())


# Global startup service instance
npc_startup_service = NPCStartupService()


def get_npc_startup_service() -> NPCStartupService:
    """Get the global NPC startup service."""
    return npc_startup_service
