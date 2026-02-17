"""
Unit tests for container loot-all endpoint (core behaviors).

Tests loot_all_items success, validation, rate limiting, and error handling.
Extended tests (register, items_looted, source types, etc.) live in
test_container_endpoints_loot_register.py.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest

# Ensure module under test is loaded so patch("server.api.container_endpoints_loot.*") can resolve.
import server.api.container_endpoints_loot  # noqa: F401
from server.exceptions import LoggedHTTPException, RateLimitError
from server.models.container import ContainerComponent
from server.services.container_service import (
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
)

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice


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
