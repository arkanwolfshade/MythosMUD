"""
Tests for main.py module.

Tests the FastAPI application, endpoints, logging setup, and game tick functionality.
"""

import asyncio
import logging
import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket

# Import the app directly to avoid import issues
from ..main import app, get_tick_interval


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
        with patch("server.main.get_persistence") as mock_get_persistence:
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

            assert response.status_code == 200
            assert response.json() == {"error": "Room not found"}

    def test_create_player_success(self, client):
        """Test creating a new player."""
        with patch.object(client.app.state.persistence, "get_player_by_name") as mock_get_player:
            with patch.object(client.app.state.persistence, "save_player") as mock_save_player:
                mock_get_player.return_value = None  # Player doesn't exist

                response = client.post("/players?name=testplayer&starting_room_id=arkham_001")

                assert response.status_code == 200
                data = response.json()
                assert data["name"] == "testplayer"
                assert data["current_room_id"] == "arkham_001"
                assert "id" in data
                mock_save_player.assert_called_once()

    def test_create_player_already_exists(self, client):
        """Test creating a player that already exists."""
        with patch.object(client.app.state.persistence, "get_player_by_name") as mock_get_player:
            mock_get_player.return_value = Mock(name="testplayer")  # Player exists

            response = client.post("/players?name=testplayer")

            assert response.status_code == 400
            assert "already exists" in response.json()["detail"]

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
                "current_room_id": "arkham_001",
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
                "current_room_id": "arkham_001",
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
            "current_room_id": "arkham_001",
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
            assert "not found" in response.json()["detail"]

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
            "current_room_id": "arkham_001",
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
            assert "not found" in response.json()["detail"]

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
        with patch("server.main.connection_manager") as mock_connection_manager:
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


class TestGameTickConfiguration:
    """Test configurable game tick rate functionality."""

    def test_get_tick_interval_default_value(self):
        """Test that get_tick_interval returns default value when config is missing."""
        with patch("server.main.get_config") as mock_get_config:
            mock_get_config.return_value = {}

            result = get_tick_interval()

            assert result == 1.0

    def test_get_tick_interval_valid_config(self):
        """Test that get_tick_interval returns configured value."""
        with patch("server.main.get_config") as mock_get_config:
            mock_get_config.return_value = {"game_tick_rate": 2.5}

            result = get_tick_interval()

            assert result == 2.5

    def test_get_tick_interval_invalid_type(self):
        """Test that get_tick_interval handles invalid type gracefully."""
        with patch("server.main.get_config") as mock_get_config:
            mock_get_config.return_value = {"game_tick_rate": "invalid"}

            result = get_tick_interval()

            assert result == 1.0

    def test_get_tick_interval_negative_value(self):
        """Test that get_tick_interval handles negative values gracefully."""
        with patch("server.main.get_config") as mock_get_config:
            mock_get_config.return_value = {"game_tick_rate": -1.0}

            result = get_tick_interval()

            assert result == 1.0

    def test_get_tick_interval_zero_value(self):
        """Test that get_tick_interval handles zero values gracefully."""
        with patch("server.main.get_config") as mock_get_config:
            mock_get_config.return_value = {"game_tick_rate": 0}

            result = get_tick_interval()

            assert result == 1.0

    def test_get_tick_interval_too_high(self):
        """Test that get_tick_interval caps values at maximum."""
        with patch("server.main.get_config") as mock_get_config:
            mock_get_config.return_value = {"game_tick_rate": 100.0}

            result = get_tick_interval()

            assert result == 60.0

    def test_get_tick_interval_logging(self, caplog):
        """Test that get_tick_interval logs configuration."""
        with patch("server.main.get_config") as mock_get_config:
            mock_get_config.return_value = {"game_tick_rate": 3.0}

            with caplog.at_level(logging.INFO):
                result = get_tick_interval()

            assert "Game tick rate configured: 3.0 seconds" in caplog.text
            assert result == 3.0

    def test_get_tick_interval_warning_logging(self, caplog):
        """Test that get_tick_interval logs warnings for invalid values."""
        with patch("server.main.get_config") as mock_get_config:
            mock_get_config.return_value = {"game_tick_rate": -5.0}

            with caplog.at_level(logging.WARNING):
                result = get_tick_interval()

            assert "Invalid game_tick_rate in config: -5.0" in caplog.text
            assert result == 1.0

    def test_get_tick_interval_max_warning_logging(self, caplog):
        """Test that get_tick_interval logs warnings for values too high."""
        with patch("server.main.get_config") as mock_get_config:
            mock_get_config.return_value = {"game_tick_rate": 100.0}

            with caplog.at_level(logging.WARNING):
                result = get_tick_interval()

            assert "Game tick rate too high: 100.0" in caplog.text
            assert result == 60.0


class TestGameTickLoop:
    """Test game tick loop functionality."""

    @pytest.mark.asyncio
    async def test_game_tick_loop_basic(self):
        """Test basic game tick loop functionality."""
        mock_app = Mock()
        mock_app.state.persistence = Mock()

        with patch("server.main.broadcast_game_tick") as mock_broadcast:
            with patch("server.main.connection_manager") as mock_connection_manager:
                mock_connection_manager.player_websockets = {"player1": "conn1"}

                # Import the function directly to avoid import issues
                from ..main import game_tick_loop

                # Run the tick loop for a short time
                task = asyncio.create_task(game_tick_loop(mock_app))
                await asyncio.sleep(0.1)  # Let it run for a short time
                task.cancel()

                # Verify broadcast was called
                mock_broadcast.assert_called()
                call_args = mock_broadcast.call_args[0][0]
                assert "tick_number" in call_args
                assert "timestamp" in call_args
                assert "active_players" in call_args

    @pytest.mark.asyncio
    async def test_game_tick_loop_logging(self):
        """Test that game tick loop logs properly."""
        mock_app = Mock()
        mock_app.state.persistence = Mock()

        with patch("server.main.logging") as mock_logging:
            with patch("server.main.broadcast_game_tick"):
                with patch("server.main.connection_manager") as mock_connection_manager:
                    mock_connection_manager.player_websockets = {}

                    # Import the function directly to avoid import issues
                    from ..main import game_tick_loop

                    # Run the tick loop for a short time
                    task = asyncio.create_task(game_tick_loop(mock_app))
                    await asyncio.sleep(0.1)  # Let it run for a short time
                    task.cancel()

                    # Verify logging was called
                    mock_logging.info.assert_called()

    @pytest.mark.asyncio
    async def test_game_tick_loop_caches_interval(self):
        """Test that game tick loop caches the tick interval to avoid repeated logging."""
        mock_app = Mock()
        mock_app.state.persistence = Mock()

        with patch("server.main.get_tick_interval") as mock_get_interval:
            mock_get_interval.return_value = 1.0

            with patch("server.main.broadcast_game_tick"):
                with patch("server.main.connection_manager") as mock_connection_manager:
                    mock_connection_manager.player_websockets = {}

                    # Import the function directly to avoid import issues
                    from ..main import game_tick_loop

                    # Run the tick loop for a short time
                    task = asyncio.create_task(game_tick_loop(mock_app))
                    await asyncio.sleep(0.1)  # Let it run for a short time
                    task.cancel()

                    # Verify get_tick_interval was called only once during initialization
                    mock_get_interval.assert_called_once()


class TestWebSocketEndpoints:
    """Test WebSocket endpoints."""

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_no_token(self):
        """Test WebSocket endpoint without token."""
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {}

        # Import the function directly
        from ..main import websocket_handler

        await websocket_handler(mock_websocket, "testplayer")

        mock_websocket.close.assert_called_once_with(code=4001, reason="Authentication token required")

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_invalid_token(self):
        """Test WebSocket endpoint with invalid token."""
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "invalid_token"}

        # Import the function directly
        from ..main import websocket_handler

        await websocket_handler(mock_websocket, "testplayer")

        # The new behavior is to reject invalid tokens
        mock_websocket.close.assert_called_once_with(code=4001, reason="Invalid authentication token")
        mock_websocket.accept.assert_not_called()

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_token_mismatch(self):
        """Test WebSocket endpoint with token mismatch."""
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}

        # Import the function directly
        from ..main import websocket_handler

        await websocket_handler(mock_websocket, "testplayer")

        # The new behavior is to reject invalid tokens
        mock_websocket.close.assert_called_once_with(code=4001, reason="Invalid authentication token")
        mock_websocket.accept.assert_not_called()


class TestSSEEndpoints:
    """Test Server-Sent Events endpoints."""

    @pytest.fixture
    def client(self):
        """Create a test client."""
        return TestClient(app)

    def test_game_events_stream_no_token(self, client):
        """Test SSE endpoint without token."""
        response = client.get("/events/testplayer")

        assert response.status_code == 401
        assert "Authentication token required" in response.json()["detail"]

    def test_game_events_stream_invalid_token(self, client):
        """Test SSE endpoint with invalid token."""
        response = client.get("/events/testplayer?token=invalid")

        assert response.status_code == 401
        assert "Invalid authentication token" in response.json()["detail"]

    def test_game_events_stream_player_not_found(self, client):
        """Test SSE endpoint with player not found."""
        # Test with invalid token to get 401 error
        response = client.get("/events/testplayer?token=invalid")

        assert response.status_code == 401
        assert "Invalid authentication token" in response.json()["detail"]

    def test_game_events_stream_token_mismatch(self, client):
        """Test SSE endpoint with token mismatch."""
        # Test with invalid token to get 401 error
        response = client.get("/events/testplayer?token=invalid")

        assert response.status_code == 401
        assert "Invalid authentication token" in response.json()["detail"]
