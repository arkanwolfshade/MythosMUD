"""
NPC ``behavior_config["aggression_level"]``: one contract, two spellings (#999).

The canonical form is an int 0-10, which ``aggro_threat._aggression_scale`` turns into a threat multiplier
(0 -> 0.5x, 10 -> 1.0x). The NPC catalog writes the names ``"passive"`` / ``"aggressive"`` instead, so both
spellings are accepted wherever the field is read or validated:

- ``"aggressive"`` -> 10, the full-threat end of the scale (the same multiplier as an unset level).
- ``"passive"`` -> 0, the damped end: healing or buffing a passive mob draws half the threat.
"""

from __future__ import annotations

from typing import Final

from server.utils.int_coercion import coerce_int

AGGRESSION_LEVEL_MIN: Final = 0
AGGRESSION_LEVEL_MAX: Final = 10

AGGRESSION_LEVEL_BY_NAME: Final[dict[str, int]] = {
    "passive": AGGRESSION_LEVEL_MIN,
    "aggressive": AGGRESSION_LEVEL_MAX,
}

# coerce_int needs a default; an absurd value tells "not a number" apart from any level a config could carry.
_NOT_A_NUMBER: Final = -(2**31)


def parse_aggression_level(raw: object) -> int | None:
    """Resolve a stored ``aggression_level`` to an int 0-10, or None when unset or unreadable (full threat)."""
    if raw is None:
        return None
    if isinstance(raw, str):
        named = AGGRESSION_LEVEL_BY_NAME.get(raw.strip().lower())
        if named is not None:
            return named
    level = coerce_int(raw, default=_NOT_A_NUMBER)
    if level == _NOT_A_NUMBER:
        return None
    return max(AGGRESSION_LEVEL_MIN, min(AGGRESSION_LEVEL_MAX, level))
