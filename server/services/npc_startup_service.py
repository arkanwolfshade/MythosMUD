"""
NPC Startup Service for MythosMUD.

This module provides automatic NPC spawning during server startup to populate
the world with static NPCs based on existing NPC definitions.

As documented in the Cultes des Goules, proper initialization of the dimensional
entities is essential for maintaining the integrity of the world's fabric.


ASYNC MIGRATION (Phase 2):
All persistence calls wrapped in asyncio.to_thread() to prevent event loop blocking.
"""

# pylint: disable=too-few-public-methods  # Reason: Startup service class with focused responsibility, minimal public interface

import asyncio
import random
from typing import TYPE_CHECKING, Any, cast

from ..npc_database import get_npc_session
from ..services.npc_instance_service import get_npc_instance_service
from ..services.npc_service import npc_service
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..models.npc import NPCDefinition
    from ..services.npc_instance_service import NPCInstanceService

logger = get_logger(__name__)

# Arena (limbo/arena, subzone arena): 11x11 grid; stable_ids limbo_arena_arena_arena_0_0 .. 10_10
ARENA_ROOM_IDS: tuple[str, ...] = tuple(f"limbo_arena_arena_arena_{r}_{c}" for r in range(11) for c in range(11))


class NPCStartupService:  # pylint: disable=too-few-public-methods  # Reason: Startup service class with focused responsibility, minimal public interface
    """
    Service for automatic NPC spawning during server startup.

    This service coordinates initial NPC population when the server starts,
    using NPCInstanceService to spawn required and optional NPCs.

    SERVICE HIERARCHY:
    - Level 4 (highest): Coordinates startup spawning
    - Uses: NPCInstanceService → NPCPopulationController → NPCLifecycleManager

    ARCHITECTURE NOTE:
    All spawning goes through NPCInstanceService.spawn_npc_instance() to ensure
    proper population validation and lifecycle tracking.
    """

    def __init__(self) -> None:
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
            "arena_spawned": 0,
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

                    # Second pass: spawn one instance per definition that was spawned into a random arena room
                    arena_results = await self._spawn_arena_npcs(
                        definitions=definitions,
                        required_results=required_results,
                        optional_results=optional_results,
                        npc_instance_service=npc_instance_service,
                    )
                    startup_results["arena_spawned"] = arena_results["spawned"]
                    startup_results["total_attempted"] += arena_results["attempted"]
                    startup_results["total_spawned"] += arena_results["spawned"]
                    startup_results["failed_spawns"] += arena_results["failed"]
                    startup_results["errors"].extend(arena_results["errors"])
                    startup_results["spawned_npcs"].extend(arena_results["spawned_npcs"])

                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawning errors unpredictable, must log and continue
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
                arena_spawned=startup_results["arena_spawned"],
                failed_spawns=startup_results["failed_spawns"],
                errors=len(startup_results["errors"]),
            )

            return startup_results

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Startup spawning errors unpredictable, must return results
            error_msg = f"Critical error in startup spawning: {str(e)}"
            logger.error(error_msg)
            startup_results["errors"].append(error_msg)
            return startup_results

    async def _spawn_required_npcs(
        self, required_npcs: list["NPCDefinition"], npc_instance_service: "NPCInstanceService"
    ) -> dict[str, Any]:
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

        empty_cache_error_added = False
        for npc_def in required_npcs:
            results["attempted"] += 1

            try:
                # Determine spawn room
                spawn_room = await self._determine_spawn_room(npc_def)
                if not spawn_room:
                    # When room cache is empty (e.g. no world data loaded), log once and at debug per NPC
                    from ..container import ApplicationContainer

                    container = ApplicationContainer.get_instance()
                    async_persistence = getattr(container, "async_persistence", None) if container else None
                    cache_size = len(async_persistence._room_cache) if async_persistence else -1  # pylint: disable=protected-access  # Reason: Check if empty cache to avoid per-NPC error spam
                    if not cache_size:
                        if not empty_cache_error_added:
                            results["errors"].append(
                                "Room cache empty; required NPC spawns skipped (world data not loaded)"
                            )
                            empty_cache_error_added = True
                        logger.debug(
                            "No valid spawn room for required NPC (cache empty)",
                            npc_name=npc_def.name,
                        )
                    else:
                        error_msg = f"No valid spawn room found for required NPC {npc_def.name}"
                        logger.warning(error_msg)
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

            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Required NPC spawning errors unpredictable, must log but continue
                error_msg = f"Error spawning required NPC {npc_def.name}: {str(e)}"
                logger.error(error_msg)
                results["errors"].append(error_msg)
                results["failed"] += 1

        logger.info("Required NPC spawning completed", spawned=results["spawned"], attempted=results["attempted"])
        return results

    async def _spawn_optional_npcs(
        self, optional_npcs: list["NPCDefinition"], npc_instance_service: "NPCInstanceService"
    ) -> dict[str, Any]:
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
            if random.random() > spawn_probability:  # nosec B311 - Game mechanics, not security-critical
                logger.debug("Skipping optional NPC", npc_name=npc_def.name, probability=spawn_probability)
                continue

            results["attempted"] += 1

            try:
                # Determine spawn room
                spawn_room = await self._determine_spawn_room(npc_def)
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
                        "Failed to spawn optional NPC",
                        npc_name=npc_def.name,
                        error_message=spawn_result.get("message", "Unknown error"),
                    )
                    results["failed"] += 1

            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Optional NPC spawning errors unpredictable, must log but continue
                error_msg = f"Error spawning optional NPC {npc_def.name}: {str(e)}"
                logger.warning(error_msg)  # Use warning for optional NPCs
                results["errors"].append(error_msg)
                results["failed"] += 1

        logger.info("Optional NPC spawning completed", spawned=results["spawned"], attempted=results["attempted"])
        return results

    async def _spawn_arena_npcs(
        self,
        definitions: list["NPCDefinition"],
        required_results: dict[str, Any],
        optional_results: dict[str, Any],
        npc_instance_service: "NPCInstanceService",
    ) -> dict[str, Any]:
        """
        Second pass: spawn one instance per definition (that was spawned in required/optional) in a random arena room.

        Room cache is warmed before this pass so arena rooms are available. Population caps may
        prevent a second instance for some definitions; failures are logged and counted.
        """
        results: dict[str, Any] = {"attempted": 0, "spawned": 0, "failed": 0, "errors": [], "spawned_npcs": []}

        spawned_definition_ids = {
            s["definition_id"]
            for s in required_results.get("spawned_npcs", []) + optional_results.get("spawned_npcs", [])
        }
        if not spawned_definition_ids:
            logger.info("No definitions were spawned in required/optional pass; skipping arena pass")
            return results

        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            async_persistence = getattr(container, "async_persistence", None) if container else None
            if async_persistence:
                await async_persistence.warmup_room_cache()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Warmup errors must not abort arena pass
            logger.warning("Room cache warmup before arena pass failed", error=str(e))
            results["errors"].append(f"Room cache warmup before arena pass failed: {e}")

        definitions_by_id = {int(d.id): d for d in definitions}
        for definition_id in spawned_definition_ids:
            npc_def = definitions_by_id.get(definition_id)
            if not npc_def:
                continue
            results["attempted"] += 1
            arena_room = random.choice(ARENA_ROOM_IDS)  # nosec B311 - Game mechanics, not security-critical
            try:
                spawn_result = await npc_instance_service.spawn_npc_instance(
                    definition_id=int(npc_def.id), room_id=arena_room, reason="startup_arena"
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
                    logger.info(
                        "Spawned NPC in arena",
                        npc_name=npc_def.name,
                        arena_room=arena_room,
                    )
                else:
                    results["failed"] += 1
                    msg = spawn_result.get("message", "Unknown error")
                    results["errors"].append(f"Arena spawn failed for {npc_def.name}: {msg}")
                    logger.debug(
                        "Arena spawn skipped or failed (e.g. population cap)",
                        npc_name=npc_def.name,
                        message=msg,
                    )
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Per-definition errors must not abort arena pass
                results["failed"] += 1
                error_msg = f"Error spawning NPC {npc_def.name} in arena: {str(e)}"
                logger.warning(error_msg)
                results["errors"].append(error_msg)

        logger.info(
            "Arena NPC spawning completed",
            spawned=results["spawned"],
            attempted=results["attempted"],
        )
        return results

    async def _determine_spawn_room(self, npc_def: "NPCDefinition") -> str | None:
        """
        Determine the appropriate room for spawning an NPC.

        Args:
            npc_def: NPC definition

        Returns:
            Room ID where the NPC should spawn, or None if no valid room found
        """
        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            async_persistence = getattr(container, "async_persistence", None) if container else None

            if not async_persistence:
                logger.error("Persistence layer not available for room validation")
                return None

            # Ensure room cache is loaded before accessing rooms (lazy loading after commit a9fd435)
            # Room cache may not be loaded if warmup_room_cache failed or hasn't completed yet
            # warmup_room_cache is idempotent - safe to call multiple times
            await async_persistence.warmup_room_cache()

            # Verify cache was loaded - if empty, log warning but continue (may be intentional in some environments)
            cache_size = len(async_persistence._room_cache)  # pylint: disable=protected-access  # Reason: Need to verify cache was loaded for room validation
            if not cache_size:
                logger.warning(
                    "Room cache is empty - room validation will fail",
                    npc_name=npc_def.name,
                    cache_size=cache_size,
                )

            persistence = async_persistence

            # If NPC has a specific room_id, verify it exists
            if hasattr(npc_def, "room_id") and npc_def.room_id:
                room_id = npc_def.room_id
                # Use sync cache method (get_room_by_id uses cache)
                room = persistence.get_room_by_id(room_id)
                if room:
                    logger.debug("Using specific room for NPC", npc_name=npc_def.name, room_id=room_id)
                    return cast(str | None, room_id)
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
                    room = await asyncio.to_thread(persistence.get_room_by_id, default_room)
                    if room:
                        logger.debug(
                            "Using default room for NPC in sub-zone",
                            npc_name=npc_def.name,
                            sub_zone_id=npc_def.sub_zone_id,
                            room_id=default_room,
                        )
                        return default_room
                    logger.warning(
                        "Default room for sub-zone not found in database",
                        npc_name=npc_def.name,
                        sub_zone_id=npc_def.sub_zone_id,
                        room_id=default_room,
                    )

            # Fallback to a default starting room
            fallback_room_id = "earth_arkhamcity_northside_intersection_derby_high"
            room = await asyncio.to_thread(persistence.get_room_by_id, fallback_room_id)
            if room:
                logger.debug("Using fallback room for NPC", npc_name=npc_def.name, room_id=fallback_room_id)
                return fallback_room_id
            # Empty cache: expected when DB has no world data (e.g. local dev) -> debug only
            cache_size = len(async_persistence._room_cache)  # pylint: disable=protected-access  # Reason: Distinguish empty-DB vs missing fallback room
            if not cache_size:
                logger.debug(
                    "Fallback room not found (room cache empty; world data may not be loaded)",
                    npc_name=npc_def.name,
                    room_id=fallback_room_id,
                )
            else:
                logger.warning(
                    "Fallback room not found in database",
                    npc_name=npc_def.name,
                    room_id=fallback_room_id,
                )
            return None

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room determination errors unpredictable, must return None
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
