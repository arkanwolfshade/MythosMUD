"""
Unit tests for motd_loader utilities.

Tests the MOTD loading functions.
"""

from unittest.mock import mock_open, patch

from server.utils.motd_loader import load_motd


def test_load_motd_file_exists():
    """Test load_motd() loads MOTD from file."""
    mock_content = "Welcome to MythosMUD!\nThis is a test MOTD."
    with (
        patch("server.utils.motd_loader.get_config") as mock_config,
        patch("os.path.exists", return_value=True),
        patch("builtins.open", mock_open(read_data=mock_content)),
    ):
        mock_config.return_value.get.return_value = "./data/motd.txt"
        result = load_motd()
        assert result == mock_content


def test_load_motd_file_not_exists():
    """Test load_motd() returns default when file doesn't exist."""
    with patch("server.utils.motd_loader.get_config") as mock_config, patch("os.path.exists", return_value=False):
        mock_config.return_value.get.return_value = "./data/motd.txt"
        result = load_motd()
        assert "Welcome" in result or len(result) > 0  # Should return default message


def test_load_motd_file_read_error():
    """Test load_motd() handles file read errors."""
    with (
        patch("server.utils.motd_loader.get_config") as mock_config,
        patch("os.path.exists", return_value=True),
        patch("builtins.open", side_effect=OSError("Read error")),
    ):
        mock_config.return_value.get.return_value = "./data/motd.txt"
        result = load_motd()
        # Should return default or handle error gracefully
        assert isinstance(result, str)


def test_load_motd_empty_file():
    """Test load_motd() handles empty file."""
    with (
        patch("server.utils.motd_loader.get_config") as mock_config,
        patch("os.path.exists", return_value=True),
        patch("builtins.open", mock_open(read_data="")),
    ):
        mock_config.return_value.get.return_value = "./data/motd.txt"
        result = load_motd()
        assert isinstance(result, str)
