"""
Tests for main.py module.

Tests the FastAPI application, endpoints, logging setup, and game tick functionality.
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket

# Import the app directly to avoid import issues
from ..main import app


class TestFastAPIApp:
    """Test FastAPI application setup."""

    def test_app_creation(self):
        """Test that the FastAPI app is created correctly."""
        assert isinstance(app, FastAPI)
        assert app.title == "MythosMUD API"
        assert app.version == "0.1.0"

    def test_app_has_cors_middleware(self):
        """Test that CORS middleware is added."""
        # Check that CORS middleware is in the app's middleware stack
        assert any("CORSMiddleware" in str(middleware.cls) for middleware in app.user_middleware)

    def test_app_includes_routers(self):
        """Test that required routers are included."""
        # Check that auth and command routers are included
        route_paths = [route.path for route in app.routes]
        assert any("/auth" in path for path in route_paths)
        assert any("/command" in path for path in route_paths)


class TestEndpoints:
    """Test API endpoints."""

    @pytest.fixture
    def client(self):
        """Create a test client with initialized app state."""
        # Initialize the app state with persistence
        with patch("server.persistence.get_persistence") as mock_get_persistence:
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence

            # Create a test client
            test_client = TestClient(app)

            # Manually set the persistence in app state
            test_client.app.state.persistence = mock_persistence

            return test_client

    def test_read_root(self, client):
        """Test the root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to MythosMUD!"}

    def test_get_room_existing(self, client):
        """Test getting an existing room."""
        with patch.object(client.app.state.persistence, "get_room") as mock_get_room:
            mock_room = {"id": "test_room", "name": "Test Room"}
            mock_get_room.return_value = mock_room

            response = client.get("/rooms/test_room")

            assert response.status_code == 200
            assert response.json() == mock_room

    def test_get_room_not_found(self, client):
        """Test getting a non-existent room."""
        with patch.object(client.app.state.persistence, "get_room") as mock_get_room:
            mock_get_room.return_value = None

            response = client.get("/rooms/nonexistent")

            assert response.status_code == 404
            assert "Room not found" in response.json()["error"]["message"]

    def test_create_player_success(self, client):
        """Test creating a new player."""
        # Mock the authentication dependency
        with patch("server.api.players.get_current_user") as mock_auth:
            mock_auth.return_value = {"user_id": "test-user-id"}

            # Mock the PlayerService to return a successful result
            with patch("server.api.players.PlayerService") as mock_player_service:
                mock_service_instance = Mock()
                mock_player = Mock()
                mock_player.name = "testplayer"
                mock_player.current_room_id = "earth_arkham_city_intersection_derby_high"
                mock_player.player_id = "550e8400-e29b-41d4-a716-446655440000"
                mock_player.id = "550e8400-e29b-41d4-a716-446655440000"
                mock_player.user_id = "550e8400-e29b-41d4-a716-446655440001"
                mock_player.experience_points = 0
                mock_player.level = 1
                mock_player.stats = {"health": 100, "sanity": 90}
                mock_player.inventory = []
                mock_player.status_effects = []
                mock_player.created_at = "2024-01-01T00:00:00Z"
                mock_player.last_active = "2024-01-01T00:00:00Z"
                mock_service_instance.create_player.return_value = mock_player
                mock_player_service.return_value = mock_service_instance

                response = client.post(
                    "/players?name=testplayer&starting_room_id=earth_arkham_city_intersection_derby_high"
                )

                assert response.status_code == 200
                # The response will be handled by the PlayerService

    def test_create_player_already_exists(self, client):
        """Test creating a player that already exists."""
        with patch.object(client.app.state.persistence, "get_player_by_name") as mock_get_player:
            mock_get_player.return_value = Mock(name="testplayer")  # Player exists

            response = client.post("/players?name=testplayer")

            assert response.status_code == 400
            assert "Invalid input provided" in response.json()["error"]["message"]

    def test_list_players(self, client):
        """Test listing all players."""
        # Create mock players that match the expected schema with proper UUIDs
        test_uuid1 = str(uuid.uuid4())
        test_uuid2 = str(uuid.uuid4())
        test_user_uuid1 = str(uuid.uuid4())
        test_user_uuid2 = str(uuid.uuid4())

        mock_players = [
            {
                "player_id": test_uuid1,
                "name": "player1",
                "user_id": test_user_uuid1,
                "stats": {"health": 100, "sanity": 90},
                "inventory": [],
                "status_effects": [],
                "created_at": "2024-01-01T00:00:00Z",
                "last_active": "2024-01-01T00:00:00Z",
                "current_room_id": "earth_arkham_city_intersection_derby_high",
                "experience_points": 0,
                "level": 1,
            },
            {
                "player_id": test_uuid2,
                "name": "player2",
                "user_id": test_user_uuid2,
                "stats": {"health": 100, "sanity": 90},
                "inventory": [],
                "status_effects": [],
                "created_at": "2024-01-01T00:00:00Z",
                "last_active": "2024-01-01T00:00:00Z",
                "current_room_id": "earth_arkham_city_intersection_derby_high",
                "experience_points": 0,
                "level": 1,
            },
        ]
        with patch.object(client.app.state.persistence, "list_players") as mock_list_players:
            mock_list_players.return_value = mock_players

            response = client.get("/players")

            assert response.status_code == 200
            # Convert expected format to match PlayerRead schema
            expected_response = []
            for player in mock_players:
                expected_player = player.copy()
                expected_player["id"] = expected_player.pop("player_id")
                expected_response.append(expected_player)
            assert response.json() == expected_response

    def test_get_player_by_id_success(self, client):
        """Test getting a player by ID."""
        test_uuid = str(uuid.uuid4())
        test_user_uuid = str(uuid.uuid4())

        mock_player = {
            "player_id": test_uuid,
            "name": "testplayer",
            "user_id": test_user_uuid,
            "stats": {"health": 100, "sanity": 90},
            "inventory": [],
            "status_effects": [],
            "created_at": "2024-01-01T00:00:00Z",
            "last_active": "2024-01-01T00:00:00Z",
            "current_room_id": "earth_arkham_city_intersection_derby_high",
            "experience_points": 0,
            "level": 1,
        }
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            mock_get_player.return_value = mock_player

            response = client.get(f"/players/{test_uuid}")

            assert response.status_code == 200
            # Convert expected format to match PlayerRead schema
            expected_player = mock_player.copy()
            expected_player["id"] = expected_player.pop("player_id")
            assert response.json() == expected_player

    def test_get_player_by_id_not_found(self, client):
        """Test getting a non-existent player by ID."""
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            mock_get_player.return_value = None

            response = client.get("/players/nonexistent")

            assert response.status_code == 404
            assert "not found" in response.json()["error"]["message"]

    def test_get_player_by_name_success(self, client):
        """Test getting a player by name."""
        test_uuid = str(uuid.uuid4())
        test_user_uuid = str(uuid.uuid4())

        mock_player = {
            "player_id": test_uuid,
            "name": "testplayer",
            "user_id": test_user_uuid,
            "stats": {"health": 100, "sanity": 90},
            "inventory": [],
            "status_effects": [],
            "created_at": "2024-01-01T00:00:00Z",
            "last_active": "2024-01-01T00:00:00Z",
            "current_room_id": "earth_arkham_city_intersection_derby_high",
            "experience_points": 0,
            "level": 1,
        }
        with patch.object(client.app.state.persistence, "get_player_by_name") as mock_get_player:
            mock_get_player.return_value = mock_player

            response = client.get("/players/name/testplayer")

            assert response.status_code == 200
            # Convert expected format to match PlayerRead schema
            expected_player = mock_player.copy()
            expected_player["id"] = expected_player.pop("player_id")
            assert response.json() == expected_player

    def test_get_player_by_name_not_found(self, client):
        """Test getting a non-existent player by name."""
        with patch.object(client.app.state.persistence, "get_player_by_name") as mock_get_player:
            mock_get_player.return_value = None

            response = client.get("/players/name/nonexistent")

            assert response.status_code == 404
            assert "not found" in response.json()["error"]["message"]

    def test_delete_player_not_found(self, client):
        """Test that delete player endpoint returns 404 for non-existent player."""
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            # Mock that player doesn't exist
            mock_get_player.return_value = None

            response = client.delete("/players/non_existent_id")

            assert response.status_code == 404
            assert "Player not found" in response.text

    def test_delete_player_success(self, client):
        """Test that delete player endpoint successfully deletes a player."""
        # Mock the persistence methods
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            with patch.object(client.app.state.persistence, "delete_player") as mock_delete_player:
                # Mock a player that exists
                mock_player = Mock()
                mock_player.name = "TestDeletePlayer"
                mock_get_player.return_value = mock_player

                # Mock successful deletion
                mock_delete_player.return_value = True

                # Test the delete endpoint
                response = client.delete("/players/test_player_id")

                assert response.status_code == 200
                assert "has been deleted" in response.text

                # Verify the persistence methods were called
                mock_get_player.assert_called_once_with("test_player_id")
                mock_delete_player.assert_called_once_with("test_player_id")

    def test_get_game_status(self, client):
        """Test getting game status."""
        with patch("server.api.game.connection_manager") as mock_connection_manager:
            mock_connection_manager.get_active_connection_count.return_value = 5
            mock_connection_manager.player_websockets = {"player1": "conn1", "player2": "conn2"}
            mock_connection_manager.room_subscriptions = {"room1": {"player1"}}

            response = client.get("/game/status")

            assert response.status_code == 200
            data = response.json()
            assert data["active_connections"] == 5
            assert data["active_players"] == 2
            assert data["room_subscriptions"] == 1
            assert "server_time" in data


class TestWebSocketEndpoints:
    """Test WebSocket endpoints."""

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_no_token(self):
        """Test WebSocket endpoint without token."""
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {}

        # Patch at the point of use in server.api.real_time
        with patch("server.api.real_time.handle_websocket_connection") as mock_handler:
            from ..api.real_time import websocket_endpoint_route

            await websocket_endpoint_route(mock_websocket, "testplayer")
            mock_handler.assert_called_once_with(mock_websocket, "testplayer")

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_invalid_token(self):
        """Test WebSocket endpoint with invalid token."""
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "invalid_token"}

        # Patch at the point of use in server.api.real_time
        with patch("server.api.real_time.handle_websocket_connection") as mock_handler:
            from ..api.real_time import websocket_endpoint_route

            await websocket_endpoint_route(mock_websocket, "testplayer")
            mock_handler.assert_called_once_with(mock_websocket, "testplayer")

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_token_mismatch(self):
        """Test WebSocket endpoint with token mismatch."""
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}

        # Patch at the point of use in server.api.real_time
        with patch("server.api.real_time.handle_websocket_connection") as mock_handler:
            from ..api.real_time import websocket_endpoint_route

            await websocket_endpoint_route(mock_websocket, "testplayer")
            mock_handler.assert_called_once_with(mock_websocket, "testplayer")


class TestSSEEndpoints:
    """Test Server-Sent Events endpoints."""

    @pytest.fixture
    def client(self):
        """Create a test client."""
        return TestClient(app)

    @pytest.mark.asyncio
    async def test_game_events_stream_no_token(self, client):
        """Test SSE endpoint without token."""
        # Mock the game_event_stream to return immediately
        with patch("server.api.real_time.game_event_stream") as mock_stream:
            mock_stream.return_value = iter(
                [
                    'data: {"type": "connected", "data": {"player_id": "testplayer"}, "timestamp": "2023-01-01T00:00:00Z"}\n\n'
                ]
            )

            response = client.get("/api/events/testplayer")

            # New simplified endpoint returns 200 with streaming response
            assert response.status_code == 200
            assert "text/event-stream" in response.headers["content-type"]

    @pytest.mark.asyncio
    async def test_game_events_stream_invalid_token(self, client):
        """Test SSE endpoint with invalid token."""
        with patch("server.api.real_time.game_event_stream") as mock_stream:
            mock_stream.return_value = iter(
                [
                    'data: {"type": "connected", "data": {"player_id": "testplayer"}, "timestamp": "2023-01-01T00:00:00Z"}\n\n'
                ]
            )

            response = client.get("/api/events/testplayer?token=invalid")

            # New simplified endpoint returns 200 with streaming response
            assert response.status_code == 200
            assert "text/event-stream" in response.headers["content-type"]

    @pytest.mark.asyncio
    async def test_game_events_stream_player_not_found(self, client):
        """Test SSE endpoint with player not found."""
        with patch("server.api.real_time.game_event_stream") as mock_stream:
            mock_stream.return_value = iter(
                [
                    'data: {"type": "connected", "data": {"player_id": "testplayer"}, "timestamp": "2023-01-01T00:00:00Z"}\n\n'
                ]
            )

            response = client.get("/api/events/testplayer?token=valid")

            # New simplified endpoint returns 200 with streaming response
            assert response.status_code == 200
            assert "text/event-stream" in response.headers["content-type"]

    @pytest.mark.asyncio
    async def test_game_events_stream_token_mismatch(self, client):
        """Test SSE endpoint with token mismatch."""
        with patch("server.api.real_time.game_event_stream") as mock_stream:
            mock_stream.return_value = iter(
                [
                    'data: {"type": "connected", "data": {"player_id": "testplayer"}, "timestamp": "2023-01-01T00:00:00Z"}\n\n'
                ]
            )

            response = client.get("/api/events/testplayer?token=valid")

            # New simplified endpoint returns 200 with streaming response
            assert response.status_code == 200
            assert "text/event-stream" in response.headers["content-type"]
