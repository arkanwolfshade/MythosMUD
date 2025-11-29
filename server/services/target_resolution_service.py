"""
Target resolution service for MythosMUD.

This service provides unified target resolution for both players and NPCs,
supporting partial name matching, disambiguation, and room-based filtering.
"""

import asyncio
import re
import uuid
from typing import Any, Protocol

from ..logging.enhanced_logging_config import get_logger
from ..npc.behaviors import NPCBase
from ..schemas.target_resolution import TargetMatch, TargetResolutionResult, TargetType

logger = get_logger(__name__)


class PersistenceProtocol(Protocol):
    """Protocol for persistence layer dependency injection."""

    def get_player(self, player_id: uuid.UUID) -> Any: ...
    def get_room(self, room_id: str) -> Any: ...
    def get_players_in_room(self, room_id: str) -> list[Any]: ...


class PlayerServiceProtocol(Protocol):
    """Protocol for player service dependency injection."""

    async def resolve_player_name(self, name: str) -> Any: ...


class TargetResolutionService:
    """
    Service for resolving target names to specific entities.

    This service handles target resolution for both players and NPCs,
    providing partial name matching, disambiguation, and room-based filtering.
    """

    def __init__(self, persistence: PersistenceProtocol, player_service: PlayerServiceProtocol) -> None:
        """
        Initialize the target resolution service.

        Args:
            persistence: Persistence layer instance
            player_service: Player service instance
        """
        self.persistence = persistence
        self.player_service = player_service

    async def resolve_target(self, player_id: uuid.UUID | str, target_name: str) -> TargetResolutionResult:
        """
        Resolve a target name to specific entities.

        Args:
            player_id: ID of the player performing the action (UUID or string for backward compatibility)
            target_name: Name or partial name of the target

        Returns:
            TargetResolutionResult: Result containing matches and metadata
        """
        # Convert to UUID if string (get_player accepts UUID)
        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        # Structlog handles UUID objects automatically, no need to convert to string
        logger.debug("Resolving target", player_id=player_id_uuid, target_name=target_name)

        # Get player's current room - handle both sync and async persistence layers
        import inspect

        # Check if persistence layer has async method (AsyncPersistenceLayer uses get_player_by_id)
        if hasattr(self.persistence, "get_player_by_id"):
            method = self.persistence.get_player_by_id
            if inspect.iscoroutinefunction(method):
                logger.debug("Using async get_player_by_id", player_id=player_id_uuid)
                player = await method(player_id_uuid)
            else:
                logger.debug("Using sync get_player_by_id", player_id=player_id_uuid)
                player = method(player_id_uuid)
        elif hasattr(self.persistence, "get_player"):
            method = self.persistence.get_player
            if inspect.iscoroutinefunction(method):
                logger.debug("Using async get_player", player_id=player_id_uuid)
                player = await method(player_id_uuid)
            else:
                logger.debug("Using sync get_player", player_id=player_id_uuid)
                player = method(player_id_uuid)
        else:
            logger.error(
                "Persistence layer has neither get_player nor get_player_by_id",
                persistence_type=type(self.persistence).__name__,
            )
            return TargetResolutionResult(
                success=False,
                error_message="Internal error: persistence layer not configured correctly",
                search_term=target_name,
                room_id="",
            )

        if not player:
            # Structlog handles UUID objects automatically, no need to convert to string
            logger.warning("Player not found for target resolution", player_id=player_id_uuid)
            return TargetResolutionResult(
                success=False, error_message="Player not found", search_term=target_name, room_id=""
            )

        room_id = player.current_room_id
        # Convert to string if it's not already (handles Mock objects in tests and UUID objects)
        if room_id is not None:
            room_id = str(room_id)
        if not room_id:
            # Structlog handles UUID objects automatically, no need to convert to string
            logger.warning("Player not in a room", player_id=player_id_uuid)
            return TargetResolutionResult(
                success=False, error_message="You are not in a room", search_term=target_name, room_id=""
            )

        # Clean the target name
        clean_target = target_name.strip().lower()
        if not clean_target:
            return TargetResolutionResult(
                success=False, error_message="No target specified", search_term=target_name, room_id=room_id
            )

        # Check for disambiguation suffix (e.g., "rat-1", "dr-2")
        disambiguation_suffix = None
        if re.match(r".*-\d+$", clean_target):
            # Extract the base name and suffix
            base_name = re.sub(r"-\d+$", "", clean_target)
            suffix_match = re.search(r"-(\d+)$", clean_target)
            if suffix_match:
                disambiguation_suffix = f"-{suffix_match.group(1)}"
                clean_target = base_name

        # Search for targets in the room
        matches = []

        # Search for players in the room
        logger.debug("About to search players in room", room_id=room_id, target_name=clean_target)
        player_matches = await self._search_players_in_room(room_id, clean_target, disambiguation_suffix)
        logger.debug("Player search completed", room_id=room_id, matches_count=len(player_matches))
        matches.extend(player_matches)

        # Search for NPCs in the room
        logger.debug("About to search NPCs in room", room_id=room_id, target_name=clean_target)
        npc_matches = await self._search_npcs_in_room(room_id, clean_target, disambiguation_suffix)
        logger.debug("NPC search completed", room_id=room_id, matches_count=len(npc_matches))
        matches.extend(npc_matches)

        # Structlog handles UUID objects automatically, no need to convert to string
        logger.debug(
            "Target resolution completed",
            player_id=player_id_uuid,
            target_name=target_name,
            room_id=room_id,
            player_matches=len(player_matches),
            npc_matches=len(npc_matches),
            total_matches=len(matches),
        )

        # Handle results
        if not matches:
            return TargetResolutionResult(
                success=False,
                error_message=f"No targets found matching '{target_name}'",
                search_term=target_name,
                room_id=room_id,
            )

        if len(matches) == 1:
            return TargetResolutionResult(success=True, matches=matches, search_term=target_name, room_id=room_id)

        # Multiple matches - check if we have a disambiguation suffix
        if disambiguation_suffix:
            # Find the specific match with this suffix
            for match in matches:
                if match.disambiguation_suffix == disambiguation_suffix:
                    return TargetResolutionResult(
                        success=True, matches=[match], search_term=target_name, room_id=room_id
                    )
            # Disambiguation suffix didn't match any target
            return TargetResolutionResult(
                success=False,
                error_message=f"No target found with suffix '{disambiguation_suffix}'",
                search_term=target_name,
                room_id=room_id,
            )

        # Multiple matches without disambiguation - require disambiguation
        return TargetResolutionResult(
            success=False,
            matches=matches,
            disambiguation_required=True,
            error_message=f"Multiple targets match '{target_name}': {', '.join([match.target_name for match in matches])}",
            search_term=target_name,
            room_id=room_id,
        )

    async def _search_players_in_room(
        self, room_id: str, target_name: str, disambiguation_suffix: str | None = None
    ) -> list[TargetMatch]:
        """Search for players in the specified room."""
        try:
            logger.debug("_search_players_in_room: Starting", room_id=room_id, target_name=target_name)
            logger.debug("_search_players_in_room: Getting players in room", room_id=room_id)
            # Check if persistence layer has async method (AsyncPersistenceLayer)
            import inspect

            method = self.persistence.get_players_in_room
            logger.debug(
                "_search_players_in_room: Checking method type",
                room_id=room_id,
                method="get_players_in_room",
                persistence_type=type(self.persistence).__name__,
            )
            is_async = inspect.iscoroutinefunction(method)
            logger.debug(
                "_search_players_in_room: Method check result",
                room_id=room_id,
                is_async=is_async,
                method_type=type(method).__name__,
            )
            if is_async:
                # Use async method directly (no thread pool needed, no lock blocking)
                logger.debug("_search_players_in_room: Using async method", room_id=room_id)
                # Protocol defines method as sync, but runtime check confirms it's async
                players_in_room = await method(room_id)  # type: ignore[misc]
                logger.debug("_search_players_in_room: Async method completed", room_id=room_id)
            else:
                # Use sync method in thread pool to avoid blocking event loop
                # Note: This may still block if the lock is held by another thread
                logger.debug("_search_players_in_room: Using sync method in thread pool", room_id=room_id)
                players_in_room = await asyncio.to_thread(method, room_id)
                logger.debug("_search_players_in_room: Thread pool method completed", room_id=room_id)
            logger.debug("_search_players_in_room: Got players", room_id=room_id, player_count=len(players_in_room))
            matches = []

            for player in players_in_room:
                if target_name in player.name.lower():
                    # Check if this is an exact match with disambiguation suffix
                    if disambiguation_suffix:
                        # For now, we'll use a simple numbering system
                        # In a real implementation, you might want more sophisticated logic
                        continue

                    matches.append(
                        TargetMatch(
                            target_id=str(player.player_id),
                            target_name=player.name,
                            target_type=TargetType.PLAYER,
                            room_id=room_id,
                            metadata={"player_id": str(player.player_id)},
                        )
                    )

            # Add disambiguation suffixes if multiple players have the same name
            if len(matches) > 1:
                name_counts: dict[str, int] = {}
                for match in matches:
                    name_counts[match.target_name] = name_counts.get(match.target_name, 0) + 1

                # Add suffixes for duplicate names
                name_suffixes = {}
                for match in matches:
                    if name_counts[match.target_name] > 1:
                        if match.target_name not in name_suffixes:
                            name_suffixes[match.target_name] = 1
                        else:
                            name_suffixes[match.target_name] += 1
                        match.disambiguation_suffix = f"-{name_suffixes[match.target_name]}"

            logger.debug("_search_players_in_room: Returning matches", room_id=room_id, matches_count=len(matches))
            return matches

        except Exception as e:
            logger.error("Error searching players in room", room_id=room_id, error=str(e))
            return []

    async def _search_npcs_in_room(
        self, room_id: str, target_name: str, disambiguation_suffix: str | None = None
    ) -> list[TargetMatch]:
        """Search for NPCs in the specified room."""
        try:
            # Validate room exists - handle both sync and async persistence layers
            # Note: We don't actually need the room object since we get NPCs from lifecycle manager
            import inspect

            room_exists = False
            # Check if persistence layer has async method (AsyncPersistenceLayer)
            if hasattr(self.persistence, "get_room_by_id"):
                method = self.persistence.get_room_by_id
                if inspect.iscoroutinefunction(method):
                    logger.debug("Using async get_room_by_id", room_id=room_id)
                    room = await method(room_id)
                    room_exists = room is not None
                else:
                    logger.debug("Using sync get_room_by_id", room_id=room_id)
                    room = method(room_id)
                    room_exists = room is not None
            elif hasattr(self.persistence, "get_room"):
                method = self.persistence.get_room
                if inspect.iscoroutinefunction(method):
                    logger.debug("Using async get_room", room_id=room_id)
                    room = await method(room_id)
                    room_exists = room is not None
                else:
                    logger.debug("Using sync get_room", room_id=room_id)
                    room = method(room_id)
                    room_exists = room is not None
            else:
                # If persistence layer doesn't have get_room, skip validation
                # (NPCs come from lifecycle manager anyway)
                logger.debug(
                    "Persistence layer has no get_room method, skipping room validation",
                    persistence_type=type(self.persistence).__name__,
                    room_id=room_id,
                )
                room_exists = True  # Assume room exists if we can't validate

            if not room_exists:
                logger.debug("Room not found", room_id=room_id)
                return []

            matches = []
            # CRITICAL FIX: Query NPCs from lifecycle manager instead of Room instance
            # Room instances are recreated from persistence and lose in-memory NPC tracking
            # NPCs are actually tracked in the lifecycle manager with their current_room_id
            npc_ids: list[str] = []
            try:
                from ..services.npc_instance_service import get_npc_instance_service

                npc_instance_service = get_npc_instance_service()
                if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                    lifecycle_manager = npc_instance_service.lifecycle_manager
                    if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                        active_npcs_dict = lifecycle_manager.active_npcs
                        # Query all active NPCs to find those in this room
                        for npc_id, npc in active_npcs_dict.items():
                            # Check both current_room and current_room_id for compatibility
                            current_room = getattr(npc, "current_room", None)
                            current_room_id = getattr(npc, "current_room_id", None)
                            npc_room_id = current_room or current_room_id
                            if npc_room_id == room_id:
                                npc_ids.append(npc_id)
            except Exception as npc_query_error:
                logger.warning(
                    "Error querying NPCs from lifecycle manager, falling back to room.get_npcs()",
                    room_id=room_id,
                    error=str(npc_query_error),
                )
                # Fallback to room.get_npcs() if lifecycle manager query fails
                npc_ids = room.get_npcs() if hasattr(room, "get_npcs") else []

            # If no NPCs were found via lifecycle manager, fall back to room.get_npcs()
            if not npc_ids and "room" in locals() and hasattr(room, "get_npcs"):
                npc_ids = room.get_npcs()

            logger.debug(
                "Searching NPCs in room",
                room_id=room_id,
                target_name=target_name,
                npc_ids=npc_ids,
                npc_count=len(npc_ids),
            )

            for npc_id in npc_ids:
                # Get NPC instance
                npc_instance = self._get_npc_instance(npc_id)
                if not npc_instance:
                    continue

                # Normalize both names by removing punctuation for better matching
                normalized_target = target_name.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
                normalized_npc_name = (
                    npc_instance.name.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")
                )

                if normalized_target in normalized_npc_name:
                    logger.debug(
                        "NPC match found",
                        npc_id=npc_id,
                        npc_name=npc_instance.name,
                        target_name=target_name,
                        room_id=room_id,
                        npc_room_id=getattr(npc_instance, "current_room_id", "unknown"),
                    )
                    matches.append(
                        TargetMatch(
                            target_id=npc_id,
                            target_name=npc_instance.name,
                            target_type=TargetType.NPC,
                            room_id=room_id,
                            metadata={"npc_id": npc_id},
                        )
                    )

            # Add disambiguation suffixes if multiple NPCs have the same name
            if len(matches) > 1:
                name_counts: dict[str, int] = {}
                for match in matches:
                    name_counts[match.target_name] = name_counts.get(match.target_name, 0) + 1

                # Add suffixes for duplicate names
                name_suffixes = {}
                for match in matches:
                    if name_counts[match.target_name] > 1:
                        if match.target_name not in name_suffixes:
                            name_suffixes[match.target_name] = 1
                        else:
                            name_suffixes[match.target_name] += 1
                        match.disambiguation_suffix = f"-{name_suffixes[match.target_name]}"

            return matches

        except Exception as e:
            logger.error("Error searching NPCs in room", room_id=room_id, error=str(e))
            return []

    def _get_npc_instance(self, npc_id: str) -> NPCBase | None:
        """Get NPC instance from the spawning service."""
        try:
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                    return lifecycle_manager.active_npcs[npc_id]

            return None

        except Exception as e:
            logger.error("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None
