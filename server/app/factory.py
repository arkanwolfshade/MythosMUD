"""
FastAPI application factory for MythosMUD server.

This module handles FastAPI app creation, middleware configuration,
and router registration.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..auth.endpoints import auth_router
from ..command_handler import router as command_router
from .lifespan import lifespan


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

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(auth_router)
    app.include_router(command_router)

    return app
