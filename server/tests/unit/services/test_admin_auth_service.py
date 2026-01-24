"""
Unit tests for admin authentication service.

Tests the AdminAuthService class for admin authentication and authorization.
"""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException, Request

from server.models.user import User
from server.services.admin_auth_service import (
    AdminAction,
    AdminAuthService,
    AdminRole,
    AdminSession,
    get_admin_auth_service,
)


@pytest.fixture
def admin_auth_service():
    """Create an AdminAuthService instance."""
    return AdminAuthService()


@pytest.fixture
def mock_user():
    """Create a mock user object."""
    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    return user


@pytest.fixture
def superuser():
    """Create a superuser object."""
    user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )
    return user


def test_admin_role_enum():
    """Test AdminRole enum values."""
    assert AdminRole.SUPERUSER.value == "superuser"
    assert AdminRole.ADMIN.value == "admin"
    assert AdminRole.MODERATOR.value == "moderator"
    assert AdminRole.VIEWER.value == "viewer"


def test_admin_action_enum():
    """Test AdminAction enum values."""
    assert AdminAction.CREATE_NPC_DEFINITION.value == "create_npc_definition"
    assert AdminAction.SPAWN_NPC.value == "spawn_npc"
    assert AdminAction.GET_POPULATION_STATS.value == "get_population_stats"


def test_admin_session_init():
    """Test AdminSession initialization."""
    session = AdminSession("user123", "testuser", AdminRole.ADMIN, "127.0.0.1")

    assert session.user_id == "user123"
    assert session.username == "testuser"
    assert session.role == AdminRole.ADMIN
    assert session.ip_address == "127.0.0.1"
    assert session.action_count == 0
    assert session.is_active is True
    assert isinstance(session.created_at, datetime)
    assert isinstance(session.last_activity, datetime)


def test_admin_auth_service_init(admin_auth_service):
    """Test AdminAuthService initialization."""
    assert admin_auth_service.active_sessions == {}
    assert admin_auth_service.audit_log == []
    assert admin_auth_service.rate_limits == {}
    assert admin_auth_service.rate_limit_window == 300
    assert admin_auth_service.rate_limit_max_requests == 100
    assert admin_auth_service.session_timeout == 3600


def test_get_user_role_superuser(admin_auth_service, superuser):
    """Test get_user_role returns SUPERUSER for superuser."""
    role = admin_auth_service.get_user_role(superuser)
    assert role == AdminRole.SUPERUSER


def test_get_user_role_viewer(admin_auth_service, mock_user):
    """Test get_user_role returns VIEWER for regular user."""
    role = admin_auth_service.get_user_role(mock_user)
    assert role == AdminRole.VIEWER


def test_get_user_role_none(admin_auth_service):
    """Test get_user_role raises for None user."""
    with pytest.raises(HTTPException, match="Authentication required"):
        admin_auth_service.get_user_role(None)


def test_get_user_role_with_is_admin_attribute(admin_auth_service):
    """Test get_user_role returns ADMIN for user with is_admin attribute."""
    user = MagicMock()
    user.is_superuser = False
    user.is_admin = True

    role = admin_auth_service.get_user_role(user)
    assert role == AdminRole.ADMIN


def test_get_user_role_with_dict_is_admin(admin_auth_service):
    """Test get_user_role returns ADMIN for dict user with is_admin."""
    user_dict = {"is_admin": True, "is_superuser": False}

    role = admin_auth_service.get_user_role(user_dict)
    assert role == AdminRole.ADMIN


def test_get_username_from_user_object(admin_auth_service, mock_user):
    """Test get_username from User object."""
    username = admin_auth_service.get_username(mock_user)
    assert username == "testuser"


def test_get_username_from_dict(admin_auth_service):
    """Test get_username from dict."""
    user_dict = {"username": "dictuser"}
    username = admin_auth_service.get_username(user_dict)
    assert username == "dictuser"


def test_get_username_none(admin_auth_service):
    """Test get_username returns 'unknown' for None."""
    username = admin_auth_service.get_username(None)
    assert username == "unknown"


def test_get_username_missing_attribute(admin_auth_service):
    """Test get_username returns 'unknown' when username missing."""

    # Create a simple object that doesn't have username or get method
    class UserWithoutUsername:
        pass

    user = UserWithoutUsername()
    # hasattr will return False for both username and get
    username = admin_auth_service.get_username(user)
    assert username == "unknown"


def test_get_username_dict_without_username(admin_auth_service):
    """Test get_username returns 'unknown' when dict doesn't have username."""
    user_dict = {"id": "123"}  # No username key
    username = admin_auth_service.get_username(user_dict)
    assert username == "unknown"


def test_get_user_id_from_user_object(admin_auth_service, mock_user):
    """Test get_user_id from User object."""
    user_id = admin_auth_service.get_user_id(mock_user)
    assert user_id == str(mock_user.id)


def test_get_user_id_from_dict(admin_auth_service):
    """Test get_user_id from dict."""
    user_id_val = str(uuid.uuid4())
    user_dict = {"id": user_id_val}
    user_id = admin_auth_service.get_user_id(user_dict)
    assert user_id == user_id_val


def test_get_user_id_none(admin_auth_service):
    """Test get_user_id returns 'unknown' for None."""
    user_id = admin_auth_service.get_user_id(None)
    assert user_id == "unknown"


def test_validate_permission_superuser_all_actions(admin_auth_service, superuser):
    """Test validate_permission allows superuser all actions."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"

    # Superuser should have permission for all actions
    for action in AdminAction:
        # Should not raise
        admin_auth_service.validate_permission(superuser, action, request)


def test_validate_permission_viewer_limited(admin_auth_service, mock_user):
    """Test validate_permission limits viewer role."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"

    # Viewer should have permission for read-only actions
    admin_auth_service.validate_permission(mock_user, AdminAction.LIST_NPC_DEFINITIONS, request)
    admin_auth_service.validate_permission(mock_user, AdminAction.GET_POPULATION_STATS, request)

    # Viewer should NOT have permission for write actions
    with pytest.raises(HTTPException, match="Permission denied"):
        admin_auth_service.validate_permission(mock_user, AdminAction.CREATE_NPC_DEFINITION, request)


def test_validate_permission_none_user(admin_auth_service):
    """Test validate_permission raises for None user."""
    request = MagicMock(spec=Request)

    with pytest.raises(HTTPException, match="Authentication required"):
        admin_auth_service.validate_permission(None, AdminAction.LIST_NPC_DEFINITIONS, request)


def test_validate_permission_rate_limit_exceeded(admin_auth_service, superuser):
    """Test validate_permission enforces rate limiting."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"

    user_id = str(superuser.id)

    # Fill up rate limit
    import time

    now = time.time()
    admin_auth_service.rate_limits[user_id] = [now] * admin_auth_service.rate_limit_max_requests

    with pytest.raises(HTTPException, match="Rate limit exceeded"):
        admin_auth_service.validate_permission(superuser, AdminAction.LIST_NPC_DEFINITIONS, request)


def test_has_permission_superuser(admin_auth_service):
    """Test _has_permission for superuser."""
    for action in AdminAction:
        assert admin_auth_service._has_permission(AdminRole.SUPERUSER, action) is True


def test_has_permission_admin(admin_auth_service):
    """Test _has_permission for admin role."""
    assert admin_auth_service._has_permission(AdminRole.ADMIN, AdminAction.CREATE_NPC_DEFINITION) is True
    assert admin_auth_service._has_permission(AdminRole.ADMIN, AdminAction.SPAWN_NPC) is True
    assert admin_auth_service._has_permission(AdminRole.ADMIN, AdminAction.LIST_NPC_DEFINITIONS) is True


def test_has_permission_moderator(admin_auth_service):
    """Test _has_permission for moderator role."""
    assert admin_auth_service._has_permission(AdminRole.MODERATOR, AdminAction.LIST_NPC_DEFINITIONS) is True
    assert admin_auth_service._has_permission(AdminRole.MODERATOR, AdminAction.GET_POPULATION_STATS) is True
    assert admin_auth_service._has_permission(AdminRole.MODERATOR, AdminAction.CREATE_NPC_DEFINITION) is False


def test_has_permission_viewer(admin_auth_service):
    """Test _has_permission for viewer role."""
    assert admin_auth_service._has_permission(AdminRole.VIEWER, AdminAction.LIST_NPC_DEFINITIONS) is True
    assert admin_auth_service._has_permission(AdminRole.VIEWER, AdminAction.GET_POPULATION_STATS) is True
    assert admin_auth_service._has_permission(AdminRole.VIEWER, AdminAction.CREATE_NPC_DEFINITION) is False


def test_check_rate_limit_cleanup_old_entries(admin_auth_service):
    """Test _check_rate_limit cleans up old entries."""
    import time

    user_id = "test_user"
    now = time.time()

    # Add old entries (outside window)
    admin_auth_service.rate_limits[user_id] = [now - 400, now - 350]  # Outside 300s window

    # Should not raise (old entries cleaned)
    admin_auth_service._check_rate_limit(user_id, None)

    # Should have cleaned old entries and added new one
    # After cleanup, only entries within window remain, plus the new one added
    assert len(admin_auth_service.rate_limits[user_id]) == 1  # Only new entry


def test_check_rate_limit_adds_request(admin_auth_service):
    """Test _check_rate_limit adds current request."""
    user_id = "test_user"

    admin_auth_service._check_rate_limit(user_id, None)

    assert len(admin_auth_service.rate_limits[user_id]) == 1


def test_update_session_creates_new(admin_auth_service):
    """Test _update_session creates new session."""
    from starlette.requests import Request as StarletteRequest

    # Create a proper request-like object
    scope = {"type": "http", "client": ("127.0.0.1", 12345)}
    request = StarletteRequest(scope)

    admin_auth_service._update_session("user123", "testuser", AdminRole.ADMIN, request)

    assert "user123" in admin_auth_service.active_sessions
    session = admin_auth_service.active_sessions["user123"]
    assert session.username == "testuser"
    assert session.role == AdminRole.ADMIN
    assert session.ip_address == "127.0.0.1"


def test_update_session_updates_existing(admin_auth_service):
    """Test _update_session updates existing session."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"

    admin_auth_service._update_session("user123", "testuser", AdminRole.ADMIN, request)
    initial_count = admin_auth_service.active_sessions["user123"].action_count

    admin_auth_service._update_session("user123", "testuser", AdminRole.ADMIN, request)

    assert admin_auth_service.active_sessions["user123"].action_count == initial_count + 1


def test_update_session_no_request(admin_auth_service):
    """Test _update_session handles None request."""
    admin_auth_service._update_session("user123", "testuser", AdminRole.ADMIN, None)

    session = admin_auth_service.active_sessions["user123"]
    assert session.ip_address == "unknown"


def test_log_audit_event(admin_auth_service):
    """Test _log_audit_event logs event."""
    from starlette.datastructures import Headers
    from starlette.requests import Request as StarletteRequest

    # Create a proper request-like object
    scope = {"type": "http", "client": ("127.0.0.1", 12345)}
    request = StarletteRequest(scope)
    request._headers = Headers({"user-agent": "test-agent"})

    admin_auth_service._log_audit_event("user123", "testuser", AdminAction.CREATE_NPC_DEFINITION, "success", request)

    assert len(admin_auth_service.audit_log) == 1
    event = admin_auth_service.audit_log[0]
    assert event["user_id"] == "user123"
    assert event["username"] == "testuser"
    assert event["action"] == "create_npc_definition"
    assert event["result"] == "success"
    assert event["ip_address"] == "127.0.0.1"
    assert event["user_agent"] == "test-agent"


def test_log_audit_event_no_request(admin_auth_service):
    """Test _log_audit_event handles None request."""
    admin_auth_service._log_audit_event("user123", "testuser", AdminAction.CREATE_NPC_DEFINITION, "success", None)

    event = admin_auth_service.audit_log[0]
    assert event["ip_address"] == "unknown"
    assert event["user_agent"] == "unknown"


def test_log_audit_event_limits_size(admin_auth_service):
    """Test _log_audit_event limits log size to 1000."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"
    request.headers = {"User-Agent": "test-agent"}

    # Add 1001 events
    for i in range(1001):
        admin_auth_service._log_audit_event(
            f"user{i}", "testuser", AdminAction.CREATE_NPC_DEFINITION, "success", request
        )

    # Should only keep last 1000
    assert len(admin_auth_service.audit_log) == 1000


def test_get_active_sessions(admin_auth_service):
    """Test get_active_sessions returns active sessions."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"

    admin_auth_service._update_session("user123", "testuser", AdminRole.ADMIN, request)

    sessions = admin_auth_service.get_active_sessions()

    assert len(sessions) == 1
    assert sessions[0]["user_id"] == "user123"
    assert sessions[0]["username"] == "testuser"
    assert sessions[0]["role"] == "admin"


def test_get_active_sessions_filters_expired(admin_auth_service):
    """Test get_active_sessions filters expired sessions."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"

    admin_auth_service._update_session("user123", "testuser", AdminRole.ADMIN, request)

    # Make session expired
    session = admin_auth_service.active_sessions["user123"]
    session.last_activity = datetime.now(UTC) - timedelta(seconds=admin_auth_service.session_timeout + 100)

    sessions = admin_auth_service.get_active_sessions()

    assert len(sessions) == 0
    assert admin_auth_service.active_sessions["user123"].is_active is False


def test_get_audit_log(admin_auth_service):
    """Test get_audit_log returns audit entries."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"
    request.headers = {"User-Agent": "test-agent"}

    for i in range(5):
        admin_auth_service._log_audit_event(
            f"user{i}", "testuser", AdminAction.CREATE_NPC_DEFINITION, "success", request
        )

    log = admin_auth_service.get_audit_log(limit=3)

    assert len(log) == 3
    # Should return last 3 entries
    assert log[0]["user_id"] == "user2"
    assert log[2]["user_id"] == "user4"


def test_get_audit_log_no_limit(admin_auth_service):
    """Test get_audit_log with limit=0 returns all entries."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"
    request.headers = {"User-Agent": "test-agent"}

    for i in range(5):
        admin_auth_service._log_audit_event(
            f"user{i}", "testuser", AdminAction.CREATE_NPC_DEFINITION, "success", request
        )

    log = admin_auth_service.get_audit_log(limit=0)

    assert len(log) == 5


def test_cleanup_expired_sessions(admin_auth_service):
    """Test cleanup_expired_sessions removes expired sessions."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"

    admin_auth_service._update_session("user123", "testuser", AdminRole.ADMIN, request)
    admin_auth_service._update_session("user456", "testuser2", AdminRole.ADMIN, request)

    # Make one session expired
    session = admin_auth_service.active_sessions["user123"]
    session.last_activity = datetime.now(UTC) - timedelta(seconds=admin_auth_service.session_timeout + 100)

    count = admin_auth_service.cleanup_expired_sessions()

    assert count == 1
    assert "user123" not in admin_auth_service.active_sessions
    assert "user456" in admin_auth_service.active_sessions


def test_cleanup_expired_sessions_no_expired(admin_auth_service):
    """Test cleanup_expired_sessions with no expired sessions."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"

    admin_auth_service._update_session("user123", "testuser", AdminRole.ADMIN, request)

    count = admin_auth_service.cleanup_expired_sessions()

    assert count == 0
    assert "user123" in admin_auth_service.active_sessions


def test_get_admin_auth_service():
    """Test get_admin_auth_service returns global instance."""
    service = get_admin_auth_service()
    assert isinstance(service, AdminAuthService)


def test_validate_permission_logs_audit(admin_auth_service, superuser):
    """Test validate_permission logs audit events."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"
    request.headers = {"User-Agent": "test-agent"}

    admin_auth_service.validate_permission(superuser, AdminAction.CREATE_NPC_DEFINITION, request)

    assert len(admin_auth_service.audit_log) == 1
    assert admin_auth_service.audit_log[0]["result"] == "success"


def test_validate_permission_logs_permission_denied(admin_auth_service, mock_user):
    """Test validate_permission logs permission denied."""
    request = MagicMock(spec=Request)
    request.client = MagicMock()
    request.client.host = "127.0.0.1"
    request.headers = {"User-Agent": "test-agent"}

    with pytest.raises(HTTPException):
        admin_auth_service.validate_permission(mock_user, AdminAction.CREATE_NPC_DEFINITION, request)

    assert len(admin_auth_service.audit_log) == 1
    assert admin_auth_service.audit_log[0]["result"] == "permission_denied"
