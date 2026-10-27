"""
Content effect dicts <-> player_effects rows (ADR-029 step 3b-i).

Content (dialogue ``apply_effect``, container ``on_put``) writes an effect as a plain dict such as
``{"type": "heal_over_time", "healing": 5, "duration": 15}`` or ``{"type": "lucidity_drain_over_time", ...,
"instance_scoped": true}``. Stored, ``type`` becomes the row's effect_type, ``instance_scoped`` its column, ``duration``
its remaining_seconds (no duration: until removed), and everything else, ``duration`` included, its payload. The tick
loop turns a row back into the same dict, so the per-effect processors read the shape content wrote.
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping

from ..models.player_effect import PlayerEffect
from ..persistence.repositories.player_effect_repository import PlayerEffectRepository
from ..utils.int_coercion import coerce_int

# Effects written by scripted content, by spells, and (in login_grace_period) the login ward ("entry_ward").
SCRIPTED_EFFECT_CATEGORY = "scripted"
SPELL_EFFECT_CATEGORY = "spell"
INSTANCE_SCOPED_EFFECT_KEY = "instance_scoped"
_COLUMN_KEYS = frozenset({"type", INSTANCE_SCOPED_EFFECT_KEY})


def effect_dict(effect: PlayerEffect) -> dict[str, object]:
    """The content-shaped dict for a stored effect: its payload plus ``type`` and ``instance_scoped``."""
    return {**effect.payload, "type": effect.effect_type, INSTANCE_SCOPED_EFFECT_KEY: effect.instance_scoped}


def effect_payload(effect: Mapping[str, object]) -> dict[str, object]:
    """The part of a content-shaped dict stored as the row's payload."""
    return {key: value for key, value in effect.items() if key not in _COLUMN_KEYS}


async def add_content_effect(player_id: uuid.UUID, effect: Mapping[str, object]) -> str:
    """Store a content-written effect for the player; returns the effect id."""
    duration = coerce_int(effect.get("duration", 0), default=0)
    return await PlayerEffectRepository().add_effect(
        player_id,
        {
            "effect_type": str(effect["type"]),
            "category": SCRIPTED_EFFECT_CATEGORY,
            "remaining_seconds": duration if duration > 0 else None,
            "payload": effect_payload(effect),
            "instance_scoped": effect.get(INSTANCE_SCOPED_EFFECT_KEY) is True,
        },
    )


async def clear_instance_scoped_effects(player_id: uuid.UUID) -> int:
    """Remove the effects tied to the player's (lost) instance; returns how many."""
    return await PlayerEffectRepository().delete_instance_scoped_effects(player_id)
