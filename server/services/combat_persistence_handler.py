"""
Publishes a combat hit's PlayerDPUpdated event. The DP itself is committed by the hit (CombatAttackHandler, ADR-029).
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-lines  # Reason: Persistence handling requires many parameters and intermediate variables for complex persistence logic. Combat persistence handler requires extensive persistence logic for comprehensive DP management.

from typing import TYPE_CHECKING, Any
from uuid import UUID

from server.services.nats_exceptions import NATSError
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    # Runtime import stays inline (in the publish method) to avoid a circular import;
    # this one is type-checking only and never executes.
    from server.events.event_types import PlayerDPUpdated

logger = get_logger(__name__)


class CombatPersistenceHandler:
    """Handles combat-related persistence operations."""

    def __init__(self, combat_service: Any) -> None:
        """
        Initialize the persistence handler.

        Args:
            combat_service: Reference to the parent CombatService
        """
        self._combat_service = combat_service

    # Exceptions from event_bus.publish()/nats_service.publish() that are logged and
    # swallowed rather than propagated -- a DP event failing to broadcast must
    # never fail the combat action that triggered it.
    _EVENT_PUBLISH_EXCEPTIONS: tuple[type[Exception], ...] = (
        NATSError,
        ValueError,
        RuntimeError,
        AttributeError,
        ConnectionError,
        TypeError,
        KeyError,
    )

    def _publish_dp_event_to_bus(
        self, event: "PlayerDPUpdated", player_id: UUID, event_label: str, success_extra: dict[str, object]
    ) -> None:
        """Publish a PlayerDPUpdated event to the shared combat-service event bus; a failure is logged, not raised."""
        # Reason: SERIALIZATION_BOUNDARY - _combat_service is Any per this class's own
        # __init__(combat_service: Any); every method in this class resolves dependencies
        # off it the same way.
        # Appropriate because: consistent with this class's established, unsuppressed
        # convention; narrowing it means Protocol-typing CombatService/EventBus, out of
        # scope for this extraction.
        event_bus = getattr(self._combat_service, "_event_bus", None)  # pyright: ignore[reportAny]
        if not event_bus:
            logger.warning("No event bus available for event", event_label=event_label, player_id=player_id)
            return
        try:
            # Reason: SERIALIZATION_BOUNDARY - event_bus is Any (see getattr above).
            # Appropriate because: same class-wide unsuppressed Any convention as above.
            event_bus.publish(event)  # pyright: ignore[reportAny]
            logger.info(
                "Published event to event bus",
                event_label=event_label,
                player_id=player_id,
                # Reason: SERIALIZATION_BOUNDARY - event_bus is Any (see getattr above).
                # Appropriate because: same class-wide unsuppressed Any convention as above.
                event_bus_type=type(event_bus).__name__,  # pyright: ignore[reportAny]
                **success_extra,
            )
        except self._EVENT_PUBLISH_EXCEPTIONS as e:
            logger.error(
                "Failed to publish event to event bus",
                event_label=event_label,
                player_id=player_id,
                error=str(e),
                exc_info=True,
            )

    async def publish_player_dp_update_event(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event publishing requires many parameters for complete event context
        self,
        player_id: UUID,
        old_dp: int,
        new_dp: int,
        max_dp: int,
        combat_id: str | None = None,
        room_id: str | None = None,
    ) -> None:
        """
        Publish a PlayerDPUpdated event for real-time UI updates.

        Args:
            player_id: ID of the player whose DP changed
            old_dp: Previous DP value
            new_dp: New DP value
            max_dp: Maximum DP value
            combat_id: Combat ID for context
            room_id: Room ID for context
        """
        await self._publish_player_dp_update_event_impl(player_id, old_dp, new_dp, max_dp, combat_id, room_id)

    # Reason: SERIALIZATION_BOUNDARY - _combat_service is Any per this class's own
    # __init__(combat_service: Any) (unchanged by this refactor); every method in this class
    # resolves its dependencies off it the same way via getattr.
    # Appropriate because: consistent with this class's established, unsuppressed convention;
    # narrowing it means Protocol-typing CombatService/NATSService/CombatEventPublisher, out
    # of scope for this extraction.
    async def _publish_dp_update_to_nats(self, dp_update_event: "PlayerDPUpdated") -> None:
        """Publish a PlayerDPUpdated event via NATS, for systems that don't use the event bus."""
        # Reason: SERIALIZATION_BOUNDARY - _combat_service is Any per this class's own
        # __init__(combat_service: Any); every method here resolves dependencies off it.
        # Appropriate because: consistent with this class's established convention; Protocol-
        # typing NATSService here is out of scope for this complexity-only extraction.
        nats_service = getattr(self._combat_service, "_nats_service", None)  # pyright: ignore[reportAny]
        if not nats_service:
            logger.debug("No NATS service available for DP update event", player_id=dp_update_event.player_id)
            return

        # Reason: SERIALIZATION_BOUNDARY - _combat_service is Any (see nats_service above).
        # Appropriate because: same class-wide convention as the nats_service lookup above.
        combat_event_publisher = getattr(self._combat_service, "_combat_event_publisher", None)  # pyright: ignore[reportAny]
        # Reason: SERIALIZATION_BOUNDARY - combat_event_publisher is Any (see getattr above).
        # Appropriate because: same class-wide convention as the nats_service lookup above.
        if combat_event_publisher and hasattr(combat_event_publisher, "subject_manager"):  # pyright: ignore[reportAny]
            # Reason: SERIALIZATION_BOUNDARY - combat_event_publisher is Any (see above).
            # Appropriate because: same class-wide convention as the nats_service lookup above.
            subject = combat_event_publisher.subject_manager.build_subject(  # pyright: ignore[reportAny]
                "combat_dp_update", player_id=str(dp_update_event.player_id)
            )
        else:
            # Legacy fallback
            subject = f"combat.dp_update.{dp_update_event.player_id}"
            logger.warning(
                "Using legacy subject construction - subject_manager not available",
                event_type="combat_dp_update",
                player_id=str(dp_update_event.player_id),
            )

        message_data = {
            "event_type": "player_dp_updated",
            "data": {
                "player_id": str(dp_update_event.player_id),
                "old_dp": dp_update_event.old_dp,
                "new_dp": dp_update_event.new_dp,
                "max_dp": dp_update_event.max_dp,
                "damage_taken": dp_update_event.damage_taken,
                "timestamp": dp_update_event.timestamp.isoformat(),
            },
        }
        # Reason: SERIALIZATION_BOUNDARY - nats_service is Any (see getattr above).
        # Appropriate because: same class-wide unsuppressed Any convention as above.
        await nats_service.publish(subject, message_data)  # pyright: ignore[reportAny]
        logger.debug("Published PlayerDPUpdated event to NATS", player_id=dp_update_event.player_id)

    async def _publish_player_dp_update_event_impl(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event publishing requires many parameters for complete event context
        self,
        player_id: UUID,
        old_dp: int,
        new_dp: int,
        max_dp: int,
        combat_id: str | None = None,
        room_id: str | None = None,
    ) -> None:
        """
        Internal implementation of player DP update event publishing.

        Args:
            player_id: ID of the player whose DP changed
            old_dp: Previous DP value
            new_dp: New DP value
            max_dp: Maximum DP value
            combat_id: Combat ID for context
            room_id: Room ID for context
        """
        try:
            logger.info(
                "_publish_player_dp_update_event called",
                player_id=player_id,
                old_dp=old_dp,
                new_dp=new_dp,
                max_dp=max_dp,
                has_player_combat_service=bool(getattr(self._combat_service, "_player_combat_service", None)),
            )
            from server.events.event_types import PlayerDPUpdated

            # Calculate damage taken (negative for healing)
            damage_taken = old_dp - new_dp

            dp_update_event = PlayerDPUpdated(
                player_id=player_id,  # player_id is already UUID
                old_dp=old_dp,
                new_dp=new_dp,
                max_dp=max_dp,
                damage_taken=damage_taken,
                source_id=None,  # Could be enhanced to track damage source
                combat_id=combat_id,  # Combat context for tracking
                room_id=room_id,  # Room context for tracking
            )

            # Publish to event bus so RealTimeEventHandler can send it to the client
            # CRITICAL: RealTimeEventHandler subscribes to the event bus, not NATS directly
            self._publish_dp_event_to_bus(
                dp_update_event,
                player_id,
                "PlayerDPUpdated event (immediate UI update)",
                {"old_dp": old_dp, "new_dp": new_dp},
            )

            # Also publish via NATS for other systems that might be listening
            await self._publish_dp_update_to_nats(dp_update_event)

            logger.info(
                "Published PlayerDPUpdated event",
                player_id=player_id,
                old_dp=old_dp,
                new_dp=new_dp,
                damage_taken=damage_taken,
            )

        except self._EVENT_PUBLISH_EXCEPTIONS as e:
            logger.error(
                "Error publishing PlayerDPUpdated event",
                player_id=player_id,
                old_dp=old_dp,
                new_dp=new_dp,
                error=str(e),
                exc_info=True,
            )
