"""
MythosMUD Server - Main Application Entry Point

This module serves as the primary entry point for the MythosMUD server,
providing FastAPI application setup, WebSocket handling, and real-time
game functionality. It integrates authentication, command handling, and
persistence layers into a cohesive gaming experience.

As noted in the Pnakotic Manuscripts, the proper organization of arcane
knowledge is essential for maintaining the delicate balance between order
and chaos. This server implementation follows those ancient principles.
"""

import warnings
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

from .app.factory import create_app
from .auth.users import get_current_user
from .config import get_config
from .middleware.correlation_middleware import CorrelationMiddleware
from .monitoring.exception_tracker import get_exception_tracker
from .monitoring.monitoring_dashboard import get_monitoring_dashboard
from .monitoring.performance_monitor import get_performance_monitor
from .structured_logging.enhanced_logging_config import get_logger, log_exception_once, setup_enhanced_logging
from .structured_logging.log_aggregator import get_log_aggregator

# Suppress passlib deprecation warning about pkg_resources
# Note: We keep passlib for fastapi-users compatibility but use our own Argon2 implementation
warnings.filterwarnings("ignore", category=DeprecationWarning, module="passlib")

# Early logging setup - must happen before any logger creation
# This ensures all startup information is captured in logfiles
config = get_config()
setup_enhanced_logging(config.to_legacy_dict())

# Get logger - now created AFTER logging is set up
logger = get_logger(__name__)
logger.info("Logging setup completed", environment=config.logging.environment)  # pylint: disable=no-member  # Reason: Pydantic model fields are dynamically accessible, pylint cannot detect them statically but they exist at runtime


# ErrorLoggingMiddleware has been replaced by ComprehensiveLoggingMiddleware
# which provides the same functionality plus request/response logging and better organization


@asynccontextmanager
async def enhanced_lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:  # pylint: disable=redefined-outer-name,unused-argument  # noqa: F811  # Reason: Parameter name matches FastAPI convention, prefixed to avoid unused-argument
    """Enhanced lifespan with comprehensive monitoring and logging."""
    logger = get_logger("server.enhanced_main")  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Context-specific logger instance
    log_aggregator = None

    try:
        get_performance_monitor()
        get_exception_tracker()
        get_monitoring_dashboard()
        log_aggregator = get_log_aggregator()

        logger.info(
            "Enhanced logging and monitoring systems initialized",
            performance_monitoring=True,
            exception_tracking=True,
            log_aggregation=True,
            monitoring_dashboard=True,
        )

        yield

    except Exception as error:
        log_exception_once(
            logger,
            "error",
            "Failed to initialize enhanced systems",
            exc=error,
            lifespan_phase="startup",
            exc_info=True,
        )
        raise
    finally:
        try:
            if log_aggregator is not None:
                log_aggregator.shutdown()
                logger.info("Enhanced systems shutdown complete")
        except Exception as error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Lifespan cleanup must not fail, catch all errors
            log_exception_once(
                logger,
                "error",
                "Error during enhanced systems shutdown",
                exc=error,
                lifespan_phase="shutdown",
                exc_info=True,
            )


async def _handle_health_check() -> dict[str, Any]:
    """Handle health check endpoint logic."""
    from fastapi import HTTPException

    try:
        dashboard = get_monitoring_dashboard()
        system_health = dashboard.get_system_health()

        return {
            "status": system_health.status,
            "timestamp": system_health.timestamp.isoformat(),
            "performance_score": system_health.performance_score,
            "error_rate": system_health.error_rate,
            "warning_rate": system_health.warning_rate,
            "active_users": system_health.active_users,
        }
    except Exception as error:
        logger = get_logger("server.health")  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Context-specific logger instance
        logger.error("Health check failed", error=str(error), exc_info=True)
        raise HTTPException(status_code=503, detail="Health check failed") from error


async def _handle_get_metrics() -> dict[str, Any]:
    """Handle metrics endpoint logic."""
    from fastapi import HTTPException

    try:
        dashboard = get_monitoring_dashboard()
        result = dashboard.export_monitoring_data()
        if not isinstance(result, dict):
            raise TypeError("export_monitoring_data must return a dict")
        return result
    except Exception as error:
        logger = get_logger("server.metrics")  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Context-specific logger instance
        logger.error("Metrics retrieval failed", error=str(error), exc_info=True)
        raise HTTPException(status_code=500, detail="Metrics retrieval failed") from error


async def _handle_get_monitoring_summary() -> dict[str, Any]:
    """Handle monitoring summary endpoint logic."""
    from fastapi import HTTPException

    try:
        dashboard = get_monitoring_dashboard()
        result = dashboard.get_monitoring_summary()
        if not isinstance(result, dict):
            raise TypeError("get_monitoring_summary must return a dict")
        return result
    except Exception as error:
        logger = get_logger("server.monitoring")  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Context-specific logger instance
        logger.error("Monitoring summary failed", error=str(error), exc_info=True)
        raise HTTPException(status_code=500, detail="Monitoring summary failed") from error


async def _handle_get_alerts() -> dict[str, Any]:
    """Handle alerts endpoint logic."""
    from fastapi import HTTPException

    try:
        dashboard = get_monitoring_dashboard()
        alerts = dashboard.check_alerts()
        return {"alerts": [alert.to_dict() if hasattr(alert, "to_dict") else alert for alert in alerts]}
    except Exception as error:
        logger = get_logger("server.alerts")  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Context-specific logger instance
        logger.error("Alert retrieval failed", error=str(error), exc_info=True)
        raise HTTPException(status_code=500, detail="Alert retrieval failed") from error


async def _handle_resolve_alert(alert_id: str) -> dict[str, str]:
    """Handle resolve alert endpoint logic."""
    from fastapi import HTTPException

    try:
        dashboard = get_monitoring_dashboard()
        success = dashboard.resolve_alert(alert_id)

        if success:
            return {"message": f"Alert {alert_id} resolved"}
        raise HTTPException(status_code=404, detail="Alert not found")
    except HTTPException:
        raise
    except Exception as error:
        logger = get_logger("server.alerts")  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Context-specific logger instance
        logger.error("Alert resolution failed", error=str(error), exc_info=True)
        raise HTTPException(status_code=500, detail="Alert resolution failed") from error


def setup_monitoring_endpoints(app: FastAPI) -> None:  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Parameter name matches FastAPI convention
    """Setup monitoring and health check endpoints."""

    @app.get("/health")
    async def health_check() -> dict[str, Any]:
        """Enhanced health check endpoint."""
        return await _handle_health_check()

    @app.get("/metrics")
    async def get_metrics() -> dict[str, Any]:
        """Get system metrics."""
        return await _handle_get_metrics()

    @app.get("/monitoring/summary")
    async def get_monitoring_summary() -> dict[str, Any]:
        """Get comprehensive monitoring summary."""
        return await _handle_get_monitoring_summary()

    @app.get("/monitoring/alerts")
    async def get_alerts() -> dict[str, Any]:
        """Get system alerts."""
        return await _handle_get_alerts()

    @app.post("/monitoring/alerts/{alert_id}/resolve")
    async def resolve_alert(alert_id: str) -> dict[str, str]:
        """Resolve a system alert."""
        return await _handle_resolve_alert(alert_id)


def main() -> FastAPI:
    """Main entry point for the MythosMUD server."""
    logger.info("Starting MythosMUD server...")
    app = create_app()  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Module-level app instance for main entry point

    # Error logging is now handled by ComprehensiveLoggingMiddleware in the factory

    logger.info("MythosMUD server started successfully")
    return app


# Create the FastAPI application
app = create_app()

# Compose lifespans: run enhanced_lifespan around the app's existing lifespan
original_lifespan = app.router.lifespan_context


@asynccontextmanager
async def composed_lifespan(application: FastAPI):
    """Compose multiple lifespan contexts for application startup/shutdown.

    This function combines the enhanced logging/monitoring lifespan with
    the factory/app lifespan (DB init, persistence binding, etc.).

    Args:
        application: The FastAPI application instance

    Yields:
        None: Control is yielded to the application
    """
    # Outer: enhanced logging/monitoring
    async with enhanced_lifespan(application):
        # Inner: factory/app lifespan (DB init, persistence binding, etc.)
        async with original_lifespan(application):
            yield


app.router.lifespan_context = composed_lifespan

app.add_middleware(CorrelationMiddleware, correlation_header="X-Correlation-ID")

# pylint: disable=no-member  # Reason: Pydantic model fields are dynamically accessible, pylint cannot detect them statically but they exist at runtime
cors_kwargs = {
    "allow_origins": config.cors.allow_origins,
    "allow_credentials": config.cors.allow_credentials,
    "allow_methods": config.cors.allow_methods,
    "allow_headers": config.cors.allow_headers,
    "max_age": config.cors.max_age,
}

if config.cors.expose_headers:
    cors_kwargs["expose_headers"] = config.cors.expose_headers

# The trusted origins list keeps our gateways as secure as the wards at the Arkham Library.
# CORSMiddleware uses **kwargs which mypy can't validate against strict Starlette signatures
app.add_middleware(CORSMiddleware, **cors_kwargs)  # type: ignore[arg-type]  # Reason: CORSMiddleware accepts **kwargs which mypy cannot validate against strict Starlette middleware signatures, but runtime validation ensures compatibility

setup_monitoring_endpoints(app)

# Security
security = HTTPBearer()


# Root endpoint
@app.get("/")
async def read_root() -> dict[str, str]:
    """Root endpoint providing basic server information."""
    return {"message": "Welcome to MythosMUD!"}


# Test endpoint for JWT validation
@app.get("/test-auth")
async def test_auth(current_user: dict = Depends(get_current_user)) -> dict[str, str]:
    """Test endpoint to verify JWT authentication is working."""
    if current_user:
        return {"message": "Authentication successful", "user": str(current_user)}
    return {"message": "No user found"}


if __name__ == "__main__":
    import uvicorn

    config = get_config()
    uvicorn.run(
        "server.main:app",  # Use the correct module path from project root
        host=config.server.host,
        port=config.server.port,  # pylint: disable=no-member  # Reason: Pydantic model fields are dynamically accessible, pylint cannot detect them statically but they exist at runtime
        reload=False,  # Hot reloading disabled due to client compatibility issues
        # Use our StructLog system for all logging
        access_log=True,
        use_colors=False,  # Disable colors for structured logging
    )
