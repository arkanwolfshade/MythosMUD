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
# TODO: Move to domain layer when implementing Phase 3.3
_current_tick = 0


def get_current_tick() -> int:
    """Get the current game tick."""
    return _current_tick


def reset_current_tick() -> None:
    """Reset the current tick for testing."""
    global _current_tick
    _current_tick = 0


# Log directory creation is now handled by logging_config.py


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

    # Create and initialize the dependency injection container
    container = ApplicationContainer()
    await container.initialize()

    # Add container to app.state for dependency injection
    app.state.container = container
    logger.info("ApplicationContainer initialized and added to app.state")

    # AI Agent: CRITICAL FIX - Ensure global persistence singleton uses container's instance
    #           This prevents the dual-cache bug where NPCs are added to one cache
    #           but player connections see a different cache
    # Import _persistence_lock from the module file (not the package)
    # Note: _persistence_lock exists in server/persistence.py but is not exported via the package
    # We import it directly from the module file using importlib
    import importlib.util
    from pathlib import Path

    _persistence_module_path = Path(__file__).parent.parent / "persistence.py"
    if _persistence_module_path.exists():
        _persistence_spec = importlib.util.spec_from_file_location(
            "server.persistence_module", _persistence_module_path
        )
        if _persistence_spec and _persistence_spec.loader:
            _persistence_module = importlib.util.module_from_spec(_persistence_spec)
            _persistence_spec.loader.exec_module(_persistence_module)
            _persistence_lock = _persistence_module._persistence_lock
    else:
        import threading

        _persistence_lock = threading.Lock()  # Fallback

    with _persistence_lock:
        globals_module = __import__("server.persistence", fromlist=["_persistence_instance"])
        globals_module._persistence_instance = container.persistence  # type: ignore[attr-defined]
    logger.info("Global persistence singleton synchronized with container instance")

    # LEGACY COMPATIBILITY: Also expose services directly on app.state
    # This maintains backward compatibility during migration
    # TODO: Remove these direct assignments once all code uses container
    app.state.task_registry = container.task_registry
    app.state.event_bus = container.event_bus
    app.state.event_handler = container.real_time_event_handler
    app.state.persistence = container.persistence
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
                    except Exception:  # noqa: BLE001
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

    # AI Agent: Use container instance instead of global singleton
    #           This completes the migration to dependency injection
    # AI Agent: Add type guard for mypy (container.connection_manager is ConnectionManager | None)
    if container.connection_manager is None:
        raise RuntimeError("Connection manager not initialized in container")

    container.connection_manager.persistence = container.persistence
    container.connection_manager._event_bus = container.event_bus
    container.connection_manager.app = app

    # Start periodic connection health checks
    container.connection_manager.start_health_checks()

    # Clear any stale pending messages from previous server sessions
    container.connection_manager.message_queue.pending_messages.clear()
    logger.info("Cleared stale pending messages from previous server sessions")

    # Initialize NPC services (not yet in container - Phase 2 migration)
    # TODO: Move these to container in Phase 2 after core services are stable
    from ..npc.lifecycle_manager import NPCLifecycleManager
    from ..npc.population_control import NPCPopulationController
    from ..npc.spawning_service import NPCSpawningService
    from ..services.npc_instance_service import initialize_npc_instance_service
    from ..services.npc_service import NPCService

    # Create NPC services using services from container
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
    # Update spawning service to use population controller
    app.state.npc_spawning_service.population_controller = app.state.npc_population_controller
    # Update lifecycle manager to use population controller
    app.state.npc_lifecycle_manager.population_controller = app.state.npc_population_controller

    # Initialize the NPC instance service
    initialize_npc_instance_service(
        lifecycle_manager=app.state.npc_lifecycle_manager,
        spawning_service=app.state.npc_spawning_service,
        population_controller=app.state.npc_population_controller,
        event_bus=container.event_bus,  # Already asserted non-None above
    )

    # Load NPC definitions and spawn rules from database
    from ..npc_database import get_npc_session

    npc_service = NPCService()
    async for npc_session in get_npc_session():
        try:
            # Load NPC definitions
            definitions = await npc_service.get_npc_definitions(npc_session)
            app.state.npc_population_controller.load_npc_definitions(definitions)
            logger.info("NPC definitions loaded", count=len(definitions))

            # Load spawn rules
            spawn_rules = await npc_service.get_spawn_rules(npc_session)
            app.state.npc_population_controller.load_spawn_rules(spawn_rules)
            logger.info("NPC spawn rules loaded", count=len(spawn_rules))

        except Exception as e:
            logger.error("Error loading NPC definitions and spawn rules", error=str(e))
        break

    logger.info("NPC services initialized and added to app.state")

    # Start NPC thread manager for behavior execution
    if hasattr(app.state.npc_lifecycle_manager, "thread_manager"):
        try:
            await app.state.npc_lifecycle_manager.thread_manager.start()
            logger.info("NPC thread manager started")

            # Process any pending thread start requests
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

    # Initialize combat services (not yet in container - Phase 2 migration)
    # TODO: Move these to container in Phase 2
    from ..services.passive_sanity_flux_service import PassiveSanityFluxService
    from ..services.player_combat_service import PlayerCombatService
    from ..services.player_death_service import PlayerDeathService
    from ..services.player_respawn_service import PlayerRespawnService

    app.state.player_combat_service = PlayerCombatService(container.persistence, container.event_bus)
    # Make player combat service available to connection manager for movement validation
    # AI Agent: Use container instance instead of global singleton
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

    async def _sanitarium_failover(player_id: str, current_san: int) -> None:
        """
        Failover callback that relocates catatonic players to the sanitarium.

        This callback runs in a background task (fire-and-forget) to avoid blocking
        the sanity service transaction. It uses a completely independent database session
        to prevent transaction conflicts.

        CRITICAL: We add a small delay to ensure the sanity service's transaction has
        completed before attempting the respawn. This prevents asyncpg connection conflicts.
        """
        # Small delay to ensure the sanity service transaction has completed
        # This prevents "another operation is in progress" errors from asyncpg
        await asyncio.sleep(0.1)

        # Use container's database manager to get a session maker
        # This ensures we get a fresh, independent session that won't conflict
        # with any active transactions from the sanity service
        if container.database_manager is None:
            logger.error(
                "Database manager not available for catatonia failover",
                player_id=player_id,
            )
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

        # Create a completely independent session for the respawn operation
        async with session_maker() as session:
            try:
                await app.state.player_respawn_service.move_player_to_limbo(player_id, "catatonia_failover", session)
                await app.state.player_respawn_service.respawn_player(player_id, session)
                logger.info(
                    "Catatonia failover completed",
                    player_id=player_id,
                    san=current_san,
                )
            except Exception as exc:  # pragma: no cover - defensive
                logger.error(
                    "Catatonia failover failed",
                    player_id=player_id,
                    error=str(exc),
                    exc_info=True,
                )
                # Rollback the session on error
                await session.rollback()

    app.state.catatonia_registry = CatatoniaRegistry(failover_callback=_sanitarium_failover)
    logger.info("Catatonia registry initialized")

    app.state.passive_sanity_flux_service = PassiveSanityFluxService(
        persistence=container.persistence,
        performance_monitor=container.performance_monitor,
        catatonia_observer=app.state.catatonia_registry,
    )
    logger.info("Passive sanity flux service initialized")

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

    # Initialize NPC startup spawning
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

        # Log any errors that occurred during startup
        if startup_results["errors"]:
            logger.warning("NPC startup spawning had errors", error_count=len(startup_results["errors"]))
            for error in startup_results["errors"]:
                logger.warning("Startup spawning error", error=str(error))

    except Exception as e:
        logger.error("Critical error during NPC startup spawning", error=str(e))
        # Don't fail server startup due to NPC spawning issues
        logger.warning("Continuing server startup despite NPC spawning errors")

    logger.info("NPC startup spawning completed - NPCs should now be present in the world")

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

    # Initialize NATS-dependent services (NATS already initialized in container)
    # Check if we're in a testing environment
    assert container.config is not None, "Config must be initialized"
    is_testing = container.config.logging.environment in ("unit_test", "e2e_test")

    if container.nats_service is not None and container.nats_service.is_connected():
        logger.info("NATS service available from container")
        app.state.nats_service = container.nats_service

        # Initialize combat service now that NATS service is available
        from ..services.combat_service import CombatService

        app.state.combat_service = CombatService(
            app.state.player_combat_service,
            container.nats_service,
            player_death_service=app.state.player_death_service,
            player_respawn_service=app.state.player_respawn_service,
        )

        # Update global combat service instance for tests and other modules
        from ..services.combat_service import set_combat_service

        set_combat_service(app.state.combat_service)

        # Update PlayerService with combat service and player combat service
        assert container.player_service is not None, "PlayerService must be initialized"
        container.player_service.combat_service = app.state.combat_service
        container.player_service.player_combat_service = app.state.player_combat_service
        logger.info("Combat service initialized and added to app.state")

        # Initialize NATS message handler (now from container, not global factory)
        # AI Agent: Migrated from global get_nats_message_handler() to container instance
        #           This follows dependency injection best practices and eliminates global singletons
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
            # In test environment, NATS connection failure is not fatal
            logger.warning("NATS service not available in test environment - using mock NATS service")
            app.state.nats_service = None
            app.state.nats_message_handler = None
        else:
            logger.error("NATS service not available - NATS is required for chat functionality")
            raise RuntimeError("NATS connection failed - NATS is mandatory for chat system")

    # Initialize chat service (not yet in container - Phase 2 migration)
    # TODO: Move to container in Phase 2
    from ..game.chat_service import ChatService
    from ..services.nats_subject_manager import nats_subject_manager

    subject_manager = None
    nats_service = getattr(app.state, "nats_service", None)
    if nats_service and getattr(nats_service, "subject_manager", None):
        subject_manager = nats_service.subject_manager
    else:
        subject_manager = nats_subject_manager

    app.state.chat_service = ChatService(
        persistence=container.persistence,
        room_service=container.persistence,  # Persistence layer provides room service functionality
        player_service=container.player_service,
        nats_service=nats_service,
        user_manager_instance=container.user_manager,
        subject_manager=subject_manager,
    )

    # Verify NATS service connection in chat service
    if app.state.chat_service.nats_service and app.state.chat_service.nats_service.is_connected():
        logger.info("Chat service NATS connection verified")
    elif is_testing:
        logger.info("Chat service running in test mode without NATS connection")
    else:
        logger.error("Chat service NATS connection failed")
        raise RuntimeError("Chat service NATS connection failed - NATS is mandatory for chat system")

    logger.info("Chat service initialized")

    # Start the game tick loop using TaskRegistry from container
    assert container.task_registry is not None, "TaskRegistry must be initialized"
    tick_task = container.task_registry.register_task(game_tick_loop(app), "lifecycle/game_tick_loop", "lifecycle")
    app.state.tick_task = tick_task
    logger.info("MythosMUD server started successfully with ApplicationContainer")
    yield

    # Shutdown logic - Using ApplicationContainer shutdown
    logger.info("Shutting down MythosMUD server...")

    try:
        # Phase 0: Persist mythos time state before shutdown
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

        # Phase 1: Stop NATS message handler if running
        if hasattr(app.state, "nats_message_handler") and app.state.nats_message_handler:
            logger.info("Stopping NATS message handler")
            try:
                await app.state.nats_message_handler.stop()
                logger.info("NATS message handler stopped successfully")
            except Exception as e:
                logger.error("Error stopping NATS message handler", error=str(e))

        # Phase 2: Connection Manager cleanup before task cancellation
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

        # Phase 3: TaskRegistry shutdown coordination
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

        # Phase 4: Container shutdown (handles NATS, event bus, database cleanup)
        logger.info("Shutting down ApplicationContainer")
        await container.shutdown()
        logger.info("ApplicationContainer shutdown complete")

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


async def game_tick_loop(app: FastAPI):
    """Main game tick loop.

    This function runs continuously and handles periodic game updates,
    including broadcasting tick information to connected players."""
    global _current_tick
    tick_count = 0
    logger.info("Game tick loop started")

    while True:
        try:
            # TODO: Implement status/effect ticks using persistence layer
            logger.debug("Game tick", tick_count=tick_count)

            # Update global tick counter
            _current_tick = tick_count

            # Process combat auto-progression
            if hasattr(app.state, "combat_service"):
                try:
                    await app.state.combat_service.process_game_tick(tick_count)
                except Exception as e:
                    logger.error("Error processing combat tick", tick_count=tick_count, error=str(e))

            # Process HP decay for mortally wounded players
            if hasattr(app.state, "player_death_service"):
                try:
                    from ..database import get_async_session

                    # Get database session for HP decay processing
                    async for session in get_async_session():
                        try:
                            # Get all mortally wounded players
                            mortally_wounded = await app.state.player_death_service.get_mortally_wounded_players(
                                session
                            )

                            if mortally_wounded:
                                logger.debug(
                                    "Processing HP decay for mortally wounded players",
                                    tick_count=tick_count,
                                    player_count=len(mortally_wounded),
                                )

                                # Process decay for each mortally wounded player
                                for player in mortally_wounded:
                                    await app.state.player_death_service.process_mortally_wounded_tick(
                                        player.player_id, session
                                    )

                                    # Refresh player stats to get HP AFTER decay using async API
                                    await session.refresh(player)
                                    stats = player.get_stats()
                                    new_hp = stats.get("current_health", 0)

                                    # Broadcast HP decay message
                                    if hasattr(app.state, "combat_service"):
                                        from ..services.combat_messaging_integration import combat_messaging_integration

                                        await combat_messaging_integration.send_hp_decay_message(
                                            player.player_id, new_hp
                                        )

                                    # Check if player reached death threshold (-10 HP) after decay
                                    if new_hp <= -10:
                                        logger.info(
                                            "Player reached death threshold",
                                            player_id=player.player_id,
                                            player_name=player.name,
                                            current_hp=new_hp,
                                        )

                                        # Handle death and move to limbo
                                        await app.state.player_death_service.handle_player_death(
                                            player.player_id,
                                            player.current_room_id,
                                            None,  # No killer info for decay death
                                            session,
                                        )

                                        # Move player to limbo
                                        await app.state.player_respawn_service.move_player_to_limbo(
                                            player.player_id,
                                            player.current_room_id,
                                            session,
                                        )

                            if hasattr(app.state, "passive_sanity_flux_service"):
                                try:
                                    await app.state.passive_sanity_flux_service.process_tick(
                                        session=session,
                                        tick_count=tick_count,
                                        now=datetime.datetime.now(datetime.UTC),
                                    )
                                except Exception as san_flux_error:
                                    logger.error(
                                        "Error processing passive SAN flux",
                                        tick_count=tick_count,
                                        error=str(san_flux_error),
                                    )

                            # Also check for players already at death threshold who need limbo transition
                            # This handles players who died but haven't been moved to limbo yet
                            # CRITICAL: Use dedicated method to find dead players for better performance and clarity
                            dead_players = await app.state.player_death_service.get_dead_players(session)

                            if dead_players:
                                logger.debug(
                                    "Found dead players",
                                    count=len(dead_players),
                                    player_ids=[p.player_id for p in dead_players],
                                )

                                for player in dead_players:
                                    stats = player.get_stats()
                                    current_hp = stats.get("current_health", 0)

                                    # If player is dead and not in limbo, move them there first
                                    if player.current_room_id != LIMBO_ROOM_ID:
                                        logger.info(
                                            "Found dead player not in limbo - moving to limbo",
                                            player_id=player.player_id,
                                            player_name=player.name,
                                            current_hp=current_hp,
                                            current_room=player.current_room_id,
                                        )

                                        # Handle death and move to limbo
                                        await app.state.player_death_service.handle_player_death(
                                            player.player_id,
                                            player.current_room_id,
                                            None,  # No killer info
                                            session,
                                        )

                                        # Move player to limbo
                                        await app.state.player_respawn_service.move_player_to_limbo(
                                            player.player_id,
                                            player.current_room_id,
                                            session,
                                        )

                                        # Refresh player to get updated room_id
                                        await session.refresh(player)

                                    # NOTE: Respawn is handled manually via /api/players/respawn endpoint
                                    # The client will show the death interstitial and the player can click
                                    # "Rejoin the earthly plane" to trigger respawn via the API
                                    # We only move players to limbo here, not respawn them automatically

                        except Exception as e:
                            logger.error("Error in HP decay processing iteration", error=str(e))

                        # Only need one session iteration - break after first session
                        break
                except Exception as e:
                    logger.error("Error processing HP decay", tick_count=tick_count, error=str(e))

            # Process NPC lifecycle maintenance (every 60 ticks = 1 minute)
            # AI Agent: This integrates the orphaned periodic_maintenance() method into the game tick loop
            #           to enable NPC respawning and periodic spawn checks
            from ..config.npc_config import NPCMaintenanceConfig

            if NPCMaintenanceConfig.should_run_maintenance(tick_count) and hasattr(app.state, "npc_lifecycle_manager"):
                try:
                    # AI Agent: CRITICAL DEBUG - Log maintenance execution even when no NPCs are processed
                    #           This helps diagnose why respawn queue is not being processed
                    logger.debug(
                        "Running NPC maintenance",
                        tick_count=tick_count,
                        has_lifecycle_manager=True,
                        respawn_queue_size=len(app.state.npc_lifecycle_manager.respawn_queue),
                    )
                    maintenance_results = app.state.npc_lifecycle_manager.periodic_maintenance()
                    # AI Agent: ALWAYS log maintenance results to track respawn queue processing
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

                    # Get all decayed corpses and clean them up
                    decayed = corpse_service.get_all_decayed_corpses()
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
                            corpse_service.cleanup_decayed_corpse(corpse.container_id)
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
        except asyncio.CancelledError:
            logger.info("Game tick loop cancelled")
            break
        except Exception as e:
            logger.error("Error in game tick loop", error=str(e))
            await asyncio.sleep(TICK_INTERVAL)
