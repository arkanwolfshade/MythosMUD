"""
Unit tests for game tick processing async functions.

Tests the async game tick processing functions (status effects: test_game_tick_status_effects.py).
"""

from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import FastAPI

from server.app.game_tick_processing import process_combat_tick


@pytest.fixture
def mock_app():
    """Create a mock FastAPI app."""
    app = MagicMock(spec=FastAPI)
    app.state = MagicMock()
    return app


@pytest.mark.asyncio
async def test_process_combat_tick_no_service(mock_app):  # pylint: disable=redefined-outer-name
    """Test process_combat_tick() when combat service is not available."""
    # Parameter name must match fixture name for pytest automatic injection
    mock_app.state.combat_service = None
    await process_combat_tick(mock_app, 1)
    # Should not raise


@pytest.mark.asyncio
async def test_process_combat_tick_success(mock_app):  # pylint: disable=redefined-outer-name
    """Test process_combat_tick() successful execution."""
    # Parameter name must match fixture name for pytest automatic injection
    mock_combat_service = AsyncMock()
    mock_combat_service.process_game_tick = AsyncMock()
    mock_app.state.container = MagicMock()
    mock_app.state.container.combat_service = mock_combat_service
    await process_combat_tick(mock_app, 1)
    mock_combat_service.process_game_tick.assert_awaited_once_with(1)
