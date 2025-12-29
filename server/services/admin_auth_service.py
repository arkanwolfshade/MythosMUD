"""
Admin Authentication and Authorization Service for MythosMUD.

This module provides enhanced authentication and authorization features
for admin endpoints, including role-based access control, audit logging,
and session management.

As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.
"""

import time
from datetime import UTC, datetime
from enum import Enum
from typing import Any

from fastapi import HTTPException, Request, status

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class AdminRole(str, Enum):
    """Enumeration of admin roles."""

    SUPERUSER = "superuser"  # Full system access
    ADMIN = "admin"  # NPC management access
    MODERATOR = "moderator"  # Limited admin access
    VIEWER = "viewer"  # Read-only access


class AdminAction(str, Enum):
    """Enumeration of admin actions for audit logging."""

    # NPC Definition Management
    CREATE_NPC_DEFINITION = "create_npc_definition"
    UPDATE_NPC_DEFINITION = "update_npc_definition"
    # Room Management
    UPDATE_ROOM_POSITION = "update_room_position"
    DELETE_NPC_DEFINITION = "delete_npc_definition"
    LIST_NPC_DEFINITIONS = "list_npc_definitions"

    # NPC Instance Management
    SPAWN_NPC = "spawn_npc"
    DESPAWN_NPC = "despawn_npc"
    MOVE_NPC = "move_npc"
    GET_NPC_STATS = "get_npc_stats"
    LIST_NPC_INSTANCES = "list_npc_instances"

    # Population Monitoring
    GET_POPULATION_STATS = "get_population_stats"
    GET_ZONE_STATS = "get_zone_stats"
    GET_SYSTEM_STATUS = "get_system_status"

    # Relationship Management
    CREATE_NPC_RELATIONSHIP = "create_npc_relationship"
    DELETE_NPC_RELATIONSHIP = "delete_npc_relationship"
    LIST_NPC_RELATIONSHIPS = "list_npc_relationships"

    # Spawn Rule Management
    CREATE_SPAWN_RULE = "create_spawn_rule"
    DELETE_SPAWN_RULE = "delete_spawn_rule"
    LIST_SPAWN_RULES = "list_spawn_rules"


class AdminSession:
    """Represents an admin session."""

    def __init__(self, user_id: str, username: str, role: AdminRole, ip_address: str) -> None:
        self.user_id = user_id
        self.username = username
        self.role = role
        self.ip_address = ip_address
        self.created_at = datetime.now(UTC)
        self.last_activity = datetime.now(UTC)
        self.action_count = 0
        self.is_active = True


class AdminAuthService:
    """Service for admin authentication and authorization."""

    def __init__(self) -> None:
        """Initialize the admin auth service."""
        self.active_sessions: dict[str, AdminSession] = {}
        self.audit_log: list[dict[str, Any]] = []
        self.rate_limits: dict[str, list[float]] = {}

        # Rate limiting configuration
        self.rate_limit_window = 300  # 5 minutes
        self.rate_limit_max_requests = 100  # Max requests per window

        # Session configuration
        self.session_timeout = 3600  # 1 hour

        logger.info("Admin authentication service initialized")

    def get_user_role(self, current_user: Any) -> AdminRole:
        """
        Determine the admin role for a user.

        Args:
            current_user: The current user object

        Returns:
            AdminRole: The user's admin role
        """
        if not current_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")

        # Check for superuser status (from FastAPI Users)
        if hasattr(current_user, "is_superuser") and current_user.is_superuser:
            return AdminRole.SUPERUSER

        # Check for admin status (from Player model - for backward compatibility)
        if hasattr(current_user, "get") and current_user.get("is_admin", False):
            return AdminRole.ADMIN

        # Check for admin status as attribute (for backward compatibility)
        if hasattr(current_user, "is_admin") and current_user.is_admin:
            return AdminRole.ADMIN

        # Default to viewer role for authenticated users
        return AdminRole.VIEWER

    def get_username(self, current_user: Any) -> str:
        """Safely get username from current user object."""
        if not current_user:
            return "unknown"

        # Try to get username from User object
        if hasattr(current_user, "username"):
            result = current_user.username
            assert isinstance(result, str)
            return result

        # Try to get username from dictionary
        if hasattr(current_user, "get"):
            result = current_user.get("username", "unknown")
            assert isinstance(result, str)
            return result

        return "unknown"

    def get_user_id(self, current_user: Any) -> str:
        """Safely get user ID from current user object."""
        if not current_user:
            return "unknown"

        # Try to get ID from User object
        if hasattr(current_user, "id"):
            return str(current_user.id)

        # Try to get ID from dictionary
        if hasattr(current_user, "get"):
            return str(current_user.get("id", "unknown"))

        return "unknown"

    def validate_permission(self, current_user: Any, action: AdminAction, request: Request | None = None) -> None:
        """
        Validate that the current user has permission to perform the action.

        Args:
            current_user: The current user object
            action: The action being performed
            request: The HTTP request (for IP address and audit logging)

        Raises:
            HTTPException: If permission is denied
        """
        if not current_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")

        # Get user role
        role = self.get_user_role(current_user)
        user_id = self.get_user_id(current_user)
        username = self.get_username(current_user)

        # Check rate limiting
        self._check_rate_limit(user_id, request)

        # Check if user has permission for this action
        if not self._has_permission(role, action):
            self._log_audit_event(user_id, username, action, "permission_denied", request)
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail=f"Permission denied for action: {action.value}"
            )

        # Update session
        self._update_session(user_id, username, role, request)

        # Log successful action
        self._log_audit_event(user_id, username, action, "success", request)

    def _has_permission(self, role: AdminRole, action: AdminAction) -> bool:
        """
        Check if a role has permission for an action.

        Args:
            role: The user's role
            action: The action being performed

        Returns:
            bool: True if permission is granted
        """
        # Define permission matrix
        permissions = {
            AdminRole.SUPERUSER: list(AdminAction),  # All permissions
            AdminRole.ADMIN: [
                AdminAction.CREATE_NPC_DEFINITION,
                AdminAction.UPDATE_NPC_DEFINITION,
                AdminAction.DELETE_NPC_DEFINITION,
                AdminAction.LIST_NPC_DEFINITIONS,
                AdminAction.SPAWN_NPC,
                AdminAction.DESPAWN_NPC,
                AdminAction.MOVE_NPC,
                AdminAction.GET_NPC_STATS,
                AdminAction.LIST_NPC_INSTANCES,
                AdminAction.GET_POPULATION_STATS,
                AdminAction.GET_ZONE_STATS,
                AdminAction.GET_SYSTEM_STATUS,
                AdminAction.CREATE_NPC_RELATIONSHIP,
                AdminAction.DELETE_NPC_RELATIONSHIP,
                AdminAction.LIST_NPC_RELATIONSHIPS,
                AdminAction.CREATE_SPAWN_RULE,
                AdminAction.DELETE_SPAWN_RULE,
                AdminAction.LIST_SPAWN_RULES,
            ],
            AdminRole.MODERATOR: [
                AdminAction.LIST_NPC_DEFINITIONS,
                AdminAction.LIST_NPC_INSTANCES,
                AdminAction.GET_NPC_STATS,
                AdminAction.GET_POPULATION_STATS,
                AdminAction.GET_ZONE_STATS,
                AdminAction.GET_SYSTEM_STATUS,
                AdminAction.LIST_NPC_RELATIONSHIPS,
                AdminAction.LIST_SPAWN_RULES,
            ],
            AdminRole.VIEWER: [
                AdminAction.LIST_NPC_DEFINITIONS,
                AdminAction.LIST_NPC_INSTANCES,
                AdminAction.GET_POPULATION_STATS,
                AdminAction.GET_ZONE_STATS,
                AdminAction.GET_SYSTEM_STATUS,
                AdminAction.LIST_NPC_RELATIONSHIPS,
                AdminAction.LIST_SPAWN_RULES,
            ],
        }

        return action in permissions.get(role, [])

    def _check_rate_limit(self, user_id: str, request: Request | None = None) -> None:
        """
        Check if user has exceeded rate limits.

        Args:
            user_id: The user ID
            request: The HTTP request

        Raises:
            HTTPException: If rate limit is exceeded
        """
        now = time.time()

        # Clean old entries
        if user_id in self.rate_limits:
            self.rate_limits[user_id] = [
                timestamp for timestamp in self.rate_limits[user_id] if now - timestamp < self.rate_limit_window
            ]
        else:
            self.rate_limits[user_id] = []

        # Check if limit exceeded
        if len(self.rate_limits[user_id]) >= self.rate_limit_max_requests:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate limit exceeded. Please try again later."
            )

        # Add current request
        self.rate_limits[user_id].append(now)

    def _update_session(self, user_id: str, username: str, role: AdminRole, request: Request | None = None) -> None:
        """
        Update or create admin session.

        Args:
            user_id: The user ID
            username: The username
            role: The user's role
            request: The HTTP request
        """
        ip_address = "unknown"
        if request and request.client:
            ip_address = request.client.host

        if user_id in self.active_sessions:
            session = self.active_sessions[user_id]
            session.last_activity = datetime.now(UTC)
            session.action_count += 1
        else:
            session = AdminSession(user_id, username, role, ip_address)
            self.active_sessions[user_id] = session
            logger.info(
                "Admin session created", user_id=user_id, username=username, role=role.value, ip_address=ip_address
            )

    def _log_audit_event(
        self, user_id: str, username: str, action: AdminAction, result: str, request: Request | None = None
    ) -> None:
        """
        Log an audit event.

        Args:
            user_id: The user ID
            username: The username
            action: The action performed
            result: The result (success, permission_denied, etc.)
            request: The HTTP request
        """
        ip_address = "unknown"
        user_agent = "unknown"

        if request:
            if request.client:
                ip_address = request.client.host
            user_agent = request.headers.get("User-Agent", "unknown")

        event = {
            "timestamp": datetime.now(UTC).isoformat(),
            "user_id": user_id,
            "username": username,
            "action": action.value,
            "result": result,
            "ip_address": ip_address,
            "user_agent": user_agent,
        }

        self.audit_log.append(event)

        # Keep only last 1000 events
        if len(self.audit_log) > 1000:
            self.audit_log = self.audit_log[-1000:]

        logger.info(
            "Admin action logged",
            user_id=user_id,
            username=username,
            action=action.value,
            result=result,
            ip_address=ip_address,
        )

    def get_active_sessions(self) -> list[dict[str, Any]]:
        """
        Get list of active admin sessions.

        Returns:
            List of active session information
        """
        now = datetime.now(UTC)
        active_sessions = []

        for user_id, session in self.active_sessions.items():
            if session.is_active and (now - session.last_activity).total_seconds() < self.session_timeout:
                active_sessions.append(
                    {
                        "user_id": user_id,
                        "username": session.username,
                        "role": session.role.value,
                        "ip_address": session.ip_address,
                        "created_at": session.created_at.isoformat(),
                        "last_activity": session.last_activity.isoformat(),
                        "action_count": session.action_count,
                    }
                )
            else:
                # Mark session as inactive
                session.is_active = False

        return active_sessions

    def get_audit_log(self, limit: int = 100) -> list[dict[str, Any]]:
        """
        Get audit log entries.

        Args:
            limit: Maximum number of entries to return

        Returns:
            List of audit log entries
        """
        return self.audit_log[-limit:] if limit > 0 else self.audit_log

    def cleanup_expired_sessions(self) -> int:
        """
        Clean up expired sessions.

        Returns:
            Number of sessions cleaned up
        """
        now = datetime.now(UTC)
        expired_sessions = []

        for user_id, session in self.active_sessions.items():
            if (now - session.last_activity).total_seconds() > self.session_timeout:
                expired_sessions.append(user_id)

        for user_id in expired_sessions:
            del self.active_sessions[user_id]

        if expired_sessions:
            logger.info("Cleaned up expired admin sessions", count=len(expired_sessions))

        return len(expired_sessions)


# Global instance
admin_auth_service = AdminAuthService()


def get_admin_auth_service() -> AdminAuthService:
    """Get the global admin auth service."""
    return admin_auth_service
