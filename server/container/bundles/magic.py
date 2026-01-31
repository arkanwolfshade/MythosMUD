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
        if container.async_persistence is None:
            raise RuntimeError("async_persistence must be initialized before magic services")
        if container.player_service is None:
            raise RuntimeError("player_service must be initialized before magic services")
        if container.combat_service is None and container.config.logging.environment not in (
            "unit_test",
            "e2e_test",
        ):
            raise RuntimeError("combat_service must be initialized before magic services in production")

        logger.debug("Initializing magic services...")

        from server.game.magic.magic_service import MagicService
        from server.game.magic.mp_regeneration_service import MPRegenerationService
        from server.game.magic.spell_effects import SpellEffects
        from server.game.magic.spell_learning_service import SpellLearningService
        from server.game.magic.spell_registry import SpellRegistry
        from server.game.magic.spell_targeting import SpellTargetingService
        from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
        from server.persistence.repositories.spell_repository import SpellRepository as SpellRepositoryClass
        from server.services.target_resolution_service import TargetResolutionService

        spell_repository = SpellRepositoryClass()
        player_spell_repository = PlayerSpellRepository()
        logger.info("Spell repositories initialized")

        self.spell_registry = SpellRegistry(spell_repository)
        await self.spell_registry.load_spells()
        spell_count = len(self.spell_registry.get_all_spell_ids())
        logger.info("SpellRegistry initialized and loaded", spell_count=spell_count)

        target_resolution_service = TargetResolutionService(
            persistence=container.async_persistence,
            player_service=container.player_service,
        )
        self.spell_targeting_service = SpellTargetingService(
            target_resolution_service=target_resolution_service,
            combat_service=container.combat_service,
            player_combat_service=container.player_combat_service,
        )
        logger.info("SpellTargetingService initialized")

        self.spell_effects = SpellEffects(player_service=container.player_service)
        logger.info("SpellEffects initialized")

        self.spell_learning_service = SpellLearningService(
            spell_registry=self.spell_registry,
            player_service=container.player_service,
            player_spell_repository=player_spell_repository,
        )
        logger.info("SpellLearningService initialized")

        self.mp_regeneration_service = MPRegenerationService(player_service=container.player_service)
        logger.info("MPRegenerationService initialized")

        self.magic_service = MagicService(
            spell_registry=self.spell_registry,
            player_service=container.player_service,
            spell_targeting_service=self.spell_targeting_service,
            spell_effects=self.spell_effects,
            player_spell_repository=player_spell_repository,
            spell_learning_service=self.spell_learning_service,
            combat_service=container.combat_service,
        )

        if container.combat_service:
            container.combat_service.magic_service = self.magic_service
            logger.info("MagicService linked to CombatService")

        logger.info("MagicService initialized")
        logger.info("All magic system services initialized")
