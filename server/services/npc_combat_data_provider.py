"""
NPC Combat Data Provider.

This module provides data retrieval and preparation for NPC combat,
including NPC instances, definitions, player data, and combat participant data.
"""

from typing import Any, cast
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from server.game.npcs.attack_damage import armor_points_from_base_stats

from ..models.combat import CombatParticipantType
from ..npc.lifecycle_manager import NPCLifecycleManager
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from .combat_types import CombatParticipantData

logger: BoundLogger = get_logger(__name__)


class NPCCombatDataProvider:
    """Provides data retrieval and preparation for NPC combat."""

    _persistence: Any  # Persistence-like object; may have get_npc_lifecycle_manager (optional)

    def __init__(self, async_persistence: Any) -> None:
        """
        Initialize the data provider.

        Args:
            async_persistence: Async persistence layer instance
        """
        self._persistence = async_persistence

    def get_npc_instance(self, npc_id: str) -> Any | None:
        """
        Get NPC instance from the spawning service.

        Args:
            npc_id: ID of the NPC

        Returns:
            NPC instance if found, None otherwise
        """
        try:
            from .npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                    return lifecycle_manager.active_npcs[npc_id]

            return None

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None

    async def get_npc_definition(self, npc_id: str) -> Any | None:
        """
        Get NPC definition for an NPC instance.

        Uses persistence.get_npc_lifecycle_manager when available; otherwise
        falls back to the instance service lifecycle (same source as get_npc_instance)
        so that XP mapping works when persistence does not expose the lifecycle manager.

        Args:
            npc_id: ID of the NPC (lifecycle key, e.g. string from _generate_npc_id or instance id)

        Returns:
            NPC definition if found, None otherwise
        """
        try:
            import asyncio

            lifecycle_manager = None
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = await asyncio.to_thread(self._persistence.get_npc_lifecycle_manager)

            if not lifecycle_manager:
                from .npc_instance_service import get_npc_instance_service

                npc_instance_service = get_npc_instance_service()
                if hasattr(npc_instance_service, "lifecycle_manager"):
                    lifecycle_manager = npc_instance_service.lifecycle_manager

            if lifecycle_manager:
                lm = cast(NPCLifecycleManager, lifecycle_manager)
                if npc_id in lm.lifecycle_records:
                    return lm.lifecycle_records[npc_id].definition

            return None

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error("Error getting NPC definition", npc_id=npc_id, error=str(e))
            return None

    async def get_player_name(self, player_id: str) -> str:
        """
        Get player name for messaging.

        Args:
            player_id: ID of the player

        Returns:
            Player name, or "Unknown Player" if not found
        """
        try:
            # Convert player_id to UUID if it's a string
            player_id_uuid = UUID(player_id)
            player = await self._persistence.get_player_by_id(player_id_uuid)
            return str(player.name) if player else "Unknown Player"
        except (OSError, ValueError, TypeError) as e:
            logger.error("Error getting player name", player_id=player_id, error=str(e), error_type=type(e).__name__)
            return "Unknown Player"

    async def get_player_room_id(self, player_id: str) -> str | None:
        """
        Get the current room ID for a player.

        Args:
            player_id: ID of the player (must be a valid UUID string)

        Returns:
            Room ID if found, None otherwise
        """
        try:
            # Convert player_id to UUID; invalid format (e.g. test placeholder "player_001") returns None without error log
            try:
                player_id_uuid = UUID(player_id)
            except ValueError:
                logger.debug(
                    "Invalid player_id format for room lookup, returning None",
                    player_id=player_id,
                )
                return None
            player = await self._persistence.get_player_by_id(player_id_uuid)
            if player:
                return str(player.current_room_id)
            return None
        except (AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error("Error getting player room ID", player_id=player_id, error=str(e))
            return None

    async def get_player_combat_data(
        self, player_id: str, attacker_uuid: UUID, player_name: str
    ) -> CombatParticipantData:
        """
        Get player combat participant data from persistence.

        Args:
            player_id: ID of the attacking player
            attacker_uuid: UUID of the attacker
            player_name: Name of the player

        Returns:
            CombatParticipantData for the player

        BUGFIX: Was hardcoded to 100, causing DP to reset between combats
        """
        # Fetch actual player stats from persistence to ensure correct DP
        player_id_uuid = UUID(player_id)
        player = await self._persistence.get_player_by_id(player_id_uuid)
        if not player:
            logger.error("Player not found when starting combat", player_id=player_id)
            raise ValueError(f"Player {player_id} not found")

        combat_stats = player.get_combat_stats()
        # #815: the player's live corruption, for the NPC-side aggro affinity curve.
        # Reason: DYNAMIC_DISPATCH - player comes from self._persistence.get_player_by_id(), and
        # _persistence is declared Any throughout this data-provider layer (a mock in tests, a
        # real AsyncPersistence in production).
        # Appropriate because: coerce_int() is the same defensive-parsing helper already used
        # everywhere else in this codebase for untyped stats dict values; retyping _persistence
        # is a much larger, unrelated change out of scope here.
        corruption = coerce_int(player.get_stats().get("corruption", 0), default=0)  # pyright: ignore[reportAny]

        logger.info(
            "Starting combat with player stats",
            player_id=player_id,
            current_dp=combat_stats["current_dp"],
            max_dp=combat_stats["max_dp"],
            dex=combat_stats["dexterity"],
        )

        return CombatParticipantData(
            participant_id=attacker_uuid,
            name=player_name,
            current_dp=combat_stats["current_dp"],
            max_dp=combat_stats["max_dp"],
            dexterity=combat_stats["dexterity"],
            participant_type=CombatParticipantType.PLAYER,
            corruption=corruption,
        )

    # Reason: DYNAMIC_DISPATCH - npc_instance is declared Any (this provider accepts a plain test
    # double or a real NPCBase subclass interchangeably, matching get_npc_combat_data's own
    # established, unsuppressed convention below).
    # Appropriate because: retyping npc_instance would mean picking one concrete NPC class for a
    # parameter this file deliberately keeps duck-typed.
    def _resolve_npc_combat_stats(
        self,
        # Reason: DYNAMIC_DISPATCH - npc_instance is Any per this class's established convention.
        # Appropriate because: same unsuppressed convention as get_npc_combat_data's own signature.
        npc_instance: Any,  # pyright: ignore[reportAny, reportExplicitAny]
        # Reason: DYNAMIC_DISPATCH - the return dict's values come from the same Any npc_instance.
        # Appropriate because: same unsuppressed convention as this function's own parameter.
    ) -> dict[str, Any]:  # pyright: ignore[reportExplicitAny]
        """Get combat_stats (current_dp/max_dp/dexterity) from an NPC instance."""
        # Reason: DYNAMIC_DISPATCH - npc_instance is Any per this function's own parameter above.
        # Appropriate because: same unsuppressed convention as this function's own signature.
        if hasattr(npc_instance, "get_combat_stats"):  # pyright: ignore[reportAny]
            # Reason: DYNAMIC_DISPATCH - same untyped npc_instance convention as above.
            # Appropriate because: same unsuppressed convention as this function's own signature.
            return cast(dict[str, Any], npc_instance.get_combat_stats())  # pyright: ignore[reportAny, reportExplicitAny]
        # Reason: DYNAMIC_DISPATCH - same untyped npc_instance convention as above.
        # Appropriate because: same unsuppressed convention as this function's own signature.
        npc_stats = npc_instance.get_stats()  # pyright: ignore[reportAny]
        return {
            # Reason: DYNAMIC_DISPATCH - npc_stats is Any per the untyped get_stats() call above.
            # Appropriate because: same unsuppressed convention as this function's own signature.
            "current_dp": int(npc_stats.get("determination_points", npc_stats.get("dp", 100))),  # pyright: ignore[reportAny]
            # Reason: DYNAMIC_DISPATCH - same untyped npc_stats convention as above.
            # Appropriate because: same unsuppressed convention as this function's own signature.
            "max_dp": int(npc_stats.get("max_dp", npc_stats.get("max_hp", 100))),  # pyright: ignore[reportAny]
            # Reason: DYNAMIC_DISPATCH - same untyped npc_stats convention as above.
            # Appropriate because: same unsuppressed convention as this function's own signature.
            "dexterity": int(npc_stats.get("dexterity", 10)),  # pyright: ignore[reportAny]
        }

    def _resolve_npc_behavior_snapshot(
        self,
        # Reason: DYNAMIC_DISPATCH - npc_instance is Any per this class's established convention
        # (see _resolve_npc_combat_stats above).
        # Appropriate because: same unsuppressed convention as this class's other NPC-instance access.
        npc_instance: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    ) -> tuple[dict[str, object] | None, int | None]:
        """Get (behavior_config snapshot, clamped aggression_level) from an NPC instance."""
        # Reason: DYNAMIC_DISPATCH - npc_instance is Any per this function's own parameter above.
        # Appropriate because: same unsuppressed convention as this function's own signature.
        if not hasattr(npc_instance, "get_behavior_config"):  # pyright: ignore[reportAny]
            return None, None
        try:
            # Reason: DYNAMIC_DISPATCH - same untyped npc_instance convention as above.
            # Appropriate because: same unsuppressed convention as this function's own signature.
            behavior_config = npc_instance.get_behavior_config()  # pyright: ignore[reportAny]
            if not isinstance(behavior_config, dict):
                return None, None
            typed_behavior_config = cast(dict[object, object], behavior_config)
            behavior_snapshot = {str(k): v for k, v in typed_behavior_config.items()}
            aggression_level: int | None = None
            raw = typed_behavior_config.get("aggression_level")
            if raw is not None:
                try:
                    # Reason: SERIALIZATION_BOUNDARY - raw is object from the untyped
                    # behavior_config dict; int() on an arbitrary object is guarded by the
                    # except clause below.
                    # Appropriate because: aggression_level's whole point is to clamp/validate
                    # this loosely-typed config value, so accepting object here is correct.
                    aggression_level = max(0, min(10, int(raw)))  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]  # Reason: CHECKER_CONFLICT:call-overload - mypy rejects int(object) statically; basedpyright is authoritative and the surrounding try/except guards the runtime case.
                except (TypeError, ValueError):
                    pass
            return behavior_snapshot, aggression_level
        except (ValueError, AttributeError, TypeError):
            return None, None

    def get_npc_combat_data(self, npc_instance: Any, target_uuid: UUID) -> CombatParticipantData:
        """
        Get NPC combat participant data from NPC instance.

        Args:
            npc_instance: NPC instance
            target_uuid: UUID of the target

        Returns:
            CombatParticipantData for the NPC
        """
        combat_stats = self._resolve_npc_combat_stats(npc_instance)

        # #815: the NPC's static corruption trait (base_stats), independent of which combat_stats
        # projection was used above -- for the aggro affinity curve.
        # Reason: DYNAMIC_DISPATCH - npc_instance is declared Any (this provider accepts a plain
        # test double or a real NPCBase subclass interchangeably).
        # Appropriate because: the isinstance(..., dict) guard below is the actual type safety
        # net; retyping npc_instance would mean picking one concrete NPC class for a parameter
        # this file deliberately keeps duck-typed.
        npc_stats_for_corruption: object = npc_instance.get_stats() if hasattr(npc_instance, "get_stats") else {}  # pyright: ignore[reportAny]
        corruption = (
            coerce_int(npc_stats_for_corruption.get("corruption", 0), default=0)  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]
            if isinstance(npc_stats_for_corruption, dict)
            else 0
        )

        npc_id = getattr(npc_instance, "id", getattr(npc_instance, "npc_id", "unknown"))
        npc_type = getattr(npc_instance, "npc_type", None)

        npc_stats_snapshot: dict[str, object] | None = None
        if isinstance(npc_stats_for_corruption, dict):
            npc_stats_snapshot = {str(k): v for k, v in cast(dict[object, object], npc_stats_for_corruption).items()}

        behavior_snapshot, aggression_level = self._resolve_npc_behavior_snapshot(npc_instance)
        logger.info(
            "NPC combat stats from model",
            npc_id=npc_id,
            npc_name=npc_instance.name,
            current_dp=combat_stats["current_dp"],
            max_dp=combat_stats["max_dp"],
        )

        # Reason: SERIALIZATION_BOUNDARY - combat_stats is dict[str, Any] per
        # _resolve_npc_combat_stats's own established, unsuppressed return type.
        # Appropriate because: current_dp/max_dp/dexterity are already coerced to int inside
        # that helper; a TypedDict is out of scope for this complexity-only extraction.
        return CombatParticipantData(
            participant_id=target_uuid,
            name=npc_instance.name,
            current_dp=combat_stats["current_dp"],  # pyright: ignore[reportAny]
            # Reason: SERIALIZATION_BOUNDARY - same dict[str, Any] convention as current_dp above.
            # Appropriate because: same unsuppressed convention as this block's own comment.
            max_dp=combat_stats["max_dp"],  # pyright: ignore[reportAny]
            # Reason: SERIALIZATION_BOUNDARY - same dict[str, Any] convention as current_dp above.
            # Appropriate because: same unsuppressed convention as this block's own comment.
            dexterity=combat_stats["dexterity"],  # pyright: ignore[reportAny]
            participant_type=CombatParticipantType.NPC,
            npc_type=npc_type,
            corruption=corruption,
            aggression_level=aggression_level,
            armor_points=armor_points_from_base_stats(npc_stats_snapshot),
            npc_base_stats=npc_stats_snapshot,
            npc_behavior_config=behavior_snapshot,
        )
