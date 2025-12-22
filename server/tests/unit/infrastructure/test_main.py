"""
Tests for main.py module.

Tests the FastAPI application, endpoints, logging setup, and game tick functionality.
"""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket

# Import the app directly to avoid import issues
from server.main import app


class TestFastAPIApp:
    """Test FastAPI application setup."""

    def test_app_creation(self) -> None:
        """Test that the FastAPI app is created correctly."""
        assert isinstance(app, FastAPI)
        assert app.title == "MythosMUD API"
        assert app.version == "0.1.0"

    def test_app_has_cors_middleware(self) -> None:
        """Test that CORS middleware is added."""
        # Check that CORS middleware is in the app's middleware stack
        assert any("CORSMiddleware" in str(middleware.cls) for middleware in app.user_middleware)

    def test_app_includes_routers(self) -> None:
        """Test that required routers are included."""
        # Check that auth and command routers are included
        route_paths = [getattr(route, "path", "") for route in app.routes]
        assert any("/auth" in path for path in route_paths)
        assert any("/command" in path for path in route_paths)


class TestEndpoints:
    """Test API endpoints."""

    @pytest.fixture
    def client(self, mock_application_container):
        """Create a test client with initialized app state."""
        # Initialize the app state with persistence
        # Use AsyncPersistenceLayer directly (PersistenceLayer removed)
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()

        # Mock profession data to return proper string values
        mock_profession = Mock()
        mock_profession.name = "Scholar"
        mock_profession.description = "A learned academic"
        mock_profession.flavor_text = "Knowledge is power"
        mock_persistence.async_get_profession_by_id = AsyncMock(return_value=mock_profession)
        # Also mock get_profession_by_id for _convert_player_to_schema
        mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

        # Create a test client
        test_client = TestClient(app)

        # Create real PlayerService with mocked persistence
        # This allows tests to patch persistence methods and have those patches
        # affect the service layer behavior
        from server.game.player_service import PlayerService

        player_service = PlayerService(mock_persistence)

        # Use the comprehensive mock container and update specific services
        mock_application_container.persistence = mock_persistence
        mock_application_container.player_service = player_service

        # Set container and services in app state
        cast(FastAPI, test_client.app).state.container = mock_application_container
        cast(FastAPI, test_client.app).state.persistence = mock_persistence
        cast(FastAPI, test_client.app).state.player_service = player_service
        cast(FastAPI, test_client.app).state.room_service = mock_application_container.room_service

        # Mock get_current_user dependency to avoid authentication failures
        # This is needed because all player endpoints require authentication
        from server.api.players import get_current_user

        # Create a mock user for authentication
        mock_user = Mock()
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "test@example.com"

        async def mock_get_current_user():
            return mock_user

        # Override the dependency
        app.dependency_overrides[get_current_user] = mock_get_current_user

        # Use pytest's yield fixture pattern for proper cleanup
        yield test_client

        # Cleanup: restore original dependencies after test
        app.dependency_overrides.pop(get_current_user, None)

    def test_read_root(self, client):
        """Test the root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to MythosMUD!"}

    def test_get_room_existing(self, client):
        """Test getting an existing room."""
        with patch.object(
            cast(FastAPI, client.app).state.room_service, "get_room", new_callable=AsyncMock
        ) as mock_get_room:
            mock_room = {"id": "test_room", "name": "Test Room"}
            mock_get_room.return_value = mock_room

            # Room router is mounted at /api/rooms (see server/app/factory.py line 177)
            response = client.get("/api/rooms/test_room")

            assert response.status_code == 200
            assert response.json() == mock_room

    def test_get_room_not_found(self, client):
        """Test getting a non-existent room."""
        # Use MagicMock as base, then explicitly set get_room as AsyncMock to prevent AsyncMock warnings
        mock_room_service = MagicMock()
        mock_room_service.get_room = AsyncMock(return_value=None)

        # Set the room_service in the container (which is used by the dependency)
        cast(FastAPI, client.app).state.container.room_service = mock_room_service
        cast(FastAPI, client.app).state.room_service = mock_room_service

        # Room router is mounted at /api/rooms (see server/app/factory.py line 177)
        response = client.get("/api/rooms/nonexistent")

        assert response.status_code == 404
        # StandardizedErrorResponse uses {"error": {"message": ...}} format
        response_data = response.json()
        # Check for standardized error format
        if "error" in response_data and "message" in response_data["error"]:
            assert "Room not found" in response_data["error"]["message"]
        elif "detail" in response_data:
            # Fallback to FastAPI's standard format
            assert "Room not found" in response_data["detail"]
        else:
            # Check if it's in a nested structure
            assert "Room not found" in str(response_data)

    def test_create_player_success(self, client):
        """Test creating a new player."""
        # Create a proper mock User object (not a dict)
        mock_user = Mock()
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "test@example.com"

        # Mock the PlayerService to return a successful result
        mock_service_instance = Mock()
        mock_player = Mock()
        mock_player.name = "testplayer"
        mock_player.current_room_id = "earth_arkhamcity_intersection_derby_high"
        mock_player.player_id = "550e8400-e29b-41d4-a716-446655440000"
        mock_player.id = "550e8400-e29b-41d4-a716-446655440000"
        mock_player.user_id = "550e8400-e29b-41d4-a716-446655440001"
        mock_player.experience_points = 0
        mock_player.level = 1
        mock_player.stats = {"health": 100, "lucidity": 90, "position": "standing"}
        mock_player.inventory = []
        mock_player.status_effects = []
        mock_player.created_at = "2024-01-01T00:00:00Z"
        mock_player.last_active = "2024-01-01T00:00:00Z"
        mock_player.is_admin = False
        mock_player.in_combat = False
        mock_player.position = "standing"
        # Add profession fields that are now required by PlayerRead schema
        mock_player.profession_id = 0
        mock_player.profession_name = "Scholar"
        mock_player.profession_description = "A learned academic"
        mock_player.profession_flavor_text = "Knowledge is power"
        mock_player.model_dump = Mock(
            return_value={
                "id": mock_player.id,  # PlayerRead expects 'id', not 'player_id'
                "name": mock_player.name,
                "current_room_id": mock_player.current_room_id,
                "user_id": mock_player.user_id,
                "experience_points": mock_player.experience_points,
                "level": mock_player.level,
                "stats": mock_player.stats,
                "inventory": mock_player.inventory,
                "status_effects": mock_player.status_effects,
                "created_at": mock_player.created_at,
                "last_active": mock_player.last_active,
                "profession_id": mock_player.profession_id,
                "profession_name": mock_player.profession_name,
                "profession_description": mock_player.profession_description,
                "profession_flavor_text": mock_player.profession_flavor_text,
            }
        )
        mock_service_instance.create_player = AsyncMock(return_value=mock_player)

        # Override the app dependencies
        import server.dependencies
        from server.api.players import get_current_user

        # Mock the authentication dependency - get_current_user is async
        async def mock_get_current_user():
            return mock_user

        app.dependency_overrides[get_current_user] = mock_get_current_user
        app.dependency_overrides[server.dependencies.get_player_service] = lambda: mock_service_instance

        try:
            response = client.post(
                "/api/players?name=testplayer&starting_room_id=earth_arkhamcity_intersection_derby_high"
            )

            assert response.status_code == 200
            # The response will be handled by the PlayerService
        finally:
            # Clean up the dependency overrides
            app.dependency_overrides.clear()

    def test_create_player_already_exists(self, client):
        """Test creating a player that already exists."""

        # Patch asyncio.create_task to prevent background task warnings
        def create_task_side_effect(coro):
            # Close the coroutine to prevent "never awaited" warning
            if hasattr(coro, "close"):
                coro.close()
            return MagicMock()

        with (
            patch("asyncio.create_task", side_effect=create_task_side_effect),
            patch.object(
                cast(FastAPI, client.app).state.persistence, "get_player_by_name", new_callable=AsyncMock
            ) as mock_get_player,
        ):
            mock_get_player.return_value = Mock(name="testplayer")  # Player exists

            response = client.post("/api/players?name=testplayer")

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
                "stats": {"health": 100, "lucidity": 90},
                "inventory": [],
                "status_effects": [],
                "created_at": "2024-01-01T00:00:00Z",
                "last_active": "2024-01-01T00:00:00Z",
                "current_room_id": "earth_arkhamcity_intersection_derby_high",
                "experience_points": 0,
                "level": 1,
                "is_admin": False,
                "in_combat": False,
                "position": "standing",
                # Add profession fields that are now required by PlayerRead schema
                "profession_id": 0,
                "profession_name": "Scholar",
                "profession_description": "A learned academic",
                "profession_flavor_text": "Knowledge is power",
            },
            {
                "player_id": test_uuid2,
                "name": "player2",
                "user_id": test_user_uuid2,
                "stats": {"health": 100, "lucidity": 90},
                "inventory": [],
                "status_effects": [],
                "created_at": "2024-01-01T00:00:00Z",
                "last_active": "2024-01-01T00:00:00Z",
                "current_room_id": "earth_arkhamcity_intersection_derby_high",
                "experience_points": 0,
                "level": 1,
                "is_admin": False,
                "in_combat": False,
                "position": "standing",
                # Add profession fields that are now required by PlayerRead schema
                "profession_id": 0,
                "profession_name": "Scholar",
                "profession_description": "A learned academic",
                "profession_flavor_text": "Knowledge is power",
            },
        ]
        # Patch player_service.list_players directly since endpoint uses dependency injection
        from server.schemas.player import PlayerRead

        # Convert player_id to id for PlayerRead schema
        player_objects = []
        for player in mock_players:
            player_data = player.copy()
            player_data["id"] = player_data.pop("player_id")
            player_objects.append(PlayerRead(**player_data))

        with patch.object(
            cast(FastAPI, client.app).state.player_service, "list_players", new_callable=AsyncMock
        ) as mock_list_players:
            mock_list_players.return_value = player_objects

            response = client.get("/api/players")

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
            "stats": {"health": 100, "lucidity": 90},
            "inventory": [],
            "status_effects": [],
            "created_at": "2024-01-01T00:00:00Z",
            "last_active": "2024-01-01T00:00:00Z",
            "current_room_id": "earth_arkhamcity_intersection_derby_high",
            "experience_points": 0,
            "level": 1,
            "is_admin": False,
            "in_combat": False,
            "position": "standing",
            # Add profession fields that are now required by PlayerRead schema
            "profession_id": 0,
            "profession_name": "Scholar",
            "profession_description": "A learned academic",
            "profession_flavor_text": "Knowledge is power",
        }
        with patch.object(
            cast(FastAPI, client.app).state.player_service, "get_player_by_id", new_callable=AsyncMock
        ) as mock_get_player:
            from server.schemas.player import PlayerRead

            # Convert player_id to id for PlayerRead schema
            mock_player_data = mock_player.copy()
            mock_player_data["id"] = mock_player_data.pop("player_id")
            mock_player_obj = PlayerRead(**mock_player_data)
            mock_get_player.return_value = mock_player_obj

            response = client.get(f"/api/players/{test_uuid}")

            assert response.status_code == 200
            # Convert expected format to match PlayerRead schema
            expected_player = mock_player.copy()
            expected_player["id"] = expected_player.pop("player_id")
            assert response.json() == expected_player

    def test_get_player_by_id_not_found(self, client):
        """Test getting a non-existent player by ID."""
        test_uuid = str(uuid.uuid4())
        with patch.object(
            cast(FastAPI, client.app).state.player_service, "get_player_by_id", new_callable=AsyncMock
        ) as mock_get_player:
            mock_get_player.return_value = None

            response = client.get(f"/api/players/{test_uuid}")

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
            "stats": {"health": 100, "lucidity": 90},
            "inventory": [],
            "status_effects": [],
            "created_at": "2024-01-01T00:00:00Z",
            "last_active": "2024-01-01T00:00:00Z",
            "current_room_id": "earth_arkhamcity_intersection_derby_high",
            "experience_points": 0,
            "level": 1,
            "is_admin": False,
            "in_combat": False,
            "position": "standing",
        }
        with patch.object(
            cast(FastAPI, client.app).state.player_service, "get_player_by_name", new_callable=AsyncMock
        ) as mock_get_player:
            from server.schemas.player import PlayerRead

            # Convert player_id to id for PlayerRead schema
            mock_player_data = mock_player.copy()
            mock_player_data["id"] = mock_player_data.pop("player_id")
            # Add profession fields that are populated by _convert_player_to_schema
            mock_player_data["profession_id"] = 0
            mock_player_data["profession_name"] = "Scholar"
            mock_player_data["profession_description"] = "A learned academic"
            mock_player_data["profession_flavor_text"] = "Knowledge is power"
            mock_player_obj = PlayerRead(**mock_player_data)
            mock_get_player.return_value = mock_player_obj

            response = client.get("/api/players/name/testplayer")

            assert response.status_code == 200
            # Convert expected format to match PlayerRead schema
            expected_player = mock_player.copy()
            expected_player["id"] = expected_player.pop("player_id")
            # Add profession fields that are now included in the response
            expected_player["profession_id"] = 0
            expected_player["profession_name"] = "Scholar"
            expected_player["profession_description"] = "A learned academic"
            expected_player["profession_flavor_text"] = "Knowledge is power"
            assert response.json() == expected_player

    def test_get_player_by_name_not_found(self, client):
        """Test getting a non-existent player by name."""
        with patch.object(
            cast(FastAPI, client.app).state.player_service, "get_player_by_name", new_callable=AsyncMock
        ) as mock_get_player:
            mock_get_player.return_value = None

            response = client.get("/api/players/name/nonexistent")

            assert response.status_code == 404
            assert "not found" in response.json()["error"]["message"]

    def test_delete_player_not_found(self, client):
        """Test that delete player endpoint returns 404 for non-existent player."""
        test_uuid = uuid.uuid4()
        test_uuid_str = str(test_uuid)
        # Mock delete_player to raise ValidationError (which the API converts to 404)
        with patch.object(
            client.app.state.player_service, "delete_player", new_callable=AsyncMock
        ) as mock_delete_player:
            from server.exceptions import ValidationError

            # Mock that delete_player raises ValidationError when player not found
            mock_delete_player.side_effect = ValidationError("Player not found for deletion")

            response = client.delete(f"/api/players/{test_uuid_str}")

            assert response.status_code == 404
            assert "Player not found" in response.text

    def test_delete_player_success(self, client):
        """Test that delete player endpoint successfully deletes a player."""
        test_uuid = uuid.uuid4()
        test_uuid_str = str(test_uuid)
        # Mock the player service delete_player method
        with patch.object(
            client.app.state.player_service, "delete_player", new_callable=AsyncMock
        ) as mock_delete_player:
            # Mock successful deletion - delete_player returns (success: bool, message: str)
            mock_delete_player.return_value = (True, f"Player {test_uuid_str} has been deleted")

            # Test the delete endpoint
            response = client.delete(f"/api/players/{test_uuid_str}")

            assert response.status_code == 200
            assert "has been deleted" in response.text

            # Verify the player service method was called
            mock_delete_player.assert_called_once_with(test_uuid)

    def test_get_game_status(self, client):
        """Test getting game status."""
        # AI Agent: Configure the connection_manager directly on client app state
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_active_connection_count.return_value = 5
        mock_connection_manager.player_websockets = {"player1": "conn1", "player2": "conn2"}
        mock_connection_manager.room_subscriptions = {"room1": {"player1"}}
        client.app.state.container.connection_manager = mock_connection_manager

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
    async def test_websocket_endpoint_route_no_token(self) -> None:
        """Test WebSocket endpoint without token."""
        test_player_id = str(uuid.uuid4())
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {}
        mock_websocket.app = Mock()
        mock_websocket.app.state = Mock()
        mock_websocket.app.state.container = Mock()
        mock_websocket.app.state.container.connection_manager = Mock()
        mock_websocket.app.state.container.connection_manager.persistence = Mock()

        # Patch at the point of use in server.api.real_time
        with (
            patch("server.api.real_time._resolve_connection_manager_from_state") as mock_resolve,
            patch("server.api.real_time.handle_websocket_connection") as mock_handler,
        ):
            mock_resolve.return_value = Mock(persistence=Mock())
            from server.api.real_time import websocket_endpoint_route

            await websocket_endpoint_route(mock_websocket, test_player_id)
            # The endpoint converts the string player_id to UUID
            expected_uuid = uuid.UUID(test_player_id)
            mock_handler.assert_called_once_with(
                mock_websocket, expected_uuid, None, connection_manager=mock_resolve.return_value
            )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_invalid_token(self) -> None:
        """Test WebSocket endpoint with invalid token."""
        test_player_id = str(uuid.uuid4())
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "invalid_token"}
        mock_websocket.app = Mock()
        mock_websocket.app.state = Mock()
        mock_websocket.app.state.container = Mock()
        mock_websocket.app.state.container.connection_manager = Mock()
        mock_websocket.app.state.container.connection_manager.persistence = Mock()

        # Patch at the point of use in server.api.real_time
        with (
            patch("server.api.real_time._resolve_connection_manager_from_state") as mock_resolve,
            patch("server.api.real_time.handle_websocket_connection") as mock_handler,
        ):
            mock_resolve.return_value = Mock(persistence=Mock())
            from server.api.real_time import websocket_endpoint_route

            await websocket_endpoint_route(mock_websocket, test_player_id)
            # The endpoint converts the string player_id to UUID
            expected_uuid = uuid.UUID(test_player_id)
            mock_handler.assert_called_once_with(
                mock_websocket, expected_uuid, None, connection_manager=mock_resolve.return_value
            )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_token_mismatch(self) -> None:
        """Test WebSocket endpoint with token mismatch."""
        test_player_id = str(uuid.uuid4())
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}
        mock_websocket.app = Mock()
        mock_websocket.app.state = Mock()
        mock_websocket.app.state.container = Mock()
        mock_websocket.app.state.container.connection_manager = Mock()
        mock_websocket.app.state.container.connection_manager.persistence = Mock()

        # Patch at the point of use in server.api.real_time
        with (
            patch("server.api.real_time._resolve_connection_manager_from_state") as mock_resolve,
            patch("server.api.real_time.handle_websocket_connection") as mock_handler,
        ):
            mock_resolve.return_value = Mock(persistence=Mock())
            from server.api.real_time import websocket_endpoint_route

            await websocket_endpoint_route(mock_websocket, test_player_id)
            # The endpoint converts the string player_id to UUID
            expected_uuid = uuid.UUID(test_player_id)
            mock_handler.assert_called_once_with(
                mock_websocket, expected_uuid, None, connection_manager=mock_resolve.return_value
            )
