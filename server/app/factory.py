"""
FastAPI application factory for MythosMUD server.

This module handles FastAPI app creation, middleware configuration,
and router registration.
"""

import json
import os
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..api.admin import npc_router as admin_npc_router
from ..api.admin import subject_router as admin_subject_router
from ..api.containers import container_router
from ..api.game import game_router
from ..api.maps import map_router
from ..api.metrics import router as metrics_router
from ..api.monitoring import monitoring_router, system_monitoring_router
from ..api.players import player_router
from ..api.professions import profession_router
from ..api.real_time import realtime_router
from ..api.rooms import room_router
from ..auth.endpoints import UserCreate, UserRead, UserUpdate, auth_router
from ..auth.users import auth_backend, fastapi_users
from ..command_handler_unified import router as command_router
from ..config import get_config

# ARCHITECTURE FIX Phase 2.1: Removed AllowedCORSMiddleware import (duplicate functionality)
# from ..middleware.allowed_cors import AllowedCORSMiddleware
from ..middleware.comprehensive_logging import ComprehensiveLoggingMiddleware
from ..middleware.error_handling_middleware import setup_error_handling
from ..middleware.security_headers import SecurityHeadersMiddleware
from ..structured_logging.enhanced_logging_config import get_logger
from .lifespan import lifespan

logger = get_logger(__name__)


# AccessLoggingMiddleware has been replaced by ComprehensiveLoggingMiddleware
# which provides the same functionality plus error logging and better organization


def create_app() -> FastAPI:  # pylint: disable=too-many-locals,too-many-statements  # Reason: Application factory requires many intermediate variables for service configuration. Application factory legitimately requires many statements for comprehensive app setup.
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

    # Resolve CORS configuration (prefer full AppConfig, fallback to environment-only if unavailable)
    try:
        config = get_config()
        cors_cfg: Any = config.cors
        allowed_origins_list = list(getattr(cors_cfg, "allow_origins", []))
        allowed_methods_list = [str(m).upper() for m in getattr(cors_cfg, "allow_methods", [])]
        allowed_headers_list = [str(h) for h in getattr(cors_cfg, "allow_headers", [])]
        expose_headers_list = list(getattr(cors_cfg, "expose_headers", []))
        allow_credentials_bool = bool(getattr(cors_cfg, "allow_credentials", True))
        max_age_int = int(getattr(cors_cfg, "max_age", 600))
    except Exception:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: CORS config errors unpredictable, must fallback to environment
        # Minimal fallback sourced only from environment
        allowed_origins_list = [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ]
        allowed_methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
        allowed_headers_list = [
            "Content-Type",
            "Authorization",
            "X-Requested-With",
            "Accept",
            "Accept-Language",
        ]
        expose_headers_list = []
        allow_credentials_bool = True
        max_age_int = 600

    logger.info(
        "CORS configuration",
        allow_origins=allowed_origins_list,
        allow_methods=allowed_methods_list,
        allow_headers=allowed_headers_list,
        expose_headers=expose_headers_list,
        allow_credentials=allow_credentials_bool,
        max_age=max_age_int,
    )

    # ARCHITECTURE FIX Phase 2.1: Simplified CORS configuration
    # Environment variables take precedence over config file
    # Precedence: ENV > CONFIG > DEFAULTS
    final_origins = allowed_origins_list
    final_methods = allowed_methods_list
    final_headers = allowed_headers_list

    # Check for environment variable overrides
    env_origins = os.getenv("ALLOWED_ORIGINS") or os.getenv("CORS_ALLOW_ORIGINS") or os.getenv("CORS_ORIGINS")
    if env_origins:
        candidate = env_origins.strip()
        if candidate.startswith("["):
            try:
                parsed = json.loads(candidate)
                final_origins = [str(o).strip() for o in parsed if str(o).strip()]
            except json.JSONDecodeError:
                final_origins = [o.strip().strip('"').strip("'") for o in candidate.strip("[]").split(",") if o.strip()]
        else:
            final_origins = [o.strip() for o in candidate.split(",") if o.strip()]

    env_methods = os.getenv("ALLOWED_METHODS") or os.getenv("CORS_ALLOW_METHODS")
    if env_methods:
        final_methods = [m.strip().upper() for m in env_methods.split(",")]

    env_headers = os.getenv("ALLOWED_HEADERS") or os.getenv("CORS_ALLOW_HEADERS")
    if env_headers:
        final_headers = [h.strip() for h in env_headers.split(",")]

    logger.info(
        "Final CORS configuration after environment overrides",
        origins=final_origins,
        methods=final_methods,
        headers=final_headers,
    )

    # Add security and logging first (inner layers)
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(ComprehensiveLoggingMiddleware)

    # Add single CORS middleware with environment-aware configuration
    # SecurityHeadersMiddleware handles all security headers
    app.add_middleware(
        CORSMiddleware,
        allow_origins=final_origins,
        allow_credentials=allow_credentials_bool,
        allow_methods=final_methods,
        allow_headers=final_headers,
        max_age=max_age_int,
        expose_headers=expose_headers_list if expose_headers_list else [],
    )

    # Note: AllowedCORSMiddleware removed - functionality consolidated into CORSMiddleware above

    # Setup comprehensive error handling (middleware + exception handlers)
    # Include details in development mode, hide in production
    include_details = os.getenv("ENV", "development") != "production"
    setup_error_handling(app, include_details=include_details)

    # Include routers
    app.include_router(auth_router)

    # Include FastAPI Users routers for authentication
    app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])

    app.include_router(command_router)
    app.include_router(player_router)
    app.include_router(profession_router)
    app.include_router(game_router)
    app.include_router(monitoring_router)
    app.include_router(system_monitoring_router)  # System-level monitoring (root-level paths)
    app.include_router(metrics_router)  # NEW: NATS metrics endpoint (CRITICAL-4)
    app.include_router(realtime_router)
    app.include_router(room_router, prefix="/api")
    app.include_router(map_router, prefix="/api")
    app.include_router(container_router)  # Container system endpoints
    app.include_router(admin_npc_router)
    app.include_router(admin_subject_router, prefix="/api/admin")  # NATS subject management endpoints

    # CORS handled by AllowedCORSMiddleware above

    return app
