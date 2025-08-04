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

from fastapi.security import HTTPBearer
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request as StarletteRequest

from .app.factory import create_app
from .logging_config import get_logger

# Suppress passlib deprecation warning about pkg_resources
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
            logger.error(f"Unhandled exception in {request.url.path}: {str(e)}", exc_info=True)
            # Re-raise the exception to maintain the error handling chain
            raise e


def main():
    """Main entry point for the MythosMUD server."""
    logger.info("Starting MythosMUD server...")
    app = create_app()

    # Add error logging middleware
    app.add_middleware(ErrorLoggingMiddleware)

    logger.info("MythosMUD server started successfully")
    return app


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


if __name__ == "__main__":
    import uvicorn

    from .config_loader import get_config

    config = get_config()
    uvicorn.run(
        "main:app",
        host=config["host"],
        port=config["port"],
        reload=True,
        log_config=None,  # Disable uvicorn's default logging
    )
