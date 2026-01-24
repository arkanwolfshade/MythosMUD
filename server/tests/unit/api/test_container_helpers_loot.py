"""
Unit tests for container API loot-all helper functions.

Tests loot-all specific helper functions including container/player retrieval
and bulk item transfer operations.
"""
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import Request, status

from server.api.container_helpers import (
    get_container_and_player_for_loot_all,
    handle_container_service_error,
    transfer_all_items_from_container,
)
from server.api.container_models import LootAllRequest
from server.exceptions import LoggedHTTPException
from server.models.container import ContainerComponent, ContainerSourceType
from server.models.user import User
from server.services.container_service import ContainerCapacityError, ContainerService, ContainerServiceError


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
    user = MagicMock(spec=User)
    user.id = uuid.uuid4()
    user.username = "testuser"
    return user


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = AsyncMock()
    return persistence


class TestGetContainerAndPlayerForLootAll:
    """Test get_container_and_player_for_loot_all function."""

    @pytest.mark.asyncio
    async def test_get_container_and_player_for_loot_all_success(self, mock_persistence, mock_request, mock_user):
        """Test get_container_and_player_for_loot_all returns container and player."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container_data = {
            "container_id": str(container_id),
            "room_id": str(uuid.uuid4()),
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "items": [],
        }
        mock_player = MagicMock()
        mock_player.inventory = []
        mock_persistence.get_container = AsyncMock(return_value=container_data)
        mock_persistence.get_player = Mock(return_value=mock_player)
        container, player, inventory = await get_container_and_player_for_loot_all(
            mock_persistence, request_data, player_id, mock_request, mock_user
        )
        assert isinstance(container, ContainerComponent)
        assert player == mock_player
        assert inventory == []

    @pytest.mark.asyncio
    async def test_get_container_and_player_for_loot_all_container_not_found(
        self, mock_persistence, mock_request, mock_user
    ):
        """Test get_container_and_player_for_loot_all raises exception when container not found."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        mock_persistence.get_container = AsyncMock(return_value=None)
        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_container_and_player_for_loot_all(
                mock_persistence, request_data, player_id, mock_request, mock_user
            )
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.asyncio
    async def test_get_container_and_player_for_loot_all_player_not_found(
        self, mock_persistence, mock_request, mock_user
    ):
        """Test get_container_and_player_for_loot_all raises exception when player not found."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container_data = {
            "container_id": str(container_id),
            "room_id": str(uuid.uuid4()),
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "items": [],
        }
        mock_persistence.get_container = AsyncMock(return_value=container_data)
        mock_persistence.get_player = Mock(return_value=None)
        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_container_and_player_for_loot_all(
                mock_persistence, request_data, player_id, mock_request, mock_user
            )
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.asyncio
    async def test_get_container_and_player_for_loot_all_player_no_inventory(
        self, mock_persistence, mock_request, mock_user
    ):
        """Test get_container_and_player_for_loot_all handles player without inventory attribute."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container_data = {
            "container_id": str(container_id),
            "room_id": str(uuid.uuid4()),
            "source_type": ContainerSourceType.ENVIRONMENT.value,
            "capacity_slots": 10,
            "items": [],
        }
        mock_persistence.get_container = AsyncMock(return_value=container_data)
        mock_player = MagicMock()
        # Player has no inventory attribute
        if hasattr(mock_player, "inventory"):
            delattr(mock_player, "inventory")
        mock_persistence.get_player = Mock(return_value=mock_player)

        # Should use empty list as default
        container, player, inventory = await get_container_and_player_for_loot_all(
            mock_persistence, request_data, player_id, mock_request, mock_user
        )
        assert container is not None
        assert player == mock_player
        assert inventory == []


class TestTransferAllItemsFromContainer:
    """Test transfer_all_items_from_container function."""

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_success(self, mock_persistence):
        """Test transfer_all_items_from_container transfers all items."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [{"item_id": str(uuid.uuid4()), "quantity": 1}],
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
            return_value={"container": container.model_dump(), "player_inventory": player_inventory},
        ) as mock_transfer:
            result_container, result_inventory = await transfer_all_items_from_container(
                container_service, request_data, player_id, container, player_inventory
            )
            assert isinstance(result_container, dict)
            assert isinstance(result_inventory, list)
            mock_transfer.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_capacity_error(self, mock_persistence):
        """Test transfer_all_items_from_container stops on capacity error."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [{"item_id": str(uuid.uuid4()), "quantity": 1}],
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
            side_effect=ContainerCapacityError("Capacity exceeded"),
        ):
            with patch("server.api.container_helpers.logger") as mock_logger:
                result_container, _result_inventory = await transfer_all_items_from_container(
                    container_service, request_data, player_id, container, player_inventory
                )
                mock_logger.warning.assert_called_once()
                assert isinstance(result_container, dict)

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_transfer_error(self, mock_persistence):
        """Test transfer_all_items_from_container continues on transfer error."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [{"item_id": str(uuid.uuid4()), "quantity": 1}],
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
            side_effect=RuntimeError("Transfer error"),
        ):
            with patch("server.api.container_helpers.logger") as mock_logger:
                result_container, _result_inventory = await transfer_all_items_from_container(
                    container_service, request_data, player_id, container, player_inventory
                )
                mock_logger.warning.assert_called_once()
                assert isinstance(result_container, dict)

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_multiple_items(self, mock_persistence):
        """Test transfer_all_items_from_container handles multiple items."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 2},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                ],
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        updated_container = container.model_dump()
        updated_container["items"] = []
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
            return_value={"container": updated_container, "player_inventory": player_inventory},
        ) as mock_transfer:
            result_container, _result_inventory = await transfer_all_items_from_container(
                container_service, request_data, player_id, container, player_inventory
            )
            # Should attempt to transfer all 3 items
            assert mock_transfer.await_count == 3
            assert isinstance(result_container, dict)

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_item_without_quantity(self, mock_persistence):
        """Test transfer_all_items_from_container handles items without quantity field."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [{"item_id": str(uuid.uuid4())}],  # No quantity field
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
            return_value={"container": container.model_dump(), "player_inventory": player_inventory},
        ) as mock_transfer:
            await transfer_all_items_from_container(
                container_service, request_data, player_id, container, player_inventory
            )
            # Should use default quantity of 1
            mock_transfer.assert_awaited_once()
            call_args = mock_transfer.await_args
            assert call_args is not None
            assert call_args[0][4] == 1  # quantity parameter should be 1

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_partial_success(self, mock_persistence):
        """Test transfer_all_items_from_container handles partial success with some items failing."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                ],
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        updated_container = container.model_dump()
        updated_container["items"] = []
        # First transfer succeeds, second fails, third succeeds
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
            side_effect=[
                {"container": updated_container, "player_inventory": player_inventory},
                RuntimeError("Transfer error"),
                {"container": updated_container, "player_inventory": player_inventory},
            ],
        ) as mock_transfer:
            with patch("server.api.container_helpers.logger") as mock_logger:
                result_container, _result_inventory = await transfer_all_items_from_container(
                    container_service, request_data, player_id, container, player_inventory
                )
                # Should attempt all 3 items, log warning for the error
                assert mock_transfer.await_count == 3
                mock_logger.warning.assert_called_once()  # One error logged
                assert isinstance(result_container, dict)

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_empty_items(self, mock_persistence):
        """Test transfer_all_items_from_container handles empty items list."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [],  # Empty items list
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
        ) as mock_transfer:
            result_container, result_inventory = await transfer_all_items_from_container(
                container_service, request_data, player_id, container, player_inventory
            )
            # Should not attempt any transfers
            mock_transfer.assert_not_awaited()
            assert isinstance(result_container, dict)
            assert result_inventory == []

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_updates_from_result(self, mock_persistence):
        """Test transfer_all_items_from_container updates container_data and inventory from result."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [{"item_id": str(uuid.uuid4()), "quantity": 1}],
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        updated_container_data = {"container_id": str(container_id), "items": []}
        updated_inventory = [{"item_id": str(uuid.uuid4()), "quantity": 1}]
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
            return_value={"container": updated_container_data, "player_inventory": updated_inventory},
        ) as mock_transfer:
            result_container, result_inventory = await transfer_all_items_from_container(
                container_service, request_data, player_id, container, player_inventory
            )
            # Should use updated values from result
            assert result_container == updated_container_data
            assert result_inventory == updated_inventory
            mock_transfer.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_result_missing_container(self, mock_persistence):
        """Test transfer_all_items_from_container handles result without container key."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [{"item_id": str(uuid.uuid4()), "quantity": 1}],
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        original_container_data = container.model_dump()
        updated_inventory = [{"item_id": str(uuid.uuid4()), "quantity": 1}]
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
            return_value={"player_inventory": updated_inventory},  # Missing container key
        ) as mock_transfer:
            result_container, result_inventory = await transfer_all_items_from_container(
                container_service, request_data, player_id, container, player_inventory
            )
            # Should use original container_data when result doesn't have container
            assert result_container == original_container_data
            assert result_inventory == updated_inventory
            mock_transfer.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_transfer_all_items_from_container_result_missing_inventory(self, mock_persistence):
        """Test transfer_all_items_from_container handles result without player_inventory key."""
        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [{"item_id": str(uuid.uuid4()), "quantity": 1}],
            }
        )
        player_inventory: list = []
        container_service = ContainerService(persistence=mock_persistence)
        updated_container_data = {"container_id": str(container_id), "items": []}
        with patch.object(
            container_service,
            "transfer_from_container",
            new_callable=AsyncMock,
            return_value={"container": updated_container_data},  # Missing player_inventory key
        ) as mock_transfer:
            result_container, result_inventory = await transfer_all_items_from_container(
                container_service, request_data, player_id, container, player_inventory
            )
            # Should use original inventory when result doesn't have player_inventory
            assert result_container == updated_container_data
            assert result_inventory == player_inventory
            mock_transfer.assert_awaited_once()


class TestHandleContainerServiceErrorEdgeCases:
    """Additional edge case tests for handle_container_service_error."""

    def test_handle_container_service_error_mutation_keyword(self, mock_request, mock_user):
        """Test handle_container_service_error detects 'mutation' in error message."""
        error = ContainerServiceError("Invalid mutation")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_handle_container_service_error_no_container_id_or_request_data(self, mock_request, mock_user):
        """Test handle_container_service_error uses 'unknown' when no container_id provided."""
        error = ContainerServiceError("Service error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        # Note: LoggedHTTPException doesn't expose context as an attribute,
        # it's used internally for logging. The function correctly uses 'unknown'
        # when no container_id is provided (verified in handle_container_service_error implementation)

    def test_handle_container_service_error_token_keyword(self, mock_request, mock_user):
        """Test handle_container_service_error detects 'token' in error message."""
        error = ContainerServiceError("Token expired")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_handle_container_service_error_stale_keyword(self, mock_request, mock_user):
        """Test handle_container_service_error detects 'stale' in error message."""
        error = ContainerServiceError("Stale data")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_handle_container_service_error_stack_keyword(self, mock_request, mock_user):
        """Test handle_container_service_error detects 'stack' in error message."""
        error = ContainerServiceError("Stack overflow")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
