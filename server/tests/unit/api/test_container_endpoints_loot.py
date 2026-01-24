"""
Unit tests for container loot-all endpoint.

Tests the loot_all_items endpoint and register_loot_endpoints function.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import APIRouter, Request

from server.exceptions import LoggedHTTPException, RateLimitError
from server.models.container import ContainerComponent
from server.models.user import User
from server.services.container_service import (
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerService,
)

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    request = Mock(spec=Request)
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.fixture
def mock_user():
    """Create a mock user."""
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
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = AsyncMock()
    return persistence


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = AsyncMock()
    return manager


@pytest.fixture
def mock_container_service():
    """Create a mock container service."""
    service = MagicMock(spec=ContainerService)
    return service


@pytest.fixture
def mock_container():
    """Create a mock container component."""
    container = MagicMock(spec=ContainerComponent)
    container.container_id = uuid.uuid4()
    container.room_id = "room_001"
    container.items = [{"item_id": str(uuid.uuid4()), "quantity": 1}]
    container.source_type = MagicMock()
    container.source_type.value = "room"
    container.model_dump = Mock(return_value={"container_id": str(container.container_id), "items": []})
    container.model_validate = Mock(return_value=container)
    return container


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    return player


class TestLootAllItems:
    """Tests for loot_all_items endpoint."""

    @pytest.mark.asyncio
    async def test_loot_all_items_success(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items successfully transfers all items."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        # Mock container data with all required fields
        from server.models.container import ContainerSourceType  # noqa: E402

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "room_id": "room_001",
        }
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        final_container = MagicMock(spec=ContainerComponent)
        final_container.items = []
        final_container.model_dump = Mock(return_value=container_data)
        final_container.source_type = MagicMock()
        final_container.source_type.value = "room"
        final_container.room_id = "room_001"

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all") as mock_validate,
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all") as mock_rate_limit,
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service") as mock_get_service,
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.emit_loot_all_event", new_callable=AsyncMock) as mock_emit,
        ):
            mock_validate.return_value = None
            mock_rate_limit.return_value = None
            mock_get_player_id.return_value = player_id
            mock_get_service.return_value = MagicMock()
            mock_get_data.return_value = (mock_container, mock_player, [])
            mock_transfer.return_value = (mock_container, [])
            # Mock container data with all required fields

            container_data = {
                "container_id": str(container_id),
                "items": [],
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "room_id": "room_001",
            }
            mock_persistence.get_container = AsyncMock(return_value=container_data)

            result = await loot_all_items(
                request_data=request_data,
                request=mock_request,
                current_user=mock_user,
                persistence=mock_persistence,
                connection_manager=mock_connection_manager,
            )

            assert result is not None
            assert "container" in result.model_dump()
            assert "player_inventory" in result.model_dump()
            assert "items_looted" in result.model_dump()
            mock_validate.assert_called_once()
            mock_rate_limit.assert_called_once()
            mock_emit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_loot_all_items_validation_error(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager
    ):
        """Test loot_all_items raises error when user validation fails."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all") as mock_validate,
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
        ):
            mock_validate.side_effect = LoggedHTTPException(status_code=403, detail="Access denied", context=None)

            with pytest.raises(LoggedHTTPException) as exc_info:
                await loot_all_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=mock_persistence,
                    connection_manager=mock_connection_manager,
                )
            assert exc_info.value.status_code == 403

    @pytest.mark.asyncio
    async def test_loot_all_items_rate_limit_error(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager
    ):
        """Test loot_all_items raises error when rate limit exceeded."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all") as mock_rate_limit,
        ):
            mock_rate_limit.side_effect = RateLimitError("Rate limit exceeded")

            with pytest.raises(RateLimitError):
                await loot_all_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=mock_persistence,
                    connection_manager=mock_connection_manager,
                )

    @pytest.mark.asyncio
    async def test_loot_all_items_player_not_found(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager
    ):
        """Test loot_all_items raises error when player not found."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
        ):
            mock_get_player_id.side_effect = LoggedHTTPException(
                status_code=404, detail="Player not found for user", context=None
            )

            with pytest.raises(LoggedHTTPException) as exc_info:
                await loot_all_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=mock_persistence,
                    connection_manager=mock_connection_manager,
                )
            assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_loot_all_items_container_not_found(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_player
    ):
        """Test loot_all_items handles container not found error."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch("server.api.container_endpoints_loot.handle_loot_all_exceptions") as mock_handler,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.side_effect = ContainerNotFoundError("Container not found")

            # Exception handler should raise
            mock_handler.side_effect = LoggedHTTPException(status_code=404, detail="Container not found", context=None)

            with pytest.raises(LoggedHTTPException) as exc_info:
                await loot_all_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=mock_persistence,
                    connection_manager=mock_connection_manager,
                )
            assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_loot_all_items_capacity_error(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items handles capacity exceeded error."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.handle_loot_all_exceptions") as mock_handler,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.return_value = (mock_container, mock_player, [])
            mock_transfer.side_effect = ContainerCapacityError("Capacity exceeded")
            mock_handler.side_effect = LoggedHTTPException(status_code=409, detail="Capacity exceeded", context=None)

            with pytest.raises(LoggedHTTPException) as exc_info:
                await loot_all_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=mock_persistence,
                    connection_manager=mock_connection_manager,
                )
            assert exc_info.value.status_code == 409

    @pytest.mark.asyncio
    async def test_loot_all_items_locked_error(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_player
    ):
        """Test loot_all_items handles container locked error."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch("server.api.container_endpoints_loot.handle_loot_all_exceptions") as mock_handler,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.side_effect = ContainerLockedError("Container is locked")
            mock_handler.side_effect = LoggedHTTPException(status_code=423, detail="Container is locked", context=None)

            with pytest.raises(LoggedHTTPException) as exc_info:
                await loot_all_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=mock_persistence,
                    connection_manager=mock_connection_manager,
                )
            assert exc_info.value.status_code == 423

    @pytest.mark.asyncio
    async def test_loot_all_items_generic_exception(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_player
    ):
        """Test loot_all_items handles generic exceptions."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.handle_loot_all_exceptions") as mock_handler,
        ):
            mock_get_player_id.side_effect = RuntimeError("Unexpected error")
            mock_handler.side_effect = LoggedHTTPException(
                status_code=500, detail="Internal server error", context=None
            )

            with pytest.raises(LoggedHTTPException) as exc_info:
                await loot_all_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=mock_persistence,
                    connection_manager=mock_connection_manager,
                )
            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_loot_all_items_final_container_none(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items handles case when final container is None."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_persistence.get_container = AsyncMock(return_value=None)  # Container not found after transfer

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.emit_loot_all_event", new_callable=AsyncMock) as mock_emit,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.return_value = (mock_container, mock_player, [])
            mock_transfer.return_value = (mock_container, [])

            result = await loot_all_items(
                request_data=request_data,
                request=mock_request,
                current_user=mock_user,
                persistence=mock_persistence,
                connection_manager=mock_connection_manager,
            )

            # Should use original container when final_container is None
            assert result is not None
            mock_emit.assert_awaited_once()


class TestRegisterLootEndpoints:
    """Tests for register_loot_endpoints function."""

    def test_register_loot_endpoints(self):
        """Test register_loot_endpoints registers the endpoint."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import register_loot_endpoints  # noqa: E402

        router = APIRouter()
        register_loot_endpoints(router)

        # Verify route was registered
        routes = list(router.routes)
        assert len(routes) == 1
        # Type narrowing: FastAPI routes are APIRoute instances with path and methods
        from fastapi.routing import APIRoute

        if isinstance(routes[0], APIRoute):
            assert routes[0].path == "/loot-all"
            assert routes[0].methods == {"POST"}

    @pytest.mark.asyncio
    async def test_loot_all_items_audit_log_error_handled(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items handles audit log errors gracefully."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        from server.models.container import ContainerSourceType  # noqa: E402

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "room_id": "room_001",
        }
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        final_container = MagicMock(spec=ContainerComponent)
        final_container.items = []
        final_container.model_dump = Mock(return_value=container_data)
        final_container.source_type = MagicMock()
        final_container.source_type.value = "room"
        final_container.room_id = "room_001"

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.emit_loot_all_event", new_callable=AsyncMock),
            patch("server.api.container_endpoints_loot.audit_logger.log_container_interaction") as mock_audit,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.return_value = (mock_container, mock_player, [])
            mock_transfer.return_value = (mock_container, [])
            # Audit log should fail but not break the request
            mock_audit.side_effect = Exception("Audit log error")

            result = await loot_all_items(
                request_data=request_data,
                request=mock_request,
                current_user=mock_user,
                persistence=mock_persistence,
                connection_manager=mock_connection_manager,
            )

            # Should still succeed despite audit log error
            assert result is not None
            assert "items_looted" in result.model_dump()

    @pytest.mark.asyncio
    async def test_loot_all_items_calculates_items_looted_correctly(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items correctly calculates items_looted count."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        # Original container has 3 items
        original_container = MagicMock(spec=ContainerComponent)
        original_container.items = [
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
        ]
        original_container.container_id = container_id

        # Final container has 1 item (2 were looted)
        from server.models.container import ContainerSourceType  # noqa: E402

        final_container_data = {
            "container_id": str(container_id),
            "items": [{"item_id": str(uuid.uuid4()), "quantity": 1}],
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "room_id": "room_001",
        }
        mock_persistence.get_container = AsyncMock(return_value=final_container_data)

        final_container = MagicMock(spec=ContainerComponent)
        final_container.items = [{"item_id": str(uuid.uuid4()), "quantity": 1}]
        final_container.model_dump = Mock(return_value=final_container_data)
        final_container.source_type = MagicMock()
        final_container.source_type.value = "room"
        final_container.room_id = "room_001"

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.emit_loot_all_event", new_callable=AsyncMock),
            patch("server.api.container_endpoints_loot.ContainerComponent.model_validate") as mock_validate,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.return_value = (original_container, mock_player, [])
            mock_transfer.return_value = (original_container, [])
            mock_validate.return_value = final_container

            result = await loot_all_items(
                request_data=request_data,
                request=mock_request,
                current_user=mock_user,
                persistence=mock_persistence,
                connection_manager=mock_connection_manager,
            )

            # Should calculate 2 items looted (3 - 1)
            assert result is not None
            assert result.items_looted == 2

    @pytest.mark.asyncio
    async def test_loot_all_items_empty_container(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items handles empty container correctly."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        # Empty container
        empty_container = MagicMock(spec=ContainerComponent)
        empty_container.items = []
        empty_container.container_id = container_id

        from server.models.container import ContainerSourceType  # noqa: E402

        final_container_data = {
            "container_id": str(container_id),
            "items": [],
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "room_id": "room_001",
        }
        mock_persistence.get_container = AsyncMock(return_value=final_container_data)

        final_container = MagicMock(spec=ContainerComponent)
        final_container.items = []
        final_container.model_dump = Mock(return_value=final_container_data)
        final_container.source_type = MagicMock()
        final_container.source_type.value = "room"
        final_container.room_id = "room_001"

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.emit_loot_all_event", new_callable=AsyncMock),
            patch("server.api.container_endpoints_loot.ContainerComponent.model_validate") as mock_validate,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.return_value = (empty_container, mock_player, [])
            mock_transfer.return_value = (empty_container, [])
            mock_validate.return_value = final_container

            result = await loot_all_items(
                request_data=request_data,
                request=mock_request,
                current_user=mock_user,
                persistence=mock_persistence,
                connection_manager=mock_connection_manager,
            )

            # Should calculate 0 items looted (0 - 0)
            assert result is not None
            assert result.items_looted == 0

    @pytest.mark.asyncio
    async def test_loot_all_items_all_items_looted(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items when all items are successfully looted."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        # Original container has 5 items
        original_container = MagicMock(spec=ContainerComponent)
        original_container.items = [
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
        ]
        original_container.container_id = container_id

        # Final container is empty (all items looted)
        from server.models.container import ContainerSourceType  # noqa: E402

        final_container_data = {
            "container_id": str(container_id),
            "items": [],
            "source_type": ContainerSourceType.EQUIPMENT.value,
            "capacity_slots": 10,
            "room_id": None,
        }
        mock_persistence.get_container = AsyncMock(return_value=final_container_data)

        final_container = MagicMock(spec=ContainerComponent)
        final_container.items = []
        final_container.model_dump = Mock(return_value=final_container_data)
        final_container.source_type = MagicMock()
        final_container.source_type.value = "equipment"
        final_container.room_id = None

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.emit_loot_all_event", new_callable=AsyncMock),
            patch("server.api.container_endpoints_loot.ContainerComponent.model_validate") as mock_validate,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.return_value = (original_container, mock_player, [])
            mock_transfer.return_value = (original_container, [])
            mock_validate.return_value = final_container

            result = await loot_all_items(
                request_data=request_data,
                request=mock_request,
                current_user=mock_user,
                persistence=mock_persistence,
                connection_manager=mock_connection_manager,
            )

            # Should calculate 5 items looted (5 - 0)
            assert result is not None
            assert result.items_looted == 5

    @pytest.mark.asyncio
    async def test_loot_all_items_different_source_types(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items with different container source types."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402
        from server.models.container import ContainerSourceType  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        # Test CORPSE source type
        container_data = {
            "container_id": str(container_id),
            "items": [{"item_id": str(uuid.uuid4()), "quantity": 1}],
            "source_type": ContainerSourceType.CORPSE.value,
            "capacity_slots": 10,
            "room_id": "room_002",
        }
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        final_container = MagicMock(spec=ContainerComponent)
        final_container.items = []
        final_container.model_dump = Mock(return_value=container_data)
        final_container.source_type = MagicMock()
        final_container.source_type.value = "corpse"
        final_container.room_id = "room_002"

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.emit_loot_all_event", new_callable=AsyncMock),
            patch("server.api.container_endpoints_loot.ContainerComponent.model_validate") as mock_validate,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.return_value = (mock_container, mock_player, [])
            mock_transfer.return_value = (mock_container, [])
            mock_validate.return_value = final_container

            result = await loot_all_items(
                request_data=request_data,
                request=mock_request,
                current_user=mock_user,
                persistence=mock_persistence,
                connection_manager=mock_connection_manager,
            )

            # Should succeed with CORPSE source type
            assert result is not None
            assert result.items_looted == 1

    @pytest.mark.asyncio
    async def test_loot_all_items_logger_info_called(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items calls logger.info with correct parameters."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        from server.models.container import ContainerSourceType  # noqa: E402

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "room_id": "room_001",
        }
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        final_container = MagicMock(spec=ContainerComponent)
        final_container.items = []
        final_container.model_dump = Mock(return_value=container_data)
        final_container.source_type = MagicMock()
        final_container.source_type.value = "room"
        final_container.room_id = "room_001"

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.emit_loot_all_event", new_callable=AsyncMock),
            patch("server.api.container_endpoints_loot.ContainerComponent.model_validate") as mock_validate,
            patch("server.api.container_endpoints_loot.logger") as mock_logger,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.return_value = (mock_container, mock_player, [])
            mock_transfer.return_value = (mock_container, [])
            mock_validate.return_value = final_container

            await loot_all_items(
                request_data=request_data,
                request=mock_request,
                current_user=mock_user,
                persistence=mock_persistence,
                connection_manager=mock_connection_manager,
            )

            # Verify logger.info was called with correct parameters
            mock_logger.info.assert_called_once()
            call_args = mock_logger.info.call_args
            assert "Loot-all completed" in call_args[0][0]
            assert call_args[1]["container_id"] == str(container_id)
            assert call_args[1]["player_id"] == str(player_id)
            assert "items_transferred" in call_args[1]

    @pytest.mark.asyncio
    async def test_loot_all_items_emit_event_failure(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items when emit_loot_all_event raises an exception."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        from server.models.container import ContainerSourceType  # noqa: E402

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "room_id": "room_001",
        }
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        final_container = MagicMock(spec=ContainerComponent)
        final_container.items = []
        final_container.model_dump = Mock(return_value=container_data)
        final_container.source_type = MagicMock()
        final_container.source_type.value = "room"
        final_container.room_id = "room_001"

        with (
            patch("server.api.container_endpoints_loot.validate_user_for_loot_all"),
            patch("server.api.container_endpoints_loot.apply_rate_limiting_for_loot_all"),
            patch(
                "server.api.container_endpoints_loot.get_player_id_from_user", new_callable=AsyncMock
            ) as mock_get_player_id,
            patch("server.api.container_endpoints_loot.get_container_service"),
            patch(
                "server.api.container_endpoints_loot.get_container_and_player_for_loot_all", new_callable=AsyncMock
            ) as mock_get_data,
            patch(
                "server.api.container_endpoints_loot.transfer_all_items_from_container", new_callable=AsyncMock
            ) as mock_transfer,
            patch("server.api.container_endpoints_loot.emit_loot_all_event", new_callable=AsyncMock) as mock_emit,
            patch("server.api.container_endpoints_loot.ContainerComponent.model_validate") as mock_validate,
            patch("server.api.container_endpoints_loot.handle_loot_all_exceptions") as mock_handler,
        ):
            mock_get_player_id.return_value = player_id
            mock_get_data.return_value = (mock_container, mock_player, [])
            mock_transfer.return_value = (mock_container, [])
            mock_validate.return_value = final_container
            mock_emit.side_effect = RuntimeError("WebSocket error")
            mock_handler.side_effect = LoggedHTTPException(
                status_code=500, detail="Internal server error", context=None
            )

            with pytest.raises(LoggedHTTPException) as exc_info:
                await loot_all_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=mock_persistence,
                    connection_manager=mock_connection_manager,
                )
            assert exc_info.value.status_code == 500
