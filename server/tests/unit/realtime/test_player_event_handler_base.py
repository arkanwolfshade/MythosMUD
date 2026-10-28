"""The respawn and state handlers share one constructor, PlayerEventHandlerBase.

Production builds both handlers with keyword arguments (PlayerEventHandler._initialize_handlers) while the
handler tests build them positionally, so this pins that both call styles keep working after the constructor
moved out of the two classes.
"""

from typing import cast
from unittest.mock import MagicMock

import pytest
from structlog.stdlib import BoundLogger

from server.realtime.connection_manager import ConnectionManager
from server.realtime.player_event_handler_base import PlayerEventHandlerBase
from server.realtime.player_event_handlers_respawn import PlayerRespawnEventHandler
from server.realtime.player_event_handlers_state import PlayerStateEventHandler
from server.realtime.player_event_handlers_utils import PlayerEventHandlerUtils

_HANDLERS: list[type[PlayerEventHandlerBase]] = [PlayerRespawnEventHandler, PlayerStateEventHandler]


def _collaborators() -> tuple[ConnectionManager, PlayerEventHandlerUtils, BoundLogger]:
    """Stand-ins for the three collaborators; the constructor only stores them."""
    return (
        cast(ConnectionManager, cast(object, MagicMock())),
        cast(PlayerEventHandlerUtils, cast(object, MagicMock())),
        cast(BoundLogger, cast(object, MagicMock())),
    )


@pytest.mark.parametrize("handler_cls", _HANDLERS)
def test_handler_builds_from_keyword_arguments_like_production(handler_cls: type[PlayerEventHandlerBase]) -> None:
    connection_manager, utils, logger = _collaborators()

    handler = handler_cls(connection_manager=connection_manager, utils=utils, logger=logger)

    assert isinstance(handler, PlayerEventHandlerBase)
    assert handler.connection_manager is connection_manager
    assert handler.utils is utils


@pytest.mark.parametrize("handler_cls", _HANDLERS)
def test_handler_builds_from_positional_arguments_like_the_handler_tests(
    handler_cls: type[PlayerEventHandlerBase],
) -> None:
    connection_manager, utils, logger = _collaborators()

    handler = handler_cls(connection_manager, utils, logger)

    assert handler.connection_manager is connection_manager
    assert handler.utils is utils


@pytest.mark.parametrize("handler_cls", _HANDLERS)
def test_handler_accepts_a_missing_connection_manager(handler_cls: type[PlayerEventHandlerBase]) -> None:
    """The collaborator is optional: handlers must still be constructible without a connection manager."""
    _, utils, logger = _collaborators()

    handler = handler_cls(None, utils, logger)

    assert handler.connection_manager is None
    assert handler.utils is utils
