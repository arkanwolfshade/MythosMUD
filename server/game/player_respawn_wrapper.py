"""
Player respawn wrapper service.

This module provides wrapper methods for player respawn operations that integrate
with the PlayerRespawnService and handle multi-character scenarios.
"""

import datetime
import uuid
from typing import TYPE_CHECKING, Any

from ..exceptions import ValidationError
from ..models.player import Player
from ..services.player_respawn_service import LIMBO_ROOM_ID
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.enhanced_error_logging import create_error_context, log_and_raise_enhanced

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from ..services.player_respawn_service import PlayerRespawnService

logger = get_logger(__name__)


class PlayerRespawnWrapper:
    """Wrapper service for player respawn operations."""

    def __init__(self, persistence: Any) -> None:
        """Initialize with a persistence layer."""
        self.persistence = persistence

    async def respawn_player_by_user_id(  # pylint: disable=too-many-locals  # Reason: Respawn requires many intermediate variables for complex respawn logic
        self,
        user_id: str,
        session: "AsyncSession",
        respawn_service: "PlayerRespawnService",
        persistence: Any,  # AsyncPersistenceLayer
    ) -> dict[str, Any]:
        """
        Respawn a dead player by user ID.

        This method handles the complete respawn flow:
        1. Gets player by user_id
        2. Verifies player is dead
        3. Calls respawn service to respawn player
        4. Gets respawn room data
        5. Returns structured response

        Args:
            user_id: The user ID to respawn
            session: Database session for player data access
            respawn_service: PlayerRespawnService instance
            persistence: AsyncPersistenceLayer for room data access

        Returns:
            dict: Respawn response with player and room data

        Raises:
            ValidationError: If player not found or not dead
        """
        from sqlalchemy import select
        from sqlalchemy.orm import selectinload

        # MULTI-CHARACTER: Get all active players for user, then find the dead one
        # Look up all active players by user_id (not primary key player_id)
        # Eagerly load user relationship to prevent N+1 queries
        stmt = (
            select(Player)
            .options(selectinload(Player.user))
            .where(Player.user_id == user_id)
            .where(Player.is_deleted.is_(False))  # Use is_() for SQLAlchemy boolean comparison
        )
        result = await session.execute(stmt)
        all_players = list(result.scalars().all())

        if not all_players:
            context = create_error_context()
            context.metadata["operation"] = "respawn_player_by_user_id"
            context.metadata["user_id"] = user_id
            log_and_raise_enhanced(
                ValidationError,
                "Player not found for respawn",
                context=context,
                details={"user_id": user_id},
                user_friendly="Player not found",
            )

        # MULTI-CHARACTER: Find the dead player(s) among active characters.
        # Treat as dead: (1) DP <= -10, or (2) in limbo (handles persistence race or restart).
        def _is_eligible_for_respawn(p: Player) -> bool:
            if p.is_dead():
                return True
            if str(p.current_room_id or "") == LIMBO_ROOM_ID:
                return True
            return False

        dead_players = [p for p in all_players if _is_eligible_for_respawn(p)]

        if not dead_players:
            # No dead players found - check if any players exist to give better error message
            context = create_error_context()
            context.metadata["operation"] = "respawn_player_by_user_id"
            context.metadata["user_id"] = user_id
            if all_players:
                context.metadata["player_dp"] = all_players[0].get_stats().get("current_dp", 0)
            log_and_raise_enhanced(
                ValidationError,
                "Player must be dead to respawn (DP must be -10 or below)",
                context=context,
                details={
                    "user_id": user_id,
                    "player_dp": all_players[0].get_stats().get("current_dp", 0) if all_players else None,
                },
                user_friendly="Player must be dead to respawn",
            )

        # MULTI-CHARACTER: If multiple dead players, select the most recently active one
        if len(dead_players) > 1:
            # Sort by last_active descending (most recent first) and take the first
            dead_players.sort(key=lambda p: p.last_active if p.last_active else datetime.datetime.min, reverse=True)

        player = dead_players[0]

        # Respawn the player
        # Convert player.player_id to UUID (handles SQLAlchemy Column[str])
        # SQLAlchemy Column[str] returns UUID at runtime, but mypy sees it as Column[str]
        # Always convert to string first, then to UUID
        player_id_value = player.player_id
        player_id_uuid = uuid.UUID(str(player_id_value))
        success = await respawn_service.respawn_player(player_id_uuid, session)
        if not success:
            logger.error("Respawn failed", player_id=player.player_id)
            context = create_error_context()
            context.metadata["operation"] = "respawn_player_by_user_id"
            context.metadata["user_id"] = user_id
            # Structlog handles UUID objects automatically, no need to convert to string
            context.metadata["player_id"] = player.player_id
            log_and_raise_enhanced(
                ValidationError,
                "Failed to respawn player",
                context=context,
                # Structlog handles UUID objects automatically, no need to convert to string
                details={"user_id": user_id, "player_id": player.player_id},
                user_friendly="Respawn failed",
            )

        # Get respawn room data
        respawn_room_id = player.current_room_id  # Updated by respawn_player
        room = persistence.get_room_by_id(str(respawn_room_id))
        if not room:
            logger.warning("Respawn room not found", respawn_room_id=respawn_room_id)
            room_data = {"id": respawn_room_id, "name": "Unknown Room"}
        else:
            room_data = room.to_dict()

        # Get updated player state
        updated_stats = player.get_stats()

        logger.info("Player respawned successfully", player_id=player.player_id, respawn_room=respawn_room_id)

        return {
            "success": True,
            "player": {
                "id": player.player_id,
                "name": player.name,
                "dp": updated_stats.get("current_dp", 100),
                "max_dp": updated_stats.get("max_dp", 100),
                "current_room_id": respawn_room_id,
            },
            "room": room_data,
            "message": "You have been resurrected and returned to the waking world",
        }

    async def respawn_player_from_delirium_by_user_id(  # pylint: disable=too-many-locals  # Reason: Delirium respawn requires many intermediate variables for complex respawn logic
        self,
        user_id: str,
        session: "AsyncSession",
        respawn_service: "PlayerRespawnService",
        persistence: Any,  # AsyncPersistenceLayer
    ) -> dict[str, Any]:
        """
        Respawn a delirious player by user ID.

        This method handles the complete delirium respawn flow:
        1. Gets player by user_id
        2. Verifies player is delirious (lucidity <= -10)
        3. Calls respawn service to respawn player from delirium
        4. Gets respawn room data
        5. Returns structured response

        Args:
            user_id: The user ID to respawn
            session: Database session for player data access
            respawn_service: PlayerRespawnService instance
            persistence: AsyncPersistenceLayer for room data access

        Returns:
            dict: Respawn response with player and room data

        Raises:
            ValidationError: If player not found or not delirious
        """
        from sqlalchemy import select
        from sqlalchemy.orm import selectinload

        from ..models.lucidity import PlayerLucidity

        # Look up player by user_id (not primary key player_id)
        # Eagerly load user relationship to prevent N+1 queries
        stmt = select(Player).options(selectinload(Player.user)).where(Player.user_id == user_id)
        result = await session.execute(stmt)
        player = result.scalar_one_or_none()
        if not player:
            context = create_error_context()
            context.metadata["operation"] = "respawn_player_from_delirium_by_user_id"
            context.metadata["user_id"] = user_id
            log_and_raise_enhanced(
                ValidationError,
                "Player not found for delirium respawn",
                context=context,
                details={"user_id": user_id},
                user_friendly="Player not found",
            )

        # Verify player is delirious (lucidity <= -10)
        lucidity_record = await session.get(PlayerLucidity, player.player_id)
        if not lucidity_record or lucidity_record.current_lcd > -10:
            context = create_error_context()
            context.metadata["operation"] = "respawn_player_from_delirium_by_user_id"
            context.metadata["user_id"] = user_id
            current_lucidity = lucidity_record.current_lcd if lucidity_record else None
            context.metadata["player_lucidity"] = current_lucidity
            log_and_raise_enhanced(
                ValidationError,
                "Player must be delirious to respawn (lucidity must be -10 or below)",
                context=context,
                details={"user_id": user_id, "player_lucidity": current_lucidity},
                user_friendly="Player must be delirious to respawn",
            )

        # Respawn the player from delirium
        # Convert player.player_id to UUID (handles SQLAlchemy Column[str])
        player_id_value = player.player_id
        player_id_uuid = uuid.UUID(str(player_id_value))
        success = await respawn_service.respawn_player_from_delirium(player_id_uuid, session)
        if not success:
            logger.error("Delirium respawn failed", player_id=player.player_id)
            context = create_error_context()
            context.metadata["operation"] = "respawn_player_from_delirium_by_user_id"
            context.metadata["user_id"] = user_id
            context.metadata["player_id"] = player.player_id
            log_and_raise_enhanced(
                ValidationError,
                "Failed to respawn player from delirium",
                context=context,
                details={"user_id": user_id, "player_id": player.player_id},
                user_friendly="Delirium respawn failed",
            )

        # Get respawn room data
        respawn_room_id = player.current_room_id  # Updated by respawn_player_from_delirium
        room = persistence.get_room_by_id(str(respawn_room_id))

        if not room:
            logger.warning("Respawn room not found", respawn_room_id=respawn_room_id)
            room_data = {"id": respawn_room_id, "name": "Unknown Room"}
        else:
            room_data = room.to_dict()

        # Get updated player state
        updated_stats = player.get_stats()

        # Get updated lucidity
        await session.refresh(lucidity_record)
        updated_lucidity = lucidity_record.current_lcd

        logger.info(
            "Player respawned from delirium successfully",
            player_id=player.player_id,
            respawn_room=respawn_room_id,
            new_lucidity=updated_lucidity,
        )

        return {
            "success": True,
            "player": {
                "id": player.player_id,
                "name": player.name,
                "dp": updated_stats.get("current_dp", 100),
                "max_dp": updated_stats.get("max_dp", 100),
                "lucidity": updated_lucidity,
                "current_room_id": respawn_room_id,
            },
            "room": room_data,
            "message": "You have been restored to lucidity and returned to the Sanitarium",
        }
