"""Shared mock wiring for communication command unit tests."""

from unittest.mock import MagicMock


def request_with_app_container() -> tuple[MagicMock, MagicMock]:
    """Return (request, container) with request.app.state.container wired.

    Typed MagicMocks avoid reportAny on chained .app.state.container access in tests.
    """
    request = MagicMock()
    app: MagicMock = MagicMock()
    state: MagicMock = MagicMock()
    container: MagicMock = MagicMock()
    request.app = app
    app.state = state
    state.container = container
    return request, container
