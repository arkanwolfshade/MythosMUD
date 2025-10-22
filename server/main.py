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

from fastapi import Depends
from fastapi.security import HTTPBearer

from .app.factory import create_app
from .auth.users import get_current_user
from .config import get_config
from .logging.enhanced_logging_config import get_logger, setup_enhanced_logging

# Suppress passlib deprecation warning about pkg_resources
# Note: We keep passlib for fastapi-users compatibility but use our own Argon2 implementation
warnings.filterwarnings("ignore", category=DeprecationWarning, module="passlib")

# Get logger
logger = get_logger(__name__)


# ErrorLoggingMiddleware has been replaced by ComprehensiveLoggingMiddleware
# which provides the same functionality plus request/response logging and better organization


def main():
    """Main entry point for the MythosMUD server."""
    # Set up logging based on configuration
    config = get_config()
    setup_enhanced_logging(config.to_legacy_dict())

    logger.info("Starting MythosMUD server...")
    app = create_app()

    # Error logging is now handled by ComprehensiveLoggingMiddleware in the factory

    logger.info("MythosMUD server started successfully")
    return app


# Set up logging when module is imported
config = get_config()
logger.info("Setting up logging with config", config=config.to_legacy_dict())
setup_enhanced_logging(config.to_legacy_dict())
logger.info("Logging setup completed")

# Create the FastAPI application
app = create_app()

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
        host=config.server.host,
        port=config.server.port,
        reload=True,
        reload_excludes=["server/tests/*"],  # Exclude test directory from hot reloading
        # Use our StructLog system for all logging
        access_log=True,
        use_colors=False,  # Disable colors for structured logging
    )
