"""
FastAPI application factory for MythosMUD server.

This module handles FastAPI app creation, middleware configuration,
and router registration.
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..api.admin import npc_router as admin_npc_router
from ..api.admin import subject_router as admin_subject_router
from ..api.game import game_router
from ..api.metrics import router as metrics_router
from ..api.monitoring import monitoring_router
from ..api.players import player_router
from ..api.professions import profession_router
from ..api.real_time import realtime_router
from ..api.rooms import room_router
from ..auth.endpoints import UserCreate, UserRead, UserUpdate, auth_router
from ..auth.users import auth_backend, fastapi_users
from ..command_handler_unified import router as command_router
from ..config import get_config
from ..logging.enhanced_logging_config import get_logger
from ..middleware.comprehensive_logging import ComprehensiveLoggingMiddleware
from ..middleware.error_handling_middleware import setup_error_handling
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
    config = get_config()
    cors_config = config.cors

    logger.info(
        "CORS configuration",
        allow_origins=cors_config.allow_origins,
        allow_methods=cors_config.allow_methods,
        allow_headers=cors_config.allow_headers,
        expose_headers=cors_config.expose_headers,
        allow_credentials=cors_config.allow_credentials,
        max_age=cors_config.max_age,
    )

    cors_kwargs = {
        "allow_origins": cors_config.allow_origins,
        "allow_credentials": cors_config.allow_credentials,
        "allow_methods": cors_config.allow_methods,
        "allow_headers": cors_config.allow_headers,
        "max_age": cors_config.max_age,
    }
    if cors_config.expose_headers:
        cors_kwargs["expose_headers"] = cors_config.expose_headers

    # Human Explanation: Ensure preflight requests honor the same wards used elsewhere in the realm.
    # AI Guidance: Maintain consistency with server.main when updating CORS parameters.
    app.add_middleware(CORSMiddleware, **cors_kwargs)

    # Add comprehensive logging middleware (add second to capture all requests and errors)
    app.add_middleware(ComprehensiveLoggingMiddleware)

    # Add security headers middleware (add last to ensure headers are added to all responses)
    app.add_middleware(SecurityHeadersMiddleware)

    # Setup comprehensive error handling (middleware + exception handlers)
    # Include details in development mode, hide in production
    include_details = os.getenv("ENV", "development") != "production"
    setup_error_handling(app, include_details=include_details)

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
    app.include_router(metrics_router)  # NEW: NATS metrics endpoint (CRITICAL-4)
    app.include_router(realtime_router)
    app.include_router(room_router)
    app.include_router(admin_npc_router)
    app.include_router(admin_subject_router, prefix="/api/admin")  # NATS subject management endpoints

    return app
