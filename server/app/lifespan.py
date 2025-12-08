"""Application lifecycle management for MythosMUD server.

This module handles application startup and shutdown logic,
including the game tick loop and dependency injection container initialization.

ARCHITECTURE MIGRATION:
This module has been refactored to use ApplicationContainer for dependency injection,
eliminating the previous pattern of manually initializing and managing services in app.state.
"""

import asyncio
import datetime
from collections.abc import Iterable
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ..container import ApplicationContainer
from ..logging.enhanced_logging_config import get_logger, update_logging_with_player_service
from ..realtime.connection_manager import broadcast_game_event
from ..services.catatonia_registry import CatatoniaRegistry
from ..services.player_respawn_service import LIMBO_ROOM_ID
from ..time.time_event_consumer import MythosTimeEventConsumer
from ..time.time_service import get_mythos_chronicle

logger = get_logger("server.lifespan")
TICK_INTERVAL = 1.0  # seconds

# Global tick counter for combat system
# NOTE: This remains global for now as it's shared state needed by combat system
# FUTURE: Move to domain layer when implementing Phase 3.3
_current_tick = 0


def get_current_tick() -> int:
    """Get the current game tick."""
    return _current_tick


def reset_current_tick() -> None:
    """Reset the current tick for testing."""
    global _current_tick  # pylint: disable=global-statement
    _current_tick = 0


# Log directory creation is now handled by logging_config.py


async def _initialize_container_and_legacy_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize container and set up legacy compatibility services on app.state."""
    with ApplicationContainer._lock:
        ApplicationContainer._instance = container

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


async def _setup_connection_manager(app: FastAPI, container: ApplicationContainer) -> None:
    """Set up connection manager with dependencies."""
    if container.connection_manager is None:
        raise RuntimeError("Connection manager not initialized in container")

    container.connection_manager.async_persistence = container.async_persistence
    container.connection_manager.set_event_bus(container.event_bus)
    container.connection_manager.app = app
    container.connection_manager.start_health_checks()
    container.connection_manager.message_queue.pending_messages.clear()
    logger.info("Cleared stale pending messages from previous server sessions")


async def _initialize_npc_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize NPC services and load definitions."""
    from ..npc.lifecycle_manager import NPCLifecycleManager
    from ..npc.population_control import NPCPopulationController
    from ..npc.spawning_service import NPCSpawningService
    from ..services.npc_instance_service import initialize_npc_instance_service
    from ..services.npc_service import NPCService

    assert container.event_bus is not None, "EventBus must be initialized"
    app.state.npc_spawning_service = NPCSpawningService(container.event_bus, None)
    assert container.persistence is not None, "Persistence must be initialized"
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
        except Exception as e:
            logger.error("Error loading NPC definitions and spawn rules", error=str(e))
        break

    logger.info("NPC services initialized and added to app.state")

    if hasattr(app.state.npc_lifecycle_manager, "thread_manager"):
        try:
            await app.state.npc_lifecycle_manager.thread_manager.start()
            logger.info("NPC thread manager started")

            if hasattr(app.state.npc_lifecycle_manager, "_pending_thread_starts"):
                for npc_id, definition in app.state.npc_lifecycle_manager._pending_thread_starts:
                    try:
                        await app.state.npc_lifecycle_manager.thread_manager.start_npc_thread(npc_id, definition)
                        logger.debug("Started queued NPC thread", npc_id=npc_id)
                    except Exception as e:
                        logger.warning("Failed to start queued NPC thread", npc_id=npc_id, error=str(e))
                app.state.npc_lifecycle_manager._pending_thread_starts.clear()
        except Exception as e:
            logger.error("Failed to start NPC thread manager", error=str(e))


async def _initialize_combat_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize combat-related services."""
    from ..services.passive_lucidity_flux_service import PassiveLucidityFluxService
    from ..services.player_combat_service import PlayerCombatService
    from ..services.player_death_service import PlayerDeathService
    from ..services.player_respawn_service import PlayerRespawnService

    app.state.player_combat_service = PlayerCombatService(container.persistence, container.event_bus)
    if container.connection_manager is not None:
        container.connection_manager._player_combat_service = app.state.player_combat_service
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
        await asyncio.sleep(0.1)

        if container.database_manager is None:
            logger.error("Database manager not available for catatonia failover", player_id=player_id)
            return

        try:
            session_maker = container.database_manager.get_session_maker()
        except Exception as exc:
            logger.error(
                "Failed to get session maker for catatonia failover",
                player_id=player_id,
                error=str(exc),
                exc_info=True,
            )
            return

        async with session_maker() as session:
            try:
                await app.state.player_respawn_service.move_player_to_limbo(player_id, "catatonia_failover", session)
                await app.state.player_respawn_service.respawn_player(player_id, session)
                logger.info("Catatonia failover completed", player_id=player_id, lcd=current_lcd)
            except Exception as exc:  # pragma: no cover - defensive
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


async def _initialize_mythos_time_consumer(app: FastAPI, container: ApplicationContainer) -> None:
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


async def _initialize_npc_startup_spawning(app: FastAPI) -> None:
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
    except Exception as e:
        logger.error("Critical error during NPC startup spawning", error=str(e))
        logger.warning("Continuing server startup despite NPC spawning errors")

    logger.info("NPC startup spawning completed - NPCs should now be present in the world")


async def _initialize_nats_and_combat_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize NATS-dependent services including combat service."""
    assert container.config is not None, "Config must be initialized"
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
        )

        set_combat_service(app.state.combat_service)

        assert container.player_service is not None, "PlayerService must be initialized"
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
        except Exception as e:
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


async def _initialize_chat_service(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize chat service."""
    from ..game.chat_service import ChatService
    from ..services.nats_subject_manager import nats_subject_manager

    assert container.config is not None, "Config must be initialized"
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


async def _shutdown_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Handle graceful shutdown of all services."""
    logger.info("Freezing mythos chronicle state")
    try:
        chronicle = get_mythos_chronicle()
        frozen_state = chronicle.freeze()
        logger.info(
            "Mythos chronicle state persisted",
            real_timestamp=frozen_state.real_timestamp.isoformat(),
            mythos_timestamp=frozen_state.mythos_timestamp.isoformat(),
        )
    except Exception as e:
        logger.error("Failed to persist mythos chronicle state during shutdown", error=str(e))

    if hasattr(app.state, "nats_message_handler") and app.state.nats_message_handler:
        logger.info("Stopping NATS message handler")
        try:
            await app.state.nats_message_handler.stop()
            logger.info("NATS message handler stopped successfully")
        except Exception as e:
            logger.error("Error stopping NATS message handler", error=str(e))

    if hasattr(app.state, "connection_manager") and app.state.connection_manager:
        logger.info("Stopping connection manager health checks")
        try:
            app.state.connection_manager.stop_health_checks()
        except Exception as e:
            logger.error("Error stopping connection manager health checks", error=str(e))

        logger.info("Cleaning up connection manager tasks")
        try:
            await app.state.connection_manager.force_cleanup()
        except Exception as e:
            logger.error("Error during connection manager cleanup", error=str(e))

    if hasattr(app.state, "mythos_tick_scheduler") and app.state.mythos_tick_scheduler:
        logger.info("Stopping Mythos tick scheduler")
        try:
            await app.state.mythos_tick_scheduler.stop()
        except Exception as e:
            logger.error("Error stopping Mythos tick scheduler", error=str(e))

    if container.task_registry:
        logger.info("Executing TaskRegistry graceful shutdown coordination")
        try:
            shutdown_success = await container.task_registry.shutdown_all(timeout=5.0)
            if shutdown_success:
                logger.info("All tasks cancelled gracefully")
            else:
                logger.warning("TaskRegistry shutdown reached timeout - forcing termination of remaining tasks")
        except Exception as e:
            logger.error("TaskRegistry shutdown coordination error", error=str(e))

    logger.info("Shutting down ApplicationContainer")
    await container.shutdown()
    logger.info("ApplicationContainer shutdown complete")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.

    Handles startup and shutdown logic using ApplicationContainer for
    dependency injection and service lifecycle management.

    ARCHITECTURE:
    - Uses ApplicationContainer to manage all service dependencies
    - Services accessed via container instead of scattered app.state attributes
    - Proper initialization order handled by container
    - Clean separation of concerns

    AI: This is the refactored version using dependency injection container.
        Much simpler than the previous 200+ lines of manual service wiring.
    """
    logger.info("Starting MythosMUD server with ApplicationContainer...")

    container = ApplicationContainer()
    await container.initialize()
    await _initialize_container_and_legacy_services(app, container)

    # NOTE: Global persistence singleton removed - all code now uses container.persistence (async_persistence)
    # No need to synchronize global singleton since we're fully async

    # LEGACY COMPATIBILITY: Also expose services directly on app.state
    # This maintains backward compatibility during migration
    # FUTURE: Remove these direct assignments once all code uses container
    app.state.task_registry = container.task_registry
    app.state.event_bus = container.event_bus
    app.state.event_handler = container.real_time_event_handler
    app.state.persistence = container.async_persistence  # Now async_persistence
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

    await _setup_connection_manager(app, container)
    await _initialize_npc_services(app, container)

    await _initialize_combat_services(app, container)
    await _initialize_mythos_time_consumer(app, container)
    await _initialize_npc_startup_spawning(app)

    # Enhance logging system with PlayerGuidFormatter now that player service is available
    update_logging_with_player_service(container.player_service)
    logger.info("Logging system enhanced with PlayerGuidFormatter")

    # Set the main event loop for the EventBus to handle async event handlers
    assert container.event_bus is not None, "EventBus must be initialized"
    main_loop = asyncio.get_running_loop()
    container.event_bus.set_main_loop(main_loop)

    if container.mythos_tick_scheduler is not None:
        await container.mythos_tick_scheduler.start()
        app.state.mythos_tick_scheduler = container.mythos_tick_scheduler
        logger.info("Mythos tick scheduler running")

    logger.info("Real-time event handler initialized")

    await _initialize_nats_and_combat_services(app, container)
    await _initialize_chat_service(app, container)

    # Start the game tick loop using TaskRegistry from container
    assert container.task_registry is not None, "TaskRegistry must be initialized"
    tick_task = container.task_registry.register_task(game_tick_loop(app), "lifecycle/game_tick_loop", "lifecycle")
    app.state.tick_task = tick_task
    logger.info("MythosMUD server started successfully with ApplicationContainer")
    yield

    logger.info("Shutting down MythosMUD server...")

    try:
        await _shutdown_services(app, container)

    except (asyncio.CancelledError, KeyboardInterrupt) as e:
        logger.warning("Shutdown interrupted", error=str(e), error_type=type(e).__name__)
        # Try to persist mythos state before cleanup
        try:
            chronicle = get_mythos_chronicle()
            chronicle.freeze()
            logger.info("Mythos chronicle state persisted during interrupted shutdown")
        except Exception:
            logger.warning("Failed to persist mythos chronicle state during interrupted shutdown")
        # Still try to cleanup container
        try:
            await container.shutdown()
        except Exception:
            pass
        raise
    except Exception as e:
        logger.error("Critical shutdown failure", error=str(e), error_type=type(e).__name__, exc_info=True)
        # Try to persist mythos state before cleanup
        try:
            chronicle = get_mythos_chronicle()
            chronicle.freeze()
            logger.info("Mythos chronicle state persisted during error shutdown")
        except Exception:
            logger.warning("Failed to persist mythos chronicle state during error shutdown")
        # Still try to cleanup container
        try:
            await container.shutdown()
        except Exception:
            pass

    logger.info("MythosMUD server shutdown complete")


async def _process_status_effects(app: FastAPI, tick_count: int) -> None:
    """Process status effects for online players."""
    if not (hasattr(app.state, "container") and app.state.container):
        return

    container = app.state.container
    if not container.async_persistence:
        return

    if not (hasattr(app.state, "connection_manager") and app.state.connection_manager):
        return

    try:
        online_player_ids = list(app.state.connection_manager.online_players.keys())
        if not online_player_ids:
            return

        processed_count = 0
        for player_id in online_player_ids:
            try:
                player = await container.async_persistence.get_player_by_id(player_id)
                if not player:
                    continue

                status_effects = player.get_status_effects()
                if not status_effects:
                    continue

                updated_effects = []
                effect_applied = False

                for effect in status_effects:
                    effect_type = effect.get("type", "")
                    duration = effect.get("duration", 0)
                    remaining = effect.get("remaining", duration) - 1

                    if effect_type == "damage_over_time" and remaining > 0:
                        damage = effect.get("damage", 0)
                        if damage > 0 and hasattr(app.state, "player_death_service"):
                            await container.async_persistence.damage_player(player, damage, "status_effect")
                            effect_applied = True
                            logger.debug(
                                "Applied damage over time", player_id=player_id, damage=damage, effect_type=effect_type
                            )
                        updated_effects.append({**effect, "remaining": remaining})
                    elif effect_type == "heal_over_time" and remaining > 0:
                        healing = effect.get("healing", 0)
                        if healing > 0:
                            await container.async_persistence.heal_player(player, healing)
                            effect_applied = True
                            logger.debug(
                                "Applied heal over time", player_id=player_id, healing=healing, effect_type=effect_type
                            )
                        updated_effects.append({**effect, "remaining": remaining})
                    elif remaining > 0:
                        updated_effects.append({**effect, "remaining": remaining})

                if len(updated_effects) != len(status_effects) or effect_applied:
                    player.set_status_effects(updated_effects)
                    await container.async_persistence.save_player(player)
                    processed_count += 1
            except Exception as e:
                logger.warning("Error processing status effects for player", player_id=player_id, error=str(e))

        if processed_count > 0:
            logger.debug("Processed status effects", tick_count=tick_count, players_processed=processed_count)
    except Exception as e:
        logger.warning("Error processing status/effect ticks", tick_count=tick_count, error=str(e))


async def _process_combat_tick(app: FastAPI, tick_count: int) -> None:
    """Process combat auto-progression."""
    if hasattr(app.state, "combat_service"):
        try:
            await app.state.combat_service.process_game_tick(tick_count)
        except Exception as e:
            logger.error("Error processing combat tick", tick_count=tick_count, error=str(e))


async def _process_hp_decay_and_death(app: FastAPI, tick_count: int) -> None:
    """Process HP decay for mortally wounded players and handle deaths."""
    if not hasattr(app.state, "player_death_service"):
        return

    try:
        from ..database import get_async_session

        async for session in get_async_session():
            try:
                mortally_wounded = await app.state.player_death_service.get_mortally_wounded_players(session)

                if mortally_wounded:
                    logger.debug(
                        "Processing HP decay for mortally wounded players",
                        tick_count=tick_count,
                        player_count=len(mortally_wounded),
                    )

                    for player in mortally_wounded:
                        await app.state.player_death_service.process_mortally_wounded_tick(player.player_id, session)

                        await session.refresh(player)
                        stats = player.get_stats()
                        new_hp = stats.get("current_health", 0)

                        if hasattr(app.state, "combat_service"):
                            from ..services.combat_messaging_integration import combat_messaging_integration

                            await combat_messaging_integration.send_hp_decay_message(player.player_id, new_hp)

                        if new_hp <= -10:
                            logger.info(
                                "Player reached death threshold",
                                player_id=player.player_id,
                                player_name=player.name,
                                current_hp=new_hp,
                            )

                            await app.state.player_death_service.handle_player_death(
                                player.player_id, player.current_room_id, None, session
                            )

                            await app.state.player_respawn_service.move_player_to_limbo(
                                player.player_id, player.current_room_id, session
                            )

                if hasattr(app.state, "passive_lucidity_flux_service"):
                    try:
                        await app.state.passive_lucidity_flux_service.process_tick(
                            session=session, tick_count=tick_count, now=datetime.datetime.now(datetime.UTC)
                        )
                    except Exception as lcd_flux_error:
                        logger.error(
                            "Error processing passive LCD flux", tick_count=tick_count, error=str(lcd_flux_error)
                        )

                dead_players = await app.state.player_death_service.get_dead_players(session)

                if dead_players:
                    logger.debug(
                        "Found dead players", count=len(dead_players), player_ids=[p.player_id for p in dead_players]
                    )

                    for player in dead_players:
                        if str(player.current_room_id) != LIMBO_ROOM_ID:
                            logger.info(
                                "Moving dead player to limbo",
                                player_id=player.player_id,
                                player_name=player.name,
                                current_room_id=player.current_room_id,
                            )

                            await app.state.player_respawn_service.move_player_to_limbo(
                                player.player_id, player.current_room_id, session
                            )
            except Exception as e:
                logger.error("Error in HP decay processing", tick_count=tick_count, error=str(e))
    except Exception as e:
        logger.error("Error getting database session for HP decay", tick_count=tick_count, error=str(e))


async def game_tick_loop(app: FastAPI):
    """Main game tick loop.

    This function runs continuously and handles periodic game updates,
    including broadcasting tick information to connected players."""
    global _current_tick
    tick_count = 0
    logger.info("Game tick loop started")

    while True:
        try:
            await _process_status_effects(app, tick_count)
            logger.debug("Game tick", tick_count=tick_count)
            _current_tick = tick_count
            await _process_combat_tick(app, tick_count)
            await _process_hp_decay_and_death(app, tick_count)

            # Broadcast game tick to all connected players (normal path)
            tick_data = {
                "tick_number": tick_count,
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
                "active_players": len(app.state.container.connection_manager.player_websockets),
            }
            logger.debug(
                "Broadcasting game tick",
                tick_count=tick_count,
                player_count=len(app.state.container.connection_manager.player_websockets),
            )
            await broadcast_game_event("game_tick", tick_data)
            logger.debug("Game tick broadcast completed", tick_count=tick_count)

            # Sleep for tick interval
            await asyncio.sleep(TICK_INTERVAL)
            tick_count += 1
        except asyncio.CancelledError:
            logger.info("Game tick loop cancelled")
            break
        except Exception as e:
            logger.error("Error in game tick loop", tick_count=tick_count, error=str(e), exc_info=True)
            try:
                await asyncio.sleep(TICK_INTERVAL)
            except asyncio.CancelledError:
                logger.info("Game tick loop cancelled during error recovery")
                break
            tick_count += 1

            # Process NPC lifecycle maintenance (every 60 ticks = 1 minute)
            from ..config.npc_config import NPCMaintenanceConfig

            if NPCMaintenanceConfig.should_run_maintenance(tick_count) and hasattr(app.state, "npc_lifecycle_manager"):
                try:
                    logger.debug(
                        "Running NPC maintenance",
                        tick_count=tick_count,
                        has_lifecycle_manager=True,
                        respawn_queue_size=len(app.state.npc_lifecycle_manager.respawn_queue),
                    )
                    maintenance_results = app.state.npc_lifecycle_manager.periodic_maintenance()
                    logger.info("NPC maintenance completed", tick_count=tick_count, **maintenance_results)
                except Exception as e:
                    logger.error("Error during NPC maintenance", tick_count=tick_count, error=str(e))

            # Cleanup decayed corpse containers (every 60 ticks = 1 minute)
            if tick_count % 60 == 0:
                try:
                    from ..services.corpse_lifecycle_service import CorpseLifecycleService
                    from ..time.time_service import get_mythos_chronicle

                    persistence = app.state.container.persistence
                    connection_manager = app.state.container.connection_manager
                    time_service = get_mythos_chronicle()

                    corpse_service = CorpseLifecycleService(
                        persistence=persistence,
                        connection_manager=connection_manager,
                        time_service=time_service,
                    )

                    decayed = await corpse_service.get_all_decayed_corpses()
                    cleaned_count = 0

                    for corpse in decayed:
                        try:
                            if connection_manager and corpse.room_id:
                                from ..services.container_websocket_events import emit_container_decayed

                                await emit_container_decayed(
                                    connection_manager=connection_manager,
                                    container_id=corpse.container_id,
                                    room_id=corpse.room_id,
                                )

                            await corpse_service.cleanup_decayed_corpse(corpse.container_id)
                            cleaned_count += 1
                        except Exception as cleanup_error:
                            logger.error(
                                "Error cleaning up individual decayed corpse",
                                error=str(cleanup_error),
                                container_id=str(corpse.container_id),
                                exc_info=True,
                            )
                            continue

                    if cleaned_count > 0:
                        logger.info(
                            "Decayed corpses cleaned up",
                            tick_count=tick_count,
                            cleaned_count=cleaned_count,
                            total_decayed=len(decayed),
                        )
                except Exception as corpse_cleanup_error:
                    logger.warning(
                        "Error cleaning up decayed corpses",
                        error=str(corpse_cleanup_error),
                        tick_count=tick_count,
                        exc_info=True,
                    )

            # Broadcast game tick to all connected players
            tick_data = {
                "tick_number": tick_count,
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
                "active_players": len(app.state.container.connection_manager.player_websockets),
            }
            logger.debug(
                "Broadcasting game tick",
                tick_count=tick_count,
                player_count=len(app.state.container.connection_manager.player_websockets),
            )
            await broadcast_game_event("game_tick", tick_data)
            logger.debug("Game tick broadcast completed", tick_count=tick_count)

            # Cleanup decayed corpse containers (every 60 ticks = 1 minute)
            if tick_count % 60 == 0:
                try:
                    from ..services.corpse_lifecycle_service import CorpseLifecycleService
                    from ..time.time_service import get_mythos_chronicle

                    persistence = app.state.container.persistence
                    connection_manager = app.state.container.connection_manager
                    time_service = get_mythos_chronicle()

                    corpse_service = CorpseLifecycleService(
                        persistence=persistence,
                        connection_manager=connection_manager,
                        time_service=time_service,
                    )

                    # Get all decayed corpses and clean them up
                    decayed = await corpse_service.get_all_decayed_corpses()
                    cleaned_count = 0

                    for corpse in decayed:
                        try:
                            # Emit decay event before cleanup
                            if connection_manager and corpse.room_id:
                                from ..services.container_websocket_events import emit_container_decayed

                                await emit_container_decayed(
                                    connection_manager=connection_manager,
                                    container_id=corpse.container_id,
                                    room_id=corpse.room_id,
                                )

                            # Cleanup corpse (this will delete it)
                            await corpse_service.cleanup_decayed_corpse(corpse.container_id)
                            cleaned_count += 1
                        except Exception as cleanup_error:
                            logger.error(
                                "Error cleaning up individual decayed corpse",
                                error=str(cleanup_error),
                                container_id=str(corpse.container_id),
                                exc_info=True,
                            )
                            continue

                    if cleaned_count > 0:
                        logger.info(
                            "Decayed corpses cleaned up",
                            tick_count=tick_count,
                            cleaned_count=cleaned_count,
                            total_decayed=len(decayed),
                        )
                except Exception as corpse_cleanup_error:
                    logger.warning(
                        "Error cleaning up decayed corpses",
                        error=str(corpse_cleanup_error),
                        tick_count=tick_count,
                        exc_info=True,
                    )

            # Broadcast game tick to all connected players
            # AI Agent: Use container instance instead of global singleton
            tick_data = {
                "tick_number": tick_count,
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
                "active_players": len(app.state.container.connection_manager.player_websockets),
            }
            logger.debug(
                "Broadcasting game tick",
                tick_count=tick_count,
                player_count=len(app.state.container.connection_manager.player_websockets),
            )
            await broadcast_game_event("game_tick", tick_data)
            logger.debug("Game tick broadcast completed", tick_count=tick_count)
            tick_count += 1
            await asyncio.sleep(TICK_INTERVAL)
