"""
Admin session and audit log endpoints under /admin/npc.

Split out from server.api.admin.npc to keep file NLOC under complexity limits.
"""

from fastapi import Depends, HTTPException, Request, status

from ...auth.users import get_current_user
from ...exceptions import LoggedHTTPException
from ...models.user import User
from ...schemas.admin import (
    AdminAuditLogResponse,
    AdminCleanupSessionsResponse,
    AdminSessionsResponse,
)
from ...services.admin_auth_service import AdminAction, get_admin_auth_service
from ...structured_logging.enhanced_logging_config import get_logger
from .npc_router_core import npc_router, validate_admin_permission

logger = get_logger(__name__)


@npc_router.get("/admin/sessions", response_model=AdminSessionsResponse)
async def get_admin_sessions(
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> AdminSessionsResponse:
    """Get active admin sessions."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_SYSTEM_STATUS, request)
        auth_service = get_admin_auth_service()
        sessions = auth_service.get_active_sessions()
        logger.info(
            "Retrieved admin sessions",
            user=auth_service.get_username(current_user),
            session_count=len(sessions),
        )
        return AdminSessionsResponse(sessions=sessions, count=len(sessions))
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error retrieving admin sessions", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving admin sessions",
        ) from e


@npc_router.get("/admin/audit-log", response_model=AdminAuditLogResponse)
async def get_admin_audit_log(
    request: Request,
    limit: int = 100,
    current_user: User | None = Depends(get_current_user),
) -> AdminAuditLogResponse:
    """Get admin audit log."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_SYSTEM_STATUS, request)
        auth_service = get_admin_auth_service()
        audit_log = auth_service.get_audit_log(limit)
        logger.info(
            "Retrieved admin audit log",
            user=auth_service.get_username(current_user),
            limit=limit,
            entries=len(audit_log),
        )
        return AdminAuditLogResponse(audit_log=audit_log, count=len(audit_log))
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error retrieving admin audit log", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving admin audit log",
        ) from e


@npc_router.post("/admin/cleanup-sessions", response_model=AdminCleanupSessionsResponse)
async def cleanup_admin_sessions(
    request: Request,
    current_user: User | None = Depends(get_current_user),
) -> AdminCleanupSessionsResponse:
    """Clean up expired admin sessions."""
    try:
        validate_admin_permission(current_user, AdminAction.GET_SYSTEM_STATUS, request)
        auth_service = get_admin_auth_service()
        cleaned_count = auth_service.cleanup_expired_sessions()
        logger.info(
            "Cleaned up admin sessions",
            user=auth_service.get_username(current_user),
            cleaned_count=cleaned_count,
        )
        return AdminCleanupSessionsResponse(
            message=f"Cleaned up {cleaned_count} expired sessions",
            cleaned_count=cleaned_count,
        )
    except HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        logger.error("Error cleaning up admin sessions", error=str(e))
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error cleaning up admin sessions",
        ) from e
