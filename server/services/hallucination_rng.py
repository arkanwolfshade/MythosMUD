"""
Shared RNG for the hallucination subsystem (#714).

Deterministic when `GAME_HALLUCINATION_RNG_SEED` is set (test/integration-test only,
see `GameConfig.hallucination_rng_seed`); otherwise behaves like the plain `random`
module. A single shared instance so every call site (fake tells, room overlays,
phantom spawns, frequency rolls) draws from the same seeded stream.
"""

from __future__ import annotations

import random


class HallucinationRng:
    """Lazily-seeded `random.Random`, shared by every hallucination call site."""

    def __init__(self) -> None:
        self._rng: random.Random | None = None

    def get(self) -> random.Random:
        """Return the shared RNG, seeding it from config on first use."""
        if self._rng is None:
            from ..config import get_config

            seed = get_config().game.hallucination_rng_seed
            self._rng = random.Random(seed) if seed is not None else random.Random()  # nosec B311
        return self._rng

    def reset(self) -> None:
        """Drop the cached RNG so the next `get()` re-reads the config seed (tests)."""
        self._rng = None


hallucination_rng = HallucinationRng()

__all__ = ["HallucinationRng", "hallucination_rng"]
