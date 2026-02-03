"""
Unit tests for NPCCombatDataProvider.

Tests get_player_combat_data and get_npc_combat_data use model get_combat_stats.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.combat import CombatParticipantType
from server.services.combat_types import CombatParticipantData
from server.services.npc_combat_data_provider import NPCCombatDataProvider


@pytest.fixture
def mock_persistence():
    """Create mock persistence layer."""
    return MagicMock()


@pytest.fixture
def data_provider(mock_persistence):
    """Create NPCCombatDataProvider instance."""
    return NPCCombatDataProvider(mock_persistence)


@pytest.mark.asyncio
async def test_get_player_combat_data_uses_get_combat_stats(data_provider, mock_persistence):
    """Test get_player_combat_data delegates to Player.get_combat_stats()."""
    from server.models.player import Player

    player_id = uuid.uuid4()
    player = Player(
        player_id=str(player_id),
        user_id=str(uuid.uuid4()),
        name="TestPlayer",
        stats={"current_dp": 60, "max_dp": 80, "dexterity": 14},
    )
    mock_persistence.get_player_by_id = AsyncMock(return_value=player)

    result = await data_provider.get_player_combat_data(
        player_id=str(player_id), attacker_uuid=player_id, player_name="TestPlayer"
    )

    assert isinstance(result, CombatParticipantData)
    assert result.participant_id == player_id
    assert result.name == "TestPlayer"
    assert result.current_dp == 60
    assert result.max_dp == 80
    assert result.dexterity == 14
    assert result.participant_type == CombatParticipantType.PLAYER


def test_get_npc_combat_data_uses_get_combat_stats(data_provider):
    """Test get_npc_combat_data delegates to NPC get_combat_stats()."""
    from server.npc.passive_mob_npc import PassiveMobNPC

    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = '{"determination_points": 45, "max_dp": 50, "dexterity": 11}'
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-001")
    target_uuid = uuid.uuid4()

    result = data_provider.get_npc_combat_data(npc_instance=npc, target_uuid=target_uuid)

    assert isinstance(result, CombatParticipantData)
    assert result.participant_id == target_uuid
    assert result.name == "TestMob"
    assert result.current_dp == 45
    assert result.max_dp == 50
    assert result.dexterity == 11
    assert result.participant_type == CombatParticipantType.NPC


def test_get_npc_combat_data_fallback_without_get_combat_stats(data_provider):
    """Test get_npc_combat_data falls back to get_stats when get_combat_stats absent."""

    class LegacyNPC:
        """Minimal NPC-like object without get_combat_stats."""

        name = "LegacyNPC"

        def get_stats(self):
            return {
                "determination_points": 30,
                "max_dp": 40,
                "dexterity": 9,
            }

    legacy_npc = LegacyNPC()
    target_uuid = uuid.uuid4()
    result = data_provider.get_npc_combat_data(npc_instance=legacy_npc, target_uuid=target_uuid)

    assert result.current_dp == 30
    assert result.max_dp == 40
    assert result.dexterity == 9
