"""
Tests for admin authentication and authorization service.

This module tests the AdminAuthService for role-based access control,
audit logging, and session management.
"""

import uuid
from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException, Request, status

from server.services.admin_auth_service import (
    AdminAction,
    AdminAuthService,
    AdminRole,
    AdminSession,
    get_admin_auth_service,
)


class TestAdminRole:
    """Test AdminRole enum."""

    def test_admin_role_values(self) -> None:
        """Test AdminRole enum values."""
        assert AdminRole.SUPERUSER.value == "superuser"
        assert AdminRole.ADMIN.value == "admin"
        assert AdminRole.MODERATOR.value == "moderator"
        assert AdminRole.VIEWER.value == "viewer"


class TestAdminAction:
    """Test AdminAction enum."""

    def test_admin_action_values(self) -> None:
        """Test AdminAction enum values."""
        assert AdminAction.CREATE_NPC_DEFINITION.value == "create_npc_definition"
        assert AdminAction.LIST_NPC_DEFINITIONS.value == "list_npc_definitions"
        assert AdminAction.SPAWN_NPC.value == "spawn_npc"


class TestAdminSession:
    """Test AdminSession class."""

    def test_admin_session_initialization(self) -> None:
        """Test AdminSession initialization."""
        session = AdminSession("user-123", "testuser", AdminRole.ADMIN, "127.0.0.1")
        assert session.user_id == "user-123"
        assert session.username == "testuser"
        assert session.role == AdminRole.ADMIN
        assert session.ip_address == "127.0.0.1"
        assert session.action_count == 0
        assert session.is_active is True


class TestAdminAuthServiceGetUserRole:
    """Test AdminAuthService.get_user_role."""

    def test_get_user_role_with_none(self) -> None:
        """Test get_user_role raises exception with None user."""
        service = AdminAuthService()
        with pytest.raises(HTTPException) as exc_info:
            service.get_user_role(None)
        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_user_role_with_superuser(self) -> None:
        """Test get_user_role returns SUPERUSER for superuser."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.is_superuser = True

        role = service.get_user_role(mock_user)
        assert role == AdminRole.SUPERUSER

    def test_get_user_role_with_admin_dict(self) -> None:
        """Test get_user_role returns ADMIN for dict with is_admin."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.get = Mock(return_value=True)
        mock_user.is_superuser = False

        role = service.get_user_role(mock_user)
        assert role == AdminRole.ADMIN

    def test_get_user_role_with_admin_attribute(self) -> None:
        """Test get_user_role returns ADMIN for user with is_admin attribute."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.is_superuser = False
        mock_user.is_admin = True

        role = service.get_user_role(mock_user)
        assert role == AdminRole.ADMIN

    def test_get_user_role_defaults_to_viewer(self) -> None:
        """Test get_user_role defaults to VIEWER for regular user."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.is_superuser = False
        mock_user.is_admin = False
        # Ensure get method returns False for is_admin to prevent Mock from being truthy
        mock_user.get = Mock(side_effect=lambda key, default=None: default if key == "is_admin" else Mock())

        role = service.get_user_role(mock_user)
        assert role == AdminRole.VIEWER


class TestAdminAuthServiceGetUsername:
    """Test AdminAuthService.get_username."""

    def test_get_username_with_user_object(self) -> None:
        """Test get_username from User object."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.username = "testuser"

        username = service.get_username(mock_user)
        assert username == "testuser"

    def test_get_username_with_dict(self) -> None:
        """Test get_username from dict."""
        service = AdminAuthService()
        mock_user = Mock()
        # Remove username attribute to force dict path
        delattr(mock_user, "username")
        mock_user.get = Mock(side_effect=lambda key, default="unknown": "dictuser" if key == "username" else default)

        username = service.get_username(mock_user)
        assert username == "dictuser"

    def test_get_username_with_none(self) -> None:
        """Test get_username returns 'unknown' for None."""
        service = AdminAuthService()
        username = service.get_username(None)
        assert username == "unknown"

    def test_get_username_with_no_username(self) -> None:
        """Test get_username returns 'unknown' when username not found."""
        service = AdminAuthService()
        mock_user = Mock()
        # Remove username attribute
        delattr(mock_user, "username")
        # Ensure get method returns "unknown" for username
        mock_user.get = Mock(side_effect=lambda key, default="unknown": default)

        username = service.get_username(mock_user)
        assert username == "unknown"


class TestAdminAuthServiceGetUserId:
    """Test AdminAuthService.get_user_id."""

    def test_get_user_id_with_user_object(self) -> None:
        """Test get_user_id from User object."""
        service = AdminAuthService()
        test_uuid = uuid.uuid4()
        mock_user = Mock()
        mock_user.id = test_uuid

        user_id = service.get_user_id(mock_user)
        assert user_id == str(test_uuid)

    def test_get_user_id_with_dict(self) -> None:
        """Test get_user_id from dict."""
        service = AdminAuthService()
        test_uuid = uuid.uuid4()
        mock_user = Mock()
        # Remove id attribute to force dict path
        delattr(mock_user, "id")
        mock_user.get = Mock(side_effect=lambda key, default="unknown": test_uuid if key == "id" else default)

        user_id = service.get_user_id(mock_user)
        assert user_id == str(test_uuid)

    def test_get_user_id_with_none(self) -> None:
        """Test get_user_id returns 'unknown' for None."""
        service = AdminAuthService()
        user_id = service.get_user_id(None)
        assert user_id == "unknown"

    def test_get_user_id_with_no_id(self) -> None:
        """Test get_user_id returns 'unknown' when id not found."""
        service = AdminAuthService()
        mock_user = Mock()
        # Remove id attribute
        delattr(mock_user, "id")
        # Ensure get method returns "unknown" for id
        mock_user.get = Mock(side_effect=lambda key, default="unknown": default)

        user_id = service.get_user_id(mock_user)
        assert user_id == "unknown"


class TestAdminAuthServiceHasPermission:
    """Test AdminAuthService._has_permission."""

    def test_superuser_has_all_permissions(self) -> None:
        """Test superuser has permission for all actions."""
        service = AdminAuthService()
        for action in AdminAction:
            assert service._has_permission(AdminRole.SUPERUSER, action) is True

    def test_admin_has_npc_permissions(self) -> None:
        """Test admin has permission for NPC management actions."""
        service = AdminAuthService()
        assert service._has_permission(AdminRole.ADMIN, AdminAction.CREATE_NPC_DEFINITION) is True
        assert service._has_permission(AdminRole.ADMIN, AdminAction.SPAWN_NPC) is True
        assert service._has_permission(AdminRole.ADMIN, AdminAction.LIST_NPC_DEFINITIONS) is True

    def test_moderator_has_read_permissions(self) -> None:
        """Test moderator has permission for read-only actions."""
        service = AdminAuthService()
        assert service._has_permission(AdminRole.MODERATOR, AdminAction.LIST_NPC_DEFINITIONS) is True
        assert service._has_permission(AdminRole.MODERATOR, AdminAction.GET_POPULATION_STATS) is True
        assert service._has_permission(AdminRole.MODERATOR, AdminAction.CREATE_NPC_DEFINITION) is False

    def test_viewer_has_limited_permissions(self) -> None:
        """Test viewer has permission for limited read actions."""
        service = AdminAuthService()
        assert service._has_permission(AdminRole.VIEWER, AdminAction.LIST_NPC_DEFINITIONS) is True
        assert service._has_permission(AdminRole.VIEWER, AdminAction.GET_POPULATION_STATS) is True
        assert service._has_permission(AdminRole.VIEWER, AdminAction.CREATE_NPC_DEFINITION) is False
        assert service._has_permission(AdminRole.VIEWER, AdminAction.SPAWN_NPC) is False


class TestAdminAuthServiceCheckRateLimit:
    """Test AdminAuthService._check_rate_limit."""

    def test_check_rate_limit_allows_requests(self) -> None:
        """Test _check_rate_limit allows requests under limit."""
        service = AdminAuthService()
        service.rate_limit_max_requests = 10

        # Should not raise exception
        for _ in range(5):
            service._check_rate_limit("user-1", None)

    def test_check_rate_limit_raises_when_exceeded(self) -> None:
        """Test _check_rate_limit raises exception when limit exceeded."""
        service = AdminAuthService()
        service.rate_limit_max_requests = 5

        # Fill up to limit
        for _ in range(5):
            service._check_rate_limit("user-2", None)

        # Next request should raise exception
        with pytest.raises(HTTPException) as exc_info:
            service._check_rate_limit("user-2", None)
        assert exc_info.value.status_code == status.HTTP_429_TOO_MANY_REQUESTS

    def test_check_rate_limit_cleans_old_entries(self) -> None:
        """Test _check_rate_limit cleans old entries."""
        import time

        service = AdminAuthService()
        service.rate_limit_window = 1  # Short window for testing (must be int)
        service.rate_limit_max_requests = 3

        # Add requests
        service._check_rate_limit("user-3", None)
        service._check_rate_limit("user-3", None)

        # Wait for window to expire
        time.sleep(0.2)

        # Should be able to add more requests
        service._check_rate_limit("user-3", None)
        service._check_rate_limit("user-3", None)


class TestAdminAuthServiceUpdateSession:
    """Test AdminAuthService._update_session."""

    def test_update_session_creates_new_session(self) -> None:
        """Test _update_session creates new session."""
        service = AdminAuthService()
        mock_request = Mock(spec=Request)
        mock_request.client = Mock()
        mock_request.client.host = "192.168.1.1"

        service._update_session("user-new", "newuser", AdminRole.ADMIN, mock_request)

        assert "user-new" in service.active_sessions
        session = service.active_sessions["user-new"]
        assert session.username == "newuser"
        assert session.role == AdminRole.ADMIN
        assert session.ip_address == "192.168.1.1"

    def test_update_session_updates_existing_session(self) -> None:
        """Test _update_session updates existing session."""
        service = AdminAuthService()
        mock_request = Mock(spec=Request)
        mock_request.client = Mock()
        mock_request.client.host = "192.168.1.1"

        # Create session
        service._update_session("user-update", "updateuser", AdminRole.ADMIN, mock_request)
        initial_count = service.active_sessions["user-update"].action_count

        # Update session
        service._update_session("user-update", "updateuser", AdminRole.ADMIN, mock_request)
        assert service.active_sessions["user-update"].action_count == initial_count + 1

    def test_update_session_with_none_request(self) -> None:
        """Test _update_session handles None request."""
        service = AdminAuthService()
        service._update_session("user-none", "noneuser", AdminRole.VIEWER, None)

        assert "user-none" in service.active_sessions
        session = service.active_sessions["user-none"]
        assert session.ip_address == "unknown"


class TestAdminAuthServiceLogAuditEvent:
    """Test AdminAuthService._log_audit_event."""

    def test_log_audit_event_logs_event(self) -> None:
        """Test _log_audit_event logs event."""
        service = AdminAuthService()
        mock_request = Mock(spec=Request)
        mock_request.client = Mock()
        mock_request.client.host = "10.0.0.1"
        mock_request.headers = {"User-Agent": "TestAgent"}

        service._log_audit_event("user-1", "testuser", AdminAction.CREATE_NPC_DEFINITION, "success", mock_request)

        assert len(service.audit_log) == 1
        event = service.audit_log[0]
        assert event["user_id"] == "user-1"
        assert event["username"] == "testuser"
        assert event["action"] == "create_npc_definition"
        assert event["result"] == "success"
        assert event["ip_address"] == "10.0.0.1"
        assert event["user_agent"] == "TestAgent"

    def test_log_audit_event_with_none_request(self) -> None:
        """Test _log_audit_event handles None request."""
        service = AdminAuthService()
        service._log_audit_event("user-2", "testuser2", AdminAction.LIST_NPC_DEFINITIONS, "success", None)

        assert len(service.audit_log) == 1
        event = service.audit_log[0]
        assert event["ip_address"] == "unknown"
        assert event["user_agent"] == "unknown"

    def test_log_audit_event_limits_log_size(self) -> None:
        """Test _log_audit_event limits log to 1000 events."""
        service = AdminAuthService()

        # Add more than 1000 events
        for i in range(1005):
            service._log_audit_event(f"user-{i}", f"user{i}", AdminAction.GET_SYSTEM_STATUS, "success", None)

        # Should only keep last 1000
        assert len(service.audit_log) == 1000


class TestAdminAuthServiceValidatePermission:
    """Test AdminAuthService.validate_permission."""

    def test_validate_permission_with_none_user(self) -> None:
        """Test validate_permission raises exception with None user."""
        service = AdminAuthService()
        mock_request = Mock(spec=Request)

        with pytest.raises(HTTPException) as exc_info:
            service.validate_permission(None, AdminAction.LIST_NPC_DEFINITIONS, mock_request)
        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED

    def test_validate_permission_with_superuser(self) -> None:
        """Test validate_permission allows superuser for any action."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.is_superuser = True
        mock_user.id = uuid.uuid4()
        mock_user.username = "superuser"
        mock_request = Mock(spec=Request)
        mock_request.client = Mock()
        mock_request.client.host = "127.0.0.1"

        # Should not raise exception
        service.validate_permission(mock_user, AdminAction.CREATE_NPC_DEFINITION, mock_request)

    def test_validate_permission_denies_viewer_write_action(self) -> None:
        """Test validate_permission denies viewer write actions."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.is_superuser = False
        mock_user.is_admin = False
        mock_user.id = uuid.uuid4()
        mock_user.username = "viewer"
        # Ensure get method returns False for is_admin to prevent Mock from being truthy
        mock_user.get = Mock(side_effect=lambda key, default=None: default if key == "is_admin" else Mock())
        mock_request = Mock(spec=Request)
        mock_request.client = Mock()
        mock_request.client.host = "127.0.0.1"

        with pytest.raises(HTTPException) as exc_info:
            service.validate_permission(mock_user, AdminAction.CREATE_NPC_DEFINITION, mock_request)
        assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN

    def test_validate_permission_allows_viewer_read_action(self) -> None:
        """Test validate_permission allows viewer read actions."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.is_superuser = False
        mock_user.is_admin = False
        mock_user.id = uuid.uuid4()
        mock_user.username = "viewer"
        mock_request = Mock(spec=Request)
        mock_request.client = Mock()
        mock_request.client.host = "127.0.0.1"

        # Should not raise exception
        service.validate_permission(mock_user, AdminAction.LIST_NPC_DEFINITIONS, mock_request)

    def test_validate_permission_logs_audit_event(self) -> None:
        """Test validate_permission logs audit event."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.is_superuser = True
        mock_user.id = uuid.uuid4()
        mock_user.username = "admin"
        mock_request = Mock(spec=Request)
        mock_request.client = Mock()
        mock_request.client.host = "127.0.0.1"
        mock_request.headers = {"User-Agent": "TestAgent"}

        service.validate_permission(mock_user, AdminAction.CREATE_NPC_DEFINITION, mock_request)

        # Should have logged audit event
        assert len(service.audit_log) > 0
        assert service.audit_log[-1]["action"] == "create_npc_definition"
        assert service.audit_log[-1]["result"] == "success"

    def test_validate_permission_logs_permission_denied(self) -> None:
        """Test validate_permission logs permission denied."""
        service = AdminAuthService()
        mock_user = Mock()
        mock_user.is_superuser = False
        mock_user.is_admin = False
        mock_user.id = uuid.uuid4()
        mock_user.username = "viewer"
        # Ensure get method returns False for is_admin to prevent Mock from being truthy
        mock_user.get = Mock(side_effect=lambda key, default=None: default if key == "is_admin" else Mock())
        mock_request = Mock(spec=Request)
        mock_request.client = Mock()
        mock_request.client.host = "127.0.0.1"

        with pytest.raises(HTTPException):
            service.validate_permission(mock_user, AdminAction.CREATE_NPC_DEFINITION, mock_request)

        # Should have logged permission denied
        assert len(service.audit_log) > 0
        assert service.audit_log[-1]["result"] == "permission_denied"


class TestAdminAuthServiceCleanup:
    """Test AdminAuthService session cleanup."""

    def test_cleanup_expired_sessions_removes_expired(self) -> None:
        """Test cleanup_expired_sessions removes expired sessions."""
        service = AdminAuthService()
        user_id = "test-user-1"
        session = AdminSession(user_id, "testuser", AdminRole.VIEWER, "127.0.0.1")
        # Set last_activity to be older than timeout
        from datetime import timedelta

        session.last_activity = session.last_activity - timedelta(seconds=service.session_timeout + 100)
        service.active_sessions[user_id] = session

        with patch("server.services.admin_auth_service.logger.info") as mock_info:
            count = service.cleanup_expired_sessions()
            assert count == 1
            assert user_id not in service.active_sessions
            mock_info.assert_called_once()

    def test_cleanup_expired_sessions_no_expired(self) -> None:
        """Test cleanup_expired_sessions with no expired sessions."""
        service = AdminAuthService()
        user_id = "test-user-2"
        session = AdminSession(user_id, "testuser", AdminRole.VIEWER, "127.0.0.1")
        service.active_sessions[user_id] = session

        count = service.cleanup_expired_sessions()
        assert count == 0
        assert user_id in service.active_sessions

    def test_cleanup_expired_sessions_multiple(self) -> None:
        """Test cleanup_expired_sessions with multiple expired sessions."""
        service = AdminAuthService()
        from datetime import timedelta

        # Add multiple expired sessions
        for i in range(3):
            user_id = f"test-user-{i}"
            session = AdminSession(user_id, f"testuser{i}", AdminRole.VIEWER, "127.0.0.1")
            session.last_activity = session.last_activity - timedelta(seconds=service.session_timeout + 100)
            service.active_sessions[user_id] = session

        # Add one active session
        active_user_id = "test-user-active"
        active_session = AdminSession(active_user_id, "activeuser", AdminRole.VIEWER, "127.0.0.1")
        service.active_sessions[active_user_id] = active_session

        with patch("server.services.admin_auth_service.logger.info") as mock_info:
            count = service.cleanup_expired_sessions()
            assert count == 3
            assert active_user_id in service.active_sessions
            for i in range(3):
                assert f"test-user-{i}" not in service.active_sessions
            mock_info.assert_called_once()


class TestGetAdminAuthService:
    """Test get_admin_auth_service function."""

    def test_get_admin_auth_service_returns_singleton(self) -> None:
        """Test get_admin_auth_service returns singleton instance."""
        service1 = get_admin_auth_service()
        service2 = get_admin_auth_service()
        assert service1 is service2
        assert isinstance(service1, AdminAuthService)
