"""
Chat bundle: chat service.

Depends on Core (config, persistence), Game (player_service, user_manager),
Realtime (nats_service).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

CHAT_ATTRS = ("chat_service",)


class ChatBundle:  # pylint: disable=too-few-public-methods
    """Chat service."""

    chat_service: Any = None

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize chat service."""
        if container.config is None:
            raise RuntimeError("Config must be initialized before chat service")
        if container.persistence is None:
            raise RuntimeError("Persistence must be initialized before chat service")
        if container.player_service is None:
            raise RuntimeError("PlayerService must be initialized before chat service")
        if container.user_manager is None:
            raise RuntimeError("UserManager must be initialized before chat service")

        logger.debug("Initializing chat service...")

        from server.game.chat_service import ChatService
        from server.services.nats_subject_manager import nats_subject_manager

        is_testing = container.config.logging.environment in (  # pylint: disable=no-member
            "unit_test",
            "e2e_test",
        )

        subject_manager = None
        nats_service = container.nats_service
        if nats_service and getattr(nats_service, "subject_manager", None):
            subject_manager = nats_service.subject_manager
        else:
            subject_manager = nats_subject_manager

        self.chat_service = ChatService(
            persistence=container.persistence,
            room_service=container.persistence,
            player_service=container.player_service,
            nats_service=nats_service,
            user_manager_instance=container.user_manager,
            subject_manager=subject_manager,
        )

        if self.chat_service.nats_service and self.chat_service.nats_service.is_connected():
            logger.info("Chat service NATS connection verified")
        elif is_testing:
            logger.info("Chat service running in test mode without NATS connection")
        else:
            logger.error("Chat service NATS connection failed")
            raise RuntimeError("Chat service NATS connection failed - NATS is mandatory for chat system")

        logger.info("Chat service initialized")
