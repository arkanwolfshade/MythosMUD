"""
NPC Communication Integration for MythosMUD.

This module provides integration between NPCs and the existing chat/whisper
systems, allowing NPCs to participate in conversations, respond to messages,
and interact with players through the game's communication channels.

As documented in the Cultes des Goules, proper communication integration is
essential for maintaining the illusion of sentient entities within our
eldritch digital realm.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..events import EventBus
from ..events.event_types import NPCListened, NPCSpoke
from ..structured_logging.enhanced_logging_config import get_logger

# Removed: from ..persistence import get_persistence - no longer needed

# Import ChatService only for type checking to avoid circular dependency
# AI: ChatService is only needed for type annotations, not runtime
if TYPE_CHECKING:
    from ..game.chat_service import ChatService

logger = get_logger(__name__)


class NPCCommunicationIntegration:
    """
    Integrates NPCs with the existing chat and whisper systems.

    This class provides methods for NPCs to participate in conversations,
    respond to messages, and interact with players through various
    communication channels.
    """

    def __init__(self, event_bus: EventBus | None = None, chat_service: ChatService | None = None):
        """
        Initialize the NPC communication integration.

        Args:
            event_bus: Optional EventBus instance. If None, will get the global
                instance.
            chat_service: Optional ChatService instance for direct integration.
        """
        self.event_bus = event_bus or EventBus()
        # Removed: self._persistence = get_persistence(event_bus) - no longer needed
        self._chat_service = chat_service
        logger.debug("NPC communication integration initialized")

    def send_message_to_room(self, npc_id: str, room_id: str, message: str, channel: str = "local") -> bool:
        """
        Send a message from an NPC to a room.

        Args:
            npc_id: ID of the NPC sending the message
            room_id: ID of the room to send the message to
            message: Message content
            channel: Communication channel (local, say, shout, etc.)

        Returns:
            bool: True if message was sent successfully
        """
        try:
            # Publish NPC spoke event
            if self.event_bus:
                self.event_bus.publish(
                    NPCSpoke(
                        npc_id=npc_id,
                        room_id=room_id,
                        message=message,
                        channel=channel,
                    )
                )

            # Direct ChatService dispatch is not used for NPCs; events drive distribution

            logger.info("NPC sent message to room", npc_id=npc_id, room_id=room_id, message=message, channel=channel)
            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC communication errors unpredictable, must return False
            logger.error("Error sending NPC message to room", npc_id=npc_id, room_id=room_id, error=str(e))
            return False

    def send_whisper_to_player(self, npc_id: str, target_player_id: str, message: str, room_id: str) -> bool:
        """
        Send a whisper from an NPC to a specific player.

        Args:
            npc_id: ID of the NPC sending the whisper
            target_player_id: ID of the target player
            message: Whisper content
            room_id: ID of the room where the whisper occurs

        Returns:
            bool: True if whisper was sent successfully
        """
        try:
            # Publish NPC spoke event with target
            if self.event_bus:
                self.event_bus.publish(
                    NPCSpoke(
                        npc_id=npc_id,
                        room_id=room_id,
                        message=message,
                        channel="whisper",
                        target_id=target_player_id,
                    )
                )

            # Direct ChatService dispatch is not used for NPCs; events drive distribution

            logger.info(
                "NPC sent whisper to player",
                npc_id=npc_id,
                target_player_id=target_player_id,
                message=message,
                room_id=room_id,
            )
            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC whisper errors unpredictable, must return False
            logger.error(
                "Error sending NPC whisper to player", npc_id=npc_id, target_player_id=target_player_id, error=str(e)
            )
            return False

    def handle_player_message(
        self, npc_id: str, player_id: str, message: str, room_id: str, channel: str = "local"
    ) -> bool:
        """
        Handle a message received by an NPC from a player.

        Args:
            npc_id: ID of the NPC receiving the message
            player_id: ID of the player who sent the message
            message: Message content
            room_id: ID of the room where the message was sent
            channel: Communication channel

        Returns:
            bool: True if message was handled successfully
        """
        try:
            # Publish NPC listened event
            if self.event_bus:
                self.event_bus.publish(
                    NPCListened(
                        npc_id=npc_id,
                        room_id=room_id,
                        message=message,
                        speaker_id=player_id,
                        channel=channel,
                    )
                )

            # Here you could add logic to trigger NPC responses based on the message
            # For example, keyword detection, sentiment analysis, etc.
            self._process_message_for_response(npc_id, message, room_id, channel)

            logger.debug(
                "NPC handled player message", npc_id=npc_id, player_id=player_id, message=message, channel=channel
            )
            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC message handling errors unpredictable, must return False
            logger.error("Error handling player message for NPC", npc_id=npc_id, player_id=player_id, error=str(e))
            return False

    def _process_message_for_response(self, npc_id: str, message: str, room_id: str, channel: str) -> None:
        """
        Process a message to determine if the NPC should respond.

        Args:
            npc_id: ID of the NPC
            message: Message content
            room_id: ID of the room
            channel: Communication channel
        """
        try:
            # Simple keyword-based response system
            message_lower = message.lower()

            # Greeting responses
            if any(greeting in message_lower for greeting in ["hello", "hi", "hey", "greetings"]):
                self.send_message_to_room(npc_id, room_id, "Hello there, traveler!", channel)

            # Question responses
            elif "?" in message:
                self.send_message_to_room(npc_id, room_id, "That's an interesting question...", channel)

            # Help requests
            elif any(help_word in message_lower for help_word in ["help", "assist", "aid"]):
                self.send_message_to_room(npc_id, room_id, "I'd be happy to help if I can.", channel)

            # Thank you responses
            elif any(thanks in message_lower for thanks in ["thank", "thanks", "appreciate"]):
                self.send_message_to_room(npc_id, room_id, "You're welcome!", channel)

            # Default response for other messages
            elif len(message.strip()) > 0:
                # Only respond to non-empty messages
                responses = [
                    "I see...",
                    "Interesting.",
                    "Hmm, I understand.",
                    "That's quite something.",
                    "I'll keep that in mind.",
                ]
                import random

                response = random.choice(responses)  # nosec B311: Game mechanics NPC response selection, not cryptographic
                self.send_message_to_room(npc_id, room_id, response, channel)

        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC message processing errors unpredictable, must handle gracefully
            logger.error("Error processing message for response", npc_id=npc_id, error=str(e))

    def subscribe_to_room_messages(self, npc_id: str, room_id: str) -> bool:
        """
        Subscribe an NPC to messages in a specific room.

        Args:
            npc_id: ID of the NPC to subscribe
            room_id: ID of the room to listen to

        Returns:
            bool: True if subscription was successful
        """
        try:
            # This would integrate with the chat service to receive messages
            # For now, this is a placeholder for future implementation
            logger.debug("NPC subscribed to room messages", npc_id=npc_id, room_id=room_id)
            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC subscription errors unpredictable, must return False
            logger.error("Error subscribing NPC to room messages", npc_id=npc_id, room_id=room_id, error=str(e))
            return False

    def unsubscribe_from_room_messages(self, npc_id: str, room_id: str) -> bool:
        """
        Unsubscribe an NPC from messages in a specific room.

        Args:
            npc_id: ID of the NPC to unsubscribe
            room_id: ID of the room to stop listening to

        Returns:
            bool: True if unsubscription was successful
        """
        try:
            # This would integrate with the chat service to stop receiving messages
            # For now, this is a placeholder for future implementation
            logger.debug("NPC unsubscribed from room messages", npc_id=npc_id, room_id=room_id)
            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NPC unsubscription errors unpredictable, must return False
            logger.error("Error unsubscribing NPC from room messages", npc_id=npc_id, room_id=room_id, error=str(e))
            return False
