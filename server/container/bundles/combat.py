"""
Combat bundle: player combat, death, respawn, combat service, catatonia, lucidity flux.

Depends on Core, Realtime (connection_manager), Game (movement_service).
"""

# pyright: reportImportCycles=false
# Reason: container/main.py imports this module (function-scoped) to construct CombatBundle;
# this file only imports ApplicationContainer under TYPE_CHECKING for parameter annotations.
# Same precedent as server/models/player.py and server/services/combat_service.py.

from __future__ import annotations

import uuid as uuid_lib
from collections.abc import Awaitable
from typing import TYPE_CHECKING, Any, cast

from anyio import sleep

from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.async_persistence import AsyncPersistenceLayer, LucidityAdjuster, LucidityReader
    from server.container.main import ApplicationContainer
    from server.game.player_registry import PlayerRegistry
    from server.services.lucidity_helpers import CatatoniaObserverProtocol
    from server.services.passive_corruption_flux.service import PassiveCorruptionFluxService
    from server.services.player_combat_service import PlayerCombatService
    from server.services.player_respawn_service import PlayerRespawnService

logger = get_logger(__name__)

COMBAT_ATTRS = (
    "player_combat_service",
    "player_death_service",
    "player_respawn_service",
    "combat_service",
    "catatonia_registry",
    "passive_lucidity_flux_service",
    "passive_corruption_flux_service",
)


def make_lucidity_adjuster(registry: PlayerRegistry, observer: CatatoniaObserverProtocol | None) -> LucidityAdjuster:
    """Apply one lucidity adjustment through LucidityService on the player registry (ADR-029 step 5b-i)."""
    from server.services.lucidity_service import LucidityService

    service = LucidityService(registry, catatonia_observer=observer)

    async def adjust(player_id: uuid_lib.UUID, delta: int, reason_code: str) -> None:
        _ = await service.apply_lucidity_adjustment(player_id, delta, reason_code=reason_code)

    return adjust


def make_lucidity_reader(registry: PlayerRegistry) -> LucidityReader:
    """Read a player's LCD from the player registry, or the starting value if there is no such player."""
    from server.constants.lucidity import STARTING_LCD

    async def read(player_id: uuid_lib.UUID) -> int:
        player = await registry.get(player_id)
        return player.lucidity.lcd if player is not None else STARTING_LCD

    return read


class CombatBundle:
    """Combat-related services."""

    player_combat_service: Any = None
    player_death_service: Any = None
    player_respawn_service: Any = None
    combat_service: Any = None
    catatonia_registry: Any = None
    passive_lucidity_flux_service: Any = None
    passive_corruption_flux_service: PassiveCorruptionFluxService | None = None

    async def _sanitarium_failover_callback(
        self, container: ApplicationContainer, player_id: str, current_lcd: int
    ) -> None:
        """Failover callback that relocates catatonic players to the sanitarium (registry units, ADR-029 step 6a)."""
        await sleep(10.0)

        try:
            player_id_uuid = uuid_lib.UUID(player_id)
            timers_cleared = 0
            if container.player_registry is not None:
                # Every hallucination timer (the old LIKE 'hallucination_%'): the player wakes in the sanitarium.
                async with container.player_registry.mutate(player_id_uuid) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                    timers_cleared = player.cooldowns.clear_prefix("hallucination_")
            logger.debug(
                "Hallucination timers cleared in failover",
                player_id=player_id,
                timers_cleared=timers_cleared,
            )

            respawn = cast("PlayerRespawnService | None", self.player_respawn_service)
            if respawn is None:
                logger.error("PlayerRespawnService not available for catatonia failover", player_id=player_id)
                return

            _ = await respawn.move_player_to_limbo(player_id_uuid, "catatonia_failover")
            _ = await respawn.respawn_player_from_sanitarium(player_id_uuid)
            logger.info("Catatonia failover completed", player_id=player_id, lcd=current_lcd)
        # LookupError: KeyError, and the registry's PlayerNotFoundError (a player deleted during the wait).
        except (ValueError, TypeError, AttributeError, LookupError, RuntimeError) as exc:
            logger.error("Catatonia failover failed", player_id=player_id, error=str(exc), exc_info=True)

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize combat services."""
        if container.persistence is None:
            raise RuntimeError("Persistence must be initialized before combat services")
        if container.event_bus is None:
            raise RuntimeError("EventBus must be initialized before combat services")
        if container.performance_monitor is None:
            raise RuntimeError("PerformanceMonitor must be initialized before passive_lucidity_flux_service")

        logger.debug("Initializing combat services...")

        from server.game.first_exposure import make_first_exposure_finish
        from server.services.catatonia_registry import CatatoniaRegistry
        from server.services.passive_lucidity_flux_service import PassiveLucidityFluxService
        from server.services.player_combat_service import PlayerCombatService
        from server.services.player_death_service import PlayerDeathService
        from server.services.player_respawn_service import PlayerRespawnService

        self.player_combat_service = PlayerCombatService(
            cast(object, container.persistence),
            cast(object, container.event_bus),
            level_service=cast(object, container.level_service),
        )
        if container.connection_manager is not None:
            container.connection_manager.set_player_combat_service(self.player_combat_service)
        if container.movement_service is not None:
            container.movement_service.set_player_combat_service(self.player_combat_service)
            logger.info("MovementService updated with player_combat_service")
        logger.info("Player combat service initialized")

        self.player_death_service = PlayerDeathService(
            event_bus=container.event_bus,
            player_combat_service=self.player_combat_service,
            async_persistence=container.async_persistence,
            player_registry=container.player_registry,
        )
        logger.info("Player death service initialized")

        # player_combat_service / async_persistence are declared Any; narrow them at this boundary.
        respawn_combat = cast("PlayerCombatService | None", self.player_combat_service)
        respawn_rooms = cast("AsyncPersistenceLayer | None", container.async_persistence)
        self.player_respawn_service = PlayerRespawnService(
            event_bus=container.event_bus,
            player_combat_service=respawn_combat,
            room_lookup=respawn_rooms.get_room_by_id if respawn_rooms else None,
            first_exposure_finish=make_first_exposure_finish(container),
            player_registry=container.player_registry,
        )
        logger.info("Player respawn service initialized")

        def failover_cb(pid: str, lcd: int) -> Awaitable[None]:
            return self._sanitarium_failover_callback(container, pid, lcd)

        self.catatonia_registry = CatatoniaRegistry(failover_callback=failover_cb)
        logger.info("Catatonia registry initialized")
        # Lucidity read and changed through the persistence layer (combat, spells, look, status) goes through the player
        # registry, like every other lucidity access (ADR-029 step 5b-i).
        persistence = cast("AsyncPersistenceLayer | None", container.async_persistence)
        player_registry = container.player_registry
        if persistence is not None and player_registry is not None:
            observer = cast("CatatoniaObserverProtocol", self.catatonia_registry)
            persistence.set_lucidity_adjuster(make_lucidity_adjuster(player_registry, observer))
            persistence.set_lucidity_reader(make_lucidity_reader(player_registry))
            # Corruption changed through the persistence layer (spells, mechanics) too (step 5c).
            from server.services.corruption_service import CorruptionService
            from server.services.player_health_service import PlayerHealthService

            persistence.set_corruption_service(CorruptionService(player_registry))
            # And DP: damage and healing from ticks, mechanics and spells (step 6a).
            persistence.set_health_service(PlayerHealthService(player_registry))

        self.passive_lucidity_flux_service = PassiveLucidityFluxService(
            persistence=container.async_persistence,
            performance_monitor=container.performance_monitor,
            catatonia_observer=self.catatonia_registry,
            player_registry=player_registry,
        )
        logger.info("Passive lucidity flux service initialized")

        from server.services.passive_corruption_flux.service import PassiveCorruptionFluxService

        # container.async_persistence is declared `Any` on ApplicationContainer (a cross-cutting
        # namespace shared by every bundle); it is always a real AsyncPersistenceLayer by
        # construction -- same precedent as container/bundles/npc.py's event_bus cast.
        async_persistence = cast("AsyncPersistenceLayer", container.async_persistence)
        self.passive_corruption_flux_service = PassiveCorruptionFluxService(
            persistence=async_persistence, player_registry=player_registry
        )
        logger.info("Passive corruption flux service initialized")

        logger.info("All combat services initialized")

    def _validate_nats_combat_prerequisites(self, container: ApplicationContainer) -> None:
        """Raise if prerequisites for NATS combat are missing."""
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

    async def _create_combat_service_with_nats(self, container: ApplicationContainer) -> None:
        """Create CombatService with NATS and register it. Assumes NATS is connected."""
        from server.services.combat_service import CombatService, PlayerLifecycleServices, set_combat_service

        combat_service = CombatService(
            self.player_combat_service,
            container.nats_service,
            player_lifecycle_services=PlayerLifecycleServices(
                self.player_death_service,
                self.player_respawn_service,
            ),
            event_bus=container.event_bus,
        )
        combat_service.skill_service = container.skill_service  # graded taunt rolls (#833)
        combat_service.player_registry = container.player_registry
        self.combat_service = combat_service
        set_combat_service(self.combat_service)
        if container.player_service is None:
            raise RuntimeError("PlayerService must be initialized")
        container.player_service.combat_service = self.combat_service
        container.player_service.player_combat_service = self.player_combat_service

    async def _start_nats_message_handler(self, container: ApplicationContainer) -> None:
        """Start NATS message handler if available. Logs and swallows errors."""
        try:
            if container.nats_message_handler:
                await container.nats_message_handler.start()
                logger.info("NATS message handler started successfully from container")
            else:
                logger.warning("NATS message handler not available (NATS disabled or failed)")
        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
            logger.error("Error starting NATS message handler", error=str(e))

    def _handle_nats_unavailable(self, is_testing: bool) -> None:
        """Handle case when NATS is not connected. Raises in prod, sets combat_service to None in tests."""
        if is_testing:
            logger.warning("NATS service not available in test environment - using mock NATS service")
            self.combat_service = None
        else:
            logger.error("NATS service not available - NATS is required for chat functionality")
            raise RuntimeError("NATS connection failed - NATS is mandatory for chat system")

    async def initialize_nats_combat(self, container: ApplicationContainer) -> None:
        """Initialize NATS-dependent combat service and start NATS message handler."""
        self._validate_nats_combat_prerequisites(container)
        logger.debug("Initializing NATS and combat service...")
        is_testing = container.config.logging.environment == "unit_test"

        if container.nats_service is not None and container.nats_service.is_connected():
            logger.info("NATS service available from container")
            await self._create_combat_service_with_nats(container)
            logger.info("Combat service initialized")
            await self._start_nats_message_handler(container)
        else:
            self._handle_nats_unavailable(is_testing)
