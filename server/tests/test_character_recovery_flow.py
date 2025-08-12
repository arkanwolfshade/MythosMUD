"""
Test Character Recovery Flow

This module tests the flow for users who registered but got disconnected
before completing character creation.
"""

import uuid

import pytest
from fastapi.testclient import TestClient

from server.main import app


class TestCharacterRecoveryFlow:
    """Test the character recovery flow for disconnected users."""

    @pytest.fixture
    def test_client(self):
        """Create a test client for the FastAPI app."""
        return TestClient(app)

    def test_user_without_character_goes_to_stats_rolling(self, test_client):
        """Test that a user without a character is directed to stats rolling."""
        # Step 1: Register a new user
        unique_username = f"recovery_test_{uuid.uuid4().hex[:8]}"

        register_response = test_client.post(
            "/auth/register", json={"username": unique_username, "password": "testpass123", "invite_code": "TEST123"}
        )

        assert register_response.status_code == 200
        register_data = register_response.json()
        assert "access_token" in register_data
        assert "user_id" in register_data
        assert not register_data["has_character"]
        assert register_data["character_name"] is None

        # Step 2: Login with the same user (simulating reconnection)
        login_response = test_client.post("/auth/login", json={"username": unique_username, "password": "testpass123"})

        assert login_response.status_code == 200
        login_data = login_response.json()
        assert "access_token" in login_data
        assert "user_id" in login_data
        assert not login_data["has_character"]
        assert login_data["character_name"] is None

        # Step 3: Verify the user can roll stats (indicating they're in stats rolling flow)
        token = login_data["access_token"]
        stats_response = test_client.post(
            "/players/roll-stats",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={"method": "3d6"},
        )

        assert stats_response.status_code == 200
        stats_data = stats_response.json()
        assert "stats" in stats_data

    def test_user_with_character_goes_to_game(self, test_client):
        """Test that a user with a character goes directly to the game."""
        # Step 1: Register a user
        unique_username = f"game_test_{uuid.uuid4().hex[:8]}"

        register_response = test_client.post(
            "/auth/register", json={"username": unique_username, "password": "testpass123", "invite_code": "TEST123"}
        )

        assert register_response.status_code == 200
        register_data = register_response.json()
        token = register_data["access_token"]

        # Step 2: Roll stats
        stats_response = test_client.post(
            "/players/roll-stats",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={"method": "3d6"},
        )

        assert stats_response.status_code == 200
        stats_data = stats_response.json()
        stats = stats_data["stats"]

        # Step 3: Create character
        create_response = test_client.post(
            "/players/create-character",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={"name": unique_username, "stats": stats},
        )

        assert create_response.status_code == 200

        # Step 4: Login again (simulating reconnection after character creation)
        login_response = test_client.post("/auth/login", json={"username": unique_username, "password": "testpass123"})

        assert login_response.status_code == 200
        login_data = login_response.json()
        assert "access_token" in login_data
        assert "user_id" in login_data
        assert login_data["has_character"]
        assert login_data["character_name"] == unique_username

    def test_registration_returns_no_character(self, test_client):
        """Test that registration always returns has_character=False."""
        unique_username = f"reg_test_{uuid.uuid4().hex[:8]}"

        register_response = test_client.post(
            "/auth/register", json={"username": unique_username, "password": "testpass123", "invite_code": "TEST123"}
        )

        assert register_response.status_code == 200
        register_data = register_response.json()
        assert not register_data["has_character"]
        assert register_data["character_name"] is None
