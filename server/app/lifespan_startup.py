"""Application startup initialization functions.

This module handles all startup logic for the MythosMUD server,
including container initialization, service setup, and dependency wiring.
"""

import asyncio
from collections.abc import Iterable

from fastapi import FastAPI

from ..container import ApplicationContainer
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_event_consumer import MythosTimeEventConsumer
from ..time.time_service import get_mythos_chronicle

logger = get_logger("server.lifespan.startup")


async def initialize_container_and_legacy_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize container and set up legacy compatibility services on app.state."""
    ApplicationContainer.set_instance(container)

    app.state.container = container
    logger.info("ApplicationContainer initialized and added to app.state")

    app.state.task_registry = container.task_registry
    app.state.event_bus = container.event_bus
    app.state.event_handler = container.real_time_event_handler
    app.state.persistence = container.async_persistence
    app.state.connection_manager = container.connection_manager
    app.state.player_service = container.player_service
    app.state.room_service = container.room_service
    app.state.user_manager = container.user_manager
    app.state.container_service = container.container_service
    app.state.holiday_service = container.holiday_service
    app.state.schedule_service = container.schedule_service
    app.state.room_cache_service = container.room_cache_service
    app.state.profession_cache_service = container.profession_cache_service
    app.state.prototype_registry = container.item_prototype_registry
    app.state.item_factory = container.item_factory

    if container.item_factory is None:
        logger.warning("Item factory unavailable during startup; summon command will be disabled")
    else:
        prototype_count = 0
        registry = container.item_prototype_registry
        if registry is not None:
            all_method = getattr(registry, "all", None)
            if callable(all_method):
                entries = all_method()
                if asyncio.iscoroutine(entries):
                    try:
                        entries = await entries
                    except Exception:  # pylint: disable=broad-exception-caught
                        entries = None
                if isinstance(entries, Iterable):
                    prototype_count = sum(1 for _ in entries)
                elif entries is not None:
                    try:
                        prototype_count = len(entries)
                    except TypeError:
                        logger.debug("Item registry returned non-iterable entries; defaulting prototype count to zero")
            else:
                logger.debug("Item prototype registry missing 'all' method; defaulting prototype count to zero")
        logger.info("Item services ready", prototype_count=prototype_count)


async def setup_connection_manager(app: FastAPI, container: ApplicationContainer) -> None:
    """Set up connection manager with dependencies."""
    if container.connection_manager is None:
        raise RuntimeError("Connection manager not initialized in container")

    container.connection_manager.async_persistence = container.async_persistence
    container.connection_manager.set_event_bus(container.event_bus)
    container.connection_manager.app = app
    container.connection_manager.start_health_checks()
    container.connection_manager.message_queue.pending_messages.clear()
    logger.info("Cleared stale pending messages from previous server sessions")


async def initialize_npc_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize NPC services and load definitions."""
    from ..npc.lifecycle_manager import NPCLifecycleManager
    from ..npc.population_control import NPCPopulationController
    from ..npc.spawning_service import NPCSpawningService
    from ..services.npc_instance_service import initialize_npc_instance_service
    from ..services.npc_service import NPCService

    if container.event_bus is None:
        raise RuntimeError("EventBus must be initialized")
    app.state.npc_spawning_service = NPCSpawningService(container.event_bus, None)
    if container.persistence is None:
        raise RuntimeError("Persistence must be initialized")
    app.state.npc_lifecycle_manager = NPCLifecycleManager(
        event_bus=container.event_bus,
        population_controller=None,
        spawning_service=app.state.npc_spawning_service,
        persistence=container.persistence,
    )
    app.state.npc_population_controller = NPCPopulationController(
        container.event_bus,
        app.state.npc_spawning_service,
        app.state.npc_lifecycle_manager,
        async_persistence=container.async_persistence,
    )
    app.state.npc_spawning_service.population_controller = app.state.npc_population_controller
    app.state.npc_lifecycle_manager.population_controller = app.state.npc_population_controller

    initialize_npc_instance_service(
        lifecycle_manager=app.state.npc_lifecycle_manager,
        spawning_service=app.state.npc_spawning_service,
        population_controller=app.state.npc_population_controller,
        event_bus=container.event_bus,
    )

    from ..npc_database import get_npc_session

    npc_service = NPCService()
    async for npc_session in get_npc_session():
        try:
            definitions = await npc_service.get_npc_definitions(npc_session)
            app.state.npc_population_controller.load_npc_definitions(definitions)
            logger.info("NPC definitions loaded", count=len(definitions))

            spawn_rules = await npc_service.get_spawn_rules(npc_session)
            app.state.npc_population_controller.load_spawn_rules(spawn_rules)
            logger.info("NPC spawn rules loaded", count=len(spawn_rules))
        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
            logger.error("Error loading NPC definitions and spawn rules", error=str(e))
        break

    logger.info("NPC services initialized and added to app.state")

    if hasattr(app.state.npc_lifecycle_manager, "thread_manager"):
        try:
            await app.state.npc_lifecycle_manager.thread_manager.start()
            logger.info("NPC thread manager started")

            if hasattr(app.state.npc_lifecycle_manager, "_pending_thread_starts"):
                # Accessing protected member via getattr() for internal state initialization
                # This is safe as we check existence first and handle gracefully
                pending_starts = getattr(app.state.npc_lifecycle_manager, "_pending_thread_starts", [])  # pylint: disable=protected-access
                for npc_id, definition in pending_starts:
                    try:
                        await app.state.npc_lifecycle_manager.thread_manager.start_npc_thread(npc_id, definition)
                        logger.debug("Started queued NPC thread", npc_id=npc_id)
                    except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
                        logger.warning("Failed to start queued NPC thread", npc_id=npc_id, error=str(e))
                pending_starts.clear()
        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
            logger.error("Failed to start NPC thread manager", error=str(e))


async def initialize_combat_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize combat-related services."""
    from ..services.catatonia_registry import CatatoniaRegistry
    from ..services.passive_lucidity_flux_service import PassiveLucidityFluxService
    from ..services.player_combat_service import PlayerCombatService
    from ..services.player_death_service import PlayerDeathService
    from ..services.player_respawn_service import PlayerRespawnService

    app.state.player_combat_service = PlayerCombatService(container.persistence, container.event_bus)
    if container.connection_manager is not None:
        container.connection_manager.set_player_combat_service(app.state.player_combat_service)
    logger.info("Player combat service initialized")

    app.state.player_death_service = PlayerDeathService(
        event_bus=container.event_bus, player_combat_service=app.state.player_combat_service
    )
    logger.info("Player death service initialized")

    app.state.player_respawn_service = PlayerRespawnService(
        event_bus=container.event_bus, player_combat_service=app.state.player_combat_service
    )
    logger.info("Player respawn service initialized")

    async def _sanitarium_failover(player_id: str, current_lcd: int) -> None:
        """Failover callback that relocates catatonic players to the sanitarium."""
        # 10-second fade before transport per spec
        await asyncio.sleep(10.0)

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
                # Clear all active hallucination timers per spec requirement
                import uuid as uuid_lib

                from ..services.lucidity_service import LucidityService

                player_id_uuid = uuid_lib.UUID(player_id) if isinstance(player_id, str) else player_id
                lucidity_service = LucidityService(session)
                timers_cleared = await lucidity_service.clear_hallucination_timers(player_id_uuid)
                logger.debug(
                    "Hallucination timers cleared in failover",
                    player_id=player_id,
                    timers_cleared=timers_cleared,
                )

                await app.state.player_respawn_service.move_player_to_limbo(player_id, "catatonia_failover", session)
                await app.state.player_respawn_service.respawn_player_from_sanitarium(player_id, session)
                logger.info("Catatonia failover completed", player_id=player_id, lcd=current_lcd)
            except (
                ValueError,
                TypeError,
                AttributeError,
                KeyError,
                RuntimeError,
            ) as exc:  # pragma: no cover - defensive
                logger.error("Catatonia failover failed", player_id=player_id, error=str(exc), exc_info=True)
                await session.rollback()

    app.state.catatonia_registry = CatatoniaRegistry(failover_callback=_sanitarium_failover)
    logger.info("Catatonia registry initialized")

    app.state.passive_lucidity_flux_service = PassiveLucidityFluxService(
        persistence=container.async_persistence,
        performance_monitor=container.performance_monitor,
        catatonia_observer=app.state.catatonia_registry,
    )
    logger.info("Passive lucidity flux service initialized")


async def initialize_mythos_time_consumer(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize Mythos time event consumer."""
    if (
        container.event_bus
        and container.holiday_service
        and container.schedule_service
        and app.state.npc_lifecycle_manager
    ):
        app.state.mythos_time_consumer = MythosTimeEventConsumer(
            event_bus=container.event_bus,
            chronicle=get_mythos_chronicle(),
            holiday_service=container.holiday_service,
            schedule_service=container.schedule_service,
            room_service=container.room_service,
            npc_lifecycle_manager=app.state.npc_lifecycle_manager,
        )
        logger.info("Mythos time consumer initialized and subscribed to hour ticks")
    else:
        logger.warning("Mythos time consumer not initialized due to missing dependencies")


async def initialize_npc_startup_spawning(_app: FastAPI) -> None:
    """Initialize and run NPC startup spawning."""
    from ..services.npc_startup_service import get_npc_startup_service

    logger.info("Starting NPC startup spawning process")
    try:
        startup_service = get_npc_startup_service()
        startup_results = await startup_service.spawn_npcs_on_startup()

        logger.info(
            "NPC startup spawning completed",
            total_spawned=startup_results["total_spawned"],
            required_spawned=startup_results["required_spawned"],
            optional_spawned=startup_results["optional_spawned"],
            failed_spawns=startup_results["failed_spawns"],
            errors=len(startup_results["errors"]),
        )

        if startup_results["errors"]:
            logger.warning("NPC startup spawning had errors", error_count=len(startup_results["errors"]))
            for error in startup_results["errors"]:
                logger.warning("Startup spawning error", error=str(error))
    except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
        logger.error("Critical error during NPC startup spawning", error=str(e))
        logger.warning("Continuing server startup despite NPC spawning errors")

    logger.info("NPC startup spawning completed - NPCs should now be present in the world")


async def initialize_nats_and_combat_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize NATS-dependent services including combat service."""
    if container.config is None:
        raise RuntimeError("Config must be initialized")
    is_testing = container.config.logging.environment in ("unit_test", "e2e_test")

    if container.nats_service is not None and container.nats_service.is_connected():
        logger.info("NATS service available from container")
        app.state.nats_service = container.nats_service

        from ..services.combat_service import CombatService, set_combat_service

        app.state.combat_service = CombatService(
            app.state.player_combat_service,
            container.nats_service,
            player_death_service=app.state.player_death_service,
            player_respawn_service=app.state.player_respawn_service,
            event_bus=container.event_bus,
        )

        set_combat_service(app.state.combat_service)

        if container.player_service is None:
            raise RuntimeError("PlayerService must be initialized")
        container.player_service.combat_service = app.state.combat_service
        container.player_service.player_combat_service = app.state.player_combat_service
        logger.info("Combat service initialized and added to app.state")

        try:
            if container.nats_message_handler:
                await container.nats_message_handler.start()
                app.state.nats_message_handler = container.nats_message_handler
                logger.info("NATS message handler started successfully from container")
            else:
                logger.warning("NATS message handler not available in container (NATS disabled or failed)")
                app.state.nats_message_handler = None
        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
            logger.error("Error starting NATS message handler", error=str(e))
            app.state.nats_message_handler = None
    else:
        if is_testing:
            logger.warning("NATS service not available in test environment - using mock NATS service")
            app.state.nats_service = None
            app.state.nats_message_handler = None
        else:
            logger.error("NATS service not available - NATS is required for chat functionality")
            raise RuntimeError("NATS connection failed - NATS is mandatory for chat system")


async def initialize_chat_service(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize chat service."""
    from ..game.chat_service import ChatService
    from ..services.nats_subject_manager import nats_subject_manager

    if container.config is None:
        raise RuntimeError("Config must be initialized")
    is_testing = container.config.logging.environment in ("unit_test", "e2e_test")

    subject_manager = None
    nats_service = getattr(app.state, "nats_service", None)
    if nats_service and getattr(nats_service, "subject_manager", None):
        subject_manager = nats_service.subject_manager
    else:
        subject_manager = nats_subject_manager

    app.state.chat_service = ChatService(
        persistence=container.persistence,
        room_service=container.persistence,
        player_service=container.player_service,
        nats_service=nats_service,
        user_manager_instance=container.user_manager,
        subject_manager=subject_manager,
    )

    if app.state.chat_service.nats_service and app.state.chat_service.nats_service.is_connected():
        logger.info("Chat service NATS connection verified")
    elif is_testing:
        logger.info("Chat service running in test mode without NATS connection")
    else:
        logger.error("Chat service NATS connection failed")
        raise RuntimeError("Chat service NATS connection failed - NATS is mandatory for chat system")

    logger.info("Chat service initialized")


async def initialize_magic_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize magic system services and wire them to app.state."""
    from ..game.magic.magic_service import MagicService
    from ..game.magic.mp_regeneration_service import MPRegenerationService
    from ..game.magic.spell_effects import SpellEffects
    from ..game.magic.spell_learning_service import SpellLearningService
    from ..game.magic.spell_registry import SpellRegistry
    from ..game.magic.spell_targeting import SpellTargetingService
    from ..persistence.repositories.player_spell_repository import PlayerSpellRepository
    from ..persistence.repositories.spell_repository import SpellRepository as SpellRepositoryClass
    from ..services.target_resolution_service import TargetResolutionService

    logger.info("Initializing magic system services...")

    # Initialize repositories
    spell_repository = SpellRepositoryClass()
    player_spell_repository = PlayerSpellRepository()
    logger.info("Spell repositories initialized")

    # Initialize SpellRegistry and load spells
    spell_registry = SpellRegistry(spell_repository)
    await spell_registry.load_spells()
    spell_count = len(spell_registry._spells)  # pylint: disable=protected-access
    app.state.spell_registry = spell_registry
    logger.info("SpellRegistry initialized and loaded", spell_count=spell_count)

    # Initialize SpellTargetingService (needs TargetResolutionService, CombatService, PlayerCombatService)
    if container.async_persistence is None:
        raise RuntimeError("async_persistence must be initialized before magic services")
    if container.player_service is None:
        raise RuntimeError("player_service must be initialized before magic services")
    # TargetResolutionService accepts both sync and async persistence layers
    # The protocol is too strict for mypy, but the service handles both at runtime
    target_resolution_service = TargetResolutionService(
        persistence=container.async_persistence,  # type: ignore[arg-type]
        player_service=container.player_service,
    )
    spell_targeting_service = SpellTargetingService(
        target_resolution_service=target_resolution_service,
        combat_service=getattr(app.state, "combat_service", None),
        player_combat_service=getattr(app.state, "player_combat_service", None),
    )
    app.state.spell_targeting_service = spell_targeting_service
    logger.info("SpellTargetingService initialized")

    # Initialize SpellEffects (needs PlayerService)
    # player_service is already checked above, but mypy doesn't know that
    if container.player_service is None:
        raise RuntimeError("player_service must be initialized before magic services")
    spell_effects = SpellEffects(player_service=container.player_service)
    app.state.spell_effects = spell_effects
    logger.info("SpellEffects initialized")

    # Initialize SpellLearningService (needs SpellRegistry, PlayerService, PlayerSpellRepository)
    spell_learning_service = SpellLearningService(
        spell_registry=spell_registry,
        player_service=container.player_service,
        player_spell_repository=player_spell_repository,
    )
    app.state.spell_learning_service = spell_learning_service
    logger.info("SpellLearningService initialized")

    # Initialize MPRegenerationService (needs PlayerService)
    mp_regeneration_service = MPRegenerationService(player_service=container.player_service)
    app.state.mp_regeneration_service = mp_regeneration_service
    logger.info("MPRegenerationService initialized")

    # Initialize MagicService (needs all of the above)
    # Get combat_service if available (for combat integration)
    combat_service = getattr(app.state, "combat_service", None)
    magic_service = MagicService(
        spell_registry=spell_registry,
        player_service=container.player_service,
        spell_targeting_service=spell_targeting_service,
        spell_effects=spell_effects,
        player_spell_repository=player_spell_repository,
        spell_learning_service=spell_learning_service,
        combat_service=combat_service,
    )
    app.state.magic_service = magic_service

    # Set magic_service reference in combat_service if available
    if combat_service:
        combat_service.magic_service = magic_service
        logger.info("MagicService linked to CombatService")

    logger.info("MagicService initialized")

    logger.info("All magic system services initialized and added to app.state")
