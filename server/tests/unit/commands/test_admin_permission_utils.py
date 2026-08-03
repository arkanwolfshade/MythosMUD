"""Unit tests for admin permission validation."""

from unittest.mock import MagicMock, patch

import pytest

from server.commands.admin_permission_utils import validate_admin_permission


@pytest.fixture
def mock_admin_logger() -> MagicMock:
    logger = MagicMock()
    with patch("server.commands.admin_permission_utils.get_admin_actions_logger", return_value=logger):
        yield logger


@pytest.mark.asyncio
async def test_validate_admin_permission_no_player(mock_admin_logger: MagicMock) -> None:
    result = await validate_admin_permission(None, "MissingPlayer")
    assert result is False
    mock_admin_logger.log_permission_check.assert_called_once_with(
        player_name="MissingPlayer",
        action="admin_teleport",
        has_permission=False,
        additional_data={"error": "No player object"},
    )


@pytest.mark.asyncio
async def test_validate_admin_permission_missing_is_admin_attr(mock_admin_logger: MagicMock) -> None:
    player = object()
    result = await validate_admin_permission(player, "PlainObject")
    assert result is False
    mock_admin_logger.log_permission_check.assert_called_once()
    call_kwargs = mock_admin_logger.log_permission_check.call_args.kwargs
    assert call_kwargs["has_permission"] is False
    assert call_kwargs["additional_data"]["error"] == "No is_admin attribute"


@pytest.mark.asyncio
async def test_validate_admin_permission_is_admin_false(mock_admin_logger: MagicMock) -> None:
    player = MagicMock()
    player.is_admin = False
    result = await validate_admin_permission(player, "RegularPlayer")
    assert result is False
    mock_admin_logger.log_permission_check.assert_called_once_with(
        player_name="RegularPlayer",
        action="admin_teleport",
        has_permission=False,
        additional_data={"player_type": "MagicMock", "is_admin_value": False},
    )


@pytest.mark.asyncio
async def test_validate_admin_permission_granted(mock_admin_logger: MagicMock) -> None:
    player = MagicMock()
    player.is_admin = True
    result = await validate_admin_permission(player, "AdminPlayer")
    assert result is True
    mock_admin_logger.log_permission_check.assert_called_once_with(
        player_name="AdminPlayer",
        action="admin_teleport",
        has_permission=True,
        additional_data={"player_type": "MagicMock", "is_admin_value": True},
    )


class _BrokenAdminPlayer:
    @property
    def is_admin(self) -> bool:
        raise AttributeError("boom")


@pytest.mark.asyncio
async def test_validate_admin_permission_attribute_error(mock_admin_logger: MagicMock) -> None:
    result = await validate_admin_permission(_BrokenAdminPlayer(), "BrokenPlayer")
    assert result is False
    mock_admin_logger.log_permission_check.assert_called_once()
    assert mock_admin_logger.log_permission_check.call_args.kwargs["has_permission"] is False


@pytest.mark.asyncio
async def test_validate_admin_permission_logs_secondary_failure() -> None:
    admin_logger = MagicMock()
    admin_logger.log_permission_check.side_effect = OSError("log disk full")
    with patch("server.commands.admin_permission_utils.get_admin_actions_logger", return_value=admin_logger):
        result = await validate_admin_permission(_BrokenAdminPlayer(), "BrokenPlayer")
    assert result is False
