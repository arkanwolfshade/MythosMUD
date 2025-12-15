"""
Spell registry for managing the global spell database.

This module provides an in-memory cache of all spells loaded from the database,
with methods for lookup, filtering, and searching.
"""

from sqlalchemy.exc import SQLAlchemyError

from server.logging.enhanced_logging_config import get_logger
from server.models.spell import Spell, SpellSchool
from server.persistence.repositories.spell_repository import SpellRepository

logger = get_logger(__name__)


class SpellRegistry:
    """
    In-memory registry for all spells.

    Loads spells from the database on initialization and provides
    fast lookup methods for spell operations.
    """

    def __init__(self, spell_repository: SpellRepository | None = None):
        """
        Initialize the spell registry.

        Args:
            spell_repository: Optional SpellRepository instance.
                If None, creates a new one.
        """
        self._spell_repository = spell_repository or SpellRepository()
        self._spells: dict[str, Spell] = {}
        self._loaded = False
        logger.info("SpellRegistry initialized")

    async def load_spells(self) -> None:
        """
        Load all spells from the database into memory.

        This should be called during application startup.
        """
        if self._loaded:
            logger.debug("Spells already loaded, skipping")
            return

        logger.info("Loading spells from database")
        try:
            spell_data = await self._spell_repository.get_all_spells()
            self._spells = {}

            for spell_dict in spell_data:
                try:
                    # Convert materials from JSONB to list of SpellMaterial
                    if "materials" in spell_dict and isinstance(spell_dict["materials"], list):
                        from server.models.spell import SpellMaterial

                        materials = [SpellMaterial(**m) if isinstance(m, dict) else m for m in spell_dict["materials"]]
                        spell_dict["materials"] = materials

                    spell = Spell.model_validate(spell_dict)
                    self._spells[spell.spell_id] = spell
                except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError) as e:
                    logger.warning("Failed to load spell", spell_id=spell_dict.get("spell_id"), error=str(e))

            self._loaded = True
            logger.info("Spells loaded successfully", spell_count=len(self._spells))
        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError) as e:
            logger.error("Failed to load spells", error=str(e))
            raise

    def get_spell(self, spell_id: str) -> Spell | None:
        """
        Get a spell by ID.

        Args:
            spell_id: The spell ID to look up

        Returns:
            Spell | None: The spell if found, None otherwise
        """
        if not self._loaded:
            logger.warning("Spells not loaded, returning None", spell_id=spell_id)
            return None

        return self._spells.get(spell_id)

    def get_spell_by_name(self, name: str) -> Spell | None:
        """
        Get a spell by name using fuzzy matching (case-insensitive).

        Uses the same fuzzy matching heuristics as item and NPC name resolution:
        1. Exact match (highest priority)
        2. Starts with match (high priority)
        3. Contains match (lower priority)

        Args:
            name: The spell name to look up

        Returns:
            Spell | None: The spell if found, None otherwise
        """
        if not self._loaded:
            logger.warning("Spells not loaded, returning None", spell_name=name)
            return None

        normalized = name.strip().lower()
        if not normalized:
            return None

        # Priority 1: Exact match (case-insensitive)
        for spell in self._spells.values():
            if spell.name.lower() == normalized:
                logger.debug("Spell found via exact match", spell_name=name, matched_spell=spell.name)
                return spell

        # Priority 2: Starts with match
        for spell in self._spells.values():
            if spell.name.lower().startswith(normalized):
                logger.debug("Spell found via starts-with match", spell_name=name, matched_spell=spell.name)
                return spell

        # Priority 3: Contains match (substring)
        for spell in self._spells.values():
            if normalized in spell.name.lower():
                logger.debug("Spell found via contains match", spell_name=name, matched_spell=spell.name)
                return spell

        return None

    def list_spells(self, school: SpellSchool | None = None) -> list[Spell]:
        """
        List all spells, optionally filtered by school.

        Args:
            school: Optional school to filter by

        Returns:
            list[Spell]: List of matching spells
        """
        if not self._loaded:
            logger.warning("Spells not loaded, returning empty list")
            return []

        if school:
            return [spell for spell in self._spells.values() if spell.school == school]
        return list(self._spells.values())

    def search_spells(self, query: str) -> list[Spell]:
        """
        Search spells by name or description.

        Args:
            query: Search query (case-insensitive)

        Returns:
            list[Spell]: List of matching spells
        """
        if not self._loaded:
            logger.warning("Spells not loaded, returning empty list")
            return []

        query_lower = query.lower()
        matches = []
        for spell in self._spells.values():
            if query_lower in spell.name.lower() or query_lower in spell.description.lower():
                matches.append(spell)
        return matches

    def get_all_spell_ids(self) -> list[str]:
        """
        Get all spell IDs.

        Returns:
            list[str]: List of all spell IDs
        """
        return list(self._spells.keys())

    def is_loaded(self) -> bool:
        """Check if spells have been loaded."""
        return self._loaded
