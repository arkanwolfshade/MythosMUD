"""FastAPI dependency providers for MythosMUD (ApplicationContainer-backed)."""

from typing import TYPE_CHECKING, Any, cast

from fastapi import Depends, Request

from .container import ApplicationContainer
from .game.chat_service import ChatService
from .game.item_catalog_service import ItemCatalogService
from .game.level_service import LevelService
from .game.magic.mp_regeneration_service import MPRegenerationService
from .game.player_service import PlayerService
from .game.profession_service import ProfessionService
from .game.quest import QuestService
from .game.room_service import RoomService
from .game.skill_service import SkillService
from .game.stats_generator import StatsGenerator
from .npc.lifecycle_manager import NPCLifecycleManager
from .npc.population_control import NPCPopulationController
from .npc.spawning_service import NPCSpawningService
from .persistence.repositories.item_catalog_repository import ItemCatalogRepository
from .persistence.repositories.skill_repository import SkillRepository
from .services.catatonia_registry import CatatoniaRegistry
from .services.combat_service import CombatService
from .services.passive_lucidity_flux_service import PassiveLucidityFluxService
from .services.player_combat_service import PlayerCombatService
from .services.player_death_service import PlayerDeathService
from .services.player_respawn_service import PlayerRespawnService
from .structured_logging.enhanced_logging_config import get_logger
from .time.time_event_consumer import MythosTimeEventConsumer

if TYPE_CHECKING:
    from .async_persistence import AsyncPersistenceLayer
    from .game.magic.magic_service import MagicService
    from .game.magic.spell_effects import SpellEffects
    from .game.magic.spell_learning_service import SpellLearningService
    from .game.magic.spell_registry import SpellRegistry
    from .game.magic.spell_targeting import SpellTargetingService
    from .realtime.connection_manager import ConnectionManager
    from .services.exploration_service import ExplorationService

logger = get_logger(__name__)


def get_container(request: Request) -> ApplicationContainer:
    """Get the application container from request state."""
    if not hasattr(request.app.state, "container"):
        raise RuntimeError(
            "ApplicationContainer not found in app.state - ensure container is initialized in lifespan context"
        )
    return cast(ApplicationContainer, request.app.state.container)


def get_player_service(request: Request) -> PlayerService:
    """Get a PlayerService instance with dependency injection."""
    logger.debug("Retrieving PlayerService from container")
    container = get_container(request)

    if container.player_service is None:
        raise RuntimeError("PlayerService not initialized in container")

    return cast(PlayerService, container.player_service)


def get_level_service(request: Request) -> LevelService:
    """Get a LevelService instance with dependency injection."""
    logger.debug("Retrieving LevelService from container")
    container = get_container(request)

    if container.level_service is None:
        raise RuntimeError("LevelService not initialized in container")

    return cast(LevelService, container.level_service)


def get_player_service_for_testing(player_service: PlayerService | None = None) -> PlayerService:
    """Get a PlayerService instance for testing purposes."""
    if player_service is not None:
        return player_service

    # Create a minimal mock for testing
    from unittest.mock import Mock

    mock_persistence = Mock()
    return PlayerService(mock_persistence)


def get_room_service(request: Request) -> RoomService:
    """Get a RoomService instance with dependency injection."""
    logger.debug("Retrieving RoomService from container")
    container = get_container(request)

    if container.room_service is None:
        raise RuntimeError("RoomService not initialized in container")

    return cast(RoomService, container.room_service)


def get_stats_generator() -> StatsGenerator:
    """Get a StatsGenerator instance via dependency injection."""
    return StatsGenerator()


def get_connection_manager(request: Request) -> "ConnectionManager":
    """Get a ConnectionManager instance with dependency injection."""
    logger.debug("Retrieving ConnectionManager from container")
    container = get_container(request)

    if container.connection_manager is None:
        raise RuntimeError("ConnectionManager not initialized in container")

    return cast("ConnectionManager", container.connection_manager)


def get_async_persistence(request: Request) -> "AsyncPersistenceLayer":
    """Get an AsyncPersistenceLayer instance with dependency injection."""
    logger.debug("Retrieving AsyncPersistenceLayer from container")
    container = get_container(request)

    if container.async_persistence is None:
        raise RuntimeError("AsyncPersistenceLayer not initialized in container")

    return cast("AsyncPersistenceLayer", container.async_persistence)


def get_exploration_service(request: Request) -> "ExplorationService":
    """Get an ExplorationService instance with dependency injection."""
    logger.debug("Retrieving ExplorationService from container")
    container = get_container(request)

    if container.exploration_service is None:
        raise RuntimeError("ExplorationService not initialized in container")

    return cast("ExplorationService", container.exploration_service)


def get_player_respawn_service(request: Request) -> "PlayerRespawnService":
    """Get a PlayerRespawnService instance with dependency injection."""
    logger.debug("Retrieving PlayerRespawnService from container")
    container = get_container(request)

    if container.player_respawn_service is None:
        raise RuntimeError("PlayerRespawnService not initialized in container")

    return cast(PlayerRespawnService, container.player_respawn_service)


# Dependency injection type aliases for use in route handlers
ContainerDep = Depends(get_container)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
PlayerServiceDep = Depends(get_player_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
LevelServiceDep = Depends(get_level_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
RoomServiceDep = Depends(get_room_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
StatsGeneratorDep = Depends(get_stats_generator)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
ConnectionManagerDep = Depends(get_connection_manager)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
AsyncPersistenceDep = Depends(get_async_persistence)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
ExplorationServiceDep = Depends(get_exploration_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
PlayerRespawnServiceDep = Depends(get_player_respawn_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions


def get_profession_service(request: Request) -> ProfessionService:
    """Get a ProfessionService instance with dependency injection."""
    logger.debug("Retrieving ProfessionService from container")
    persistence = get_async_persistence(request)
    return ProfessionService(persistence)


ProfessionServiceDep = Depends(get_profession_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions


def get_skill_repository() -> SkillRepository:
    """Get a SkillRepository instance for skills catalog queries."""
    return SkillRepository()


SkillRepositoryDep = Depends(get_skill_repository)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions


def get_item_catalog_service() -> ItemCatalogService:
    """Get ItemCatalogService for /catalog and GET /api/item-catalog."""
    return ItemCatalogService(ItemCatalogRepository())


def get_skill_service(request: Request) -> SkillService:
    """Get SkillService from container (set_player_skills, get_player_skills)."""
    logger.debug("Retrieving SkillService from container")
    container = get_container(request)
    if container.skill_service is None:
        raise RuntimeError("SkillService not initialized in container")
    return cast(SkillService, container.skill_service)


SkillServiceDep = Depends(get_skill_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions


def get_quest_service(request: Request) -> QuestService:
    """Get QuestService from container (quest log, start, progress, abandon)."""
    logger.debug("Retrieving QuestService from container")
    container = get_container(request)
    if container.quest_service is None:
        raise RuntimeError("QuestService not initialized in container")
    return cast(QuestService, container.quest_service)


QuestServiceDep = Depends(get_quest_service)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions


# Combat service dependency injection functions
def get_player_combat_service(request: Request) -> "PlayerCombatService":
    """Get a PlayerCombatService instance with dependency injection."""
    logger.debug("Retrieving PlayerCombatService from container")
    container = get_container(request)

    if container.player_combat_service is None:
        raise RuntimeError("PlayerCombatService not initialized in container")

    return cast(PlayerCombatService, container.player_combat_service)


def get_player_death_service(request: Request) -> "PlayerDeathService":
    """Get a PlayerDeathService instance with dependency injection."""
    logger.debug("Retrieving PlayerDeathService from container")
    container = get_container(request)

    if container.player_death_service is None:
        raise RuntimeError("PlayerDeathService not initialized in container")

    return cast(PlayerDeathService, container.player_death_service)


def get_combat_service(request: Request) -> "CombatService":
    """Get a CombatService instance with dependency injection."""
    logger.debug("Retrieving CombatService from container")
    container = get_container(request)

    if container.combat_service is None:
        raise RuntimeError("CombatService not initialized in container")

    return cast(CombatService, container.combat_service)


# Magic service dependency injection functions
def get_magic_service(request: Request) -> "MagicService":
    """Get a MagicService instance with dependency injection."""
    logger.debug("Retrieving MagicService from container")
    container = get_container(request)

    if container.magic_service is None:
        raise RuntimeError("MagicService not initialized in container")

    # Import here to avoid circular dependency
    from .game.magic.magic_service import MagicService  # noqa: PLC0415

    return cast(MagicService, container.magic_service)


def get_spell_registry(request: Request) -> "SpellRegistry":
    """Get a SpellRegistry instance with dependency injection."""
    logger.debug("Retrieving SpellRegistry from container")
    container = get_container(request)

    if container.spell_registry is None:
        raise RuntimeError("SpellRegistry not initialized in container")

    # Import here to avoid circular dependency
    from .game.magic.spell_registry import SpellRegistry  # noqa: PLC0415

    return cast(SpellRegistry, container.spell_registry)


def get_spell_targeting_service(request: Request) -> "SpellTargetingService":
    """Get a SpellTargetingService instance with dependency injection."""
    logger.debug("Retrieving SpellTargetingService from container")
    container = get_container(request)

    if container.spell_targeting_service is None:
        raise RuntimeError("SpellTargetingService not initialized in container")

    # Import here to avoid circular dependency
    from .game.magic.spell_targeting import SpellTargetingService  # noqa: PLC0415

    return cast(SpellTargetingService, container.spell_targeting_service)


def get_spell_effects(request: Request) -> "SpellEffects":
    """Get a SpellEffects instance with dependency injection."""
    logger.debug("Retrieving SpellEffects from container")
    container = get_container(request)

    if container.spell_effects is None:
        raise RuntimeError("SpellEffects not initialized in container")

    # Import here to avoid circular dependency
    from .game.magic.spell_effects import SpellEffects  # noqa: PLC0415

    return cast(SpellEffects, container.spell_effects)


def get_spell_learning_service(request: Request) -> "SpellLearningService":
    """Get a SpellLearningService instance with dependency injection."""
    logger.debug("Retrieving SpellLearningService from container")
    container = get_container(request)

    if container.spell_learning_service is None:
        raise RuntimeError("SpellLearningService not initialized in container")

    # Import here to avoid circular dependency
    from .game.magic.spell_learning_service import SpellLearningService  # noqa: PLC0415

    return cast(SpellLearningService, container.spell_learning_service)


def get_mp_regeneration_service(request: Request) -> "MPRegenerationService":
    """Get an MPRegenerationService instance with dependency injection."""
    logger.debug("Retrieving MPRegenerationService from container")
    container = get_container(request)

    if container.mp_regeneration_service is None:
        raise RuntimeError("MPRegenerationService not initialized in container")

    return cast(MPRegenerationService, container.mp_regeneration_service)


# NPC service dependency injection functions
def get_npc_lifecycle_manager(request: Request) -> "NPCLifecycleManager":
    """Get an NPCLifecycleManager instance with dependency injection."""
    logger.debug("Retrieving NPCLifecycleManager from container")
    container = get_container(request)

    if container.npc_lifecycle_manager is None:
        raise RuntimeError("NPCLifecycleManager not initialized in container")

    return cast(NPCLifecycleManager, container.npc_lifecycle_manager)


def get_npc_spawning_service(request: Request) -> "NPCSpawningService":
    """Get an NPCSpawningService instance with dependency injection."""
    logger.debug("Retrieving NPCSpawningService from container")
    container = get_container(request)

    if container.npc_spawning_service is None:
        raise RuntimeError("NPCSpawningService not initialized in container")

    return cast(NPCSpawningService, container.npc_spawning_service)


def get_npc_population_controller(request: Request) -> "NPCPopulationController":
    """Get an NPCPopulationController instance with dependency injection."""
    logger.debug("Retrieving NPCPopulationController from container")
    container = get_container(request)

    if container.npc_population_controller is None:
        raise RuntimeError("NPCPopulationController not initialized in container")

    return cast(NPCPopulationController, container.npc_population_controller)


# Other service dependency injection functions
def get_catatonia_registry(request: Request) -> "CatatoniaRegistry":
    """Get a CatatoniaRegistry instance with dependency injection."""
    logger.debug("Retrieving CatatoniaRegistry from container")
    container = get_container(request)

    if container.catatonia_registry is None:
        raise RuntimeError("CatatoniaRegistry not initialized in container")

    return cast(CatatoniaRegistry, container.catatonia_registry)


def get_passive_lucidity_flux_service(request: Request) -> "PassiveLucidityFluxService":
    """Get a PassiveLucidityFluxService instance with dependency injection."""
    logger.debug("Retrieving PassiveLucidityFluxService from container")
    container = get_container(request)

    if container.passive_lucidity_flux_service is None:
        raise RuntimeError("PassiveLucidityFluxService not initialized in container")

    return cast(PassiveLucidityFluxService, container.passive_lucidity_flux_service)


def get_mythos_time_consumer(request: Request) -> "MythosTimeEventConsumer":
    """Get a MythosTimeEventConsumer instance with dependency injection."""
    logger.debug("Retrieving MythosTimeEventConsumer from container")
    container = get_container(request)

    if container.mythos_time_consumer is None:
        raise RuntimeError("MythosTimeEventConsumer not initialized in container")

    return cast(MythosTimeEventConsumer, container.mythos_time_consumer)


def get_chat_service(request: Request) -> "ChatService":
    """Get a ChatService instance with dependency injection."""
    logger.debug("Retrieving ChatService from container")
    container = get_container(request)

    if container.chat_service is None:
        raise RuntimeError("ChatService not initialized in container")

    return cast(ChatService, container.chat_service)


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
    """Get NATS message handler from container with dependency injection."""
    container = get_container(request)
    return container.nats_message_handler


NatsMessageHandlerDep = Depends(get_nats_message_handler)  # pylint: disable=invalid-name  # Reason: FastAPI dependency name follows FastAPI conventions
