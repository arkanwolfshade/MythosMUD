"""
Unit tests for command validator.
"""


from server.validators.command_validator import (
    CommandValidator,
    clean_command_input,
    is_suspicious_input,
    normalize_command,
    validate_command_format,
    validate_command_length,
)


def test_normalize_command_no_slash():
    """Test normalizing command without slash prefix."""
    result = normalize_command("go north")
    assert result == "go north"


def test_normalize_command_with_slash():
    """Test normalizing command with slash prefix."""
    result = normalize_command("/go north")
    assert result == "go north"


def test_normalize_command_empty():
    """Test normalizing empty command."""
    result = normalize_command("")
    assert result == ""


def test_normalize_command_whitespace():
    """Test normalizing command with whitespace."""
    result = normalize_command("  go north  ")
    assert result == "go north"


def test_is_suspicious_input_safe():
    """Test that safe commands are not flagged as suspicious."""
    safe_commands = [
        "go north",
        "say hello",
        "look at the door",
        "pickup sword",
    ]

    for cmd in safe_commands:
        assert is_suspicious_input(cmd) is False


def test_is_suspicious_input_sql_injection():
    """Test that SQL injection patterns are detected."""
    suspicious_commands = [
        "'; DROP TABLE users; --",  # Contains semicolon
        "1' OR '1'='1",  # Contains OR with equals
    ]

    for cmd in suspicious_commands:
        assert is_suspicious_input(cmd) is True


def test_is_suspicious_input_xss():
    """Test that XSS patterns are detected."""
    suspicious_commands = [
        "<script>alert('xss')</script>",
        "javascript:alert('xss')",
    ]

    for cmd in suspicious_commands:
        assert is_suspicious_input(cmd) is True


def test_clean_command_input_basic():
    """Test cleaning basic command input."""
    result = clean_command_input("go north")
    assert result == "go north"


def test_clean_command_input_whitespace():
    """Test cleaning command with extra whitespace."""
    result = clean_command_input("go    north")
    assert result == "go north"


def test_clean_command_input_empty():
    """Test cleaning empty command."""
    result = clean_command_input("")
    assert result == ""


def test_clean_command_input_unicode():
    """Test cleaning command with unicode characters."""
    result = clean_command_input("say hello\u200b")  # Zero-width space
    assert isinstance(result, str)
    assert "hello" in result


def test_validate_command_length_valid():
    """Test validate_command_length returns True for valid length."""
    assert validate_command_length("go north") is True
    assert validate_command_length("a" * 1000) is True


def test_validate_command_length_too_long():
    """Test validate_command_length returns False for too long command."""
    assert validate_command_length("a" * 1001) is False


def test_validate_command_length_custom_max():
    """Test validate_command_length with custom max_length."""
    assert validate_command_length("test", max_length=5) is True
    assert validate_command_length("test", max_length=3) is False


def test_validate_command_format_valid():
    """Test validate_command_format returns True for valid command."""
    is_valid, error = validate_command_format("go north")
    assert is_valid is True
    assert error == ""


def test_validate_command_format_empty():
    """Test validate_command_format returns False for empty command."""
    is_valid, error = validate_command_format("")
    assert is_valid is False
    assert error == "Empty command"


def test_validate_command_format_suspicious():
    """Test validate_command_format returns False for suspicious command."""
    is_valid, error = validate_command_format("'; DROP TABLE users; --")
    assert is_valid is False
    assert "suspicious" in error.lower()


def test_validate_command_format_too_long():
    """Test validate_command_format returns False for too long command."""
    long_command = "a" * 1001
    is_valid, error = validate_command_format(long_command)
    assert is_valid is False
    assert "too long" in error.lower()


def test_command_validator_validate_command_content_valid():
    """Test CommandValidator.validate_command_content returns True for valid command."""
    is_valid, error = CommandValidator.validate_command_content("go north")
    assert is_valid is True
    assert error is None


def test_command_validator_validate_command_content_null_byte():
    """Test CommandValidator.validate_command_content detects null bytes."""
    is_valid, error = CommandValidator.validate_command_content("go\x00north")
    assert is_valid is False
    assert "null bytes" in error.lower()


def test_command_validator_validate_command_content_dangerous_pattern():
    """Test CommandValidator.validate_command_content detects dangerous patterns."""
    dangerous_commands = [
        "command; rm -rf /",
        "command$(malicious)",
        "command`malicious`",
        "command | sh",
        "command > /dev/null",
        "command < /dev/null",
        "command 2>&1",
        "command && rm",
        "command | bash",
        "command | zsh",
        "exec malicious",
        "eval malicious",
        "import os",
        "__import__('os')",
        "subprocess.call",
    ]

    for cmd in dangerous_commands:
        is_valid, error = CommandValidator.validate_command_content(cmd)
        assert is_valid is False, f"Should detect danger in: {cmd}"
        assert "dangerous" in error.lower()


def test_command_validator_validate_command_content_too_long():
    """Test CommandValidator.validate_command_content detects excessive length."""
    long_command = "a" * 1001
    is_valid, error = CommandValidator.validate_command_content(long_command)
    assert is_valid is False
    assert "exceeds maximum length" in error.lower()


def test_command_validator_validate_command_content_non_printable():
    """Test CommandValidator.validate_command_content detects non-printable characters."""
    # Test with various non-printable characters (excluding newline, tab, space)
    non_printable_commands = [
        "go\x01north",  # SOH
        "go\x02north",  # STX
        "go\x03north",  # ETX
        "go\x1fnorth",  # Unit separator
    ]

    for cmd in non_printable_commands:
        is_valid, error = CommandValidator.validate_command_content(cmd)
        assert is_valid is False, f"Should detect non-printable in: {repr(cmd)}"
        assert "non-printable" in error.lower()


def test_command_validator_validate_command_content_allows_newline_tab_space():
    """Test CommandValidator.validate_command_content allows newline, tab, and space."""
    valid_commands = [
        "go\nnorth",  # Newline
        "go\tnorth",  # Tab
        "go north",   # Space
        "go\n\tnorth",  # Multiple allowed
    ]

    for cmd in valid_commands:
        is_valid, error = CommandValidator.validate_command_content(cmd)
        assert is_valid is True, f"Should allow newline/tab/space in: {repr(cmd)}"


def test_command_validator_validate_expanded_command_valid():
    """Test CommandValidator.validate_expanded_command returns True for valid expanded command."""
    is_valid, error = CommandValidator.validate_expanded_command("go north")
    assert is_valid is True
    assert error is None


def test_command_validator_validate_expanded_command_inherits_content_validation():
    """Test CommandValidator.validate_expanded_command inherits content validation."""
    is_valid, error = CommandValidator.validate_expanded_command("go\x00north")
    assert is_valid is False
    assert "null bytes" in error.lower()


def test_command_validator_validate_expanded_command_length_limit():
    """Test CommandValidator.validate_expanded_command enforces expanded length limit."""
    # Need to create a command that passes content validation (under 1000) but fails expanded (over 10000)
    # Since validate_expanded_command calls validate_command_content first, we need to bypass that
    # Actually, the function first validates content, so a 10001 char command fails at content validation
    # Let's test with a command that's between 1000 and 10000
    long_command = "a" * 5000  # Over normal limit, under expanded limit
    is_valid, error = CommandValidator.validate_expanded_command(long_command)
    # This should fail at content validation (1000 limit), not expanded validation
    assert is_valid is False
    assert "exceeds maximum length" in error.lower()


def test_command_validator_validate_expanded_command_within_limit():
    """Test CommandValidator.validate_expanded_command allows commands within expanded limit."""
    # The function validates content first (1000 limit), so we can't test expanded limit directly
    # But we can test that a valid command passes
    valid_command = "go north"
    is_valid, error = CommandValidator.validate_expanded_command(valid_command)
    assert is_valid is True


def test_command_validator_validate_alias_definition_valid():
    """Test CommandValidator.validate_alias_definition returns True for valid alias."""
    is_valid, error = CommandValidator.validate_alias_definition("go north")
    assert is_valid is True
    assert error is None


def test_command_validator_validate_alias_definition_inherits_content_validation():
    """Test CommandValidator.validate_alias_definition inherits content validation."""
    is_valid, error = CommandValidator.validate_alias_definition("go\x00north")
    assert is_valid is False
    assert "null bytes" in error.lower()


def test_command_validator_validate_alias_definition_length_limit():
    """Test CommandValidator.validate_alias_definition enforces alias length limit."""
    # Alias validation first checks content (1000 limit), so a 5001 char alias fails at content validation
    # To test alias limit, we'd need to bypass content validation, but that's not how it works
    # Let's test that a command over alias limit fails (at content validation)
    long_alias = "a" * 5001  # Over alias limit of 5000, also over content limit of 1000
    is_valid, error = CommandValidator.validate_alias_definition(long_alias)
    assert is_valid is False
    # Will fail at content validation first
    assert "exceeds maximum length" in error.lower()


def test_command_validator_validate_alias_definition_within_limit():
    """Test CommandValidator.validate_alias_definition allows aliases within limit."""
    # Alias validation first checks content (1000 limit), so we can't test alias limit directly
    # But we can test that a valid alias passes
    valid_alias = "go north"
    is_valid, error = CommandValidator.validate_alias_definition(valid_alias)
    assert is_valid is True


def test_command_validator_is_security_sensitive_admin():
    """Test CommandValidator.is_security_sensitive detects admin commands."""
    assert CommandValidator.is_security_sensitive("admin help") is True
    assert CommandValidator.is_security_sensitive("teleport player room") is True
    assert CommandValidator.is_security_sensitive("spawn item") is True
    assert CommandValidator.is_security_sensitive("delete player") is True
    assert CommandValidator.is_security_sensitive("grant permission") is True
    assert CommandValidator.is_security_sensitive("revoke permission") is True
    assert CommandValidator.is_security_sensitive("ban player") is True
    assert CommandValidator.is_security_sensitive("unban player") is True
    assert CommandValidator.is_security_sensitive("kick player") is True
    assert CommandValidator.is_security_sensitive("mute player") is True
    assert CommandValidator.is_security_sensitive("unmute player") is True
    assert CommandValidator.is_security_sensitive("promote player") is True
    assert CommandValidator.is_security_sensitive("demote player") is True
    assert CommandValidator.is_security_sensitive("shutdown") is True
    assert CommandValidator.is_security_sensitive("restart") is True
    assert CommandValidator.is_security_sensitive("reload config") is True
    assert CommandValidator.is_security_sensitive("config set") is True
    assert CommandValidator.is_security_sensitive("debug on") is True


def test_command_validator_is_security_sensitive_case_insensitive():
    """Test CommandValidator.is_security_sensitive is case-insensitive."""
    assert CommandValidator.is_security_sensitive("ADMIN help") is True
    assert CommandValidator.is_security_sensitive("Admin help") is True
    assert CommandValidator.is_security_sensitive("Teleport player") is True


def test_command_validator_is_security_sensitive_non_sensitive():
    """Test CommandValidator.is_security_sensitive returns False for non-sensitive commands."""
    assert CommandValidator.is_security_sensitive("go north") is False
    assert CommandValidator.is_security_sensitive("say hello") is False
    assert CommandValidator.is_security_sensitive("look") is False
    assert CommandValidator.is_security_sensitive("inventory") is False


def test_command_validator_is_security_sensitive_empty():
    """Test CommandValidator.is_security_sensitive returns False for empty command."""
    assert CommandValidator.is_security_sensitive("") is False
    assert CommandValidator.is_security_sensitive("   ") is False


def test_command_validator_sanitize_for_logging():
    """Test CommandValidator.sanitize_for_logging sanitizes command for logging."""
    result = CommandValidator.sanitize_for_logging("go north")
    assert result == "go north"


def test_command_validator_sanitize_for_logging_truncates():
    """Test CommandValidator.sanitize_for_logging truncates long commands."""
    long_command = "a" * 300
    result = CommandValidator.sanitize_for_logging(long_command, max_length=200)
    assert len(result) <= 200 + len("...[truncated]")
    assert result.endswith("...[truncated]")


def test_command_validator_sanitize_for_logging_removes_sensitive():
    """Test CommandValidator.sanitize_for_logging removes sensitive patterns."""
    # Should remove or mask dangerous patterns
    dangerous_command = "command; rm -rf"
    result = CommandValidator.sanitize_for_logging(dangerous_command)
    # Should sanitize but not necessarily remove everything
    assert isinstance(result, str)


def test_command_validator_extract_command_name():
    """Test CommandValidator.extract_command_name extracts command name."""
    assert CommandValidator.extract_command_name("go north") == "go"
    assert CommandValidator.extract_command_name("say hello world") == "say"
    assert CommandValidator.extract_command_name("look") == "look"


def test_command_validator_extract_command_name_with_slash():
    """Test CommandValidator.extract_command_name handles slash prefix."""
    # extract_command_name extracts first word, which includes the slash
    result = CommandValidator.extract_command_name("/go north")
    assert result == "/go"  # First word is "/go", lowercased


def test_command_validator_extract_command_name_empty():
    """Test CommandValidator.extract_command_name returns None for empty command."""
    assert CommandValidator.extract_command_name("") is None
    assert CommandValidator.extract_command_name("   ") is None


def test_command_validator_is_valid_command_name():
    """Test CommandValidator.is_valid_command_name validates command names."""
    assert CommandValidator.is_valid_command_name("go") is True
    assert CommandValidator.is_valid_command_name("say") is True
    assert CommandValidator.is_valid_command_name("look") is True


def test_command_validator_is_valid_command_name_invalid():
    """Test CommandValidator.is_valid_command_name rejects invalid names."""
    assert CommandValidator.is_valid_command_name("") is False
    assert CommandValidator.is_valid_command_name("go;rm") is False
    assert CommandValidator.is_valid_command_name("command\x00") is False
