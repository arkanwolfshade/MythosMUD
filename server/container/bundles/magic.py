"""
Magic bundle: spell registry, targeting, effects, learning, MP regen, magic service.

Depends on Core (async_persistence), Game (player_service), Combat (combat_service, player_combat_service).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

MAGIC_ATTRS = (
    "spell_registry",
    "spell_targeting_service",
    "spell_effects",
    "spell_learning_service",
    "mp_regeneration_service",
    "magic_service",
)


def _validate_magic_prerequisites(container: ApplicationContainer) -> None:
    """Raise if prerequisites for magic services are missing."""
    if container.async_persistence is None:
        raise RuntimeError("async_persistence must be initialized before magic services")
    if container.player_service is None:
        raise RuntimeError("player_service must be initialized before magic services")
    if container.combat_service is None and container.config.logging.environment not in (
        "unit_test",
        "e2e_test",
    ):
        raise RuntimeError("combat_service must be initialized before magic services in production")


async def _create_registry_and_targeting(bundle: MagicBundle, container: ApplicationContainer) -> tuple[Any, Any]:
    """Create spell registry, targeting, and effects services. Return (spell_registry, player_spell_repository)."""
    from server.game.magic.spell_effects import SpellEffects
    from server.game.magic.spell_registry import SpellRegistry
    from server.game.magic.spell_targeting import SpellTargetingService
    from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
    from server.persistence.repositories.spell_repository import SpellRepository as SpellRepositoryClass
    from server.services.target_resolution_service import TargetResolutionService

    spell_repository = SpellRepositoryClass()
    player_spell_repository = PlayerSpellRepository()
    logger.info("Spell repositories initialized")

    bundle.spell_registry = SpellRegistry(spell_repository)
    await bundle.spell_registry.load_spells()
    spell_count = len(bundle.spell_registry.get_all_spell_ids())
    logger.info("SpellRegistry initialized and loaded", spell_count=spell_count)

    target_resolution_service = TargetResolutionService(
        persistence=container.async_persistence,
        player_service=container.player_service,
    )
    bundle.spell_targeting_service = SpellTargetingService(
        target_resolution_service=target_resolution_service,
        combat_service=container.combat_service,
        player_combat_service=container.player_combat_service,
    )
    logger.info("SpellTargetingService initialized")

    bundle.spell_effects = SpellEffects(
        player_service=container.player_service,
        combat_service=container.combat_service,
    )
    logger.info("SpellEffects initialized")

    return bundle.spell_registry, player_spell_repository


def _create_learning_mp_regen_and_magic(
    bundle: MagicBundle, container: ApplicationContainer, player_spell_repository: Any
) -> None:
    """Create spell learning, MP regen, and magic services; link magic to combat."""
    from server.game.magic.magic_service import MagicService
    from server.game.magic.mp_regeneration_service import MPRegenerationService
    from server.game.magic.spell_learning_service import SpellLearningService

    bundle.spell_learning_service = SpellLearningService(
        spell_registry=bundle.spell_registry,
        player_service=container.player_service,
        player_spell_repository=player_spell_repository,
    )
    logger.info("SpellLearningService initialized")

    bundle.mp_regeneration_service = MPRegenerationService(player_service=container.player_service)
    logger.info("MPRegenerationService initialized")

    bundle.magic_service = MagicService(
        bundle.spell_registry,
        container.player_service,
        bundle.spell_targeting_service,
        bundle.spell_effects,
        {
            "player_spell_repository": player_spell_repository,
            "spell_learning_service": bundle.spell_learning_service,
            "combat_service": container.combat_service,
        },
    )

    if container.combat_service:
        container.combat_service.magic_service = bundle.magic_service
        logger.info("MagicService linked to CombatService")

    logger.info("MagicService initialized")
    logger.info("All magic system services initialized")


class MagicBundle:  # pylint: disable=too-few-public-methods
    """Magic system services."""

    spell_registry: Any = None
    spell_targeting_service: Any = None
    spell_effects: Any = None
    spell_learning_service: Any = None
    mp_regeneration_service: Any = None
    magic_service: Any = None

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize magic services."""
        _validate_magic_prerequisites(container)
        logger.debug("Initializing magic services...")
        _, player_spell_repository = await _create_registry_and_targeting(self, container)
        _create_learning_mp_regen_and_magic(self, container, player_spell_repository)
