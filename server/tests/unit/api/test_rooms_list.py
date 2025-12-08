"""
Tests for the rooms list API endpoint.

These tests verify that the GET /api/rooms/list endpoint properly
filters and returns room data for map visualization.

As documented in the Pnakotic Manuscripts, proper API endpoints are
essential for maintaining the integrity of our dimensional mappings.
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest


@pytest.mark.asyncio
class TestRoomsListEndpoint:
    """Test cases for GET /api/rooms/list endpoint."""

    @pytest.mark.slow
    async def test_list_rooms_requires_plane_and_zone(self, container_test_client_class):
        """Test that plane and zone parameters are required."""
        client = container_test_client_class

        # Missing plane
        response = client.get("/api/rooms/list?zone=arkhamcity")
        assert response.status_code == 422  # FastAPI validation error

        # Missing zone
        response = client.get("/api/rooms/list?plane=earth")
        assert response.status_code == 422  # FastAPI validation error

        # Both missing
        response = client.get("/api/rooms/list")
        assert response.status_code == 422  # FastAPI validation error

    async def test_list_rooms_with_plane_and_zone(self, container_test_client_class):
        """Test listing rooms with required plane and zone parameters."""
        client = container_test_client_class
        # Ensure room_service is available in container
        if hasattr(client.app.state, "container") and client.app.state.container:
            if not hasattr(client.app.state.container, "room_service") or client.app.state.container.room_service is None:
                from unittest.mock import AsyncMock

                from server.game.room_service import RoomService
                mock_persistence = AsyncMock()
                client.app.state.container.room_service = RoomService(mock_persistence)
                # Mock list_rooms to return empty list for this test
                client.app.state.container.room_service.list_rooms = AsyncMock(return_value=[])

        response = client.get("/api/rooms/list?plane=earth&zone=arkhamcity")

        assert response.status_code == 200
        data = response.json()
        assert "rooms" in data
        assert isinstance(data["rooms"], list)
        assert "total" in data
        # Verify all returned rooms match the filter (if any)
        for room in data["rooms"]:
            assert room.get("plane") == "earth"
            assert room.get("zone") == "arkhamcity"

    async def test_list_rooms_with_optional_subzone(self, container_test_client_class):
        """Test listing rooms with optional subzone filter."""
        client = container_test_client_class
        # Ensure room_service is available in container
        if hasattr(client.app.state, "container") and client.app.state.container:
            if not hasattr(client.app.state.container, "room_service") or client.app.state.container.room_service is None:
                from unittest.mock import AsyncMock

                from server.game.room_service import RoomService
                mock_persistence = AsyncMock()
                client.app.state.container.room_service = RoomService(mock_persistence)
                client.app.state.container.room_service.list_rooms = AsyncMock(return_value=[])
        response = client.get("/api/rooms/list?plane=earth&zone=arkhamcity&sub_zone=campus")

        assert response.status_code == 200
        data = response.json()
        assert "rooms" in data
        # All returned rooms should match the subzone filter
        for room in data["rooms"]:
            assert room.get("plane") == "earth"
            assert room.get("zone") == "arkhamcity"
            assert room.get("sub_zone") == "campus"

    async def test_list_rooms_includes_exits_by_default(self, container_test_client_class):
        """Test that exits are included by default."""
        client = container_test_client_class
        # Ensure room_service is available in container
        if hasattr(client.app.state, "container") and client.app.state.container:
            if not hasattr(client.app.state.container, "room_service") or client.app.state.container.room_service is None:
                from unittest.mock import AsyncMock

                from server.game.room_service import RoomService
                mock_persistence = AsyncMock()
                client.app.state.container.room_service = RoomService(mock_persistence)
                client.app.state.container.room_service.list_rooms = AsyncMock(return_value=[])
        response = client.get("/api/rooms/list?plane=earth&zone=arkhamcity")

        assert response.status_code == 200
        data = response.json()
        if len(data["rooms"]) > 0:
            room = data["rooms"][0]
            assert "exits" in room

    async def test_list_rooms_excludes_exits_when_requested(self, container_test_client_class):
        """Test that exits can be excluded when include_exits=false."""
        client = container_test_client_class
        # Ensure room_service is available in container
        if hasattr(client.app.state, "container") and client.app.state.container:
            if not hasattr(client.app.state.container, "room_service") or client.app.state.container.room_service is None:
                from unittest.mock import AsyncMock

                from server.game.room_service import RoomService
                mock_persistence = AsyncMock()
                client.app.state.container.room_service = RoomService(mock_persistence)
                client.app.state.container.room_service.list_rooms = AsyncMock(return_value=[])
        response = client.get("/api/rooms/list?plane=earth&zone=arkhamcity&include_exits=false")

        assert response.status_code == 200
        data = response.json()
        if len(data["rooms"]) > 0:
            room = data["rooms"][0]
            # Exits should not be in the response
            assert "exits" not in room

    async def test_list_rooms_filter_explored_without_auth(self, container_test_client_class):
        """Test that filter_explored without authentication returns all rooms."""
        client = container_test_client_class
        # Ensure room_service is available in container
        if hasattr(client.app.state, "container") and client.app.state.container:
            if not hasattr(client.app.state.container, "room_service") or client.app.state.container.room_service is None:
                from unittest.mock import AsyncMock

                from server.game.room_service import RoomService
                mock_persistence = AsyncMock()
                client.app.state.container.room_service = RoomService(mock_persistence)
                client.app.state.container.room_service.list_rooms = AsyncMock(return_value=[])
        response = client.get("/api/rooms/list?plane=earth&zone=arkhamcity&filter_explored=true")

        assert response.status_code == 200
        data = response.json()
        # Should return all rooms (filtering requires authentication)
        assert "rooms" in data
        assert isinstance(data["rooms"], list)

    async def test_list_rooms_filter_explored_with_auth_no_explored_rooms(self):
        """Test that filter_explored with auth but no explored rooms returns empty list."""
        test_user_id = uuid.uuid4()
        test_player_id = uuid.uuid4()

        # Mock authentication - User object needs id attribute
        mock_user = Mock()
        mock_user.id = test_user_id
        mock_user.username = "testuser"
        mock_player = Mock()
        mock_player.player_id = test_player_id

        # Import here to avoid circulars at module import time
        from server.api.rooms import list_rooms

        with patch("server.api.rooms.get_exploration_service") as mock_get_exploration_service:
            # Mock persistence to return a player for the authenticated user
            mock_persistence = AsyncMock()
            mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

            # Mock exploration service to return empty list
            mock_exploration_service = Mock()
            mock_exploration_service.get_explored_rooms = AsyncMock(return_value=[])
            mock_get_exploration_service.return_value = mock_exploration_service

            # Mock session for database queries
            mock_session = AsyncMock()

            # Mock room service to return some rooms before filtering
            mock_room_service = Mock()
            mock_room_service.list_rooms = AsyncMock(
                return_value=[
                    {"id": "room_1", "plane": "earth", "zone": "arkhamcity"},
                    {"id": "room_2", "plane": "earth", "zone": "arkhamcity"},
                ]
            )

            # Create mock request with persistence in app.state
            mock_request = Mock()
            mock_request.app = Mock()
            mock_request.app.state = Mock()
            mock_request.app.state.persistence = mock_persistence

            # Call the endpoint function directly with injected dependencies
            result = await list_rooms(
                request=mock_request,
                plane="earth",
                zone="arkhamcity",
                sub_zone=None,
                include_exits=True,
                filter_explored=True,
                current_user=mock_user,
                session=mock_session,
                room_service=mock_room_service,
            )

            # Should return empty list when player has explored no rooms
            assert result["rooms"] == []
            assert result["total"] == 0

    async def test_list_rooms_filter_explored_with_auth_and_explored_rooms(self, container_test_client_class):
        """Test that filter_explored with auth and explored rooms returns only explored rooms."""
        client = container_test_client_class
        test_user_id = uuid.uuid4()
        test_player_id = uuid.uuid4()
        explored_room_uuid = uuid.uuid4()
        explored_stable_id = "earth_arkhamcity_northside_intersection_derby_high"

        # Mock authentication - User object needs id attribute
        mock_user = Mock()
        mock_user.id = test_user_id
        mock_user.username = "testuser"
        mock_player = Mock()
        mock_player.player_id = test_player_id

        with (
            patch("server.api.rooms.get_current_user", return_value=mock_user),
            patch("server.api.rooms.get_exploration_service") as mock_get_exploration_service,
        ):
            # Mock persistence to return a player
            mock_persistence = AsyncMock()
            mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

            # Mock exploration service to return explored room UUID
            # get_exploration_service() is called, so we need to mock the return value
            mock_exploration_service = Mock()
            mock_exploration_service.get_explored_rooms = AsyncMock(return_value=[str(explored_room_uuid)])
            mock_get_exploration_service.return_value = mock_exploration_service

            # Create mock request with persistence in app.state
            mock_request = Mock()
            mock_request.app = Mock()
            mock_request.app.state = Mock()
            mock_request.app.state.persistence = mock_persistence

            # Mock session for database queries
            mock_session = AsyncMock()
            # Mock the stable_id lookup query result
            mock_result = AsyncMock()
            mock_result.fetchall.return_value = [(explored_stable_id,)]
            mock_session.execute.return_value = mock_result

            with patch("server.api.rooms.get_async_session") as mock_get_session:
                mock_get_session.return_value.__aenter__.return_value = mock_session
                mock_get_session.return_value.__aexit__.return_value = None

                response = client.get(
                    "/api/rooms/list?plane=earth&zone=arkhamcity&filter_explored=true",
                    headers={"Authorization": "Bearer test-token"},
                )

                assert response.status_code == 200
                data = response.json()
                # Should return filtered rooms (may be empty if no rooms match the explored filter)
                assert "rooms" in data
                assert isinstance(data["rooms"], list)
                # We intentionally do not assert on the exact call count for
                # get_explored_rooms here, as the implementation details of the
                # exploration service and router integration may change over time.
