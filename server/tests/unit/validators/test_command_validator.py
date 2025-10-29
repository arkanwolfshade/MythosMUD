"""
Unit tests for command validation utilities.

This module tests both legacy validation functions and the CommandValidator class
to ensure comprehensive security validation of command input.

Tests cover:
- Legacy validation functions (normalize_command, is_suspicious_input, etc.)
- CommandValidator class methods (validation, sanitization, pattern detection)
- Security pattern detection and prevention
- Edge cases and boundary conditions
"""

from server.validators.command_validator import (
    CommandValidator,
    clean_command_input,
    is_suspicious_input,
    normalize_command,
    validate_command_format,
    validate_command_length,
)

# ============================================================================
# LEGACY VALIDATION FUNCTIONS TESTS
# ============================================================================


class TestNormalizeCommand:
    """Test suite for normalize_command() function."""

    def test_normalize_command_with_slash_prefix(self):
        """Test that slash prefix is removed correctly."""
        assert normalize_command("/look") == "look"
        assert normalize_command("/go north") == "go north"
        assert normalize_command("/attack rat") == "attack rat"

    def test_normalize_command_without_slash(self):
        """Test that commands without slash are returned with whitespace stripped."""
        assert normalize_command("look") == "look"
        assert normalize_command("go north") == "go north"
        assert normalize_command("  look  ") == "look"

    def test_normalize_command_empty_string(self):
        """Test that empty string is returned as is."""
        assert normalize_command("") == ""

    def test_normalize_command_none(self):
        """Test that None is returned as is."""
        assert normalize_command(None) is None

    def test_normalize_command_with_whitespace(self):
        """Test that whitespace is properly normalized."""
        # The function strips whitespace after removing slash
        assert normalize_command("/  look  ") == "look"
        # Leading whitespace before slash is preserved, then stripped
        assert normalize_command("  /look  ") == "/look"  # Doesn't start with slash after strip
        assert normalize_command("   look   ") == "look"


class TestIsSuspiciousInput:
    """Test suite for is_suspicious_input() function."""

    def test_is_suspicious_input_shell_injection(self):
        """Test detection of shell injection patterns."""
        # Test various shell metacharacters
        # Note: These patterns come from INJECTION_PATTERNS in security_validator
        assert is_suspicious_input("look; echo 'test'") is True  # Shell metacharacter
        assert is_suspicious_input("attack' OR '1'='1") is True  # SQL injection
        assert is_suspicious_input("look<script>alert(1)</script>") is True  # XSS

    def test_is_suspicious_input_sql_injection(self):
        """Test detection of SQL injection patterns."""
        assert is_suspicious_input("look'; DROP TABLE players--") is True
        assert is_suspicious_input("name' OR '1'='1") is True

    def test_is_suspicious_input_python_injection(self):
        """Test detection of Python code injection patterns."""
        assert is_suspicious_input("import os; os.system('ls')") is True
        assert is_suspicious_input("__import__('os')") is True
        assert is_suspicious_input("exec('print(1)')") is True

    def test_is_suspicious_input_safe_creative_text(self):
        """Test that legitimate creative text is not flagged."""
        # Creative roleplay text should pass
        assert is_suspicious_input("look around the ancient library") is False
        assert is_suspicious_input("say Hello, my name is O'Brien!") is False
        assert is_suspicious_input("emote *waves frantically*") is False

    def test_is_suspicious_input_legitimate_special_chars(self):
        """Test that legitimate special characters don't trigger false positives."""
        assert is_suspicious_input("look north") is False
        assert is_suspicious_input("say I'm feeling great!") is False
        assert is_suspicious_input("whisper Are you okay?") is False


class TestCleanCommandInput:
    """Test suite for clean_command_input() function."""

    def test_clean_command_input_unicode_normalization(self):
        """Test that Unicode is properly normalized."""
        # Unicode normalization should fix mojibake and normalize forms
        result = clean_command_input("look café")
        assert result is not None
        assert len(result) > 0

    def test_clean_command_input_ansi_removal(self):
        """Test that ANSI codes are removed."""
        # ANSI escape codes should be stripped
        command_with_ansi = "look \x1b[31mred\x1b[0m north"
        result = clean_command_input(command_with_ansi)
        assert "\x1b" not in result

    def test_clean_command_input_whitespace_normalization(self):
        """Test that whitespace is normalized."""
        assert clean_command_input("look   north") == "look north"
        assert clean_command_input("  look  ") == "look"
        assert clean_command_input("look\t\tnorth") == "look north"

    def test_clean_command_input_control_char_removal(self):
        """Test that control characters are removed."""
        # Control characters should be stripped
        command_with_control = "look\x00north"
        result = clean_command_input(command_with_control)
        assert "\x00" not in result

    def test_clean_command_input_preserves_valid_text(self):
        """Test that valid text is preserved."""
        valid_commands = [
            "look north",
            "attack rat",
            "say Hello, world!",
            "go east",
        ]
        for cmd in valid_commands:
            result = clean_command_input(cmd)
            assert result == cmd


class TestValidateCommandLength:
    """Test suite for validate_command_length() function."""

    def test_validate_command_length_within_limits(self):
        """Test that commands within limits pass validation."""
        assert validate_command_length("look") is True
        assert validate_command_length("a" * 100) is True
        assert validate_command_length("a" * 999) is True

    def test_validate_command_length_at_limit(self):
        """Test that commands at exact limit pass validation."""
        assert validate_command_length("a" * 1000) is True

    def test_validate_command_length_exceeds_limit(self):
        """Test that commands exceeding limits fail validation."""
        assert validate_command_length("a" * 1001) is False
        assert validate_command_length("a" * 2000) is False

    def test_validate_command_length_custom_max_length(self):
        """Test validation with custom max_length parameter."""
        assert validate_command_length("a" * 50, max_length=100) is True
        assert validate_command_length("a" * 100, max_length=100) is True
        assert validate_command_length("a" * 101, max_length=100) is False


class TestValidateCommandFormat:
    """Test suite for validate_command_format() function."""

    def test_validate_command_format_valid(self):
        """Test that valid commands pass format validation."""
        is_valid, error = validate_command_format("look north")
        assert is_valid is True
        assert error == ""

    def test_validate_command_format_empty(self):
        """Test that empty commands fail validation."""
        is_valid, error = validate_command_format("")
        assert is_valid is False
        assert error == "Empty command"

    def test_validate_command_format_suspicious(self):
        """Test that suspicious patterns fail validation."""
        is_valid, error = validate_command_format("look; rm -rf /")
        assert is_valid is False
        assert error == "Command contains suspicious patterns"

    def test_validate_command_format_too_long(self):
        """Test that overly long commands fail validation."""
        is_valid, error = validate_command_format("a" * 1001)
        assert is_valid is False
        assert error == "Command too long"

    def test_validate_command_format_error_messages(self):
        """Test that error messages are meaningful."""
        _, error = validate_command_format("")
        assert len(error) > 0
        assert isinstance(error, str)


# ============================================================================
# COMMANDVALIDATOR CLASS TESTS
# ============================================================================


class TestCommandValidatorValidateCommandContent:
    """Test suite for CommandValidator.validate_command_content()."""

    def test_validate_command_content_valid(self):
        """Test that valid commands pass validation."""
        is_valid, error = CommandValidator.validate_command_content("look north")
        assert is_valid is True
        assert error is None

    def test_validate_command_content_null_bytes(self):
        """Test that null bytes are detected."""
        is_valid, error = CommandValidator.validate_command_content("look\x00north")
        assert is_valid is False
        assert "null bytes" in error.lower()

    def test_validate_command_content_dangerous_pattern_rm_rf(self):
        """Test detection of dangerous rm -rf pattern."""
        is_valid, error = CommandValidator.validate_command_content("; rm -rf /")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_command_substitution(self):
        """Test detection of command substitution pattern."""
        is_valid, error = CommandValidator.validate_command_content("look $(cat /etc/passwd)")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_backtick(self):
        """Test detection of backtick command execution."""
        is_valid, error = CommandValidator.validate_command_content("look `whoami`")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_pipe_shell(self):
        """Test detection of pipe to shell."""
        is_valid, error = CommandValidator.validate_command_content("look | sh")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_device_redirect(self):
        """Test detection of device file redirection."""
        is_valid, error = CommandValidator.validate_command_content("look > /dev/null")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_stderr_redirect(self):
        """Test detection of stderr redirection."""
        is_valid, error = CommandValidator.validate_command_content("look 2>&1")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_chained_rm(self):
        """Test detection of chained rm command."""
        is_valid, error = CommandValidator.validate_command_content("look && rm -rf")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_pipe_bash(self):
        """Test detection of pipe to bash."""
        is_valid, error = CommandValidator.validate_command_content("look | bash")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_pipe_zsh(self):
        """Test detection of pipe to zsh."""
        is_valid, error = CommandValidator.validate_command_content("look | zsh")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_exec(self):
        """Test detection of exec command."""
        is_valid, error = CommandValidator.validate_command_content("exec ls")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_eval(self):
        """Test detection of eval command."""
        is_valid, error = CommandValidator.validate_command_content("eval print(1)")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_import_os(self):
        """Test detection of Python os import."""
        is_valid, error = CommandValidator.validate_command_content("import os")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_dunder_import(self):
        """Test detection of Python dynamic import."""
        is_valid, error = CommandValidator.validate_command_content("__import__('os')")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_dangerous_pattern_subprocess(self):
        """Test detection of subprocess usage."""
        is_valid, error = CommandValidator.validate_command_content("subprocess.call(['ls'])")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_command_content_excessive_length(self):
        """Test that excessive length is detected."""
        long_command = "a" * (CommandValidator.MAX_COMMAND_LENGTH + 1)
        is_valid, error = CommandValidator.validate_command_content(long_command)
        assert is_valid is False
        assert "maximum length" in error.lower()

    def test_validate_command_content_non_printable_chars(self):
        """Test that non-printable characters are detected."""
        # ASCII control characters (except tab, newline, space)
        is_valid, error = CommandValidator.validate_command_content("look\x01north")
        assert is_valid is False
        assert "non-printable" in error.lower()

    def test_validate_command_content_allows_tabs_and_newlines(self):
        """Test that tabs and newlines are allowed."""
        is_valid, error = CommandValidator.validate_command_content("look\tnorth")
        assert is_valid is True
        assert error is None

        is_valid, error = CommandValidator.validate_command_content("look\nnorth")
        assert is_valid is True
        assert error is None

    def test_validate_command_content_error_message_accuracy(self):
        """Test that error messages are accurate and helpful."""
        # Null bytes
        _, error = CommandValidator.validate_command_content("look\x00")
        assert "null bytes" in error.lower()

        # Dangerous pattern
        _, error = CommandValidator.validate_command_content("; rm -rf")
        assert "dangerous pattern" in error.lower()

        # Too long
        _, error = CommandValidator.validate_command_content("a" * 1001)
        assert "maximum length" in error.lower()

        # Non-printable
        _, error = CommandValidator.validate_command_content("look\x01")
        assert "non-printable" in error.lower()


class TestCommandValidatorValidateExpandedCommand:
    """Test suite for CommandValidator.validate_expanded_command()."""

    def test_validate_expanded_command_valid(self):
        """Test that valid expanded commands pass validation."""
        is_valid, error = CommandValidator.validate_expanded_command("look north; go east; attack rat")
        assert is_valid is True
        assert error is None

    def test_validate_expanded_command_exceeds_max_length(self):
        """Test that commands exceeding expanded max length fail."""
        # Need a command that passes normal validation but exceeds expanded limit
        # Normal max is 1000, expanded max is 10000
        long_command = "a" * (CommandValidator.MAX_EXPANDED_COMMAND_LENGTH + 1)
        is_valid, error = CommandValidator.validate_expanded_command(long_command)
        assert is_valid is False
        # It will fail on the basic validation first (exceeds MAX_COMMAND_LENGTH)
        assert "maximum length" in error.lower()

    def test_validate_expanded_command_dangerous_pattern(self):
        """Test that dangerous patterns in expanded commands are detected."""
        is_valid, error = CommandValidator.validate_expanded_command("look; rm -rf /")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_expanded_command_null_bytes(self):
        """Test that null bytes in expanded commands are detected."""
        is_valid, error = CommandValidator.validate_expanded_command("look\x00north")
        assert is_valid is False
        assert "null bytes" in error.lower()


class TestCommandValidatorValidateAliasDefinition:
    """Test suite for CommandValidator.validate_alias_definition()."""

    def test_validate_alias_definition_valid(self):
        """Test that valid alias definitions pass validation."""
        is_valid, error = CommandValidator.validate_alias_definition("look north; say I see something")
        assert is_valid is True
        assert error is None

    def test_validate_alias_definition_exceeds_max_length(self):
        """Test that alias definitions exceeding max length fail."""
        # Alias max is 5000, but validate_command_content checks against 1000 first
        long_alias = "a" * (CommandValidator.MAX_ALIAS_DEFINITION_LENGTH + 1)
        is_valid, error = CommandValidator.validate_alias_definition(long_alias)
        assert is_valid is False
        # It will fail on the basic validation first (exceeds MAX_COMMAND_LENGTH of 1000)
        assert "maximum length" in error.lower()

    def test_validate_alias_definition_dangerous_pattern(self):
        """Test that dangerous patterns in alias definitions are detected."""
        is_valid, error = CommandValidator.validate_alias_definition("look; rm -rf /")
        assert is_valid is False
        assert "dangerous pattern" in error.lower()

    def test_validate_alias_definition_null_bytes(self):
        """Test that null bytes in alias definitions are detected."""
        is_valid, error = CommandValidator.validate_alias_definition("look\x00north")
        assert is_valid is False
        assert "null bytes" in error.lower()


class TestCommandValidatorIsSecuritySensitive:
    """Test suite for CommandValidator.is_security_sensitive()."""

    def test_is_security_sensitive_admin_commands(self):
        """Test that all security-sensitive commands are detected."""
        sensitive_commands = [
            "admin status",
            "teleport player1 room2",
            "spawn dragon",
            "delete item123",
            "grant admin player1",
            "revoke mod player2",
            "ban player3",
            "unban player4",
            "kick player5",
            "mute player6",
            "unmute player7",
            "promote player8",
            "demote player9",
            "shutdown now",
            "restart server",
            "reload config",
            "config set debug true",
            "debug on",
        ]

        for cmd in sensitive_commands:
            assert CommandValidator.is_security_sensitive(cmd) is True, f"Failed for: {cmd}"

    def test_is_security_sensitive_non_admin_commands(self):
        """Test that non-sensitive commands are not flagged."""
        normal_commands = [
            "look north",
            "go east",
            "attack rat",
            "say hello",
            "whisper Are you there?",
            "inventory",
            "stats",
        ]

        for cmd in normal_commands:
            assert CommandValidator.is_security_sensitive(cmd) is False, f"Failed for: {cmd}"

    def test_is_security_sensitive_empty_command(self):
        """Test that empty commands are not flagged as sensitive."""
        assert CommandValidator.is_security_sensitive("") is False
        assert CommandValidator.is_security_sensitive("   ") is False

    def test_is_security_sensitive_case_insensitive(self):
        """Test that detection is case-insensitive."""
        assert CommandValidator.is_security_sensitive("ADMIN status") is True
        assert CommandValidator.is_security_sensitive("Admin status") is True
        assert CommandValidator.is_security_sensitive("aDmIn status") is True

    def test_is_security_sensitive_command_with_arguments(self):
        """Test that commands with various arguments are detected."""
        assert CommandValidator.is_security_sensitive("teleport player1 room2 force") is True
        assert CommandValidator.is_security_sensitive("ban player reason=spam duration=7d") is True


class TestCommandValidatorSanitizeForLogging:
    """Test suite for CommandValidator.sanitize_for_logging()."""

    def test_sanitize_for_logging_password_masking(self):
        """Test that passwords are masked."""
        sanitized = CommandValidator.sanitize_for_logging("login user password=secret123")
        assert "secret123" not in sanitized
        assert "password=****" in sanitized

    def test_sanitize_for_logging_token_masking(self):
        """Test that tokens are masked."""
        sanitized = CommandValidator.sanitize_for_logging("api_call token abc123xyz")
        assert "abc123xyz" not in sanitized
        assert "token=****" in sanitized

    def test_sanitize_for_logging_secret_masking(self):
        """Test that secrets are masked."""
        sanitized = CommandValidator.sanitize_for_logging("config secret=verysecret")
        assert "verysecret" not in sanitized
        assert "secret=****" in sanitized

    def test_sanitize_for_logging_key_masking(self):
        """Test that keys are masked."""
        sanitized = CommandValidator.sanitize_for_logging("auth key:apikey123")
        assert "apikey123" not in sanitized
        assert "key=****" in sanitized

    def test_sanitize_for_logging_truncation(self):
        """Test that long commands are truncated."""
        long_command = "a" * 300
        sanitized = CommandValidator.sanitize_for_logging(long_command, max_length=200)
        assert len(sanitized) <= 215  # 200 + "[truncated]" length
        assert "[truncated]" in sanitized

    def test_sanitize_for_logging_control_char_removal(self):
        """Test that control characters are replaced."""
        command = "look\x00\x01north"
        sanitized = CommandValidator.sanitize_for_logging(command)
        assert "\x00" not in sanitized
        assert "\x01" not in sanitized
        assert "?" in sanitized or "north" in sanitized

    def test_sanitize_for_logging_custom_max_length(self):
        """Test sanitization with custom max_length."""
        long_command = "a" * 200
        sanitized = CommandValidator.sanitize_for_logging(long_command, max_length=50)
        assert len(sanitized) <= 65  # 50 + "[truncated]" length


class TestCommandValidatorExtractCommandName:
    """Test suite for CommandValidator.extract_command_name()."""

    def test_extract_command_name_simple(self):
        """Test extraction from simple commands."""
        assert CommandValidator.extract_command_name("look") == "look"
        assert CommandValidator.extract_command_name("go") == "go"
        assert CommandValidator.extract_command_name("attack") == "attack"

    def test_extract_command_name_with_args(self):
        """Test extraction from commands with arguments."""
        assert CommandValidator.extract_command_name("look north") == "look"
        assert CommandValidator.extract_command_name("go east quickly") == "go"
        assert CommandValidator.extract_command_name("attack rat fiercely") == "attack"

    def test_extract_command_name_with_pipes(self):
        """Test extraction from commands with pipes."""
        assert CommandValidator.extract_command_name("look | grep rat") == "look"
        assert CommandValidator.extract_command_name("inventory | wc") == "inventory"

    def test_extract_command_name_with_semicolons(self):
        """Test extraction from commands with semicolons."""
        assert CommandValidator.extract_command_name("look; go north") == "look"
        assert CommandValidator.extract_command_name("attack rat; inventory") == "attack"

    def test_extract_command_name_empty(self):
        """Test extraction from empty/whitespace commands."""
        assert CommandValidator.extract_command_name("") is None
        assert CommandValidator.extract_command_name("   ") is None

    def test_extract_command_name_only_whitespace(self):
        """Test extraction from commands with only whitespace."""
        assert CommandValidator.extract_command_name("     ") is None
        assert CommandValidator.extract_command_name("\t\t\t") is None

    def test_extract_command_name_mixed_separators(self):
        """Test extraction from commands with mixed separators."""
        assert CommandValidator.extract_command_name("look | grep rat; go north") == "look"
        assert CommandValidator.extract_command_name("attack; inventory | sort") == "attack"


class TestCommandValidatorIsValidCommandName:
    """Test suite for CommandValidator.is_valid_command_name()."""

    def test_is_valid_command_name_valid_names(self):
        """Test that valid command names pass validation."""
        valid_names = [
            "look",
            "go",
            "attack",
            "look_around",
            "multi-word",
            "cmd123",
            "a",  # Single character
            "MyCommand",
            "UPPERCASE",
        ]

        for name in valid_names:
            assert CommandValidator.is_valid_command_name(name) is True, f"Failed for: {name}"

    def test_is_valid_command_name_invalid_start_digit(self):
        """Test that names starting with digits fail validation."""
        assert CommandValidator.is_valid_command_name("123cmd") is False
        assert CommandValidator.is_valid_command_name("9attack") is False

    def test_is_valid_command_name_invalid_special_chars(self):
        """Test that names with invalid special characters fail."""
        invalid_names = [
            "look!",
            "go@north",
            "attack#rat",
            "cmd$",
            "look%",
            "go^up",
            "attack&",
            "cmd*",
            "look()",
            "go=east",
            "attack+",
        ]

        for name in invalid_names:
            assert CommandValidator.is_valid_command_name(name) is False, f"Failed for: {name}"

    def test_is_valid_command_name_too_long(self):
        """Test that names exceeding 50 characters fail validation."""
        assert CommandValidator.is_valid_command_name("a" * 51) is False
        assert CommandValidator.is_valid_command_name("a" * 100) is False

    def test_is_valid_command_name_empty(self):
        """Test that empty names fail validation."""
        assert CommandValidator.is_valid_command_name("") is False
        assert CommandValidator.is_valid_command_name(None) is False

    def test_is_valid_command_name_edge_cases(self):
        """Test edge cases for command name validation."""
        # Exactly 50 characters - should pass
        assert CommandValidator.is_valid_command_name("a" * 50) is True

        # Names with underscores and dashes - should pass
        assert CommandValidator.is_valid_command_name("look_around-carefully") is True

        # Name starting with underscore - should fail
        assert CommandValidator.is_valid_command_name("_private") is False

        # Name starting with dash - should fail
        assert CommandValidator.is_valid_command_name("-command") is False


# ============================================================================
# INTEGRATION AND EDGE CASE TESTS
# ============================================================================


class TestCommandValidatorIntegration:
    """Integration tests for command validation workflow."""

    def test_validation_workflow_safe_command(self):
        """Test complete validation workflow for a safe command."""
        # Normalize
        normalized = normalize_command("/look north")
        assert normalized == "look north"

        # Clean
        cleaned = clean_command_input(normalized)
        assert cleaned == "look north"

        # Validate format
        is_valid, error_msg = validate_command_format(cleaned)
        assert is_valid is True
        assert error_msg == ""

        # Validate content
        is_valid, error_msg = CommandValidator.validate_command_content(cleaned)
        assert is_valid is True
        assert error_msg is None

    def test_validation_workflow_dangerous_command(self):
        """Test complete validation workflow for a dangerous command."""
        # Start with a malicious command
        dangerous = "/look; rm -rf /"

        # Normalize
        normalized = normalize_command(dangerous)
        assert normalized == "look; rm -rf /"

        # This should be caught by validation
        is_valid, error = validate_command_format(normalized)
        assert is_valid is False
        assert "suspicious" in error.lower()

    def test_validation_workflow_with_unicode(self):
        """Test validation workflow with Unicode characters."""
        unicode_command = "/look café"
        normalized = normalize_command(unicode_command)
        cleaned = clean_command_input(normalized)
        is_valid, _ = CommandValidator.validate_command_content(cleaned)
        assert is_valid is True

    def test_security_sensitive_command_workflow(self):
        """Test workflow for security-sensitive commands."""
        admin_cmd = "admin status"

        # Should pass validation
        is_valid, error = CommandValidator.validate_command_content(admin_cmd)
        assert is_valid is True

        # But should be flagged as security-sensitive
        assert CommandValidator.is_security_sensitive(admin_cmd) is True

        # Should be sanitized for logging
        sanitized = CommandValidator.sanitize_for_logging(admin_cmd)
        assert len(sanitized) > 0
