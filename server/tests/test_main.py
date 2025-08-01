"""
Tests for main.py module.

Tests the FastAPI application, endpoints, logging setup, and game tick functionality.
"""

import asyncio
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket

from ..main import app, game_tick_loop, setup_logging


class TestSetupLogging:
    """Test logging setup functionality."""

    def test_setup_logging_creates_logs_directory(self):
        """Test that setup_logging creates the logs directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch("main.Path") as mock_path:
                mock_path.return_value.parent = Path(temp_dir)
                mock_logs_dir = Path(temp_dir) / "logs"
                mock_path.return_value.parent.__truediv__.return_value = mock_logs_dir

                setup_logging()

                assert mock_logs_dir.exists()

    def test_setup_logging_rotates_existing_log(self):
        """Test that setup_logging rotates existing log files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch("main.Path") as mock_path:
                mock_path.return_value.parent = Path(temp_dir)
                mock_logs_dir = Path(temp_dir) / "logs"
                mock_logs_dir.mkdir(exist_ok=True)
                mock_path.return_value.parent.__truediv__.return_value = mock_logs_dir

                # Create an existing log file
                existing_log = mock_logs_dir / "server.log"
                existing_log.write_text("old log content")

                with patch("main.datetime.datetime") as mock_datetime:
                    mock_datetime.now.return_value.strftime.return_value = "2024_01_01_120000"

                    setup_logging()

                    # Check that the old log was rotated
                    rotated_log = mock_logs_dir / "server.log.2024_01_01_120000"
                    assert rotated_log.exists()
                    assert rotated_log.read_text() == "old log content"


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
        middleware_types = [type(middleware.cls) for middleware in app.user_middleware]
        from fastapi.middleware.cors import CORSMiddleware
        assert CORSMiddleware in middleware_types

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
        """Create a test client."""
        return TestClient(app)

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
        mock_players = [
            {"id": "1", "name": "player1"},
            {"id": "2", "name": "player2"},
        ]
        with patch.object(client.app.state.persistence, "list_players") as mock_list_players:
            mock_list_players.return_value = mock_players

            response = client.get("/players")

            assert response.status_code == 200
            assert response.json() == mock_players

    def test_get_player_by_id_success(self, client):
        """Test getting a player by ID."""
        mock_player = {"id": "1", "name": "testplayer"}
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            mock_get_player.return_value = mock_player

            response = client.get("/players/1")

            assert response.status_code == 200
            assert response.json() == mock_player

    def test_get_player_by_id_not_found(self, client):
        """Test getting a non-existent player by ID."""
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            mock_get_player.return_value = None

            response = client.get("/players/nonexistent")

            assert response.status_code == 404
            assert "not found" in response.json()["detail"]

    def test_get_player_by_name_success(self, client):
        """Test getting a player by name."""
        mock_player = {"id": "1", "name": "testplayer"}
        with patch.object(client.app.state.persistence, "get_player_by_name") as mock_get_player:
            mock_get_player.return_value = mock_player

            response = client.get("/players/name/testplayer")

            assert response.status_code == 200
            assert response.json() == mock_player

    def test_get_player_by_name_not_found(self, client):
        """Test getting a non-existent player by name."""
        with patch.object(client.app.state.persistence, "get_player_by_name") as mock_get_player:
            mock_get_player.return_value = None

            response = client.get("/players/name/nonexistent")

            assert response.status_code == 404
            assert "not found" in response.json()["detail"]

    def test_delete_player_not_implemented(self, client):
        """Test that delete player endpoint raises NotImplementedError."""
        response = client.delete("/players/1")

        assert response.status_code == 500
        assert "NotImplementedError" in response.text

    def test_apply_sanity_loss_success(self, client):
        """Test applying sanity loss to a player."""
        mock_player = Mock(name="testplayer")
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            with patch.object(client.app.state.persistence, "apply_sanity_loss") as mock_apply:
                mock_get_player.return_value = mock_player

                response = client.post("/players/1/sanity-loss?amount=5&source=test")

                assert response.status_code == 200
                assert "Applied 5 sanity loss" in response.json()["message"]
                mock_apply.assert_called_once_with(mock_player, 5, "test")

    def test_apply_sanity_loss_player_not_found(self, client):
        """Test applying sanity loss to non-existent player."""
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            mock_get_player.return_value = None

            response = client.post("/players/nonexistent/sanity-loss?amount=5")

            assert response.status_code == 404
            assert "not found" in response.json()["detail"]

    def test_apply_fear_success(self, client):
        """Test applying fear to a player."""
        mock_player = Mock(name="testplayer")
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            with patch.object(client.app.state.persistence, "apply_fear") as mock_apply:
                mock_get_player.return_value = mock_player

                response = client.post("/players/1/fear?amount=3&source=test")

                assert response.status_code == 200
                assert "Applied 3 fear" in response.json()["message"]
                mock_apply.assert_called_once_with(mock_player, 3, "test")

    def test_apply_corruption_success(self, client):
        """Test applying corruption to a player."""
        mock_player = Mock(name="testplayer")
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            with patch.object(client.app.state.persistence, "apply_corruption") as mock_apply:
                mock_get_player.return_value = mock_player

                response = client.post("/players/1/corruption?amount=2&source=test")

                assert response.status_code == 200
                assert "Applied 2 corruption" in response.json()["message"]
                mock_apply.assert_called_once_with(mock_player, 2, "test")

    def test_gain_occult_knowledge_success(self, client):
        """Test gaining occult knowledge."""
        mock_player = Mock(name="testplayer")
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            with patch.object(client.app.state.persistence, "gain_occult_knowledge") as mock_gain:
                mock_get_player.return_value = mock_player

                response = client.post("/players/1/occult-knowledge?amount=1&source=test")

                assert response.status_code == 200
                assert "Gained 1 occult knowledge" in response.json()["message"]
                mock_gain.assert_called_once_with(mock_player, 1, "test")

    def test_heal_player_success(self, client):
        """Test healing a player."""
        mock_player = Mock(name="testplayer")
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            with patch.object(client.app.state.persistence, "heal_player") as mock_heal:
                mock_get_player.return_value = mock_player

                response = client.post("/players/1/heal?amount=10")

                assert response.status_code == 200
                assert "Healed testplayer for 10 health" in response.json()["message"]
                mock_heal.assert_called_once_with(mock_player, 10)

    def test_damage_player_success(self, client):
        """Test damaging a player."""
        mock_player = Mock(name="testplayer")
        with patch.object(client.app.state.persistence, "get_player") as mock_get_player:
            with patch.object(client.app.state.persistence, "damage_player") as mock_damage:
                mock_get_player.return_value = mock_player

                response = client.post("/players/1/damage?amount=5&damage_type=fire")

                assert response.status_code == 200
                assert "Damaged testplayer for 5 fire damage" in response.json()["message"]
                mock_damage.assert_called_once_with(mock_player, 5, "fire")

    def test_get_game_status(self, client):
        """Test getting game status."""
        with patch("main.connection_manager") as mock_connection_manager:
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

    def test_broadcast_message(self, client):
        """Test broadcasting a message."""
        with patch("main.get_current_user") as mock_get_current_user:
            mock_get_current_user.return_value = {"username": "admin"}

            response = client.post("/game/broadcast?message=test message")

            assert response.status_code == 200
            assert "Broadcast message: test message" in response.json()["message"]


class TestGameTickLoop:
    """Test game tick loop functionality."""

    @pytest.mark.asyncio
    async def test_game_tick_loop_basic(self):
        """Test basic game tick loop functionality."""
        mock_app = Mock()
        mock_app.state.persistence = Mock()

        with patch("main.broadcast_game_tick") as mock_broadcast:
            with patch("main.connection_manager") as mock_connection_manager:
                mock_connection_manager.player_websockets = {"player1": "conn1"}

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

        with patch("main.logging") as mock_logging:
            with patch("main.broadcast_game_tick"):
                with patch("main.connection_manager") as mock_connection_manager:
                    mock_connection_manager.player_websockets = {}

                    # Run the tick loop for a short time
                    task = asyncio.create_task(game_tick_loop(mock_app))
                    await asyncio.sleep(0.1)  # Let it run for a short time
                    task.cancel()

                    # Verify logging was called
                    mock_logging.info.assert_called()


class TestWebSocketEndpoints:
    """Test WebSocket endpoints."""

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_no_token(self):
        """Test WebSocket endpoint without token."""
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {}

        await app.websocket_endpoint_route(mock_websocket, "testplayer")

        mock_websocket.close.assert_called_once_with(
            code=4001, reason="Authentication token required"
        )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_invalid_token(self):
        """Test WebSocket endpoint with invalid token."""
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "invalid_token"}

        with patch("main.get_persistence") as mock_get_persistence:
            mock_persistence = Mock()
            mock_persistence.get_player_by_name.return_value = None
            mock_get_persistence.return_value = mock_persistence

            await app.websocket_endpoint_route(mock_websocket, "testplayer")

            mock_websocket.close.assert_called_once_with(
                code=4004, reason="Player not found in database"
            )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_token_mismatch(self):
        """Test WebSocket endpoint with token mismatch."""
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}

        with patch("main.get_persistence") as mock_get_persistence:
            mock_persistence = Mock()
            mock_player = Mock()
            mock_player.name = "different_player"
            mock_persistence.get_player_by_name.return_value = mock_player
            mock_get_persistence.return_value = mock_persistence

            await app.websocket_endpoint_route(mock_websocket, "testplayer")

            mock_websocket.close.assert_called_once_with(
                code=4003, reason="Access denied: token does not match player ID"
            )


class TestSSEEndpoints:
    """Test Server-Sent Events endpoints."""

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
        with patch("main.get_persistence") as mock_get_persistence:
            mock_persistence = Mock()
            mock_persistence.get_player_by_name.return_value = None
            mock_get_persistence.return_value = mock_persistence

            response = client.get("/events/testplayer?token=valid")

            assert response.status_code == 404
            assert "not found" in response.json()["detail"]

    def test_game_events_stream_token_mismatch(self, client):
        """Test SSE endpoint with token mismatch."""
        with patch("main.get_persistence") as mock_get_persistence:
            mock_persistence = Mock()
            mock_player = Mock()
            mock_player.name = "different_player"
            mock_persistence.get_player_by_name.return_value = mock_player
            mock_get_persistence.return_value = mock_persistence

            response = client.get("/events/testplayer?token=valid")

            assert response.status_code == 403
            assert "Access denied" in response.json()["detail"]
