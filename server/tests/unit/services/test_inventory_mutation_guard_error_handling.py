"""
Unit tests for inventory mutation guard - error handling and monitoring.

Tests error handling scenarios and monitoring/alerting integration.
"""

import uuid

import pytest

from server.services.inventory_mutation_guard import InventoryMutationGuard

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def guard():
    """Create an InventoryMutationGuard instance."""
    return InventoryMutationGuard(token_ttl_seconds=300.0, max_tokens=128)


@pytest.mark.asyncio
async def test_cleanup_async_state_lock_attribute_error(guard):
    """Test _cleanup_async_state handles AttributeError from lock.locked()."""
    player_id = str(uuid.uuid4())
    state = await guard._get_async_state(player_id)

    # Create a mock lock that raises AttributeError when locked() is called
    class MockLock:
        """Mock lock for testing error handling when locked() raises AttributeError."""

        def __init__(self):
            self._locked = False

        async def acquire(self):
            """Acquire the lock by setting _locked to True."""
            self._locked = True

        def release(self):
            """Release the lock by setting _locked to False."""
            self._locked = False

        def locked(self):
            """Raise AttributeError to simulate lock method not available."""
            raise AttributeError("locked() not available")

    mock_lock = MockLock()
    state.lock = mock_lock

    # Should handle AttributeError gracefully and skip cleanup
    await guard._cleanup_async_state(player_id)
    # State should still exist (cleanup skipped due to error)
    assert player_id in guard._async_states


@pytest.mark.asyncio
async def test_cleanup_async_state_lock_runtime_error(guard):
    """Test _cleanup_async_state handles RuntimeError from lock.locked()."""
    player_id = str(uuid.uuid4())
    state = await guard._get_async_state(player_id)

    # Create a mock lock that raises RuntimeError when locked() is called
    class MockLock:
        """Mock lock for testing error handling when locked() raises RuntimeError."""

        def __init__(self):
            self._locked = False

        async def acquire(self):
            """Acquire the lock by setting _locked to True."""
            self._locked = True

        def release(self):
            """Release the lock by setting _locked to False."""
            self._locked = False

        def locked(self):
            """Raise RuntimeError to simulate lock in inconsistent state."""
            raise RuntimeError("Lock in inconsistent state")

    mock_lock = MockLock()
    state.lock = mock_lock

    # Should handle RuntimeError gracefully and skip cleanup
    await guard._cleanup_async_state(player_id)
    # State should still exist (cleanup skipped due to error)
    assert player_id in guard._async_states


def test_acquire_record_custom_alert_with_message_param(guard):
    """Test acquire handles record_custom_alert with message parameter."""
    from unittest.mock import MagicMock, patch

    player_id = str(uuid.uuid4())
    token = "duplicate_token"

    # First acquisition
    with guard.acquire(player_id, token):
        pass

    # Mock dashboard with record_custom_alert that has 'message' parameter
    mock_dashboard = MagicMock()

    def record_with_message(_alert_type, *, _severity=None, _message=None, _metadata=None):
        pass

    mock_dashboard.record_custom_alert = record_with_message

    with patch("server.services.inventory_mutation_guard.get_monitoring_dashboard", return_value=mock_dashboard):
        with patch("server.services.inventory_mutation_guard.metrics_collector") as mock_metrics:
            # Second acquisition should trigger duplicate detection
            with guard.acquire(player_id, token) as decision:
                assert decision.should_apply is False
                assert decision.duplicate is True
                mock_metrics.record_message_failed.assert_called_once()


@pytest.mark.asyncio
async def test_acquire_async_record_custom_alert_with_message_param(guard):
    """Test acquire_async handles record_custom_alert with message parameter."""
    from unittest.mock import MagicMock, patch

    player_id = str(uuid.uuid4())
    token = "duplicate_token_async"

    # First acquisition
    async with guard.acquire_async(player_id, token):
        pass

    # Mock dashboard with record_custom_alert that has 'message' parameter
    mock_dashboard = MagicMock()

    def record_with_message(_alert_type, *, _severity=None, _message=None, _metadata=None):
        pass

    mock_dashboard.record_custom_alert = record_with_message

    with patch("server.services.inventory_mutation_guard.get_monitoring_dashboard", return_value=mock_dashboard):
        with patch("server.services.inventory_mutation_guard.metrics_collector") as mock_metrics:
            # Second acquisition should trigger duplicate detection
            async with guard.acquire_async(player_id, token) as decision:
                assert decision.should_apply is False
                assert decision.duplicate is True
                mock_metrics.record_message_failed.assert_called_once()


def test_acquire_record_custom_alert_type_error_fallback(guard):
    """Test acquire handles TypeError from record_custom_alert and uses fallback."""
    from unittest.mock import MagicMock, patch

    player_id = str(uuid.uuid4())
    token = "duplicate_token"

    # First acquisition
    with guard.acquire(player_id, token):
        pass

    # Mock dashboard with record_custom_alert that raises TypeError
    mock_dashboard = MagicMock()

    def record_raises_typeerror(alert_type, *, severity=None, metadata=None):
        raise TypeError("Invalid arguments")

    mock_dashboard.record_custom_alert = record_raises_typeerror

    with patch("server.services.inventory_mutation_guard.get_monitoring_dashboard", return_value=mock_dashboard):
        with patch("server.services.inventory_mutation_guard.metrics_collector") as mock_metrics:
            # Should handle TypeError gracefully
            with guard.acquire(player_id, token) as decision:
                assert decision.should_apply is False
                assert decision.duplicate is True
                mock_metrics.record_message_failed.assert_called_once()


@pytest.mark.asyncio
async def test_acquire_async_record_custom_alert_type_error_fallback(guard):
    """Test acquire_async handles TypeError from record_custom_alert and uses fallback."""
    from unittest.mock import MagicMock, patch

    player_id = str(uuid.uuid4())
    token = "duplicate_token_async"

    # First acquisition
    async with guard.acquire_async(player_id, token):
        pass

    # Mock dashboard with record_custom_alert that raises TypeError
    mock_dashboard = MagicMock()

    def record_raises_typeerror(alert_type, *, severity=None, metadata=None):
        raise TypeError("Invalid arguments")

    mock_dashboard.record_custom_alert = record_raises_typeerror

    with patch("server.services.inventory_mutation_guard.get_monitoring_dashboard", return_value=mock_dashboard):
        with patch("server.services.inventory_mutation_guard.metrics_collector") as mock_metrics:
            # Should handle TypeError gracefully
            async with guard.acquire_async(player_id, token) as decision:
                assert decision.should_apply is False
                assert decision.duplicate is True
                mock_metrics.record_message_failed.assert_called_once()
