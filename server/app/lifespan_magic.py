"""Magic system initialization for application startup.

Extracted from lifespan_startup to keep module line count under limit.
"""

from fastapi import FastAPI

from ..container import ApplicationContainer
from ..game.magic.magic_service import MagicService
from ..game.magic.mp_regeneration_service import MPRegenerationService
from ..game.magic.spell_effects import SpellEffects
from ..game.magic.spell_learning_service import SpellLearningService
from ..game.magic.spell_registry import SpellRegistry
from ..game.magic.spell_targeting import SpellTargetingService
from ..persistence.repositories.player_spell_repository import PlayerSpellRepository
from ..persistence.repositories.spell_repository import SpellRepository as SpellRepositoryClass
from ..services.target_resolution_service import TargetResolutionService
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("server.lifespan.magic")


def _validate_magic_prerequisites(container: ApplicationContainer) -> None:
    """Ensure required container services exist before magic initialization."""
    if container.async_persistence is None:
        raise RuntimeError("async_persistence must be initialized before magic services")
    if container.player_service is None:
        raise RuntimeError("player_service must be initialized before magic services")


def _initialize_spell_repositories() -> tuple[SpellRepositoryClass, PlayerSpellRepository]:
    """Create spell-related repositories."""
    spell_repository = SpellRepositoryClass()
    player_spell_repository = PlayerSpellRepository()
    logger.info("Spell repositories initialized")
    return spell_repository, player_spell_repository


async def _initialize_spell_registry(app: FastAPI, spell_repository: SpellRepositoryClass) -> SpellRegistry:
    """Initialize SpellRegistry, load spells, and attach to app.state."""
    spell_registry = SpellRegistry(spell_repository)
    await spell_registry.load_spells()
    spell_count = len(spell_registry._spells)  # pylint: disable=protected-access  # Reason: Accessing internal spell dictionary for initialization logging, SpellRegistry manages this as internal state
    app.state.spell_registry = spell_registry
    logger.info("SpellRegistry initialized and loaded", spell_count=spell_count)
    return spell_registry


def _initialize_spell_targeting_service(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize SpellTargetingService and attach to app.state."""
    target_resolution_service = TargetResolutionService(
        persistence=container.async_persistence,
        player_service=container.player_service,
    )
    spell_targeting_service = SpellTargetingService(
        target_resolution_service=target_resolution_service,
        combat_service=getattr(app.state, "combat_service", None),
        player_combat_service=getattr(app.state, "player_combat_service", None),
    )
    app.state.spell_targeting_service = spell_targeting_service
    logger.info("SpellTargetingService initialized")


def _initialize_spell_effects(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize SpellEffects and attach to app.state."""
    get_room = container.async_persistence.get_room_by_id if container.async_persistence else None
    spell_effects = SpellEffects(
        player_service=container.player_service,
        combat_service=getattr(app.state, "combat_service", None),
        movement_service=getattr(container, "movement_service", None),
        get_room_by_id=get_room,
        connection_manager=getattr(container, "connection_manager", None),
    )
    app.state.spell_effects = spell_effects
    logger.info("SpellEffects initialized")


def _initialize_spell_learning_service(
    app: FastAPI,
    container: ApplicationContainer,
    spell_registry: SpellRegistry,
    player_spell_repository: PlayerSpellRepository,
) -> None:
    """Initialize SpellLearningService and attach to app.state."""
    spell_learning_service = SpellLearningService(
        spell_registry=spell_registry,
        player_service=container.player_service,
        player_spell_repository=player_spell_repository,
    )
    app.state.spell_learning_service = spell_learning_service
    logger.info("SpellLearningService initialized")


def _initialize_mp_regeneration_service(app: FastAPI, container: ApplicationContainer) -> None:
    """Initialize MPRegenerationService and attach to app.state."""
    mp_regeneration_service = MPRegenerationService(player_service=container.player_service)
    app.state.mp_regeneration_service = mp_regeneration_service
    logger.info("MPRegenerationService initialized")


def _initialize_magic_service(
    app: FastAPI,
    container: ApplicationContainer,
    spell_registry: SpellRegistry,
    player_spell_repository: PlayerSpellRepository,
) -> MagicService:
    """Initialize MagicService and attach to app.state."""
    combat_service = getattr(app.state, "combat_service", None)
    spell_targeting_service = getattr(app.state, "spell_targeting_service", None)
    spell_effects = getattr(app.state, "spell_effects", None)
    if not isinstance(spell_targeting_service, SpellTargetingService) or not isinstance(spell_effects, SpellEffects):
        raise RuntimeError("spell_targeting_service and spell_effects must be initialized before MagicService")
    magic_service = MagicService(
        spell_registry,
        container.player_service,
        spell_targeting_service,
        spell_effects,
        {
            "player_spell_repository": player_spell_repository,
            "spell_learning_service": getattr(app.state, "spell_learning_service", None),
            "combat_service": combat_service,
        },
    )
    app.state.magic_service = magic_service
    return magic_service


def _link_magic_to_combat(app: FastAPI, magic_service: MagicService) -> None:
    """Set magic_service reference in combat_service if available."""
    combat_service = getattr(app.state, "combat_service", None)
    if combat_service:
        combat_service.magic_service = magic_service
        logger.info("MagicService linked to CombatService")


async def initialize_magic_services(app: FastAPI, container: ApplicationContainer) -> None:
    """
    Initialize magic system services and wire them to app.state.

    DEPRECATED: This function is no longer called. Magic services are now initialized
    in ApplicationContainer.initialize() via _initialize_magic_services().
    This function is kept for backward compatibility but should not be used.
    """
    _validate_magic_prerequisites(container)

    logger.info("Initializing magic system services...")

    spell_repository, player_spell_repository = _initialize_spell_repositories()
    spell_registry = await _initialize_spell_registry(app, spell_repository)

    _initialize_spell_targeting_service(app, container)
    _initialize_spell_effects(app, container)
    _initialize_spell_learning_service(app, container, spell_registry, player_spell_repository)
    _initialize_mp_regeneration_service(app, container)

    magic_service = _initialize_magic_service(app, container, spell_registry, player_spell_repository)
    _link_magic_to_combat(app, magic_service)

    logger.info("MagicService initialized")
    logger.info("All magic system services initialized and added to app.state")
