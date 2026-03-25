"""
Router and shared auth helper for NPC Admin API.

Submodules import from here to avoid circular imports; npc.py re-exports and
imports submodules so "from server.api.admin.npc import npc_router" still works.
"""

from fastapi import APIRouter, Request

from ...models.user import User
from ...services.admin_auth_service import AdminAction, get_admin_auth_service
from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)
npc_router = APIRouter(prefix="/admin/npc", tags=["admin", "npc"])
logger.info("NPC Admin API router initialized")


def validate_admin_permission(
    current_user: User | None,
    action: AdminAction,
    request: Request,
) -> None:
    """Validate that the current user has admin permissions for the specified action."""
    auth_service = get_admin_auth_service()
    auth_service.validate_permission(current_user, action, request)
