"""
Unit tests for combat messaging service.

Tests the CombatMessagingService class for generating thematic combat messages.
"""

import pytest

from server.services.combat_messaging_service import CombatMessagingService


class TestCombatMessagingService:
    """Test suite for CombatMessagingService class."""

    @pytest.fixture
    def service(self):
        """Create a CombatMessagingService instance for testing."""
        return CombatMessagingService()

    def test_init(self):
        """Test CombatMessagingService initialization."""
        service = CombatMessagingService()
        assert service.default_messages is not None
        assert "attack_attacker" in service.default_messages
        assert "attack_defender" in service.default_messages
        assert "attack_other" in service.default_messages
        assert "death_message" in service.default_messages

    @pytest.mark.asyncio
    async def test_get_attack_message_attacker_perspective(self, service):
        """Test get_attack_message from attacker perspective."""
        message = await service.get_attack_message(
            attacker_name="Player1", target_name="NPC1", damage=10, perspective="attacker"
        )
        assert "You" in message
        assert "NPC1" in message
        assert "10" in message

    @pytest.mark.asyncio
    async def test_get_attack_message_defender_perspective(self, service):
        """Test get_attack_message from defender perspective."""
        message = await service.get_attack_message(
            attacker_name="Player1", target_name="NPC1", damage=15, perspective="defender"
        )
        assert "Player1" in message
        assert "you" in message.lower()
        assert "15" in message

    @pytest.mark.asyncio
    async def test_get_attack_message_other_perspective(self, service):
        """Test get_attack_message from other perspective."""
        message = await service.get_attack_message(
            attacker_name="Player1", target_name="NPC1", damage=20, perspective="other"
        )
        assert "Player1" in message
        assert "NPC1" in message
        assert "20" in message

    @pytest.mark.asyncio
    async def test_get_attack_message_custom_action_type(self, service):
        """Test get_attack_message with custom action type."""
        message = await service.get_attack_message(
            attacker_name="Player1", target_name="NPC1", damage=10, action_type="punch", perspective="attacker"
        )
        assert "punch" in message.lower()

    @pytest.mark.asyncio
    async def test_get_attack_message_custom_npc_messages(self, service):
        """Test get_attack_message with custom NPC messages."""
        npc_messages = {
            "attack_attacker": "You strike {target_name} with {damage} points of damage!",
            "attack_defender": "{attacker_name} strikes you for {damage} damage!",
            "attack_other": "{attacker_name} strikes {target_name} for {damage} damage!",
        }
        message = await service.get_attack_message(
            attacker_name="Player1", target_name="NPC1", damage=25, npc_messages=npc_messages, perspective="attacker"
        )
        assert "strike" in message.lower()
        assert "25" in message

    @pytest.mark.asyncio
    async def test_get_attack_message_fallback_to_default(self, service):
        """Test get_attack_message falls back to default when NPC message missing."""
        npc_messages = {
            "attack_defender": "Custom defender message",
            # Missing attack_attacker
        }
        message = await service.get_attack_message(
            attacker_name="Player1", target_name="NPC1", damage=10, npc_messages=npc_messages, perspective="attacker"
        )
        # Should use default message
        assert "You" in message

    @pytest.mark.asyncio
    async def test_get_death_message_default(self, service):
        """Test get_death_message with default template."""
        message = await service.get_death_message("NPC1")
        assert "NPC1" in message
        assert "dies" in message.lower()

    @pytest.mark.asyncio
    async def test_get_death_message_custom(self, service):
        """Test get_death_message with custom template."""
        npc_messages = {"death_message": "{npc_name} collapses in a heap of eldritch matter."}
        message = await service.get_death_message("NPC1", npc_messages=npc_messages)
        assert "NPC1" in message
        assert "collapses" in message.lower()

    @pytest.mark.asyncio
    async def test_get_combat_start_messages(self, service):
        """Test get_combat_start_messages generates messages for all occupants."""
        occupants = ["Player1", "Player2", "NPC1"]
        messages = await service.get_combat_start_messages("Player1", "NPC1", occupants)
        assert len(messages) == 3
        assert "You attack" in messages["Player1"]
        assert "attacks you" in messages["NPC1"]
        assert "attacks" in messages["Player2"]

    @pytest.mark.asyncio
    async def test_get_combat_start_messages_single_occupant(self, service):
        """Test get_combat_start_messages with single occupant."""
        occupants = ["Player1"]
        messages = await service.get_combat_start_messages("Player1", "NPC1", occupants)
        assert len(messages) == 1
        assert "You attack" in messages["Player1"]

    @pytest.mark.asyncio
    async def test_get_combat_end_messages(self, service):
        """Test get_combat_end_messages generates messages for all occupants."""
        occupants = ["Player1", "Player2", "NPC1"]
        messages = await service.get_combat_end_messages("Player1", "NPC1", occupants)
        assert len(messages) == 3
        assert "You defeat" in messages["Player1"]
        assert "You are defeated by" in messages["NPC1"]
        assert "defeats" in messages["Player2"]

    @pytest.mark.asyncio
    async def test_get_combat_end_messages_winner_perspective(self, service):
        """Test get_combat_end_messages from winner perspective."""
        occupants = ["Player1", "NPC1"]
        messages = await service.get_combat_end_messages("Player1", "NPC1", occupants)
        assert "You defeat" in messages["Player1"]

    @pytest.mark.asyncio
    async def test_get_combat_end_messages_loser_perspective(self, service):
        """Test get_combat_end_messages from loser perspective."""
        occupants = ["Player1", "NPC1"]
        messages = await service.get_combat_end_messages("Player1", "NPC1", occupants)
        assert "You are defeated by" in messages["NPC1"]

    @pytest.mark.asyncio
    async def test_get_combat_end_messages_empty_occupants(self, service):
        """Test get_combat_end_messages with empty occupants list."""
        messages = await service.get_combat_end_messages("Player1", "NPC1", [])
        assert len(messages) == 0

    @pytest.mark.asyncio
    async def test_get_attack_message_zero_damage(self, service):
        """Test get_attack_message handles zero damage."""
        message = await service.get_attack_message(
            attacker_name="Player1", target_name="NPC1", damage=0, perspective="attacker"
        )
        assert "0" in message

    @pytest.mark.asyncio
    async def test_get_attack_message_high_damage(self, service):
        """Test get_attack_message handles high damage values."""
        message = await service.get_attack_message(
            attacker_name="Player1", target_name="NPC1", damage=999, perspective="attacker"
        )
        assert "999" in message
