"""
Player Preferences Service for Advanced Chat Channels.

This module provides functionality for managing player channel preferences
including default channel settings and channel muting preferences.
"""

# pylint: disable=too-many-return-statements  # Reason: Preferences service methods require multiple return statements for early validation returns (permission checks, validation, error handling)

import json
import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from server.models.player import PlayerChannelPreferences
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PlayerPreferencesService:
    """
    Service for managing player channel preferences.

    This service handles:
    - Player default channel preferences
    - Channel muting preferences (stored in PostgreSQL database)
    - Preference persistence across sessions
    """

    def __init__(self) -> None:
        """
        Initialize the PlayerPreferencesService.

        Note: This service now uses PostgreSQL via SQLAlchemy async sessions.
        The session must be provided to each method call.
        """
        # Valid channel names
        self._valid_channels = {"local", "global", "whisper", "system"}

        logger.info("PlayerPreferencesService initialized (PostgreSQL)")

    async def create_player_preferences(self, session: AsyncSession, player_id: uuid.UUID | str) -> dict[str, Any]:
        """
        Create default preferences for a new player.

        Args:
            session: Database session
            player_id: The player's unique identifier (UUID or string)

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        # Normalize player_id to UUID object for database operations
        if isinstance(player_id, str):
            player_id = uuid.UUID(player_id)

        try:
            # Check if preferences already exist
            result = await session.execute(
                select(PlayerChannelPreferences).where(PlayerChannelPreferences.player_id == player_id)
            )
            existing = result.scalar_one_or_none()
            if existing:
                return {"success": False, "error": "Player preferences already exist"}

            # Create new preferences
            preferences = PlayerChannelPreferences(
                player_id=player_id,
                default_channel="local",
                muted_channels=[],
                created_at=datetime.now(UTC),
                updated_at=datetime.now(UTC),
            )
            session.add(preferences)
            await session.commit()

            logger.info("Created player preferences", player_id=player_id)
            return {"success": True}

        except IntegrityError as e:
            await session.rollback()
            logger.error("Failed to create player preferences - integrity error", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Database integrity error: {str(e)}"}
        except SQLAlchemyError as e:
            await session.rollback()
            logger.error("Failed to create player preferences - database error", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Preference creation errors unpredictable, must rollback
            await session.rollback()
            logger.error("Failed to create player preferences", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Unexpected error: {str(e)}"}

    async def get_player_preferences(self, session: AsyncSession, player_id: uuid.UUID | str) -> dict[str, Any]:
        """
        Get preferences for a player.

        Args:
            session: Database session
            player_id: The player's unique identifier (UUID or string)

        Returns:
            Dictionary with success status and preferences data or error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        # Normalize player_id to UUID object for database operations
        if isinstance(player_id, str):
            player_id = uuid.UUID(player_id)

        try:
            result = await session.execute(
                select(PlayerChannelPreferences).where(PlayerChannelPreferences.player_id == player_id)
            )
            preferences = result.scalar_one_or_none()

            if not preferences:
                return {"success": False, "error": "Player preferences not found"}

            # Convert to dictionary
            prefs_dict = {
                "player_id": preferences.player_id,
                "default_channel": preferences.default_channel,
                "muted_channels": preferences.muted_channels,
                "created_at": preferences.created_at.isoformat() if preferences.created_at else None,
                "updated_at": preferences.updated_at.isoformat() if preferences.updated_at else None,
            }

            return {"success": True, "data": prefs_dict}

        except SQLAlchemyError as e:
            logger.error("Failed to get player preferences", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Preference retrieval errors unpredictable, must handle gracefully
            logger.error("Failed to get player preferences", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Unexpected error: {str(e)}"}

    async def update_default_channel(
        self, session: AsyncSession, player_id: uuid.UUID | str, channel: str
    ) -> dict[str, Any]:
        """
        Update a player's default channel.

        Args:
            session: Database session
            player_id: The player's unique identifier
            channel: The new default channel name

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        # Normalize player_id to UUID object for database operations
        if isinstance(player_id, str):
            player_id = uuid.UUID(player_id)

        if not self._is_valid_channel(channel):
            return {"success": False, "error": "Invalid channel name"}

        try:
            # Check if player preferences exist
            result = await session.execute(
                select(PlayerChannelPreferences).where(PlayerChannelPreferences.player_id == player_id)
            )
            preferences = result.scalar_one_or_none()
            if not preferences:
                return {"success": False, "error": "Player preferences not found"}

            # Update default channel
            preferences.default_channel = channel
            preferences.updated_at = datetime.now(UTC)
            await session.commit()

            logger.info("Updated default channel", player_id=player_id, channel=channel)
            return {"success": True}

        except SQLAlchemyError as e:
            await session.rollback()
            logger.error("Failed to update default channel", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Channel update errors unpredictable, must rollback
            await session.rollback()
            logger.error("Failed to update default channel", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Unexpected error: {str(e)}"}

    async def mute_channel(self, session: AsyncSession, player_id: uuid.UUID | str, channel: str) -> dict[str, Any]:
        """
        Mute a channel for a player.

        Args:
            session: Database session
            player_id: The player's unique identifier
            channel: The channel to mute

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        # Normalize player_id to UUID object for database operations
        if isinstance(player_id, str):
            player_id = uuid.UUID(player_id)

        if not self._is_valid_channel(channel):
            return {"success": False, "error": "Invalid channel name"}

        # System channel cannot be muted
        if channel == "system":
            return {"success": False, "error": "System channel cannot be muted"}

        try:
            # Get current preferences
            result = await session.execute(
                select(PlayerChannelPreferences).where(PlayerChannelPreferences.player_id == player_id)
            )
            preferences = result.scalar_one_or_none()
            if not preferences:
                return {"success": False, "error": "Player preferences not found"}

            # Add channel if not already muted
            if channel not in preferences.muted_channels:
                preferences.muted_channels.append(channel)
                preferences.updated_at = datetime.now(UTC)
                await session.commit()

                logger.info("Muted channel for player", player_id=player_id, channel=channel)

            return {"success": True}

        except SQLAlchemyError as e:
            await session.rollback()
            logger.error("Failed to mute channel", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Channel mute errors unpredictable, must rollback
            await session.rollback()
            logger.error("Failed to mute channel", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Unexpected error: {str(e)}"}

    async def unmute_channel(self, session: AsyncSession, player_id: uuid.UUID | str, channel: str) -> dict[str, Any]:
        """
        Unmute a channel for a player.

        Args:
            session: Database session
            player_id: The player's unique identifier
            channel: The channel to unmute

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        # Normalize player_id to UUID object for database operations
        if isinstance(player_id, str):
            player_id = uuid.UUID(player_id)

        if not self._is_valid_channel(channel):
            return {"success": False, "error": "Invalid channel name"}

        try:
            # Get current preferences
            result = await session.execute(
                select(PlayerChannelPreferences).where(PlayerChannelPreferences.player_id == player_id)
            )
            preferences = result.scalar_one_or_none()
            if not preferences:
                return {"success": False, "error": "Player preferences not found"}

            # Remove channel if muted
            if channel in preferences.muted_channels:
                preferences.muted_channels.remove(channel)
                preferences.updated_at = datetime.now(UTC)
                await session.commit()

                logger.info("Unmuted channel for player", player_id=player_id, channel=channel)

            return {"success": True}

        except SQLAlchemyError as e:
            await session.rollback()
            logger.error("Failed to unmute channel", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Channel unmute errors unpredictable, must rollback
            await session.rollback()
            logger.error("Failed to unmute channel", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Unexpected error: {str(e)}"}

    async def get_muted_channels(self, session: AsyncSession, player_id: uuid.UUID | str) -> dict[str, Any]:
        """
        Get list of muted channels for a player.

        Args:
            session: Database session
            player_id: The player's unique identifier

        Returns:
            Dictionary with success status and list of muted channels or error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        # Normalize player_id to UUID object for database operations
        if isinstance(player_id, str):
            player_id = uuid.UUID(player_id)

        try:
            result = await session.execute(
                select(PlayerChannelPreferences).where(PlayerChannelPreferences.player_id == player_id)
            )
            preferences = result.scalar_one_or_none()
            if not preferences:
                return {"success": False, "error": "Player preferences not found"}

            return {"success": True, "data": preferences.muted_channels}

        except SQLAlchemyError as e:
            logger.error("Failed to get muted channels", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Muted channels retrieval errors unpredictable, must handle gracefully
            logger.error("Failed to get muted channels", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Unexpected error: {str(e)}"}

    async def is_channel_muted(self, session: AsyncSession, player_id: uuid.UUID | str, channel: str) -> dict[str, Any]:
        """
        Check if a specific channel is muted for a player.

        Args:
            session: Database session
            player_id: The player's unique identifier
            channel: The channel to check

        Returns:
            Dictionary with success status and boolean result or error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        # Normalize player_id to UUID object for database operations
        if isinstance(player_id, str):
            player_id = uuid.UUID(player_id)

        if not self._is_valid_channel(channel):
            return {"success": False, "error": "Invalid channel name"}

        try:
            result = await session.execute(
                select(PlayerChannelPreferences).where(PlayerChannelPreferences.player_id == player_id)
            )
            preferences = result.scalar_one_or_none()
            if not preferences:
                return {"success": False, "error": "Player preferences not found"}

            is_muted = channel in preferences.muted_channels

            return {"success": True, "data": is_muted}

        except SQLAlchemyError as e:
            logger.error("Failed to check channel mute status", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Mute status check errors unpredictable, must handle gracefully
            logger.error("Failed to check channel mute status", player_id=player_id, channel=channel, error=str(e))
            return {"success": False, "error": f"Unexpected error: {str(e)}"}

    async def delete_player_preferences(self, session: AsyncSession, player_id: uuid.UUID | str) -> dict[str, Any]:
        """
        Delete preferences for a player.

        Args:
            session: Database session
            player_id: The player's unique identifier

        Returns:
            Dictionary with success status and optional error message
        """
        if not self._is_valid_player_id(player_id):
            return {"success": False, "error": "Invalid player ID"}

        # Normalize player_id to UUID object for database operations
        if isinstance(player_id, str):
            player_id = uuid.UUID(player_id)

        try:
            result = await session.execute(
                select(PlayerChannelPreferences).where(PlayerChannelPreferences.player_id == player_id)
            )
            preferences = result.scalar_one_or_none()

            if not preferences:
                return {"success": False, "error": "Player preferences not found"}

            await session.delete(preferences)
            await session.commit()

            logger.info("Deleted player preferences", player_id=player_id)
            return {"success": True}

        except SQLAlchemyError as e:
            await session.rollback()
            logger.error("Failed to delete player preferences", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Database error: {str(e)}"}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Preference deletion errors unpredictable, must rollback
            await session.rollback()
            logger.error("Failed to delete player preferences", player_id=player_id, error=str(e))
            return {"success": False, "error": f"Unexpected error: {str(e)}"}

    def _is_valid_player_id(self, player_id: uuid.UUID | str) -> bool:
        """
        Validate player ID.

        Args:
            player_id: The player ID to validate (UUID or string)

        Returns:
            True if valid, False otherwise
        """
        if not player_id:
            return False

        # Accept both UUID objects and UUID strings
        if isinstance(player_id, uuid.UUID):
            return True

        if isinstance(player_id, str):
            # Try to parse as UUID
            try:
                uuid.UUID(player_id)
                return True
            except (ValueError, AttributeError, TypeError):
                return False

        # Type signature guarantees player_id is uuid.UUID | str, so all cases are handled above
        # This line is unreachable but kept for defensive programming
        return False  # type: ignore[unreachable]  # Reason: Type signature guarantees all cases are handled, this line is unreachable but kept for defensive programming

    def _is_valid_channel(self, channel: str) -> bool:
        """
        Validate channel name.

        Args:
            channel: The channel name to validate

        Returns:
            True if valid, False otherwise
        """
        if not channel or not isinstance(channel, str):
            return False

        return channel in self._valid_channels

    def _is_valid_json_array(self, json_str: str) -> bool:
        """
        Validate that a string is a valid JSON array.

        Args:
            json_str: The JSON string to validate

        Returns:
            True if valid JSON array, False otherwise
        """
        if not json_str or not isinstance(json_str, str):
            return False

        try:
            parsed = json.loads(json_str)
            return isinstance(parsed, list)
        except (json.JSONDecodeError, TypeError):
            return False
