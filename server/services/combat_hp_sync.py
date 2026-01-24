"""
DP synchronization module for combat service.

This module handles player DP persistence and event publishing for combat operations.
Separated from combat_service.py to reduce file size and improve maintainability.

As documented in the restricted archives, DP synchronization requires careful
coordination between in-memory combat state and persistent database storage.
"""

# pylint: disable=too-few-public-methods,too-many-arguments,too-many-positional-arguments  # Reason: HP sync module has focused responsibility with minimal public interface, and requires many parameters for synchronization logic

from typing import TYPE_CHECKING, Any
from uuid import UUID

from ..events.event_bus import EventBus
from ..events.event_types import PlayerDPUpdated
from ..exceptions import DatabaseError
from ..models.game import PositionState
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer

logger = get_logger(__name__)


class CombatDPSync:  # pylint: disable=too-few-public-methods  # Reason: DP sync class with focused responsibility, minimal public interface
    """Handles DP synchronization for combat operations."""

    def __init__(self, combat_service: Any) -> None:
        """Initialize DP sync with reference to parent combat service."""
        self._combat_service = combat_service
        self._nats_service = getattr(combat_service, "_nats_service", None)
        self._combat_event_publisher = getattr(combat_service, "_combat_event_publisher", None)

    def _persist_player_dp_background(
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
        """
        import asyncio

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
                DatabaseError,
                AttributeError,
                ValueError,
                TypeError,
                RuntimeError,
                ConnectionError,
                TimeoutError,
                OSError,
            ) as e:
                logger.error(
                    "Background DP persistence failed - sending correction event",
                    player_id=player_id,
                    current_dp=current_dp,
                    error=str(e),
                    error_type=type(e).__name__,
                    exc_info=True,
                )
                try:
                    await self._publish_player_dp_correction_event(
                        player_id, old_dp, max_dp, room_id, combat_id, str(e)
                    )
                except (
                    DatabaseError,
                    AttributeError,
                    ValueError,
                    TypeError,
                    RuntimeError,
                    ConnectionError,
                    TimeoutError,
                    OSError,
                ) as correction_error:
                    logger.error(
                        "Failed to send DP correction event after persistence failure",
                        player_id=player_id,
                        error=str(correction_error),
                        error_type=type(correction_error).__name__,
                        exc_info=True,
                    )

        task_coro = _persist_and_handle_errors()
        try:
            task = asyncio.create_task(task_coro)
            logger.debug(
                "Created background task for DP persistence",
                player_id=player_id,
                current_dp=current_dp,
            )
            # If a test double returns something other than an asyncio.Task, close the coroutine to avoid leaks.
            # Type checker thinks this is unreachable (asyncio.create_task always returns Task),
            # but test doubles may return non-Task objects, so we keep the check for test safety
            if not isinstance(task, asyncio.Task):
                task_coro.close()  # type: ignore[unreachable]  # Reason: Type checker thinks this is unreachable (asyncio.create_task always returns Task), but test doubles may return non-Task objects, we keep the check for test safety
        except RuntimeError as e:
            task_coro.close()
            logger.error(
                "Cannot create background task - no event loop available",
                player_id=player_id,
                error=str(e),
            )
        except Exception as e:  # noqa: B904  # pragma: no cover - defensive path for unexpected test doubles  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task creation errors unpredictable, must handle gracefully
            task_coro.close()
            logger.error(
                "Failed to create background task for DP persistence",
                player_id=player_id,
                current_dp=current_dp,
                error=str(e),
                error_type=type(e).__name__,
            )

    def _get_persistence(self, player_id: UUID) -> "AsyncPersistenceLayer | None":
        """
        Get persistence layer from application container.

        Args:
            player_id: Player ID for logging context

        Returns:
            Persistence instance or None if unavailable
        """
        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            return getattr(container, "async_persistence", None) if container else None
        except (ImportError, AttributeError, RuntimeError, TypeError) as e:
            logger.warning("Could not get persistence from container", error=str(e), player_id=player_id)
            return None

    def _update_player_position(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Position update requires many parameters for context and position updates
        self, stats: dict[str, Any], current_dp: int, old_dp: int, player_id: UUID, player_name: str
    ) -> None:
        """
        Update player position based on DP threshold.

        Args:
            stats: Player stats dictionary to update
            current_dp: New current DP value
            old_dp: Previous DP value
            player_id: Player ID for logging
            player_name: Player name for logging
        """
        if current_dp <= 0 < old_dp:
            stats["position"] = PositionState.LYING
            logger.info(
                "Player posture changed to lying (unconscious in combat)",
                player_id=player_id,
                player_name=player_name,
                dp=current_dp,
            )
        elif current_dp <= 0 and stats.get("position") != PositionState.LYING:
            stats["position"] = PositionState.LYING

    async def _verify_player_save(
        self, persistence: "AsyncPersistenceLayer", player_id: UUID, player_name: str, old_dp: int, current_dp: int
    ) -> None:
        """
        Verify that player DP was successfully saved to database.

        Args:
            persistence: Persistence layer instance
            player_id: Player ID
            player_name: Player name for logging
            old_dp: Previous DP value
            current_dp: Expected current DP value
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

    def _log_death_threshold_events(self, current_dp: int, old_dp: int, player_id: UUID, player_name: str) -> None:
        """
        Log death threshold events based on DP changes.

        Args:
            current_dp: New current DP value
            old_dp: Previous DP value
            player_id: Player ID for logging
            player_name: Player name for logging
        """
        if current_dp <= -10 and old_dp > -10:
            logger.info(
                "Player reached death threshold in combat - triggering immediate death handling",
                player_id=player_id,
                player_name=player_name,
                final_dp=current_dp,
            )
            logger.debug(
                "Player reached death threshold - will be handled by game tick loop within 1 second",
                player_id=player_id,
                player_name=player_name,
            )
        elif current_dp <= 0 < old_dp:
            logger.info(
                "Player became mortally wounded in combat",
                player_id=player_id,
                player_name=player_name,
                dp=current_dp,
            )

    async def _update_and_save_player_dp(
        self, persistence: "AsyncPersistenceLayer", player_id: UUID, current_dp: int
    ) -> tuple[Any, int] | None:
        """
        Update player DP and save to database.

        Args:
            persistence: Persistence layer instance
            player_id: Player ID
            current_dp: New current DP value

        Returns:
            Tuple of (player, old_dp) if successful, None otherwise
        """
        player = await persistence.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for DP persistence", player_id=player_id)
            return None

        stats = player.get_stats()
        old_dp = stats.get("current_dp", 100)

        logger.debug(
            "Stats before DP update",
            player_id=player_id,
            raw_stats=player.stats,
            parsed_stats=stats,
            current_dp_in_stats=stats.get("current_dp"),
        )

        stats["current_dp"] = current_dp
        self._update_player_position(stats, current_dp, old_dp, player_id, player.name)
        player.set_stats(stats)

        logger.debug(
            "Stats after DP update, before save",
            player_id=player_id,
            raw_stats_after_set=player.stats,
            new_current_dp=current_dp,
        )

        await persistence.save_player(player)
        return (player, old_dp)

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
            logger.info("_persist_player_dp called", player_id=player_id, current_dp=current_dp)

            persistence = self._get_persistence(player_id)
            if not persistence:
                logger.warning("No persistence layer available for DP persistence", player_id=player_id)
                return

            result = await self._update_and_save_player_dp(persistence, player_id, current_dp)
            if not result:
                return

            player, old_dp = result
            await self._verify_player_save(persistence, player_id, player.name, old_dp, current_dp)
            self._log_death_threshold_events(current_dp, old_dp, player_id, player.name)

        except (
            DatabaseError,
            AttributeError,
            ValueError,
            TypeError,
            RuntimeError,
            ConnectionError,
            TimeoutError,
            OSError,
        ) as e:
            logger.error(
                "Error persisting player DP",
                player_id=player_id,
                current_dp=current_dp,
                error=str(e),
                exc_info=True,
            )

    async def _publish_player_dp_update_event(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event publishing requires many parameters for complete event context
        self,
        player_id: UUID,
        old_dp: int,
        new_dp: int,
        max_dp: int,
        combat_id: str | None = None,
        room_id: str | None = None,
    ) -> None:
        """Publish a PlayerDPUpdated event for real-time UI updates."""
        try:
            logger.info(
                "_publish_player_dp_update_event called",
                player_id=player_id,
                old_dp=old_dp,
                new_dp=new_dp,
                max_dp=max_dp,
            )

            event_bus = EventBus()
            damage_taken = old_dp - new_dp

            dp_update_event = PlayerDPUpdated(
                player_id=player_id,
                old_dp=old_dp,
                new_dp=new_dp,
                max_dp=max_dp,
                damage_taken=damage_taken,
                source_id=None,
                combat_id=combat_id,
                room_id=room_id,
            )

            if event_bus:
                try:
                    event_bus.publish(dp_update_event)
                    logger.info(
                        "Published PlayerDPUpdated event to event bus (immediate UI update)",
                        player_id=player_id,
                        old_dp=old_dp,
                        new_dp=new_dp,
                        event_bus_type=type(event_bus).__name__,
                    )
                except (
                    AttributeError,
                    RuntimeError,
                    ValueError,
                    TypeError,
                ) as e:
                    logger.error(
                        "Failed to publish PlayerDPUpdated event to event bus",
                        player_id=player_id,
                        error=str(e),
                        error_type=type(e).__name__,
                        exc_info=True,
                    )
            else:
                logger.warning("No event bus available for DP update event", player_id=player_id)

            if self._nats_service:
                if (
                    self._combat_event_publisher is not None
                    and hasattr(self._combat_event_publisher, "subject_manager")
                    and self._combat_event_publisher.subject_manager
                ):
                    subject = self._combat_event_publisher.subject_manager.build_subject(
                        "combat_dp_update", player_id=str(dp_update_event.player_id)
                    )
                else:
                    subject = f"combat.dp_update.{dp_update_event.player_id}"
                    logger.warning(
                        "Using legacy subject construction - subject_manager not available",
                        event_type="combat_dp_update",
                        player_id=str(dp_update_event.player_id),
                    )

                message_data = {
                    "event_type": "player_dp_updated",
                    "data": {
                        "player_id": dp_update_event.player_id,
                        "old_dp": dp_update_event.old_dp,
                        "new_dp": dp_update_event.new_dp,
                        "max_dp": dp_update_event.max_dp,
                        "damage_taken": dp_update_event.damage_taken,
                        "timestamp": dp_update_event.timestamp.isoformat(),
                    },
                }
                await self._nats_service.publish(subject, message_data)
                logger.debug("Published PlayerDPUpdated event to NATS", player_id=player_id)
            else:
                logger.debug("No NATS service available for DP update event", player_id=player_id)

            logger.info(
                "Published PlayerDPUpdated event",
                player_id=player_id,
                old_dp=old_dp,
                new_dp=new_dp,
                damage_taken=damage_taken,
            )

        except (
            DatabaseError,
            AttributeError,
            ValueError,
            TypeError,
            RuntimeError,
            ConnectionError,
            TimeoutError,
            OSError,
        ) as e:
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
        """Publish a correction event when database persistence fails."""
        try:
            logger.warning(
                "Publishing DP correction event due to persistence failure",
                player_id=player_id,
                correct_dp=correct_dp,
                error_message=error_message,
            )

            event_bus = EventBus()

            correction_event = PlayerDPUpdated(
                player_id=player_id,
                old_dp=correct_dp,
                new_dp=correct_dp,
                max_dp=max_dp,
                damage_taken=0,
                source_id=None,
                combat_id=combat_id,
                room_id=room_id,
            )

            if event_bus:
                try:
                    event_bus.publish(correction_event)
                    logger.info(
                        "Published DP correction event to event bus",
                        player_id=player_id,
                        correct_dp=correct_dp,
                    )
                except (
                    AttributeError,
                    RuntimeError,
                    ValueError,
                    TypeError,
                ) as e:
                    logger.error(
                        "Failed to publish DP correction event to event bus",
                        player_id=player_id,
                        error=str(e),
                        exc_info=True,
                    )
            else:
                logger.warning("No event bus available for DP correction event", player_id=player_id)

        except (
            DatabaseError,
            AttributeError,
            ValueError,
            TypeError,
            RuntimeError,
            ConnectionError,
            TimeoutError,
            OSError,
        ) as e:
            logger.error(
                "Error publishing DP correction event",
                player_id=player_id,
                error=str(e),
                exc_info=True,
            )
