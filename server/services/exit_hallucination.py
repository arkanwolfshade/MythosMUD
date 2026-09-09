"""
Server-side exit hallucination for the deranged lucidity tier (#626, #714).

Bit-for-bit port of `client/src/utils/directionHallucination.ts`'s `seedFrom`/`mulberry32`/
`getHallucinatedExits`, moved server-side so the lie is authoritative: the same seeded set of
fake exits now appears in both `/look` and the per-viewer room payload, instead of #626's
original design where only the Location panel lied and `/look` told the truth. See ADR-024.

The seed is keyed on (room_id, player_id), so the hallucination is stable across re-entry and
re-render for one player, but different players in the same room see different lies -- exactly
matching the client-side behavior this replaces.
"""

from __future__ import annotations

from collections.abc import Callable

DIRECTION_POOL: tuple[str, ...] = ("north", "south", "east", "west", "up", "down")

_MASK32 = 0xFFFFFFFF


def _hash_string(value: str) -> int:
    """
    32-bit string hash (djb2 variant) -- port of hashString() in directionHallucination.ts.

    Deterministic, no crypto dependency. Masking the full expression with `& _MASK32` on each
    iteration gives the same low-32-bit result as JS's `| 0` int32 truncation, since bitwise
    shift/add operations only depend on the bit pattern mod 2**32, not on signed vs. unsigned
    interpretation.
    """
    hash_value = 5381
    for char in value:
        hash_value = ((hash_value << 5) + hash_value + ord(char)) & _MASK32
    return hash_value


def seed_from(room_id: str, player_id: str) -> int:
    """Combine room + player into a single seed -- order matters, port of seedFrom()."""
    return _hash_string(f"{room_id}::{player_id}")


def mulberry32(seed: int) -> Callable[[], float]:
    """
    mulberry32: small, fast, deterministic PRNG -- port of mulberry32() in
    directionHallucination.ts. Returns a callable yielding floats in [0, 1).

    All intermediate values are kept as unsigned 32-bit accumulators (`& _MASK32`); XOR, shift,
    and multiply only depend on the bit pattern, so this is bit-for-bit identical to the JS
    original's signed-int32 arithmetic without needing to emulate JS's sign semantics directly.
    """
    state = seed & _MASK32

    def _next() -> float:
        nonlocal state
        state = (state + 0x6D2B79F5) & _MASK32
        a = state
        t = ((a ^ (a >> 15)) * (a | 1)) & _MASK32
        prior_t = t
        t = (prior_t + (((prior_t ^ (prior_t >> 7)) * (prior_t | 61)) & _MASK32)) & _MASK32
        t ^= prior_t
        t &= _MASK32
        return ((t ^ (t >> 14)) & _MASK32) / 4294967296

    return _next


def _shuffle(items: tuple[str, ...], rng: Callable[[], float]) -> list[str]:
    """Deterministic shuffle driven by rng -- port of shuffle() (random-key sort, not Fisher-Yates)."""
    keyed = [(rng(), item) for item in items]
    keyed.sort(key=lambda pair: pair[0])
    return [item for _, item in keyed]


def get_hallucinated_exits(room_id: str, player_id: str) -> list[str]:
    """
    Return this viewer's seeded, deterministic fake exit set for this room (#626, #714).

    Port of getHallucinatedExits(): NOT a reversal map -- the displayed exit set (count and
    labels) is intentionally independent of the room's real exits.
    """
    rng = mulberry32(seed_from(room_id, player_id))
    count = 1 + int(rng() * len(DIRECTION_POOL))
    return _shuffle(DIRECTION_POOL, rng)[:count]


__all__ = ["DIRECTION_POOL", "get_hallucinated_exits", "mulberry32", "seed_from"]
