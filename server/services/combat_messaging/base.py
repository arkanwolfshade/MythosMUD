"""Base integration with connection manager resolution."""

from typing import Any

from server.services.combat_messaging_service import CombatMessagingService
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class HasConnectionManager:
    """Base for mixins that require connection_manager. Satisfies mypy attr-defined checks."""

    connection_manager: Any  # Provided by CombatMessagingBase when mixed in


def log_room_broadcast_result(action: str, room_id: str, broadcast_stats: dict[str, Any]) -> None:
    """
    Log a room broadcast's outcome -- error-level on any failed delivery, debug-level otherwise.

    broadcast_to_room never raises on individual delivery failures (#634); this is the floor that
    keeps a dropped combat broadcast from being invisible outside a debug log.
    """
    failed = broadcast_stats.get("failed_deliveries", 0)
    if failed:
        logger.error("Broadcast had failed deliveries", action=action, room_id=room_id, broadcast_stats=broadcast_stats)
    else:
        logger.debug("Broadcast completed", action=action, room_id=room_id, broadcast_stats=broadcast_stats)


class CombatMessagingBase:
    """Base class with connection manager setup. Used by CombatMessagingIntegration."""

    def __init__(self, connection_manager: Any = None) -> None:
        self.messaging_service = CombatMessagingService()
        self._connection_manager = None
        if connection_manager is not None:
            self.connection_manager = connection_manager

    def _resolve_connection_manager_from_container(self) -> Any:
        """Lazily resolve the connection manager from the application container."""
        try:
            from server.container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            connection_manager = getattr(container, "connection_manager", None)
            if connection_manager is None:
                raise RuntimeError("Application container does not have an initialized connection_manager")
            return connection_manager
        except (ImportError, AttributeError, RuntimeError, ValueError) as exc:
            logger.error(
                "Failed to resolve connection manager from container",
                error=str(exc),
            )
            raise RuntimeError("Connection manager is not available") from exc

    @property
    def connection_manager(self) -> Any:
        """Return the connection manager, resolving it from the application container if needed."""
        if self._connection_manager is None:
            self._connection_manager = self._resolve_connection_manager_from_container()
        return self._connection_manager

    @connection_manager.setter
    def connection_manager(self, value: Any) -> None:
        """Explicitly set the connection manager (primarily used in tests)."""
        self._connection_manager = value
