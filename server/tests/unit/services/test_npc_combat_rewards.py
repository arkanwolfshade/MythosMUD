"""
Unit tests for NPC combat rewards.

Tests the NPCCombatRewards class for XP calculation. Awarding XP moved to
LevelService.grant_xp (#879); this class only calculates the reward amount.
"""

from unittest.mock import MagicMock

import pytest

from server.services.npc_combat_rewards import NPCCombatRewards


class TestNPCCombatRewards:
    """Test suite for NPCCombatRewards class."""

    @pytest.fixture
    def rewards_service(self):
        """Create a NPCCombatRewards instance for testing."""
        return NPCCombatRewards()

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
