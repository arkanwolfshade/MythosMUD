"""
Tests for Metrics API endpoints.

This module tests the metrics API for monitoring NATS message delivery,
circuit breaker state, and dead letter queue status.

AI Agent: Tests for admin-only metrics endpoints covering authentication,
         authorization, and basic metric retrieval with mocked dependencies.
"""

# pylint: disable=redefined-outer-name,protected-access
# Justification: pytest fixtures redefine names, protected access needed for testing internals

from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException, status


# Import the module under test
# Note: We avoid importing from server.main to prevent bcrypt re-initialization
@pytest.fixture
def metrics_module():
    """Lazily import metrics module to avoid bcrypt issues."""
    from server.api import metrics

    return metrics


@pytest.fixture
def mock_admin_user():
    """Provide mock admin user."""
    user = Mock()
    user.username = "admin_user"
    user.is_admin = True
    user.is_superuser = False
    user.player_id = "admin-123"
    return user


@pytest.fixture
def mock_regular_user():
    """Provide mock regular user."""
    user = Mock()
    user.username = "regular_user"
    user.is_admin = False
    user.is_superuser = False
    user.player_id = "user-123"
    return user


@pytest.fixture
def mock_superuser():
    """Provide mock superuser."""
    user = Mock()
    user.username = "superuser"
    user.is_admin = False
    user.is_superuser = True
    user.player_id = "super-123"
    return user


class TestVerifyAdminAccess:
    """Test admin access verification."""

    def test_verify_admin_access_with_no_user_raises_401(self, metrics_module):
        """Test verification fails when user is None."""
        with pytest.raises(HTTPException) as exc_info:
            metrics_module.verify_admin_access(current_user=None)

        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
        assert "Authentication required" in exc_info.value.detail

    def test_verify_admin_access_with_regular_user_raises_403(self, metrics_module, mock_regular_user):
        """Test verification fails when user is not admin."""
        with pytest.raises(HTTPException) as exc_info:
            metrics_module.verify_admin_access(current_user=mock_regular_user)

        assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN
        assert "Admin access required" in exc_info.value.detail

    def test_verify_admin_access_with_admin_succeeds(self, metrics_module, mock_admin_user):
        """Test verification succeeds for admin user."""
        result = metrics_module.verify_admin_access(current_user=mock_admin_user)

        assert result == mock_admin_user

    def test_verify_admin_access_with_superuser_succeeds(self, metrics_module, mock_superuser):
        """Test verification succeeds for superuser."""
        result = metrics_module.verify_admin_access(current_user=mock_superuser)

        assert result == mock_superuser


class TestGetMetrics:
    """Test comprehensive metrics retrieval."""

    @pytest.mark.asyncio
    @patch("server.api.metrics.metrics_collector")
    @patch("server.services.nats_service.nats_service")
    @patch("server.main.app")
    async def test_get_metrics_without_nats_handler(
        self, mock_app, mock_nats_service, mock_metrics_collector, metrics_module, mock_admin_user
    ):
        """Test metrics retrieval when NATS handler not available."""
        mock_metrics_collector.get_metrics.return_value = {"messages_sent": 100, "circuit_breaker": {}}
        mock_nats_service.is_connected.return_value = True

        mock_app.state.container.nats_message_handler = None

        result = await metrics_module.get_metrics(current_user=mock_admin_user)

        assert isinstance(result, dict)
        assert result["messages_sent"] == 100
        mock_metrics_collector.get_metrics.assert_called_once()


class TestGetMetricsSummary:
    """Test metrics summary retrieval."""

    @pytest.mark.asyncio
    @patch("server.api.metrics.metrics_collector")
    @patch("server.services.nats_service.nats_service")
    @patch("server.main.app")
    async def test_get_metrics_summary_without_nats_handler(
        self, mock_app, mock_nats_service, mock_metrics_collector, metrics_module, mock_admin_user
    ):
        """Test summary retrieval when NATS handler not available."""
        mock_metrics_collector.get_summary.return_value = {"health": "ok", "uptime": 3600}
        mock_nats_service.is_connected.return_value = True

        mock_app.state.container.nats_message_handler = None

        result = await metrics_module.get_metrics_summary(current_user=mock_admin_user)

        assert isinstance(result, dict)
        assert result["health"] == "ok"
        assert result["uptime"] == 3600


class TestResetMetrics:
    """Test metrics reset endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.metrics.metrics_collector")
    async def test_reset_metrics_success(self, mock_metrics_collector, metrics_module, mock_admin_user):
        """Test successful metrics reset."""
        result = await metrics_module.reset_metrics(current_user=mock_admin_user)

        assert result["status"] == "success"
        assert "reset" in result["message"].lower()
        mock_metrics_collector.reset_metrics.assert_called_once()


class TestGetDLQMessages:
    """Test DLQ message retrieval."""

    @pytest.mark.asyncio
    @patch("server.main.app")
    async def test_get_dlq_messages_when_handler_not_available(self, mock_app, metrics_module, mock_admin_user):
        """Test DLQ endpoint returns empty when handler not available."""
        mock_app.state.container.nats_message_handler = None

        result = await metrics_module.get_dlq_messages(limit=100, current_user=mock_admin_user)

        assert result["messages"] == []
        assert result["count"] == 0


class TestResetCircuitBreaker:
    """Test circuit breaker reset endpoint."""

    @pytest.mark.asyncio
    @patch("server.main.app")
    async def test_reset_circuit_breaker_when_handler_not_available(self, mock_app, metrics_module, mock_admin_user):
        """Test circuit breaker reset fails when handler not available."""
        mock_app.state.container.nats_message_handler = None

        with pytest.raises(HTTPException) as exc_info:
            await metrics_module.reset_circuit_breaker(current_user=mock_admin_user)

        assert exc_info.value.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert "not available" in exc_info.value.detail.lower()
