"""
Unit tests for command handler unified helper functions.

Tests helper functions, validation, rate limiting, and special command routing.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing


class TestHelperFunctions:
    """Test helper functions in command_handler_unified."""

    def test_check_rate_limit_allowed(self):
        """Test _check_rate_limit returns None when allowed."""
        from server.command_handler_unified import _check_rate_limit

        with patch("server.command_handler_unified.command_rate_limiter.is_allowed", return_value=True):
            result = _check_rate_limit("testplayer")
            assert result is None

    def test_check_rate_limit_blocked(self):
        """Test _check_rate_limit returns result when blocked."""
        from server.command_handler_unified import _check_rate_limit

        with (
            patch("server.command_handler_unified.command_rate_limiter.is_allowed", return_value=False),
            patch("server.command_handler_unified.command_rate_limiter.get_wait_time", return_value=5.0),
            patch("server.command_handler_unified.audit_logger.log_security_event") as mock_audit,
        ):
            result = _check_rate_limit("testplayer")
            assert result is not None
            assert "Too many commands" in result["result"]
            mock_audit.assert_called_once()

    def test_validate_command_basics_empty(self):
        """Test _validate_command_basics returns result for empty command."""
        from server.command_handler_unified import _validate_command_basics

        result = _validate_command_basics("", "testplayer")
        assert result == {"result": ""}

    def test_validate_command_basics_too_long(self):
        """Test _validate_command_basics returns result for command too long."""
        from server.command_handler import MAX_COMMAND_LENGTH
        from server.command_handler_unified import _validate_command_basics

        long_command = "a" * (MAX_COMMAND_LENGTH + 1)
        result = _validate_command_basics(long_command, "testplayer")
        assert result is not None
        assert "too long" in result["result"].lower()

    def test_validate_command_basics_invalid_content(self):
        """Test _validate_command_basics returns result for invalid content."""
        from server.command_handler_unified import _validate_command_basics

        with (
            patch(
                "server.command_handler_unified.CommandValidator.validate_command_content",
                return_value=(False, "Invalid"),
            ),
            patch("server.command_handler_unified.audit_logger.log_security_event") as mock_audit,
        ):
            result = _validate_command_basics("invalid command", "testplayer")
            assert result is not None
            assert result["result"] == "Invalid command format"
            mock_audit.assert_called_once()

    def test_validate_command_basics_valid(self):
        """Test _validate_command_basics returns None for valid command."""
        from server.command_handler_unified import _validate_command_basics

        with patch(
            "server.command_handler_unified.CommandValidator.validate_command_content", return_value=(True, None)
        ):
            result = _validate_command_basics("look", "testplayer")
            assert result is None

    def test_ensure_alias_storage_provided(self):
        """Test _ensure_alias_storage returns provided storage."""
        from server.alias_storage import AliasStorage
        from server.command_handler_unified import _ensure_alias_storage

        provided_storage = MagicMock(spec=AliasStorage)
        result = _ensure_alias_storage(provided_storage)
        assert result == provided_storage

    def test_ensure_alias_storage_creates_new(self):
        """Test _ensure_alias_storage creates new storage when None."""
        from server.command_handler_unified import _ensure_alias_storage

        with (
            patch("server.command_handler_unified.get_config") as mock_config,
            patch("server.command_handler_unified.AliasStorage") as mock_storage_class,
        ):
            mock_config.return_value.game.aliases_dir = "/test/aliases"
            mock_storage = MagicMock()
            mock_storage_class.return_value = mock_storage

            result = _ensure_alias_storage(None)
            assert result == mock_storage
            mock_storage_class.assert_called_once_with(storage_dir="/test/aliases")

    def test_ensure_alias_storage_handles_error(self):
        """Test _ensure_alias_storage returns None on error."""
        from server.command_handler_unified import _ensure_alias_storage

        with (
            patch("server.command_handler_unified.get_config", side_effect=OSError("Config error")),
            patch("server.command_handler_unified.logger") as mock_logger,
        ):
            result = _ensure_alias_storage(None)
            assert result is None
            mock_logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_check_grace_period_block_no_connection_manager(self):
        """Test _check_grace_period_block returns None when no connection manager."""
        from server.command_handler_unified import _check_grace_period_block

        mock_request = MagicMock()
        mock_request.app.state = MagicMock()
        delattr(mock_request.app.state, "connection_manager")

        result = await _check_grace_period_block("testplayer", mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_check_grace_period_block_not_in_grace_period(self):
        """Test _check_grace_period_block returns None when not in grace period."""
        from server.command_handler_unified import _check_grace_period_block

        mock_request = MagicMock()
        mock_connection_manager = MagicMock()
        mock_player_service = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = "test-id"

        mock_request.app.state.connection_manager = mock_connection_manager
        mock_request.app.state.player_service = mock_player_service
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)

        with patch("server.command_handler_unified.is_player_in_grace_period", return_value=False):
            result = await _check_grace_period_block("testplayer", mock_request)
            assert result is None

    def test_prepare_command_for_processing_rate_limited(self):
        """Test _prepare_command_for_processing returns rate limit result."""
        from server.command_handler_unified import _prepare_command_for_processing

        with patch("server.command_handler_unified._check_rate_limit", return_value={"result": "Rate limited"}):
            result = _prepare_command_for_processing("look", "testplayer", None)
            assert result[4] == {"result": "Rate limited"}

    def test_prepare_command_for_processing_validation_failed(self):
        """Test _prepare_command_for_processing returns validation result."""
        from server.command_handler_unified import _prepare_command_for_processing

        with (
            patch("server.command_handler_unified._check_rate_limit", return_value=None),
            patch("server.command_handler_unified._validate_command_basics", return_value={"result": "Invalid"}),
        ):
            result = _prepare_command_for_processing("", "testplayer", None)
            assert result[4] == {"result": "Invalid"}

    def test_prepare_command_for_processing_empty_after_cleaning(self):
        """Test _prepare_command_for_processing returns empty result after cleaning."""
        from server.command_handler_unified import _prepare_command_for_processing

        with (
            patch("server.command_handler_unified._check_rate_limit", return_value=None),
            patch("server.command_handler_unified._validate_command_basics", return_value=None),
            patch("server.command_handler_unified.clean_command_input", return_value=""),
        ):
            result = _prepare_command_for_processing("   ", "testplayer", None)
            assert result[4] == {"result": ""}

    def test_prepare_command_for_processing_success(self):
        """Test _prepare_command_for_processing successfully prepares command."""
        from server.command_handler_unified import _prepare_command_for_processing

        with (
            patch("server.command_handler_unified._check_rate_limit", return_value=None),
            patch("server.command_handler_unified._validate_command_basics", return_value=None),
            patch("server.command_handler_unified.clean_command_input", return_value="look around"),
            patch("server.command_handler_unified.normalize_command", return_value="look around"),
            patch("server.command_handler_unified._ensure_alias_storage", return_value=MagicMock()),
        ):
            _command_line, cmd, args, _alias_storage, error_result = _prepare_command_for_processing(
                "look around", "testplayer", None
            )
            assert error_result is None
            assert cmd == "look"
            assert "around" in args

    @pytest.mark.asyncio
    async def test_check_casting_state_allowed_commands(self):
        """Test _check_casting_state allows stop, interrupt, status during casting."""
        from server.command_handler_unified import _check_casting_state

        mock_request = MagicMock()
        for cmd in ["stop", "interrupt", "status"]:
            result = await _check_casting_state(cmd, "testplayer", mock_request)
            assert result is None

    @pytest.mark.asyncio
    async def test_check_casting_state_not_casting(self):
        """Test _check_casting_state returns None when player is not casting."""
        from server.command_handler_unified import _check_casting_state

        mock_request = MagicMock()
        mock_magic_service = MagicMock()
        mock_magic_service.casting_state_manager = MagicMock()
        mock_magic_service.casting_state_manager.is_casting = MagicMock(return_value=False)
        mock_request.app.state.magic_service = mock_magic_service

        result = await _check_casting_state("look", "testplayer", mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_check_casting_state_is_casting(self):
        """Test _check_casting_state returns block result when player is casting."""
        from server.command_handler_unified import _check_casting_state

        mock_request = MagicMock()
        mock_magic_service = MagicMock()
        mock_casting_manager = MagicMock()
        mock_casting_state = MagicMock()
        mock_casting_state.spell_name = "fireball"
        mock_casting_manager.is_casting = MagicMock(return_value=True)
        mock_casting_manager.get_casting_state = MagicMock(return_value=mock_casting_state)
        mock_magic_service.casting_state_manager = mock_casting_manager

        mock_player_service = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = "test-id"
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_request.app.state.magic_service = mock_magic_service
        mock_request.app.state.player_service = mock_player_service

        result = await _check_casting_state("look", "testplayer", mock_request)
        assert result is not None
        assert "casting" in result["result"].lower()
        assert "fireball" in result["result"]

    @pytest.mark.asyncio
    async def test_check_casting_state_no_magic_service(self):
        """Test _check_casting_state returns None when magic service is not available."""
        from server.command_handler_unified import _check_casting_state

        mock_request = MagicMock()
        mock_request.app.state.magic_service = None

        result = await _check_casting_state("look", "testplayer", mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_check_casting_state_error_handling(self):
        """Test _check_casting_state handles errors gracefully."""
        from server.command_handler_unified import _check_casting_state

        mock_request = MagicMock()
        mock_request.app.state.magic_service = MagicMock()
        mock_request.app.state.magic_service.casting_state_manager = None

        result = await _check_casting_state("look", "testplayer", mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_process_alias_expansion_no_storage(self):
        """Test _process_alias_expansion returns None when alias storage is None."""
        from server.command_handler_unified import _process_alias_expansion

        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}

        result = await _process_alias_expansion("look", [], None, "testplayer", mock_user, mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_process_alias_expansion_no_alias(self):
        """Test _process_alias_expansion returns None when alias doesn't exist."""
        from server.command_handler_unified import _process_alias_expansion

        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}
        mock_storage = MagicMock()
        mock_storage.get_alias = MagicMock(return_value=None)

        result = await _process_alias_expansion("look", [], mock_storage, "testplayer", mock_user, mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_process_alias_expansion_unsafe_alias(self):
        """Test _process_alias_expansion returns error when alias is unsafe."""
        from server.command_handler_unified import _process_alias_expansion

        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}
        mock_storage = MagicMock()
        mock_alias = MagicMock()
        mock_alias.name = "test_alias"
        mock_storage.get_alias = MagicMock(return_value=mock_alias)

        with patch("server.command_handler_unified.check_alias_safety", return_value=(False, "Unsafe alias", 0)):
            result = await _process_alias_expansion("test", [], mock_storage, "testplayer", mock_user, mock_request)
            assert result is not None
            assert result["result"] == "Unsafe alias"

    @pytest.mark.asyncio
    async def test_process_alias_expansion_invalid_expanded(self):
        """Test _process_alias_expansion returns error when expanded command is invalid."""
        from server.command_handler_unified import _process_alias_expansion

        mock_request = MagicMock()
        mock_user = {"username": "testplayer"}
        mock_storage = MagicMock()
        mock_alias = MagicMock()
        mock_alias.name = "test_alias"
        mock_alias.get_expanded_command = MagicMock(return_value="invalid command")
        mock_storage.get_alias = MagicMock(return_value=mock_alias)

        with (
            patch("server.command_handler_unified.check_alias_safety", return_value=(True, None, 1)),
            patch("server.command_handler_unified.validate_expanded_command", return_value=(False, "Invalid command")),
        ):
            result = await _process_alias_expansion("test", [], mock_storage, "testplayer", mock_user, mock_request)
            assert result is not None
            assert result["result"] == "Invalid command"

    @pytest.mark.asyncio
    async def test_check_all_command_blocks_catatonia(self):
        """Test _check_all_command_blocks returns result when catatonia blocks."""
        from server.command_handler_unified import _check_all_command_blocks

        mock_request = MagicMock()

        with patch("server.command_handler_unified.check_catatonia_block", return_value=(True, "Catatonic state")):
            result = await _check_all_command_blocks("look", "testplayer", mock_request)
            assert result is not None
            assert result["result"] == "Catatonic state"

    @pytest.mark.asyncio
    async def test_check_all_command_blocks_grace_period(self):
        """Test _check_all_command_blocks returns result when grace period blocks."""
        from server.command_handler_unified import _check_all_command_blocks

        mock_request = MagicMock()

        with (
            patch("server.command_handler_unified.check_catatonia_block", return_value=(False, None)),
            patch(
                "server.command_handler_unified._check_grace_period_block",
                return_value={"result": "In grace period"},
            ),
        ):
            result = await _check_all_command_blocks("look", "testplayer", mock_request)
            assert result is not None
            assert result["result"] == "In grace period"

    @pytest.mark.asyncio
    async def test_check_all_command_blocks_casting(self):
        """Test _check_all_command_blocks returns result when casting blocks."""
        from server.command_handler_unified import _check_all_command_blocks

        mock_request = MagicMock()

        with (
            patch("server.command_handler_unified.check_catatonia_block", return_value=(False, None)),
            patch("server.command_handler_unified._check_grace_period_block", return_value=None),
            patch(
                "server.command_handler_unified._check_casting_state",
                return_value={"result": "Casting spell"},
            ),
        ):
            result = await _check_all_command_blocks("look", "testplayer", mock_request)
            assert result is not None
            assert result["result"] == "Casting spell"

    @pytest.mark.asyncio
    async def test_check_grace_period_block_in_grace_period(self):
        """Test _check_grace_period_block returns result when player is in grace period."""
        import uuid

        from server.command_handler_unified import _check_grace_period_block

        mock_request = MagicMock()
        mock_connection_manager = MagicMock()
        mock_player_service = MagicMock()
        mock_player = MagicMock()
        # Use a valid UUID string format
        test_uuid = uuid.uuid4()
        mock_player.player_id = str(test_uuid)

        mock_request.app.state.connection_manager = mock_connection_manager
        mock_request.app.state.player_service = mock_player_service
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)

        with patch("server.command_handler_unified.is_player_in_grace_period", return_value=True):
            result = await _check_grace_period_block("testplayer", mock_request)
            assert result is not None
            assert "disconnected" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_check_grace_period_block_no_player(self):
        """Test _check_grace_period_block returns None when player not found."""
        from server.command_handler_unified import _check_grace_period_block

        mock_request = MagicMock()
        mock_connection_manager = MagicMock()
        mock_player_service = MagicMock()

        mock_request.app.state.connection_manager = mock_connection_manager
        mock_request.app.state.player_service = mock_player_service
        mock_player_service.get_player_by_name = AsyncMock(return_value=None)

        result = await _check_grace_period_block("testplayer", mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_check_grace_period_block_uuid_conversion(self):
        """Test _check_grace_period_block handles UUID conversion."""
        import uuid

        from server.command_handler_unified import _check_grace_period_block

        mock_request = MagicMock()
        mock_connection_manager = MagicMock()
        mock_player_service = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = uuid.uuid4()  # Already a UUID

        mock_request.app.state.connection_manager = mock_connection_manager
        mock_request.app.state.player_service = mock_player_service
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)

        with patch("server.command_handler_unified.is_player_in_grace_period", return_value=False):
            result = await _check_grace_period_block("testplayer", mock_request)
            assert result is None


class TestHandleSpecialCommandRouting:
    """Tests for _handle_special_command_routing function."""

    @pytest.mark.asyncio
    async def test_handle_special_command_routing_alias_command(self):
        """Test _handle_special_command_routing processes alias commands."""
        from server.command_handler_unified import _handle_special_command_routing

        mock_request = MagicMock()
        mock_user = {"player_id": "test-id"}
        mock_alias_storage = MagicMock()

        with patch(
            "server.command_handler_unified.command_service.process_command", new_callable=AsyncMock
        ) as mock_process:
            mock_process.return_value = {"result": "Alias created"}
            result = await _handle_special_command_routing(
                "alias", ["test", "look"], "alias test look", mock_alias_storage, "testplayer", mock_user, mock_request
            )
            assert result == {"result": "Alias created"}
            mock_process.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_handle_special_command_routing_alias_storage_none(self):
        """Test _handle_special_command_routing returns error when alias_storage is None."""
        from server.command_handler_unified import _handle_special_command_routing

        mock_request = MagicMock()
        mock_user = {"player_id": "test-id"}

        result = await _handle_special_command_routing(
            "alias", ["test", "look"], "alias test look", None, "testplayer", mock_user, mock_request
        )
        assert result == {"result": "Alias system not available"}

    @pytest.mark.asyncio
    async def test_handle_special_command_routing_emote_conversion(self):
        """Test _handle_special_command_routing converts single-word emotes."""
        from server.command_handler_unified import _handle_special_command_routing

        mock_request = MagicMock()
        mock_user = {"player_id": "test-id"}
        mock_alias_storage = MagicMock()

        with (
            patch("server.command_handler_unified._process_alias_expansion", new_callable=AsyncMock, return_value=None),
            patch("server.command_handler_unified.should_treat_as_emote", return_value=True),
            patch(
                "server.command_handler_unified.command_service.process_command", new_callable=AsyncMock
            ) as mock_process,
        ):
            mock_process.return_value = {"result": "You smile"}
            result = await _handle_special_command_routing(
                "smile", [], "smile", mock_alias_storage, "testplayer", mock_user, mock_request
            )
            assert result == {"result": "You smile"}
            mock_process.assert_awaited_once_with(
                "emote smile", mock_user, mock_request, mock_alias_storage, "testplayer"
            )

    @pytest.mark.asyncio
    async def test_handle_special_command_routing_returns_none(self):
        """Test _handle_special_command_routing returns None for normal commands."""
        from server.command_handler_unified import _handle_special_command_routing

        mock_request = MagicMock()
        mock_user = {"player_id": "test-id"}
        mock_alias_storage = MagicMock()

        with (
            patch("server.command_handler_unified._process_alias_expansion", new_callable=AsyncMock, return_value=None),
            patch("server.command_handler_unified.should_treat_as_emote", return_value=False),
        ):
            result = await _handle_special_command_routing(
                "look", ["around"], "look around", mock_alias_storage, "testplayer", mock_user, mock_request
            )
            assert result is None
