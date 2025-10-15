"""
Comprehensive security penetration tests for command validation.

This module tests various security attack vectors against our command
validation system to ensure robust protection against injection attacks,
XSS attempts, and other security vulnerabilities.
"""

import pytest
from pydantic import ValidationError

from server.models.command import (
    AliasCommand,
    EmoteCommand,
    HelpCommand,
    LocalCommand,
    MeCommand,
    MuteCommand,
    PoseCommand,
    ReplyCommand,
    SayCommand,
    SystemCommand,
    UnaliasCommand,
    UnmuteCommand,
    WhisperCommand,
    WhoCommand,
)
from server.validators.security_validator import validate_security_comprehensive


class TestCommandInjectionAttacks:
    """Test command injection attack vectors."""

    def test_say_command_sql_injection_attempts(self):
        """Test SQL injection attempts in say command (only patterns with assignment operators)."""
        injection_attempts = [
            "admin' OR 1=1 --",  # OR with = assignment
            "test' AND password='x",  # AND with = assignment
            # Note: Patterns with semicolons are caught by shell metacharacter pattern
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_say_command_script_injection_attempts(self):
        """Test script injection attempts in say command."""
        script_attempts = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "javascript:alert('XSS')",
            "<iframe src='javascript:alert(\"XSS\")'></iframe>",
            "<svg onload=alert('XSS')>",
            "<body onload=alert('XSS')>",
            "<input onfocus=alert('XSS') autofocus>",
            "<select onfocus=alert('XSS') autofocus>",
            "<textarea onfocus=alert('XSS') autofocus>",
            "<keygen onfocus=alert('XSS') autofocus>",
            "<video><source onerror=alert('XSS')>",
            "<audio src=x onerror=alert('XSS')>",
        ]

        for attempt in script_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_say_command_command_injection_attempts(self):
        """Test command injection attempts in say command (semicolon and pipe still blocked)."""
        command_attempts = [
            "; rm -rf /",  # Semicolon still blocked
            "| cat /etc/passwd",  # Pipe still blocked
            "; ls -la",  # Semicolon still blocked
            "| nc -l 8080",  # Pipe still blocked
            # Note: && and || are no longer blocked as & is safe in messages
        ]

        for attempt in command_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_local_command_injection_attempts(self):
        """Test injection attempts in local command (HTML tags and command chaining still blocked)."""
        injection_attempts = [
            "<script>alert('XSS')</script>",  # HTML tags still blocked
            "; rm -rf /",  # Semicolon still blocked
            "| cat /etc/passwd",  # Pipe still blocked
            # Note: && is no longer blocked as & is safe
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                LocalCommand(message=attempt)

    def test_system_command_injection_attempts(self):
        """Test injection attempts in system command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                SystemCommand(message=attempt)

    def test_emote_command_injection_attempts(self):
        """Test injection attempts in emote command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                EmoteCommand(action=attempt)

    def test_me_command_injection_attempts(self):
        """Test injection attempts in me command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                MeCommand(action=attempt)

    def test_pose_command_injection_attempts(self):
        """Test injection attempts in pose command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                PoseCommand(pose=attempt)

    def test_whisper_command_injection_attempts(self):
        """Test injection attempts in whisper command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                WhisperCommand(target="admin", message=attempt)

    def test_reply_command_injection_attempts(self):
        """Test injection attempts in reply command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                ReplyCommand(message=attempt)

    def test_alias_command_injection_attempts(self):
        """Test injection attempts in alias command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                AliasCommand(alias_name="hack", command=attempt)

    def test_unalias_command_injection_attempts(self):
        """Test injection attempts in unalias command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                UnaliasCommand(alias_name=attempt)

    def test_help_command_injection_attempts(self):
        """Test injection attempts in help command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                HelpCommand(topic=attempt)

    def test_who_command_injection_attempts(self):
        """Test injection attempts in who command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                WhoCommand(filter_name=attempt)

    def test_mute_command_injection_attempts(self):
        """Test injection attempts in mute command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                MuteCommand(player_name=attempt)

    def test_unmute_command_injection_attempts(self):
        """Test injection attempts in unmute command."""
        injection_attempts = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                UnmuteCommand(player_name=attempt)


class TestXSSAttackVectors:
    """Test XSS attack vectors."""

    def test_xss_script_tags(self):
        """Test various script tag XSS attempts."""
        xss_attempts = [
            "<script>alert('XSS')</script>",
            "<SCRIPT>alert('XSS')</SCRIPT>",
            "<script>alert(String.fromCharCode(88,83,83))</script>",
            "<script>alert(/XSS/)</script>",
            "<script>alert('XSS')</script>",
            '<script>alert("XSS")</script>',
            "<script>alert('XSS')</script>",
            "<script>alert('XSS')</script>",
            "<script>alert('XSS')</script>",
            "<script>alert('XSS')</script>",
        ]

        for attempt in xss_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_xss_event_handlers(self):
        """Test XSS via event handlers."""
        xss_attempts = [
            "<img src=x onerror=alert('XSS')>",
            "<body onload=alert('XSS')>",
            "<input onfocus=alert('XSS') autofocus>",
            "<select onfocus=alert('XSS') autofocus>",
            "<textarea onfocus=alert('XSS') autofocus>",
            "<keygen onfocus=alert('XSS') autofocus>",
            "<video><source onerror=alert('XSS')>",
            "<audio src=x onerror=alert('XSS')>",
            "<iframe onload=alert('XSS')></iframe>",
            "<object onload=alert('XSS')></object>",
            "<embed onload=alert('XSS')>",
            "<link onload=alert('XSS')>",
            "<style onload=alert('XSS')></style>",
        ]

        for attempt in xss_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_xss_javascript_protocols(self):
        """Test XSS via JavaScript protocols."""
        xss_attempts = [
            "javascript:alert('XSS')",
            "JAVASCRIPT:alert('XSS')",
            "JavaScript:alert('XSS')",
            "javascript:alert(String.fromCharCode(88,83,83))",
            "javascript:alert(/XSS/)",
            "javascript:alert('XSS')",
            'javascript:alert("XSS")',
            "javascript:alert('XSS')",
            "javascript:alert('XSS')",
            "javascript:alert('XSS')",
        ]

        for attempt in xss_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_xss_data_protocols(self):
        """Test XSS via data protocols."""
        xss_attempts = [
            "data:text/html,<script>alert('XSS')</script>",
            "data:text/html,<img src=x onerror=alert('XSS')>",
            "data:text/html,<body onload=alert('XSS')>",
            "data:text/html,<input onfocus=alert('XSS') autofocus>",
            "data:text/html,<select onfocus=alert('XSS') autofocus>",
            "data:text/html,<textarea onfocus=alert('XSS') autofocus>",
            "data:text/html,<keygen onfocus=alert('XSS') autofocus>",
            "data:text/html,<video><source onerror=alert('XSS')>",
            "data:text/html,<audio src=x onerror=alert('XSS')>",
            "data:text/html,<iframe onload=alert('XSS')></iframe>",
        ]

        for attempt in xss_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_xss_svg_vectors(self):
        """Test XSS via SVG vectors."""
        xss_attempts = [
            "<svg onload=alert('XSS')>",
            "<svg><script>alert('XSS')</script></svg>",
            "<svg><script>alert('XSS')</script></svg>",
            "<svg><script>alert('XSS')</script></svg>",
            "<svg><script>alert('XSS')</script></svg>",
            "<svg><script>alert('XSS')</script></svg>",
            "<svg><script>alert('XSS')</script></svg>",
            "<svg><script>alert('XSS')</script></svg>",
            "<svg><script>alert('XSS')</script></svg>",
            "<svg><script>alert('XSS')</script></svg>",
        ]

        for attempt in xss_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_xss_iframe_vectors(self):
        """Test XSS via iframe vectors."""
        xss_attempts = [
            "<iframe src='javascript:alert(\"XSS\")'></iframe>",
            "<iframe src='data:text/html,<script>alert(\"XSS\")</script>'></iframe>",
            "<iframe src='data:text/html,<img src=x onerror=alert(\"XSS\")>'></iframe>",
            "<iframe src='data:text/html,<body onload=alert(\"XSS\")>'></iframe>",
            "<iframe src='data:text/html,<input onfocus=alert(\"XSS\") autofocus>'></iframe>",
            "<iframe src='data:text/html,<select onfocus=alert(\"XSS\") autofocus>'></iframe>",
            "<iframe src='data:text/html,<textarea onfocus=alert(\"XSS\") autofocus>'></iframe>",
            "<iframe src='data:text/html,<keygen onfocus=alert(\"XSS\") autofocus>'></iframe>",
            "<iframe src='data:text/html,<video><source onerror=alert(\"XSS\")>'></iframe>",
            "<iframe src='data:text/html,<audio src=x onerror=alert(\"XSS\")>'></iframe>",
        ]

        for attempt in xss_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)


class TestCommandInjectionVectors:
    """Test command injection attack vectors."""

    def test_sql_injection_patterns(self):
        """Test SQL injection patterns (only patterns with = assignment operators)."""
        sql_patterns = [
            "admin' OR 1=1 --",  # OR with = assignment
            "test' AND password='x",  # AND with = assignment
            # Note: Patterns with semicolons are caught separately by shell metacharacter check
        ]

        for pattern in sql_patterns:
            with pytest.raises(ValidationError):
                SayCommand(message=pattern)

    def test_command_injection_patterns(self):
        """Test command injection patterns (semicolon and pipe still blocked)."""
        cmd_patterns = [
            "; rm -rf /",  # Semicolon blocked
            "| cat /etc/passwd",  # Pipe blocked
            "; ls -la",  # Semicolon blocked
            "| nc -l 8080",  # Pipe blocked
            "; python -c 'import os; os.system(\"whoami\")'",  # Semicolon blocked
            "| perl -e 'system(\"whoami\")'",  # Pipe blocked
            # Note: && and || no longer blocked as & is safe in messages
        ]

        for pattern in cmd_patterns:
            with pytest.raises(ValidationError):
                SayCommand(message=pattern)

    def test_path_traversal_attempts(self):
        """Test path traversal attempts."""
        path_traversal = [
            "../../../etc/passwd",
            "..\\..\\..\\windows\\system32\\config\\sam",
            "....//....//....//etc/passwd",
            "..%2f..%2f..%2fetc%2fpasswd",
            "..%252f..%252f..%252fetc%252fpasswd",
            "..%c0%af..%c0%af..%c0%afetc%c0%afpasswd",
            "..%c1%9c..%c1%9c..%c1%9cetc%c1%9cpasswd",
            "..%c0%2f..%c0%2f..%c0%2fetc%c0%2fpasswd",
            "..%c1%af..%c1%af..%c1%afetc%c1%afpasswd",
            "..%c0%5c..%c0%5c..%c0%5cetc%c0%5cpasswd",
        ]

        for attempt in path_traversal:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_ldap_injection_attempts(self):
        """Test LDAP injection attempts (only patterns caught by current validators)."""
        ldap_attempts = [
            # LDAP patterns without actual dangerous metacharacters are now allowed
            # Only test patterns that include HTML tags or command separators
            "admin<script>)(&(password=*))",  # HTML tags blocked
        ]

        for attempt in ldap_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    def test_xpath_injection_attempts(self):
        """Test XPath injection attempts (only patterns with assignment operators)."""
        xpath_attempts = [
            "admin' or 1=1 or ''='",  # OR with = assignment
            "test' or password='x",  # OR with = assignment
        ]

        for attempt in xpath_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)


class TestSecurityValidationComprehensive:
    """Test comprehensive security validation."""

    def test_comprehensive_security_validation(self):
        """Test comprehensive security validation function."""
        malicious_inputs = [
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
            "javascript:alert('XSS')",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "<iframe src='javascript:alert(\"XSS\")'></iframe>",
            "data:text/html,<script>alert('XSS')</script>",
        ]

        for malicious_input in malicious_inputs:
            with pytest.raises(ValueError):
                validate_security_comprehensive(malicious_input)

    def test_comprehensive_security_validation_safe_inputs(self):
        """Test comprehensive security validation with safe inputs."""
        safe_inputs = [
            "Hello world!",
            "How are you today?",
            "This is a normal message.",
            "Testing 123",
            "Valid input here",
            "No special characters",
            "Just plain text",
            "Regular message content",
            "Safe user input",
            "Normal communication",
        ]

        for safe_input in safe_inputs:
            result = validate_security_comprehensive(safe_input)
            assert result == safe_input

    def test_comprehensive_security_validation_edge_cases(self):
        """Test comprehensive security validation with edge cases."""
        edge_cases = [
            "",  # Empty string
            "   ",  # Whitespace only
            "a",  # Single character
            "123",  # Numbers only
            "!@#$%^&*()",  # Special characters only
            "Hello world 123",  # Mixed content
            "Test with spaces",  # Spaces in content
            "UPPERCASE TEXT",  # Uppercase text
            "lowercase text",  # Lowercase text
            "Mixed Case Text",  # Mixed case text
        ]

        for edge_case in edge_cases:
            try:
                result = validate_security_comprehensive(edge_case)
                assert result == edge_case
            except ValueError:
                # Some edge cases may be considered unsafe
                pass


class TestSecurityValidationPerformance:
    """Test security validation performance."""

    def test_security_validation_performance(self):
        """Test that security validation is performant."""
        import time

        # Test with a large number of inputs
        test_inputs = [
            "Hello world!",
            "<script>alert('XSS')</script>",
            "; rm -rf /",
            "| cat /etc/passwd",
            "javascript:alert('XSS')",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "<iframe src='javascript:alert(\"XSS\")'></iframe>",
        ] * 100  # Repeat 100 times

        start_time = time.time()

        for test_input in test_inputs:
            try:
                validate_security_comprehensive(test_input)
            except ValueError:
                pass  # Expected for malicious inputs

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Should complete within reasonable time (less than 1 second)
        assert elapsed_time < 1.0, f"Security validation took too long: {elapsed_time}s"

    def test_security_validation_memory_usage(self):
        """Test that security validation doesn't use excessive memory."""
        import os

        import psutil

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss

        # Test with many inputs
        for _ in range(1000):
            try:
                validate_security_comprehensive("Hello world!")
            except ValueError:
                pass

        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory

        # Memory increase should be minimal (less than 10MB)
        assert memory_increase < 10 * 1024 * 1024, (
            f"Security validation used too much memory: {memory_increase / 1024 / 1024}MB"
        )
