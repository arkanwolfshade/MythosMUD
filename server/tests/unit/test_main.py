"""
Unit tests for main.py monitoring endpoints and lifespan functions.

Tests monitoring endpoints and enhanced lifespan functionality.
"""

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any
from unittest.mock import MagicMock, Mock, patch

import pytest
from fastapi import FastAPI

from server.exceptions import LoggedHTTPException
from server.main import enhanced_lifespan


class TestEnhancedLifespan:
    """Test enhanced_lifespan() context manager."""

    @pytest.mark.asyncio
    async def test_enhanced_lifespan_success(self):
        """Test enhanced_lifespan() initializes monitoring successfully."""
        app = FastAPI()
        async with enhanced_lifespan(app):
            # Should not raise
            pass

    @pytest.mark.asyncio
    async def test_enhanced_lifespan_shutdown(self):
        """Test enhanced_lifespan() shuts down properly."""
        app = FastAPI()
        async with enhanced_lifespan(app):
            pass
        # Shutdown should complete without errors

    @pytest.mark.asyncio
    async def test_enhanced_lifespan_initialization_failure(self):
        """Test enhanced_lifespan() handles initialization failure."""
        app = FastAPI()

        with patch("server.main.get_performance_monitor", side_effect=RuntimeError("Init error")):
            with pytest.raises(RuntimeError, match="Init error"):
                async with enhanced_lifespan(app):
                    pass


class TestMonitoringEndpoints:
    """Test monitoring endpoint functions."""

    @pytest.fixture
    def mock_app(self):
        """Create a mock FastAPI app."""
        app = FastAPI()
        return app

    @pytest.fixture
    def mock_dashboard(self):
        """Create a mock monitoring dashboard."""
        dashboard = MagicMock()
        system_health = MagicMock()
        system_health.status = "healthy"
        system_health.timestamp = datetime.now(UTC)
        system_health.performance_score = 0.95
        system_health.error_rate = 0.01
        system_health.warning_rate = 0.02
        system_health.active_users = 10
        dashboard.get_system_health = Mock(return_value=system_health)
        dashboard.export_monitoring_data = Mock(return_value={"metrics": "data"})

        @dataclass
        class MockMonitoringSummary:
            timestamp: datetime
            system_health: Any
            performance_stats: dict
            exception_stats: Any
            log_stats: Any
            alerts: list
            recommendations: list

        dashboard.get_monitoring_summary = Mock(
            return_value=MockMonitoringSummary(
                timestamp=datetime.now(UTC),
                system_health=system_health,
                performance_stats={},
                exception_stats=MagicMock(),
                log_stats=MagicMock(),
                alerts=[],
                recommendations=[],
            )
        )
        dashboard.check_alerts = Mock(return_value=[])
        dashboard.resolve_alert = Mock(return_value=True)
        return dashboard

    @pytest.mark.asyncio
    async def test_health_check_success(self, mock_app, mock_dashboard):
        """Test health check endpoint returns system health."""
        from fastapi import Request

        from server.api.monitoring import get_system_health  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", return_value=mock_dashboard):
            result = await get_system_health(mock_request)
            assert result.status == "healthy"
            assert result.timestamp is not None
            assert result.performance_score == 0.95

    @pytest.mark.asyncio
    async def test_health_check_failure(self, mock_app):
        """Test health check endpoint handles errors."""
        from fastapi import Request

        from server.api.monitoring import get_system_health  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            # Should raise LoggedHTTPException
            with pytest.raises(LoggedHTTPException) as exc_info:
                await get_system_health(mock_request)

            assert exc_info.value.status_code == 503

    @pytest.mark.asyncio
    async def test_get_metrics_success(self, mock_app, mock_dashboard):
        """Test metrics endpoint returns monitoring data."""
        from fastapi import Request

        from server.api.monitoring import get_system_metrics  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", return_value=mock_dashboard):
            result = await get_system_metrics(mock_request)
            assert isinstance(result, dict) or hasattr(result, "model_dump")
            result_dict = result.model_dump() if hasattr(result, "model_dump") else result
            assert "metrics" in result_dict or result_dict == {"metrics": "data"}

    @pytest.mark.asyncio
    async def test_get_metrics_failure(self, mock_app):
        """Test metrics endpoint handles errors."""
        from fastapi import Request

        from server.api.monitoring import get_system_metrics  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await get_system_metrics(mock_request)

            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_get_monitoring_summary_success(self, mock_app, mock_dashboard):
        """Test monitoring summary endpoint returns summary data."""
        from fastapi import Request

        from server.api.monitoring import get_system_monitoring_summary  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", return_value=mock_dashboard):
            result = await get_system_monitoring_summary(mock_request)
            assert isinstance(result, dict) or hasattr(result, "model_dump")

    @pytest.mark.asyncio
    async def test_get_monitoring_summary_failure(self, mock_app):
        """Test monitoring summary endpoint handles errors."""
        from fastapi import Request

        from server.api.monitoring import get_system_monitoring_summary  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await get_system_monitoring_summary(mock_request)

            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_get_alerts_success(self, mock_app, mock_dashboard):
        """Test alerts endpoint returns alert data."""
        from fastapi import Request

        from server.api.monitoring import get_system_monitoring_alerts  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", return_value=mock_dashboard):
            result = await get_system_monitoring_alerts(mock_request)
            assert isinstance(result, dict) or hasattr(result, "model_dump")
            result_dict = result.model_dump() if hasattr(result, "model_dump") else result
            assert "alerts" in result_dict

    @pytest.mark.asyncio
    async def test_get_alerts_failure(self, mock_app):
        """Test alerts endpoint handles errors."""
        from fastapi import Request

        from server.api.monitoring import get_system_monitoring_alerts  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await get_system_monitoring_alerts(mock_request)

            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_resolve_alert_success(self, mock_app, mock_dashboard):
        """Test resolve alert endpoint succeeds."""
        from fastapi import Request

        from server.api.monitoring import resolve_system_alert  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", return_value=mock_dashboard):
            result = await resolve_system_alert("alert_123", mock_request)
            assert isinstance(result, dict) or hasattr(result, "model_dump")
            result_dict = result.model_dump() if hasattr(result, "model_dump") else result
            assert "message" in result_dict

    @pytest.mark.asyncio
    async def test_resolve_alert_not_found(self, mock_app, mock_dashboard):
        """Test resolve alert endpoint returns 404 when alert not found."""
        from fastapi import Request

        from server.api.monitoring import resolve_system_alert  # noqa: E402

        mock_request = MagicMock(spec=Request)
        mock_dashboard.resolve_alert = Mock(return_value=False)

        with patch("server.api.monitoring.get_monitoring_dashboard", return_value=mock_dashboard):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await resolve_system_alert("nonexistent_alert", mock_request)

            assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_resolve_alert_failure(self, mock_app):
        """Test resolve alert endpoint handles errors."""
        from fastapi import Request

        from server.api.monitoring import resolve_system_alert  # noqa: E402

        mock_request = MagicMock(spec=Request)

        with patch("server.api.monitoring.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await resolve_system_alert("alert_123", mock_request)

            assert exc_info.value.status_code == 500
