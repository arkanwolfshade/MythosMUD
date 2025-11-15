"""Helpers for caching player objects during a single command request.

This avoids repeated persistence lookups when multiple systems (catatonia
checks, command handlers, etc.) all need the same player record.
"""

from __future__ import annotations

from typing import Any

_CACHE_ATTR = "_command_player_cache"


def _get_request_state(request: Any) -> Any | None:
    """Safely extract the state object from a FastAPI/Starlette request."""
    return getattr(request, "state", None) if request else None


def get_cached_player(request: Any, player_name: str) -> Any | None:
    """Return a cached player object for this request if one exists."""
    state = _get_request_state(request)
    if state is None:
        return None

    cache = getattr(state, _CACHE_ATTR, None)
    if isinstance(cache, dict):
        return cache.get(player_name)
    return None


def cache_player(request: Any, player_name: str, player: Any) -> None:
    """Cache a player object on the request for reuse within the command."""
    state = _get_request_state(request)
    if state is None:
        return

    cache = getattr(state, _CACHE_ATTR, None)
    if cache is None or not isinstance(cache, dict):
        cache = {}
        setattr(state, _CACHE_ATTR, cache)

    cache[player_name] = player
