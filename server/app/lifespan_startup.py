"""Application startup initialization functions.

This module handles all startup logic for the MythosMUD server,
including container initialization, service setup, and dependency wiring.
"""

import asyncio
import logging as stdlib_logging
import uuid as uuid_lib
from collections.abc import Iterable
from typing import Any

from anyio import sleep
from fastapi import FastAPI

from ..container import ApplicationContainer
from ..game.chat_service import ChatService
from ..npc.lifecycle_manager import NPCLifecycleManager
from ..npc.population_control import NPCPopulationController
from ..npc.spawning_service import NPCSpawningService
from ..npc_database import get_npc_session
from ..services.catatonia_registry import CatatoniaRegistry
from ..services.lucidity_service import LucidityService
from ..services.nats_subject_manager import nats_subject_manager
from ..services.npc_instance_service import initialize_npc_instance_service
from ..services.npc_service import NPCService
from ..services.npc_startup_service import get_npc_startup_service
from ..services.passive_lucidity_flux_service import PassiveLucidityFluxService
from ..services.player_combat_service import PlayerCombatService
from ..services.player_death_service import PlayerDeathService
from ..services.player_respawn_service import PlayerRespawnService
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_event_consumer import MythosTimeEventConsumer
from ..time.time_service import get_mythos_chronicle

logger = get_logger("server.lifespan.startup")


async def _get_item_prototype_entries(registry: Any) -> Any:
    """Return raw entries from the item prototype registry, or None on error."""
    if registry is None:
        return None
    all_method = getattr(registry, "all", None)
    if not callable(all_method):
        logger.debug("Item prototype registry missing 'all' method; defaulting prototype count to zero")
        return None
    entries = all_method()
    if asyncio.iscoroutine(entries):
        try:
            entries = await entries
        except Exception:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Startup code must handle all exceptions gracefully to prevent application failure during initialization. Item registry errors are non-critical and should not block startup.
            return None
    return entries


async def _get_item_prototype_count(registry: Any) -> int:
    """Get count of item prototypes from registry."""
    entries = await _get_item_prototype_entries(registry)
    if isinstance(entries, Iterable):
        return sum(1 for _ in entries)
    if entries is None:
        return 0
    try:
        return len(entries)
    except TypeError:
        logger.debug("Item registry returned non-iterable entries; defaulting prototype count to zero")
        return 0


def _legacy_service_bindings(container: ApplicationContainer) -> list[tuple[str, Any, str]]:
    """Return (app.state attr, service value, display name) for legacy service bindings."""
    return [
        ("player_service", container.player_service, "Player service"),
        ("user_manager", container.user_manager, "User manager"),
        ("persistence", container.persistence, "Persistence"),
        ("item_factory", container.item_factory, "Item factory"),
        ("prototype_registry", container.item_prototype_registry, "Prototype registry"),
        ("connection_manager", container.connection_manager, "Connection manager"),
        ("chat_service", container.chat_service, "Chat service"),
        ("magic_service", container.magic_service, "Magic service"),
        ("spell_registry", container.spell_registry, "Spell registry"),
        ("spell_learning_service", container.spell_learning_service, "Spell learning service"),
    ]


async def _set_legacy_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Set services on app.state for backward compatibility."""
    for state_attr, service, name in _legacy_service_bindings(container):
        if service is not None:
            setattr(app.state, state_attr, service)
            logger.debug("Legacy service set on app.state", service_name=name)
        else:
            logger.warning("Service not available in container during initialization", service_name=name)


async def initialize_container_and_legacy_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize container and set up container reference on app.state.

    Services are now accessed exclusively via app.state.container.* or dependency injection.
    The dual storage pattern has been removed - all services are in the container only.

    However, some legacy command handlers still expect services directly on app.state,
    so we set them here for backward compatibility.
    """
    ApplicationContainer.set_instance(container)

    app.state.container = container
    # BUGFIX: Combat turn processor and other services use config._app_instance to access
    # the container for weapon damage resolution. Without this, round attacks fall back to
    # basic_unarmed_damage instead of using equipped weapon damage.
    from ..config import get_config

    config = get_config()
    object.__setattr__(config, "_app_instance", app)
    # When NATS TLS is enabled but verification is off (self-signed local certs), suppress nats-py
    # "TLS verification disabled - using unverified certificates" so it does not fill warnings.log
    nats_cfg = getattr(config, "nats", None)
    if nats_cfg and getattr(nats_cfg, "tls_enabled", False) and not getattr(nats_cfg, "tls_verify", True):
        stdlib_logging.getLogger("nats").setLevel(stdlib_logging.ERROR)
    logger.info("ApplicationContainer initialized and added to app.state")

    # Set services on app.state for backward compatibility with legacy command handlers
    # that access app.state.user_manager and app.state.player_service directly
    # This fixes Bugs #1 and #3 where State object was missing these attributes
    await _set_legacy_services(app, container)

    if container.item_factory is None:
        logger.warning("Item factory unavailable during startup; summon command will be disabled")
    else:
        registry = container.item_prototype_registry
        prototype_count = await _get_item_prototype_count(registry)
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

    from .lifespan_event_subscriptions import subscribe_quest_events, subscribe_room_occupants_refresh

    subscribe_room_occupants_refresh(container)
    subscribe_quest_events(container)


def _validate_npc_services_prerequisites(container: ApplicationContainer) -> None:
    """Raise if prerequisites for NPC services are missing."""
    if container.event_bus is None:
        raise RuntimeError("EventBus must be initialized")
    if container.persistence is None:
        raise RuntimeError("Persistence must be initialized")


def _create_npc_services_on_app(app: FastAPI, container: ApplicationContainer) -> None:
    """Create NPC spawning, lifecycle, population services and instance service. Attach to app.state."""
    app.state.npc_spawning_service = NPCSpawningService(container.event_bus, None)
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


async def _load_npc_definitions_and_rules(app: FastAPI) -> None:
    """Load NPC definitions and spawn rules from first NPC session. Single iteration then break."""
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


async def _start_npc_thread_manager_and_pending(app: FastAPI) -> None:
    """Start NPC thread manager and process any pending thread starts. Logs and swallows errors."""
    if not hasattr(app.state.npc_lifecycle_manager, "thread_manager"):
        return
    try:
        await app.state.npc_lifecycle_manager.thread_manager.start()
        logger.info("NPC thread manager started")
        if not hasattr(app.state.npc_lifecycle_manager, "_pending_thread_starts"):
            return
        pending_starts = getattr(app.state.npc_lifecycle_manager, "_pending_thread_starts", [])  # pylint: disable=protected-access  # Reason: Accessing internal state for startup initialization, existence checked first and handled gracefully
        for npc_id, definition in pending_starts:
            try:
                await app.state.npc_lifecycle_manager.thread_manager.start_npc_thread(npc_id, definition)
                logger.debug("Started queued NPC thread", npc_id=npc_id)
            except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
                logger.warning("Failed to start queued NPC thread", npc_id=npc_id, error=str(e))
        pending_starts.clear()
    except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
        logger.error("Failed to start NPC thread manager", error=str(e))


async def initialize_npc_services(app: FastAPI, container: ApplicationContainer) -> None:
    """
    Initialize NPC services and load definitions.

    DEPRECATED: This function is no longer called. NPC services are now initialized
    in ApplicationContainer.initialize() via _initialize_npc_services().
    This function is kept for backward compatibility but should not be used.
    """
    _validate_npc_services_prerequisites(container)
    _create_npc_services_on_app(app, container)
    await _load_npc_definitions_and_rules(app)
    logger.info("NPC services initialized and added to app.state")
    await _start_npc_thread_manager_and_pending(app)


async def initialize_combat_services(app: FastAPI, container: ApplicationContainer) -> None:
    """
    Initialize combat-related services.

    DEPRECATED: This function is no longer called. Combat services are now initialized
    in ApplicationContainer.initialize() via _initialize_combat_services().
    This function is kept for backward compatibility but should not be used.
    """
    app.state.player_combat_service = PlayerCombatService(container.persistence, container.event_bus)
    if container.connection_manager is not None:
        container.connection_manager.set_player_combat_service(app.state.player_combat_service)
    # Update MovementService with combat service if it exists
    if hasattr(container, "movement_service") and container.movement_service is not None:
        container.movement_service.set_player_combat_service(app.state.player_combat_service)
        logger.info("MovementService updated with player_combat_service")
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
                # Clear all active hallucination timers per spec requirement
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
    """
    Initialize Mythos time event consumer.

    DEPRECATED: This function is no longer called. Mythos time consumer is now initialized
    in ApplicationContainer.initialize() via _initialize_mythos_time_consumer().
    This function is kept for backward compatibility but should not be used.
    """
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


async def _ensure_room_cache_before_npc_startup() -> None:
    """Ensure room cache is loaded before NPC startup; raise in production if empty."""
    container = ApplicationContainer.get_instance()
    if not container or not getattr(container, "async_persistence", None) or not container.async_persistence:
        return
    logger.debug("Ensuring room cache is loaded before NPC startup")
    await container.async_persistence.warmup_room_cache()
    cache_size = len(container.async_persistence._room_cache)  # pylint: disable=protected-access  # Reason: Need to verify cache was loaded for NPC startup
    if cache_size:
        logger.debug("Room cache loaded successfully", cache_size=cache_size)
        return
    env = getattr(container.config.logging, "environment", "local") if container.config else "local"
    if env == "production":
        logger.error(
            "Room cache is empty after warmup - rooms table has no data. "
            "Populate world data: run scripts/load_world_seed.py (with DATABASE_URL) or "
            "psql -d your_db -f data/db/mythos_dev_dml.sql (or mythos_unit_dml.sql / mythos_e2e_dml.sql). See db/README.md.",
            cache_size=cache_size,
            cache_loaded=container.async_persistence._room_cache_loaded,  # pylint: disable=protected-access  # Reason: Need to check cache load status
        )
        raise RuntimeError(
            "Room cache is empty in production. The rooms table must be populated with world seed data. "
            "Run: scripts/load_world_seed.py (set DATABASE_URL) or psql -d your_db -f data/db/mythos_<env>_dml.sql. "
            "See db/README.md."
        )
    logger.warning(
        "Room cache is empty after warmup - NPC spawning may fail. "
        "To populate: run scripts/load_world_seed.py or psql -d your_db -f data/db/mythos_<env>_dml.sql",
        cache_size=cache_size,
        cache_loaded=container.async_persistence._room_cache_loaded,  # pylint: disable=protected-access  # Reason: Need to check cache load status
    )


def _log_npc_startup_errors(startup_results: dict[str, Any]) -> None:
    """Log any errors from NPC startup spawning results."""
    errors = startup_results.get("errors") or []
    if not errors:
        return
    logger.warning("NPC startup spawning had errors", error_count=len(errors))
    for error in errors:
        logger.warning("Startup spawning error", error=str(error))


async def initialize_npc_startup_spawning(_app: FastAPI) -> None:
    """Initialize and run NPC startup spawning."""
    logger.info("Starting NPC startup spawning process")
    try:
        await _ensure_room_cache_before_npc_startup()
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
        _log_npc_startup_errors(startup_results)
    except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
        logger.error("Critical error during NPC startup spawning", error=str(e))
        logger.warning("Continuing server startup despite NPC spawning errors")
    logger.info("NPC startup spawning completed - NPCs should now be present in the world")


async def initialize_nats_and_combat_services(app: FastAPI, container: ApplicationContainer) -> None:
    """
    Initialize NATS-dependent services including combat service.

    DEPRECATED: This function is no longer called. NATS and combat services are now initialized
    in ApplicationContainer.initialize() via _initialize_nats_combat_service().
    This function is kept for backward compatibility but should not be used.
    """
    if container.config is None:
        raise RuntimeError("Config must be initialized")
    is_testing = container.config.logging.environment in ("unit_test", "e2e_test")

    if container.nats_service is not None and container.nats_service.is_connected():
        logger.info("NATS service available from container")
        app.state.nats_service = container.nats_service

        # Lazy import to avoid circular dependency with combat_service
        from ..services.combat_service import (  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Lazy import required to avoid circular dependency with combat_service module
            CombatService,
            PlayerLifecycleServices,
            set_combat_service,
        )

        app.state.combat_service = CombatService(
            app.state.player_combat_service,
            container.nats_service,
            player_lifecycle_services=PlayerLifecycleServices(
                app.state.player_death_service,
                app.state.player_respawn_service,
            ),
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
    """
    Initialize chat service.

    DEPRECATED: This function is no longer called. Chat service is now initialized
    in ApplicationContainer.initialize() via _initialize_chat_service().
    This function is kept for backward compatibility but should not be used.
    """
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


# Re-export for backward compatibility (deprecated path; tests use this)
