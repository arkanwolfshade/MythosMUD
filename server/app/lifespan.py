"""Application lifecycle management for MythosMUD server.

This module handles application startup and shutdown logic,
including the game tick loop and persistence layer initialization."""

import asyncio
import datetime
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from sqlalchemy import select

from ..config import get_config
from ..database import init_db
from ..logging.enhanced_logging_config import get_logger, update_logging_with_player_service
from ..npc_database import init_npc_db
from ..persistence import get_persistence
from ..realtime.connection_manager import connection_manager
from ..realtime.event_handler import get_real_time_event_handler
from ..realtime.nats_message_handler import get_nats_message_handler
from ..realtime.sse_handler import broadcast_game_event
from ..services.nats_service import nats_service
from .task_registry import TaskRegistry

logger = get_logger("server.lifespan")
TICK_INTERVAL = 1.0  # seconds

# Global tick counter for combat system
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
    """Application lifespan manager.

    Handles startup and shutdown logic for the FastAPI application,
    including persistence layer initialization and game tick loop."""
    logger.info("Starting MythosMUD server...")

    # Initialize TaskRegistry for managing all asyncio.Tasks in total coordination
    task_registry = TaskRegistry()
    app.state.task_registry = task_registry

    await init_db()
    await init_npc_db()
    # Initialize real-time event handler first to obtain its EventBus with task tracking
    app.state.event_handler = get_real_time_event_handler(event_bus=None, task_registry=task_registry)
    # Ensure the event handler has access to the connection manager
    app.state.event_handler.connection_manager = connection_manager

    # Make EventBus available directly on app.state for easier access
    app.state.event_bus = app.state.event_handler.event_bus

    # Make connection_manager available directly on app.state for command handlers
    app.state.connection_manager = connection_manager

    # Initialize persistence with the same EventBus so Rooms publish to it
    app.state.persistence = get_persistence(event_bus=app.state.event_handler.event_bus)
    connection_manager.persistence = app.state.persistence
    # Ensure connection manager exposes the same EventBus for command handlers
    connection_manager._event_bus = app.state.event_handler.event_bus
    # Give connection manager access to app for WebSocket command processing
    connection_manager.app = app

    # Initialize cache services for improved performance
    from ..caching import ProfessionCacheService, RoomCacheService
    from ..caching.lru_cache import get_cache_manager

    # Ensure cache manager is initialized
    _ = get_cache_manager()

    try:
        app.state.room_cache_service = RoomCacheService(app.state.persistence)
        app.state.profession_cache_service = ProfessionCacheService(app.state.persistence)
        logger.info("Cache services initialized and added to app.state")
    except RuntimeError as e:
        logger.warning("Cache initialization failed, using persistence directly", error=str(e))
        app.state.room_cache_service = None
        app.state.profession_cache_service = None

    # Clear any stale pending messages from previous server sessions
    connection_manager.message_queue.pending_messages.clear()
    logger.info("Cleared stale pending messages from previous server sessions")

    # Initialize critical services and add to app.state
    from ..game.player_service import PlayerService
    from ..services.user_manager import UserManager

    app.state.player_service = PlayerService(app.state.persistence)

    # Initialize UserManager with environment-aware data directory
    config = get_config()
    environment = config.logging.environment

    # Find the project root (where pyproject.toml is located)
    current_file = Path(__file__).resolve()
    project_root = current_file.parent
    while project_root.parent != project_root:
        if (project_root / "pyproject.toml").exists():
            break
        project_root = project_root.parent

    # CRITICAL: Include environment in path for data isolation
    # data/{environment}/user_management NOT data/user_management
    user_management_dir = project_root / "data" / environment / "user_management"
    app.state.user_manager = UserManager(data_dir=user_management_dir)

    logger.info("Critical services (player_service, user_manager) added to app.state")
    logger.info("Player service initialized", player_service=app.state.player_service)
    logger.info("User manager initialized", user_manager=app.state.user_manager)

    # Initialize NPC services
    from ..npc.lifecycle_manager import NPCLifecycleManager
    from ..npc.population_control import NPCPopulationController
    from ..npc.spawning_service import NPCSpawningService
    from ..services.npc_instance_service import initialize_npc_instance_service
    from ..services.npc_service import NPCService

    # Create NPC services
    # Create spawning service first (it doesn't depend on population controller)
    app.state.npc_spawning_service = NPCSpawningService(app.state.event_bus, None)
    # Create lifecycle manager with persistence for proper room state mutation
    app.state.npc_lifecycle_manager = NPCLifecycleManager(
        event_bus=app.state.event_bus,
        population_controller=None,
        spawning_service=app.state.npc_spawning_service,
        persistence=app.state.persistence,
    )
    # Create population controller with spawning service and lifecycle manager
    app.state.npc_population_controller = NPCPopulationController(
        app.state.event_bus, app.state.npc_spawning_service, app.state.npc_lifecycle_manager
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
        event_bus=app.state.event_bus,
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

    # Initialize player combat service (NATS service not needed yet)
    from ..services.player_combat_service import PlayerCombatService

    app.state.player_combat_service = PlayerCombatService(app.state.persistence, app.state.event_bus)
    # Make player combat service available to connection manager for movement validation
    connection_manager._player_combat_service = app.state.player_combat_service
    logger.info("Player combat service initialized and added to app.state and connection_manager")

    # Initialize player death service for death/respawn mechanics
    from ..services.player_death_service import PlayerDeathService

    app.state.player_death_service = PlayerDeathService(event_bus=app.state.event_bus)
    logger.info("Player death service initialized and added to app.state")

    # Initialize player respawn service for resurrection mechanics
    from ..services.player_respawn_service import PlayerRespawnService

    app.state.player_respawn_service = PlayerRespawnService(event_bus=app.state.event_bus)
    logger.info("Player respawn service initialized and added to app.state")

    # Initialize NPC startup spawning
    # Re-enabled to ensure NPCs spawn during server startup
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

    update_logging_with_player_service(app.state.player_service)
    logger.info("Logging system enhanced with PlayerGuidFormatter")

    # Set the main event loop for the EventBus to handle async event handlers
    main_loop = asyncio.get_running_loop()
    app.state.event_handler.event_bus.set_main_loop(main_loop)

    logger.info("Real-time event handler initialized")

    # Initialize NATS service for real-time messaging
    config = get_config()
    nats_config = config.nats

    # Check if we're in a testing environment
    is_testing = config.logging.environment in ("unit_test", "e2e_test")

    if nats_config.enabled:
        logger.info("Initializing NATS service for real-time messaging")
        try:
            # Configure NATS service with config
            nats_service.config = nats_config

            # Connect to NATS server
            connected = await nats_service.connect()
            if connected:
                logger.info("NATS service connected successfully")
                app.state.nats_service = nats_service

                # Initialize combat service now that NATS service is available
                from ..services.combat_service import CombatService

                app.state.combat_service = CombatService(app.state.player_combat_service, app.state.nats_service)

                # Update global combat service instance for tests and other modules
                from ..services.combat_service import set_combat_service

                set_combat_service(app.state.combat_service)

                # Update PlayerService with combat service and player combat service for dynamic combat state checking
                app.state.player_service.combat_service = app.state.combat_service
                app.state.player_service.player_combat_service = app.state.player_combat_service
                logger.info("Combat service initialized and added to app.state")

                # Initialize NATS message handler
                try:
                    # Get subject manager from NATS service if available
                    subject_manager = getattr(nats_service, "subject_manager", None)
                    nats_message_handler = get_nats_message_handler(nats_service, subject_manager)
                    await nats_message_handler.start()
                    app.state.nats_message_handler = nats_message_handler
                    logger.info("NATS message handler started successfully")
                except Exception as e:
                    logger.error("Error initializing NATS message handler", error=str(e))
                    app.state.nats_message_handler = None
            else:
                if is_testing:
                    # In test environment, NATS connection failure is not fatal
                    logger.warning("Failed to connect to NATS server in test environment - using mock NATS service")
                    app.state.nats_service = None
                    app.state.nats_message_handler = None
                else:
                    logger.error("Failed to connect to NATS server - NATS is required for chat functionality")
                    raise RuntimeError("NATS connection failed - NATS is mandatory for chat system")
        except Exception as e:
            if is_testing:
                # In test environment, NATS errors are not fatal
                logger.warning(
                    "NATS initialization failed in test environment", error=str(e), message="continuing without NATS"
                )
                app.state.nats_service = None
                app.state.nats_message_handler = None
            else:
                logger.error("Error initializing NATS service", error=str(e))
                raise RuntimeError(f"NATS initialization failed: {str(e)} - NATS is mandatory for chat system") from e
    else:
        if is_testing:
            # In test environment, NATS can be disabled
            logger.info("NATS service disabled in test environment - using mock NATS service")
            app.state.nats_service = None
            app.state.nats_message_handler = None
        else:
            logger.error("NATS service disabled - NATS is mandatory for chat functionality")
            raise RuntimeError("NATS service is disabled - NATS is mandatory for chat system")

    # Initialize chat service and add to app.state (after NATS initialization)
    from ..game.chat_service import ChatService

    # Initialize chat service with required dependencies using proper dependency injection
    app.state.chat_service = ChatService(
        persistence=app.state.persistence,
        room_service=app.state.persistence,  # Persistence layer provides room service functionality
        player_service=app.state.player_service,
        nats_service=app.state.nats_service if hasattr(app.state, "nats_service") else None,
    )

    # Verify NATS service connection in chat service
    if app.state.chat_service.nats_service and app.state.chat_service.nats_service.is_connected():
        logger.info("Chat service NATS connection verified - NATS is connected and ready")
    elif is_testing:
        logger.info("Chat service running in test mode without NATS connection")
    else:
        logger.error("Chat service NATS connection failed - NATS is not connected")
        raise RuntimeError("Chat service NATS connection failed - NATS is mandatory for chat system")

    logger.info("Chat service added to app.state")
    logger.info("Chat service initialized", chat_service=app.state.chat_service)

    # Start the game tick loop using TaskRegistry
    tick_task = app.state.task_registry.register_task(game_tick_loop(app), "lifecycle/game_tick_loop", "lifecycle")
    app.state.tick_task = tick_task
    logger.info("MythosMUD server started successfully")
    yield

    # Shutdown logic - Enhanced with centralized TaskRegistry coordination
    logger.info("Shutting down MythosMUD server...")

    # Phase 1: Stop services using nuinepTs'dh-ḥāks logic
    try:
        # Stop NATS message handler if running
        if hasattr(app.state, "nats_message_handler") and app.state.nats_message_handler:
            logger.info("Stopping NATS message handler")
            try:
                await app.state.nats_message_handler.stop()
                logger.info("NATS message handler stopped successfully")
            except Exception as e:
                logger.error("Error stopping NATS message handler", error=str(e))

        # Disconnect NATS service if connected
        if hasattr(app.state, "nats_service") and app.state.nats_service:
            logger.info("Disconnecting NATS service")
            try:
                await app.state.nats_service.disconnect()
                logger.info("NATS service disconnected successfully")
            except Exception as e:
                logger.error("Error disconnecting NATS service", error=str(e))

        # Phase 2: Connection Manager cleanup before task cancellation
        if hasattr(app.state, "connection_manager") and app.state.connection_manager:
            logger.info("Cleaning up connection manager tasks")
            try:
                await app.state.connection_manager.force_cleanup()
            except Exception as e:
                logger.error("Error during connection manager cleanup", error=str(e))

        # Phase 3: TaskRegistry shutdown coordination with enhanced reprocation logic
        if hasattr(app.state, "task_registry") and app.state.task_registry:
            logger.info("Executing TaskRegistry graceful shutdown coordination")
            try:
                shutdown_success = await app.state.task_registry.shutdown_all(timeout=5.0)
                if shutdown_success:
                    logger.info("All tasks cancelled gracefully pursuant to dark arts of task-registry coordination")
                else:
                    logger.warning(
                        "TaskRegistry shutdown reached timeout - forcing static termination of remaining tasks"
                    )
            except Exception as e:
                logger.error("TaskRegistry shutdown coordination error", error=str(e))
                # Proceedings continue unless critical failure
        else:
            logger.warning("No TaskRegistry found in shutdown phase - falling back to manual task cancellation")

            # Manual cleanup fallback logic  if no task registry present for handling legacy state
            current_task = asyncio.current_task()
            remaining_tasks = [task for task in asyncio.all_tasks() if task is not current_task and not task.done()]
            if remaining_tasks:
                logger.info("Manual cleanup of orphaned tasks", task_count=len(remaining_tasks))
                for task in remaining_tasks:
                    task.cancel()
                await asyncio.gather(*remaining_tasks, return_exceptions=True)
    except (asyncio.CancelledError, KeyboardInterrupt) as e:
        logger.warning("Shutdown interrupted", error=str(e), error_type=type(e).__name__)
        raise
    except Exception as e:
        logger.error("Critical shutdown failure:", exc_info=True)
        logger.error("Lifespan shutdown failed", error=str(e), error_type=type(e).__name__)
    finally:
        # Phase 4: Database cleanup
        logger.info("Closing database connections")
        try:
            from ..database import close_db

            await close_db()
            logger.info("Database connections closed successfully")
        except (asyncio.CancelledError, KeyboardInterrupt) as e:
            logger.warning("Database cleanup interrupted", error=str(e), error_type=type(e).__name__)
            raise
        except Exception as e:
            logger.error("Error closing database connections", error=str(e), error_type=type(e).__name__)

        logger.info("MythosMUD server shutdown execution phase completed")

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
                    from ..models.player import Player

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

                            # Also check for players already at death threshold who need limbo transition
                            # This handles players who died but haven't been moved to limbo yet
                            result = await session.execute(select(Player))
                            all_players = result.scalars().all()
                            for player in all_players:
                                stats = player.get_stats()
                                current_hp = stats.get("current_health", 0)

                                # If player is dead and not in limbo, move them there
                                if current_hp <= -10 and player.current_room_id != "limbo_death_void":
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

                        except Exception as e:
                            logger.error("Error in HP decay processing iteration", error=str(e))

                        # Only need one session iteration - break after first session
                        break
                except Exception as e:
                    logger.error("Error processing HP decay", tick_count=tick_count, error=str(e))

            # Broadcast game tick to all connected players
            tick_data = {
                "tick_number": tick_count,
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
                "active_players": len(connection_manager.player_websockets),
            }
            logger.debug(
                "Broadcasting game tick", tick_count=tick_count, player_count=len(connection_manager.player_websockets)
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
