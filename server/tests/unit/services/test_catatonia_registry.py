"""
Unit tests for catatonia registry.

Tests the CatatoniaRegistry class for tracking catatonic players
and coordinating failover hooks.
"""

import asyncio
import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.catatonia_registry import CatatoniaRegistry


class TestCatatoniaRegistry:
    """Test suite for CatatoniaRegistry class."""

    def test_init(self):
        """Test CatatoniaRegistry initialization."""
        registry = CatatoniaRegistry()
        assert registry._catatonic == {}
        assert registry._failover_callback is None

    def test_init_with_failover_callback(self):
        """Test CatatoniaRegistry initialization with failover callback."""
        callback = MagicMock()
        registry = CatatoniaRegistry(failover_callback=callback)
        assert registry._failover_callback is callback

    def test_on_catatonia_entered_with_uuid(self):
        """Test on_catatonia_entered with UUID player_id."""
        registry = CatatoniaRegistry()
        player_id = uuid.uuid4()
        entered_at = datetime.now(UTC)

        registry.on_catatonia_entered(player_id=player_id, entered_at=entered_at, current_lcd=0)

        assert str(player_id) in registry._catatonic
        assert registry._catatonic[str(player_id)] == entered_at

    def test_on_catatonia_entered_with_string(self):
        """Test on_catatonia_entered with string player_id."""
        registry = CatatoniaRegistry()
        player_id = "test-player-123"
        entered_at = datetime.now(UTC)

        registry.on_catatonia_entered(player_id=player_id, entered_at=entered_at, current_lcd=0)

        assert player_id in registry._catatonic
        assert registry._catatonic[player_id] == entered_at

    def test_on_catatonia_cleared_with_uuid(self):
        """Test on_catatonia_cleared removes player from registry."""
        registry = CatatoniaRegistry()
        player_id = uuid.uuid4()
        entered_at = datetime.now(UTC)

        registry.on_catatonia_entered(player_id=player_id, entered_at=entered_at, current_lcd=0)
        assert str(player_id) in registry._catatonic

        resolved_at = datetime.now(UTC)
        registry.on_catatonia_cleared(player_id=player_id, resolved_at=resolved_at)

        assert str(player_id) not in registry._catatonic

    def test_on_catatonia_cleared_with_string(self):
        """Test on_catatonia_cleared with string player_id."""
        registry = CatatoniaRegistry()
        player_id = "test-player-123"
        entered_at = datetime.now(UTC)

        registry.on_catatonia_entered(player_id=player_id, entered_at=entered_at, current_lcd=0)
        assert player_id in registry._catatonic

        resolved_at = datetime.now(UTC)
        registry.on_catatonia_cleared(player_id=player_id, resolved_at=resolved_at)

        assert player_id not in registry._catatonic

    def test_on_catatonia_cleared_not_registered(self):
        """Test on_catatonia_cleared handles player not in registry."""
        registry = CatatoniaRegistry()
        player_id = uuid.uuid4()
        resolved_at = datetime.now(UTC)

        # Should not raise an error
        registry.on_catatonia_cleared(player_id=player_id, resolved_at=resolved_at)
        assert str(player_id) not in registry._catatonic

    def test_on_sanitarium_failover_with_uuid(self):
        """Test on_sanitarium_failover with UUID player_id."""
        registry = CatatoniaRegistry()
        player_id = uuid.uuid4()

        registry.on_sanitarium_failover(player_id=player_id, current_lcd=0)

        assert str(player_id) in registry._catatonic
        # Should have been set to current time (approximately)
        assert isinstance(registry._catatonic[str(player_id)], datetime)

    def test_on_sanitarium_failover_with_string(self):
        """Test on_sanitarium_failover with string player_id."""
        registry = CatatoniaRegistry()
        player_id = "test-player-123"

        registry.on_sanitarium_failover(player_id=player_id, current_lcd=0)

        assert player_id in registry._catatonic
        assert isinstance(registry._catatonic[player_id], datetime)

    def test_on_sanitarium_failover_with_sync_callback(self):
        """Test on_sanitarium_failover with synchronous callback."""
        callback = MagicMock(return_value=None)
        registry = CatatoniaRegistry(failover_callback=callback)
        player_id = "test-player-123"

        registry.on_sanitarium_failover(player_id=player_id, current_lcd=0)

        callback.assert_called_once_with(player_id, 0)

    @pytest.mark.asyncio
    async def test_on_sanitarium_failover_with_async_callback(self):
        """Test on_sanitarium_failover with async callback."""
        async_callback = AsyncMock()
        registry = CatatoniaRegistry(failover_callback=async_callback)
        player_id = "test-player-123"

        registry.on_sanitarium_failover(player_id=player_id, current_lcd=0)

        # Give the task a moment to be created
        await asyncio.sleep(0.1)
        async_callback.assert_called_once_with(player_id, 0)

    def test_on_sanitarium_failover_without_callback(self):
        """Test on_sanitarium_failover without callback."""
        registry = CatatoniaRegistry()
        player_id = uuid.uuid4()

        # Should not raise an error
        registry.on_sanitarium_failover(player_id=player_id, current_lcd=0)
        assert str(player_id) in registry._catatonic

    def test_on_sanitarium_failover_callback_exception(self):
        """Test on_sanitarium_failover handles callback exceptions."""
        callback = MagicMock(side_effect=ValueError("Callback error"))
        registry = CatatoniaRegistry(failover_callback=callback)
        player_id = "test-player-123"

        # Should not raise an error, should handle gracefully
        with patch("server.services.catatonia_registry.logger") as mock_logger:
            registry.on_sanitarium_failover(player_id=player_id, current_lcd=0)
            mock_logger.error.assert_called_once()

    def test_is_catatonic_with_uuid(self):
        """Test is_catatonic with UUID player_id."""
        registry = CatatoniaRegistry()
        player_id = uuid.uuid4()
        entered_at = datetime.now(UTC)

        assert registry.is_catatonic(player_id) is False

        registry.on_catatonia_entered(player_id=player_id, entered_at=entered_at, current_lcd=0)
        assert registry.is_catatonic(player_id) is True

    def test_is_catatonic_with_string(self):
        """Test is_catatonic with string player_id."""
        registry = CatatoniaRegistry()
        player_id = "test-player-123"
        entered_at = datetime.now(UTC)

        assert registry.is_catatonic(player_id) is False

        registry.on_catatonia_entered(player_id=player_id, entered_at=entered_at, current_lcd=0)
        assert registry.is_catatonic(player_id) is True

    def test_is_catatonic_after_cleared(self):
        """Test is_catatonic returns False after player is cleared."""
        registry = CatatoniaRegistry()
        player_id = uuid.uuid4()
        entered_at = datetime.now(UTC)

        registry.on_catatonia_entered(player_id=player_id, entered_at=entered_at, current_lcd=0)
        assert registry.is_catatonic(player_id) is True

        registry.on_catatonia_cleared(player_id=player_id, resolved_at=datetime.now(UTC))
        assert registry.is_catatonic(player_id) is False

    def test_get_snapshot_empty(self):
        """Test get_snapshot returns empty dict when no catatonic players."""
        registry = CatatoniaRegistry()
        snapshot = registry.get_snapshot()
        assert snapshot == {}

    def test_get_snapshot_with_players(self):
        """Test get_snapshot returns copy of catatonic players."""
        registry = CatatoniaRegistry()
        player_id1 = uuid.uuid4()
        player_id2 = uuid.uuid4()
        entered_at1 = datetime.now(UTC)
        entered_at2 = datetime.now(UTC)

        registry.on_catatonia_entered(player_id=player_id1, entered_at=entered_at1, current_lcd=0)
        registry.on_catatonia_entered(player_id=player_id2, entered_at=entered_at2, current_lcd=0)

        snapshot = registry.get_snapshot()
        assert len(snapshot) == 2
        assert str(player_id1) in snapshot
        assert str(player_id2) in snapshot
        assert snapshot[str(player_id1)] == entered_at1
        assert snapshot[str(player_id2)] == entered_at2

    def test_get_snapshot_is_copy(self):
        """Test get_snapshot returns a copy, not a reference."""
        registry = CatatoniaRegistry()
        player_id = uuid.uuid4()
        entered_at = datetime.now(UTC)

        registry.on_catatonia_entered(player_id=player_id, entered_at=entered_at, current_lcd=0)
        snapshot = registry.get_snapshot()

        # Modify snapshot
        snapshot["new-player"] = datetime.now(UTC)

        # Original registry should not be affected
        assert "new-player" not in registry._catatonic

    def test_multiple_players_catatonic(self):
        """Test registry can track multiple catatonic players."""
        registry = CatatoniaRegistry()
        player_id1 = uuid.uuid4()
        player_id2 = uuid.uuid4()
        player_id3 = "test-player-123"
        entered_at = datetime.now(UTC)

        registry.on_catatonia_entered(player_id=player_id1, entered_at=entered_at, current_lcd=0)
        registry.on_catatonia_entered(player_id=player_id2, entered_at=entered_at, current_lcd=0)
        registry.on_catatonia_entered(player_id=player_id3, entered_at=entered_at, current_lcd=0)

        assert registry.is_catatonic(player_id1) is True
        assert registry.is_catatonic(player_id2) is True
        assert registry.is_catatonic(player_id3) is True
        assert len(registry.get_snapshot()) == 3
