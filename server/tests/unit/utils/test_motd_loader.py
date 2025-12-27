"""
Unit tests for MOTD (Message of the Day) loader.

Tests MOTD loading functionality with various file scenarios.
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from server.utils.motd_loader import load_motd


def test_load_motd_file_exists():
    """Test load_motd when MOTD file exists."""
    with tempfile.TemporaryDirectory() as tmpdir:
        motd_file = os.path.join(tmpdir, "motd.txt")
        with open(motd_file, "w", encoding="utf-8") as f:
            f.write("Welcome to MythosMUD!\nTest MOTD content.")
        
        with patch("server.utils.motd_loader.get_config") as mock_config:
            mock_config_instance = MagicMock()
            mock_config_instance.get.return_value = motd_file
            mock_config.return_value = mock_config_instance
            
            result = load_motd()
            
            assert "Welcome to MythosMUD!" in result
            assert "Test MOTD content" in result


def test_load_motd_file_not_found():
    """Test load_motd when MOTD file does not exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        motd_file = os.path.join(tmpdir, "nonexistent.txt")
        
        with patch("server.utils.motd_loader.get_config") as mock_config:
            mock_config_instance = MagicMock()
            mock_config_instance.get.return_value = motd_file
            mock_config.return_value = mock_config_instance
            
            result = load_motd()
            
            assert "Welcome to MythosMUD" in result
            assert "Enter the realm of forbidden knowledge" in result


def test_load_motd_default_path():
    """Test load_motd uses default path when config doesn't specify."""
    with patch("server.utils.motd_loader.get_config") as mock_config:
        mock_config_instance = MagicMock()
        mock_config_instance.get.return_value = "./data/motd.txt"
        mock_config.return_value = mock_config_instance
        
        with patch("os.path.exists", return_value=False):
            result = load_motd()
            
            assert "Welcome to MythosMUD" in result


def test_load_motd_relative_path_resolution():
    """Test load_motd resolves relative paths correctly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        motd_file = "./data/motd.txt"
        
        with patch("server.utils.motd_loader.get_config") as mock_config:
            mock_config_instance = MagicMock()
            mock_config_instance.get.return_value = motd_file
            mock_config.return_value = mock_config_instance
            
            with patch("server.utils.motd_loader.os.path.dirname") as mock_dirname:
                # Mock the path resolution
                mock_dirname.side_effect = lambda x: tmpdir if "utils" in str(x) else os.path.dirname(x)
                
                with patch("os.path.exists", return_value=False):
                    result = load_motd()
                    
                    assert "Welcome to MythosMUD" in result


def test_load_motd_file_read_error():
    """Test load_motd handles file read errors gracefully."""
    with tempfile.TemporaryDirectory() as tmpdir:
        motd_file = os.path.join(tmpdir, "motd.txt")
        
        with patch("server.utils.motd_loader.get_config") as mock_config:
            mock_config_instance = MagicMock()
            mock_config_instance.get.return_value = motd_file
            mock_config.return_value = mock_config_instance
            
            with patch("os.path.exists", return_value=True):
                with patch("builtins.open", side_effect=IOError("Permission denied")):
                    result = load_motd()
                    
                    assert "Welcome to MythosMUD" in result


def test_load_motd_config_error():
    """Test load_motd handles config errors gracefully."""
    with patch("server.utils.motd_loader.get_config", side_effect=Exception("Config error")):
        result = load_motd()
        
        assert "Welcome to MythosMUD" in result


def test_load_motd_strips_whitespace():
    """Test load_motd strips whitespace from file content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        motd_file = os.path.join(tmpdir, "motd.txt")
        with open(motd_file, "w", encoding="utf-8") as f:
            f.write("   \n  Welcome to MythosMUD  \n  \n")
        
        with patch("server.utils.motd_loader.get_config") as mock_config:
            mock_config_instance = MagicMock()
            mock_config_instance.get.return_value = motd_file
            mock_config.return_value = mock_config_instance
            
            result = load_motd()
            
            # Should strip leading/trailing whitespace
            assert result == "Welcome to MythosMUD"
