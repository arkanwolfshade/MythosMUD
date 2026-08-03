"""Unit tests for alias_expansion module."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.command_handler.alias_expansion import (
    check_alias_safety,
    handle_expanded_command,
    validate_expanded_command,
)


@pytest.mark.asyncio
async def test_check_alias_safety_cycle_detected() -> None:
    mock_storage = MagicMock()
    mock_graph = MagicMock()
    mock_graph.is_safe_to_expand.return_value = False
    mock_graph.detect_cycle.return_value = ["a", "b", "a"]

    with (
        patch("server.command_handler.alias_expansion.AliasGraph", return_value=mock_graph),
        patch("server.command_handler.alias_expansion.audit_logger") as audit,
    ):
        is_safe, error, depth = await check_alias_safety(mock_storage, "player1", "a")

    assert is_safe is False
    assert error is not None
    assert "circular dependency" in error.lower()
    assert depth == 0
    audit.log_alias_expansion.assert_called_once()


@pytest.mark.asyncio
async def test_check_alias_safety_depth_too_deep() -> None:
    mock_storage = MagicMock()
    mock_graph = MagicMock()
    mock_graph.is_safe_to_expand.return_value = True
    mock_graph.get_expansion_depth.return_value = 11

    with patch("server.command_handler.alias_expansion.AliasGraph", return_value=mock_graph):
        is_safe, error, depth = await check_alias_safety(mock_storage, "player1", "deep")

    assert is_safe is False
    assert "excessive expansion depth" in (error or "").lower()
    assert depth == 11


@pytest.mark.asyncio
async def test_check_alias_safety_ok() -> None:
    mock_storage = MagicMock()
    mock_graph = MagicMock()
    mock_graph.is_safe_to_expand.return_value = True
    mock_graph.get_expansion_depth.return_value = 2

    with patch("server.command_handler.alias_expansion.AliasGraph", return_value=mock_graph):
        is_safe, error, depth = await check_alias_safety(mock_storage, "player1", "look")

    assert is_safe is True
    assert error is None
    assert depth == 2


def test_validate_expanded_command_too_long() -> None:
    with (
        patch("server.command_handler.alias_expansion.MAX_EXPANDED_COMMAND_LENGTH", 5),
        patch("server.command_handler.alias_expansion.audit_logger") as audit,
    ):
        is_valid, error = validate_expanded_command("toolong", "player1", "alias1", 1)

    assert is_valid is False
    assert "too long" in (error or "").lower()
    audit.log_alias_expansion.assert_called_once()


def test_validate_expanded_command_invalid_content() -> None:
    with (
        patch(
            "server.command_handler.alias_expansion.CommandValidator.validate_expanded_command",
            return_value=(False, "dangerous"),
        ),
        patch("server.command_handler.alias_expansion.audit_logger") as audit,
    ):
        is_valid, error = validate_expanded_command("look", "player1", "alias1", 1)

    assert is_valid is False
    assert "blocked" in (error or "").lower()
    audit.log_security_event.assert_called_once()


def test_validate_expanded_command_ok() -> None:
    with patch(
        "server.command_handler.alias_expansion.CommandValidator.validate_expanded_command",
        return_value=(True, None),
    ):
        is_valid, error = validate_expanded_command("look north", "player1", "alias1", 1)

    assert is_valid is True
    assert error is None


@pytest.mark.asyncio
async def test_handle_expanded_command_depth_limit() -> None:
    result = await handle_expanded_command("look", {}, MagicMock(), MagicMock(), "player1", depth=11)
    assert result == {"result": "Alias expansion too deep - possible loop detected"}


@pytest.mark.asyncio
async def test_handle_expanded_command_delegates() -> None:
    mock_request = MagicMock()
    mock_storage = MagicMock()
    with patch(
        "server.command_handler.processing.process_command_with_validation",
        new_callable=AsyncMock,
        return_value={"result": "ok"},
    ) as mock_process:
        result = await handle_expanded_command(
            "look north", {"id": "u1"}, mock_request, mock_storage, "player1", depth=0
        )

    assert result == {"result": "ok"}
    mock_process.assert_awaited_once()
