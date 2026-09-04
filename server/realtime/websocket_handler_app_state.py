"""
WebSocket app.state / container service wiring for command processing.

Extracted from websocket_handler to reduce file size and cyclomatic complexity (Lizard).
"""

from typing import TYPE_CHECKING, cast

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from .request_context import WebSocketRequestContext

logger: BoundLogger = get_logger(__name__)


def _services_from_container(app_state: object) -> tuple[object | None, object | None]:
    """Read player_service and user_manager from app_state.container."""
    container = cast(object | None, getattr(app_state, "container", None))
    if container is None:
        return None, None
    player_service = cast(object | None, getattr(container, "player_service", None))
    user_manager = cast(object | None, getattr(container, "user_manager", None))
    return player_service, user_manager


def _mirror_service_to_app_state(app_state: object, attr: str, service: object | None) -> None:
    """Copy container service onto app.state if missing."""
    if not service:
        return
    if hasattr(app_state, attr) and getattr(app_state, attr, None):
        return
    setattr(app_state, attr, service)
    logger.debug("service mirrored to app.state from container", attr=attr)


def resolve_and_setup_app_state_services(
    app_state: object | None, request_context: "WebSocketRequestContext"
) -> tuple[object | None, object | None]:
    """
    Resolve player_service and user_manager from container or app.state.

    Mutates app_state when services exist on container but not on state.
    """
    player_service: object | None = None
    user_manager: object | None = None

    if app_state and getattr(app_state, "container", None):
        player_service, user_manager = _services_from_container(app_state)
        _mirror_service_to_app_state(app_state, "player_service", player_service)
        _mirror_service_to_app_state(app_state, "user_manager", user_manager)
    elif app_state:
        player_service = getattr(app_state, "player_service", None)
        user_manager = getattr(app_state, "user_manager", None)

    if player_service and user_manager:
        request_context.set_app_state_services(player_service, user_manager)

    logger.debug("App state services available", player_service=player_service, user_manager=user_manager)
    if not player_service or not user_manager:
        logger.warning("Missing required app state services - player_service or user_manager not available")

    return player_service, user_manager
