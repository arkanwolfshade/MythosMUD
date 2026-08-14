"""Shared FastAPI APIRouter for player endpoints (avoids import cycles with route submodules)."""

from fastapi import APIRouter

player_router = APIRouter(prefix="/api/players", tags=["players"])
