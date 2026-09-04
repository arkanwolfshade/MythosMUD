"""
Profession service for MythosMUD server.

This module handles profession-related business logic including
data transformation and profession retrieval operations.
"""

from typing import TYPE_CHECKING, Any

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..models.profession import Profession

logger = get_logger(__name__)


class ProfessionService:
    """Service class for profession-related business operations."""

    def __init__(self, persistence: "AsyncPersistenceLayer") -> None:
        """Initialize the profession service with a persistence layer."""
        self.persistence = persistence
        logger.info("ProfessionService initialized")

    def profession_to_dict(self, profession: "Profession") -> dict[str, Any]:
        """
        Convert a Profession model to a dictionary for API responses.

        Args:
            profession: Profession model instance

        Returns:
            dict: Profession data as dictionary with stat_requirements and mechanical_effects
                  converted to list format for ProfessionData schema
        """
        # Convert stat_requirements dict to list of StatRequirement objects
        stat_reqs_dict = profession.get_stat_requirements()
        stat_requirements_list = [
            {"stat": stat_name, "minimum": min_value} for stat_name, min_value in stat_reqs_dict.items()
        ]

        # Convert mechanical_effects dict to list of MechanicalEffect objects
        mech_effects_dict = profession.get_mechanical_effects()
        mechanical_effects_list = []
        for effect_key, effect_value in mech_effects_dict.items():
            # Handle different formats: if value is a dict, use it directly; otherwise create structure
            if isinstance(effect_value, dict):
                mechanical_effects_list.append(effect_value)
            else:
                mechanical_effects_list.append({"effect_type": effect_key, "value": effect_value, "description": None})

        result_dict = {
            "id": profession.id,
            "name": profession.name,
            "description": profession.description,
            "flavor_text": profession.flavor_text,
            "stat_requirements": stat_requirements_list,
            "mechanical_effects": mechanical_effects_list,
            "is_available": profession.is_available,
        }
        return result_dict

    async def get_all_professions_dict(self) -> list[dict[str, Any]]:
        """
        Get all available professions as dictionaries.

        Returns:
            list[dict[str, Any]]: List of profession dictionaries
        """
        professions = await self.persistence.get_professions()
        result = []
        for profession in professions:
            profession_dict = self.profession_to_dict(profession)
            result.append(profession_dict)
        return result

    async def get_profession_by_id_dict(self, profession_id: int) -> dict[str, Any] | None:
        """
        Get a profession by ID as a dictionary.

        Args:
            profession_id: Profession ID

        Returns:
            dict[str, Any] | None: Profession data as dictionary, or None if not found
        """
        profession = await self.persistence.get_profession_by_id(profession_id)
        if not profession:
            return None
        return self.profession_to_dict(profession)

    async def validate_and_get_profession(self, profession_id: int) -> "Profession":
        """
        Validate that a profession exists and return it.

        This method encapsulates the business logic for profession validation,
        ensuring consistent error handling across the application.

        Args:
            profession_id: Profession ID to validate

        Returns:
            Profession: The validated profession model

        Raises:
            ValidationError: If profession_id is None or profession not found
        """
        from ..exceptions import ValidationError

        if profession_id is None:
            raise ValidationError("profession_id is required for profession-based operations")

        profession = await self.persistence.get_profession_by_id(profession_id)
        if not profession:
            raise ValidationError(f"Profession with ID {profession_id} not found")

        return profession
