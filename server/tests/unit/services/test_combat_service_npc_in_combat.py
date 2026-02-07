"""
Unit tests for CombatService.is_npc_in_combat_sync.

Tests the NPC-in-combat check used to block normal NPC movement while in combat.
"""

import uuid
from unittest.mock import MagicMock, patch

import pytest

from server.services.combat_service import CombatService

# pylint: disable=protected-access  # Reason: Test file - accessing protected members for combat state setup
# pylint: disable=redefined-outer-name  # Reason: Pytest fixture parameter names


@pytest.fixture
def combat_service():
    """Create CombatService with mocked dependencies so is_npc_in_combat_sync can be tested."""
    with patch("server.services.combat_service.get_config") as mock_config:
        mock_config.return_value.game.combat_tick_interval = 10
        with patch("server.services.combat_service.CombatEventPublisher") as mock_pub:
            mock_pub.return_value = MagicMock()
            service = CombatService(
                player_combat_service=MagicMock(),
                nats_service=None,
                npc_combat_integration_service=None,
            )
            yield service


def test_is_npc_in_combat_sync_returns_false_when_npc_not_in_combat(combat_service):
    """Test is_npc_in_combat_sync returns False when NPC is not in any combat."""
    assert combat_service.is_npc_in_combat_sync("npc_001") is False
    assert combat_service.is_npc_in_combat_sync(str(uuid.uuid4())) is False


def test_is_npc_in_combat_sync_returns_true_when_npc_uuid_in_combat(combat_service):
    """Test is_npc_in_combat_sync returns True when NPC UUID is in _npc_combats."""
    npc_uuid = uuid.uuid4()
    combat_id = uuid.uuid4()
    combat_service._npc_combats[npc_uuid] = combat_id
    assert combat_service.is_npc_in_combat_sync(str(npc_uuid)) is True


def test_is_npc_in_combat_sync_returns_false_for_invalid_uuid_string(combat_service):
    """Test is_npc_in_combat_sync returns False for non-UUID string when no mapping."""
    assert combat_service.is_npc_in_combat_sync("cultist_001") is False


def test_is_npc_in_combat_sync_returns_true_when_string_id_mapped_to_combat(combat_service):
    """Test is_npc_in_combat_sync returns True when integration service maps string id to NPC in combat."""
    npc_uuid = uuid.uuid4()
    combat_id = uuid.uuid4()
    combat_service._npc_combats[npc_uuid] = combat_id
    mock_integration = MagicMock()
    mock_mapping = MagicMock()
    mock_mapping._uuid_to_string_id_mapping = {npc_uuid: "cultist_001"}
    mock_integration._uuid_mapping = mock_mapping
    combat_service._npc_combat_integration_service = mock_integration
    assert combat_service.is_npc_in_combat_sync("cultist_001") is True
