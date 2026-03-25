"""
Login grace-period checks for NPC combat integration (extracted to keep service file smaller).
"""

import uuid
from typing import cast
from uuid import UUID

from structlog.stdlib import BoundLogger

from ..config import get_app_instance
from ..realtime.connection_manager import ConnectionManager
from ..realtime.login_grace_period import is_player_in_login_grace_period
from ..structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


def _connection_manager_from_config_app() -> ConnectionManager | None:
    """
    Resolve connection_manager from the public config app accessor.

    Uses getattr on object-typed locals so basedpyright does not treat app.state as Any.
    """
    app_obj: object | None = get_app_instance()
    if app_obj is None:
        return None
    state_obj: object | None = getattr(app_obj, "state", None)
    if state_obj is None:
        return None
    return cast(
        ConnectionManager | None,
        getattr(state_obj, "connection_manager", None),
    )


def is_player_attack_blocked_by_login_grace_period(player_id: str) -> bool:
    """
    True if the player should not attack (in login grace period). Fail-open on config errors.
    """
    try:
        connection_manager = _connection_manager_from_config_app()
        if not connection_manager:
            return False
        player_uuid = uuid.UUID(player_id)
        return bool(is_player_in_login_grace_period(player_uuid, connection_manager))
    except (AttributeError, ImportError, TypeError, ValueError) as e:
        logger.debug("Could not check login grace period for player attack", player_id=player_id, error=str(e))
        return False


def is_npc_attack_on_player_blocked_by_login_grace_period(target_uuid: UUID) -> bool:
    """
    True if NPC attack on this player should be blocked (player in login grace period).
    """
    try:
        conn_mgr = _connection_manager_from_config_app()
        if not conn_mgr:
            return False
        return bool(is_player_in_login_grace_period(target_uuid, conn_mgr))
    except (AttributeError, ImportError, TypeError, ValueError) as e:
        logger.debug("Could not check login grace period for NPC attack", error=str(e))
        return False
