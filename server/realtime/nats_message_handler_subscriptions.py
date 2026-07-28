"""Room/subzone/event subscription mixin for NATSMessageHandler.

Extracted to keep nats_message_handler.py under the Lizard file-nloc limit.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from ..services.nats_exceptions import NATSError
from ..structured_logging.enhanced_logging_config import get_logger
from .nats_message_handler_base import NATSMessageHandlerMixinBase

logger = get_logger("communications.nats_message_handler")


class NATSMessageSubscriptionMixin(NATSMessageHandlerMixinBase):
    """Mixin: room, subzone, and event NATS subscription lifecycle."""

    async def subscribe_to_room(self, room_id: str) -> None:
        """
        Subscribe to chat messages for a specific room.

        Args:
            room_id: Room ID to subscribe to

        Raises:
            RuntimeError: If subject manager is not available

        AI: Uses subject manager to build standardized subscription subjects.
            Subject manager is required - no legacy fallback.
        """
        if not self.subject_manager:
            raise RuntimeError("NATSSubjectManager is required for room subscriptions")

        # Build subjects using standardized patterns
        subjects = [
            self.subject_manager.build_subject("chat_say_room", room_id=room_id),
        ]

        for subject in subjects:
            if subject not in self.subscriptions:
                await self._subscribe_to_subject(subject)

    async def unsubscribe_from_room(self, room_id: str) -> None:
        """
        Unsubscribe from chat messages for a specific room.

        Args:
            room_id: Room ID to unsubscribe from

        Raises:
            RuntimeError: If subject manager is not available

        AI: Uses subject manager to build standardized unsubscription subjects.
            Subject manager is required - no legacy fallback.
        """
        if not self.subject_manager:
            raise RuntimeError("NATSSubjectManager is required for room unsubscriptions")

        # Build subjects using standardized patterns
        subjects = [
            self.subject_manager.build_subject("chat_say_room", room_id=room_id),
        ]

        for subject in subjects:
            if subject in self.subscriptions:
                await self._unsubscribe_from_subject(subject)

    def get_subscription_count(self) -> int:
        """Get the number of active subscriptions."""
        return len(self.subscriptions)

    def get_active_subjects(self) -> list[str]:
        """Get list of active subscription subjects."""
        return list(self.subscriptions.keys())

    async def subscribe_to_subzone(self, subzone: str) -> bool:
        """
        Subscribe to local channel messages for a specific sub-zone.

        Args:
            subzone: Sub-zone name to subscribe to

        Returns:
            True if subscribed successfully, False otherwise
        """
        try:
            # Build subject using standardized pattern - subject manager required
            if not self.subject_manager:
                raise RuntimeError("NATSSubjectManager is required for subzone subscriptions")
            subzone_subject = self.subject_manager.build_subject("chat_local_subzone", subzone=subzone)

            # Check if already subscribed
            if subzone_subject in self.subscriptions:
                self.subzone_subscriptions[subzone] = self.subzone_subscriptions.get(subzone, 0) + 1
                logger.debug(
                    "Sub-zone subscription count increased", subzone=subzone, count=self.subzone_subscriptions[subzone]
                )
                return True

            # Subscribe to sub-zone subject
            success = await self._subscribe_to_subject(subzone_subject)
            if success:
                self.subzone_subscriptions[subzone] = 1
                logger.info("Subscribed to sub-zone local channel", subzone=subzone, subject=subzone_subject)
                return True
            logger.error("Failed to subscribe to sub-zone local channel", subzone=subzone, subject=subzone_subject)
            return False

        except NATSError as e:
            logger.error("Error subscribing to sub-zone local channel", error=str(e), subzone=subzone)
            return False

    async def unsubscribe_from_subzone(self, subzone: str) -> bool:
        """
        Unsubscribe from local channel messages for a specific sub-zone.

        Args:
            subzone: Sub-zone name to unsubscribe from

        Returns:
            True if unsubscribed successfully, False otherwise
        """
        try:
            # Build subject using standardized pattern - subject manager required
            if not self.subject_manager:
                raise RuntimeError("NATSSubjectManager is required for subzone unsubscriptions")
            subzone_subject = self.subject_manager.build_subject("chat_local_subzone", subzone=subzone)

            # Decrease subscription count
            if subzone in self.subzone_subscriptions:
                self.subzone_subscriptions[subzone] -= 1
                count = self.subzone_subscriptions[subzone]

                if count <= 0:
                    # No more subscribers, unsubscribe from NATS
                    success = await self._unsubscribe_from_subject(subzone_subject)
                    if success:
                        del self.subzone_subscriptions[subzone]
                        logger.info(
                            "Unsubscribed from sub-zone local channel", subzone=subzone, subject=subzone_subject
                        )
                        return True
                    logger.error(
                        "Failed to unsubscribe from sub-zone local channel",
                        subzone=subzone,
                        subject=subzone_subject,
                    )
                    return False
                logger.debug("Sub-zone subscription count decreased", subzone=subzone, count=count)
                return True
            logger.warning("Not subscribed to sub-zone local channel", subzone=subzone)
            return False

        except NATSError as e:
            logger.error("Error unsubscribing from sub-zone local channel", error=str(e), subzone=subzone)
            return False

    def track_player_subzone_subscription(self, player_id: str, subzone: str) -> None:
        """
        Track a player's sub-zone subscription for local channels.

        Args:
            player_id: Player ID
            subzone: Sub-zone name
        """
        try:
            # Update player's sub-zone subscription
            old_subzone = self.player_subzone_subscriptions.get(player_id)
            if old_subzone and old_subzone != subzone:
                # Player moved to different sub-zone, decrease count for old sub-zone
                if old_subzone in self.subzone_subscriptions:
                    self.subzone_subscriptions[old_subzone] = max(0, self.subzone_subscriptions[old_subzone] - 1)
                    logger.debug(
                        "Player moved to different sub-zone",
                        player_id=player_id,
                        old_subzone=old_subzone,
                        new_subzone=subzone,
                    )

            self.player_subzone_subscriptions[player_id] = subzone
            logger.debug("Tracked player sub-zone subscription", player_id=player_id, subzone=subzone)

        except NATSError as e:
            logger.error(
                "Error tracking player sub-zone subscription", error=str(e), player_id=player_id, subzone=subzone
            )

    def get_players_in_subzone(self, subzone: str) -> list[str]:
        """
        Get list of players currently in a specific sub-zone.

        Args:
            subzone: Sub-zone name

        Returns:
            List of player IDs in the sub-zone
        """
        try:
            players = []
            for player_id, player_subzone in self.player_subzone_subscriptions.items():
                if player_subzone == subzone:
                    players.append(player_id)
            return players

        except NATSError as e:
            logger.error("Error getting players in sub-zone", error=str(e), subzone=subzone)
            return []

    async def handle_player_movement(self, player_id: str, old_room_id: str, new_room_id: str) -> None:
        """
        Handle player movement between rooms and update sub-zone subscriptions.

        Args:
            player_id: Player ID
            old_room_id: Previous room ID
            new_room_id: New room ID
        """
        try:
            from ..utils.room_utils import extract_subzone_from_room_id

            old_subzone = extract_subzone_from_room_id(old_room_id) if old_room_id else None
            new_subzone = extract_subzone_from_room_id(new_room_id) if new_room_id else None

            if old_subzone != new_subzone:
                # Player moved to different sub-zone
                if old_subzone:
                    await self.unsubscribe_from_subzone(old_subzone)

                if new_subzone:
                    await self.subscribe_to_subzone(new_subzone)
                    self.track_player_subzone_subscription(player_id, new_subzone)

                logger.info(
                    "Player moved between sub-zones",
                    player_id=player_id,
                    old_subzone=old_subzone,
                    new_subzone=new_subzone,
                    old_room_id=old_room_id,
                    new_room_id=new_room_id,
                )
            else:
                # Player moved within same sub-zone, just update tracking
                if new_subzone:
                    self.track_player_subzone_subscription(player_id, new_subzone)

        except NATSError as e:
            logger.error(
                "Error handling player movement",
                error=str(e),
                player_id=player_id,
                old_room_id=old_room_id,
                new_room_id=new_room_id,
            )

    async def cleanup_empty_subzone_subscriptions(self) -> None:
        """Clean up sub-zone subscriptions that have no active players."""
        try:
            subzones_to_cleanup = []

            for subzone, count in self.subzone_subscriptions.items():
                players_in_subzone = self.get_players_in_subzone(subzone)
                if not players_in_subzone and count <= 0:
                    subzones_to_cleanup.append(subzone)

            for subzone in subzones_to_cleanup:
                await self.unsubscribe_from_subzone(subzone)
                logger.info("Cleaned up empty sub-zone subscription", subzone=subzone)

        except NATSError as e:
            logger.error("Error cleaning up empty sub-zone subscriptions", error=str(e))

    # Event subscription methods
    async def subscribe_to_event_subjects(self) -> bool:
        """
        Subscribe to all event-related NATS subjects using standardized patterns.

        Raises:
            RuntimeError: If subject manager is not available

        AI: Uses subject manager to generate event subscription patterns dynamically.
            Subject manager is required - no legacy fallback.
        """
        if not self.subject_manager:
            raise RuntimeError("NATSSubjectManager is required for event subscriptions")

        try:
            # Use standardized event subscription patterns from subject manager
            event_subjects = self.subject_manager.get_event_subscription_patterns()
            logger.info(
                "Subscribing to event subjects using standardized patterns",
                pattern_count=len(event_subjects),
            )

            logger.debug("Event subscription patterns", subjects=event_subjects)

            success_count = 0
            for subject in event_subjects:
                try:
                    await self._subscribe_to_subject(subject)
                    success_count += 1
                except NATSError as e:
                    logger.error(
                        "Failed to subscribe to event subject",
                        subject=subject,
                        error=str(e),
                    )

            if success_count == len(event_subjects):
                logger.info("Successfully subscribed to all event subjects", count=success_count)
                return True
            logger.warning(
                "Partial success subscribing to event subjects", successful=success_count, total=len(event_subjects)
            )
            return success_count == len(event_subjects)

        except NATSError as e:
            logger.error("Error subscribing to event subjects", error=str(e))
            return False

    async def unsubscribe_from_event_subjects(self) -> bool:
        """
        Unsubscribe from all event-related NATS subjects using standardized patterns.

        Raises:
            RuntimeError: If subject manager is not available

        Returns:
            True if all unsubscriptions successful, False otherwise

        AI: Uses subject manager to get event subscription patterns dynamically.
            Subject manager is required - no legacy fallback.
        """
        if not self.subject_manager:
            raise RuntimeError("NATSSubjectManager is required for event unsubscriptions")

        try:
            # Use standardized event subscription patterns from subject manager
            event_subjects = self.subject_manager.get_event_subscription_patterns()
            logger.info(
                "Unsubscribing from event subjects using standardized patterns",
                pattern_count=len(event_subjects),
            )

            logger.debug("Unsubscribing from event subjects", subjects=event_subjects)

            success_count = 0
            for subject in event_subjects:
                if subject in self.subscriptions:
                    success = await self._unsubscribe_from_subject(subject)
                    if success:
                        success_count += 1

            if success_count == len(event_subjects):
                logger.info("Successfully unsubscribed from all event subjects", count=success_count)
                return True
            logger.warning(
                "Partial success unsubscribing from event subjects",
                successful=success_count,
                total=len(event_subjects),
            )
            return success_count == len(event_subjects)

        except NATSError as e:
            logger.error("Error unsubscribing from event subjects", error=str(e))
            return False

    def _get_event_handler_map(self) -> dict[str, Callable[[dict[str, Any]], Any]]:
        """Get mapping of event types to their handler methods."""
        return self._event_handler.get_event_handler_map()

    def _validate_event_message(self, event_type: str | None, data: dict[str, Any]) -> bool:
        """Validate that event message has required fields."""
        return self._event_handler.validate_event_message(event_type, data)

    async def _handle_event_message(self, message_data: dict[str, Any]) -> None:
        """Handle incoming event messages from NATS."""
        await self._event_handler.handle_event_message(message_data)

    async def _handle_player_entered_event(self, data: dict[str, Any]) -> None:
        """Handle player_entered event."""
        await self._event_handler.handle_player_entered_event(data)

    async def _handle_player_left_event(self, data: dict[str, Any]) -> None:
        """Handle player_left event."""
        await self._event_handler.handle_player_left_event(data)

    async def _handle_game_tick_event(self, data: dict[str, Any]) -> None:
        """Handle game_tick event."""
        await self._event_handler.handle_game_tick_event(data)

    def get_event_subscription_count(self) -> int:
        """
        Get the number of active event subscriptions.

        Returns:
            Number of active event subscriptions
        """
        event_subjects = [
            "events.player_entered.*",
            "events.player_left.*",
            "events.game_tick",
        ]

        count = 0
        for subject in event_subjects:
            if subject in self.subscriptions:
                count += 1

        return count

    def is_event_subscription_active(self, subject: str) -> bool:
        """
        Check if a specific event subscription is active.

        Args:
            subject: NATS subject to check

        Returns:
            True if subscription is active, False otherwise
        """
        return subject in self.subscriptions

    async def _handle_combat_started_event(self, data: dict[str, Any]) -> None:
        """Handle combat_started event."""
        await self._event_handler.handle_combat_started_event(data)

    async def _handle_combat_ended_event(self, data: dict[str, Any]) -> None:
        """Handle combat_ended event."""
        await self._event_handler.handle_combat_ended_event(data)

    async def _handle_player_attacked_event(self, data: dict[str, Any]) -> None:
        """Handle player_attacked event."""
        await self._event_handler.handle_player_attacked_event(data)

    async def _handle_npc_attacked_event(self, data: dict[str, Any]) -> None:
        """Handle npc_attacked event."""
        await self._event_handler.handle_npc_attacked_event(data)

    async def _handle_npc_took_damage_event(self, data: dict[str, Any]) -> None:
        """Handle npc_took_damage event."""
        await self._event_handler.handle_npc_took_damage_event(data)

    async def _handle_npc_died_event(self, data: dict[str, Any]) -> None:
        """Handle npc_died event - NATS to EventBus bridge pattern."""
        await self._event_handler.handle_npc_died_event(data)


# AI Agent: Global singleton removed - use ApplicationContainer.nats_message_handler instead
# Migration complete: All code now uses dependency injection via container
