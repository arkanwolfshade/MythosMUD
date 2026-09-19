"""
Combat persistence handling logic.

Handles player DP persistence, verification, and event publishing.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-lines  # Reason: Persistence handling requires many parameters and intermediate variables for complex persistence logic. Combat persistence handler requires extensive persistence logic for comprehensive DP management.

import asyncio
from typing import TYPE_CHECKING, Any
from uuid import UUID

from server.services.nats_exceptions import NATSError
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    # Runtime import stays inline (in the two publish methods) to avoid a circular import;
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
    # swallowed rather than propagated -- a DP event/correction failing to broadcast must
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
        """Publish a PlayerDPUpdated(-shaped) event to the shared combat-service event bus.

        Shared by _publish_player_dp_update_event_impl and _publish_player_dp_correction_event
        (issue #787): both looked up the same event_bus and ran the identical
        publish-or-log-and-swallow sequence, differing only in the log text/extra fields.
        """
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

    def _get_persistence_layer(self) -> Any | None:
        """
        Get persistence layer from application container.

        Returns:
            Persistence layer instance or None if unavailable
        """
        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            return getattr(container, "async_persistence", None) if container else None
        except (
            ImportError,
            AttributeError,
            ValueError,
            TypeError,
            RuntimeError,
            NATSError,
            ConnectionError,
            KeyError,
        ) as e:
            logger.warning("Could not get persistence from container", error=str(e))
            return None

    async def _verify_player_save(
        self, persistence: Any, player_id: UUID, player_name: str, old_dp: int, current_dp: int
    ) -> None:
        """
        Verify that player save was successful by reading back from database.

        Args:
            persistence: Persistence layer instance
            player_id: ID of the player
            player_name: Name of the player
            old_dp: Previous DP value
            current_dp: New DP value
        """
        verification_player = await persistence.get_player_by_id(player_id)
        if verification_player:
            verification_stats = verification_player.get_stats()
            verification_dp = verification_stats.get("current_dp", -999)
            logger.info(
                "Player DP persisted to database - VERIFICATION",
                player_id=player_id,
                player_name=player_name,
                old_dp=old_dp,
                new_dp=current_dp,
                verified_dp_from_db=verification_dp,
                save_successful=verification_dp == current_dp,
            )
        else:
            logger.error("Could not verify player save - player not found after save", player_id=player_id)

    def _log_death_state_changes(self, player_id: UUID, player_name: str, current_dp: int, old_dp: int) -> None:
        """
        Log death state changes (death threshold or mortally wounded).

        Args:
            player_id: ID of the player
            player_name: Name of the player
            current_dp: Current DP value
            old_dp: Previous DP value
        """
        # Check if player has reached death threshold
        # CRITICAL: Players at 0 DP or below should enter mortally wounded state immediately
        # Players at -10 DP should trigger death handling and limbo transition
        if current_dp <= -10 and old_dp > -10:
            logger.info(
                "Player reached death threshold in combat - triggering immediate death handling",
                player_id=player_id,
                player_name=player_name,
                final_dp=current_dp,
            )
            # Immediately trigger death handling and move to limbo
            # NOTE: The game tick loop will also check for dead players, but this provides immediate handling
            # We'll let the game tick loop handle it since we don't have easy access to a database session here
            # The tick loop runs every second, so the delay is minimal
            logger.debug(
                "Player reached death threshold - will be handled by game tick loop within 1 second",
                player_id=player_id,
                player_name=player_name,
            )
        elif current_dp <= 0 < old_dp:
            # Player just became mortally wounded
            logger.info(
                "Player became mortally wounded in combat",
                player_id=player_id,
                player_name=player_name,
                current_dp=current_dp,
            )
            # DP decay will be processed automatically by the tick loop

    async def _persist_player_dp_sync(self, player_id: UUID, current_dp: int) -> None:
        """
        Synchronously persist player DP to database.

        This is the actual persistence logic, called from the background task.
        Separated from the old _persist_player_dp to allow background execution.

        Args:
            player_id: ID of the player whose DP changed
            current_dp: New current DP value
        """
        try:
            logger.info("_persist_player_dp_sync called", player_id=player_id, current_dp=current_dp)

            # Get persistence layer from application container
            persistence = self._get_persistence_layer()
            if not persistence:
                logger.warning("No persistence layer available for DP persistence", player_id=player_id)
                return

            # Get player from database
            player = await persistence.get_player_by_id(player_id)
            if not player:
                logger.warning("Player not found for DP persistence", player_id=player_id)
                return

            # Delegate DP and posture updates to Player domain model
            old_dp, became_mortally_wounded, _became_dead = player.apply_dp_change(current_dp)
            if became_mortally_wounded:
                logger.info(
                    "Player posture changed to lying (unconscious in combat)",
                    player_id=player_id,
                    player_name=player.name,
                    dp=current_dp,
                )

            # Save player to database
            await persistence.save_player(player)

            # Verify save was successful
            await self._verify_player_save(persistence, player_id, player.name, old_dp, current_dp)

            # NOTE: DP update event is now published IMMEDIATELY in process_attack()
            # before this persistence method is called. This method only handles database persistence.
            # The event was already sent for real-time UI updates.

            # Log death state changes
            self._log_death_state_changes(player_id, player.name, current_dp, old_dp)

        except (
            NATSError,
            ValueError,
            RuntimeError,
            AttributeError,
            ConnectionError,
            TypeError,
            KeyError,
        ) as e:
            logger.error(
                "Error persisting player DP to database",
                player_id=player_id,
                current_dp=current_dp,
                error=str(e),
                exc_info=True,
            )

    def _persist_player_dp_background(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: DP persistence requires many parameters for context and persistence operations
        self,
        player_id: UUID,
        current_dp: int,
        old_dp: int,
        max_dp: int,
        room_id: str | None = None,
        combat_id: str | None = None,
    ) -> None:
        """
        Persist player DP to database in background (fire-and-forget).

        This method runs database persistence asynchronously without blocking the combat flow.
        If persistence fails, a correction event is sent to update the client with the correct DP.

        Args:
            player_id: ID of the player whose DP changed
            current_dp: New current DP value
            old_dp: Previous DP value (for correction events if save fails)
            max_dp: Maximum DP value
            room_id: Room ID where the change occurred (for error context)
            combat_id: Combat ID for context
        """

        async def _persist_and_handle_errors() -> None:
            """Background task to persist DP and handle errors."""
            try:
                await self._persist_player_dp_sync(player_id, current_dp)
                logger.debug(
                    "Background DP persistence completed successfully",
                    player_id=player_id,
                    current_dp=current_dp,
                )
            except (
                AttributeError,
                ValueError,
                TypeError,
                RuntimeError,
                ConnectionError,
                OSError,
                ImportError,
                KeyError,
                NATSError,
            ) as e:
                logger.error(
                    "Background DP persistence failed - sending correction event",
                    player_id=player_id,
                    current_dp=current_dp,
                    error=str(e),
                    exc_info=True,
                )
                # Send correction event with old_dp to revert the optimistic update
                # This ensures the client shows the correct DP if database save failed
                try:
                    await self._publish_player_dp_correction_event(
                        player_id, old_dp, max_dp, room_id, combat_id, str(e)
                    )
                except (
                    AttributeError,
                    ValueError,
                    TypeError,
                    RuntimeError,
                    ConnectionError,
                    OSError,
                    ImportError,
                    KeyError,
                    NATSError,
                ) as correction_error:
                    logger.error(
                        "Failed to send DP correction event after persistence failure",
                        player_id=player_id,
                        error=str(correction_error),
                        exc_info=True,
                    )

        # Create background task (fire-and-forget)
        try:
            asyncio.create_task(_persist_and_handle_errors())
            logger.debug(
                "Created background task for DP persistence",
                player_id=player_id,
                current_dp=current_dp,
            )
        except RuntimeError as e:
            # No event loop available - log error but don't crash
            logger.error(
                "Cannot create background task - no event loop available",
                player_id=player_id,
                error=str(e),
            )

    def persist_player_dp_background(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: DP persistence requires many parameters for context and persistence operations
        self,
        player_id: UUID,
        current_dp: int,
        old_dp: int,
        max_dp: int,
        room_id: str | None = None,
        combat_id: str | None = None,
    ) -> None:
        """
        Persist player DP to database in background (fire-and-forget).

        Public API method that wraps the internal implementation.

        Args:
            player_id: ID of the player whose DP changed
            current_dp: New current DP value
            old_dp: Previous DP value (for correction events if save fails)
            max_dp: Maximum DP value
            room_id: Room ID where the change occurred (for error context)
            combat_id: Combat ID for context
        """
        self._persist_player_dp_background(player_id, current_dp, old_dp, max_dp, room_id, combat_id)

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

    async def _publish_player_dp_correction_event(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event publishing requires many parameters for complete event context
        self,
        player_id: UUID,
        correct_dp: int,
        max_dp: int,
        room_id: str | None = None,
        combat_id: str | None = None,
        error_message: str | None = None,
    ) -> None:
        """
        Publish a correction event when database persistence fails.

        This sends a PlayerDPUpdated event with the correct (previous) DP value
        to revert an optimistic update that failed to persist.

        Args:
            player_id: ID of the player whose DP needs correction
            correct_dp: The correct DP value (from before the failed update)
            max_dp: Maximum DP value
            room_id: Room ID where the change occurred
            combat_id: Combat ID for context
            error_message: Error message explaining why correction is needed
        """
        try:
            logger.warning(
                "Publishing DP correction event due to persistence failure",
                player_id=player_id,
                correct_dp=correct_dp,
                error_message=error_message,
            )
            from server.events.event_types import PlayerDPUpdated

            # Create correction event - damage_taken is 0 since we're reverting
            correction_event = PlayerDPUpdated(
                player_id=player_id,  # player_id is already UUID
                old_dp=correct_dp,  # This will be the "new" DP shown to client
                new_dp=correct_dp,  # Revert to correct DP
                max_dp=max_dp,
                damage_taken=0,  # No damage change, just correction
                source_id=None,
                combat_id=combat_id,
                room_id=room_id,
            )

            self._publish_dp_event_to_bus(
                correction_event, player_id, "DP correction event", {"correct_dp": correct_dp}
            )

        except self._EVENT_PUBLISH_EXCEPTIONS as e:
            logger.error(
                "Error publishing DP correction event",
                player_id=player_id,
                error=str(e),
                exc_info=True,
            )
