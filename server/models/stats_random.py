"""Random core stat rolls for character creation (no Stats import — breaks game/stats_generator cycle)."""

from __future__ import annotations

import random
from typing import Literal, TypedDict

CoreStatKey = Literal[
    "strength",
    "dexterity",
    "constitution",
    "size",
    "intelligence",
    "power",
    "education",
    "charisma",
    "luck",
]

CORE_STAT_KEYS: tuple[CoreStatKey, ...] = (
    "strength",
    "dexterity",
    "constitution",
    "size",
    "intelligence",
    "power",
    "education",
    "charisma",
    "luck",
)

__all__ = ["CORE_STAT_KEYS", "CoreStatKey", "CoreStatValues", "roll_random_core_stat_values"]


class CoreStatValues(TypedDict):
    """Core attribute ints rolled for a new character (keys match Stats core fields only)."""

    strength: int
    dexterity: int
    constitution: int
    size: int
    intelligence: int
    power: int
    education: int
    charisma: int
    luck: int


def roll_random_core_stat_values(seed: int | None = None) -> CoreStatValues:
    """
    Roll core attribute values for a new character.

    Returns a plain dict so models.game and game.stats_generator can share logic
    without importing each other.
    """
    local_rng = random.Random(seed) if seed is not None else random.Random()  # nosec B311
    size_roll = local_rng.randint(2, 12) + 6
    size = size_roll * 5
    return {
        "strength": local_rng.randint(15, 90),
        "dexterity": local_rng.randint(15, 90),
        "constitution": local_rng.randint(15, 90),
        "size": size,
        "intelligence": local_rng.randint(15, 90),
        "power": local_rng.randint(15, 90),
        "education": local_rng.randint(15, 90),
        "charisma": local_rng.randint(15, 90),
        "luck": local_rng.randint(15, 90),
    }
