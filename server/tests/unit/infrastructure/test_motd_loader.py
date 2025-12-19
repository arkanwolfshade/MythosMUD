"""
Tests for motd_loader.py module.

Tests the Message of the Day loading functionality including file loading,
error handling, and fallback behavior.
"""

import os
import tempfile
from unittest.mock import patch

from server.utils.motd_loader import load_motd


class TestLoadMotd:
    """Test MOTD loading functionality."""

    def test_load_motd_file_exists(self) -> None:
        """Test loading MOTD from existing file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("Welcome to the Mythos!\n\nEnter at your own risk...")
            motd_file = f.name

        try:
            with patch("server.utils.motd_loader.get_config") as mock_config:
                mock_config.return_value = {"motd_file": motd_file}
                result = load_motd()

                assert "Welcome to the Mythos!" in result
                assert "Enter at your own risk" in result
        finally:
            os.unlink(motd_file)

    def test_load_motd_file_not_found(self) -> None:
        """Test loading MOTD when file doesn't exist."""
        with patch("server.utils.motd_loader.get_config") as mock_config:
            mock_config.return_value = {"motd_file": "./nonexistent/motd.txt"}
            result = load_motd()

            assert "Welcome to MythosMUD" in result

    def test_load_motd_config_error(self) -> None:
        """Test loading MOTD when config fails."""
        with patch("server.utils.motd_loader.get_config") as mock_config:
            mock_config.side_effect = Exception("Config error")
            result = load_motd()

            assert "Welcome to MythosMUD" in result

    def test_load_motd_file_read_error(self) -> None:
        """Test loading MOTD when file read fails."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("Test MOTD")
            motd_file = f.name

        try:
            # On Windows, 0o000 might not prevent reading, so we'll delete the file
            # to simulate a read error
            os.unlink(motd_file)

            with patch("server.utils.motd_loader.get_config") as mock_config:
                mock_config.return_value = {"motd_file": motd_file}
                result = load_motd()

                # The file doesn't exist, so it should return the fallback
                assert "Welcome to MythosMUD - Enter the realm of forbidden knowledge..." in result
        except OSError:
            # Clean up if the file still exists
            if os.path.exists(motd_file):
                os.chmod(motd_file, 0o644)  # Use secure permissions
                os.unlink(motd_file)
