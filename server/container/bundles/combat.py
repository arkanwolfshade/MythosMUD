"""
Combat bundle: player combat, death, respawn, combat service, catatonia, lucidity flux.

Depends on Core, Realtime (connection_manager), Game (movement_service).
"""

from __future__ import annotations

import uuid as uuid_lib
from typing import TYPE_CHECKING, Any

from anyio import sleep

from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

COMBAT_ATTRS = (
    "player_combat_service",
    "player_death_service",
    "player_respawn_service",
    "combat_service",
    "catatonia_registry",
    "passive_lucidity_flux_service",
)


class CombatBundle:
    """Combat-related services."""

    player_combat_service: Any = None
    player_death_service: Any = None
    player_respawn_service: Any = None
    combat_service: Any = None
    catatonia_registry: Any = None
    passive_lucidity_flux_service: Any = None

    async def _sanitarium_failover_callback(
        self, container: ApplicationContainer, player_id: str, current_lcd: int
    ) -> None:
        """Failover callback that relocates catatonic players to the sanitarium."""
        from server.services.lucidity_service import LucidityService

        await sleep(10.0)

        if container.database_manager is None:
            logger.error("Database manager not available for catatonia failover", player_id=player_id)
            return

        try:
            session_maker = container.database_manager.get_session_maker()
        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as exc:
            logger.error(
                "Failed to get session maker for catatonia failover",
                player_id=player_id,
                error=str(exc),
                exc_info=True,
            )
            return

        async with session_maker() as session:
            try:
                player_id_uuid = uuid_lib.UUID(player_id) if isinstance(player_id, str) else player_id
                lucidity_service = LucidityService(session)
                timers_cleared = await lucidity_service.clear_hallucination_timers(player_id_uuid)
                logger.debug(
                    "Hallucination timers cleared in failover",
                    player_id=player_id,
                    timers_cleared=timers_cleared,
                )

                if self.player_respawn_service is None:
                    logger.error("PlayerRespawnService not available for catatonia failover", player_id=player_id)
                    return

                await self.player_respawn_service.move_player_to_limbo(player_id, "catatonia_failover", session)
                await self.player_respawn_service.respawn_player_from_sanitarium(player_id, session)
                logger.info("Catatonia failover completed", player_id=player_id, lcd=current_lcd)
            except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as exc:
                logger.error("Catatonia failover failed", player_id=player_id, error=str(exc), exc_info=True)
                await session.rollback()

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize combat services."""
        if container.persistence is None:
            raise RuntimeError("Persistence must be initialized before combat services")
        if container.event_bus is None:
            raise RuntimeError("EventBus must be initialized before combat services")
        if container.performance_monitor is None:
            raise RuntimeError("PerformanceMonitor must be initialized before passive_lucidity_flux_service")

        logger.debug("Initializing combat services...")

        from server.services.catatonia_registry import CatatoniaRegistry
        from server.services.passive_lucidity_flux_service import PassiveLucidityFluxService
        from server.services.player_combat_service import PlayerCombatService
        from server.services.player_death_service import PlayerDeathService
        from server.services.player_respawn_service import PlayerRespawnService

        self.player_combat_service = PlayerCombatService(container.persistence, container.event_bus)
        if container.connection_manager is not None:
            container.connection_manager.set_player_combat_service(self.player_combat_service)
        if container.movement_service is not None:
            container.movement_service.set_player_combat_service(self.player_combat_service)
            logger.info("MovementService updated with player_combat_service")
        logger.info("Player combat service initialized")

        self.player_death_service = PlayerDeathService(
            event_bus=container.event_bus, player_combat_service=self.player_combat_service
        )
        logger.info("Player death service initialized")

        self.player_respawn_service = PlayerRespawnService(
            event_bus=container.event_bus, player_combat_service=self.player_combat_service
        )
        logger.info("Player respawn service initialized")

        def failover_cb(pid: str, lcd: Any):
            return self._sanitarium_failover_callback(container, pid, lcd)

        self.catatonia_registry = CatatoniaRegistry(failover_callback=failover_cb)
        logger.info("Catatonia registry initialized")

        self.passive_lucidity_flux_service = PassiveLucidityFluxService(
            persistence=container.async_persistence,
            performance_monitor=container.performance_monitor,
            catatonia_observer=self.catatonia_registry,
        )
        logger.info("Passive lucidity flux service initialized")

        logger.info("All combat services initialized")

    async def initialize_nats_combat(self, container: ApplicationContainer) -> None:
        """Initialize NATS-dependent combat service and start NATS message handler."""
        if container.config is None:
            raise RuntimeError("Config must be initialized before NATS combat service")
        if (
            self.player_combat_service is None
            or self.player_death_service is None
            or self.player_respawn_service is None
        ):
            raise RuntimeError("Combat services must be initialized before NATS combat")
        if container.event_bus is None:
            raise RuntimeError("EventBus must be initialized before combat service")

        logger.debug("Initializing NATS and combat service...")
        is_testing = container.config.logging.environment in ("unit_test", "e2e_test")

        if container.nats_service is not None and container.nats_service.is_connected():
            logger.info("NATS service available from container")
            from server.services.combat_service import CombatService, set_combat_service

            self.combat_service = CombatService(
                self.player_combat_service,
                container.nats_service,
                player_death_service=self.player_death_service,
                player_respawn_service=self.player_respawn_service,
                event_bus=container.event_bus,
            )
            set_combat_service(self.combat_service)

            if container.player_service is None:
                raise RuntimeError("PlayerService must be initialized")
            container.player_service.combat_service = self.combat_service
            container.player_service.player_combat_service = self.player_combat_service
            logger.info("Combat service initialized")

            try:
                if container.nats_message_handler:
                    await container.nats_message_handler.start()
                    logger.info("NATS message handler started successfully from container")
                else:
                    logger.warning("NATS message handler not available (NATS disabled or failed)")
            except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
                logger.error("Error starting NATS message handler", error=str(e))
        else:
            if is_testing:
                logger.warning("NATS service not available in test environment - using mock NATS service")
                self.combat_service = None
            else:
                logger.error("NATS service not available - NATS is required for chat functionality")
                raise RuntimeError("NATS connection failed - NATS is mandatory for chat system")
