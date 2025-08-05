"""
Base API router and common dependencies for MythosMUD server.

This module provides the base router and common dependencies
that are shared across all API endpoints.
"""

from fastapi import APIRouter, Depends

from ..auth.users import get_current_user

# Create base router for API endpoints
api_router = APIRouter(prefix="/api", tags=["api"])

# Common dependencies
CurrentUser = Depends(get_current_user)
