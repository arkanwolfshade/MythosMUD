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


# Handler functions moved to server/api/monitoring.py
# These are kept for backward compatibility but are no longer used


# Monitoring endpoints have been moved to server/api/monitoring.py
# This function is kept for backward compatibility but is now a no-op
def setup_monitoring_endpoints(app: FastAPI) -> None:  # pylint: disable=redefined-outer-name  # noqa: F811  # Reason: Parameter name matches FastAPI convention, kept for backward compatibility
    """Setup monitoring and health check endpoints.

    NOTE: Monitoring endpoints have been moved to server/api/monitoring.py
    and are now registered via the monitoring_router. This function registers
    the routers for testing purposes.
    """
    from server.api.monitoring import monitoring_router, system_monitoring_router

    app.include_router(monitoring_router)
    app.include_router(system_monitoring_router)


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
