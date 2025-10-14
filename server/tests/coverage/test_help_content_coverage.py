"""
Tests for help content functions to improve coverage.

This module provides targeted tests for help_content.py
to cover the remaining uncovered utility functions.

As noted in the restricted archives, all scholarly tools
must be tested, even those rarely invoked.
"""

from ..help.help_content import get_command_categories, get_commands_by_category, get_help_content


class TestHelpContentUtilities:
    """Test help content utility functions."""

    def test_get_command_categories(self):
        """Test getting all command categories.

        AI: Tests get_command_categories function (lines 478-483).
        """
        categories = get_command_categories()

        assert isinstance(categories, list)
        assert len(categories) > 0
        # Verify sorted order
        assert categories == sorted(categories)
        # Verify expected categories are present
        assert "System" in categories
        assert "Communication" in categories

    def test_get_commands_by_category_system(self):
        """Test getting commands by category - System.

        AI: Tests get_commands_by_category function (lines 486-492).
        """
        commands = get_commands_by_category("System")

        assert isinstance(commands, list)
        assert len(commands) > 0
        # Verify all returned commands are tuples
        for cmd_name, cmd_info in commands:
            assert isinstance(cmd_name, str)
            assert isinstance(cmd_info, dict)
            assert cmd_info["category"] == "System"

    def test_get_commands_by_category_communication(self):
        """Test getting commands by category - Communication.

        AI: Tests get_commands_by_category with different category.
        """
        commands = get_commands_by_category("Communication")

        assert isinstance(commands, list)
        assert len(commands) > 0
        for _cmd_name, cmd_info in commands:
            assert cmd_info["category"] == "Communication"

    def test_get_commands_by_category_empty(self):
        """Test getting commands for nonexistent category.

        AI: Tests edge case with category that has no commands.
        """
        commands = get_commands_by_category("NonexistentCategory")

        assert isinstance(commands, list)
        assert len(commands) == 0

    def test_get_help_content_general(self):
        """Test general help content retrieval.

        AI: Tests help content with no specific command.
        """
        content = get_help_content(None)

        assert isinstance(content, str)
        assert "MythosMUD Help System" in content
        assert "Commands" in content

    def test_get_help_content_specific_command(self):
        """Test help content for specific commands.

        AI: Tests help content for known commands.
        """
        for command in ["look", "go", "say", "help"]:
            content = get_help_content(command)

            assert isinstance(content, str)
            assert command.upper() in content.upper()

    def test_get_help_content_unknown_command(self):
        """Test help content for unknown command.

        AI: Tests fallback help for unknown commands.
        """
        content = get_help_content("unknowncommand")

        assert isinstance(content, str)
        assert "not found" in content.lower()
        assert "unknowncommand" in content.lower()

    def test_get_help_content_case_insensitive(self):
        """Test that help content is case-insensitive.

        AI: Tests that command lookup is case-insensitive.
        """
        lower_content = get_help_content("look")
        upper_content = get_help_content("LOOK")
        mixed_content = get_help_content("LoOk")

        # Should all return the same content
        assert lower_content == upper_content == mixed_content
