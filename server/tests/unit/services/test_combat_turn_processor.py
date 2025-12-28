"""
Unit tests for combat turn processor.

Tests the CombatTurnProcessor class.
"""

from unittest.mock import MagicMock

import pytest

from server.models.combat import CombatStatus
from server.services.combat_turn_processor import CombatTurnProcessor


@pytest.fixture
def mock_combat_service():
    """Create a mock combat service."""
    return MagicMock()


@pytest.fixture
def combat_turn_processor(mock_combat_service):
    """Create a CombatTurnProcessor instance."""
    return CombatTurnProcessor(mock_combat_service)


def test_combat_turn_processor_init(combat_turn_processor, mock_combat_service):
    """Test CombatTurnProcessor initialization."""
    assert combat_turn_processor._combat_service == mock_combat_service


@pytest.mark.asyncio
async def test_process_game_tick_disabled(combat_turn_processor):
    """Test process_game_tick() returns early when auto-progression is disabled."""
    active_combats = {}
    await combat_turn_processor.process_game_tick(100, active_combats, auto_progression_enabled=False)
    # Should return early without processing


@pytest.mark.asyncio
async def test_process_game_tick_no_combats(combat_turn_processor):
    """Test process_game_tick() with no active combats."""
    active_combats = {}
    await combat_turn_processor.process_game_tick(100, active_combats, auto_progression_enabled=True)
    # Should complete without errors


@pytest.mark.asyncio
async def test_process_game_tick_inactive_combat(combat_turn_processor):
    """Test process_game_tick() skips inactive combats."""
    mock_combat = MagicMock()
    mock_combat.status = CombatStatus.ENDED
    active_combats = {"combat_001": mock_combat}
    await combat_turn_processor.process_game_tick(100, active_combats, auto_progression_enabled=True)
    # Should skip inactive combat
