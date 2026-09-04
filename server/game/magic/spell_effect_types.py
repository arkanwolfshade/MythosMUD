"""
Shared Protocol types for spell effect modules.

Used by basedpyright to type NPC/player surfaces without importing heavy concrete classes
in every helper (per Pnakotic style: name the boundary, not the entire bestiary).
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping, Sequence
from typing import Protocol, runtime_checkable

# Protocol method bodies use Ellipsis per PEP 544; Pylint W2301 flags it as redundant vs pass,
# but pass breaks pyright (no return) and triggers unnecessary-pass. Keep ... and silence W2301.
# pylint: disable=unnecessary-ellipsis


@runtime_checkable
class NpcSpellDamageTarget(Protocol):
    """Minimal NPC surface for spell damage, steal-life, and NATS publish helpers."""

    current_room: str | None
    npc_id: uuid.UUID | str

    @property
    def is_alive(self) -> bool:
        """True if the NPC is still alive (structural typing stub for pyright)."""
        ...

    def take_damage(self, damage: int, damage_type: str = "physical", source_id: str | None = None) -> bool:
        """Apply damage; return True if the instance accepted the hit."""
        ...

    def get_combat_stats(self) -> dict[str, int]:
        """Current combat stats (e.g. current_dp, max_dp) for events and UI sync."""
        ...


@runtime_checkable
class SpellEffectPlayer(Protocol):
    """Player surface for stat modify, lucidity, corruption, and teleport spell paths."""

    name: str
    current_room_id: str | None

    def get_stats(self) -> Mapping[str, object]:
        """Mutable stats mapping as returned by the live player object."""
        ...

    def set_stats(self, stats: Mapping[str, object]) -> None:
        """Replace player stats after spell-driven changes."""
        ...

    def get_status_effects(self) -> Sequence[Mapping[str, object]]:
        """Active status effects (buffs/debuffs) for spell stat modify paths."""
        ...

    def set_status_effects(self, effects: Sequence[Mapping[str, object]]) -> None:
        """Persist updated status effect list after spell application."""
        ...


class PlayerPersistenceSpellPort(Protocol):
    """Async persistence surface used by SpellEffects player-targeting paths."""

    async def get_player_by_id(self, player_id: uuid.UUID) -> object | None:
        """Load player by id; None if missing."""
        ...

    async def save_player(self, player: object) -> None:
        """Persist player after spell mutations."""
        ...

    async def apply_lucidity_gain(self, player: object, amount: int, source: str) -> None:
        """Increase lucidity from a spell effect."""
        ...

    async def apply_lucidity_loss(self, player: object, amount: int, source: str) -> None:
        """Decrease lucidity from a spell effect."""
        ...


class NpcLifecycleManagerPort(Protocol):
    """NPC instance lifecycle registry (string id -> live instance) for steal-life lookup."""

    active_npcs: Mapping[str, object]


class NpcIntegrationStringIdPort(Protocol):
    """Maps combat UUID npc ids back to lifecycle string keys."""

    def get_original_string_id(self, npc_uuid: uuid.UUID) -> str | None:
        """Return registry string id for npc_uuid, or None if unmapped."""
        ...


class PlayerServiceHealPort(Protocol):
    """Player service methods used by heal and steal-life spell paths."""

    persistence: PlayerPersistenceSpellPort

    async def heal_player(self, player_id: uuid.UUID, amount: int) -> Mapping[str, object]:
        """Apply healing to a player by id."""
        ...

    async def damage_player(
        self, player_id: uuid.UUID, amount: int, damage_type: str = "physical"
    ) -> Mapping[str, object]:
        """Apply typed damage to a player; returns damage result payload."""
        ...


class SpellEffectsEngineHealPort(Protocol):
    """SpellEffects engine surface for spell_effects_heal (no import cycle with spell_effects)."""

    player_service: PlayerServiceHealPort
