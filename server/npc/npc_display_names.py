"""NPC display names for chat delivery (kept free of ChatService imports)."""

from __future__ import annotations

_npc_display_names: dict[str, str] = {}


def register_npc_display_name(npc_id: str, name: str) -> None:
    """Remember an NPC display name for NPCSpoke chat bridging."""
    if npc_id and name:
        _npc_display_names[npc_id] = name


def resolve_npc_display_name(npc_id: str, explicit: str | None = None) -> str:
    """Resolve NPC display name for chat speaker_name."""
    if explicit:
        return explicit
    return _npc_display_names.get(npc_id) or "Someone"
