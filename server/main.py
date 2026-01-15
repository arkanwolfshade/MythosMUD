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
from collections.abc import Callable

from fastapi import Depends, FastAPI
from fastapi.security import HTTPBearer

from .app.factory import create_app
from .auth.users import get_current_user
from .config import get_config
from .middleware.correlation_middleware import CorrelationMiddleware
from .structured_logging.enhanced_logging_config import get_logger, setup_enhanced_logging

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
    # Lifespan (including enhanced logging/monitoring) is configured in factory

    logger.info("MythosMUD server started successfully")
    return app


def _create_get_app() -> Callable[[], FastAPI]:
    """
    Factory function that creates the get_app function with encapsulated cache.

    This closure pattern avoids global variables while maintaining lazy initialization.
    """
    app_instance: FastAPI | None = None

    def _app_getter() -> FastAPI:
        """
        Get or create the FastAPI application instance.

        This function provides lazy app creation for better testability and
        uvicorn reload compatibility. The app is created on first access.

        Returns:
            FastAPI: The configured FastAPI application instance
        """
        nonlocal app_instance
        if app_instance is None:
            app_instance = create_app()
        return app_instance

    return _app_getter


get_app = _create_get_app()


# Create the FastAPI application for uvicorn compatibility
# Note: This is created at module level for uvicorn's "server.main:app" reference
# but uses lazy initialization pattern internally
app = get_app()

# Add correlation middleware (CORS is already configured in factory)
app.add_middleware(CorrelationMiddleware, correlation_header="X-Correlation-ID")

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
