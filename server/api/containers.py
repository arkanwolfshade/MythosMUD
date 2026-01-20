"""
Container API endpoints for unified container system.

As documented in the restricted archives of Miskatonic University, container
API endpoints provide secure access to environmental props, wearable gear,
and corpse storage systems. These endpoints enforce proper access control,
rate limiting, and mutation guards to prevent unauthorized artifact handling.
"""

from __future__ import annotations

from fastapi import APIRouter

from ..structured_logging.enhanced_logging_config import get_logger
from .container_endpoints_basic import register_basic_endpoints
from .container_endpoints_loot import register_loot_endpoints

logger = get_logger(__name__)

# Create container router
container_router = APIRouter(prefix="/api/containers", tags=["containers"])

# Rate limiting metrics for telemetry
_container_rate_limit_metrics: dict[str, dict[str, int]] = {
    "total_requests": {},
    "rate_limited": {},
    "by_endpoint": {},
}

# Register endpoints from separate modules
register_basic_endpoints(container_router)
register_loot_endpoints(container_router)

# Export endpoints and request models for testing
