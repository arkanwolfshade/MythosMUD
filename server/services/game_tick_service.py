"""
GameTickService for MythosMUD.
Handles the game tick system that runs at regular intervals.
"""

import asyncio
from datetime import UTC, datetime

from ..app.tracked_task_manager import get_global_tracked_manager
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("services.game_tick_service")


class GameTickService:
    """
    Service that manages the game tick system.

    The game tick system runs at regular intervals (default 10 seconds)
    and publishes game_tick events via the EventPublisher.
    """

    def __init__(self, event_publisher, tick_interval: float = 10.0):
        """
        Initialize the GameTickService.

        Args:
            event_publisher: EventPublisher instance for publishing events
            tick_interval: Interval between ticks in seconds (default: 10.0)
        """
        self.event_publisher = event_publisher
        self.tick_interval = tick_interval
        self.is_running = False
        self.tick_count = 0
        self._tick_task: asyncio.Task | None = None

    async def start(self) -> bool:
        """
        Start the game tick service.

        Returns:
            bool: True if started successfully, False otherwise
        """
        if self.is_running:
            logger.warning("GameTickService is already running")
            return True

        try:
            # Task 4.4: Replace with tracked task creation to prevent memory leaks
            tracked_manager = get_global_tracked_manager()
            self._tick_task = tracked_manager.create_tracked_task(
                self._tick_loop(), task_name="gametick_service/tick_loop", task_type="system_lifecycle"
            )
            self.is_running = True
            logger.info("GameTickService started", tick_interval=self.tick_interval)
            return True
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Service startup errors unpredictable, must return False to indicate failure without crashing application
            logger.error("Failed to start GameTickService", error=str(e))
            return False

    async def stop(self) -> bool:
        """
        Stop the game tick service.

        Returns:
            bool: True if stopped successfully, False otherwise
        """
        if not self.is_running:
            logger.warning("GameTickService is not running")
            return True

        try:
            self.is_running = False

            if self._tick_task and not self._tick_task.done():
                self._tick_task.cancel()
                try:
                    await self._tick_task
                except asyncio.CancelledError:
                    pass

            self._tick_task = None
            logger.info("GameTickService stopped")
            return True
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Service shutdown errors unpredictable, must return False to indicate failure without crashing application
            logger.error("Failed to stop GameTickService", error=str(e))
            return False

    async def _tick_loop(self):
        """
        Main tick loop that runs at the specified interval.
        """
        logger.info("Game tick loop started")

        while self.is_running:
            try:
                # Increment tick count
                self.tick_count += 1

                # Create timestamp for this tick
                timestamp = datetime.now(UTC).isoformat()

                # Create additional metadata for this tick
                additional_metadata = {
                    "tick_number": self.tick_count,
                    "tick_interval": self.tick_interval,
                    "service_start_time": datetime.now(UTC).isoformat(),
                }

                # Publish the game tick event
                success = await self.event_publisher.publish_game_tick_event(
                    timestamp=timestamp, additional_metadata=additional_metadata
                )

                if success:
                    logger.debug("Published game tick event", tick_count=self.tick_count)
                else:
                    logger.warning("Failed to publish game tick event", tick_count=self.tick_count)

                # Wait for the next tick
                await asyncio.sleep(self.tick_interval)

            except asyncio.CancelledError:
                logger.info("Game tick loop cancelled")
                break
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Continue loop on error to maintain game tick, errors are logged but must not stop the core game mechanics
                logger.error("Error in game tick loop", error=str(e))
                # Continue the loop even if there's an error
                await asyncio.sleep(self.tick_interval)

        logger.info("Game tick loop ended")

    def get_tick_count(self) -> int:
        """
        Get the current tick count.

        Returns:
            int: Current number of ticks processed
        """
        return self.tick_count

    def reset_tick_count(self) -> None:
        """
        Reset the tick count to zero.
        """
        self.tick_count = 0
        logger.info("Game tick count reset to 0")

    def get_tick_interval(self) -> float:
        """
        Get the current tick interval.

        Returns:
            float: Current tick interval in seconds
        """
        return self.tick_interval

    def set_tick_interval(self, interval: float) -> None:
        """
        Set a new tick interval.

        Args:
            interval: New tick interval in seconds
        """
        if interval <= 0:
            raise ValueError("Tick interval must be positive")

        self.tick_interval = interval
        logger.info("Game tick interval set", interval=interval)

    def is_service_running(self) -> bool:
        """
        Check if the service is currently running.

        Returns:
            bool: True if running, False otherwise
        """
        return self.is_running
