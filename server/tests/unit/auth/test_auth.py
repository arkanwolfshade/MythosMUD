"""
Tests for authentication endpoints.

This module tests the authentication system including registration,
login, and user management endpoints.

ARCHITECTURE FIX: Updated to use container_test_client fixture
Following pytest best practices for API endpoint testing.
"""

import uuid
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.auth.endpoints import LoginRequest, LoginResponse, UserCreate
from server.exceptions import LoggedHTTPException
from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@pytest.fixture
def mock_auth_persistence(container_test_client):
    """
    Mock persistence for auth testing.

    AI: Reuses container_test_client following pytest best practices
    """
    app = container_test_client.app
    mock_persistence = AsyncMock()

    # Configure mock behaviors for auth operations
    mock_persistence.async_get_user_by_username = AsyncMock(return_value=None)
    mock_persistence.async_get_user_by_email = AsyncMock(return_value=None)
    mock_persistence.async_create_user = AsyncMock(return_value=None)

    # Replace container persistence
    app.state.container.persistence = mock_persistence
    app.state.persistence = mock_persistence

    # Update service persistence
    if hasattr(app.state.container, "player_service") and app.state.container.player_service:
        app.state.container.player_service.persistence = mock_persistence

    if hasattr(app.state.container, "room_service") and app.state.container.room_service:
        app.state.container.room_service.persistence = mock_persistence

    return mock_persistence


class TestSchemaValidation:
    """Test Pydantic schema validation."""

    def test_user_create_schema(self):
        """Test UserCreate schema validation."""
        # Test with all fields
        user_data = {
            "username": "testuser",
            "password": "testpass123",
            "email": "test@example.com",
            "invite_code": "TEST123",
        }
        user_create = UserCreate(**user_data)
        assert user_create.username == "testuser"
        assert user_create.password == "testpass123"
        assert user_create.email == "test@example.com"
        assert user_create.invite_code == "TEST123"

    def test_user_create_schema_optional_fields(self):
        """Test UserCreate schema with optional fields."""
        # Test without email and invite_code
        user_data = {"username": "testuser", "password": "testpass123"}
        user_create = UserCreate(**user_data)
        assert user_create.username == "testuser"
        assert user_create.password == "testpass123"
        assert user_create.email is None
        assert user_create.invite_code is None

    def test_login_request_schema(self):
        """Test LoginRequest schema validation."""
        login_data = {"username": "testuser", "password": "testpass123"}
        login_request = LoginRequest(**login_data)
        assert login_request.username == "testuser"
        assert login_request.password == "testpass123"

    def test_login_response_schema(self):
        """Test LoginResponse schema validation."""
        response_data = {"access_token": "test-token", "token_type": "bearer", "user_id": "test-user-id"}
        login_response = LoginResponse(**response_data)
        assert login_response.access_token == "test-token"
        assert login_response.token_type == "bearer"
        assert login_response.user_id == "test-user-id"

    def test_login_response_schema_default_token_type(self):
        """Test LoginResponse schema with default token type."""
        response_data = {"access_token": "test-token", "user_id": "test-user-id"}
        login_response = LoginResponse(**response_data)
        assert login_response.access_token == "test-token"
        assert login_response.token_type == "bearer"  # Default value
        assert login_response.user_id == "test-user-id"


class TestRegistrationEndpoints:
    """Test registration endpoint functionality."""

    def test_successful_registration(self, container_test_client, mock_auth_persistence):
        """Test successful user registration with real database (isolated test)."""
        # This test uses the real database but is designed to be isolated
        # The test database should have the TEST123 invite already inserted

        # Use a unique username to avoid conflicts with previous test runs
        import uuid

        unique_username = f"newuser_{uuid.uuid4().hex[:8]}"

        # Test registration
        response = container_test_client.post(
            "/auth/register",
            json={"username": unique_username, "password": "testpass123", "invite_code": "TEST123"},
        )

        # Verify the response
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "user_id" in data
        assert data["token_type"] == "bearer"

    @patch("server.auth.endpoints.get_invite_manager")
    def test_registration_invalid_invite_code(self, mock_get_invite, container_test_client, mock_auth_persistence):
        """Test registration with invalid invite code."""
        mock_manager = AsyncMock()
        mock_manager.validate_invite.side_effect = LoggedHTTPException(status_code=400, detail="Invalid invite code")
        mock_get_invite.return_value = mock_manager

        response = container_test_client.post(
            "/auth/register", json={"username": "newuser", "password": "testpass123", "invite_code": "INVALID"}
        )

        assert response.status_code == 400
        assert "Invalid invite code" in response.json()["error"]["message"]

    def test_registration_duplicate_username(self, container_test_client, mock_auth_persistence):
        """Test registration with duplicate username."""
        import uuid

        # Use a unique username to avoid conflicts with other tests
        unique_username = f"duplicate_test_{uuid.uuid4().hex[:8]}"

        # First, register a user to create the duplicate condition
        first_response = container_test_client.post(
            "/auth/register", json={"username": unique_username, "password": "testpass123", "invite_code": "TEST456"}
        )

        # The first registration should succeed
        assert first_response.status_code == 200

        # Now try to register with the same username
        response = container_test_client.post(
            "/auth/register", json={"username": unique_username, "password": "testpass123", "invite_code": "TEST456"}
        )

        # Debug output
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        assert response.status_code == 400
        assert "Username already exists" in response.json()["error"]["message"]

    def test_registration_with_empty_password(self, container_test_client, mock_auth_persistence):
        """Test registration with empty password should be rejected for security."""
        # Use a unique username to avoid conflicts
        import uuid

        unique_username = f"weakuser_{uuid.uuid4().hex[:8]}"

        # Test with an empty password which should fail validation
        response = container_test_client.post(
            "/auth/register", json={"username": unique_username, "password": "", "invite_code": "TEST456"}
        )

        # Debug: Print response details
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Empty passwords should be rejected for security
        assert response.status_code == 422  # Unprocessable Entity for validation errors
        data = response.json()
        assert "detail" in data
        # The error message should indicate password validation failure
        # For validation errors, detail is a list of error objects
        error_detail = data["detail"]
        assert isinstance(error_detail, list)
        assert len(error_detail) > 0
        # Check that the error message contains password-related keywords
        error_msg = error_detail[0].get("msg", "").lower()
        assert any(keyword in error_msg for keyword in ["password", "empty"])

    def test_registration_with_whitespace_password(self, container_test_client, mock_auth_persistence):
        """Test registration with whitespace-only password should be rejected."""
        # Use a unique username to avoid conflicts
        import uuid

        unique_username = f"whitespaceuser_{uuid.uuid4().hex[:8]}"

        # Test with a whitespace-only password which should fail validation
        response = container_test_client.post(
            "/auth/register", json={"username": unique_username, "password": "   ", "invite_code": "TEST456"}
        )

        # Debug: Print response details
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Whitespace-only passwords should be rejected for security
        assert response.status_code == 422  # Unprocessable Entity for validation errors
        data = response.json()
        assert "detail" in data
        # For validation errors, detail is a list of error objects
        error_detail = data["detail"]
        assert isinstance(error_detail, list)
        assert len(error_detail) > 0
        # Check that the error message contains password-related keywords
        error_msg = error_detail[0].get("msg", "").lower()
        assert any(keyword in error_msg for keyword in ["password", "empty"])


class TestLoginEndpoints:
    """Test login endpoint functionality."""

    def test_successful_login(self, container_test_client, mock_auth_persistence):
        """Test successful login with valid credentials."""
        # Create mock user
        mock_user = MagicMock()
        mock_user.id = uuid.uuid4()  # FastAPI Users v14 uses 'id' instead of 'user_id'
        mock_user.email = "testuser@wolfshade.org"
        mock_user.username = "testuser"

        # Create mock session with proper user lookup
        mock_session = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_user
        mock_session.execute.return_value = mock_result

        # Create mock user manager
        mock_manager = AsyncMock()
        mock_manager.authenticate.return_value = mock_user

        # Override the dependencies at the app level
        from server.auth.endpoints import get_async_session, get_user_manager

        async def mock_get_async_session():
            return mock_session

        async def mock_get_user_manager():
            return mock_manager

        # Override the dependencies in the app
        container_test_client.app.dependency_overrides[get_async_session] = mock_get_async_session
        container_test_client.app.dependency_overrides[get_user_manager] = mock_get_user_manager

        try:
            response = container_test_client.post(
                "/auth/login", json={"username": "testuser", "password": "testpass123"}
            )

            assert response.status_code == 200
            data = response.json()
            assert "access_token" in data
            assert "user_id" in data  # This is the response field name, not the model property
            assert data["token_type"] == "bearer"
        finally:
            # Clean up the override
            container_test_client.app.dependency_overrides.clear()

    @patch("server.auth.endpoints.get_async_session")
    def test_login_user_not_found(self, mock_get_session, container_test_client, mock_auth_persistence):
        """Test login with nonexistent user."""
        mock_session = AsyncMock()
        mock_get_session.return_value = mock_session

        # Mock empty user lookup
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        response = container_test_client.post(
            "/auth/login", json={"username": "nonexistent", "password": "testpass123"}
        )

        assert response.status_code == 401
        assert "Invalid credentials" in response.json()["error"]["message"]

    @patch("server.auth.endpoints.get_async_session")
    def test_login_user_no_email(self, mock_get_session, container_test_client, mock_auth_persistence):
        """Test login with user that has no email."""
        mock_session = AsyncMock()
        mock_get_session.return_value = mock_session

        # Mock user lookup with no email
        mock_user = MagicMock()
        mock_user.id = uuid.uuid4()  # FastAPI Users v14 uses 'id' instead of 'user_id'
        mock_user.email = None
        mock_user.username = "testuser"

        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_user
        mock_session.execute.return_value = mock_result

        response = container_test_client.post("/auth/login", json={"username": "testuser", "password": "testpass123"})

        assert response.status_code == 401
        assert "Invalid credentials" in response.json()["error"]["message"]


class TestUserInfoEndpoints:
    """Test user information endpoint functionality."""

    @patch("server.auth.endpoints.get_current_active_user")
    def test_get_current_user_info_superuser(self, mock_get_current, container_test_client, mock_auth_persistence):
        """Test /auth/me endpoint with superuser."""
        mock_user = MagicMock()
        mock_user.id = uuid.uuid4()  # FastAPI Users v14 uses 'id' instead of 'user_id'
        mock_user.email = "admin@wolfshade.org"
        mock_user.username = "admin"
        mock_user.is_superuser = True

        # Override the dependency at the app level
        from server.auth.dependencies import get_current_active_user

        async def mock_get_current_active_user():
            return mock_user

        # Override the dependency in the app
        container_test_client.app.dependency_overrides[get_current_active_user] = mock_get_current_active_user

        try:
            response = container_test_client.get("/auth/me")

            assert response.status_code == 200
            data = response.json()
            assert data["id"] == str(mock_user.id)  # Use 'id' instead of 'user_id'
            assert data["email"] == mock_user.email
            assert data["username"] == mock_user.username
            assert data["is_superuser"] is True
        finally:
            # Clean up the override
            container_test_client.app.dependency_overrides.clear()

    @patch("server.auth.endpoints.get_current_active_user")
    def test_get_current_user_info_regular_user(self, mock_get_current, container_test_client, mock_auth_persistence):
        """Test /auth/me endpoint with regular user."""
        mock_user = MagicMock()
        mock_user.id = uuid.uuid4()  # FastAPI Users v14 uses 'id' instead of 'user_id'
        mock_user.email = "user@wolfshade.org"
        mock_user.username = "user"
        mock_user.is_superuser = False

        # Override the dependency at the app level
        from server.auth.dependencies import get_current_active_user

        async def mock_get_current_active_user():
            return mock_user

        # Override the dependency in the app
        container_test_client.app.dependency_overrides[get_current_active_user] = mock_get_current_active_user

        try:
            response = container_test_client.get("/auth/me")

            assert response.status_code == 200
            data = response.json()
            assert data["id"] == str(mock_user.id)  # Use 'id' instead of 'user_id'
            assert data["email"] == mock_user.email
            assert data["username"] == mock_user.username
            assert data["is_superuser"] is False
        finally:
            # Clean up the override
            container_test_client.app.dependency_overrides.clear()


class TestInviteManagementEndpoints:
    """Test invite management endpoint functionality."""

    @patch("server.auth.endpoints.get_current_superuser")
    @patch("server.auth.endpoints.get_invite_manager")
    def test_list_invites(self, mock_get_invite, mock_get_current, container_test_client, mock_auth_persistence):
        """Test listing all invite codes."""
        mock_user = MagicMock()
        mock_user.is_superuser = True
        mock_get_current.return_value = mock_user

        # Create mock invites with proper UUIDs and data types
        mock_invite1 = MagicMock()
        mock_invite1.id = str(uuid.uuid4())
        mock_invite1.invite_code = "TEST123"
        mock_invite1.is_used = False
        mock_invite1.used_by_user_id = None  # Not used yet
        mock_invite1.created_at = datetime.now(UTC)
        mock_invite1.expires_at = datetime.now(UTC) + timedelta(days=30)

        mock_invite2 = MagicMock()
        mock_invite2.id = str(uuid.uuid4())
        mock_invite2.invite_code = "TEST456"
        mock_invite2.is_used = False
        mock_invite2.used_by_user_id = None  # Not used yet
        mock_invite2.created_at = datetime.now(UTC)
        mock_invite2.expires_at = datetime.now(UTC) + timedelta(days=30)

        mock_manager = AsyncMock()
        mock_manager.list_invites.return_value = [mock_invite1, mock_invite2]
        mock_get_invite.return_value = mock_manager

        # Override the dependency at the app level
        from server.auth.dependencies import get_current_superuser
        from server.auth.invites import get_invite_manager

        # Create a mock dependency that returns our mock user
        async def mock_get_current_superuser():
            return mock_user

        async def mock_get_invite_manager():
            return mock_manager

        # Override the dependencies in the app
        container_test_client.app.dependency_overrides[get_current_superuser] = mock_get_current_superuser
        container_test_client.app.dependency_overrides[get_invite_manager] = mock_get_invite_manager

        try:
            response = container_test_client.get("/auth/invites")

            assert response.status_code == 200
            data = response.json()
            assert len(data) == 2
            assert data[0]["invite_code"] == "TEST123"
            assert data[1]["invite_code"] == "TEST456"
        finally:
            # Clean up the override
            container_test_client.app.dependency_overrides.clear()

    @patch("server.auth.endpoints.get_current_superuser")
    @patch("server.auth.endpoints.get_invite_manager")
    def test_create_invite(self, mock_get_invite, mock_get_current, container_test_client, mock_auth_persistence):
        """Test creating a new invite code."""
        mock_user = MagicMock()
        mock_user.is_superuser = True
        mock_get_current.return_value = mock_user

        # Create a mock invite with a specific code and proper data types
        mock_invite = MagicMock()
        mock_invite.id = str(uuid.uuid4())
        mock_invite.invite_code = "NEW123"
        mock_invite.is_used = False
        mock_invite.used_by_user_id = None  # Not used yet
        mock_invite.created_at = datetime.now(UTC)
        mock_invite.expires_at = datetime.now(UTC) + timedelta(days=30)

        mock_manager = AsyncMock()
        mock_manager.create_invite.return_value = mock_invite
        mock_get_invite.return_value = mock_manager

        # Override the dependency at the app level
        from server.auth.dependencies import get_current_superuser
        from server.auth.invites import get_invite_manager

        # Create a mock dependency that returns our mock user
        async def mock_get_current_superuser():
            return mock_user

        async def mock_get_invite_manager():
            return mock_manager

        # Override the dependencies in the app
        container_test_client.app.dependency_overrides[get_current_superuser] = mock_get_current_superuser
        container_test_client.app.dependency_overrides[get_invite_manager] = mock_get_invite_manager

        try:
            response = container_test_client.post("/auth/invites")

            assert response.status_code == 200
            data = response.json()
            assert data["invite_code"] == "NEW123"
        finally:
            # Clean up the override
            container_test_client.app.dependency_overrides.clear()

    def test_database_connection(self, container_test_client, mock_auth_persistence):
        """Test that the database connection and invite table work."""
        import sqlite3

        # Check if we can access the test database
        # Use absolute path for test database (correct path in data/unit_test)
        # Path: server/tests/unit/auth/test_auth.py -> server/tests/unit/auth -> server/tests/unit -> server/tests -> server -> project root
        project_root = Path(__file__).parent.parent.parent.parent.parent
        db_path = project_root / "data" / "unit_test" / "players" / "unit_test_players.db"
        with sqlite3.connect(db_path) as conn:
            cursor = conn.execute("SELECT COUNT(*) FROM invites")
            count = cursor.fetchone()[0]
            assert count >= 0  # Should have at least 0 invites

            # Check if TEST123 invite exists
            cursor = conn.execute("SELECT * FROM invites WHERE invite_code = 'TEST123'")
            invite = cursor.fetchone()
            assert invite is not None, "TEST123 invite should exist in test database"
