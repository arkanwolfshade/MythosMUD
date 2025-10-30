"""
Enhanced main.py with comprehensive logging, monitoring, and error tracking.

This module provides the main entry point for the MythosMUD server with
enhanced logging, monitoring, and error tracking capabilities.

As noted in the Pnakotic Manuscripts, proper initialization of our systems
is essential for maintaining their stability and observability.
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .app.factory import create_app

# Import existing server components
from .config import get_config

# Import enhanced logging and monitoring systems
from .logging.enhanced_logging_config import get_logger, setup_enhanced_logging
from .logging.log_aggregator import get_log_aggregator
from .middleware.correlation_middleware import CorrelationMiddleware
from .monitoring.exception_tracker import get_exception_tracker
from .monitoring.monitoring_dashboard import get_monitoring_dashboard
from .monitoring.performance_monitor import get_performance_monitor


# Enhanced lifespan with monitoring
@asynccontextmanager
async def enhanced_lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Enhanced lifespan with comprehensive monitoring and logging."""
    logger = get_logger("server.enhanced_main")

    try:
        # Initialize enhanced logging
        config = get_config()
        setup_enhanced_logging(config.dict())

        # Initialize monitoring systems
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

        # Start the application
        yield

    except Exception as e:
        logger.error("Failed to initialize enhanced systems", error=str(e), exc_info=True)
        raise
    finally:
        # Cleanup
        try:
            log_aggregator.shutdown()
            logger.info("Enhanced systems shutdown complete")
        except Exception as e:
            logger.error("Error during enhanced systems shutdown", error=str(e), exc_info=True)


def create_enhanced_app() -> FastAPI:
    """
    Create FastAPI application with enhanced logging and monitoring.

    Returns:
        Configured FastAPI application
    """
    # Get configuration
    config = get_config()

    # Create base application
    app = create_app()

    # Add enhanced lifespan
    app.router.lifespan_context = enhanced_lifespan

    # Add correlation middleware
    app.add_middleware(CorrelationMiddleware, correlation_header="X-Correlation-ID")

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors.allow_origins,
        allow_credentials=config.cors.allow_credentials,
        allow_methods=config.cors.allow_methods,
        allow_headers=config.cors.allow_headers,
    )

    # Add monitoring endpoints
    setup_monitoring_endpoints(app)

    return app


def setup_monitoring_endpoints(app: FastAPI) -> None:
    """Setup monitoring and health check endpoints."""
    from fastapi import HTTPException

    @app.get("/health")  # type: ignore[misc]
    async def health_check() -> dict[str, Any]:
        """Enhanced health check endpoint."""
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
        except Exception as e:
            logger = get_logger("server.health")
            logger.error("Health check failed", error=str(e), exc_info=True)
            raise HTTPException(status_code=503, detail="Health check failed") from e

    @app.get("/metrics")  # type: ignore[misc]
    async def get_metrics() -> dict[str, Any]:
        """Get system metrics."""
        try:
            dashboard = get_monitoring_dashboard()
            result = dashboard.export_monitoring_data()
            assert isinstance(result, dict)
            return result
        except Exception as e:
            logger = get_logger("server.metrics")
            logger.error("Metrics retrieval failed", error=str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Metrics retrieval failed") from e

    @app.get("/monitoring/summary")  # type: ignore[misc]
    async def get_monitoring_summary() -> dict[str, Any]:
        """Get comprehensive monitoring summary."""
        try:
            dashboard = get_monitoring_dashboard()
            result = dashboard.get_monitoring_summary()
            assert isinstance(result, dict)
            return result
        except Exception as e:
            logger = get_logger("server.monitoring")
            logger.error("Monitoring summary failed", error=str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Monitoring summary failed") from e

    @app.get("/monitoring/alerts")  # type: ignore[misc]
    async def get_alerts() -> dict[str, Any]:
        """Get system alerts."""
        try:
            dashboard = get_monitoring_dashboard()
            result = dashboard.check_alerts()
            assert isinstance(result, dict)
            return result
        except Exception as e:
            logger = get_logger("server.alerts")
            logger.error("Alert retrieval failed", error=str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Alert retrieval failed") from e

    @app.post("/monitoring/alerts/{alert_id}/resolve")  # type: ignore[misc]
    async def resolve_alert(alert_id: str) -> dict[str, str]:
        """Resolve a system alert."""
        try:
            dashboard = get_monitoring_dashboard()
            success = dashboard.resolve_alert(alert_id)

            if success:
                return {"message": f"Alert {alert_id} resolved"}
            else:
                raise HTTPException(status_code=404, detail="Alert not found")
        except HTTPException:
            raise
        except Exception as e:
            logger = get_logger("server.alerts")
            logger.error("Alert resolution failed", error=str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Alert resolution failed") from e


def main() -> None:
    """Main entry point for enhanced server."""
    import uvicorn

    # Get configuration
    config = get_config()

    # Create enhanced application
    app = create_enhanced_app()

    # Configure uvicorn
    uvicorn_config = {
        "app": app,
        "host": config.server.host,
        "port": config.server.port,
        "log_level": config.logging.level.lower(),
        "access_log": True,
        "use_colors": True,
    }

    # Start server
    logger = get_logger("server.enhanced_main")
    logger.info(
        "Starting enhanced MythosMUD server",
        host=config.server.host,
        port=config.server.port,
        log_level=config.logging.level,
        enhanced_logging=True,
        monitoring=True,
        correlation_ids=True,
    )

    uvicorn.run(**uvicorn_config)


if __name__ == "__main__":
    main()
