"""
FastAPI application factory for MythosMUD server.

This module handles FastAPI app creation, middleware configuration,
and router registration.
"""

import time
from collections.abc import Callable

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from ..api.admin import npc_router as admin_npc_router
from ..api.game import game_router
from ..api.monitoring import router as monitoring_router
from ..api.players import player_router
from ..api.real_time import realtime_router
from ..api.rooms import room_router
from ..auth.endpoints import UserCreate, UserRead, UserUpdate, auth_router
from ..auth.users import auth_backend, fastapi_users
from ..command_handler_unified import router as command_router
from ..error_handlers import register_error_handlers
from ..logging_config import get_logger
from .lifespan import lifespan

logger = get_logger(__name__)


class AccessLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log all HTTP requests and responses."""

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()

        # Log the incoming request
        logger.info(
            "HTTP request started",
            method=request.method,
            url=str(request.url),
            client_ip=request.client.host if request.client else "unknown",
            user_agent=request.headers.get("user-agent", "unknown"),
        )

        # Process the request
        response = await call_next(request)

        # Calculate processing time
        process_time = time.time() - start_time

        # Log the response
        logger.info(
            "HTTP request completed",
            method=request.method,
            url=str(request.url),
            status_code=response.status_code,
            process_time=process_time,
            client_ip=request.client.host if request.client else "unknown",
        )

        return response


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

    # Add access logging middleware (add first to capture all requests)
    app.add_middleware(AccessLoggingMiddleware)

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

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
    app.include_router(game_router)
    app.include_router(monitoring_router)
    app.include_router(realtime_router)
    app.include_router(room_router)
    app.include_router(admin_npc_router)

    return app
