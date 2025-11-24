"""
Tests for container API endpoints.

As documented in the restricted archives of Miskatonic University, container
API endpoints require thorough testing to ensure proper security and
compliance with forbidden artifact handling protocols.
"""

from __future__ import annotations

import uuid
from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI, status
from fastapi.testclient import TestClient

from server.api.containers import container_router
from server.models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from server.models.user import User
from server.services.container_service import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerServiceError,
)


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def sample_player_id():
    """Generate a sample player UUID."""
    return uuid.uuid4()


@pytest.fixture
def sample_container_id():
    """Generate a sample container UUID."""
    return uuid.uuid4()


@pytest.fixture
def sample_room_id():
    """Return a sample room ID."""
    return "earth_arkhamcity_sanitarium_room_foyer_001"


@pytest.fixture
def sample_environment_container(sample_container_id, sample_room_id):
    """Create a sample environmental container."""
    return ContainerComponent(
        container_id=sample_container_id,
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id=sample_room_id,
        capacity_slots=8,
        lock_state=ContainerLockState.UNLOCKED,
        items=[],
    )


@pytest.fixture
def authenticated_user(sample_player_id):
    """Create a mock authenticated user."""
    user = User(
        id=uuid.uuid4(),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
    )
    return user


@pytest.fixture
def mock_player(sample_player_id):
    """Create a mock player object."""
    player = MagicMock()
    player.player_id = sample_player_id
    player.inventory = []
    return player


@pytest.fixture
def test_client(mock_persistence, authenticated_user, mock_player):
    """Create a test client with mocked dependencies."""
    app = FastAPI()
    app.include_router(container_router)

    # Mock get_current_user
    async def get_current_user_override():
        return authenticated_user

    # Mock persistence.get_player_by_user_id
    def get_player_by_user_id_override(user_id: str):
        return mock_player

    mock_persistence.get_player_by_user_id = get_player_by_user_id_override

    # Override dependencies - FastAPI routers don't have a dependencies list
    # Override get_current_user directly
    from server.auth.users import get_current_user
    app.dependency_overrides[get_current_user] = get_current_user_override

    with patch("server.api.containers.get_persistence", return_value=mock_persistence):
        with patch("server.dependencies.get_persistence", return_value=mock_persistence):
            client = TestClient(app)
            yield client

    # Clean up
    app.dependency_overrides.clear()


class TestContainerOpenEndpoint:
    """Test POST /api/containers/open endpoint."""

    def test_open_container_success(
        self,
        test_client,
        mock_persistence,
        sample_container_id,
        sample_environment_container,
        authenticated_user,
        mock_player,
    ):
        """Test successfully opening a container."""
        mutation_token = str(uuid.uuid4())

        # Mock container service
        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.open_container.return_value = {
                "container": sample_environment_container.model_dump(),
                "mutation_token": mutation_token,
            }
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/open",
                json={"container_id": str(sample_container_id)},
            )

            assert response.status_code == status.HTTP_200_OK
            data = response.json()
            assert "container" in data
            assert "mutation_token" in data
            assert data["mutation_token"] == mutation_token

    def test_open_container_not_found(
        self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player
    ):
        """Test opening a non-existent container."""
        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.open_container.side_effect = ContainerNotFoundError("Container not found")
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/open",
                json={"container_id": str(sample_container_id)},
            )

            assert response.status_code == status.HTTP_404_NOT_FOUND
            assert "not found" in response.json()["detail"].lower()

    def test_open_container_locked(
        self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player
    ):
        """Test opening a locked container."""
        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.open_container.side_effect = ContainerLockedError("Container is locked")
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/open",
                json={"container_id": str(sample_container_id)},
            )

            assert response.status_code == status.HTTP_423_LOCKED
            assert "locked" in response.json()["detail"].lower()

    def test_open_container_access_denied(
        self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player
    ):
        """Test opening a container with access denied."""
        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.open_container.side_effect = ContainerAccessDeniedError("Access denied")
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/open",
                json={"container_id": str(sample_container_id)},
            )

            assert response.status_code == status.HTTP_403_FORBIDDEN
            assert "access" in response.json()["detail"].lower()

    def test_open_container_already_open(
        self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player
    ):
        """Test opening a container that is already open."""
        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.open_container.side_effect = ContainerServiceError("Container already open")
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/open",
                json={"container_id": str(sample_container_id)},
            )

            assert response.status_code == status.HTTP_409_CONFLICT
            assert "already" in response.json()["detail"].lower()


class TestContainerTransferEndpoint:
    """Test POST /api/containers/transfer endpoint."""

    def test_transfer_to_container_success(
        self,
        test_client,
        mock_persistence,
        sample_container_id,
        sample_environment_container,
        authenticated_user,
        mock_player,
    ):
        """Test successfully transferring items to container."""
        mutation_token = str(uuid.uuid4())
        item = {
            "item_instance_id": "inst_001",
            "prototype_id": "elder_sign",
            "item_id": "elder_sign",
            "item_name": "Elder Sign",
            "slot_type": "backpack",
            "quantity": 1,
        }

        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.transfer_to_container.return_value = {
                "container": sample_environment_container.model_dump(),
                "player_inventory": [],
            }
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/transfer",
                json={
                    "container_id": str(sample_container_id),
                    "mutation_token": mutation_token,
                    "direction": "to_container",
                    "stack": item,
                    "quantity": 1,
                },
            )

            assert response.status_code == status.HTTP_200_OK
            data = response.json()
            assert "container" in data
            assert "player_inventory" in data

    def test_transfer_from_container_success(
        self,
        test_client,
        mock_persistence,
        sample_container_id,
        sample_environment_container,
        authenticated_user,
        mock_player,
    ):
        """Test successfully transferring items from container."""
        mutation_token = str(uuid.uuid4())
        item = {
            "item_instance_id": "inst_001",
            "prototype_id": "elder_sign",
            "item_id": "elder_sign",
            "item_name": "Elder Sign",
            "slot_type": "backpack",
            "quantity": 1,
        }

        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.transfer_from_container.return_value = {
                "container": sample_environment_container.model_dump(),
                "player_inventory": [item],
            }
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/transfer",
                json={
                    "container_id": str(sample_container_id),
                    "mutation_token": mutation_token,
                    "direction": "to_player",
                    "stack": item,
                    "quantity": 1,
                },
            )

            assert response.status_code == status.HTTP_200_OK
            data = response.json()
            assert "container" in data
            assert "player_inventory" in data

    def test_transfer_capacity_exceeded(
        self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player
    ):
        """Test transfer when capacity is exceeded."""
        mutation_token = str(uuid.uuid4())
        item = {
            "item_instance_id": "inst_001",
            "prototype_id": "elder_sign",
            "item_id": "elder_sign",
            "item_name": "Elder Sign",
            "slot_type": "backpack",
            "quantity": 1,
        }

        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.transfer_to_container.side_effect = ContainerCapacityError("Capacity exceeded")
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/transfer",
                json={
                    "container_id": str(sample_container_id),
                    "mutation_token": mutation_token,
                    "direction": "to_container",
                    "stack": item,
                    "quantity": 1,
                },
            )

            assert response.status_code == status.HTTP_409_CONFLICT
            assert "capacity" in response.json()["detail"].lower()

    def test_transfer_invalid_direction(self, test_client, sample_container_id):
        """Test transfer with invalid direction."""
        mutation_token = str(uuid.uuid4())
        item = {
            "item_instance_id": "inst_001",
            "prototype_id": "elder_sign",
            "item_id": "elder_sign",
            "item_name": "Elder Sign",
            "slot_type": "backpack",
            "quantity": 1,
        }

        response = test_client.post(
            "/api/containers/transfer",
            json={
                "container_id": str(sample_container_id),
                "mutation_token": mutation_token,
                "direction": "invalid_direction",
                "stack": item,
                "quantity": 1,
            },
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestContainerCloseEndpoint:
    """Test POST /api/containers/close endpoint."""

    def test_close_container_success(
        self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player
    ):
        """Test successfully closing a container."""
        mutation_token = str(uuid.uuid4())

        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.close_container.return_value = None
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/close",
                json={
                    "container_id": str(sample_container_id),
                    "mutation_token": mutation_token,
                },
            )

            assert response.status_code == status.HTTP_200_OK
            data = response.json()
            assert data["status"] == "closed"

    def test_close_container_not_found(
        self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player
    ):
        """Test closing a non-existent container."""
        mutation_token = str(uuid.uuid4())

        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.close_container.side_effect = ContainerNotFoundError("Container not found")
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/close",
                json={
                    "container_id": str(sample_container_id),
                    "mutation_token": mutation_token,
                },
            )

            assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_close_container_invalid_token(
        self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player
    ):
        """Test closing a container with invalid token."""
        mutation_token = str(uuid.uuid4())

        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.close_container.side_effect = ContainerServiceError("Invalid token")
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/close",
                json={
                    "container_id": str(sample_container_id),
                    "mutation_token": mutation_token,
                },
            )

            assert response.status_code == status.HTTP_400_BAD_REQUEST
            assert "token" in response.json()["detail"].lower()


class TestContainerLootAllEndpoint:
    """Test POST /api/containers/loot-all endpoint."""

    def test_loot_all_success(
        self,
        test_client,
        mock_persistence,
        sample_container_id,
        sample_environment_container,
        authenticated_user,
        mock_player,
    ):
        """Test successfully looting all items from container."""
        mutation_token = str(uuid.uuid4())

        # Mock container data
        mock_persistence.get_container.return_value = sample_environment_container.model_dump()
        mock_persistence.get_player.return_value = mock_player

        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.transfer_from_container.return_value = {
                "container": sample_environment_container.model_dump(),
                "player_inventory": [
                    {
                        "item_instance_id": "inst_001",
                        "prototype_id": "elder_sign",
                        "item_id": "elder_sign",
                        "item_name": "Elder Sign",
                        "slot_type": "backpack",
                        "quantity": 1,
                    },
                ],
            }
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/loot-all",
                json={
                    "container_id": str(sample_container_id),
                    "mutation_token": mutation_token,
                },
            )

            assert response.status_code == status.HTTP_200_OK
            data = response.json()
            assert "container" in data
            assert "player_inventory" in data

    def test_loot_all_capacity_exceeded(
        self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player
    ):
        """Test loot-all when player inventory capacity is exceeded."""
        mutation_token = str(uuid.uuid4())

        # Mock container with items
        container_with_items = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="test_room",
            capacity_slots=8,
            items=[
                {
                    "item_instance_id": "inst_001",
                    "prototype_id": "elder_sign",
                    "item_id": "elder_sign",
                    "item_name": "Elder Sign",
                    "slot_type": "backpack",
                    "quantity": 1,
                },
            ],
        )

        mock_persistence.get_container.return_value = container_with_items.model_dump()
        mock_persistence.get_player.return_value = mock_player

        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.transfer_from_container.side_effect = ContainerCapacityError("Player inventory full")
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/loot-all",
                json={
                    "container_id": str(sample_container_id),
                    "mutation_token": mutation_token,
                },
            )

            # Should return 200 with partial transfer, or 409 if first item fails
            assert response.status_code in (status.HTTP_200_OK, status.HTTP_409_CONFLICT)

    def test_loot_all_locked(self, test_client, mock_persistence, sample_container_id, authenticated_user, mock_player):
        """Test loot-all when container is locked."""
        mutation_token = str(uuid.uuid4())

        mock_persistence.get_container.return_value = None

        with patch("server.api.containers._get_container_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.transfer_from_container.side_effect = ContainerLockedError("Container is locked")
            mock_get_service.return_value = mock_service

            response = test_client.post(
                "/api/containers/loot-all",
                json={
                    "container_id": str(sample_container_id),
                    "mutation_token": mutation_token,
                },
            )

            # Should handle gracefully or return 404 if container not found
            assert response.status_code in (status.HTTP_404_NOT_FOUND, status.HTTP_423_LOCKED)
