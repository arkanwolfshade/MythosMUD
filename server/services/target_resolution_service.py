"""
Target resolution service for MythosMUD.

This service provides unified target resolution for both players and NPCs,
supporting partial name matching, disambiguation, and room-based filtering.
"""

import re
from typing import Any, Protocol

from ..logging.enhanced_logging_config import get_logger
from ..schemas.target_resolution import TargetMatch, TargetResolutionResult, TargetType

logger = get_logger(__name__)


class PersistenceProtocol(Protocol):
    """Protocol for persistence layer dependency injection."""

    def get_player(self, player_id: str) -> Any: ...
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

    async def resolve_target(self, player_id: str, target_name: str) -> TargetResolutionResult:
        """
        Resolve a target name to specific entities.

        Args:
            player_id: ID of the player performing the action
            target_name: Name or partial name of the target

        Returns:
            TargetResolutionResult: Result containing matches and metadata
        """
        logger.debug("Resolving target", player_id=player_id, target_name=target_name)

        # Get player's current room
        player = self.persistence.get_player(player_id)
        if not player:
            logger.warning("Player not found for target resolution", player_id=player_id)
            return TargetResolutionResult(
                success=False, error_message="Player not found", search_term=target_name, room_id=""
            )

        room_id = player.current_room_id
        if not room_id:
            logger.warning("Player not in a room", player_id=player_id)
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
        player_matches = await self._search_players_in_room(room_id, clean_target, disambiguation_suffix)
        matches.extend(player_matches)

        # Search for NPCs in the room
        npc_matches = await self._search_npcs_in_room(room_id, clean_target, disambiguation_suffix)
        matches.extend(npc_matches)

        logger.debug(
            "Target resolution completed",
            player_id=player_id,
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
            players_in_room = self.persistence.get_players_in_room(room_id)  # type: ignore[attr-defined]
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

            return matches

        except Exception as e:
            logger.error("Error searching players in room", room_id=room_id, error=str(e))
            return []

    async def _search_npcs_in_room(
        self, room_id: str, target_name: str, disambiguation_suffix: str | None = None
    ) -> list[TargetMatch]:
        """Search for NPCs in the specified room."""
        try:
            # Get room data
            room = self.persistence.get_room(room_id)
            if not room:
                return []

            matches = []
            npc_ids = room.get_npcs() if hasattr(room, "get_npcs") else []

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

    def _get_npc_instance(self, npc_id: str) -> Any | None:
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
