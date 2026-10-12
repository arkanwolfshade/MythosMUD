"""
Shared base for the player event handler classes.

The respawn and state handlers take the same collaborators; keeping the constructor in one place stops the two
copies drifting apart.
"""

from __future__ import annotations

from structlog.stdlib import BoundLogger

from .connection_manager import ConnectionManager
from .player_event_handlers_utils import PlayerEventHandlerUtils


class PlayerEventHandlerBase:  # pylint: disable=too-few-public-methods  # Reason: Holds collaborators shared by subclasses
    """Holds the collaborators every player event handler needs."""

    connection_manager: ConnectionManager | None
    utils: PlayerEventHandlerUtils
    _logger: BoundLogger

    def __init__(
        self,
        connection_manager: ConnectionManager | None,
        utils: PlayerEventHandlerUtils,
        logger: BoundLogger,
    ) -> None:
        """
        Initialize the shared collaborators.

        Args:
            connection_manager: ConnectionManager instance
            utils: PlayerEventHandlerUtils instance
            logger: Logger instance
        """
        self.connection_manager = connection_manager
        self.utils = utils
        self._logger = logger
