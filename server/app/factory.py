"""
FastAPI application factory for MythosMUD server.

This module handles FastAPI app creation, middleware configuration,
and router registration.
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..api.admin import npc_router as admin_npc_router
from ..api.game import game_router
from ..api.monitoring import router as monitoring_router
from ..api.players import player_router
from ..api.professions import profession_router
from ..api.real_time import realtime_router
from ..api.rooms import room_router
from ..auth.endpoints import UserCreate, UserRead, UserUpdate, auth_router
from ..auth.users import auth_backend, fastapi_users
from ..command_handler_unified import router as command_router
from ..error_handlers import register_error_handlers
from ..logging_config import get_logger
from ..middleware.comprehensive_logging import ComprehensiveLoggingMiddleware
from ..middleware.security_headers import SecurityHeadersMiddleware
from .lifespan import lifespan

logger = get_logger(__name__)


# AccessLoggingMiddleware has been replaced by ComprehensiveLoggingMiddleware
# which provides the same functionality plus error logging and better organization


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    This function sets up the FastAPI app with all necessary middleware,
    routers, and configuration for the MythosMUD server.

    Returns:
        FastAPI: The configured FastAPI application instance
    """
    app = FastAPI(
        title="MythosMUD API",
        description=("A Cthulhu Mythos-themed MUD game API with real-time communication"),
        version="0.1.0",
        lifespan=lifespan,
    )

    # Add CORS middleware first (it handles preflight requests)
    allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")
    allowed_methods = os.getenv("ALLOWED_METHODS", "GET,POST,PUT,DELETE,OPTIONS").split(",")
    allowed_headers = os.getenv("ALLOWED_HEADERS", "Content-Type,Authorization,X-Requested-With").split(",")

    logger.info(
        "CORS configuration",
        allowed_origins=allowed_origins,
        allowed_methods=allowed_methods,
        allowed_headers=allowed_headers,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=allowed_methods,
        allow_headers=allowed_headers,
    )

    # Add comprehensive logging middleware (add second to capture all requests and errors)
    app.add_middleware(ComprehensiveLoggingMiddleware)

    # Add security headers middleware (add last to ensure headers are added to all responses)
    app.add_middleware(SecurityHeadersMiddleware)

    # Register error handlers
    register_error_handlers(app)

    # Include routers
    app.include_router(auth_router)

    # Include FastAPI Users routers for authentication
    app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
    app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
    app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])

    app.include_router(command_router)
    app.include_router(player_router)
    app.include_router(profession_router)
    app.include_router(game_router)
    app.include_router(monitoring_router)
    app.include_router(realtime_router)
    app.include_router(room_router)
    app.include_router(admin_npc_router)

    return app
