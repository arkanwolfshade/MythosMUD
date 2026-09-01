"""Shared TypedDicts and occupant helpers for respawn event handlers."""

from __future__ import annotations

from collections.abc import Callable
from typing import NotRequired, TypedDict


class RespawnPlayerStatsPayload(TypedDict):
    """Nested stats object in WebSocket respawn player payloads."""

    current_dp: int
    max_dp: int
    lucidity: int
    max_lucidity: int
    position: str
    occult_knowledge: int
    fear: int
    corruption: int
    cult_affiliation: int
    strength: NotRequired[object | None]
    dexterity: NotRequired[object | None]
    constitution: NotRequired[object | None]
    intelligence: NotRequired[object | None]
    wisdom: NotRequired[object | None]
    charisma: NotRequired[object | None]


class RespawnPlayerEventPayload(TypedDict):
    """Client-facing player snapshot sent in respawn WebSocket events."""

    id: str
    name: str
    level: int
    xp: int
    stats: RespawnPlayerStatsPayload
    position: str
    in_combat: bool


def occupant_str_field(occ: dict[str, object], field_keys: tuple[str, ...]) -> str | None:
    """Return the first string value found for any of the given occupant dict keys."""
    for key in field_keys:
        value = occ.get(key)
        if isinstance(value, str):
            return value
    return None


def is_npc_occupant_row(occ: dict[str, object]) -> bool:
    """True when the occupant row should be classified as an NPC."""
    return bool(occ.get("is_npc")) or "npc_name" in occ


def append_unique_valid_occupant(
    name: str | None,
    *,
    primary: list[str],
    occupant_names: list[str],
    validate_name: Callable[[object], bool],
) -> None:
    """Append a validated name to primary and occupant lists when not already present."""
    if not name or not validate_name(name) or name in primary:
        return
    primary.append(name)
    if name not in occupant_names:
        occupant_names.append(name)


def ensure_respawned_player_in_lists(
    respawned_player_name: str,
    *,
    player_names: list[str],
    occupant_names: list[str],
    validate_name: Callable[[object], bool],
) -> None:
    """Ensure the respawned player appears in player and occupant name lists."""
    if not respawned_player_name or not validate_name(respawned_player_name):
        return
    if respawned_player_name not in occupant_names:
        occupant_names.append(respawned_player_name)
    if respawned_player_name not in player_names:
        player_names.append(respawned_player_name)
