"""
Content effect dicts <-> player effects (ADR-029 steps 3b-i and 6d).

Content (dialogue ``apply_effect``, container ``on_put``) writes an effect as a plain dict such as
``{"type": "heal_over_time", "healing": 5, "duration": 15}`` or ``{"type": "lucidity_drain_over_time", ...,
"instance_scoped": true}``. Stored, ``type`` becomes the row's effect_type, ``instance_scoped`` its column, ``duration``
its remaining_seconds (no duration: until removed), and everything else, ``duration`` included, its payload. The tick
loop turns an effect back into the same dict, so the per-effect processors read the shape content wrote.

``PlayerEffects`` is how effects are started and ended: every call is a unit of work on the player registry, which
owns the ``player_effects`` rows (it joins the caller's unit when one is open).
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING

from ..async_persistence_types import PlayerEffectOptions
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int

if TYPE_CHECKING:
    from .player_registry import EffectData, PlayerRegistry

logger = get_logger(__name__)

# Effects written by scripted content, by spells, and (in login_grace_period) the login ward ("entry_ward").
SCRIPTED_EFFECT_CATEGORY = "scripted"
SPELL_EFFECT_CATEGORY = "spell"
INSTANCE_SCOPED_EFFECT_KEY = "instance_scoped"
_COLUMN_KEYS = frozenset({"type", INSTANCE_SCOPED_EFFECT_KEY})


def effect_dict(effect: EffectData) -> dict[str, object]:
    """The content-shaped dict for a running effect: its payload plus ``type`` and ``instance_scoped``."""
    return {**effect.payload, "type": effect.effect_type, INSTANCE_SCOPED_EFFECT_KEY: effect.instance_scoped}


def effect_payload(effect: Mapping[str, object]) -> dict[str, object]:
    """The part of a content-shaped dict stored as the row's payload."""
    return {key: value for key, value in effect.items() if key not in _COLUMN_KEYS}


class PlayerEffects:
    """Start and end a player's status effects, each call as one registry unit."""

    def __init__(self, registry: PlayerRegistry) -> None:
        self._registry: PlayerRegistry = registry

    async def add(
        self,
        player_id: uuid.UUID | str,
        effect_type: str,
        category: str,
        remaining_seconds: int | None,
        options: PlayerEffectOptions | None = None,
    ) -> str:
        """Start an effect lasting ``remaining_seconds`` online game seconds (None = until removed); returns its id."""
        extra = options or {}
        async with self._registry.mutate(uuid.UUID(str(player_id))) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            effect_id = player.effects.add(
                effect_type,
                category,
                remaining_seconds=remaining_seconds,
                payload=extra.get("payload"),
                instance_scoped=extra.get("instance_scoped", False),
                intensity=extra.get("intensity", 1),
                source=extra.get("source"),
                visibility_level=extra.get("visibility_level", "visible"),
            )
        return str(effect_id)

    async def add_content(self, player_id: uuid.UUID, effect: Mapping[str, object]) -> str:
        """Start a content-written effect (see the module doc) for the player; returns the effect id."""
        duration = coerce_int(effect.get("duration", 0), default=0)
        return await self.add(
            player_id,
            str(effect["type"]),
            SCRIPTED_EFFECT_CATEGORY,
            duration if duration > 0 else None,
            {"payload": effect_payload(effect), "instance_scoped": effect.get(INSTANCE_SCOPED_EFFECT_KEY) is True},
        )

    async def remove_by_type(self, player_id: uuid.UUID | str, effect_type: str) -> int:
        """End every effect of one type on the player; returns how many."""
        async with self._registry.mutate(uuid.UUID(str(player_id))) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            return player.effects.remove_by_type(effect_type)

    async def clear_instance_scoped(self, player_id: uuid.UUID) -> int:
        """End the effects tied to the player's (lost) instance; returns how many."""
        async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            return player.effects.clear_instance_scoped()


async def clear_instance_scoped_effects(registry: PlayerRegistry | None, player_id: uuid.UUID) -> int:
    """End the effects tied to the player's (lost) instance; returns how many. With no registry nothing can be
    cleared, which is logged: the effects would follow the player out of the instance."""
    if registry is None:
        logger.warning("No player registry, instance-scoped effects kept", player_id=str(player_id))
        return 0
    return await PlayerEffects(registry).clear_instance_scoped(player_id)
