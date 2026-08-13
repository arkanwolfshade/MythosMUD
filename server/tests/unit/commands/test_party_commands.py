"""Unit tests for party command handlers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.party_commands import (
    _get_member_display,
    _handle_party_chat,
    _handle_party_leave,
    handle_party_command,
)
from server.schemas.shared import TargetType as SchemaTargetType


def _party_request(player_id: uuid.UUID | None = None) -> tuple[MagicMock, MagicMock]:
    """Build request and container wired for party commands."""
    player_id = player_id or uuid.uuid4()
    request = MagicMock()
    app = MagicMock()
    state = MagicMock()
    container = MagicMock()

    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "Leader"

    async_persistence = AsyncMock()
    async_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

    party_service = MagicMock()
    container.party_service = party_service
    container.async_persistence = async_persistence

    request.app = app
    app.state = state
    state.container = container
    return request, container


@pytest.mark.asyncio
async def test_handle_party_command_no_party_service():
    """Party command rejected when party service is unavailable."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.container = MagicMock()
    request.app.state.container.party_service = None

    result = await handle_party_command({}, {"username": "alice"}, request, None, "alice")
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_command_player_not_in_game():
    """Party command rejected when player record is missing."""
    request, container = _party_request()
    container.async_persistence.get_player_by_name = AsyncMock(return_value=None)

    result = await handle_party_command({}, {"username": "ghost"}, request, None, "ghost")
    assert "not in the game" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_command_list_not_in_party():
    """Default party command shows not-in-party message."""
    request, container = _party_request()
    container.party_service.get_party_for_player.return_value = None

    result = await handle_party_command({}, {"username": "Leader"}, request, None, "Leader")
    assert "not in a party" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_command_list_with_members():
    """Party list shows members and leader suffix."""
    player_id = uuid.uuid4()
    request, container = _party_request(player_id)
    party = MagicMock()
    party.member_ids = [str(player_id), str(uuid.uuid4())]
    party.leader_id = str(player_id)
    container.party_service.get_party_for_player.return_value = party
    container.async_persistence.get_player_by_id = AsyncMock(return_value=MagicMock(name="Ally"))

    result = await handle_party_command({"subcommand": "list"}, {"username": "Leader"}, request, None, "Leader")
    assert "Your party:" in result["result"]
    assert "(leader)" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_command_leave():
    """Party leave removes member when in a party."""
    player_id = uuid.uuid4()
    request, container = _party_request(player_id)
    party = MagicMock()
    party.party_id = "party-1"
    container.party_service.get_party_for_player.return_value = party
    container.party_service.remove_member.return_value = {"result": "You have left the party."}

    result = await handle_party_command({"subcommand": "leave"}, {"username": "Leader"}, request, None, "Leader")
    assert "left the party" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_leave_not_in_party():
    """_handle_party_leave returns error when player has no party."""
    party_service = MagicMock()
    party_service.get_party_for_player.return_value = None
    result = _handle_party_leave(party_service, uuid.uuid4())
    assert "not in a party" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_chat_no_party():
    """Party chat rejected when sender is not in a party."""
    party_service = MagicMock()
    party_service.get_party_for_player.return_value = None
    result = await _handle_party_chat(MagicMock(), party_service, uuid.uuid4(), "id", "hello")
    assert "not in a party" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_chat_success():
    """Party chat sends message through chat service."""
    player_id = uuid.uuid4()
    party = MagicMock()
    party.party_id = "p1"
    party.member_ids = [str(player_id)]
    party_service = MagicMock()
    party_service.get_party_for_player.return_value = party
    container = MagicMock()
    chat_service = AsyncMock()
    chat_service.send_party_message = AsyncMock(return_value={"success": True})
    container.chat_service = chat_service

    result = await _handle_party_chat(container, party_service, player_id, str(player_id), "hello team")
    assert result["result"] == "Sent."


@pytest.mark.asyncio
async def test_handle_party_command_invite_no_target():
    """Party invite requires a target name."""
    request, container = _party_request()
    party = MagicMock()
    party.party_id = "p1"
    container.party_service.get_party_for_player.return_value = party
    container.party_service.is_leader.return_value = True

    result = await handle_party_command({"subcommand": "invite"}, {"username": "Leader"}, request, None, "Leader")
    assert "Invite whom" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_command_invite_success():
    """Party invite resolves target and sends invite request."""
    player_id = uuid.uuid4()
    target_id = uuid.uuid4()
    request, container = _party_request(player_id)
    party = MagicMock()
    party.party_id = "p1"
    container.party_service.get_party_for_player.return_value = party
    container.party_service.is_leader.return_value = True
    container.party_service.request_party_invite = AsyncMock(return_value={"success": True, "result": "Invite sent."})
    container.player_service = MagicMock()

    match = MagicMock()
    match.target_type = SchemaTargetType.PLAYER
    match.target_id = target_id
    target_result = MagicMock()
    target_result.success = True
    target_result.get_single_match.return_value = match

    with patch("server.commands.party_commands.TargetResolutionService") as mock_resolver:
        mock_resolver.return_value.resolve_target = AsyncMock(return_value=target_result)
        result = await handle_party_command(
            {"subcommand": "invite", "target": "Ally"},
            {"username": "Leader"},
            request,
            None,
            "Leader",
        )

    assert "Invite sent" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_command_kick_not_leader():
    """Party kick rejected when caller is not leader."""
    request, container = _party_request()
    container.party_service.get_party_for_player.return_value = MagicMock()
    container.party_service.is_leader.return_value = False

    result = await handle_party_command(
        {"subcommand": "kick", "target": "Ally"},
        {"username": "Leader"},
        request,
        None,
        "Leader",
    )
    assert "leader" in result["result"]


@pytest.mark.asyncio
async def test_handle_party_command_unknown_subcommand():
    """Unknown party subcommand returns usage message."""
    request, container = _party_request()
    container.party_service.get_party_for_player.return_value = MagicMock()

    result = await handle_party_command({"subcommand": "dance"}, {"username": "Leader"}, request, None, "Leader")
    assert "Usage:" in result["result"]


@pytest.mark.asyncio
async def test_get_member_display_invalid_uuid():
    """_get_member_display returns raw id when UUID parsing fails."""
    async_persistence = AsyncMock()
    result = await _get_member_display("not-a-uuid", async_persistence)
    assert result == "not-a-uuid"
