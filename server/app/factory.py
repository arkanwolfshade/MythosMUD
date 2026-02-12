"""
FastAPI application factory for MythosMUD server.

This module handles FastAPI app creation, middleware configuration,
and router registration.
"""

import json
import os
from typing import Any, TypedDict, cast

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..api.admin import npc_router as admin_npc_router
from ..api.admin import subject_router as admin_subject_router
from ..api.containers import container_router
from ..api.game import game_router
from ..api.maps import map_router
from ..api.metrics import router as metrics_router
from ..api.monitoring import monitoring_router
from ..api.players import player_router
from ..api.professions import profession_router
from ..api.real_time import realtime_router
from ..api.rooms import room_router
from ..api.system_monitoring import system_monitoring_router
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


class CORSConfigDict(TypedDict):
    """Type definition for CORS configuration dictionary."""

    allow_origins: list[str]
    allow_methods: list[str]
    allow_headers: list[str]
    expose_headers: list[str]
    allow_credentials: bool
    max_age: int


def _get_default_cors_config() -> CORSConfigDict:
    """
    Get default CORS configuration values.

    Returns:
        CORSConfigDict: Dictionary with default CORS settings
    """
    return {
        "allow_origins": [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ],
        "allow_methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        "allow_headers": [
            "Content-Type",
            "Authorization",
            "X-Requested-With",
            "Accept",
            "Accept-Language",
        ],
        "expose_headers": [],
        "allow_credentials": True,
        "max_age": 600,
    }


def _get_cors_config_from_app_config() -> CORSConfigDict:
    """
    Get CORS configuration from AppConfig, with fallback to defaults.

    Returns:
        CORSConfigDict: CORS configuration from config or defaults
    """
    try:
        config = get_config()
        cors_cfg: Any = config.cors
        return {
            "allow_origins": list(getattr(cors_cfg, "allow_origins", [])),
            "allow_methods": [str(m).upper() for m in getattr(cors_cfg, "allow_methods", [])],
            "allow_headers": [str(h) for h in getattr(cors_cfg, "allow_headers", [])],
            "expose_headers": list(getattr(cors_cfg, "expose_headers", [])),
            "allow_credentials": bool(getattr(cors_cfg, "allow_credentials", True)),
            "max_age": int(getattr(cors_cfg, "max_age", 600)),
        }
    except Exception:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: CORS config errors unpredictable, must fallback to environment
        return _get_default_cors_config()


def _parse_cors_env_vars() -> dict[str, Any]:
    """
    Parse CORS-related environment variables and return overrides.

    Environment variables take precedence over config file values.
    Supports multiple formats:
    - Comma-separated values: "origin1,origin2"
    - JSON arrays: '["origin1","origin2"]'

    Returns:
        dict: Dictionary with environment variable overrides (may be empty)
    """
    overrides: dict[str, Any] = {}

    # Parse ALLOWED_ORIGINS / CORS_ALLOW_ORIGINS / CORS_ORIGINS
    env_origins = os.getenv("ALLOWED_ORIGINS") or os.getenv("CORS_ALLOW_ORIGINS") or os.getenv("CORS_ORIGINS")
    if env_origins:
        candidate = env_origins.strip()
        if candidate.startswith("["):
            try:
                parsed = json.loads(candidate)
                overrides["allow_origins"] = [str(o).strip() for o in parsed if str(o).strip()]
            except json.JSONDecodeError:
                overrides["allow_origins"] = [
                    o.strip().strip('"').strip("'") for o in candidate.strip("[]").split(",") if o.strip()
                ]
        else:
            overrides["allow_origins"] = [o.strip() for o in candidate.split(",") if o.strip()]

    # Parse ALLOWED_METHODS / CORS_ALLOW_METHODS
    env_methods = os.getenv("ALLOWED_METHODS") or os.getenv("CORS_ALLOW_METHODS")
    if env_methods:
        overrides["allow_methods"] = [m.strip().upper() for m in env_methods.split(",")]

    # Parse ALLOWED_HEADERS / CORS_ALLOW_HEADERS
    env_headers = os.getenv("ALLOWED_HEADERS") or os.getenv("CORS_ALLOW_HEADERS")
    if env_headers:
        overrides["allow_headers"] = [h.strip() for h in env_headers.split(",")]

    return overrides


def _configure_cors() -> CORSConfigDict:
    """
    Configure CORS settings from config file and environment variables.

    Precedence: ENV > CONFIG > DEFAULTS

    Returns:
        CORSConfigDict: Final CORS configuration dictionary
    """
    # Start with config file values (or defaults)
    cors_config = _get_cors_config_from_app_config()

    logger.info(
        "CORS configuration",
        allow_origins=cors_config["allow_origins"],
        allow_methods=cors_config["allow_methods"],
        allow_headers=cors_config["allow_headers"],
        expose_headers=cors_config["expose_headers"],
        allow_credentials=cors_config["allow_credentials"],
        max_age=cors_config["max_age"],
    )

    # Apply environment variable overrides
    env_overrides = _parse_cors_env_vars()
    # Cast to CORSConfigDict for type safety - env_overrides only contains valid CORS keys
    cors_config.update(cast(CORSConfigDict, env_overrides))

    logger.info(
        "Final CORS configuration after environment overrides",
        origins=cors_config["allow_origins"],
        methods=cors_config["allow_methods"],
        headers=cors_config["allow_headers"],
    )

    return cors_config


# OpenAPI tag metadata for API documentation (Swagger/ReDoc).
# Order defines display order in docs UI.
OPENAPI_TAGS = [
    {"name": "auth", "description": "Authentication: JWT login, registration, user management."},
    {"name": "users", "description": "User account operations (FastAPI Users)."},
    {"name": "players", "description": "Player characters: create, list, select, delete, stats, effects."},
    {"name": "professions", "description": "Character class and profession data."},
    {"name": "game", "description": "Game state: enter game, movement, combat actions."},
    {"name": "containers", "description": "Unified container system: environmental, wearable, corpse storage."},
    {"name": "rooms", "description": "Room data and exploration."},
    {"name": "maps", "description": "ASCII map rendering and exploration views."},
    {"name": "realtime", "description": "WebSocket connection and real-time game events."},
    {"name": "monitoring", "description": "Health checks, performance metrics, observability."},
    {"name": "metrics", "description": "NATS and system metrics."},
    {"name": "admin", "description": "Administrative endpoints: NPC management, teleport."},
    {"name": "npc", "description": "NPC spawn and lifecycle administration."},
    {"name": "nats", "description": "NATS subject management (admin)."},
    {"name": "subjects", "description": "NATS subject inspection and management."},
    {"name": "system", "description": "System-level monitoring and diagnostics."},
    {"name": "api", "description": "Base API utilities."},
]


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
        description=(
            "A Cthulhu Mythos-themed MUD game API with real-time communication via WebSocket. "
            "REST endpoints handle authentication, player management, rooms, containers, and game state. "
            "Contract documentation: docs/architecture/API_OPENAPI_SPECIFICATION.md"
        ),
        version="0.1.0",
        openapi_tags=OPENAPI_TAGS,
        license_info={"name": "MIT", "identifier": "MIT"},
        lifespan=lifespan,
    )

    # Configure CORS settings (precedence: ENV > CONFIG > DEFAULTS)
    cors_config = _configure_cors()

    # Add security and logging first (inner layers)
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(ComprehensiveLoggingMiddleware)

    # Add single CORS middleware with environment-aware configuration
    # SecurityHeadersMiddleware handles all security headers
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_config["allow_origins"],
        allow_credentials=cors_config["allow_credentials"],
        allow_methods=cors_config["allow_methods"],
        allow_headers=cors_config["allow_headers"],
        max_age=cors_config["max_age"],
        expose_headers=cors_config["expose_headers"] if cors_config["expose_headers"] else [],
    )

    # Note: AllowedCORSMiddleware removed - functionality consolidated into CORSMiddleware above

    # Setup comprehensive error handling (middleware + exception handlers)
    # Include details in development mode, hide in production
    include_details = os.getenv("ENV", "development") != "production"
    setup_error_handling(app, include_details=include_details)

    # API v1: mount all versioned API routers under /v1
    v1_router = APIRouter(prefix="/v1")
    v1_router.include_router(auth_router)
    v1_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
    v1_router.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"],
    )
    v1_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])
    v1_router.include_router(command_router)
    v1_router.include_router(player_router)
    v1_router.include_router(profession_router)
    v1_router.include_router(game_router)
    v1_router.include_router(monitoring_router)
    v1_router.include_router(system_monitoring_router)
    v1_router.include_router(metrics_router)
    v1_router.include_router(realtime_router)
    v1_router.include_router(room_router, prefix="/api")
    v1_router.include_router(map_router, prefix="/api")
    v1_router.include_router(container_router)
    v1_router.include_router(admin_npc_router)
    v1_router.include_router(admin_subject_router, prefix="/api/admin")
    app.include_router(v1_router)

    # CORS handled by AllowedCORSMiddleware above

    return app
