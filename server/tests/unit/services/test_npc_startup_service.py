"""
Unit tests for NPC startup service.

Tests the NPCStartupService class.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.npc_startup_service import NPCStartupService


@pytest.fixture
def npc_startup_service():
    """Create an NPCStartupService instance."""
    return NPCStartupService()


def test_npc_startup_service_init(npc_startup_service):
    """Test NPCStartupService initialization."""
    assert npc_startup_service is not None


@pytest.mark.asyncio
async def test_spawn_npcs_on_startup(npc_startup_service):
    """Test spawn_npcs_on_startup() processes startup spawning."""
    # This is a complex integration test that would require many mocks
    # For now, just verify the method exists and can be called
    with patch("server.services.npc_startup_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_get_service.return_value = mock_service
        with patch("server.services.npc_startup_service.get_npc_session") as mock_get_session:
            mock_session = AsyncMock()
            mock_get_session.return_value = [mock_session]
            with patch("server.services.npc_startup_service.npc_service") as mock_npc_service:
                mock_npc_service.get_npc_definitions = AsyncMock(return_value=[])
                result = await npc_startup_service.spawn_npcs_on_startup()
                assert "total_attempted" in result
                assert "total_spawned" in result
