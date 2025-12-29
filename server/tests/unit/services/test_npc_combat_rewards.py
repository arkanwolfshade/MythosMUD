"""
Unit tests for NPC combat rewards.

Tests the NPCCombatRewards class for XP calculation and rewards.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.services.npc_combat_rewards import NPCCombatRewards


class TestNPCCombatRewards:
    """Test suite for NPCCombatRewards class."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return MagicMock()

    @pytest.fixture
    def mock_game_mechanics(self):
        """Create a mock game mechanics service."""
        mechanics = MagicMock()
        mechanics.gain_experience = MagicMock(return_value=(True, "XP awarded"))
        return mechanics

    @pytest.fixture
    def rewards_service(self, mock_persistence, mock_game_mechanics):
        """Create a NPCCombatRewards instance for testing."""
        return NPCCombatRewards(mock_persistence, mock_game_mechanics)

    def test_init(self, mock_persistence, mock_game_mechanics):
        """Test NPCCombatRewards initialization."""
        service = NPCCombatRewards(mock_persistence, mock_game_mechanics)
        assert service._persistence == mock_persistence
        assert service._game_mechanics == mock_game_mechanics

    @pytest.mark.asyncio
    async def test_calculate_xp_reward_with_npc_definition(self, rewards_service):
        """Test calculate_xp_reward returns XP from NPC definition."""
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = {"xp_value": 100}
        result = await rewards_service.calculate_xp_reward(mock_npc)
        assert result == 100

    @pytest.mark.asyncio
    async def test_calculate_xp_reward_no_xp_value(self, rewards_service):
        """Test calculate_xp_reward returns 0 when no xp_value in stats."""
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = {"hp": 50}
        result = await rewards_service.calculate_xp_reward(mock_npc)
        assert result == 0

    @pytest.mark.asyncio
    async def test_calculate_xp_reward_none_npc(self, rewards_service):
        """Test calculate_xp_reward returns 0 when NPC is None."""
        result = await rewards_service.calculate_xp_reward(None)
        assert result == 0

    @pytest.mark.asyncio
    async def test_calculate_xp_reward_non_dict_stats(self, rewards_service):
        """Test calculate_xp_reward returns 0 when stats is not a dict."""
        mock_npc = MagicMock()
        mock_npc.get_base_stats.return_value = "not_a_dict"
        result = await rewards_service.calculate_xp_reward(mock_npc)
        assert result == 0

    @pytest.mark.asyncio
    async def test_is_valid_uuid_valid(self, rewards_service):
        """Test _is_valid_uuid returns True for valid UUID."""
        from uuid import uuid4

        valid_uuid = str(uuid4())
        assert rewards_service._is_valid_uuid(valid_uuid) is True

    @pytest.mark.asyncio
    async def test_is_valid_uuid_invalid(self, rewards_service):
        """Test _is_valid_uuid returns False for invalid UUID."""
        assert rewards_service._is_valid_uuid("not-a-uuid") is False
        assert rewards_service._is_valid_uuid("12345") is False

    @pytest.mark.asyncio
    async def test_check_player_connection_state_with_connection_manager(self, rewards_service):
        """Test check_player_connection_state logs connection state."""
        from uuid import UUID, uuid4

        player_id = str(uuid4())
        # ApplicationContainer is imported inside the method, so patch it at the import location
        with patch("server.container.ApplicationContainer") as mock_container:
            mock_instance = MagicMock()
            mock_instance.connection_manager = MagicMock()
            mock_instance.connection_manager.player_websockets = {UUID(player_id): MagicMock()}
            mock_container.get_instance.return_value = mock_instance

            await rewards_service.check_player_connection_state(player_id)
            # Should not raise

    @pytest.mark.asyncio
    async def test_check_player_connection_state_no_container(self, rewards_service):
        """Test check_player_connection_state handles missing container."""
        from uuid import uuid4

        player_id = str(uuid4())
        # ApplicationContainer is imported inside the method, so patch it at the import location
        with patch("server.container.ApplicationContainer", side_effect=ImportError("Test")):
            await rewards_service.check_player_connection_state(player_id)
            # Should not raise

    @pytest.mark.asyncio
    async def test_award_xp_to_killer_success(self, rewards_service):
        """Test award_xp_to_killer successfully awards XP."""
        killer_id = "player_001"
        npc_id = "npc_001"
        xp_reward = 100

        await rewards_service.award_xp_to_killer(killer_id, npc_id, xp_reward)

        rewards_service._game_mechanics.gain_experience.assert_called_once_with(
            killer_id, xp_reward, f"killed_{npc_id}"
        )

    @pytest.mark.asyncio
    async def test_award_xp_to_killer_failure(self, rewards_service, mock_game_mechanics):
        """Test award_xp_to_killer handles failure gracefully."""
        killer_id = "player_001"
        npc_id = "npc_001"
        xp_reward = 100

        mock_game_mechanics.gain_experience.return_value = (False, "Error message")

        await rewards_service.award_xp_to_killer(killer_id, npc_id, xp_reward)

        # Should not raise, just log warning

    @pytest.mark.asyncio
    async def test_award_xp_to_killer_exception(self, rewards_service, mock_game_mechanics):
        """Test award_xp_to_killer handles exceptions gracefully."""
        killer_id = "player_001"
        npc_id = "npc_001"
        xp_reward = 100

        mock_game_mechanics.gain_experience.side_effect = ValueError("Test error")

        await rewards_service.award_xp_to_killer(killer_id, npc_id, xp_reward)

        # Should not raise, just log error

    @pytest.mark.asyncio
    async def test_award_xp_to_killer_zero_xp(self, rewards_service):
        """Test award_xp_to_killer handles zero XP."""
        killer_id = "player_001"
        npc_id = "npc_001"
        xp_reward = 0

        await rewards_service.award_xp_to_killer(killer_id, npc_id, xp_reward)

        rewards_service._game_mechanics.gain_experience.assert_called_once_with(killer_id, 0, f"killed_{npc_id}")
