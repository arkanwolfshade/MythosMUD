"""
Channel Broadcasting Strategies for NATS Message Handler.

This module implements the Strategy pattern for handling different channel types
in the NATS message handler, replacing the if/elif chain with a more maintainable
and extensible approach. As noted in the restricted archives, this pattern provides
O(1) lookup and eliminates the need for repetitive conditional logic.
"""

import uuid
from abc import ABC, abstractmethod

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ChannelBroadcastingStrategy(ABC):
    """Abstract base class for channel broadcasting strategies."""

    @abstractmethod
    async def broadcast(
        self,
        chat_event: dict,
        room_id: str,
        party_id: str,
        target_player_id: uuid.UUID | None,
        sender_id: uuid.UUID,
        nats_handler,
    ) -> None:
        """
        Broadcast message according to channel strategy.

        Args:
            chat_event: WebSocket event to broadcast
            room_id: Room ID for room-based channels
            party_id: Party ID for party-based channels
            target_player_id: Target player ID for whisper messages (UUID or None)
            sender_id: Sender player ID (UUID)
            nats_handler: NATS message handler instance
        """
        pass


class RoomBasedChannelStrategy(ChannelBroadcastingStrategy):
    """Strategy for room-based channels (say, local, emote, pose)."""

    def __init__(self, channel_type: str):
        """
        Initialize room-based channel strategy.

        Args:
            channel_type: Type of room-based channel (say, local, emote, pose)
        """
        self.channel_type = channel_type

    async def broadcast(
        self,
        chat_event: dict,
        room_id: str,
        party_id: str,
        target_player_id: uuid.UUID | None,
        sender_id: uuid.UUID,
        nats_handler,
    ) -> None:
        """Broadcast room-based message with server-side filtering."""
        if room_id:
            # Convert UUID to string for _broadcast_to_room_with_filtering which expects string
            sender_id_str = str(sender_id)
            await nats_handler._broadcast_to_room_with_filtering(room_id, chat_event, sender_id_str, self.channel_type)
            logger.debug(
                "Broadcasted room message with server-side filtering",
                channel=self.channel_type,
                room_id=room_id,
                sender_id=sender_id,
            )
        else:
            logger.warning("Room-based message missing room_id")


class GlobalChannelStrategy(ChannelBroadcastingStrategy):
    """Strategy for global channel broadcasting."""

    async def broadcast(
        self,
        chat_event: dict,
        room_id: str,
        party_id: str,
        target_player_id: uuid.UUID | None,
        sender_id: uuid.UUID,
        nats_handler,
    ) -> None:
        """Broadcast global message to all connected players."""
        # AI Agent: Use connection_manager from nats_handler (injected dependency)
        # Convert UUID to string for broadcast_global which expects string
        sender_id_str = str(sender_id)
        await nats_handler.connection_manager.broadcast_global(chat_event, exclude_player=sender_id_str)
        logger.debug("Broadcasted global message", sender_id=sender_id)


class PartyChannelStrategy(ChannelBroadcastingStrategy):
    """Strategy for party channel broadcasting."""

    async def broadcast(
        self,
        chat_event: dict,
        room_id: str,
        party_id: str,
        target_player_id: uuid.UUID | None,
        sender_id: uuid.UUID,
        nats_handler,
    ) -> None:
        """Broadcast party message to party members."""
        if party_id:
            # TODO: Implement party-based broadcasting when party system is available
            logger.debug("Party message received")
        else:
            logger.warning("Party message missing party_id")


class WhisperChannelStrategy(ChannelBroadcastingStrategy):
    """Strategy for whisper channel broadcasting."""

    async def broadcast(
        self,
        chat_event: dict,
        room_id: str,
        party_id: str,
        target_player_id: uuid.UUID | None,
        sender_id: uuid.UUID,
        nats_handler,
    ) -> None:
        """Send whisper message to specific player."""
        if target_player_id:
            # AI Agent: Use connection_manager from nats_handler (injected dependency)
            await nats_handler.connection_manager.send_personal_message(target_player_id, chat_event)
            logger.debug(
                "Sent whisper message",
                sender_id=sender_id,
                target_player_id=target_player_id,
            )
        else:
            logger.warning("Whisper message missing target_player_id")


class SystemAdminChannelStrategy(ChannelBroadcastingStrategy):
    """Strategy for system/admin channel broadcasting."""

    def __init__(self, channel_type: str):
        """
        Initialize system/admin channel strategy.

        Args:
            channel_type: Type of system/admin channel (system, admin)
        """
        self.channel_type = channel_type

    async def broadcast(
        self,
        chat_event: dict,
        room_id: str,
        party_id: str,
        target_player_id: uuid.UUID | None,
        sender_id: uuid.UUID,
        nats_handler,
    ) -> None:
        """Broadcast system/admin message to all players."""
        # AI Agent: Use connection_manager from nats_handler (injected dependency)
        # Convert UUID to string for broadcast_global which expects string
        sender_id_str = str(sender_id)
        await nats_handler.connection_manager.broadcast_global(chat_event, exclude_player=sender_id_str)
        logger.debug("Broadcasted message", channel_type=self.channel_type, sender_id=sender_id)


class UnknownChannelStrategy(ChannelBroadcastingStrategy):
    """Strategy for unknown channel types."""

    def __init__(self, channel_type: str):
        """
        Initialize unknown channel strategy.

        Args:
            channel_type: Unknown channel type
        """
        self.channel_type = channel_type

    async def broadcast(
        self,
        chat_event: dict,
        room_id: str,
        party_id: str,
        target_player_id: uuid.UUID | None,
        sender_id: uuid.UUID,
        nats_handler,
    ) -> None:
        """Handle unknown channel type."""
        logger.warning("Unknown channel type")


class ChannelBroadcastingStrategyFactory:
    """Factory for creating channel broadcasting strategies."""

    def __init__(self):
        """Initialize the strategy factory."""
        # Pre-create strategies for known channel types
        self._strategies = {
            # Room-based channels
            "say": RoomBasedChannelStrategy("say"),
            "local": RoomBasedChannelStrategy("local"),
            "emote": RoomBasedChannelStrategy("emote"),
            "pose": RoomBasedChannelStrategy("pose"),
            # Global channel
            "global": GlobalChannelStrategy(),
            # Party channel
            "party": PartyChannelStrategy(),
            # Whisper channel
            "whisper": WhisperChannelStrategy(),
            # System/Admin channels
            "system": SystemAdminChannelStrategy("system"),
            "admin": SystemAdminChannelStrategy("admin"),
        }

    def get_strategy(self, channel_type: str) -> ChannelBroadcastingStrategy:
        """
        Get strategy for channel type.

        Args:
            channel_type: Type of channel to get strategy for

        Returns:
            ChannelBroadcastingStrategy: Strategy for the channel type
        """
        return self._strategies.get(channel_type, UnknownChannelStrategy(channel_type))

    def register_strategy(self, channel_type: str, strategy: ChannelBroadcastingStrategy) -> None:
        """
        Register a new strategy for a channel type.

        Args:
            channel_type: Channel type to register strategy for
            strategy: Strategy to register
        """
        self._strategies[channel_type] = strategy
        logger.info("Registered strategy for channel type", channel_type=channel_type)


# Global strategy factory instance
channel_strategy_factory = ChannelBroadcastingStrategyFactory()
