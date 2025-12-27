"""
Smoke test for LucidityService.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.lucidity import PlayerLucidity
from server.services.lucidity_service import LucidityService


@pytest.mark.asyncio
async def test_lucidity_service_apply_adjustment():
    """Test that LucidityService can apply a lucidity adjustment with mocked repo."""
    # Create a mock session with async methods
    mock_session = MagicMock()
    mock_session.flush = AsyncMock()
    
    # Create a mock repository
    mock_repo = MagicMock()
    mock_record = PlayerLucidity(
        player_id=uuid.uuid4(),
        current_lcd=50,
        current_tier="uneasy",
    )
    mock_repo.get_or_create_player_lucidity = AsyncMock(return_value=mock_record)
    mock_repo.add_adjustment_log = AsyncMock()
    
    # Create service with mocked repo
    service = LucidityService(mock_session)
    service._repo = mock_repo  # Replace with mock
    
    # Apply adjustment
    player_id = uuid.uuid4()
    result = await service.apply_lucidity_adjustment(
        player_id=player_id,
        delta=-10,
        reason_code="test_adjustment",
    )
    
    # Verify repo was called
    mock_repo.get_or_create_player_lucidity.assert_called_once()
    
    # Verify result structure
    assert result.player_id == player_id
    assert result.previous_lcd == 50
    assert result.new_lcd == 40  # 50 - 10
    assert isinstance(result.liabilities_added, list)

