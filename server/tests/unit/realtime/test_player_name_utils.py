"""
Tests for player name extraction and validation utilities.

As documented in "Identity Protection Protocols" - Dr. Armitage, 1928
"""

import uuid
from unittest.mock import MagicMock, patch

from server.realtime.player_name_utils import PlayerNameExtractor


class TestPlayerNameExtractor:
    """Test suite for PlayerNameExtractor class."""

    def test_init(self):
        """Test PlayerNameExtractor initialization."""
        extractor = PlayerNameExtractor()
        assert extractor is not None
        assert hasattr(extractor, "_logger")

    def test_is_uuid_string_valid_uuid(self):
        """Test _is_uuid_string with valid UUID."""
        extractor = PlayerNameExtractor()
        test_uuid = str(uuid.uuid4())
        assert extractor._is_uuid_string(test_uuid) is True

    def test_is_uuid_string_invalid_length(self):
        """Test _is_uuid_string with invalid length."""
        extractor = PlayerNameExtractor()
        assert extractor._is_uuid_string("12345") is False
        assert extractor._is_uuid_string("a" * 50) is False

    def test_is_uuid_string_invalid_dash_count(self):
        """Test _is_uuid_string with invalid dash count."""
        extractor = PlayerNameExtractor()
        # String with 5 dashes (invalid - should have exactly 4)
        assert extractor._is_uuid_string("12345678-1234-1234-1234-1234-123456789012") is False
        # String with 0 dashes (invalid - should have exactly 4)
        assert extractor._is_uuid_string("12345678123412341234123456789012") is False

    def test_is_uuid_string_invalid_characters(self):
        """Test _is_uuid_string with invalid characters."""
        extractor = PlayerNameExtractor()
        assert extractor._is_uuid_string("12345678-1234-1234-1234-12345678901g") is False  # 'g' invalid
        assert extractor._is_uuid_string("12345678-1234-1234-1234-12345678901@") is False  # '@' invalid

    def test_is_uuid_string_valid_format(self):
        """Test _is_uuid_string with valid format variations."""
        extractor = PlayerNameExtractor()
        assert extractor._is_uuid_string("12345678-1234-1234-1234-123456789012") is True
        assert extractor._is_uuid_string("ABCDEF12-3456-7890-ABCD-EF1234567890") is True
        assert extractor._is_uuid_string("abcdef12-3456-7890-abcd-ef1234567890") is True

    def test_is_valid_name_valid_string(self):
        """Test _is_valid_name with valid string."""
        extractor = PlayerNameExtractor()
        assert extractor._is_valid_name("TestPlayer") is True
        assert extractor._is_valid_name("Player Name") is True

    def test_is_valid_name_empty_string(self):
        """Test _is_valid_name with empty string."""
        extractor = PlayerNameExtractor()
        assert extractor._is_valid_name("") is False
        assert extractor._is_valid_name("   ") is False

    def test_is_valid_name_none(self):
        """Test _is_valid_name with None."""
        extractor = PlayerNameExtractor()
        assert extractor._is_valid_name(None) is False

    def test_is_valid_name_not_string(self):
        """Test _is_valid_name with non-string type."""
        extractor = PlayerNameExtractor()
        assert extractor._is_valid_name(123) is False
        assert extractor._is_valid_name([]) is False

    def test_is_valid_name_uuid_string(self):
        """Test _is_valid_name with UUID string."""
        extractor = PlayerNameExtractor()
        test_uuid = str(uuid.uuid4())
        assert extractor._is_valid_name(test_uuid) is False

    def test_is_valid_name_string_valid(self):
        """Test _is_valid_name_string with valid string."""
        extractor = PlayerNameExtractor()
        assert extractor._is_valid_name_string("TestPlayer") is True

    def test_is_valid_name_string_invalid(self):
        """Test _is_valid_name_string with invalid inputs."""
        extractor = PlayerNameExtractor()
        assert not extractor._is_valid_name_string(None)  # Returns None (falsy)
        assert not extractor._is_valid_name_string("")  # Returns False
        assert not extractor._is_valid_name_string(123)  # Returns False
        test_uuid = str(uuid.uuid4())
        assert not extractor._is_valid_name_string(test_uuid)  # Returns False

    def test_extract_initial_player_name_with_name_attr(self):
        """Test _extract_initial_player_name with name attribute."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = "TestPlayer"
        assert extractor._extract_initial_player_name(player) == "TestPlayer"

    def test_extract_initial_player_name_with_getattr(self):
        """Test _extract_initial_player_name with getattr fallback."""
        extractor = PlayerNameExtractor()
        player = MagicMock(spec=[])  # Mock without name attribute
        # Use spec to prevent automatic attribute creation
        type(player).name = property(lambda self: "TestPlayer")
        result = extractor._extract_initial_player_name(player)
        assert result == "TestPlayer"

    def test_extract_initial_player_name_none(self):
        """Test _extract_initial_player_name when name is None."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = None
        assert extractor._extract_initial_player_name(player) is None

    def test_try_player_username_valid(self):
        """Test _try_player_username with valid username."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.username = "TestUser"
        assert extractor._try_player_username(player) == "TestUser"

    def test_try_player_username_invalid_uuid(self):
        """Test _try_player_username rejects UUID-formatted string as username."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        # Test that a UUID-formatted string is rejected (security check)
        uuid_formatted_string = str(uuid.uuid4())
        player.username = uuid_formatted_string
        assert extractor._try_player_username(player) is None

    def test_try_player_username_getattr_fallback(self):
        """Test _try_player_username with getattr fallback."""
        extractor = PlayerNameExtractor()
        player = MagicMock(spec=[])  # Mock without username attribute
        # Use spec to prevent automatic attribute creation, then set via property
        type(player).username = property(lambda self: "TestUser")
        result = extractor._try_player_username(player)
        assert result == "TestUser"

    def test_try_player_username_none(self):
        """Test _try_player_username when username is None."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.username = None
        assert extractor._try_player_username(player) is None

    def test_get_name_from_user_object_username(self):
        """Test _get_name_from_user_object with username."""
        extractor = PlayerNameExtractor()
        user = MagicMock()
        user.username = "TestUser"
        assert extractor._get_name_from_user_object(user) == "TestUser"

    def test_get_name_from_user_object_display_name(self):
        """Test _get_name_from_user_object with display_name."""
        extractor = PlayerNameExtractor()
        user = MagicMock()
        user.username = None
        user.display_name = "Display Name"
        assert extractor._get_name_from_user_object(user) == "Display Name"

    def test_get_name_from_user_object_getattr_fallback(self):
        """Test _get_name_from_user_object with getattr fallback."""
        extractor = PlayerNameExtractor()
        user = MagicMock(spec=[])  # Mock without attributes
        # Use property to simulate getattr fallback behavior
        type(user).username = property(lambda self: "TestUser")
        type(user).display_name = property(lambda self: None)
        result = extractor._get_name_from_user_object(user)
        assert result == "TestUser"

    def test_get_name_from_user_object_none(self):
        """Test _get_name_from_user_object when no name available."""
        extractor = PlayerNameExtractor()
        user = MagicMock()
        user.username = None
        user.display_name = None
        result = extractor._get_name_from_user_object(user)
        assert result is None

    def test_try_user_object_name_with_user(self):
        """Test _try_user_object_name with user attribute."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        user = MagicMock()
        user.username = "TestUser"
        player.user = user
        assert extractor._try_user_object_name(player) == "TestUser"

    def test_try_user_object_name_no_user_attr(self):
        """Test _try_user_object_name without user attribute."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        del player.user
        assert extractor._try_user_object_name(player) is None

    def test_try_user_object_name_user_none(self):
        """Test _try_user_object_name when user is None."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.user = None
        assert extractor._try_user_object_name(player) is None

    def test_try_user_object_name_exception_handling(self):
        """Test _try_user_object_name with exception handling."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.user = MagicMock()
        with patch.object(extractor, "_get_name_from_user_object", side_effect=ValueError("Test error")):
            result = extractor._try_user_object_name(player)
            assert result is None

    def test_try_fallback_name_sources_valid_current(self):
        """Test _try_fallback_name_sources with valid current name."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        assert extractor._try_fallback_name_sources(player, "ValidName") == "ValidName"

    def test_try_fallback_name_sources_invalid_current_username_fallback(self):
        """Test _try_fallback_name_sources with username fallback."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.username = "TestUser"
        assert extractor._try_fallback_name_sources(player, None) == "TestUser"

    def test_try_fallback_name_sources_user_object_fallback(self):
        """Test _try_fallback_name_sources with user object fallback."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.username = None
        user = MagicMock()
        user.username = "UserObjectName"
        player.user = user
        assert extractor._try_fallback_name_sources(player, None) == "UserObjectName"

    def test_validate_name_basic_valid(self):
        """Test _validate_name_basic with valid name."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        result = extractor._validate_name_basic("TestPlayer", str(player_id), player_id, player)
        assert result == "TestPlayer"

    def test_validate_name_basic_none(self):
        """Test _validate_name_basic with None."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        with patch.object(extractor._logger, "warning") as mock_warning:
            result = extractor._validate_name_basic(None, str(player_id), player_id, player)
            assert result is None
            mock_warning.assert_called_once()

    def test_validate_name_basic_empty_string(self):
        """Test _validate_name_basic with empty string."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        with patch.object(extractor._logger, "warning") as mock_warning:
            result = extractor._validate_name_basic("", str(player_id), player_id, player)
            assert result is None
            # Empty string triggers one warning after stripping
            mock_warning.assert_called_once()

    def test_validate_name_basic_whitespace_only(self):
        """Test _validate_name_basic with whitespace only."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        with patch.object(extractor._logger, "warning") as mock_warning:
            result = extractor._validate_name_basic("   ", str(player_id), player_id, player)
            assert result is None
            mock_warning.assert_called_once()

    def test_check_uuid_pattern_match_valid(self):
        """Test _check_uuid_pattern_match with valid UUID pattern."""
        extractor = PlayerNameExtractor()
        test_uuid = str(uuid.uuid4())
        assert extractor._check_uuid_pattern_match(test_uuid) is True

    def test_check_uuid_pattern_match_invalid(self):
        """Test _check_uuid_pattern_match with invalid pattern."""
        extractor = PlayerNameExtractor()
        assert extractor._check_uuid_pattern_match("NotAUUID") is False
        assert extractor._check_uuid_pattern_match("12345") is False

    def test_check_uuid_string_matches_exact(self):
        """Test _check_uuid_string_matches with exact match."""
        extractor = PlayerNameExtractor()
        player_id = uuid.uuid4()
        player_id_str = str(player_id)
        assert extractor._check_uuid_string_matches(player_id_str, player_id_str, player_id) is True

    def test_check_uuid_string_matches_lowercase(self):
        """Test _check_uuid_string_matches with lowercase match."""
        extractor = PlayerNameExtractor()
        player_id = uuid.uuid4()
        player_id_str = str(player_id)
        assert extractor._check_uuid_string_matches(player_id_str.lower(), player_id_str, player_id) is True

    def test_check_uuid_string_matches_no_match(self):
        """Test _check_uuid_string_matches with no match."""
        extractor = PlayerNameExtractor()
        player_id = uuid.uuid4()
        player_id_str = str(player_id)
        assert extractor._check_uuid_string_matches("DifferentUUID", player_id_str, player_id) is False

    def test_log_uuid_validation_failure_critical(self):
        """Test _log_uuid_validation_failure with critical error."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        with patch.object(extractor._logger, "error") as mock_error:
            extractor._log_uuid_validation_failure(str(player_id), str(player_id), player_id, player, True, True)
            mock_error.assert_called_once()

    def test_log_uuid_validation_failure_warning_pattern(self):
        """Test _log_uuid_validation_failure with UUID pattern warning."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        with patch.object(extractor._logger, "warning") as mock_warning:
            extractor._log_uuid_validation_failure(
                "12345678-1234-1234-1234-123456789012", str(player_id), player_id, player, True, False
            )
            mock_warning.assert_called_once()

    def test_log_uuid_validation_failure_warning_string(self):
        """Test _log_uuid_validation_failure with UUID string warning."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        with patch.object(extractor._logger, "warning") as mock_warning:
            extractor._log_uuid_validation_failure(str(player_id), str(player_id), player_id, player, False, False)
            mock_warning.assert_called_once()

    def test_validate_name_not_uuid_valid(self):
        """Test _validate_name_not_uuid with valid name."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        assert extractor._validate_name_not_uuid("ValidName", str(player_id), player_id, player) is True

    def test_validate_name_not_uuid_uuid_pattern(self):
        """Test _validate_name_not_uuid with UUID pattern."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        test_uuid = str(uuid.uuid4())
        with patch.object(extractor, "_log_uuid_validation_failure") as mock_log:
            result = extractor._validate_name_not_uuid(test_uuid, str(player_id), player_id, player)
            assert result is False
            mock_log.assert_called_once()

    def test_validate_name_not_uuid_matches_player_id(self):
        """Test _validate_name_not_uuid with name matching player ID."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        player_id_str = str(player_id)
        with patch.object(extractor, "_log_uuid_validation_failure") as mock_log:
            result = extractor._validate_name_not_uuid(player_id_str, player_id_str, player_id, player)
            assert result is False
            mock_log.assert_called_once()

    def test_extract_and_validate_player_name_success(self):
        """Test extract_and_validate_player_name with valid player."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = "TestPlayer"
        player_id = uuid.uuid4()
        result = extractor.extract_and_validate_player_name(player, str(player_id), player_id)
        assert result == "TestPlayer"

    def test_extract_and_validate_player_name_fallback_username(self):
        """Test extract_and_validate_player_name with username fallback."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = None
        player.username = "TestUser"
        player_id = uuid.uuid4()
        result = extractor.extract_and_validate_player_name(player, str(player_id), player_id)
        assert result == "TestUser"

    def test_extract_and_validate_player_name_fallback_user_object(self):
        """Test extract_and_validate_player_name with user object fallback."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = None
        player.username = None
        user = MagicMock()
        user.username = "UserObjectName"
        player.user = user
        player_id = uuid.uuid4()
        result = extractor.extract_and_validate_player_name(player, str(player_id), player_id)
        assert result == "UserObjectName"

    def test_extract_and_validate_player_name_invalid_uuid(self):
        """Test extract_and_validate_player_name rejects UUID-formatted string as name."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        # Test that a UUID-formatted string is rejected (security check)
        uuid_formatted_string = str(uuid.uuid4())
        player.name = uuid_formatted_string
        player.username = None  # Ensure no fallback
        del player.user  # Ensure no user object fallback
        player_id = uuid.uuid4()
        result = extractor.extract_and_validate_player_name(player, str(player_id), player_id)
        assert result is None

    def test_extract_and_validate_player_name_none(self):
        """Test extract_and_validate_player_name with no name available."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = None
        player.username = None
        del player.user
        player_id = uuid.uuid4()
        result = extractor.extract_and_validate_player_name(player, str(player_id), player_id)
        assert result is None

    def test_extract_player_name_from_player(self):
        """Test extract_player_name with valid player name."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = "TestPlayer"
        player_id = uuid.uuid4()
        result = extractor.extract_player_name(player, player_id)
        assert result == "TestPlayer"

    def test_extract_player_name_from_user_object(self):
        """Test extract_player_name with user object fallback."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = None
        user = MagicMock()
        user.username = "UserObjectName"
        player.user = user
        player_id = uuid.uuid4()
        result = extractor.extract_player_name(player, player_id)
        assert result == "UserObjectName"

    def test_extract_player_name_placeholder(self):
        """Test extract_player_name with placeholder fallback."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = None
        del player.user
        player_id = uuid.uuid4()
        with patch.object(extractor._logger, "warning") as mock_warning:
            result = extractor.extract_player_name(player, player_id)
            assert result == "Unknown Player"
            mock_warning.assert_called_once()

    def test_extract_player_name_user_exception(self):
        """Test extract_player_name with user access exception."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player.name = None
        user = MagicMock()
        # Make user.username and user.display_name raise AttributeError when accessed
        user.username = MagicMock(side_effect=AttributeError("Test error"))
        user.display_name = MagicMock(side_effect=AttributeError("Test error"))
        player.user = user
        player_id = uuid.uuid4()
        # Exception should be caught and "Unknown Player" returned
        result = extractor.extract_player_name(player, player_id)
        assert result == "Unknown Player"

    def test_validate_player_name_not_uuid_valid(self):
        """Test validate_player_name_not_uuid with valid name."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        result = extractor.validate_player_name_not_uuid("ValidName", player_id, player)
        assert result == "ValidName"

    def test_validate_player_name_not_uuid_uuid_string(self):
        """Test validate_player_name_not_uuid with UUID string."""
        extractor = PlayerNameExtractor()
        player = MagicMock()
        player_id = uuid.uuid4()
        test_uuid = str(uuid.uuid4())
        with patch.object(extractor._logger, "error") as mock_error:
            result = extractor.validate_player_name_not_uuid(test_uuid, player_id, player)
            assert result == "Unknown Player"
            mock_error.assert_called_once()

    def test_is_valid_name_for_occupant_valid(self):
        """Test is_valid_name_for_occupant with valid name."""
        extractor = PlayerNameExtractor()
        assert extractor.is_valid_name_for_occupant("TestPlayer") is True

    def test_is_valid_name_for_occupant_invalid(self):
        """Test is_valid_name_for_occupant with invalid inputs."""
        extractor = PlayerNameExtractor()
        assert not extractor.is_valid_name_for_occupant(None)  # Returns None (falsy)
        assert not extractor.is_valid_name_for_occupant("")  # Returns False
        assert not extractor.is_valid_name_for_occupant(123)  # Returns False
        test_uuid = str(uuid.uuid4())
        assert not extractor.is_valid_name_for_occupant(test_uuid)  # Returns False
