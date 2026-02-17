"""
Unit tests for container loot-all endpoint (register and extended behaviors).

Tests register_loot_endpoints and additional loot_all_items behaviors
(items_looted calculation, source types, logging, audit/emit error handling).
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import APIRouter

# Ensure module under test is loaded so patch("server.api.container_endpoints_loot.*") can resolve.
import server.api.container_endpoints_loot  # noqa: F401
from server.exceptions import LoggedHTTPException
from server.models.container import ContainerComponent

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice


class TestRegisterLootEndpoints:
    """Tests for register_loot_endpoints function."""

    def test_register_loot_endpoints(self):
        """Test register_loot_endpoints registers the endpoint."""
        from server.api.container_endpoints_loot import register_loot_endpoints  # noqa: E402

        router = APIRouter()
        register_loot_endpoints(router)

        routes = list(router.routes)
        assert len(routes) == 1
        from fastapi.routing import APIRoute

        if isinstance(routes[0], APIRoute):
            assert routes[0].path == "/loot-all"
            assert routes[0].methods == {"POST"}

    @pytest.mark.asyncio
    async def test_loot_all_items_audit_log_error_handled(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items handles audit log errors gracefully."""
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
            mock_audit.side_effect = Exception("Audit log error")

            result = await loot_all_items(
                request_data=request_data,
                request=mock_request,
                current_user=mock_user,
                persistence=mock_persistence,
                connection_manager=mock_connection_manager,
            )

            assert result is not None
            assert "items_looted" in result.model_dump()

    @pytest.mark.asyncio
    async def test_loot_all_items_calculates_items_looted_correctly(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_player
    ):
        """Test loot_all_items correctly calculates items_looted count."""
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        original_container = MagicMock(spec=ContainerComponent)
        original_container.items = [
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
        ]
        original_container.container_id = container_id

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

            assert result is not None
            assert result.items_looted == 2

    @pytest.mark.asyncio
    async def test_loot_all_items_empty_container(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_player
    ):
        """Test loot_all_items handles empty container correctly."""
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

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

            assert result is not None
            assert result.items_looted == 0

    @pytest.mark.asyncio
    async def test_loot_all_items_all_items_looted(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_player
    ):
        """Test loot_all_items when all items are successfully looted."""
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        original_container = MagicMock(spec=ContainerComponent)
        original_container.items = [
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
            {"item_id": str(uuid.uuid4()), "quantity": 1},
        ]
        original_container.container_id = container_id

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

            assert result is not None
            assert result.items_looted == 5

    @pytest.mark.asyncio
    async def test_loot_all_items_different_source_types(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items with different container source types."""
        from server.api.container_endpoints_loot import loot_all_items  # noqa: E402
        from server.api.container_models import LootAllRequest  # noqa: E402
        from server.models.container import ContainerSourceType  # noqa: E402

        container_id = uuid.uuid4()
        player_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

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

            assert result is not None
            assert result.items_looted == 1

    @pytest.mark.asyncio
    async def test_loot_all_items_logger_info_called(
        self, mock_request, mock_user, mock_persistence, mock_connection_manager, mock_container, mock_player
    ):
        """Test loot_all_items calls logger.info with correct parameters."""
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
