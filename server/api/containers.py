"""
Container API endpoints for unified container system.

As documented in the restricted archives of Miskatonic University, container
API endpoints provide secure access to environmental props, wearable gear,
and corpse storage systems. These endpoints enforce proper access control,
rate limiting, and mutation guards to prevent unauthorized artifact handling.
"""

from __future__ import annotations

import importlib

from fastapi import APIRouter

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Create container router
container_router = APIRouter(prefix="/api/containers", tags=["containers"])

# Rate limiting metrics for telemetry
_container_rate_limit_metrics: dict[str, dict[str, int]] = {
    "total_requests": {},
    "rate_limited": {},
    "by_endpoint": {},
}


def _register_endpoints() -> None:
    # importlib: avoid a static import edge containers -> loot/basic that closes the cycle
    # loot/basic -> auth -> ... -> factory -> containers
    basic = importlib.import_module("server.api.container_endpoints_basic")
    loot = importlib.import_module("server.api.container_endpoints_loot")
    basic.register_basic_endpoints(container_router)
    loot.register_loot_endpoints(container_router)


_register_endpoints()

# Export endpoints and request models for testing
