"""Protocols for NPC combat and communication integration (used by NPCBase)."""

from typing import Protocol


class CombatIntegrationProtocol(Protocol):
    """Protocol for combat integration handle_npc_death."""

    def handle_npc_death(self, npc_id: str, room_id: str | None, cause: str, source_id: str | None) -> None:
        """Handle NPC death in the combat integration layer."""


class CommunicationIntegrationProtocol(Protocol):
    """Protocol for communication integration (whisper, room message, handle player message)."""

    def send_whisper_to_player(self, npc_id: str, target_id: str, message: str, room_id: str | None) -> bool:
        """Send a private whisper from this NPC to a single player."""
        return False

    def send_message_to_room(self, npc_id: str, room_id: str | None, message: str, channel: str) -> bool:
        """Send a message from this NPC to all players in a room."""
        return False

    def handle_player_message(
        self, npc_id: str, speaker_id: str, message: str, room_id: str | None, channel: str
    ) -> bool:
        """Handle an incoming player message directed at this NPC."""
        return False
