"""
Stats Generator Service for MythosMUD.

This module provides random stat generation functionality for character creation,
allowing players to roll for their character's starting statistics within defined
ranges while ensuring they meet class prerequisites.
"""

import random
import time

from ..logging_config import get_logger
from ..models import AttributeType, Stats

logger = get_logger(__name__)


class StatsGenerator:
    """Service for generating random character statistics."""

    # Standard D&D-style stat ranges (3-18)
    MIN_STAT = 3
    MAX_STAT = 18

    # Class prerequisites (minimum stats required for each class)
    # Based on Lovecraftian investigator archetypes
    CLASS_PREREQUISITES = {
        "investigator": {
            AttributeType.INT: 12,  # High intelligence for research
            AttributeType.WIS: 10,  # Good perception
        },
        "occultist": {
            AttributeType.INT: 14,  # Very high intelligence for forbidden knowledge
            AttributeType.WIS: 12,  # Good willpower to resist corruption
        },
        "survivor": {
            AttributeType.CON: 12,  # High constitution for survival
            AttributeType.DEX: 10,  # Good reflexes
        },
        "cultist": {
            AttributeType.CHA: 12,  # High charisma for cult leadership
            AttributeType.INT: 10,  # Basic intelligence for rituals
        },
        "academic": {
            AttributeType.INT: 14,  # Very high intelligence for research
            AttributeType.WIS: 10,  # Good perception
        },
        "detective": {
            AttributeType.INT: 12,  # High intelligence for investigation
            AttributeType.WIS: 12,  # Good perception and intuition
        },
    }

    def __init__(self):
        """Initialize the stats generator."""
        logger.info("StatsGenerator initialized")

    def roll_stats(self, method: str = "3d6") -> Stats:
        """
        Roll character stats using the specified method.

        Args:
            method: Rolling method ("3d6", "4d6_drop_lowest", "point_buy")

        Returns:
            Stats: A new Stats object with randomly generated values
        """
        logger.info("Rolling stats", method=method)

        # Stats rolling method factory - maps method names to their implementation functions
        # This pattern eliminates the if/elif chain and provides O(1) lookup
        # As noted in the restricted archives, this approach scales better as new methods are added
        rolling_methods = {
            "3d6": self._roll_3d6,
            "4d6_drop_lowest": self._roll_4d6_drop_lowest,
            "point_buy": self._roll_point_buy,
        }

        roll_method = rolling_methods.get(method)
        if roll_method:
            stats = roll_method()
        else:
            logger.warning("Unknown rolling method, using 3d6", method=method)
            stats = self._roll_3d6()

        logger.info("Stats rolled successfully", stats=stats.model_dump())
        return stats

    def _roll_3d6(self) -> Stats:
        """Roll stats using 3d6 method (standard D&D)."""
        return Stats(
            strength=random.randint(3, 18),
            dexterity=random.randint(3, 18),
            constitution=random.randint(3, 18),
            intelligence=random.randint(3, 18),
            wisdom=random.randint(3, 18),
            charisma=random.randint(3, 18),
        )

    def _roll_4d6_drop_lowest(self) -> Stats:
        """Roll stats using 4d6 drop lowest method (more generous)."""

        def roll_4d6_drop_lowest() -> int:
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            return sum(rolls)

        return Stats(
            strength=roll_4d6_drop_lowest(),
            dexterity=roll_4d6_drop_lowest(),
            constitution=roll_4d6_drop_lowest(),
            intelligence=roll_4d6_drop_lowest(),
            wisdom=roll_4d6_drop_lowest(),
            charisma=roll_4d6_drop_lowest(),
        )

    def _roll_point_buy(self) -> Stats:
        """Generate stats using a point-buy system (balanced)."""
        # Start with 8 in all stats, then distribute 27 points
        # Each point increases a stat by 1, up to 15
        # Stats 16-18 cost 2 points each
        base_stats = {
            "strength": 8,
            "dexterity": 8,
            "constitution": 8,
            "intelligence": 8,
            "wisdom": 8,
            "charisma": 8,
        }

        points_remaining = 27
        stat_names = list(base_stats.keys())

        while points_remaining > 0:
            stat = random.choice(stat_names)
            current_value = base_stats[stat]

            if current_value >= 18:
                continue  # Stat is maxed out

            # Calculate cost for next point
            if current_value < 15:
                cost = 1
            else:
                cost = 2

            if points_remaining >= cost:
                base_stats[stat] += 1
                points_remaining -= cost
            else:
                break

        return Stats(**base_stats)

    def validate_class_prerequisites(self, stats: Stats, class_name: str) -> tuple[bool, list[str]]:
        """
        Check if stats meet the prerequisites for a given class.

        Args:
            stats: The character's stats
            class_name: The class to check prerequisites for

        Returns:
            Tuple[bool, List[str]]: (meets_prerequisites, list_of_failed_requirements)
        """
        if class_name not in self.CLASS_PREREQUISITES:
            logger.warning("Unknown class for prerequisite check", class_name=class_name)
            return True, []  # Unknown classes have no prerequisites

        prerequisites = self.CLASS_PREREQUISITES[class_name]
        failed_requirements = []

        for attribute, minimum_value in prerequisites.items():
            current_value = getattr(stats, attribute.value)
            if current_value < minimum_value:
                failed_requirements.append(f"{attribute.value.title()} {current_value} < {minimum_value}")

        meets_prerequisites = len(failed_requirements) == 0

        logger.debug(
            "Class prerequisite check",
            class_name=class_name,
            meets_prerequisites=meets_prerequisites,
            failed_requirements=failed_requirements,
        )

        return meets_prerequisites, failed_requirements

    def get_available_classes(self, stats: Stats) -> list[str]:
        """
        Get a list of classes that the character qualifies for.

        Args:
            stats: The character's stats

        Returns:
            List[str]: List of available class names
        """
        available_classes = []

        for class_name in self.CLASS_PREREQUISITES.keys():
            meets_prerequisites, _ = self.validate_class_prerequisites(stats, class_name)
            if meets_prerequisites:
                available_classes.append(class_name)

        logger.debug("Available classes determined", available_classes=available_classes)
        return available_classes

    def roll_stats_with_validation(
        self, method: str = "3d6", required_class: str | None = None, max_attempts: int = 10
    ) -> tuple[Stats, list[str]]:
        """
        Roll stats and validate against class requirements.

        Args:
            method: The rolling method to use
            required_class: Optional class that the stats must qualify for
            max_attempts: Maximum number of attempts to roll valid stats

        Returns:
            Tuple[Stats, List[str]]: (stats, available_classes)
        """
        logger.info(
            "Rolling stats with validation", method=method, required_class=required_class, max_attempts=max_attempts
        )

        for attempt in range(max_attempts):
            stats = self.roll_stats(method)
            available_classes = self.get_available_classes(stats)

            if required_class is None or required_class in available_classes:
                logger.info("Valid stats rolled", attempt=attempt + 1, available_classes=available_classes)
                return stats, available_classes

            logger.debug(
                "Stats don't meet class requirements, retrying",
                attempt=attempt + 1,
                required_class=required_class,
                available_classes=available_classes,
            )

        # If we couldn't roll valid stats, return the last roll anyway
        logger.warning(
            "Could not roll stats meeting class requirements", required_class=required_class, max_attempts=max_attempts
        )
        stats = self.roll_stats(method)
        available_classes = self.get_available_classes(stats)
        return stats, available_classes

    def roll_stats_with_profession(
        self, method: str = "3d6", profession_id: int = 0, timeout_seconds: float = 1.0
    ) -> tuple[Stats, bool]:
        """
        Roll stats and validate against profession requirements.

        Args:
            method: The rolling method to use
            profession_id: The profession ID to validate against
            timeout_seconds: Maximum time in seconds to spend rolling for valid stats

        Returns:
            Tuple[Stats, bool]: (stats, meets_requirements)
        """
        logger.info(
            "Rolling stats with profession validation",
            method=method,
            profession_id=profession_id,
            timeout_seconds=timeout_seconds,
        )

        logger.debug(f"DEBUG: Starting profession-based stats rolling for profession_id={profession_id}")

        # Get profession requirements from persistence
        try:
            from ..persistence import get_persistence

            persistence = get_persistence()
            profession = persistence.get_profession_by_id(profession_id)

            if not profession:
                raise ValueError(f"Invalid profession ID: {profession_id}")

            stat_requirements = profession.get_stat_requirements()
            logger.debug(f"DEBUG: Retrieved profession {profession_id} with requirements: {stat_requirements}")

        except Exception as e:
            logger.error(f"Error retrieving profession {profession_id}: {e}")
            raise ValueError(f"Invalid profession ID: {profession_id}") from e

        # If no requirements, just roll normally
        if not stat_requirements:
            stats = self.roll_stats(method)
            logger.info("Profession has no stat requirements, returning normal roll")
            logger.debug(f"DEBUG: No requirements found for profession {profession_id}, rolling normally")
            return stats, True

        # Try to roll stats that meet profession requirements within timeout
        start_time = time.time()
        attempt = 0

        logger.debug(f"DEBUG: Starting validation loop with {timeout_seconds}s timeout")
        while time.time() - start_time < timeout_seconds:
            attempt += 1
            stats = self.roll_stats(method)
            logger.debug(f"DEBUG: Attempt {attempt}: Rolled stats: {stats.model_dump()}")

            # Check if stats meet profession requirements
            meets_requirements = self._check_profession_requirements(stats, stat_requirements)
            logger.debug(f"DEBUG: Attempt {attempt}: Meets requirements: {meets_requirements}")

            if meets_requirements:
                elapsed_time = time.time() - start_time
                logger.info("Valid stats rolled for profession", attempt=attempt, profession_id=profession_id, elapsed_time=elapsed_time)
                return stats, True

            logger.debug(
                "Stats don't meet profession requirements, retrying",
                attempt=attempt,
                profession_id=profession_id,
                requirements=stat_requirements,
            )

        # Timeout reached - return the last roll with failure status
        elapsed_time = time.time() - start_time
        logger.warning(
            "Timeout reached while rolling stats for profession requirements",
            profession_id=profession_id,
            timeout_seconds=timeout_seconds,
            elapsed_time=elapsed_time,
            attempts_made=attempt,
        )
        stats = self.roll_stats(method)
        meets_requirements = self._check_profession_requirements(stats, stat_requirements)
        return stats, meets_requirements

    def _check_profession_requirements(self, stats: Stats, requirements: dict[str, int]) -> bool:
        """
        Check if stats meet profession requirements.

        Args:
            stats: The character's stats
            requirements: Dictionary of stat requirements (e.g., {"strength": 12, "intelligence": 14})

        Returns:
            bool: True if all requirements are met
        """
        logger.debug(f"DEBUG: Checking requirements {requirements} against stats {stats.model_dump()}")
        for stat_name, min_value in requirements.items():
            stat_value = getattr(stats, stat_name, None)
            logger.debug(f"DEBUG: Checking {stat_name}: {stat_value} >= {min_value}")
            if stat_value is None:
                logger.warning(f"Unknown stat name in requirements: {stat_name}")
                return False
            if stat_value < min_value:
                logger.debug(f"DEBUG: Requirement failed: {stat_name} {stat_value} < {min_value}")
                return False
        logger.debug("DEBUG: All requirements met")
        return True

    def get_stat_summary(self, stats: Stats) -> dict[str, any]:
        """
        Get a summary of the character's stats including modifiers and totals.

        Args:
            stats: The character's stats

        Returns:
            Dict: Summary of stats with modifiers and totals
        """
        summary = {
            "attributes": {
                "strength": {"value": stats.strength, "modifier": stats.get_attribute_modifier(AttributeType.STR)},
                "dexterity": {"value": stats.dexterity, "modifier": stats.get_attribute_modifier(AttributeType.DEX)},
                "constitution": {
                    "value": stats.constitution,
                    "modifier": stats.get_attribute_modifier(AttributeType.CON),
                },
                "intelligence": {
                    "value": stats.intelligence,
                    "modifier": stats.get_attribute_modifier(AttributeType.INT),
                },
                "wisdom": {"value": stats.wisdom, "modifier": stats.get_attribute_modifier(AttributeType.WIS)},
                "charisma": {"value": stats.charisma, "modifier": stats.get_attribute_modifier(AttributeType.CHA)},
            },
            "derived_stats": {
                "max_health": stats.max_health,
                "max_sanity": stats.max_sanity,
            },
            "total_points": sum(
                [stats.strength, stats.dexterity, stats.constitution, stats.intelligence, stats.wisdom, stats.charisma]
            ),
            "average_stat": sum(
                [stats.strength, stats.dexterity, stats.constitution, stats.intelligence, stats.wisdom, stats.charisma]
            )
            / 6,
        }

        return summary
