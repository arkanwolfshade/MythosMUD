"""
Unit tests for main.py monitoring endpoints and lifespan functions.

Tests monitoring endpoints and enhanced lifespan functionality.
"""

from unittest.mock import MagicMock, Mock, patch

import pytest
from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from server.main import enhanced_lifespan, setup_monitoring_endpoints


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
        system_health.timestamp.isoformat = Mock(return_value="2023-01-01T00:00:00")
        system_health.performance_score = 0.95
        system_health.error_rate = 0.01
        system_health.warning_rate = 0.02
        system_health.active_users = 10
        dashboard.get_system_health = Mock(return_value=system_health)
        dashboard.export_monitoring_data = Mock(return_value={"metrics": "data"})
        dashboard.get_monitoring_summary = Mock(return_value={"summary": "data"})
        dashboard.check_alerts = Mock(return_value=[])
        dashboard.resolve_alert = Mock(return_value=True)
        return dashboard

    @pytest.mark.asyncio
    async def test_health_check_success(self, mock_app, mock_dashboard):
        """Test health check endpoint returns system health."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", return_value=mock_dashboard):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/health":
                    route = r
                    break

            assert route is not None
            # Call the endpoint handler
            result = await route.endpoint()
            assert result["status"] == "healthy"
            assert "timestamp" in result
            assert result["performance_score"] == 0.95

    @pytest.mark.asyncio
    async def test_health_check_failure(self, mock_app):
        """Test health check endpoint handles errors."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/health":
                    route = r
                    break

            assert route is not None
            # Should raise HTTPException
            with pytest.raises(HTTPException) as exc_info:
                await route.endpoint()

            assert exc_info.value.status_code == 503

    @pytest.mark.asyncio
    async def test_get_metrics_success(self, mock_app, mock_dashboard):
        """Test metrics endpoint returns monitoring data."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", return_value=mock_dashboard):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/metrics":
                    route = r
                    break

            assert route is not None
            result = await route.endpoint()
            assert isinstance(result, dict)
            assert "metrics" in result or result == {"metrics": "data"}

    @pytest.mark.asyncio
    async def test_get_metrics_failure(self, mock_app):
        """Test metrics endpoint handles errors."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/metrics":
                    route = r
                    break

            assert route is not None
            with pytest.raises(HTTPException) as exc_info:
                await route.endpoint()

            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_get_monitoring_summary_success(self, mock_app, mock_dashboard):
        """Test monitoring summary endpoint returns summary data."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", return_value=mock_dashboard):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/monitoring/summary":
                    route = r
                    break

            assert route is not None
            result = await route.endpoint()
            assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_get_monitoring_summary_failure(self, mock_app):
        """Test monitoring summary endpoint handles errors."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/monitoring/summary":
                    route = r
                    break

            assert route is not None
            with pytest.raises(HTTPException) as exc_info:
                await route.endpoint()

            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_get_alerts_success(self, mock_app, mock_dashboard):
        """Test alerts endpoint returns alert data."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", return_value=mock_dashboard):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/monitoring/alerts":
                    route = r
                    break

            assert route is not None
            result = await route.endpoint()
            assert isinstance(result, dict)
            assert "alerts" in result

    @pytest.mark.asyncio
    async def test_get_alerts_failure(self, mock_app):
        """Test alerts endpoint handles errors."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/monitoring/alerts":
                    route = r
                    break

            assert route is not None
            with pytest.raises(HTTPException) as exc_info:
                await route.endpoint()

            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_resolve_alert_success(self, mock_app, mock_dashboard):
        """Test resolve alert endpoint succeeds."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", return_value=mock_dashboard):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/monitoring/alerts/{alert_id}/resolve":
                    route = r
                    break

            assert route is not None
            result = await route.endpoint("alert_123")
            assert isinstance(result, dict)
            assert "message" in result

    @pytest.mark.asyncio
    async def test_resolve_alert_not_found(self, mock_app, mock_dashboard):
        """Test resolve alert endpoint returns 404 when alert not found."""
        mock_dashboard.resolve_alert = Mock(return_value=False)
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", return_value=mock_dashboard):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/monitoring/alerts/{alert_id}/resolve":
                    route = r
                    break

            assert route is not None
            with pytest.raises(HTTPException) as exc_info:
                await route.endpoint("nonexistent_alert")

            assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_resolve_alert_failure(self, mock_app):
        """Test resolve alert endpoint handles errors."""
        setup_monitoring_endpoints(mock_app)

        with patch("server.main.get_monitoring_dashboard", side_effect=Exception("Dashboard error")):
            # Get the endpoint handler
            route = None
            for r in mock_app.routes:
                if hasattr(r, "path") and r.path == "/monitoring/alerts/{alert_id}/resolve":
                    route = r
                    break

            assert route is not None
            with pytest.raises(HTTPException) as exc_info:
                await route.endpoint("alert_123")

            assert exc_info.value.status_code == 500
