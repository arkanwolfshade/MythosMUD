"""Protocols for NPC combat integration (shared by base and facade modules)."""

from typing import Protocol

from ..events.combat_events import PlayerAttackedEvent


class CombatEventPublisherProtocol(Protocol):
    """Combat event publisher (avoids importing CombatEventPublisher)."""

    async def publish_player_attacked(self, event: PlayerAttackedEvent) -> bool:
        """Publish a PlayerAttackedEvent to the combat event stream."""
        return False


class NpcCombatServiceProtocol(Protocol):
    """Typed surface for npc_combat_service.handle_npc_attack_on_player."""

    async def handle_npc_attack_on_player(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int,
        npc_instance: object | None = None,
    ) -> bool:
        """Handle an NPC attack against a player via the main combat service."""
        return False
