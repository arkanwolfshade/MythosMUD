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
from ..middleware.allowed_cors import AllowedCORSMiddleware
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
    except Exception:
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

    # Allow explicit env overrides for methods/headers to support legacy variables in runtime
    env_methods = os.getenv("ALLOWED_METHODS") or os.getenv("CORS_ALLOW_METHODS")
    env_headers = os.getenv("ALLOWED_HEADERS") or os.getenv("CORS_ALLOW_HEADERS")

    allow_methods = [m.strip().upper() for m in env_methods.split(",")] if env_methods else allowed_methods_list
    allow_headers = [h.strip() for h in env_headers.split(",")] if env_headers else allowed_headers_list
    env_origins = os.getenv("ALLOWED_ORIGINS") or os.getenv("CORS_ALLOW_ORIGINS") or os.getenv("CORS_ORIGINS")
    if env_origins:
        candidate = env_origins.strip()
        if candidate.startswith("["):
            try:
                parsed = json.loads(candidate)
                allow_origins = [str(o).strip() for o in parsed if str(o).strip()]
            except json.JSONDecodeError:
                allow_origins = [o.strip().strip('"').strip("'") for o in candidate.strip("[]").split(",") if o.strip()]
        else:
            allow_origins = [o.strip() for o in env_origins.split(",") if o.strip()]
    else:
        allow_origins = allowed_origins_list

    # Add security and logging first (inner layers)
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(ComprehensiveLoggingMiddleware)

    # Add FastAPI CORSMiddleware for standard CORS behavior (tests inspect for this)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins_list,
        allow_credentials=True,
        allow_methods=allowed_methods_list,
        allow_headers=allowed_headers_list,
        max_age=max_age_int,
        expose_headers=expose_headers_list or None,
    )

    app.add_middleware(
        AllowedCORSMiddleware,
        allow_origins=allow_origins,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
        allow_credentials=allow_credentials_bool,
        max_age=max_age_int,
    )

    # Note: CORS handling is provided by AllowedCORSMiddleware above

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

    # CORS handled by AllowedCORSMiddleware above

    return app
