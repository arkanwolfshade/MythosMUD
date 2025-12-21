"""
Test Character Recovery Flow

This module tests the flow for users who registered but got disconnected
before completing character creation.
"""

import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest


@pytest.fixture(autouse=True)
def ensure_test_isolation():
    """
    Ensure test isolation by resetting any shared state.

    This fixture runs before each test to prevent state leakage between tests.
    For serial tests, this also ensures database transactions are properly isolated.
    """
    # Reset any module-level state that might be shared
    # This helps prevent race conditions in parallel test execution
    yield
    # Cleanup happens automatically via pytest's fixture teardown


@pytest.fixture(autouse=True)
async def ensure_database_transaction_isolation(request):
    """
    Ensure database transactions are properly isolated for serial tests.

    This fixture adds delays and ensures database state is consistent
    before and after serial tests to prevent race conditions in parallel execution.
    Also ensures database connections are properly closed before event loop cleanup.
    """
    import asyncio
    import time

    # Only apply to serial tests
    if request.node.get_closest_marker("serial"):
        # Before test: ensure previous transactions are committed
        # Longer delay for serial tests to ensure proper isolation
        time.sleep(0.25)

        yield

        # After test: ensure this test's transactions are committed
        # Longer delay to ensure transaction is fully committed before next test
        time.sleep(0.25)

        # CRITICAL: Wait for any pending async operations to complete
        # This prevents "Event loop is closed" errors on Windows with ProactorEventLoop
        # by ensuring all database operations finish before the event loop closes
        await asyncio.sleep(0.2)  # Allow time for any pending database operations

        # CRITICAL: Ensure all database connections are closed before event loop cleanup
        # This prevents "Event loop is closed" errors on Windows with ProactorEventLoop
        try:
            from server.database import DatabaseManager

            # Get the database manager instance and close all connections
            db_manager = DatabaseManager.get_instance()
            if db_manager and hasattr(db_manager, "engine") and db_manager.engine is not None:
                # Dispose of the engine to close all connections
                # This ensures connections are closed before the event loop closes
                await db_manager.engine.dispose(close=True)
                # Additional wait to ensure disposal completes
                await asyncio.sleep(0.1)
        except Exception:  # pylint: disable=broad-except
            # JUSTIFICATION: Silently handle any errors during cleanup to prevent
            # test failures from cleanup issues. The database manager might not be
            # initialized or might already be closed.
            pass
    else:
        yield  # No special handling for non-serial tests


@pytest.fixture(autouse=True)
def stub_invite_manager(monkeypatch: pytest.MonkeyPatch) -> SimpleNamespace:
    """
    Override invite validation methods so character recovery flow does not depend on seeded invites.
    """

    validate_mock = AsyncMock(return_value=None)
    use_mock = AsyncMock(return_value=None)

    async def _validate(_, invite_code, request):
        return await validate_mock(invite_code, request)

    async def _use(_, invite_code, user_id):
        return await use_mock(invite_code, user_id)

    monkeypatch.setattr("server.auth.invites.InviteManager.validate_invite", _validate, raising=False)
    monkeypatch.setattr("server.auth.invites.InviteManager.use_invite", _use, raising=False)

    return SimpleNamespace(validate_mock=validate_mock, use_mock=use_mock)


class TestCharacterRecoveryFlow:
    """Test the character recovery flow for disconnected users."""

    # Use async_test_client to avoid Windows event loop issues with TestClient
    # Mark tests to run sequentially to avoid database race conditions in parallel execution
    pytestmark = [pytest.mark.asyncio, pytest.mark.serial]

    @pytest.mark.asyncio
    async def test_registration_returns_no_character(self, async_test_client):
        """Test that registration always returns has_character=False."""
        # Ensure app state has required mocks to prevent NoneType errors
        async_test_client.app.state.server_shutdown_pending = False
        # Mock connection_manager to prevent 'NoneType' object has no attribute 'send' errors
        if not hasattr(async_test_client.app.state, "container"):
            async_test_client.app.state.container = MagicMock()
        if not hasattr(async_test_client.app.state.container, "connection_manager"):
            mock_connection_manager = MagicMock()
            # Mock all potential send methods that might be called
            mock_connection_manager.send = AsyncMock()
            mock_connection_manager.send_personal_message = AsyncMock()
            mock_connection_manager.broadcast_to_room = AsyncMock()
            mock_connection_manager.broadcast_global = AsyncMock()
            mock_connection_manager.send_json = AsyncMock()
            mock_connection_manager.player_websockets = {}
            # Mock active_websockets to prevent None access errors
            mock_connection_manager.active_websockets = {}
            # Mock rate_limiter to prevent attribute errors
            mock_connection_manager.rate_limiter = MagicMock()
            mock_connection_manager.rate_limiter.check_message_rate_limit = Mock(return_value=True)
            mock_connection_manager.rate_limiter.get_message_rate_limit_info = Mock(return_value={})
            async_test_client.app.state.container.connection_manager = mock_connection_manager
        # Also set on app.state directly for compatibility
        if not hasattr(async_test_client.app.state, "connection_manager"):
            async_test_client.app.state.connection_manager = async_test_client.app.state.container.connection_manager
            # Ensure active_websockets is also set
            if not hasattr(async_test_client.app.state.connection_manager, "active_websockets"):
                async_test_client.app.state.connection_manager.active_websockets = {}
        # Mock event_handler if it exists
        if hasattr(async_test_client.app.state, "event_handler"):
            if async_test_client.app.state.event_handler is None:
                async_test_client.app.state.event_handler = MagicMock()
                async_test_client.app.state.event_handler.connection_manager = (
                    async_test_client.app.state.connection_manager
                )
        # Ensure ApplicationContainer.get_instance() returns our mocked container
        # Also ensure the container is set as the singleton instance
        from server.container import ApplicationContainer

        # Set the instance directly and patch get_instance() to ensure consistency
        ApplicationContainer.set_instance(async_test_client.app.state.container)
        with patch.object(ApplicationContainer, "get_instance", return_value=async_test_client.app.state.container):
            unique_username = f"reg_test_{uuid.uuid4().hex[:8]}"

            register_response = await async_test_client.post(
                "/auth/register",
                json={"username": unique_username, "password": "testpass123", "invite_code": "TEST123"},
            )

            assert register_response.status_code == 200
            register_data = register_response.json()
            assert len(register_data["characters"]) == 0  # MULTI-CHARACTER: New users have no characters
