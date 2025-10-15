"""
Test JWT Authentication Flow

This module tests the complete JWT authentication flow from registration
to stats rolling to ensure the authentication system works end-to-end.
"""

import uuid

import pytest


class TestJWTAuthenticationFlow:
    """Test the complete JWT authentication flow."""

    # Use the test_client fixture from conftest.py instead of defining our own

    @pytest.mark.skip(reason="Database concurrency issue - needs investigation")
    def test_complete_authentication_flow(self, test_client):
        """Test the complete authentication flow: registration -> JWT -> stats rolling."""
        # Step 1: Register a new user
        unique_username = f"flow_test_{uuid.uuid4().hex[:8]}"

        register_response = test_client.post(
            "/auth/register", json={"username": unique_username, "password": "testpass123", "invite_code": "TEST123"}
        )

        assert register_response.status_code == 200
        register_data = register_response.json()
        assert "access_token" in register_data
        assert "user_id" in register_data
        assert register_data["token_type"] == "bearer"

        # Extract the JWT token
        token = register_data["access_token"]
        user_id = register_data["user_id"]

        # Step 2: Test the token with the test-auth endpoint
        auth_response = test_client.get("/test-auth", headers={"Authorization": f"Bearer {token}"})

        assert auth_response.status_code == 200
        auth_data = auth_response.json()
        assert auth_data["message"] == "Authentication successful"
        assert auth_data["user"]["username"] == unique_username
        assert auth_data["user"]["id"] == user_id

        # Step 3: Test the token with the stats rolling endpoint
        stats_response = test_client.post(
            "/players/roll-stats",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={"method": "3d6"},
        )

        assert stats_response.status_code == 200
        stats_data = stats_response.json()
        assert "stats" in stats_data
        assert "stat_summary" in stats_data
        assert "available_classes" in stats_data

        # Verify the stats structure
        stats = stats_data["stats"]
        assert "strength" in stats
        assert "dexterity" in stats
        assert "constitution" in stats
        assert "intelligence" in stats
        assert "wisdom" in stats
        assert "charisma" in stats

        # Verify stat values are within expected ranges (3d6 = 3-18)
        for stat_name in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            assert 3 <= stats[stat_name] <= 18

    def test_authentication_without_token_fails(self, test_client):
        """Test that stats rolling fails without authentication token."""
        stats_response = test_client.post(
            "/players/roll-stats", headers={"Content-Type": "application/json"}, json={"method": "3d6"}
        )

        assert stats_response.status_code == 401
        error_data = stats_response.json()
        assert "error" in error_data

    def test_authentication_with_invalid_token_fails(self, test_client):
        """Test that stats rolling fails with invalid authentication token."""
        stats_response = test_client.post(
            "/players/roll-stats",
            headers={"Authorization": "Bearer invalid-token", "Content-Type": "application/json"},
            json={"method": "3d6"},
        )

        assert stats_response.status_code == 401
        error_data = stats_response.json()
        assert "error" in error_data

    @pytest.mark.skip(reason="Database concurrency issue - needs investigation")
    def test_login_flow_works(self, test_client):
        """Test that login works and generates valid JWT tokens."""
        # First register a user
        unique_username = f"login_test_{uuid.uuid4().hex[:8]}"

        register_response = test_client.post(
            "/auth/register", json={"username": unique_username, "password": "testpass123", "invite_code": "TEST123"}
        )

        assert register_response.status_code == 200

        # Then login with the same credentials
        login_response = test_client.post("/auth/login", json={"username": unique_username, "password": "testpass123"})

        assert login_response.status_code == 200
        login_data = login_response.json()
        assert "access_token" in login_data
        assert "user_id" in login_data
        assert login_data["token_type"] == "bearer"

        # Test the login token with stats rolling
        token = login_data["access_token"]
        stats_response = test_client.post(
            "/players/roll-stats",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={"method": "3d6"},
        )

        assert stats_response.status_code == 200
