"""
Stats Generator Service for MythosMUD.

This module provides random stat generation functionality for character creation,
allowing players to roll for their character's starting statistics within defined
ranges while ensuring they meet class prerequisites.
"""

import random
import time
from typing import Literal, Protocol, cast

import numpy as np

from ..models.game import AttributeType, Stats
from ..models.stats_random import CoreStatValues, roll_random_core_stat_values
from ..structured_logging.enhanced_logging_config import get_logger
from .stats_generator_summary import build_stat_summary


def generate_random_stats(seed: int | None = None) -> Stats:
    """
    Generate Stats with random attribute values.

    Factory function for creating Stats objects with randomly generated attributes.
    This separates business logic from the model's __init__ method.

    The raw rolls come from models/stats_random.py, which imports nothing from game/ —
    that is what keeps models/ -> game/ off the import graph (ADR-001; #757).

    Args:
        seed: Optional random seed for reproducible generation (useful for testing)

    Returns:
        Stats: A new Stats object with randomly generated attribute values
    """
    return Stats(**roll_random_core_stat_values(seed=seed))


logger = get_logger(__name__)

PointBuyAdjustableStat = Literal[
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "power",
    "education",
    "charisma",
    "luck",
]


class _ProfessionStatRequirementsSource(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Minimal profession surface for stat rolling (avoids importing models.profession)."""

    def get_stat_requirements(self) -> dict[str, int]: ...  # pylint: disable=missing-function-docstring  # Reason: Protocol stub


class StatsGenerator:
    """Service for generating random character statistics."""

    # Standard D&D-style stat ranges (15-90, scaled from 3-18)
    MIN_STAT: int = 15
    MAX_STAT: int = 90

    # Class prerequisites (minimum stats required for each class)
    # Based on Lovecraftian investigator archetypes
    # Values scaled by 5x from original 1-20 range to 1-100 range
    CLASS_PREREQUISITES: dict[str, dict[AttributeType, int]] = {
        "investigator": {
            AttributeType.INT: 60,  # High intelligence for research (scaled from 12)
            AttributeType.EDU: 50,  # Good education (scaled from 10)
        },
        "occultist": {
            AttributeType.INT: 70,  # Very high intelligence for forbidden knowledge (scaled from 14)
            AttributeType.POW: 60,  # Good willpower to resist corruption (scaled from 12)
        },
        "survivor": {
            AttributeType.CON: 60,  # High constitution for survival (scaled from 12)
            AttributeType.DEX: 50,  # Good reflexes (scaled from 10)
        },
        "cultist": {
            AttributeType.CHA: 60,  # High charisma for cult leadership (scaled from 12)
            AttributeType.INT: 50,  # Basic intelligence for rituals (scaled from 10)
        },
        "academic": {
            AttributeType.INT: 70,  # Very high intelligence for research (scaled from 14)
            AttributeType.EDU: 50,  # Good education (scaled from 10)
        },
        "detective": {
            AttributeType.INT: 60,  # High intelligence for investigation (scaled from 12)
            AttributeType.EDU: 60,  # Good education and knowledge (scaled from 12)
        },
    }

    def __init__(self) -> None:
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

    def _roll_size(self) -> int:
        """Roll Size using formula: (2D6+6)*5 (range 40-90)."""
        size_roll = random.randint(2, 12) + 6  # nosec B311: Game mechanics dice roll, not cryptographic  # 2D6+6 (range 8-18)
        return size_roll * 5  # Multiply by 5 (range 40-90)

    def _roll_3d6(self) -> Stats:
        """Roll stats using 3d6 method (scaled to 15-90 range)."""
        return Stats(
            strength=random.randint(15, 90),  # nosec B311: Game mechanics stat generation, not cryptographic
            dexterity=random.randint(15, 90),  # nosec B311: Game mechanics stat generation, not cryptographic
            constitution=random.randint(15, 90),  # nosec B311: Game mechanics stat generation, not cryptographic
            size=self._roll_size(),
            intelligence=random.randint(15, 90),  # nosec B311: Game mechanics stat generation, not cryptographic
            power=random.randint(15, 90),  # nosec B311: Game mechanics stat generation, not cryptographic
            education=random.randint(15, 90),  # nosec B311: Game mechanics stat generation, not cryptographic
            charisma=random.randint(15, 90),  # nosec B311: Game mechanics stat generation, not cryptographic
            luck=random.randint(15, 90),  # nosec B311: Game mechanics stat generation, not cryptographic
        )

    def _roll_4d6_drop_lowest(self) -> Stats:
        """Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range)."""

        def roll_4d6_drop_lowest() -> int:
            # Roll 4d6 using NumPy for efficient array operations
            rolls = np.random.randint(1, 7, size=4, dtype=np.int32)  # nosec B311: Game mechanics dice roll, not cryptographic
            # Drop lowest by sorting and taking last 3, then sum
            result = np.sum(np.sort(rolls)[1:])  # Sort and take last 3 (drop lowest)
            # Scale from 3-18 range to 15-90 range (multiply by 5)
            return int(result * 5)

        return Stats(
            strength=roll_4d6_drop_lowest(),
            dexterity=roll_4d6_drop_lowest(),
            constitution=roll_4d6_drop_lowest(),
            size=self._roll_size(),
            intelligence=roll_4d6_drop_lowest(),
            power=roll_4d6_drop_lowest(),
            education=roll_4d6_drop_lowest(),
            charisma=roll_4d6_drop_lowest(),
            luck=roll_4d6_drop_lowest(),
        )

    def _roll_point_buy(self) -> Stats:
        """Generate stats using a point-buy system (balanced, scaled to 1-100 range)."""
        # Start with 40 in all stats (scaled from 8), then distribute points
        # Each point increases a stat by 1, up to 75 (scaled from 15)
        # Stats 76-90 cost 2 points each (scaled from 16-18)
        # Size uses CoC formula, so roll it separately
        base_stats: CoreStatValues = {
            "strength": 40,
            "dexterity": 40,
            "constitution": 40,
            "size": self._roll_size(),  # Size uses CoC formula
            "intelligence": 40,
            "power": 40,
            "education": 40,
            "charisma": 40,
            "luck": 40,
        }

        # Adjust points for 9 stats instead of 6 (more points needed)
        points_remaining = 200  # Increased from 135 to account for more stats
        stat_names: list[PointBuyAdjustableStat] = [
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "power",
            "education",
            "charisma",
            "luck",
        ]

        while points_remaining > 0:
            stat: PointBuyAdjustableStat = random.choice(stat_names)  # nosec B311: Game mechanics stat selection, not cryptographic
            current_value = base_stats[stat]

            if current_value >= 90:
                continue  # Stat is maxed out

            # Calculate cost for next point
            if current_value < 75:
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
        failed_requirements: list[str] = []

        for attribute, minimum_value in prerequisites.items():
            current_value = cast(int | None, getattr(stats, attribute.value, None))
            if current_value is None or current_value < minimum_value:
                failed_requirements.append(f"{attribute.value.title()} {current_value} < {minimum_value}")

        meets_prerequisites = not failed_requirements

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
        available_classes: list[str] = []

        for class_name in StatsGenerator.CLASS_PREREQUISITES:
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

    def _resolve_profession_stat_requirements(
        self,
        profession: _ProfessionStatRequirementsSource | None,
        profession_id: int,
    ) -> dict[str, int]:
        """Load stat requirements from the caller-supplied profession object."""
        logger.debug("DEBUG: Starting profession-based stats rolling", profession_id=profession_id)
        try:
            if profession is None:
                raise ValueError(
                    f"Profession must be provided for profession_id={profession_id}. "
                    + "Fetch via async persistence at the call site and pass profession=."
                )
            stat_requirements = profession.get_stat_requirements()
            logger.debug(
                "DEBUG: Retrieved profession with requirements",
                profession_id=profession_id,
                stat_requirements=stat_requirements,
            )
            return stat_requirements
        except Exception as e:
            logger.error("Error retrieving profession", profession_id=profession_id, error=str(e))
            raise ValueError(f"Invalid profession ID: {profession_id}") from e

    def _roll_until_profession_requirements_met(
        self,
        method: str,
        stat_requirements: dict[str, int],
        profession_id: int,
        timeout_seconds: float,
        max_attempts: int,
    ) -> tuple[Stats, bool]:
        """Retry rolling until profession stat requirements are met or limits are hit."""
        start_time = time.time()
        attempt = 0
        logger.debug("DEBUG: Starting validation loop", timeout_seconds=timeout_seconds, max_attempts=max_attempts)
        while (time.time() - start_time) < timeout_seconds and attempt < max_attempts:
            attempt += 1
            stats = self.roll_stats(method)
            logger.debug("DEBUG: Attempt rolled stats", attempt=attempt, stats=stats.model_dump())
            meets_requirements = self._check_profession_requirements(stats, stat_requirements)
            logger.debug("DEBUG: Attempt meets requirements", attempt=attempt, meets_requirements=meets_requirements)
            if meets_requirements:
                elapsed_time = time.time() - start_time
                logger.info(
                    "Valid stats rolled for profession",
                    attempt=attempt,
                    profession_id=profession_id,
                    elapsed_time=elapsed_time,
                )
                return stats, True
            logger.debug(
                "Stats don't meet profession requirements, retrying",
                attempt=attempt,
                profession_id=profession_id,
                requirements=stat_requirements,
            )
        elapsed_time = time.time() - start_time
        logger.warning(
            "Limits reached while rolling stats for profession requirements",
            profession_id=profession_id,
            timeout_seconds=timeout_seconds,
            elapsed_time=elapsed_time,
            attempts_made=attempt,
        )
        stats = self.roll_stats(method)
        meets_requirements = self._check_profession_requirements(stats, stat_requirements)
        return stats, meets_requirements

    def roll_stats_with_profession(
        self,
        method: str = "3d6",
        profession_id: int = 0,
        timeout_seconds: float = 5.0,  # Increased from 1.0 to allow more time for automatic rerolls
        max_attempts: int = 50,  # Increased from 10 to improve success rate for profession requirements
        profession: _ProfessionStatRequirementsSource | None = None,
    ) -> tuple[Stats, bool]:
        """
        Roll stats and validate against profession requirements.

        Args:
            method: The rolling method to use
            profession_id: The profession ID to validate against
            timeout_seconds: Maximum time in seconds to spend rolling for valid stats
            max_attempts: Maximum number of attempts to roll stats that meet requirements
            profession: Optional profession object (if provided, skips database lookup)

        Returns:
            Tuple[Stats, bool]: (stats, meets_requirements)
        """
        logger.info(
            "Rolling stats with profession validation",
            method=method,
            profession_id=profession_id,
            timeout_seconds=timeout_seconds,
            max_attempts=max_attempts,
        )
        stat_requirements = self._resolve_profession_stat_requirements(profession, profession_id)
        if not stat_requirements:
            stats = self.roll_stats(method)
            logger.info("Profession has no stat requirements, returning normal roll")
            logger.debug("DEBUG: No requirements found for profession, rolling normally", profession_id=profession_id)
            return stats, True
        return self._roll_until_profession_requirements_met(
            method, stat_requirements, profession_id, timeout_seconds, max_attempts
        )

    def _check_profession_requirements(self, stats: Stats, requirements: dict[str, int]) -> bool:
        """
        Check if stats meet profession requirements.

        Args:
            stats: The character's stats
            requirements: Dictionary of stat requirements (e.g., {"strength": 12, "intelligence": 14})

        Returns:
            bool: True if all requirements are met
        """
        logger.debug("DEBUG: Checking requirements against stats", requirements=requirements, stats=stats.model_dump())

        # STAT NAME MAPPING: Map legacy/alternative stat names to actual Stats model attributes
        # In Call of Cthulhu, "wisdom" is typically represented by "power" (willpower)
        stat_name_map = {  # pylint: disable=invalid-name  # Reason: Local variable, not a constant
            "wisdom": "power",  # Wisdom maps to power (willpower) in CoC
        }

        for stat_name, min_value in requirements.items():
            # Map stat name if needed
            mapped_stat_name = stat_name_map.get(stat_name, stat_name)
            stat_value = getattr(stats, mapped_stat_name, None)

            logger.debug(
                "DEBUG: Checking stat",
                stat_name=stat_name,
                mapped_stat_name=mapped_stat_name,
                stat_value=stat_value,
                min_value=min_value,
            )
            if stat_value is None:
                logger.warning(
                    "Unknown stat name in requirements", stat_name=stat_name, mapped_stat_name=mapped_stat_name
                )
                return False
            if stat_value < min_value:
                logger.debug(
                    "DEBUG: Requirement failed",
                    stat_name=stat_name,
                    mapped_stat_name=mapped_stat_name,
                    stat_value=stat_value,
                    min_value=min_value,
                )
                return False
        logger.debug("DEBUG: All requirements met")
        return True

    def get_stat_summary(self, stats: Stats) -> dict[str, object]:
        """
        Get a summary of the character's stats including modifiers and totals.

        Args:
            stats: The character's stats

        Returns:
            Dict: Summary of stats with modifiers and totals
        """
        return build_stat_summary(stats)
