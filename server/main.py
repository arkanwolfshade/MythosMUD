"""
MythosMUD Server - Main Application Entry Point

This module serves as the primary entry point for the MythosMUD server,
providing FastAPI application setup, WebSocket handling, and real-time
game functionality. It integrates authentication, command handling, and
persistence layers into a cohesive gaming experience.

As noted in the Pnakotic Manuscripts, the proper organization of arcane
knowledge is essential for maintaining the delicate balance between order
and chaos in our digital realm.
"""

import warnings

from fastapi import Depends
from fastapi.security import HTTPBearer
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request as StarletteRequest

from .app.factory import create_app
from .auth.users import get_current_user
from .config_loader import get_config
from .logging_config import get_logger, setup_logging

# Suppress passlib deprecation warning about pkg_resources
# Note: We keep passlib for fastapi-users compatibility but use our own Argon2 implementation
warnings.filterwarnings("ignore", category=DeprecationWarning, module="passlib")

# Get logger
logger = get_logger(__name__)


class ErrorLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log all errors and exceptions."""

    async def dispatch(self, request: StarletteRequest, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logger.error("Unhandled exception in request", path=request.url.path, error=str(e), exc_info=True)
            # Re-raise the exception to maintain the error handling chain
            raise e


def main():
    """Main entry point for the MythosMUD server."""
    from .config_loader import get_config

    # Set up logging based on configuration
    config = get_config()
    setup_logging(config)

    logger.info("Starting MythosMUD server...")
    app = create_app()

    # Add error logging middleware
    app.add_middleware(ErrorLoggingMiddleware)

    logger.info("MythosMUD server started successfully")
    return app


# Set up logging when module is imported
config = get_config()
logger.info("Setting up logging with config", config=config)
setup_logging(config)
logger.info("Logging setup completed")

# Create the FastAPI application
app = create_app()

# Add error logging middleware
app.add_middleware(ErrorLoggingMiddleware)

# Security
security = HTTPBearer()


# Root endpoint
@app.get("/")
async def read_root():
    """Root endpoint providing basic server information."""
    return {"message": "Welcome to MythosMUD!"}


# Test endpoint for JWT validation
@app.get("/test-auth")
async def test_auth(current_user: dict = Depends(get_current_user)):
    """Test endpoint to verify JWT authentication is working."""
    if current_user:
        return {"message": "Authentication successful", "user": current_user}
    else:
        return {"message": "No user found"}


if __name__ == "__main__":
    import uvicorn

    config = get_config()
    uvicorn.run(
        "server.main:app",  # Use the correct module path from project root
        host=config["host"],
        port=config["port"],
        reload=True,
        # Use our StructLog system for all logging
        access_log=True,
        use_colors=False,  # Disable colors for structured logging
    )
