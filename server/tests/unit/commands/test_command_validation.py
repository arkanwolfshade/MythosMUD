"""
Unit tests for command validation and blocking.

Tests catatonia checks, rate limiting, command validation, grace period, casting state, and command blocks.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import Request

from server.command_handler.catatonia_check import (
    _check_catatonia_database,
    _check_catatonia_registry,
    _fetch_lucidity_record,
    _is_catatonic,
    _load_player_for_catatonia_check,
    _query_lucidity_record,
    check_catatonia_block,
)
from server.command_handler_unified import (
    _check_all_command_blocks,
    _check_casting_state,
    _check_grace_period_block,
    _check_rate_limit,
    _validate_command_basics,
)


class TestCatatoniaChecks:
    """Test catatonia checking functions."""

    def test_is_catatonic_with_tier(self):
        """Test _is_catatonic() returns True for catatonic tier."""
        mock_record = MagicMock()
        mock_record.current_tier = "catatonic"
        mock_record.current_lcd = 5
        result = _is_catatonic(mock_record)
        assert result is True

    def test_is_catatonic_with_zero_lcd(self):
        """Test _is_catatonic() returns True for zero LCD."""
        mock_record = MagicMock()
        mock_record.current_tier = "normal"
        mock_record.current_lcd = 0
        result = _is_catatonic(mock_record)
        assert result is True

    def test_is_catatonic_with_negative_lcd(self):
        """Test _is_catatonic() returns True for negative LCD."""
        mock_record = MagicMock()
        mock_record.current_tier = "normal"
        mock_record.current_lcd = -5
        result = _is_catatonic(mock_record)
        assert result is True

    def test_is_catatonic_not_catatonic(self):
        """Test _is_catatonic() returns False for normal player."""
        mock_record = MagicMock()
        mock_record.current_tier = "normal"
        mock_record.current_lcd = 50
        result = _is_catatonic(mock_record)
        assert result is False

    def test_is_catatonic_none(self):
        """Test _is_catatonic() returns False for None record."""
        result = _is_catatonic(None)
        assert result is False

    @pytest.mark.asyncio
    async def test_fetch_lucidity_record(self):
        """Test _fetch_lucidity_record() fetches record."""
        mock_session = AsyncMock()
        mock_record = MagicMock()
        mock_session.get = AsyncMock(return_value=mock_record)
        player_id = uuid.uuid4()

        result = await _fetch_lucidity_record(mock_session, player_id, "testplayer")
        assert result == mock_record
        mock_session.get.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_query_lucidity_record_success(self):
        """Test _query_lucidity_record() queries database."""
        player_id = uuid.uuid4()
        mock_record = MagicMock()

        mock_session = AsyncMock()
        mock_session.get = AsyncMock(return_value=mock_record)

        async def mock_async_gen():
            """Create async generator that yields mock_session."""
            yield mock_session

        with patch("server.command_handler.catatonia_check.get_async_session", return_value=mock_async_gen()):
            result = await _query_lucidity_record(player_id, "testplayer")
            assert result == mock_record

    @pytest.mark.asyncio
    async def test_check_catatonia_database_catatonic(self):
        """Test _check_catatonia_database() detects catatonic player."""
        player_id = uuid.uuid4()
        mock_record = MagicMock()
        mock_record.current_tier = "catatonic"
        mock_record.current_lcd = 0

        with patch("server.command_handler.catatonia_check._query_lucidity_record", return_value=mock_record):
            blocked, message = await _check_catatonia_database(player_id, "testplayer")
            assert blocked is True
            assert message is not None

    @pytest.mark.asyncio
    async def test_check_catatonia_database_not_catatonic(self):
        """Test _check_catatonia_database() returns False for normal player."""
        player_id = uuid.uuid4()
        mock_record = MagicMock()
        mock_record.current_tier = "normal"
        mock_record.current_lcd = 50

        with patch("server.command_handler.catatonia_check._query_lucidity_record", return_value=mock_record):
            blocked, message = await _check_catatonia_database(player_id, "testplayer")
            assert blocked is False
            assert message is None

    @pytest.mark.asyncio
    async def test_check_catatonia_registry_catatonic(self):
        """Test _check_catatonia_registry() detects catatonic via registry."""
        player_id = uuid.uuid4()
        mock_registry = MagicMock()
        mock_registry.is_catatonic = Mock(return_value=True)
        mock_state = MagicMock()
        mock_state.__dict__ = {"catatonia_registry": mock_registry}

        blocked, message = _check_catatonia_registry(mock_state, player_id, "testplayer")
        assert blocked is True
        assert message is not None

    @pytest.mark.asyncio
    async def test_check_catatonia_registry_not_catatonic(self):
        """Test _check_catatonia_registry() returns False for normal player."""
        player_id = uuid.uuid4()
        mock_registry = MagicMock()
        mock_registry.is_catatonic = Mock(return_value=False)
        mock_state = MagicMock()
        mock_state.__dict__ = {"catatonia_registry": mock_registry}

        blocked, message = _check_catatonia_registry(mock_state, player_id, "testplayer")
        assert blocked is False
        assert message is None

    @pytest.mark.asyncio
    async def test_load_player_for_catatonia_check_from_cache(self):
        """Test _load_player_for_catatonia_check() uses cache."""
        request = Mock(spec=Request)
        mock_player = MagicMock()
        player_name = "testplayer"

        with patch("server.command_handler.catatonia_check.get_cached_player", return_value=mock_player):
            result = await _load_player_for_catatonia_check(request, player_name, None)
            assert result == mock_player

    @pytest.mark.asyncio
    async def test_load_player_for_catatonia_check_from_persistence(self):
        """Test _load_player_for_catatonia_check() loads from persistence."""
        request = Mock(spec=Request)
        mock_player = MagicMock()
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        player_name = "testplayer"

        with patch("server.command_handler.catatonia_check.get_cached_player", return_value=None):
            with patch("server.command_handler.catatonia_check.cache_player"):
                result = await _load_player_for_catatonia_check(request, player_name, mock_persistence)
                assert result == mock_player

    @pytest.mark.asyncio
    async def test_check_catatonia_block_allowed_command(self):
        """Test _check_catatonia_block() allows certain commands."""
        request = Mock(spec=Request)
        blocked, message = await check_catatonia_block("testplayer", "help", request)
        assert blocked is False
        assert message is None

    @pytest.mark.asyncio
    async def test_check_catatonia_block_no_app_state(self):
        """Test _check_catatonia_block() returns False when no app state."""
        request = Mock(spec=Request)
        del request.app
        blocked, _message = await check_catatonia_block("testplayer", "look", request)
        assert blocked is False


class TestCheckRateLimit:
    """Test _check_rate_limit function."""

    def test_check_rate_limit_allowed(self):
        """Test _check_rate_limit returns None when allowed."""
        with patch("server.command_handler_unified.command_rate_limiter.is_allowed", return_value=True):
            result = _check_rate_limit("testplayer")
            assert result is None

    def test_check_rate_limit_blocked(self):
        """Test _check_rate_limit returns result when blocked."""
        with (
            patch("server.command_handler_unified.command_rate_limiter.is_allowed", return_value=False),
            patch("server.command_handler_unified.command_rate_limiter.get_wait_time", return_value=5.0),
            patch("server.command_handler_unified.audit_logger.log_security_event") as mock_audit,
        ):
            result = _check_rate_limit("testplayer")
            assert result is not None
            assert "Too many commands" in result["result"]
            mock_audit.assert_called_once()


class TestValidateCommandBasics:
    """Test _validate_command_basics function."""

    def test_validate_command_basics_empty(self):
        """Test _validate_command_basics returns result for empty command."""
        result = _validate_command_basics("", "testplayer")
        assert result == {"result": ""}

    def test_validate_command_basics_too_long(self):
        """Test _validate_command_basics returns result for command too long."""
        long_command = "a" * 1001  # Assuming MAX_COMMAND_LENGTH is 1000
        with (
            patch("server.command_handler_unified.MAX_COMMAND_LENGTH", 1000),
            patch("server.command_handler_unified.audit_logger.log_security_event") as mock_audit,
        ):
            result = _validate_command_basics(long_command, "testplayer")
            assert result is not None
            assert "too long" in result["result"].lower()
            # Should not log security event for length violations
            mock_audit.assert_not_called()

    def test_validate_command_basics_invalid_content(self):
        """Test _validate_command_basics returns result for invalid command content."""
        with (
            patch(
                "server.command_handler_unified.CommandValidator.validate_command_content",
                return_value=(False, "Invalid"),
            ),
            patch("server.command_handler_unified.CommandValidator.sanitize_for_logging", return_value="test"),
            patch("server.command_handler_unified.audit_logger.log_security_event") as mock_audit,
        ):
            result = _validate_command_basics("invalid; command", "testplayer")
            assert result == {"result": "Invalid command format"}
            mock_audit.assert_called_once()

    def test_validate_command_basics_valid(self):
        """Test _validate_command_basics returns None for valid command."""
        with patch(
            "server.command_handler_unified.CommandValidator.validate_command_content", return_value=(True, None)
        ):
            result = _validate_command_basics("look", "testplayer")
            assert result is None


class TestCheckGracePeriodBlock:
    """Test _check_grace_period_block function."""

    @pytest.mark.asyncio
    async def test_check_grace_period_block_no_connection_manager(self):
        """Test _check_grace_period_block returns None when no connection manager."""
        mock_request = MagicMock()
        mock_request.app.state.connection_manager = None

        result = await _check_grace_period_block("testplayer", mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_check_grace_period_block_no_player_service(self):
        """Test _check_grace_period_block returns None when no player service."""
        mock_request = MagicMock()
        mock_request.app.state.connection_manager = MagicMock()
        mock_request.app.state.player_service = None

        result = await _check_grace_period_block("testplayer", mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_check_grace_period_block_player_not_found(self):
        """Test _check_grace_period_block returns None when player not found."""
        mock_request = MagicMock()
        mock_request.app.state.connection_manager = MagicMock()
        mock_player_service = AsyncMock()
        mock_player_service.get_player_by_name = AsyncMock(return_value=None)
        mock_request.app.state.player_service = mock_player_service

        result = await _check_grace_period_block("testplayer", mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_check_grace_period_block_player_in_grace_period(self):
        """Test _check_grace_period_block returns block result when player in grace period."""
        mock_request = MagicMock()
        mock_connection_manager = MagicMock()
        mock_request.app.state.connection_manager = mock_connection_manager
        mock_player = MagicMock()
        mock_player.player_id = str(uuid.uuid4())
        mock_player_service = AsyncMock()
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.player_service = mock_player_service

        with patch("server.command_handler_unified.is_player_in_grace_period", return_value=True):
            result = await _check_grace_period_block("testplayer", mock_request)
            assert result is not None
            assert "disconnected" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_check_grace_period_block_handles_error(self):
        """Test _check_grace_period_block returns None on error."""
        mock_request = MagicMock()
        del mock_request.app

        result = await _check_grace_period_block("testplayer", mock_request)
        assert result is None


class TestCheckCastingState:
    """Test _check_casting_state function."""

    @pytest.mark.asyncio
    async def test_check_casting_state_allowed_command(self):
        """Test _check_casting_state allows stop/interrupt/status during casting."""
        result = await _check_casting_state("stop", "testplayer", MagicMock())
        assert result is None

    @pytest.mark.asyncio
    async def test_check_casting_state_no_magic_service(self):
        """Test _check_casting_state returns None when no magic service."""
        mock_request = MagicMock()
        mock_request.app.state.magic_service = None

        result = await _check_casting_state("look", "testplayer", mock_request)
        assert result is None

    @pytest.mark.asyncio
    async def test_check_casting_state_player_casting(self):
        """Test _check_casting_state returns block result when player is casting."""
        mock_request = MagicMock()
        mock_magic_service = MagicMock()
        mock_casting_state = MagicMock()
        mock_casting_state.spell_name = "fireball"
        mock_casting_manager = MagicMock()
        mock_casting_manager.is_casting.return_value = True
        mock_casting_manager.get_casting_state.return_value = mock_casting_state
        mock_magic_service.casting_state_manager = mock_casting_manager
        mock_request.app.state.magic_service = mock_magic_service

        mock_player = MagicMock()
        mock_player.player_id = str(uuid.uuid4())
        mock_player_service = AsyncMock()
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.player_service = mock_player_service

        result = await _check_casting_state("look", "testplayer", mock_request)
        assert result is not None
        assert "casting" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_check_casting_state_handles_error(self):
        """Test _check_casting_state returns None on error."""
        mock_request = MagicMock()
        del mock_request.app

        result = await _check_casting_state("look", "testplayer", mock_request)
        assert result is None


class TestCheckAllCommandBlocks:
    """Test _check_all_command_blocks function."""

    @pytest.mark.asyncio
    async def test_check_all_command_blocks_catatonia(self):
        """Test _check_all_command_blocks returns block result for catatonia."""
        mock_request = MagicMock()

        with patch("server.command_handler_unified.check_catatonia_block", return_value=(True, "Catatonic")):
            result = await _check_all_command_blocks("look", "testplayer", mock_request)
            assert result == {"result": "Catatonic"}

    @pytest.mark.asyncio
    async def test_check_all_command_blocks_grace_period(self):
        """Test _check_all_command_blocks returns block result for grace period."""
        mock_request = MagicMock()

        with (
            patch("server.command_handler_unified.check_catatonia_block", return_value=(False, None)),
            patch(
                "server.command_handler_unified._check_grace_period_block", return_value={"result": "In grace period"}
            ),
        ):
            result = await _check_all_command_blocks("look", "testplayer", mock_request)
            assert result == {"result": "In grace period"}

    @pytest.mark.asyncio
    async def test_check_all_command_blocks_casting(self):
        """Test _check_all_command_blocks returns block result for casting."""
        mock_request = MagicMock()

        with (
            patch("server.command_handler_unified.check_catatonia_block", return_value=(False, None)),
            patch("server.command_handler_unified._check_grace_period_block", return_value=None),
            patch("server.command_handler_unified._check_casting_state", return_value={"result": "Casting"}),
        ):
            result = await _check_all_command_blocks("look", "testplayer", mock_request)
            assert result == {"result": "Casting"}

    @pytest.mark.asyncio
    async def test_check_all_command_blocks_no_blocks(self):
        """Test _check_all_command_blocks returns None when no blocks."""
        mock_request = MagicMock()

        with (
            patch("server.command_handler_unified.check_catatonia_block", return_value=(False, None)),
            patch("server.command_handler_unified._check_grace_period_block", return_value=None),
            patch("server.command_handler_unified._check_casting_state", return_value=None),
        ):
            result = await _check_all_command_blocks("look", "testplayer", mock_request)
            assert result is None
