"""
Target resolution service for MythosMUD.

This service provides unified target resolution for both players and NPCs,
supporting partial name matching, disambiguation, and room-based filtering.
"""

# pylint: disable=too-few-public-methods  # Reason: Target resolution service classes with focused responsibility, minimal public interface

import asyncio
import re
import uuid
from typing import Any, Protocol

from ..npc.behaviors import NPCBase
from ..schemas.target_resolution import TargetMatch, TargetResolutionResult, TargetType
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PersistenceProtocol(Protocol):
    """Protocol for persistence layer dependency injection."""

    def get_player(self, player_id: uuid.UUID) -> Any:
        """Get a player by ID."""

    def get_room(self, room_id: str) -> Any:
        """Get a room by ID."""

    def get_players_in_room(self, room_id: str) -> list[Any]:
        """Get all players in a room."""


class PlayerServiceProtocol(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol class with focused responsibility, minimal public interface
    """Protocol for player service dependency injection."""

    async def resolve_player_name(self, name: str) -> Any:
        """Resolve a player by name."""


class TargetResolutionService:  # pylint: disable=too-few-public-methods  # Reason: Resolution service class with focused responsibility, minimal public interface
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

    async def _get_player_from_persistence(self, player_id_uuid: uuid.UUID) -> Any | None:
        """Get player from persistence layer, handling both async and sync methods."""
        import inspect

        if hasattr(self.persistence, "get_player_by_id"):
            method = self.persistence.get_player_by_id
            if inspect.iscoroutinefunction(method):
                logger.debug("Using async get_player_by_id", player_id=player_id_uuid)
                return await method(player_id_uuid)
            logger.debug("Using sync get_player_by_id", player_id=player_id_uuid)
            return method(player_id_uuid)
        if hasattr(self.persistence, "get_player"):
            method = self.persistence.get_player
            if inspect.iscoroutinefunction(method):
                logger.debug("Using async get_player", player_id=player_id_uuid)
                return await method(player_id_uuid)
            logger.debug("Using sync get_player", player_id=player_id_uuid)
            return method(player_id_uuid)
        logger.error(
            "Persistence layer has neither get_player nor get_player_by_id",
            persistence_type=type(self.persistence).__name__,
        )
        return None

    def _validate_player_and_room(
        self, player: Any | None, player_id_uuid: uuid.UUID
    ) -> tuple[str | None, TargetResolutionResult | None]:
        """Validate player exists and is in a room. Returns (room_id, error_result)."""
        if not player:
            logger.warning("Player not found for target resolution", player_id=player_id_uuid)
            return None, TargetResolutionResult(
                success=False, error_message="Player not found", search_term="", room_id=""
            )

        room_id = player.current_room_id
        if room_id is not None:
            room_id = str(room_id)
        if not room_id:
            logger.warning("Player not in a room", player_id=player_id_uuid)
            return None, TargetResolutionResult(
                success=False, error_message="You are not in a room", search_term="", room_id=""
            )

        return room_id, None

    def _clean_target_name(self, target_name: str) -> tuple[str, str | None]:
        """Clean target name and extract disambiguation suffix. Returns (clean_target, suffix)."""
        clean_target = target_name.strip().lower()
        if not clean_target:
            return clean_target, None

        disambiguation_suffix = None
        if re.match(r".*-\d+$", clean_target):
            base_name = re.sub(r"-\d+$", "", clean_target)
            suffix_match = re.search(r"-(\d+)$", clean_target)
            if suffix_match:
                disambiguation_suffix = f"-{suffix_match.group(1)}"
                clean_target = base_name

        return clean_target, disambiguation_suffix

    def _build_target_result(
        self, matches: list[TargetMatch], target_name: str, room_id: str, disambiguation_suffix: str | None
    ) -> TargetResolutionResult:
        """Build TargetResolutionResult from matches."""
        if not matches:
            return TargetResolutionResult(
                success=False,
                error_message=f"No targets found matching '{target_name}'",
                search_term=target_name,
                room_id=room_id,
            )

        if len(matches) == 1:
            return TargetResolutionResult(success=True, matches=matches, search_term=target_name, room_id=room_id)

        if disambiguation_suffix:
            for match in matches:
                if match.disambiguation_suffix == disambiguation_suffix:
                    return TargetResolutionResult(
                        success=True, matches=[match], search_term=target_name, room_id=room_id
                    )
            return TargetResolutionResult(
                success=False,
                error_message=f"No target found with suffix '{disambiguation_suffix}'",
                search_term=target_name,
                room_id=room_id,
            )

        return TargetResolutionResult(
            success=False,
            matches=matches,
            disambiguation_required=True,
            error_message=f"Multiple targets match '{target_name}': {', '.join([match.target_name for match in matches])}",
            search_term=target_name,
            room_id=room_id,
        )

    async def resolve_target(self, player_id: uuid.UUID | str, target_name: str) -> TargetResolutionResult:
        """
        Resolve a target name to specific entities.

        Args:
            player_id: ID of the player performing the action (UUID or string for backward compatibility)
            target_name: Name or partial name of the target

        Returns:
            TargetResolutionResult: Result containing matches and metadata
        """
        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        logger.debug("Resolving target", player_id=player_id_uuid, target_name=target_name)

        player = await self._get_player_from_persistence(player_id_uuid)
        if player is None:
            return TargetResolutionResult(
                success=False,
                error_message="Internal error: persistence layer not configured correctly",
                search_term=target_name,
                room_id="",
            )

        room_id, error_result = self._validate_player_and_room(player, player_id_uuid)
        if error_result:
            error_result.search_term = target_name
            return error_result

        if room_id is None:
            return TargetResolutionResult(
                success=False, error_message="Player not in a room", search_term=target_name, room_id=""
            )

        clean_target, disambiguation_suffix = self._clean_target_name(target_name)
        if not clean_target:
            return TargetResolutionResult(
                success=False, error_message="No target specified", search_term=target_name, room_id=room_id
            )

        logger.debug("About to search players in room", room_id=room_id, target_name=clean_target)
        player_matches = await self._search_players_in_room(room_id, clean_target, disambiguation_suffix)
        logger.debug("Player search completed", room_id=room_id, matches_count=len(player_matches))

        logger.debug("About to search NPCs in room", room_id=room_id, target_name=clean_target)
        npc_matches = await self._search_npcs_in_room(room_id, clean_target, disambiguation_suffix)
        logger.debug("NPC search completed", room_id=room_id, matches_count=len(npc_matches))

        matches = player_matches + npc_matches
        logger.debug(
            "Target resolution completed",
            player_id=player_id_uuid,
            target_name=target_name,
            room_id=room_id,
            player_matches=len(player_matches),
            npc_matches=len(npc_matches),
            total_matches=len(matches),
        )

        return self._build_target_result(matches, target_name, room_id, disambiguation_suffix)

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
                players_in_room = await method(room_id)  # type: ignore[misc]  # Reason: Protocol defines method as sync, but runtime check confirms it's async, type checker cannot infer runtime behavior
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Player search errors unpredictable, must return empty list
            logger.error("Error searching players in room", room_id=room_id, error=str(e))
            return []

    def _validate_room_exists(self, room_id: str) -> bool:
        """Validate that a room exists using persistence layer."""
        import inspect

        # Check if persistence layer has async method (AsyncPersistenceLayer)
        if hasattr(self.persistence, "get_room_by_id"):
            method = self.persistence.get_room_by_id
            if inspect.iscoroutinefunction(method):
                logger.debug("Using async get_room_by_id", room_id=room_id)
                # Note: This is called from async context, but we can't await here
                # The caller will handle the async call
                return True
            logger.debug("Using sync get_room_by_id", room_id=room_id)
            room = method(room_id)
            return room is not None
        if hasattr(self.persistence, "get_room"):
            method = self.persistence.get_room
            if inspect.iscoroutinefunction(method):
                logger.debug("Using async get_room", room_id=room_id)
                return True
            logger.debug("Using sync get_room", room_id=room_id)
            room = method(room_id)
            return room is not None
        # If persistence layer doesn't have get_room, skip validation
        logger.debug(
            "Persistence layer has no get_room method, skipping room validation",
            persistence_type=type(self.persistence).__name__,
            room_id=room_id,
        )
        return True  # Assume room exists if we can't validate

    async def _validate_room_exists_async(self, room_id: str) -> bool:
        """Validate that a room exists using async persistence layer."""
        import inspect

        if hasattr(self.persistence, "get_room_by_id"):
            method = self.persistence.get_room_by_id
            if inspect.iscoroutinefunction(method):
                room = await method(room_id)
                return room is not None
            room = method(room_id)
            return room is not None
        if hasattr(self.persistence, "get_room"):
            method = self.persistence.get_room
            if inspect.iscoroutinefunction(method):
                room = await method(room_id)
                return room is not None
            room = method(room_id)
            return room is not None
        return True

    def _normalize_name_for_matching(self, name: str) -> str:
        """Normalize name by removing punctuation for better matching."""
        return name.replace(".", "").replace(",", "").replace("!", "").replace("?", "").lower()

    def _match_npcs_by_name(self, npc_ids: list[str], target_name: str, room_id: str) -> list[TargetMatch]:
        """Match NPCs by name and create TargetMatch objects."""
        matches = []
        normalized_target = self._normalize_name_for_matching(target_name)

        for npc_id in npc_ids:
            npc_instance = self._get_npc_instance(npc_id)
            if not npc_instance:
                continue

            normalized_npc_name = self._normalize_name_for_matching(npc_instance.name)

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

        return matches

    def _add_disambiguation_suffixes(self, matches: list[TargetMatch]) -> list[TargetMatch]:
        """Add disambiguation suffixes to matches with duplicate names."""
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

    def _get_npcs_from_lifecycle_manager(self, room_id: str) -> list[str]:
        """Get NPC IDs from lifecycle manager for a room."""
        try:
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                    active_npcs_dict = lifecycle_manager.active_npcs
                    npc_ids = []
                    for npc_id, npc in active_npcs_dict.items():
                        current_room = getattr(npc, "current_room", None)
                        current_room_id = getattr(npc, "current_room_id", None)
                        npc_room_id = current_room or current_room_id
                        if npc_room_id == room_id:
                            npc_ids.append(npc_id)
                    return npc_ids
        except Exception as npc_query_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC query errors unpredictable, must fallback to room.get_npcs()
            logger.warning(
                "Error querying NPCs from lifecycle manager, falling back to room.get_npcs()",
                room_id=room_id,
                error=str(npc_query_error),
            )
        return []

    async def _search_npcs_in_room(
        self,
        room_id: str,
        target_name: str,
        _disambiguation_suffix: str | None = None,  # pylint: disable=unused-argument  # Reason: Reserved for future disambiguation feature
    ) -> list[TargetMatch]:
        """Search for NPCs in the specified room."""
        try:
            # Validate room exists
            room_exists = await self._validate_room_exists_async(room_id)
            if not room_exists:
                logger.debug("Room not found", room_id=room_id)
                return []

            matches = []
            # CRITICAL FIX: Query NPCs from lifecycle manager instead of Room instance
            # Room instances are recreated from persistence and lose in-memory NPC tracking
            # NPCs are actually tracked in the lifecycle manager with their current_room_id
            npc_ids = self._get_npcs_from_lifecycle_manager(room_id)

            # Fallback to room.get_npcs() if lifecycle manager query fails
            if not npc_ids:
                import inspect

                if hasattr(self.persistence, "get_room_by_id"):
                    method = self.persistence.get_room_by_id
                    if inspect.iscoroutinefunction(method):
                        room = await method(room_id)
                    else:
                        room = method(room_id)
                    if room and hasattr(room, "get_npcs"):
                        npc_ids = room.get_npcs()

            logger.debug(
                "Searching NPCs in room",
                room_id=room_id,
                target_name=target_name,
                npc_ids=npc_ids,
                npc_count=len(npc_ids),
            )

            matches = self._match_npcs_by_name(npc_ids, target_name, room_id)

            # Add disambiguation suffixes if multiple NPCs have the same name
            if len(matches) > 1:
                matches = self._add_disambiguation_suffixes(matches)

            return matches

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC search errors unpredictable, must return empty list
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC instance retrieval errors unpredictable, must return None
            logger.error("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None
