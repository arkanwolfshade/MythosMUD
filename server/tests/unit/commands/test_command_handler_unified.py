"""
Unit tests for unified command handler.

Tests core command processing, HTTP endpoints, and legacy compatibility.
"""

import uuid
from types import SimpleNamespace
from typing import cast
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import HTTPException, Request
from pydantic import ValidationError

from server.command_handler_unified import (
    CommandRequest,
    get_help_content,
    handle_command,
    process_command,
    process_command_unified,
)
from server.models.user import User

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing


def test_command_request_rejects_unknown_field() -> None:
    """#755: CommandRequest inherits SecureBaseModel - an extra field must be rejected."""
    with pytest.raises(ValidationError):
        _ = CommandRequest.model_validate({"command": "look", "unexpected_field": "nope"})


class TestLegacyFunctions:
    """Test legacy compatibility functions."""

    @pytest.mark.asyncio
    async def test_process_command_legacy(self):
        """Test process_command() legacy function."""
        mock_current_user = {"username": "testuser"}
        mock_request = Mock(spec=Request)
        mock_alias_storage = MagicMock()
        player_name = "testuser"

        with patch("server.command_handler_unified.process_command_unified") as mock_unified:
            mock_unified.return_value = {"result": "Success"}
            result = await process_command(
                cmd="look",
                args=[],
                current_user=mock_current_user,
                request=mock_request,
                alias_storage=mock_alias_storage,
                player_name=player_name,
            )
            assert "result" in result
            mock_unified.assert_awaited_once()

    def test_get_help_content(self):
        """Test get_help_content() delegates to help system."""
        with patch("server.command_handler_unified.get_help_content_new", return_value="Help text"):
            result = get_help_content("look")
            assert result == "Help text"

    def test_get_help_content_none(self):
        """Test get_help_content() with None command."""
        with patch("server.command_handler_unified.get_help_content_new", return_value="General help"):
            result = get_help_content(None)
            assert result == "General help"


class TestProcessCommandUnified:
    """Test process_command_unified function."""

    @pytest.mark.asyncio
    async def test_process_command_unified_rate_limited(self):
        """Test process_command_unified returns rate limit result."""
        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        with patch(
            "server.command_handler_unified._prepare_command_for_processing",
            return_value=("", "", [], None, {"result": "Rate limited"}),
        ):
            result = await process_command_unified("look", mock_user, mock_request)
            assert result == {"result": "Rate limited"}

    @pytest.mark.asyncio
    async def test_process_command_unified_blocked(self):
        """Test process_command_unified returns block result."""
        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        with (
            patch(
                "server.command_handler_unified._prepare_command_for_processing",
                return_value=("look", "look", [], None, None),
            ),
            patch("server.command_handler_unified._check_all_command_blocks", return_value={"result": "Blocked"}),
        ):
            result = await process_command_unified("look", mock_user, mock_request)
            assert result == {"result": "Blocked"}

    @pytest.mark.asyncio
    async def test_process_command_unified_special_routing(self):
        """Test process_command_unified handles special command routing."""
        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        with (
            patch(
                "server.command_handler_unified._prepare_command_for_processing",
                return_value=("alias test=look", "alias", ["test=look"], MagicMock(), None),
            ),
            patch("server.command_handler_unified._check_all_command_blocks", return_value=None),
            patch(
                "server.command_handler_unified._handle_special_command_routing", return_value={"result": "Alias set"}
            ),
        ):
            result = await process_command_unified("alias test=look", mock_user, mock_request)
            assert result == {"result": "Alias set"}

    @pytest.mark.asyncio
    async def test_process_command_unified_normal_processing(self):
        """Test process_command_unified processes normal commands."""
        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        with (
            patch(
                "server.command_handler_unified._prepare_command_for_processing",
                return_value=("look", "look", [], None, None),
            ),
            patch("server.command_handler_unified._check_all_command_blocks", return_value=None),
            patch("server.command_handler_unified._handle_special_command_routing", return_value=None),
            patch(
                "server.command_handler_unified.process_command_with_validation",
                return_value={"result": "You look around"},
            ),
        ):
            result = await process_command_unified("look", mock_user, mock_request)
            assert result == {"result": "You look around"}


class TestHandleCommand:
    """Test handle_command HTTP endpoint."""

    @pytest.mark.asyncio
    async def test_handle_command_unauthorized(self):
        """Test handle_command raises HTTPException when not authenticated."""

        mock_request = MagicMock()

        with pytest.raises(HTTPException, match="Authentication required"):
            # None represents an unauthenticated user - handle_command's `if not current_user`
            # check raises before current_user is ever read further, so None exercises the
            # same branch a falsy stand-in did while satisfying the real User | None type.
            _ = await handle_command(CommandRequest(command="look"), mock_request, None)

    @pytest.mark.asyncio
    async def test_handle_command_success(self):
        """Test handle_command successfully processes command."""
        mock_request = MagicMock()
        # get_username_from_user(user_obj: object) genuinely accepts this dict shape at
        # runtime; handle_command's own signature just narrows current_user to User | None
        # (FastAPI's real dependency type). Cast the duck-typed double through object rather
        # than building a full User, matching the existing test_professions_endpoints.py precedent.
        mock_user = cast(User, cast(object, {"username": "testplayer"}))

        with patch("server.command_handler_unified.process_command_unified", return_value={"result": "Success"}):
            result = await handle_command(CommandRequest(command="look"), mock_request, mock_user)
            assert result == {"result": "Success"}


class TestHandleCommandCharacterId:
    """MULTI-CHARACTER: the command acts as the selected character, not the account username."""

    @staticmethod
    def _user(user_id: uuid.UUID | str) -> User:
        """Duck-typed account: get_username_from_user reads .username, ownership reads .id."""
        return cast(User, cast(object, SimpleNamespace(id=user_id, username="ArkanWolfshade")))

    @staticmethod
    def _persistence(player: object | None) -> MagicMock:
        persistence = MagicMock()
        persistence.get_player_by_id = AsyncMock(return_value=player)
        return persistence

    @pytest.mark.asyncio
    async def test_commands_run_as_the_selected_character(self):
        """A character named differently from the account (Arkan_Lovecraft vs ArkanWolfshade) is resolved by id."""
        user_id, character_id = uuid.uuid4(), uuid.uuid4()
        player = SimpleNamespace(user_id=user_id, is_deleted=False, name="Arkan_Lovecraft")

        with (
            patch(
                "server.command_handler_unified.get_container_async_persistence",
                return_value=self._persistence(player),
            ),
            patch("server.command_handler_unified.process_command_unified", new_callable=AsyncMock) as process,
        ):
            process.return_value = {"result": "Logged out successfully"}
            request = CommandRequest(command="logout", character_id=str(character_id))
            _ = await handle_command(request, MagicMock(), self._user(user_id))

        assert process.await_args is not None
        assert process.await_args.kwargs["player_name"] == "Arkan_Lovecraft"

    @pytest.mark.asyncio
    async def test_without_character_id_falls_back_to_the_account_username(self):
        with patch("server.command_handler_unified.process_command_unified", new_callable=AsyncMock) as process:
            process.return_value = {"result": "ok"}
            _ = await handle_command(CommandRequest(command="look"), MagicMock(), self._user(uuid.uuid4()))

        assert process.await_args is not None
        assert process.await_args.kwargs["player_name"] == "ArkanWolfshade"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ("character_id", "player", "expected_status"),
        [
            ("not-a-uuid", None, 400),
            (str(uuid.uuid4()), None, 404),
            (str(uuid.uuid4()), SimpleNamespace(user_id="owner", is_deleted=True, name="Gone"), 404),
            (str(uuid.uuid4()), SimpleNamespace(user_id="someone-else", is_deleted=False, name="Theirs"), 403),
        ],
    )
    async def test_rejects_unusable_characters(self, character_id: str, player: object | None, expected_status: int):
        """Unknown, deleted, malformed and other users' characters never reach the command pipeline."""
        with (
            patch(
                "server.command_handler_unified.get_container_async_persistence",
                return_value=self._persistence(player),
            ),
            patch("server.command_handler_unified.process_command_unified", new_callable=AsyncMock) as process,
            pytest.raises(HTTPException) as exc_info,
        ):
            request = CommandRequest(command="logout", character_id=character_id)
            _ = await handle_command(request, MagicMock(), self._user("owner"))

        assert exc_info.value.status_code == expected_status
        process.assert_not_awaited()
