"""
Chat moderation utilities.

This module provides moderation functionality including muting,
admin management, and mute status reporting.
"""

import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from typing import Protocol

    class PlayerServiceProtocol(Protocol):
        """Protocol for player service."""

        async def get_player_by_id(self, player_id: str | uuid.UUID) -> Any:
            """Get player by ID."""

        async def resolve_player_name(self, player_name: str) -> Any:
            """Resolve player name to player object."""

    class UserManagerProtocol(Protocol):
        """Protocol for user manager."""

        def mute_channel(self, player_id: str, player_name: str, channel: str) -> bool:
            """Mute a channel for a player."""

        def unmute_channel(self, player_id: str, player_name: str, channel: str) -> bool:
            """Unmute a channel for a player."""

        def is_channel_muted(self, player_id: str, channel: str) -> bool:
            """Check if channel is muted."""

        def mute_player(self, muter_id: str, muter_name: str, target_id: str, target_name: str) -> bool:
            """Mute a player for another player."""

        def unmute_player(self, muter_id: str, muter_name: str, target_id: str, target_name: str) -> bool:
            """Unmute a player for another player."""

        def is_player_muted(self, muter_id: str, target_id: str) -> bool:
            """Check if player is muted."""

        def mute_global(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Mute operations require many parameters for context and validation
            self,
            muter_id: str,
            muter_name: str,
            target_id: str,
            target_name: str,
            duration_minutes: int | None,
            reason: str,
        ) -> bool:
            """Apply global mute."""

        def unmute_global(self, unmuter_id: str, unmuter_name: str, target_id: str, target_name: str) -> bool:
            """Remove global mute."""

        def is_globally_muted(self, player_id: str) -> bool:
            """Check if player is globally muted."""

        def add_admin(self, player_id: str, player_name: str) -> None:
            """Add admin."""

        def remove_admin(self, player_id: str, player_name: str) -> None:
            """Remove admin."""

        def is_admin(self, player_id: str) -> bool:
            """Check if player is admin."""

        def can_send_message(self, sender_id: str, target_id: str | None, channel: str | None) -> bool:
            """Check if player can send message."""

        def get_player_mutes(self, player_id: str) -> dict[str, Any]:
            """Get player mutes."""

        def get_system_stats(self) -> dict[str, Any]:
            """Get system stats."""

        def load_player_mutes(self, player_id: str) -> None:
            """Load player mutes."""


logger = get_logger("communications.chat_moderation")


def normalize_player_id(player_id: uuid.UUID | str) -> str:
    """Normalize player identifiers to string form."""
    return str(player_id)


class ChatModeration:
    """Handles chat moderation operations."""

    def __init__(self, player_service: "PlayerServiceProtocol", user_manager: "UserManagerProtocol") -> None:
        """
        Initialize moderation handler.

        Args:
            player_service: Player service for player lookups
            user_manager: User manager for mute/admin operations
        """
        self.player_service = player_service
        self.user_manager = user_manager

    async def mute_channel(self, player_id: uuid.UUID | str, channel: str) -> bool:
        """Mute a specific channel for a player."""
        player_id_str = normalize_player_id(player_id)

        # Get player name for logging
        player = await self.player_service.get_player_by_id(player_id_str)
        player_name = player.name if player else player_id_str

        success = self.user_manager.mute_channel(player_id_str, player_name, channel)
        if success:
            logger.info("Player muted channel", player_id=player_id_str, channel=channel)
        return bool(success)

    async def unmute_channel(self, player_id: uuid.UUID | str, channel: str) -> bool:
        """Unmute a specific channel for a player."""
        player_id_str = normalize_player_id(player_id)

        # Get player name for logging
        player = await self.player_service.get_player_by_id(player_id_str)
        player_name = player.name if player else player_id_str

        success = self.user_manager.unmute_channel(player_id_str, player_name, channel)
        if success:
            logger.info("Player unmuted channel", player_id=player_id_str, channel=channel)
        return bool(success)

    def is_channel_muted(self, player_id: uuid.UUID | str, channel: str) -> bool:
        """Check if a channel is muted for a player."""
        player_id_str = normalize_player_id(player_id)
        return bool(self.user_manager.is_channel_muted(player_id_str, channel))

    async def mute_player(self, muter_id: uuid.UUID | str, target_player_name: str) -> bool:
        """Mute a specific player for another player."""
        # Get muter name for logging
        muter_id_str = normalize_player_id(muter_id)
        muter = await self.player_service.get_player_by_id(muter_id_str)
        muter_name = muter.name if muter else muter_id_str

        # Resolve target player name to ID
        target_player = await self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        target_id_str = normalize_player_id(target_player.id)

        success = self.user_manager.mute_player(muter_id_str, muter_name, target_id_str, target_player_name)
        if success:
            logger.info("Player muted another player", muter_id=muter_id_str, target=target_player_name)
        return bool(success)

    async def unmute_player(self, muter_id: uuid.UUID | str, target_player_name: str) -> bool:
        """Unmute a specific player for another player."""
        # Get muter name for logging
        muter_id_str = normalize_player_id(muter_id)
        muter = await self.player_service.get_player_by_id(muter_id_str)
        muter_name = muter.name if muter else muter_id_str

        # Resolve target player name to ID
        target_player = await self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        target_id_str = normalize_player_id(target_player.id)

        success = self.user_manager.unmute_player(muter_id_str, muter_name, target_id_str, target_player_name)
        if success:
            logger.info("Player unmuted another player", muter_id=muter_id_str, target=target_player_name)
        return bool(success)

    def is_player_muted(self, muter_id: uuid.UUID | str, target_player_id: uuid.UUID | str) -> bool:
        """Check if a player is muted by another player."""
        muter_id_str = normalize_player_id(muter_id)
        target_id_str = normalize_player_id(target_player_id)
        return bool(self.user_manager.is_player_muted(muter_id_str, target_id_str))

    async def mute_global(
        self, muter_id: uuid.UUID | str, target_player_name: str, duration_minutes: int | None = None, reason: str = ""
    ) -> bool:
        """Apply a global mute to a player (cannot use any chat channels)."""
        # Get muter name for logging
        muter_id_str = normalize_player_id(muter_id)
        muter = await self.player_service.get_player_by_id(muter_id_str)
        muter_name = muter.name if muter else muter_id_str

        # Resolve target player name to ID
        target_player = await self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        target_id_str = normalize_player_id(target_player.id)

        success = self.user_manager.mute_global(
            muter_id_str, muter_name, target_id_str, target_player_name, duration_minutes, reason
        )
        if success:
            logger.info(
                "Player globally muted", muter_id=muter_id_str, target=target_player_name, duration=duration_minutes
            )
        return bool(success)

    async def unmute_global(self, unmuter_id: uuid.UUID | str, target_player_name: str) -> bool:
        """Remove a global mute from a player."""
        # Get unmuter name for logging
        unmuter_id_str = normalize_player_id(unmuter_id)
        unmuter = await self.player_service.get_player_by_id(unmuter_id_str)
        unmuter_name = unmuter.name if unmuter else unmuter_id_str

        # Resolve target player name to ID
        target_player = await self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        target_id_str = normalize_player_id(target_player.id)

        success = self.user_manager.unmute_global(unmuter_id_str, unmuter_name, target_id_str, target_player_name)
        if success:
            logger.info("Player globally unmuted", unmuter_id=unmuter_id_str, target=target_player_name)
        return bool(success)

    def is_globally_muted(self, player_id: uuid.UUID | str) -> bool:
        """Check if a player is globally muted."""
        player_id_str = normalize_player_id(player_id)
        return bool(self.user_manager.is_globally_muted(player_id_str))

    async def add_admin(self, player_id: uuid.UUID | str) -> bool:
        """Add a player as an admin."""
        player_id_str = normalize_player_id(player_id)
        player = await self.player_service.get_player_by_id(player_id_str)
        player_name = player.name if player else player_id_str

        self.user_manager.add_admin(player_id_str, player_name)
        logger.info("Player added as admin", player_id=player_id, player_name=player_name)
        return True

    async def remove_admin(self, player_id: uuid.UUID | str) -> bool:
        """Remove a player's admin status."""
        player_id_str = normalize_player_id(player_id)
        player = await self.player_service.get_player_by_id(player_id_str)
        player_name = player.name if player else player_id_str

        self.user_manager.remove_admin(player_id_str, player_name)
        logger.info("Player admin status removed", player_id=player_id, player_name=player_name)
        return True

    def is_admin(self, player_id: uuid.UUID | str) -> bool:
        """Check if a player is an admin."""
        player_id_str = normalize_player_id(player_id)
        return bool(self.user_manager.is_admin(player_id_str))

    def can_send_message(self, sender_id: str, target_id: str | None = None, channel: str | None = None) -> bool:
        """Check if a player can send a message."""
        return bool(self.user_manager.can_send_message(sender_id, target_id, channel))

    def get_player_mutes(self, player_id: uuid.UUID | str) -> dict[str, Any]:
        """Get all mutes applied by a player."""
        player_id_str = normalize_player_id(player_id)
        return self.user_manager.get_player_mutes(player_id_str)

    def get_user_management_stats(self) -> dict[str, Any]:
        """Get user management system statistics."""
        return self.user_manager.get_system_stats()

    def _format_mute_duration(self, expires_at: str | datetime | None) -> str:
        """Format mute duration text with remaining time or expiration status."""
        if not expires_at:
            return " (PERMANENT)"

        try:
            if isinstance(expires_at, str):
                expires_dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
            else:
                expires_dt = expires_at

            now = datetime.now(UTC)
            if expires_dt.tzinfo is None:
                expires_dt = expires_dt.replace(tzinfo=UTC)

            remaining = expires_dt - now
            if remaining.total_seconds() > 0:
                minutes_left = int(remaining.total_seconds() / 60)
                return f" ({minutes_left} minutes remaining)"
            return " (EXPIRED)"
        except (ValueError, TypeError, AttributeError) as e:
            logger.debug("Error calculating mute duration", error=str(e), error_type=type(e).__name__)
            return ""

    def _format_mute_entry(self, mute_data: dict[str, Any]) -> str:
        """Format a single mute entry for display."""
        target_name = mute_data.get("target_name", "Unknown")
        expires_at = mute_data.get("expires_at")
        reason = mute_data.get("reason", "")

        duration_text = self._format_mute_duration(expires_at)
        reason_text = f" - {reason}" if reason else ""
        return f"  • {target_name}{duration_text}{reason_text}"

    def _format_mute_section(self, section_title: str, mutes: dict[str, Any], empty_message: str) -> list[str]:
        """Format a section of mutes (personal or global) for display."""
        status_lines = []
        if mutes:
            status_lines.append(section_title)
            for _target_id, mute_data in mutes.items():
                status_lines.append(self._format_mute_entry(mute_data))
        else:
            status_lines.append(empty_message)
        return status_lines

    async def get_mute_status(self, player_id: uuid.UUID | str) -> str:
        """
        Get comprehensive mute status for a player.

        Args:
            player_id: Player ID to get mute status for

        Returns:
            Formatted string with mute status information
        """
        try:
            # Convert player_id to UUID if it's a string
            if isinstance(player_id, str):
                try:
                    player_id_uuid = uuid.UUID(player_id)
                except (ValueError, AttributeError):
                    logger.error("Invalid player_id format", player_id=player_id)
                    return "Invalid player ID format."
            else:
                player_id_uuid = player_id

            # Get player name (player_service accepts UUID)
            player = await self.player_service.get_player_by_id(player_id_uuid)
            if not player:
                return "Player not found."

            player_name = player.name

            # Convert to string for user_manager methods (they expect strings)
            player_id_str = str(player_id_uuid)

            # Load player's mute data first
            self.user_manager.load_player_mutes(player_id_str)

            # Get mute information from UserManager
            mute_info = self.user_manager.get_player_mutes(player_id_str)

            # Check if player is admin
            is_admin = self.user_manager.is_admin(player_id_str)

            # Build status report
            status_lines = []
            status_lines.append(f"=== MUTE STATUS FOR {player_name.upper()} ===")

            if is_admin:
                status_lines.append("🔴 ADMIN STATUS: You are an admin (immune to all mutes)")

            status_lines.append("")

            # Personal mutes (players you have muted)
            personal_mutes = mute_info.get("player_mutes", {})
            status_lines.extend(
                self._format_mute_section(
                    "🔇 PLAYERS YOU HAVE MUTED:", personal_mutes, "🔇 PLAYERS YOU HAVE MUTED: None"
                )
            )

            status_lines.append("")

            # Global mutes (players you have globally muted)
            global_mutes = mute_info.get("global_mutes", {})
            status_lines.extend(
                self._format_mute_section(
                    "🌐 PLAYERS YOU HAVE GLOBALLY MUTED:", global_mutes, "🌐 PLAYERS YOU HAVE GLOBALLY MUTED: None"
                )
            )

            status_lines.append("")

            # Note: We do not show if you are muted by others to prevent retaliation
            # This information is kept private for the protection of players who mute others

            return "\n".join(status_lines)

        except (AttributeError, TypeError, ValueError, KeyError, RuntimeError) as e:
            # Handle attribute access errors, type mismatches, value errors, key errors, or runtime issues
            logger.error("Error getting mute status", error=str(e), player_id=player_id)
            return "Error retrieving mute status."
