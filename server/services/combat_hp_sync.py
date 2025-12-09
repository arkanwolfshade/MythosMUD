"""
HP synchronization module for combat service.

This module handles player HP persistence and event publishing for combat operations.
Separated from combat_service.py to reduce file size and improve maintainability.

As documented in the restricted archives, HP synchronization requires careful
coordination between in-memory combat state and persistent database storage.
"""

from uuid import UUID

from ..events.event_bus import EventBus
from ..events.event_types import PlayerHPUpdated
from ..logging.enhanced_logging_config import get_logger
from ..models.game import PositionState

logger = get_logger(__name__)


class CombatHPSync:
    """Handles HP synchronization for combat operations."""

    def __init__(self, combat_service):
        """Initialize HP sync with reference to parent combat service."""
        self._combat_service = combat_service
        self._nats_service = getattr(combat_service, "_nats_service", None)
        self._combat_event_publisher = getattr(combat_service, "_combat_event_publisher", None)

    def _persist_player_hp_background(
        self,
        player_id: UUID,
        current_hp: int,
        old_hp: int,
        max_hp: int,
        room_id: str | None = None,
        combat_id: str | None = None,
    ) -> None:
        """
        Persist player HP to database in background (fire-and-forget).

        This method runs database persistence asynchronously without blocking the combat flow.
        If persistence fails, a correction event is sent to update the client with the correct HP.

        Args:
            player_id: ID of the player whose HP changed
            current_hp: New current HP value
            old_hp: Previous HP value (for correction events if save fails)
            max_hp: Maximum HP value
            room_id: Room ID where the change occurred (for error context)
        """
        import asyncio

        async def _persist_and_handle_errors() -> None:
            """Background task to persist HP and handle errors."""
            try:
                await self._persist_player_hp_sync(player_id, current_hp)
                logger.debug(
                    "Background HP persistence completed successfully",
                    player_id=player_id,
                    current_hp=current_hp,
                )
            except Exception as e:
                logger.error(
                    "Background HP persistence failed - sending correction event",
                    player_id=player_id,
                    current_hp=current_hp,
                    error=str(e),
                    exc_info=True,
                )
                try:
                    await self._combat_service._publish_player_hp_correction_event(
                        player_id, old_hp, max_hp, room_id, combat_id, str(e)
                    )
                except Exception as correction_error:
                    logger.error(
                        "Failed to send HP correction event after persistence failure",
                        player_id=player_id,
                        error=str(correction_error),
                        exc_info=True,
                    )

        try:
            asyncio.create_task(_persist_and_handle_errors())
            logger.debug(
                "Created background task for HP persistence",
                player_id=player_id,
                current_hp=current_hp,
            )
        except RuntimeError as e:
            logger.error(
                "Cannot create background task - no event loop available",
                player_id=player_id,
                error=str(e),
            )

    async def _persist_player_hp_sync(self, player_id: UUID, current_hp: int) -> None:
        """
        Synchronously persist player HP to database.

        This is the actual persistence logic, called from the background task.
        Separated from the old _persist_player_hp to allow background execution.

        Args:
            player_id: ID of the player whose HP changed
            current_hp: New current HP value
        """
        try:
            logger.info("_persist_player_hp called", player_id=player_id, current_hp=current_hp)

            try:
                from ..container import ApplicationContainer

                container = ApplicationContainer.get_instance()
                persistence = getattr(container, "async_persistence", None) if container else None
            except Exception as e:
                logger.warning("Could not get persistence from container", error=str(e), player_id=player_id)
                persistence = None

            if not persistence:
                logger.warning("No persistence layer available for HP persistence", player_id=player_id)
                return

            player = await persistence.get_player_by_id(player_id)
            if not player:
                logger.warning("Player not found for HP persistence", player_id=player_id)
                return

            stats = player.get_stats()
            old_hp = stats.get("current_health", 100)

            logger.debug(
                "Stats before HP update",
                player_id=player_id,
                raw_stats=player.stats,
                parsed_stats=stats,
                current_health_in_stats=stats.get("current_health"),
            )

            stats["current_health"] = current_hp

            if current_hp <= 0 and old_hp > 0:
                stats["position"] = PositionState.LYING
                logger.info(
                    "Player posture changed to lying (unconscious in combat)",
                    player_id=player_id,
                    player_name=player.name,
                    hp=current_hp,
                )
            elif current_hp <= 0 and stats.get("position") != PositionState.LYING:
                stats["position"] = PositionState.LYING

            player.set_stats(stats)

            logger.debug(
                "Stats after HP update, before save",
                player_id=player_id,
                raw_stats_after_set=player.stats,
                new_current_health=current_hp,
            )

            await persistence.save_player(player)

            verification_player = await persistence.get_player_by_id(player_id)
            if verification_player:
                verification_stats = verification_player.get_stats()
                verification_hp = verification_stats.get("current_health", -999)
                logger.info(
                    "Player HP persisted to database - VERIFICATION",
                    player_id=player_id,
                    player_name=player.name,
                    old_hp=old_hp,
                    new_hp=current_hp,
                    verified_hp_from_db=verification_hp,
                    save_successful=verification_hp == current_hp,
                )
            else:
                logger.error("Could not verify player save - player not found after save", player_id=player_id)

            if current_hp <= -10 and old_hp > -10:
                logger.info(
                    "Player reached death threshold in combat - triggering immediate death handling",
                    player_id=player_id,
                    player_name=player.name,
                    final_hp=current_hp,
                )
                logger.debug(
                    "Player reached death threshold - will be handled by game tick loop within 1 second",
                    player_id=player_id,
                    player_name=player.name,
                )
            elif current_hp <= 0 and old_hp > 0:
                logger.info(
                    "Player became mortally wounded in combat",
                    player_id=player_id,
                    player_name=player.name,
                    hp=current_hp,
                )

        except Exception as e:
            logger.error(
                "Error persisting player HP",
                player_id=player_id,
                current_hp=current_hp,
                error=str(e),
                exc_info=True,
            )

    async def _publish_player_hp_update_event(
        self,
        player_id: UUID,
        old_hp: int,
        new_hp: int,
        max_hp: int,
        combat_id: str | None = None,
        room_id: str | None = None,
    ) -> None:
        """Publish a PlayerHPUpdated event for real-time UI updates."""
        try:
            logger.info(
                "_publish_player_hp_update_event called",
                player_id=player_id,
                old_hp=old_hp,
                new_hp=new_hp,
                max_hp=max_hp,
            )

            event_bus = EventBus()
            damage_taken = old_hp - new_hp

            hp_update_event = PlayerHPUpdated(
                player_id=player_id,
                old_hp=old_hp,
                new_hp=new_hp,
                max_hp=max_hp,
                damage_taken=damage_taken,
                source_id=None,
                combat_id=combat_id,
                room_id=room_id,
            )

            if event_bus:
                try:
                    event_bus.publish(hp_update_event)
                    logger.info(
                        "Published PlayerHPUpdated event to event bus (immediate UI update)",
                        player_id=player_id,
                        old_hp=old_hp,
                        new_hp=new_hp,
                        event_bus_type=type(event_bus).__name__,
                    )
                except Exception as e:
                    logger.error(
                        "Failed to publish PlayerHPUpdated event to event bus",
                        player_id=player_id,
                        error=str(e),
                        error_type=type(e).__name__,
                        exc_info=True,
                    )
            else:
                logger.warning("No event bus available for HP update event", player_id=player_id)

            if self._nats_service:
                if (
                    hasattr(self._combat_event_publisher, "subject_manager")
                    and self._combat_event_publisher.subject_manager
                ):
                    subject = self._combat_event_publisher.subject_manager.build_subject(
                        "combat_hp_update", player_id=str(hp_update_event.player_id)
                    )
                else:
                    subject = f"combat.hp_update.{hp_update_event.player_id}"
                    logger.warning(
                        "Using legacy subject construction - subject_manager not available",
                        event_type="combat_hp_update",
                        player_id=str(hp_update_event.player_id),
                    )

                message_data = {
                    "event_type": "player_hp_updated",
                    "data": {
                        "player_id": hp_update_event.player_id,
                        "old_hp": hp_update_event.old_hp,
                        "new_hp": hp_update_event.new_hp,
                        "max_hp": hp_update_event.max_hp,
                        "damage_taken": hp_update_event.damage_taken,
                        "timestamp": hp_update_event.timestamp.isoformat(),
                    },
                }
                await self._nats_service.publish(subject, message_data)
                logger.debug("Published PlayerHPUpdated event to NATS", player_id=player_id)
            else:
                logger.debug("No NATS service available for HP update event", player_id=player_id)

            logger.info(
                "Published PlayerHPUpdated event",
                player_id=player_id,
                old_hp=old_hp,
                new_hp=new_hp,
                damage_taken=damage_taken,
            )

        except Exception as e:
            logger.error(
                "Error publishing PlayerHPUpdated event",
                player_id=player_id,
                old_hp=old_hp,
                new_hp=new_hp,
                error=str(e),
                exc_info=True,
            )

    async def _publish_player_hp_correction_event(
        self,
        player_id: UUID,
        correct_hp: int,
        max_hp: int,
        room_id: str | None = None,
        combat_id: str | None = None,
        error_message: str | None = None,
    ) -> None:
        """Publish a correction event when database persistence fails."""
        try:
            logger.warning(
                "Publishing HP correction event due to persistence failure",
                player_id=player_id,
                correct_hp=correct_hp,
                error_message=error_message,
            )

            event_bus = EventBus()

            correction_event = PlayerHPUpdated(
                player_id=player_id,
                old_hp=correct_hp,
                new_hp=correct_hp,
                max_hp=max_hp,
                damage_taken=0,
                source_id=None,
                combat_id=combat_id,
                room_id=room_id,
            )

            if event_bus:
                try:
                    event_bus.publish(correction_event)
                    logger.info(
                        "Published HP correction event to event bus",
                        player_id=player_id,
                        correct_hp=correct_hp,
                    )
                except Exception as e:
                    logger.error(
                        "Failed to publish HP correction event to event bus",
                        player_id=player_id,
                        error=str(e),
                        exc_info=True,
                    )
            else:
                logger.warning("No event bus available for HP correction event", player_id=player_id)

        except Exception as e:
            logger.error(
                "Error publishing HP correction event",
                player_id=player_id,
                error=str(e),
                exc_info=True,
            )
