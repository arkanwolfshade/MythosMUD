"""
Dependency injection providers for MythosMUD server.

This module provides dependency injection functions for services using the
ApplicationContainer pattern, following clean architecture principles and
ensuring proper separation of concerns.

ARCHITECTURE MIGRATION:
This file has been updated to use the ApplicationContainer for dependency injection
instead of directly accessing app.state. This provides better testability and
follows the dependency inversion principle.

As noted in the Pnakotic Manuscripts, proper organization of arcane knowledge
requires clear separation between the presentation layer and the underlying
mysteries. This dependency injection system provides that separation.
"""

# pylint: disable=too-many-lines  # Reason: This file serves as the central dependency injection registry for all services. It contains 20+ getter functions and their corresponding Depends aliases, each following a consistent pattern with proper documentation. Splitting this file would fragment the DI system and reduce discoverability. The line count is justified by the architectural requirement to centralize all DI providers in one location.

from typing import TYPE_CHECKING, Any

from fastapi import Depends, Request

from .container import ApplicationContainer
from .game.player_service import PlayerService
from .game.profession_service import ProfessionService
from .game.room_service import RoomService
from .game.stats_generator import StatsGenerator
from .structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from .async_persistence import AsyncPersistenceLayer
    from .game.chat_service import ChatService

    # Magic services
    from .game.magic.magic_service import MagicService
    from .game.magic.mp_regeneration_service import MPRegenerationService
    from .game.magic.spell_effects import SpellEffects
    from .game.magic.spell_learning_service import SpellLearningService
    from .game.magic.spell_registry import SpellRegistry
    from .game.magic.spell_targeting import SpellTargetingService

    # NPC services
    from .npc.lifecycle_manager import NPCLifecycleManager
    from .npc.population_control import NPCPopulationController
    from .npc.spawning_service import NPCSpawningService
    from .realtime.connection_manager import ConnectionManager

    # Other services
    from .services.catatonia_registry import CatatoniaRegistry
    from .services.combat_service import CombatService
    from .services.exploration_service import ExplorationService
    from .services.passive_lucidity_flux_service import PassiveLucidityFluxService

    # Combat services
    from .services.player_combat_service import PlayerCombatService
    from .services.player_death_service import PlayerDeathService
    from .services.player_respawn_service import PlayerRespawnService
    from .time.time_event_consumer import MythosTimeEventConsumer

logger = get_logger(__name__)


def get_container(request: Request) -> ApplicationContainer:
    """
    Get the application container from request state.

    This is the base dependency that all other dependencies use.

    Args:
        request: The FastAPI request object

    Returns:
        ApplicationContainer: The application container with all services

    AI: This is the root of the dependency injection tree.
        All other dependencies should use this to access services.
    """
    if not hasattr(request.app.state, "container"):
        raise RuntimeError(
            "ApplicationContainer not found in app.state - ensure container is initialized in lifespan context"
        )
    return request.app.state.container


def get_player_service(request: Request) -> PlayerService:
    """
    Get a PlayerService instance with dependency injection.

    This function provides a PlayerService instance from the container,
    ensuring proper dependency injection and avoiding global state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        PlayerService: A configured PlayerService instance

    AI: Migrated from app.state direct access to container-based injection.
        This enables proper testing and follows clean architecture principles.
    """
    logger.debug("Retrieving PlayerService from container")
    container = get_container(request)

    if container.player_service is None:
        raise RuntimeError("PlayerService not initialized in container")

    return container.player_service


def get_player_service_for_testing(player_service: PlayerService | None = None) -> PlayerService:
    """
    Get a PlayerService instance for testing purposes.

    This function allows tests to provide their own PlayerService instance
    or get a mock instance for testing.

    Args:
        player_service: Optional PlayerService instance (for test injection)

    Returns:
        PlayerService: A PlayerService instance for testing

    AI: This provides a test seam without requiring full app context.
        Tests can inject mock dependencies easily.
    """
    if player_service is not None:
        return player_service

    # Create a minimal mock for testing
    from unittest.mock import Mock

    mock_persistence = Mock()
    return PlayerService(mock_persistence)


def get_room_service(request: Request) -> RoomService:
    """
    Get a RoomService instance with dependency injection.

    This function provides a RoomService instance from the container,
    ensuring proper dependency injection and avoiding global state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        RoomService: A configured RoomService instance

    AI: Migrated from app.state direct access to container-based injection.
    """
    logger.debug("Retrieving RoomService from container")
    container = get_container(request)

    if container.room_service is None:
        raise RuntimeError("RoomService not initialized in container")

    return container.room_service


def get_stats_generator() -> StatsGenerator:
    """
    Get a StatsGenerator instance via dependency injection.

    StatsGenerator is stateless and can be safely reused across requests.

    Returns:
        StatsGenerator: A StatsGenerator instance
    """
    return StatsGenerator()


def get_connection_manager(request: Request) -> "ConnectionManager":
    """
    Get a ConnectionManager instance with dependency injection.

    This function provides a ConnectionManager instance from the container,
    ensuring proper dependency injection and avoiding global state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        ConnectionManager: A configured ConnectionManager instance

    AI: Migrated from app.state direct access to container-based injection.
        This enables proper testing and follows clean architecture principles.
    """
    logger.debug("Retrieving ConnectionManager from container")
    container = get_container(request)

    if container.connection_manager is None:
        raise RuntimeError("ConnectionManager not initialized in container")

    return container.connection_manager


def get_async_persistence(request: Request) -> "AsyncPersistenceLayer":
    """
    Get an AsyncPersistenceLayer instance with dependency injection.

    This function provides an AsyncPersistenceLayer instance from the container,
    ensuring proper dependency injection and avoiding global state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        AsyncPersistenceLayer: A configured AsyncPersistenceLayer instance

    AI: Migrated from app.state direct access to container-based injection.
        This enables proper testing and follows clean architecture principles.
    """
    logger.debug("Retrieving AsyncPersistenceLayer from container")
    container = get_container(request)

    if container.async_persistence is None:
        raise RuntimeError("AsyncPersistenceLayer not initialized in container")

    return container.async_persistence


def get_exploration_service(request: Request) -> "ExplorationService":
    """
    Get an ExplorationService instance with dependency injection.

    This function provides an ExplorationService instance from the container,
    ensuring proper dependency injection and avoiding global state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        ExplorationService: A configured ExplorationService instance

    AI: Migrated from app.state direct access to container-based injection.
        This enables proper testing and follows clean architecture principles.
    """
    logger.debug("Retrieving ExplorationService from container")
    container = get_container(request)

    if container.exploration_service is None:
        raise RuntimeError("ExplorationService not initialized in container")

    return container.exploration_service


def get_player_respawn_service(request: Request) -> "PlayerRespawnService":
    """
    Get a PlayerRespawnService instance with dependency injection.

    This function provides a PlayerRespawnService instance from the container,
    ensuring proper dependency injection and avoiding global state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        PlayerRespawnService: A configured PlayerRespawnService instance

    AI: Migrated from app.state direct access to container-based injection.
        This enables proper testing and follows clean architecture principles.
    """
    logger.debug("Retrieving PlayerRespawnService from container")
    container = get_container(request)

    if container.player_respawn_service is None:
        raise RuntimeError("PlayerRespawnService not initialized in container")

    return container.player_respawn_service


# Dependency injection type aliases for use in route handlers
ContainerDep = Depends(get_container)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
PlayerServiceDep = Depends(get_player_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
RoomServiceDep = Depends(get_room_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
StatsGeneratorDep = Depends(get_stats_generator)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
ConnectionManagerDep = Depends(get_connection_manager)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
AsyncPersistenceDep = Depends(get_async_persistence)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
ExplorationServiceDep = Depends(get_exploration_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
PlayerRespawnServiceDep = Depends(get_player_respawn_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions


def get_profession_service(request: Request) -> ProfessionService:
    """
    Get a ProfessionService instance with dependency injection.

    This function provides a ProfessionService instance from the container,
    ensuring proper dependency injection and avoiding global state.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        ProfessionService: A configured ProfessionService instance
    """
    logger.debug("Retrieving ProfessionService from container")
    persistence = get_async_persistence(request)
    return ProfessionService(persistence)


ProfessionServiceDep = Depends(get_profession_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions


# Combat service dependency injection functions
def get_player_combat_service(request: Request) -> "PlayerCombatService":
    """
    Get a PlayerCombatService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        PlayerCombatService: A configured PlayerCombatService instance
    """
    logger.debug("Retrieving PlayerCombatService from container")
    container = get_container(request)

    if container.player_combat_service is None:
        raise RuntimeError("PlayerCombatService not initialized in container")

    return container.player_combat_service


def get_player_death_service(request: Request) -> "PlayerDeathService":
    """
    Get a PlayerDeathService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        PlayerDeathService: A configured PlayerDeathService instance
    """
    logger.debug("Retrieving PlayerDeathService from container")
    container = get_container(request)

    if container.player_death_service is None:
        raise RuntimeError("PlayerDeathService not initialized in container")

    return container.player_death_service


def get_combat_service(request: Request) -> "CombatService":
    """
    Get a CombatService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        CombatService: A configured CombatService instance

    Note: CombatService may be None if NATS is not available in test environments.
    """
    logger.debug("Retrieving CombatService from container")
    container = get_container(request)

    if container.combat_service is None:
        raise RuntimeError("CombatService not initialized in container")

    return container.combat_service


# Magic service dependency injection functions
def get_magic_service(request: Request) -> "MagicService":
    """
    Get a MagicService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        MagicService: A configured MagicService instance
    """
    logger.debug("Retrieving MagicService from container")
    container = get_container(request)

    if container.magic_service is None:
        raise RuntimeError("MagicService not initialized in container")

    return container.magic_service


def get_spell_registry(request: Request) -> "SpellRegistry":
    """
    Get a SpellRegistry instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        SpellRegistry: A configured SpellRegistry instance
    """
    logger.debug("Retrieving SpellRegistry from container")
    container = get_container(request)

    if container.spell_registry is None:
        raise RuntimeError("SpellRegistry not initialized in container")

    return container.spell_registry


def get_spell_targeting_service(request: Request) -> "SpellTargetingService":
    """
    Get a SpellTargetingService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        SpellTargetingService: A configured SpellTargetingService instance
    """
    logger.debug("Retrieving SpellTargetingService from container")
    container = get_container(request)

    if container.spell_targeting_service is None:
        raise RuntimeError("SpellTargetingService not initialized in container")

    return container.spell_targeting_service


def get_spell_effects(request: Request) -> "SpellEffects":
    """
    Get a SpellEffects instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        SpellEffects: A configured SpellEffects instance
    """
    logger.debug("Retrieving SpellEffects from container")
    container = get_container(request)

    if container.spell_effects is None:
        raise RuntimeError("SpellEffects not initialized in container")

    return container.spell_effects


def get_spell_learning_service(request: Request) -> "SpellLearningService":
    """
    Get a SpellLearningService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        SpellLearningService: A configured SpellLearningService instance
    """
    logger.debug("Retrieving SpellLearningService from container")
    container = get_container(request)

    if container.spell_learning_service is None:
        raise RuntimeError("SpellLearningService not initialized in container")

    return container.spell_learning_service


def get_mp_regeneration_service(request: Request) -> "MPRegenerationService":
    """
    Get an MPRegenerationService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        MPRegenerationService: A configured MPRegenerationService instance
    """
    logger.debug("Retrieving MPRegenerationService from container")
    container = get_container(request)

    if container.mp_regeneration_service is None:
        raise RuntimeError("MPRegenerationService not initialized in container")

    return container.mp_regeneration_service


# NPC service dependency injection functions
def get_npc_lifecycle_manager(request: Request) -> "NPCLifecycleManager":
    """
    Get an NPCLifecycleManager instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        NPCLifecycleManager: A configured NPCLifecycleManager instance
    """
    logger.debug("Retrieving NPCLifecycleManager from container")
    container = get_container(request)

    if container.npc_lifecycle_manager is None:
        raise RuntimeError("NPCLifecycleManager not initialized in container")

    return container.npc_lifecycle_manager


def get_npc_spawning_service(request: Request) -> "NPCSpawningService":
    """
    Get an NPCSpawningService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        NPCSpawningService: A configured NPCSpawningService instance
    """
    logger.debug("Retrieving NPCSpawningService from container")
    container = get_container(request)

    if container.npc_spawning_service is None:
        raise RuntimeError("NPCSpawningService not initialized in container")

    return container.npc_spawning_service


def get_npc_population_controller(request: Request) -> "NPCPopulationController":
    """
    Get an NPCPopulationController instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        NPCPopulationController: A configured NPCPopulationController instance
    """
    logger.debug("Retrieving NPCPopulationController from container")
    container = get_container(request)

    if container.npc_population_controller is None:
        raise RuntimeError("NPCPopulationController not initialized in container")

    return container.npc_population_controller


# Other service dependency injection functions
def get_catatonia_registry(request: Request) -> "CatatoniaRegistry":
    """
    Get a CatatoniaRegistry instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        CatatoniaRegistry: A configured CatatoniaRegistry instance
    """
    logger.debug("Retrieving CatatoniaRegistry from container")
    container = get_container(request)

    if container.catatonia_registry is None:
        raise RuntimeError("CatatoniaRegistry not initialized in container")

    return container.catatonia_registry


def get_passive_lucidity_flux_service(request: Request) -> "PassiveLucidityFluxService":
    """
    Get a PassiveLucidityFluxService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        PassiveLucidityFluxService: A configured PassiveLucidityFluxService instance
    """
    logger.debug("Retrieving PassiveLucidityFluxService from container")
    container = get_container(request)

    if container.passive_lucidity_flux_service is None:
        raise RuntimeError("PassiveLucidityFluxService not initialized in container")

    return container.passive_lucidity_flux_service


def get_mythos_time_consumer(request: Request) -> "MythosTimeEventConsumer":
    """
    Get a MythosTimeEventConsumer instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        MythosTimeEventConsumer: A configured MythosTimeEventConsumer instance

    Note: MythosTimeEventConsumer may be None if dependencies are not available.
    """
    logger.debug("Retrieving MythosTimeEventConsumer from container")
    container = get_container(request)

    if container.mythos_time_consumer is None:
        raise RuntimeError("MythosTimeEventConsumer not initialized in container")

    return container.mythos_time_consumer


def get_chat_service(request: Request) -> "ChatService":
    """
    Get a ChatService instance with dependency injection.

    Args:
        request: The FastAPI request object containing app state

    Returns:
        ChatService: A configured ChatService instance
    """
    logger.debug("Retrieving ChatService from container")
    container = get_container(request)

    if container.chat_service is None:
        raise RuntimeError("ChatService not initialized in container")

    return container.chat_service


# Dependency injection type aliases for combat services
PlayerCombatServiceDep = Depends(get_player_combat_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
PlayerDeathServiceDep = Depends(get_player_death_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
CombatServiceDep = Depends(get_combat_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions

# Dependency injection type aliases for magic services
MagicServiceDep = Depends(get_magic_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
SpellRegistryDep = Depends(get_spell_registry)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
SpellTargetingServiceDep = Depends(get_spell_targeting_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
SpellEffectsDep = Depends(get_spell_effects)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
SpellLearningServiceDep = Depends(get_spell_learning_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
MPRegenerationServiceDep = Depends(get_mp_regeneration_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions

# Dependency injection type aliases for NPC services
NPCLifecycleManagerDep = Depends(get_npc_lifecycle_manager)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
NPCSpawningServiceDep = Depends(get_npc_spawning_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
NPCPopulationControllerDep = Depends(get_npc_population_controller)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions

# Dependency injection type aliases for other services
CatatoniaRegistryDep = Depends(get_catatonia_registry)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
PassiveLucidityFluxServiceDep = Depends(get_passive_lucidity_flux_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
MythosTimeEventConsumerDep = Depends(get_mythos_time_consumer)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
ChatServiceDep = Depends(get_chat_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions


def get_nats_message_handler(request: Request) -> Any:
    """
    Get NATS message handler from container with dependency injection.

    Args:
        request: The FastAPI request object

    Returns:
        NATSMessageHandler: The NATS message handler instance (may be None if NATS is disabled)

    Raises:
        RuntimeError: If container is not initialized

    AI: Migrated from app.state direct access to container-based injection.
        This enables proper testing and follows clean architecture principles.
    """
    container = get_container(request)
    return container.nats_message_handler


NatsMessageHandlerDep = Depends(get_nats_message_handler)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
