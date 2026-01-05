"""
Unit tests for unified command handler.

Tests command processing, validation, normalization, and catatonia checks.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import Request

from server.command_handler_unified import (
    _check_catatonia_block,
    _check_catatonia_database,
    _check_catatonia_registry,
    _fetch_lucidity_record,
    _is_catatonic,
    _is_predefined_emote,
    _load_player_for_catatonia_check,
    _query_lucidity_record,
    _should_treat_as_emote,
    clean_command_input,
    get_help_content,
    normalize_command,
    process_command,
)


class TestCommandNormalization:
    """Test command normalization functions."""

    def test_clean_command_input_basic(self):
        """Test clean_command_input() with normal command."""
        result = clean_command_input("look around")
        assert result == "look around"

    def test_clean_command_input_multiple_spaces(self):
        """Test clean_command_input() collapses multiple spaces."""
        result = clean_command_input("look    around   here")
        assert result == "look around here"

    def test_clean_command_input_leading_trailing_whitespace(self):
        """Test clean_command_input() strips leading/trailing whitespace."""
        result = clean_command_input("  look around  ")
        assert result == "look around"

    def test_clean_command_input_tabs(self):
        """Test clean_command_input() handles tabs."""
        result = clean_command_input("look\taround")
        assert result == "look around"

    def test_normalize_command_no_slash(self):
        """Test normalize_command() with no slash prefix."""
        result = normalize_command("look around")
        assert result == "look around"

    def test_normalize_command_with_slash(self):
        """Test normalize_command() removes slash prefix."""
        result = normalize_command("/look around")
        assert result == "look around"

    def test_normalize_command_empty(self):
        """Test normalize_command() with empty string."""
        result = normalize_command("")
        assert result == ""

    def test_normalize_command_whitespace_only(self):
        """Test normalize_command() with whitespace only."""
        result = normalize_command("   ")
        assert result == ""

    def test_normalize_command_slash_only(self):
        """Test normalize_command() with slash only."""
        result = normalize_command("/")
        assert result == ""

    def test_normalize_command_slash_with_spaces(self):
        """Test normalize_command() removes slash and trims spaces."""
        result = normalize_command("  /look  ")
        assert result == "look"


class TestEmoteDetection:
    """Test emote detection functions."""

    @patch("server.game.emote_service.EmoteService")
    def test_is_predefined_emote_true(self, mock_emote_service_class):
        """Test _is_predefined_emote() returns True for predefined emote."""
        mock_service = MagicMock()
        mock_service.is_emote_alias = Mock(return_value=True)
        mock_emote_service_class.return_value = mock_service

        result = _is_predefined_emote("smile")
        assert result is True

    @patch("server.game.emote_service.EmoteService")
    def test_is_predefined_emote_false(self, mock_emote_service_class):
        """Test _is_predefined_emote() returns False for non-emote."""
        mock_service = MagicMock()
        mock_service.is_emote_alias = Mock(return_value=False)
        mock_emote_service_class.return_value = mock_service

        result = _is_predefined_emote("look")
        assert result is False

    @patch("server.game.emote_service.EmoteService")
    def test_is_predefined_emote_handles_error(self, mock_emote_service_class):
        """Test _is_predefined_emote() handles errors gracefully."""
        mock_emote_service_class.side_effect = ImportError("Module not found")
        result = _is_predefined_emote("test")
        assert result is False

    def test_should_treat_as_emote_system_command(self):
        """Test _should_treat_as_emote() returns False for system commands."""
        result = _should_treat_as_emote("look")
        assert result is False

    def test_should_treat_as_emote_unknown_word(self):
        """Test _should_treat_as_emote() returns False for unknown words."""
        with patch("server.command_handler_unified._is_predefined_emote", return_value=False):
            result = _should_treat_as_emote("unknownword")
            assert result is False

    def test_should_treat_as_emote_predefined_emote(self):
        """Test _should_treat_as_emote() returns True for predefined emotes."""
        with patch("server.command_handler_unified._is_predefined_emote", return_value=True):
            result = _should_treat_as_emote("smile")
            assert result is True


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

        with patch("server.command_handler_unified.get_async_session", return_value=mock_async_gen()):
            result = await _query_lucidity_record(player_id, "testplayer")
            assert result == mock_record

    @pytest.mark.asyncio
    async def test_check_catatonia_database_catatonic(self):
        """Test _check_catatonia_database() detects catatonic player."""
        player_id = uuid.uuid4()
        mock_record = MagicMock()
        mock_record.current_tier = "catatonic"
        mock_record.current_lcd = 0

        with patch("server.command_handler_unified._query_lucidity_record", return_value=mock_record):
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

        with patch("server.command_handler_unified._query_lucidity_record", return_value=mock_record):
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

        with patch("server.command_handler_unified.get_cached_player", return_value=mock_player):
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

        with patch("server.command_handler_unified.get_cached_player", return_value=None):
            with patch("server.command_handler_unified.cache_player"):
                result = await _load_player_for_catatonia_check(request, player_name, mock_persistence)
                assert result == mock_player

    @pytest.mark.asyncio
    async def test_check_catatonia_block_allowed_command(self):
        """Test _check_catatonia_block() allows certain commands."""
        request = Mock(spec=Request)
        blocked, message = await _check_catatonia_block("testplayer", "help", request)
        assert blocked is False
        assert message is None

    @pytest.mark.asyncio
    async def test_check_catatonia_block_no_app_state(self):
        """Test _check_catatonia_block() returns False when no app state."""
        request = Mock(spec=Request)
        del request.app
        blocked, _message = await _check_catatonia_block("testplayer", "look", request)
        assert blocked is False


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
        with patch("server.help.help_content.get_help_content", return_value="Help text"):
            result = get_help_content("look")
            assert result == "Help text"

    def test_get_help_content_none(self):
        """Test get_help_content() with None command."""
        with patch("server.help.help_content.get_help_content", return_value="General help"):
            result = get_help_content(None)
            assert result == "General help"
