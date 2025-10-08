"""Application lifecycle management for MythosMUD server.

This module handles application startup and shutdown logic,
including the game tick loop and persistence layer initialization."""

import asyncio
import datetime
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

from ..config_loader import get_config
from ..database import init_db
from ..logging_config import get_logger
from ..npc_database import init_npc_database
from ..persistence import get_persistence
from ..realtime.connection_manager import connection_manager
from ..realtime.event_handler import get_real_time_event_handler
from ..realtime.nats_message_handler import get_nats_message_handler
from ..realtime.sse_handler import broadcast_game_event
from ..services.nats_service import nats_service
from .task_registry import TaskRegistry

logger = get_logger("server.lifespan")
TICK_INTERVAL = 1.0  # seconds

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
    await init_npc_database()
    # Initialize real-time event handler first to obtain its EventBus with task tracking
    app.state.event_handler = get_real_time_event_handler(task_registry=task_registry)
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

    # Initialize critical services and add to app.state
    from ..game.player_service import PlayerService
    from ..services.user_manager import UserManager

    app.state.player_service = PlayerService(app.state.persistence)

    # Initialize UserManager with proper data directory from config
    config = get_config()
    data_dir = config.get("data_dir", "data")

    # Resolve data_dir relative to project root (same logic as logging_config.py)
    data_path = Path(data_dir)
    if not data_path.is_absolute():
        # Find the project root (where pyproject.toml is located)
        current_dir = Path.cwd()
        project_root = None
        for parent in [current_dir] + list(current_dir.parents):
            if (parent / "pyproject.toml").exists():
                project_root = parent
                break

        if project_root:
            data_path = project_root / data_path
            # Resolve to handle any .. or . in the path
            data_path = data_path.resolve()
        else:
            # Fallback to current directory if project root not found
            data_path = current_dir / data_path
            data_path = data_path.resolve()

    user_management_dir = data_path / "user_management"
    app.state.user_manager = UserManager(data_dir=user_management_dir)

    logger.info("Critical services (player_service, user_manager) added to app.state")
    logger.info(f"app.state.player_service: {app.state.player_service}")
    logger.info(f"app.state.user_manager: {app.state.user_manager}")

    # Initialize NPC services
    from ..npc.lifecycle_manager import NPCLifecycleManager
    from ..npc.population_control import NPCPopulationController
    from ..npc.spawning_service import NPCSpawningService
    from ..services.npc_instance_service import initialize_npc_instance_service
    from ..services.npc_service import NPCService

    # Create NPC services
    # Create spawning service first (it doesn't depend on population controller)
    app.state.npc_spawning_service = NPCSpawningService(app.state.event_bus, None)
    # Create population controller with spawning service
    app.state.npc_population_controller = NPCPopulationController(app.state.event_bus, app.state.npc_spawning_service)
    # Update spawning service to use population controller
    app.state.npc_spawning_service.population_controller = app.state.npc_population_controller
    app.state.npc_lifecycle_manager = NPCLifecycleManager(
        app.state.event_bus, app.state.npc_population_controller, app.state.npc_spawning_service
    )

    # Initialize the NPC instance service
    initialize_npc_instance_service(
        lifecycle_manager=app.state.npc_lifecycle_manager,
        spawning_service=app.state.npc_spawning_service,
        population_controller=app.state.npc_population_controller,
        event_bus=app.state.event_bus,
    )

    # Load NPC definitions and spawn rules from database
    from ..npc_database import get_npc_async_session

    npc_service = NPCService()
    async for npc_session in get_npc_async_session():
        try:
            # Load NPC definitions
            definitions = await npc_service.get_npc_definitions(npc_session)
            app.state.npc_population_controller.load_npc_definitions(definitions)
            logger.info(f"Loaded {len(definitions)} NPC definitions")

            # Load spawn rules
            spawn_rules = await npc_service.get_spawn_rules(npc_session)
            app.state.npc_population_controller.load_spawn_rules(spawn_rules)
            logger.info(f"Loaded {len(spawn_rules)} NPC spawn rules")

        except Exception as e:
            logger.error(f"Error loading NPC definitions and spawn rules: {e}")
        break

    logger.info("NPC services initialized and added to app.state")

    # Initialize NPC startup spawning - DISABLED TO PREVENT DUPLICATION
    # Multiple systems were spawning NPCs during startup causing duplication
    # Only the NPC Population Controller should handle startup spawning
    # from ..services.npc_startup_service import get_npc_startup_service

    # logger.info("Starting NPC startup spawning process")
    # try:
    #     startup_service = get_npc_startup_service()
    #     startup_results = await startup_service.spawn_npcs_on_startup()

    #     logger.info(
    #         "NPC startup spawning completed",
    #         context={
    #             "total_spawned": startup_results["total_spawned"],
    #             "required_spawned": startup_results["required_spawned"],
    #             "optional_spawned": startup_results["optional_spawned"],
    #             "failed_spawns": startup_results["failed_spawns"],
    #             "errors": len(startup_results["errors"]),
    #         },
    #     )

    #     # Log any errors that occurred during startup
    #     if startup_results["errors"]:
    #         logger.warning(f"NPC startup spawning had {len(startup_results['errors'])} errors")
    #         for error in startup_results["errors"]:
    #             logger.warning(f"Startup spawning error: {error}")

    # except Exception as e:
    #     logger.error(f"Critical error during NPC startup spawning: {str(e)}")
    #     # Don't fail server startup due to NPC spawning issues
    #     logger.warning("Continuing server startup despite NPC spawning errors")

    logger.info("NPC startup spawning DISABLED to prevent duplication - using Population Controller only")

    # Enhance logging system with PlayerGuidFormatter now that player service is available
    from ..logging_config import update_logging_with_player_service

    update_logging_with_player_service(app.state.player_service)
    logger.info("Logging system enhanced with PlayerGuidFormatter")

    # Set the main event loop for the EventBus to handle async event handlers
    main_loop = asyncio.get_running_loop()
    app.state.event_handler.event_bus.set_main_loop(main_loop)

    logger.info("Real-time event handler initialized")

    # Initialize NATS service for real-time messaging
    config = get_config()
    nats_config = config.get("nats", {})

    if nats_config.get("enabled", False):
        logger.info("Initializing NATS service for real-time messaging")
        try:
            # Configure NATS service with config
            nats_service.config = nats_config

            # Connect to NATS server
            connected = await nats_service.connect()
            if connected:
                logger.info("NATS service connected successfully")
                app.state.nats_service = nats_service

                # Initialize NATS message handler
                try:
                    nats_message_handler = get_nats_message_handler(nats_service)
                    await nats_message_handler.start()
                    app.state.nats_message_handler = nats_message_handler
                    logger.info("NATS message handler started successfully")
                except Exception as e:
                    logger.error("Error initializing NATS message handler", error=str(e))
                    app.state.nats_message_handler = None
            else:
                logger.error("Failed to connect to NATS server - NATS is required for chat functionality")
                raise RuntimeError("NATS connection failed - NATS is mandatory for chat system")
        except Exception as e:
            logger.error("Error initializing NATS service", error=str(e))
            raise RuntimeError(f"NATS initialization failed: {str(e)} - NATS is mandatory for chat system") from e
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
        nats_service=app.state.nats_service,  # Pass the properly configured NATS service
    )

    # Verify NATS service connection in chat service
    if app.state.chat_service.nats_service and app.state.chat_service.nats_service.is_connected():
        logger.info("Chat service NATS connection verified - NATS is connected and ready")
    else:
        logger.error("Chat service NATS connection failed - NATS is not connected")
        raise RuntimeError("Chat service NATS connection failed - NATS is mandatory for chat system")

    logger.info("Chat service added to app.state")
    logger.info(f"app.state.chat_service: {app.state.chat_service}")

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
                logger.error(f"Error during connection manager cleanup: {e}")

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
                logger.error(f"TaskRegistry shutdown coordination error: {e}")
                # Proceedings continue unless critical failure
        else:
            logger.warning("No TaskRegistry found in shutdown phase - falling back to manual task cancellation")

            # Manual cleanup fallback logic  if no task registry present for handling legacy state
            current_task = asyncio.current_task()
            remaining_tasks = [task for task in asyncio.all_tasks() if task is not current_task and not task.done()]
            if remaining_tasks:
                logger.info(f"Manual cleanup of {len(remaining_tasks)} orphaned tasks")
                for task in remaining_tasks:
                    task.cancel()
                await asyncio.gather(*remaining_tasks, return_exceptions=True)
    except Exception as e:
        logger.error("Critical shutdown failure:", exc_info=True)
        logger.error(f"Lifespan shutdown failed with error: {e}")
    finally:
        logger.info("MythosMUD server shutdown execution phase completed")

    logger.info("MythosMUD server shutdown complete")


async def game_tick_loop(app: FastAPI):
    """Main game tick loop.

    This function runs continuously and handles periodic game updates,
    including broadcasting tick information to connected players."""
    tick_count = 0
    logger.info("Game tick loop started")

    while True:
        try:
            # TODO: Implement status/effect ticks using persistence layer
            logger.debug(f"Game tick {tick_count}")

            # Broadcast game tick to all connected players
            tick_data = {
                "tick_number": tick_count,
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
                "active_players": len(connection_manager.player_websockets),
            }
            await broadcast_game_event("game_tick", tick_data)
            tick_count += 1
            await asyncio.sleep(TICK_INTERVAL)
        except asyncio.CancelledError:
            logger.info("Game tick loop cancelled")
            break
        except Exception as e:
            logger.error(f"Error in game tick loop: {e}")
            await asyncio.sleep(TICK_INTERVAL)
