"""
Character creation service for MythosMUD server.

This module handles all character creation-related business logic including
stats generation, validation, and character creation with proper error handling.
"""

import uuid
from typing import Any

from pydantic import ValidationError as PydanticValidationError

from ..exceptions import ValidationError
from ..game.stats_generator import StatsGenerator
from ..models import Stats
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class CharacterCreationService:
    """Service class for character creation and stats generation business operations."""

    def __init__(self, player_service: Any) -> None:
        """Initialize the character creation service with a player service."""
        self.player_service = player_service
        self.stats_generator = StatsGenerator()
        logger.info("CharacterCreationService initialized")

    def roll_character_stats(
        self,
        method: str = "3d6",
        required_class: str | None = None,
        max_attempts: int = 50,  # Increased from 10 to improve success rate for profession requirements
        profession_id: int | None = None,
    ) -> dict[str, Any]:
        """
        Roll random stats for character creation.

        Args:
            method: The dice rolling method to use
            required_class: Optional class to validate against
            max_attempts: Maximum number of attempts to meet requirements
            profession_id: Optional profession ID for profession-based rolling

        Returns:
            dict: Stats and validation results

        Raises:
            ValueError: If invalid parameters are provided
        """
        logger.info(
            "Rolling character stats",
            method=method,
            required_class=required_class,
            max_attempts=max_attempts,
            profession_id=profession_id,
        )

        try:
            if profession_id is not None:
                # Use profession-based stat rolling
                # Use default timeout_seconds from RollStatsRequest (5.0) for better success rate
                stats, meets_requirements = self.stats_generator.roll_stats_with_profession(
                    method=method, profession_id=profession_id, max_attempts=max_attempts, timeout_seconds=5.0
                )
                stat_summary = self.stats_generator.get_stat_summary(stats)

                return {
                    "stats": stats.model_dump(),
                    "stat_summary": stat_summary,
                    "profession_id": profession_id,
                    "meets_requirements": meets_requirements,
                    "method_used": method,
                }

            # Use legacy class-based stat rolling
            stats, available_classes = self.stats_generator.roll_stats_with_validation(
                method=method, required_class=required_class, max_attempts=max_attempts
            )
            stat_summary = self.stats_generator.get_stat_summary(stats)

            return {
                "stats": stats.model_dump(),
                "stat_summary": stat_summary,
                "available_classes": available_classes,
                "method_used": method,
                "meets_class_requirements": required_class in available_classes if required_class else True,
            }
        except ValueError as e:
            logger.error("Invalid parameters for stats rolling", error=str(e))
            context = create_error_context()
            context.metadata["operation"] = "roll_stats"
            context.metadata["error"] = str(e)
            log_and_raise(
                ValidationError,
                f"Invalid profession: {str(e)}",
                context=context,
                details={"error": str(e)},
                user_friendly="Invalid parameters provided",
            )

    def validate_character_stats(self, stats: dict[str, Any], class_name: str | None = None) -> dict[str, Any]:
        """
        Validate character stats against class prerequisites.

        Args:
            stats: The stats dictionary to validate
            class_name: Optional class name to validate against

        Returns:
            dict: Validation results

        Raises:
            ValueError: If stats format is invalid
        """
        logger.info("Validating character stats", class_name=class_name)

        try:
            # Convert dict to Stats object
            stats_obj = Stats(**stats)

            if class_name:
                meets_prerequisites, failed_requirements = self.stats_generator.validate_class_prerequisites(
                    stats_obj, class_name
                )
                available_classes = self.stats_generator.get_available_classes(stats_obj)

                return {
                    "meets_prerequisites": meets_prerequisites,
                    "failed_requirements": failed_requirements,
                    "available_classes": available_classes,
                    "requested_class": class_name,
                }

            available_classes = self.stats_generator.get_available_classes(stats_obj)
            stat_summary = self.stats_generator.get_stat_summary(stats_obj)

            return {"available_classes": available_classes, "stat_summary": stat_summary}
        except (ValueError, PydanticValidationError) as e:
            logger.error("Stats validation failed", error=str(e))
            context = create_error_context()
            context.metadata["operation"] = "validate_stats"
            log_and_raise(
                ValidationError,
                "Invalid stats format",
                context=context,
                details={"error": str(e)},
                user_friendly="Invalid stats format provided",
            )

    def create_character_with_stats(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Character creation requires many parameters for stats and configuration
        self,
        name: str,
        stats: dict[str, Any],
        profession_id: int = 0,
        starting_room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001",
        user_id: uuid.UUID | None = None,
    ) -> dict[str, Any]:
        """
        Create a new character with specific stats.

        Args:
            name: The character's name
            stats: The character's stats
            profession_id: The profession ID for the character
            starting_room_id: The room ID where the character starts
            user_id: Optional user ID (will be generated if not provided)

        Returns:
            dict: Creation result with player data and stats

        Raises:
            ValidationError: If character creation fails
        """
        logger.info(
            "Creating character with stats",
            name=name,
            profession_id=profession_id,
            starting_room_id=starting_room_id,
            user_id=user_id,
        )

        try:
            # Convert dict to Stats object
            stats_obj = Stats(**stats)

            # Create player with stats using the player service
            player = self.player_service.create_player_with_stats(
                name=name,
                stats=stats_obj,
                profession_id=profession_id,
                starting_room_id=starting_room_id,
                user_id=user_id,
            )

            logger.info("Character created successfully", name=name, player_id=player.id)

            return {
                "message": f"Character {name} created successfully",
                "player": player.model_dump(),
                "stats": stats_obj.model_dump(),
            }
        except (ValueError, PydanticValidationError, ValidationError) as e:
            logger.error("Character creation failed", name=name, error=str(e))
            context = create_error_context()
            context.metadata["operation"] = "create_character"
            context.metadata["character_name"] = name
            log_and_raise(
                ValidationError,
                "Character creation failed",
                context=context,
                details={"error": str(e), "character_name": name},
                user_friendly="Failed to create character",
            )

    def get_available_classes_info(self) -> dict[str, Any]:
        """
        Get information about all available character classes and their prerequisites.

        Returns:
            dict: Class information and stat ranges
        """
        logger.info("Getting available classes information")

        class_info = {}
        for class_name, prerequisites in self.stats_generator.CLASS_PREREQUISITES.items():
            # Handle both enum values and string keys
            prereq_dict = {}
            for attr, min_value in prerequisites.items():
                if hasattr(attr, "value"):
                    prereq_dict[attr.value] = min_value
                else:
                    prereq_dict[str(attr)] = min_value

            class_info[class_name] = {
                "prerequisites": prereq_dict,
                "description": self._get_class_description(class_name),
            }

        return {
            "classes": class_info,
            "stat_range": {"min": self.stats_generator.MIN_STAT, "max": self.stats_generator.MAX_STAT},
        }

    def _get_class_description(self, class_name: str) -> str:
        """Get a description for a character class."""
        descriptions = {
            "investigator": "A skilled researcher and detective, specializing in uncovering mysteries and gathering information.",
            "occultist": "A scholar of forbidden knowledge, capable of wielding dangerous magic at the cost of lucidity.",
            "survivor": "A resilient individual who has learned to endure the horrors of the Mythos through sheer determination.",
            "cultist": "A charismatic leader who can manipulate others and has ties to dark organizations.",
            "academic": "A brilliant researcher and scholar, specializing in historical and scientific knowledge.",
            "detective": "A sharp-witted investigator with exceptional intuition and deductive reasoning skills.",
        }
        return descriptions.get(class_name, "A mysterious character with unknown capabilities.")
