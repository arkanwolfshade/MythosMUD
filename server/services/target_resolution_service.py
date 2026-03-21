"""
Target resolution service for MythosMUD.

This service provides unified target resolution for both players and NPCs,
supporting partial name matching, disambiguation, and room-based filtering.
"""

# pylint: disable=too-few-public-methods,unnecessary-ellipsis  # Reason: Protocol stubs use ellipsis per PEP 544; focused service interfaces

import asyncio
import inspect
import re
import uuid
from collections.abc import Awaitable, Callable, Mapping, Sequence
from typing import Protocol, cast

from structlog.stdlib import BoundLogger

from ..models.player import Player
from ..models.room import Room
from ..npc.behaviors import NPCBase
from ..schemas.players.player import PlayerRead
from ..schemas.shared import TargetMatch, TargetResolutionResult, TargetType
from ..schemas.shared.target_metadata import TargetMetadata
from ..structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


class PersistenceProtocol(Protocol):
    """
    Persistence surface for target resolution.

    Matches ``AsyncPersistenceLayer`` (async player/room queries; ``get_room_by_id`` is sync).
    Runtime code still accepts legacy sync ``get_player`` / ``get_room`` via duck typing.
    """

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        """Get a player by ID."""

        ...

    def get_room_by_id(self, room_id: str) -> Room | None:
        """Get a room by ID."""

        ...

    async def get_players_in_room(self, room_id: str) -> Sequence[Player]:
        """Get all players in a room."""

        ...


class PlayerServiceProtocol(Protocol):
    """Protocol for player service dependency injection."""

    async def resolve_player_name(self, player_name: str) -> PlayerRead | None:
        """Resolve a player by name (parameter name matches ``PlayerService``)."""

        ...


class TargetResolutionService:  # pylint: disable=too-few-public-methods  # Reason: Resolution service class with focused responsibility, minimal public interface
    """
    Service for resolving target names to specific entities.

    This service handles target resolution for both players and NPCs,
    providing partial name matching, disambiguation, and room-based filtering.
    """

    persistence: PersistenceProtocol
    player_service: PlayerServiceProtocol

    def __init__(self, persistence: PersistenceProtocol, player_service: PlayerServiceProtocol) -> None:
        """
        Initialize the target resolution service.

        Args:
            persistence: Persistence layer instance
            player_service: Player service instance
        """
        self.persistence = persistence
        self.player_service = player_service

    async def _get_player_from_persistence(self, player_id_uuid: uuid.UUID) -> Player | None:
        """Get player from persistence layer, handling both async and sync methods."""
        raw: object = self.persistence
        if hasattr(raw, "get_player_by_id"):
            lookup: object = cast(object, getattr(raw, "get_player_by_id"))  # noqa: B009
            if inspect.iscoroutinefunction(lookup):
                logger.debug("Using async get_player_by_id", player_id=player_id_uuid)
                afn = cast(Callable[[uuid.UUID], Awaitable[object]], lookup)
                return cast(Player | None, await afn(player_id_uuid))
            logger.debug("Using sync get_player_by_id", player_id=player_id_uuid)
            sfn = cast(Callable[[uuid.UUID], object], lookup)
            return cast(Player | None, sfn(player_id_uuid))
        if hasattr(raw, "get_player"):
            lookup = cast(object, getattr(raw, "get_player"))  # noqa: B009
            if inspect.iscoroutinefunction(lookup):
                logger.debug("Using async get_player", player_id=player_id_uuid)
                afn = cast(Callable[[uuid.UUID], Awaitable[object]], lookup)
                return cast(Player | None, await afn(player_id_uuid))
            logger.debug("Using sync get_player", player_id=player_id_uuid)
            sfn = cast(Callable[[uuid.UUID], object], lookup)
            return cast(Player | None, sfn(player_id_uuid))
        logger.error(
            "Persistence layer has neither get_player nor get_player_by_id",
            persistence_type=type(self.persistence).__name__,
        )
        return None

    def _validate_player_and_room(
        self, player: Player | None, player_id_uuid: uuid.UUID
    ) -> tuple[str | None, TargetResolutionResult | None]:
        """Validate player exists and is in a room. Returns (room_id, error_result)."""
        if not player:
            logger.warning("Player not found for target resolution", player_id=player_id_uuid)
            return None, TargetResolutionResult(
                success=False, error_message="Player not found", search_term="", room_id=""
            )

        raw_room_id = getattr(player, "current_room_id", None)
        if raw_room_id is None:
            logger.warning("Player not in a room", player_id=player_id_uuid)
            return None, TargetResolutionResult(
                success=False, error_message="You are not in a room", search_term="", room_id=""
            )

        room_id = str(raw_room_id).strip()
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

    async def _gather_room_target_matches(
        self,
        room_id: str,
        clean_target: str,
        disambiguation_suffix: str | None,
        player_id_uuid: uuid.UUID,
        target_name: str,
    ) -> list[TargetMatch]:
        """Run player and NPC searches and log aggregate resolution stats."""
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
        return matches

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

        matches = await self._gather_room_target_matches(
            room_id, clean_target, disambiguation_suffix, player_id_uuid, target_name
        )
        return self._build_target_result(matches, target_name, room_id, disambiguation_suffix)

    async def _fetch_players_in_room(self, room_id: str) -> list[Player]:
        """Load players in room via persistence (async or sync ``get_players_in_room``)."""
        raw: object = self.persistence
        method: object = cast(object, getattr(raw, "get_players_in_room"))  # noqa: B009
        logger.debug(
            "_search_players_in_room: Checking method type",
            room_id=room_id,
            method="get_players_in_room",
            persistence_type=type(raw).__name__,
        )
        is_async = inspect.iscoroutinefunction(method)
        logger.debug(
            "_search_players_in_room: Method check result",
            room_id=room_id,
            is_async=is_async,
            method_type=type(method).__name__,
        )
        if is_async:
            logger.debug("_search_players_in_room: Using async method", room_id=room_id)
            afn = cast(Callable[[str], Awaitable[object]], method)
            players_raw = await afn(room_id)
            logger.debug("_search_players_in_room: Async method completed", room_id=room_id)
        else:
            logger.debug("_search_players_in_room: Using sync method in thread pool", room_id=room_id)
            sfn = cast(Callable[[str], object], method)
            players_raw = await asyncio.to_thread(sfn, room_id)
            logger.debug("_search_players_in_room: Thread pool method completed", room_id=room_id)
        return list(cast(Sequence[Player], players_raw))

    async def _search_players_in_room(
        self, room_id: str, target_name: str, disambiguation_suffix: str | None = None
    ) -> list[TargetMatch]:
        """Search for players in the specified room."""
        try:
            logger.debug("_search_players_in_room: Starting", room_id=room_id, target_name=target_name)
            logger.debug("_search_players_in_room: Getting players in room", room_id=room_id)
            players_in_room = await self._fetch_players_in_room(room_id)
            logger.debug("_search_players_in_room: Got players", room_id=room_id, player_count=len(players_in_room))
            matches: list[TargetMatch] = []

            for player in players_in_room:
                if target_name in player.name.lower():
                    if disambiguation_suffix:
                        continue

                    matches.append(
                        TargetMatch(
                            target_id=str(player.player_id),
                            target_name=player.name,
                            target_type=TargetType.PLAYER,
                            room_id=room_id,
                            metadata=TargetMetadata(additional_info={"player_id": str(player.player_id)}),
                        )
                    )

            if len(matches) > 1:
                matches = self._add_disambiguation_suffixes(matches)

            logger.debug("_search_players_in_room: Returning matches", room_id=room_id, matches_count=len(matches))
            return matches

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Player search errors unpredictable, must return empty list
            logger.error("Error searching players in room", room_id=room_id, error=str(e))
            return []

    def _validate_room_exists(self, room_id: str) -> bool:
        """Validate that a room exists using persistence layer."""
        raw: object = self.persistence
        if hasattr(raw, "get_room_by_id"):
            room_fn: object = cast(object, getattr(raw, "get_room_by_id"))  # noqa: B009
            if inspect.iscoroutinefunction(room_fn):
                logger.debug("Using async get_room_by_id", room_id=room_id)
                return True
            logger.debug("Using sync get_room_by_id", room_id=room_id)
            sfn = cast(Callable[[str], object], room_fn)
            room = sfn(room_id)
            return room is not None
        if hasattr(raw, "get_room"):
            room_fn = cast(object, getattr(raw, "get_room"))  # noqa: B009
            if inspect.iscoroutinefunction(room_fn):
                logger.debug("Using async get_room", room_id=room_id)
                return True
            logger.debug("Using sync get_room", room_id=room_id)
            sfn = cast(Callable[[str], object], room_fn)
            room = sfn(room_id)
            return room is not None
        logger.debug(
            "Persistence layer has no get_room method, skipping room validation",
            persistence_type=type(self.persistence).__name__,
            room_id=room_id,
        )
        return True

    async def _validate_room_exists_async(self, room_id: str) -> bool:
        """Validate that a room exists using async persistence layer."""
        raw: object = self.persistence
        if hasattr(raw, "get_room_by_id"):
            room_fn: object = cast(object, getattr(raw, "get_room_by_id"))  # noqa: B009
            if inspect.iscoroutinefunction(room_fn):
                afn = cast(Callable[[str], Awaitable[object]], room_fn)
                room = await afn(room_id)
                return room is not None
            sfn = cast(Callable[[str], object], room_fn)
            room = sfn(room_id)
            return room is not None
        if hasattr(raw, "get_room"):
            room_fn = cast(object, getattr(raw, "get_room"))  # noqa: B009
            if inspect.iscoroutinefunction(room_fn):
                afn = cast(Callable[[str], Awaitable[object]], room_fn)
                room = await afn(room_id)
                return room is not None
            sfn = cast(Callable[[str], object], room_fn)
            room = sfn(room_id)
            return room is not None
        return True

    def _normalize_name_for_matching(self, name: str) -> str:
        """Normalize name by removing punctuation for better matching."""
        return name.replace(".", "").replace(",", "").replace("!", "").replace("?", "").lower()

    def _match_npcs_by_name(self, npc_ids: list[str], target_name: str, room_id: str) -> list[TargetMatch]:
        """Match NPCs by name and create TargetMatch objects."""
        matches: list[TargetMatch] = []
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
                        metadata=TargetMetadata(additional_info={"npc_id": npc_id}),
                    )
                )

        return matches

    def _add_disambiguation_suffixes(self, matches: list[TargetMatch]) -> list[TargetMatch]:
        """Add disambiguation suffixes to matches with duplicate names."""
        name_counts: dict[str, int] = {}
        for match in matches:
            name_counts[match.target_name] = name_counts.get(match.target_name, 0) + 1

        name_suffixes: dict[str, int] = {}
        for match in matches:
            if name_counts[match.target_name] > 1:
                if match.target_name not in name_suffixes:
                    name_suffixes[match.target_name] = 1
                else:
                    name_suffixes[match.target_name] += 1
                match.disambiguation_suffix = f"-{name_suffixes[match.target_name]}"

        return matches

    @staticmethod
    def _npc_ids_in_room_from_active_map(active_npcs: Mapping[str, NPCBase], room_id: str) -> list[str]:
        """Collect NPC ids whose current room matches ``room_id``."""
        npc_ids: list[str] = []
        for npc_id, npc in active_npcs.items():
            current_room = getattr(npc, "current_room", None)
            current_room_id = getattr(npc, "current_room_id", None)
            npc_room_id = current_room or current_room_id
            if npc_room_id == room_id:
                npc_ids.append(npc_id)
        return npc_ids

    def _get_npcs_from_lifecycle_manager(self, room_id: str) -> list[str]:
        """Get NPC IDs from lifecycle manager for a room."""
        try:
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
                return []
            lifecycle_manager = npc_instance_service.lifecycle_manager
            if not lifecycle_manager or not hasattr(lifecycle_manager, "active_npcs"):
                return []
            active_npcs_dict = cast(Mapping[str, NPCBase], lifecycle_manager.active_npcs)
            return self._npc_ids_in_room_from_active_map(active_npcs_dict, room_id)
        except Exception as npc_query_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC query errors unpredictable, must fallback to room.get_npcs()
            logger.warning(
                "Error querying NPCs from lifecycle manager, falling back to room.get_npcs()",
                room_id=room_id,
                error=str(npc_query_error),
            )
        return []

    async def _load_npc_ids_with_room_fallback(self, room_id: str) -> list[str]:
        """NPC ids from lifecycle manager, else from room.get_npcs() via persistence."""
        npc_ids = self._get_npcs_from_lifecycle_manager(room_id)
        if npc_ids:
            return npc_ids

        raw: object = self.persistence
        if not hasattr(raw, "get_room_by_id"):
            return []
        room_fn: object = cast(object, getattr(raw, "get_room_by_id"))  # noqa: B009
        if inspect.iscoroutinefunction(room_fn):
            afn = cast(Callable[[str], Awaitable[object]], room_fn)
            room = await afn(room_id)
        else:
            sfn = cast(Callable[[str], object], room_fn)
            room = sfn(room_id)
        if room is not None and hasattr(room, "get_npcs"):
            get_npcs = cast(Callable[[], list[str]], cast(object, getattr(room, "get_npcs")))  # noqa: B009
            return list(get_npcs())
        return []

    async def _search_npcs_in_room(
        self,
        room_id: str,
        target_name: str,
        _disambiguation_suffix: str | None = None,  # pylint: disable=unused-argument  # Reason: Reserved for future disambiguation feature
    ) -> list[TargetMatch]:
        """Search for NPCs in the specified room."""
        try:
            room_exists = await self._validate_room_exists_async(room_id)
            if not room_exists:
                logger.debug("Room not found", room_id=room_id)
                return []

            npc_ids = await self._load_npc_ids_with_room_fallback(room_id)

            logger.debug(
                "Searching NPCs in room",
                room_id=room_id,
                target_name=target_name,
                npc_ids=npc_ids,
                npc_count=len(npc_ids),
            )

            matches = self._match_npcs_by_name(npc_ids, target_name, room_id)

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
