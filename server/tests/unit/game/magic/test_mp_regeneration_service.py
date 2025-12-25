"""
Tests for MP regeneration service.

This module tests the MPRegenerationService class which handles
passive MP regeneration and accelerated recovery from rest/meditation.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.game.magic.mp_regeneration_service import REST_MP_REGEN_MULTIPLIER, MPRegenerationService
from server.game.player_service import PlayerService


class TestMPRegenerationService:
    """Test MPRegenerationService functionality."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock()
        mock_persistence.save_player = AsyncMock()
        return mock_persistence

    @pytest.fixture
    def mock_player_service(self, mock_persistence):
        """Create a mock player service."""
        player_service = MagicMock(spec=PlayerService)
        player_service.persistence = mock_persistence
        return player_service

    @pytest.fixture
    def mp_service(self, mock_player_service):
        """Create MP regeneration service instance with higher regen rate for testing."""
        # Use higher regen rate (1.0) to ensure immediate MP restoration in tests
        # Default rate (0.01) requires fractional accumulation over many ticks
        return MPRegenerationService(mock_player_service, regen_rate=1.0)

    @pytest.fixture
    def sample_player(self):
        """Create a sample player with stats."""
        player = MagicMock()
        player.player_id = uuid4()
        player.get_stats.return_value = {
            "magic_points": 10,
            "max_magic_points": 20,
            "power": 50,
            "position": "standing",
        }
        return player

    @pytest.mark.asyncio
    async def test_process_tick_regeneration_success(self, mp_service, mock_player_service, sample_player):
        """Test successful MP regeneration on tick."""
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.mp_regeneration_service.logger"):
            result = await mp_service.process_tick_regeneration(player_id)

            assert result["mp_restored"] > 0
            assert result["current_mp"] > 10
            assert result["max_mp"] == 20
            mock_player_service.persistence.save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_tick_regeneration_player_not_found(self, mp_service, mock_player_service):
        """Test MP regeneration when player is not found."""
        player_id = uuid4()
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=None)

        result = await mp_service.process_tick_regeneration(player_id)

        assert result == {"mp_restored": 0, "current_mp": 0, "max_mp": 0}
        mock_player_service.persistence.save_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_process_tick_regeneration_already_at_max(self, mp_service, mock_player_service, sample_player):
        """Test MP regeneration when player is already at max MP."""
        sample_player.get_stats.return_value = {
            "magic_points": 20,
            "max_magic_points": 20,
            "power": 50,
            "position": "standing",
        }
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await mp_service.process_tick_regeneration(player_id)

        assert result["mp_restored"] == 0
        assert result["current_mp"] == 20
        assert result["max_mp"] == 20
        mock_player_service.persistence.save_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_process_tick_regeneration_calculates_max_from_power(
        self, mp_service, mock_player_service, sample_player
    ):
        """Test MP regeneration calculates max_mp from power when not present."""
        sample_player.get_stats.return_value = {
            "magic_points": 5,
            "power": 100,  # Should give max_mp = 20
            "position": "standing",
        }
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.mp_regeneration_service.logger"):
            result = await mp_service.process_tick_regeneration(player_id)

            assert result["max_mp"] == 20  # ceil(100 * 0.2) = 20
            assert result["current_mp"] > 5

    @pytest.mark.asyncio
    async def test_process_tick_regeneration_with_fractional_mp(self, mp_service, mock_player_service, sample_player):
        """Test MP regeneration with fractional MP accumulation."""
        sample_player.get_stats.return_value = {
            "magic_points": 10,
            "max_magic_points": 20,
            "power": 50,
            "position": "standing",
            "_mp_fractional": 0.5,  # Existing fractional MP
        }
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.mp_regeneration_service.logger"):
            result = await mp_service.process_tick_regeneration(player_id)

            assert result["mp_restored"] >= 0
            assert result["current_mp"] >= 10

    @pytest.mark.asyncio
    async def test_process_tick_regeneration_with_float_current_mp(
        self, mp_service, mock_player_service, sample_player
    ):
        """Test MP regeneration when current_mp is a float."""
        sample_player.get_stats.return_value = {
            "magic_points": 10.7,  # Float value
            "max_magic_points": 20,
            "power": 50,
            "position": "standing",
        }
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.mp_regeneration_service.logger"):
            result = await mp_service.process_tick_regeneration(player_id)

            assert result["current_mp"] >= 10
            # Fractional part should be extracted and stored

    @pytest.mark.asyncio
    async def test_process_tick_regeneration_sends_update_event(self, mp_service, mock_player_service, sample_player):
        """Test MP regeneration sends player_update event."""
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.mp_regeneration_service.logger"):
            # Patch at the import location since send_game_event is imported inside the method
            with patch("server.realtime.connection_manager_api.send_game_event") as mock_send:
                result = await mp_service.process_tick_regeneration(player_id)

                if result["mp_restored"] > 0:
                    mock_send.assert_called_once()
                    call_args = mock_send.call_args
                    assert call_args[0][0] == player_id
                    assert call_args[0][1] == "player_update"

    @pytest.mark.asyncio
    async def test_process_tick_regeneration_handles_event_send_error(
        self, mp_service, mock_player_service, sample_player
    ):
        """Test MP regeneration handles event send errors gracefully."""
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.mp_regeneration_service.logger") as mock_logger:
            # Patch at the import location since send_game_event is imported inside the method
            with patch(
                "server.realtime.connection_manager_api.send_game_event", side_effect=ValueError("Connection error")
            ):
                result = await mp_service.process_tick_regeneration(player_id)

                assert result["mp_restored"] >= 0
                mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_tick_regeneration_no_change_skips_save(self, mp_service, mock_player_service, sample_player):
        """Test MP regeneration skips save when no MP is restored."""
        sample_player.get_stats.return_value = {
            "magic_points": 20,
            "max_magic_points": 20,
            "power": 50,
            "position": "standing",
            "_mp_fractional": 0.0,
        }
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await mp_service.process_tick_regeneration(player_id)

        assert result["mp_restored"] == 0
        mock_player_service.persistence.save_player.assert_not_called()

    def test_get_regen_multiplier_standing(self, mp_service):
        """Test regeneration multiplier for standing position."""
        stats = {"position": "standing"}
        multiplier = mp_service._get_regen_multiplier(stats)
        assert multiplier == 1.0

    def test_get_regen_multiplier_sitting(self, mp_service):
        """Test regeneration multiplier for sitting position."""
        stats = {"position": "sitting"}
        multiplier = mp_service._get_regen_multiplier(stats)
        assert multiplier == REST_MP_REGEN_MULTIPLIER

    def test_get_regen_multiplier_lying(self, mp_service):
        """Test regeneration multiplier for lying position."""
        stats = {"position": "lying"}
        multiplier = mp_service._get_regen_multiplier(stats)
        assert multiplier == REST_MP_REGEN_MULTIPLIER * 1.2

    def test_get_regen_multiplier_default_position(self, mp_service):
        """Test regeneration multiplier with no position specified."""
        stats = {}
        multiplier = mp_service._get_regen_multiplier(stats)
        assert multiplier == 1.0

    @pytest.mark.asyncio
    async def test_restore_mp_from_rest_success(self, mp_service, mock_player_service, sample_player):
        """Test successful MP restoration from rest."""
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.mp_regeneration_service.logger"):
            result = await mp_service.restore_mp_from_rest(player_id, 60)

            assert result["success"] is True
            assert result["mp_restored"] > 0
            assert "rest and recover" in result["message"]
            mock_player_service.persistence.save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_restore_mp_from_rest_player_not_found(self, mp_service, mock_player_service):
        """Test MP restoration from rest when player is not found."""
        player_id = uuid4()
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=None)

        result = await mp_service.restore_mp_from_rest(player_id, 60)

        assert result["success"] is False
        assert "not found" in result["message"]
        assert result["mp_restored"] == 0

    @pytest.mark.asyncio
    async def test_restore_mp_from_rest_already_full(self, mp_service, mock_player_service, sample_player):
        """Test MP restoration from rest when MP is already full."""
        sample_player.get_stats.return_value = {
            "magic_points": 20,
            "max_magic_points": 20,
            "power": 50,
        }
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await mp_service.restore_mp_from_rest(player_id, 60)

        assert result["success"] is True
        assert result["mp_restored"] == 0
        assert "already full" in result["message"]

    @pytest.mark.asyncio
    async def test_restore_mp_from_rest_calculates_max_from_power(self, mp_service, mock_player_service, sample_player):
        """Test MP restoration calculates max_mp from power."""
        sample_player.get_stats.return_value = {
            "magic_points": 5,
            "power": 100,
        }
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.mp_regeneration_service.logger"):
            result = await mp_service.restore_mp_from_rest(player_id, 60)

            assert result["success"] is True
            assert result["max_mp"] == 20

    @pytest.mark.asyncio
    async def test_restore_mp_from_meditation_success(self, mp_service, mock_player_service, sample_player):
        """Test successful MP restoration from meditation."""
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        with patch("server.game.magic.mp_regeneration_service.logger"):
            result = await mp_service.restore_mp_from_meditation(player_id, 180)

            assert result["success"] is True
            assert result["mp_restored"] > 0
            assert "meditation" in result["message"].lower()
            mock_player_service.persistence.save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_restore_mp_from_meditation_player_not_found(self, mp_service, mock_player_service):
        """Test MP restoration from meditation when player is not found."""
        player_id = uuid4()
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=None)

        result = await mp_service.restore_mp_from_meditation(player_id, 180)

        assert result["success"] is False
        assert "not found" in result["message"]

    @pytest.mark.asyncio
    async def test_restore_mp_from_meditation_already_full(self, mp_service, mock_player_service, sample_player):
        """Test MP restoration from meditation when MP is already full."""
        sample_player.get_stats.return_value = {
            "magic_points": 20,
            "max_magic_points": 20,
            "power": 50,
        }
        player_id = sample_player.player_id
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await mp_service.restore_mp_from_meditation(player_id, 180)

        assert result["success"] is True
        assert result["mp_restored"] == 0
        assert "already full" in result["message"]

    @pytest.mark.asyncio
    async def test_restore_mp_from_item_with_magic_service(self, mp_service, mock_player_service, sample_player):
        """Test MP restoration from item when magic_service is available."""
        player_id = sample_player.player_id
        mock_magic_service = MagicMock()
        mock_magic_service.restore_mp = AsyncMock(return_value={"success": True, "mp_restored": 10})
        mock_player_service.magic_service = mock_magic_service

        result = await mp_service.restore_mp_from_item(player_id, 10)

        assert result["success"] is True
        assert result["mp_restored"] == 10
        mock_magic_service.restore_mp.assert_called_once_with(player_id, 10)

    @pytest.mark.asyncio
    async def test_restore_mp_from_item_without_magic_service(self, mp_service, mock_player_service, sample_player):
        """Test MP restoration from item when magic_service is not available."""
        player_id = sample_player.player_id
        mock_player_service.magic_service = None
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await mp_service.restore_mp_from_item(player_id, 10)

        assert result["success"] is True
        assert result["mp_restored"] > 0
        mock_player_service.persistence.save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_restore_mp_from_item_player_not_found(self, mp_service, mock_player_service):
        """Test MP restoration from item when player is not found."""
        player_id = uuid4()
        mock_player_service.magic_service = None
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=None)

        result = await mp_service.restore_mp_from_item(player_id, 10)

        assert result["success"] is False
        assert "not found" in result["message"]

    @pytest.mark.asyncio
    async def test_restore_mp_from_item_caps_at_max(self, mp_service, mock_player_service, sample_player):
        """Test MP restoration from item caps at max_mp."""
        sample_player.get_stats.return_value = {
            "magic_points": 18,
            "max_magic_points": 20,
            "power": 50,
        }
        player_id = sample_player.player_id
        mock_player_service.magic_service = None
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await mp_service.restore_mp_from_item(player_id, 10)  # Would go over max

        assert result["success"] is True
        assert result["current_mp"] == 20  # Capped at max
        assert result["mp_restored"] == 2  # Only 2 MP restored (18 -> 20)

    @pytest.mark.asyncio
    async def test_restore_mp_from_item_calculates_max_from_power(self, mp_service, mock_player_service, sample_player):
        """Test MP restoration calculates max_mp from power when not present."""
        sample_player.get_stats.return_value = {
            "magic_points": 5,
            "power": 100,
        }
        player_id = sample_player.player_id
        mock_player_service.magic_service = None
        mock_player_service.persistence.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await mp_service.restore_mp_from_item(player_id, 10)

        assert result["success"] is True
        assert result["max_mp"] == 20

    def test_service_initialization(self, mock_player_service):
        """Test service initialization with custom regen rate."""
        custom_rate = 0.02
        with patch("server.game.magic.mp_regeneration_service.logger"):
            service = MPRegenerationService(mock_player_service, regen_rate=custom_rate)
            assert service.regen_rate == custom_rate
            assert service.player_service == mock_player_service

    def test_service_initialization_default_rate(self, mock_player_service):
        """Test service initialization with default regen rate."""
        with patch("server.game.magic.mp_regeneration_service.logger"):
            service = MPRegenerationService(mock_player_service)
            assert service.regen_rate > 0
