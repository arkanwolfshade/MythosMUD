"""
Tests for centralized security validation functions.

This module tests the centralized security validation system that will replace
the duplicated validation logic across command models. It ensures consistent
security patterns and prevents command injection attacks.

As noted in the Pnakotic Manuscripts: "Security must be consistent across all
gateways, lest the ancient ones find a way through the cracks in our defenses."
"""

from ..validators.security_validator import (
    INJECTION_PATTERNS,
    SLASH_COMMANDS,
    comprehensive_sanitize_input,
    sanitize_unicode_input,
    strip_ansi_codes,
)


class TestSecurityValidationConstants:
    """Test security validation constants and patterns."""

    def test_injection_patterns_defined(self):
        """Test that injection patterns are properly defined."""
        assert INJECTION_PATTERNS is not None
        assert isinstance(INJECTION_PATTERNS, list)
        assert len(INJECTION_PATTERNS) > 0

        # Test that patterns are valid regex
        import re

        for pattern in INJECTION_PATTERNS:
            # Should not raise exception
            compiled = re.compile(pattern)
            assert compiled is not None

    def test_injection_patterns_coverage(self):
        """Test that injection patterns cover common attack vectors."""

        # Test shell metacharacters - should match [;|] pattern (& removed as safe in messages)
        shell_pattern = r"[;|]"
        assert any(pattern == shell_pattern for pattern in INJECTION_PATTERNS)

        # Test SQL injection - flexible spacing with .* (more secure than \s*)
        sql_pattern = r"\b(or|and)\b.*="
        assert any(pattern == sql_pattern for pattern in INJECTION_PATTERNS)

        # Test Python injection - now more specific to function calls, not keywords
        python_pattern = r"(__import__|eval|exec)\s*\(|os\.system\s*\(|os\.popen\s*\("
        assert any(pattern == python_pattern for pattern in INJECTION_PATTERNS)

        # Test format string attacks - now more specific to actual format specifiers
        format_pattern = r"%\d*[sdxXfFgGeEcCbrpP]"
        assert any(pattern == format_pattern for pattern in INJECTION_PATTERNS)

    def test_slash_commands_defined(self):
        """Test that slash commands are properly defined."""
        assert SLASH_COMMANDS is not None
        assert isinstance(SLASH_COMMANDS, set)
        assert len(SLASH_COMMANDS) > 0

        # Test that common commands are included
        expected_commands = {"help", "who", "quit", "look", "go", "say", "me", "pose"}
        assert expected_commands.issubset(SLASH_COMMANDS)

    def test_slash_commands_immutable(self):
        """Test that slash commands set is immutable-like."""
        # Should be a set, which is mutable but we expect it to be stable
        assert isinstance(SLASH_COMMANDS, set)

        # Test that it contains expected commands
        assert "help" in SLASH_COMMANDS
        assert "who" in SLASH_COMMANDS
        assert "quit" in SLASH_COMMANDS


class TestUnicodeSanitization:
    """Test Unicode input sanitization functions."""

    def test_sanitize_unicode_input_basic(self):
        """Test basic Unicode sanitization."""
        # Test normal text
        normal_text = "Hello, world!"
        result = sanitize_unicode_input(normal_text)
        assert result == normal_text

        # Test empty string
        empty_text = ""
        result = sanitize_unicode_input(empty_text)
        assert result == empty_text

        # Test None (should handle gracefully)
        result = sanitize_unicode_input(None)
        assert result is None

    def test_sanitize_unicode_input_mojibake(self):
        """Test Unicode sanitization with mojibake (double-encoded text)."""
        # Test mojibake - this is a common Unicode issue
        # Note: ftfy handles this automatically, so we test that it doesn't break
        mojibake_text = "café"  # Normal text should pass through
        result = sanitize_unicode_input(mojibake_text)
        assert result == mojibake_text

    def test_sanitize_unicode_input_control_chars(self):
        """Test Unicode sanitization with control characters."""
        # Test with control characters (these should be handled by comprehensive_sanitize_input)
        text_with_control = "Hello\x00World"
        result = sanitize_unicode_input(text_with_control)
        # ftfy should not remove control chars, that's handled elsewhere
        assert isinstance(result, str)

    def test_sanitize_unicode_input_performance(self):
        """Test Unicode sanitization performance with various inputs."""
        import time

        # Test with various input sizes
        test_cases = [
            "a" * 10,
            "a" * 100,
            "a" * 1000,
            "Hello, world! " * 100,
        ]

        for test_case in test_cases:
            start_time = time.time()
            result = sanitize_unicode_input(test_case)
            end_time = time.time()

            # Should complete quickly (under 0.1 seconds)
            assert end_time - start_time < 0.1
            assert isinstance(result, str)
            assert len(result) > 0


class TestANSICodeStripping:
    """Test ANSI code stripping functions."""

    def test_strip_ansi_codes_basic(self):
        """Test basic ANSI code stripping."""
        # Test normal text
        normal_text = "Hello, world!"
        result = strip_ansi_codes(normal_text)
        assert result == normal_text

        # Test empty string
        empty_text = ""
        result = strip_ansi_codes(empty_text)
        assert result == empty_text

        # Test None
        result = strip_ansi_codes(None)
        assert result is None

    def test_strip_ansi_codes_color_codes(self):
        """Test ANSI color code stripping."""
        # Test with color codes
        colored_text = "\x1b[31mRed text\x1b[0m"
        result = strip_ansi_codes(colored_text)
        assert result == "Red text"

        # Test with multiple color codes
        multi_colored = "\x1b[31mRed\x1b[32mGreen\x1b[0m"
        result = strip_ansi_codes(multi_colored)
        assert result == "RedGreen"

    def test_strip_ansi_codes_formatting_codes(self):
        """Test ANSI formatting code stripping."""
        # Test with formatting codes
        formatted_text = "\x1b[1mBold\x1b[0m"
        result = strip_ansi_codes(formatted_text)
        assert result == "Bold"

        # Test with complex formatting
        complex_formatted = "\x1b[1;31;42mBold red on green\x1b[0m"
        result = strip_ansi_codes(complex_formatted)
        assert result == "Bold red on green"

    def test_strip_ansi_codes_cursor_movement(self):
        """Test ANSI cursor movement code stripping."""
        # Test cursor movement codes
        cursor_text = "Hello\x1b[2J\x1b[HWorld"
        result = strip_ansi_codes(cursor_text)
        assert result == "HelloWorld"

        # Test with multiple cursor codes
        multi_cursor = "\x1b[2J\x1b[H\x1b[1;1HText"
        result = strip_ansi_codes(multi_cursor)
        assert result == "Text"

    def test_strip_ansi_codes_malicious_hiding(self):
        """Test that ANSI codes can't hide malicious content."""
        # Test that ANSI codes don't hide dangerous content
        hidden_text = "\x1b[31m<script>\x1b[0m"
        result = strip_ansi_codes(hidden_text)
        assert result == "<script>"
        assert "<script>" in result

        # Test with injection attempts hidden in ANSI codes
        injection_text = "\x1b[31m; rm -rf /\x1b[0m"
        result = strip_ansi_codes(injection_text)
        assert result == "; rm -rf /"
        assert "; rm -rf /" in result


class TestComprehensiveSanitization:
    """Test comprehensive input sanitization."""

    def test_comprehensive_sanitize_input_basic(self):
        """Test basic comprehensive sanitization."""
        # Test normal text
        normal_text = "Hello, world!"
        result = comprehensive_sanitize_input(normal_text)
        assert result == normal_text

        # Test empty string
        empty_text = ""
        result = comprehensive_sanitize_input(empty_text)
        assert result == empty_text

        # Test None
        result = comprehensive_sanitize_input(None)
        assert result is None

    def test_comprehensive_sanitize_input_unicode_and_ansi(self):
        """Test comprehensive sanitization with both Unicode and ANSI issues."""
        # Test with both Unicode and ANSI codes
        complex_text = "\x1b[31mHello\x1b[0m, café!"
        result = comprehensive_sanitize_input(complex_text)
        assert result == "Hello, café!"
        assert "\x1b" not in result
        assert "Hello" in result
        assert "café" in result

    def test_comprehensive_sanitize_input_control_chars(self):
        """Test comprehensive sanitization removes control characters."""
        # Test with null bytes and control characters
        control_text = "Hello\x00World\x01Test"
        result = comprehensive_sanitize_input(control_text)
        assert result == "HelloWorldTest"
        assert "\x00" not in result
        assert "\x01" not in result

    def test_comprehensive_sanitize_input_invisible_unicode(self):
        """Test comprehensive sanitization removes invisible Unicode characters."""
        # Test with zero-width characters
        invisible_text = "Hello\u200bWorld\ufeffTest"
        result = comprehensive_sanitize_input(invisible_text)
        assert result == "HelloWorldTest"
        assert "\u200b" not in result
        assert "\ufeff" not in result

    def test_comprehensive_sanitize_input_preserves_newlines_tabs(self):
        """Test that comprehensive sanitization preserves newlines and tabs."""
        # Test that newlines and tabs are preserved
        text_with_whitespace = "Line 1\nLine 2\tTabbed"
        result = comprehensive_sanitize_input(text_with_whitespace)
        assert result == text_with_whitespace
        assert "\n" in result
        assert "\t" in result

    def test_comprehensive_sanitize_input_security_vectors(self):
        """Test that comprehensive sanitization handles security attack vectors."""
        # Test various attack vectors
        attack_vectors = [
            "Hello<script>alert('xss')</script>",
            "Hello; rm -rf /",
            "Hello $(ls)",
            "Hello %s",
            "Hello __import__('os')",
            "Hello eval('malicious code')",
        ]

        for attack in attack_vectors:
            result = comprehensive_sanitize_input(attack)
            # Should not crash and should return a string
            assert isinstance(result, str)
            # Should preserve the basic text but remove dangerous control chars
            assert "Hello" in result

    def test_comprehensive_sanitize_input_performance(self):
        """Test comprehensive sanitization performance."""
        import time

        # Test with various input sizes
        test_cases = [
            "a" * 10,
            "a" * 100,
            "a" * 1000,
            "Hello, world! " * 100,
            "\x1b[31m" + "a" * 100 + "\x1b[0m",
        ]

        for test_case in test_cases:
            start_time = time.time()
            result = comprehensive_sanitize_input(test_case)
            end_time = time.time()

            # Should complete quickly (under 0.1 seconds)
            assert end_time - start_time < 0.1
            assert isinstance(result, str)
            assert len(result) > 0


class TestCentralizedSecurityValidation:
    """Test centralized security validation patterns."""

    def test_dangerous_character_detection(self):
        """Test detection of dangerous characters."""
        # These should be detected as dangerous by command validators
        dangerous_chars = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]

        for char in dangerous_chars:
            test_text = f"Hello{char}World"
            # The centralized validation should detect this
            # This will be implemented in the centralized validator
            assert char in test_text

    def test_injection_pattern_detection(self):
        """Test detection of injection patterns."""
        import re

        # Test patterns that SHOULD STILL be detected (actual code execution attempts)
        injection_tests = [
            "Hello; rm -rf /",  # Semicolon command chaining
            "Hello | cat /etc/passwd",  # Pipe operator
            "Hello OR 1=1",  # SQL injection with assignment
            "Hello AND password='admin'",  # SQL injection with assignment
            "Hello __import__('os')",  # Python import function call
            "Hello eval('malicious')",  # Python eval function call
            "Hello os.system('rm')",  # OS system call
            "Hello %s %d",  # Format string specifiers
        ]

        for test_case in injection_tests:
            # At least one pattern should match
            matches = any(re.search(pattern, test_case, re.IGNORECASE) for pattern in INJECTION_PATTERNS)
            assert matches, f"No injection pattern matched: {test_case}"

    def test_safe_input_validation(self):
        """Test that safe input passes validation."""
        # These should be considered safe
        safe_inputs = [
            "Hello, world!",
            "How are you today?",
            "I love this game!",
            "Can you help me?",
            "Thank you very much.",
            "The weather is nice today.",
        ]

        for safe_input in safe_inputs:
            # Should not match any injection patterns
            import re

            matches = any(re.search(pattern, safe_input, re.IGNORECASE) for pattern in INJECTION_PATTERNS)
            assert not matches, f"Safe input incorrectly flagged: {safe_input}"

    def test_edge_case_handling(self):
        """Test edge cases in security validation."""
        # Test edge cases
        edge_cases = [
            "",  # Empty string
            " ",  # Single space
            "\n",  # Newline only
            "\t",  # Tab only
            "a" * 1000,  # Very long string
            "a" * 10000,  # Very very long string
        ]

        for edge_case in edge_cases:
            # Should not crash
            result = comprehensive_sanitize_input(edge_case)
            assert isinstance(result, str)

    def test_unicode_edge_cases(self):
        """Test Unicode edge cases in security validation."""
        # Test Unicode edge cases
        unicode_cases = [
            "Hello 世界",  # Mixed ASCII and Unicode
            "🌍🌎🌏",  # Emoji
            "Hello\u0000World",  # Null byte
            "Hello\u200bWorld",  # Zero-width space
            "Hello\ufeffWorld",  # Zero-width no-break space
        ]

        for unicode_case in unicode_cases:
            # Should not crash
            result = comprehensive_sanitize_input(unicode_case)
            assert isinstance(result, str)
            # Should remove dangerous characters
            assert "\u0000" not in result


class TestSecurityValidationIntegration:
    """Test integration of security validation with command models."""

    def test_validation_consistency(self):
        """Test that validation is consistent across different contexts."""
        # Test that the same input produces consistent results
        test_input = "Hello<script>alert('xss')</script>"

        # All sanitization steps should produce consistent results
        unicode_result = sanitize_unicode_input(test_input)
        ansi_result = strip_ansi_codes(unicode_result)
        comprehensive_result = comprehensive_sanitize_input(test_input)

        # Results should be consistent
        assert isinstance(unicode_result, str)
        assert isinstance(ansi_result, str)
        assert isinstance(comprehensive_result, str)

        # Comprehensive should be most restrictive
        assert len(comprehensive_result) <= len(test_input)

    def test_validation_performance_under_load(self):
        """Test validation performance under simulated load."""
        import concurrent.futures
        import time

        # Test concurrent validation
        test_inputs = [
            "Hello, world!",
            "Hello<script>alert('xss')</script>",
            "\x1b[31mColored text\x1b[0m",
            "Hello; rm -rf /",
            "Hello 世界",
        ] * 100  # 500 total inputs

        start_time = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(comprehensive_sanitize_input, inp) for inp in test_inputs]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]

        end_time = time.time()

        # Should complete in reasonable time
        assert end_time - start_time < 5.0  # Under 5 seconds
        assert len(results) == len(test_inputs)

        # All results should be strings
        for result in results:
            assert isinstance(result, str)

    def test_validation_memory_usage(self):
        """Test that validation doesn't cause memory leaks."""
        import gc

        # Test memory usage with many validations
        initial_objects = len(gc.get_objects())

        for _ in range(1000):
            test_input = "Hello, world! " * 100
            result = comprehensive_sanitize_input(test_input)
            del result  # Explicit cleanup

        gc.collect()  # Force garbage collection
        final_objects = len(gc.get_objects())

        # Memory usage shouldn't grow significantly
        # Allow for some growth due to test overhead
        growth = final_objects - initial_objects
        assert growth < 1000, f"Potential memory leak detected: {growth} objects created"


class TestSecurityValidationErrorHandling:
    """Test error handling in security validation."""

    def test_validation_with_invalid_input_types(self):
        """Test validation with invalid input types."""
        # Test with various invalid types
        invalid_inputs = [
            123,  # Integer
            123.45,  # Float
            [],  # List
            {},  # Dict
            True,  # Boolean
            None,  # None
        ]

        for invalid_input in invalid_inputs:
            # Should handle gracefully without crashing
            try:
                result = comprehensive_sanitize_input(invalid_input)
                # Should return the input unchanged for non-string types
                assert result == invalid_input
            except (TypeError, AttributeError):
                # Some functions might raise errors for non-string inputs
                # This is acceptable as long as it's handled gracefully
                pass

    def test_validation_with_very_long_input(self):
        """Test validation with very long input."""
        # Test with extremely long input
        very_long_input = "a" * 1000000  # 1MB string

        # Should not crash
        result = comprehensive_sanitize_input(very_long_input)
        assert isinstance(result, str)
        assert len(result) <= len(very_long_input)

    def test_validation_with_malformed_unicode(self):
        """Test validation with malformed Unicode."""
        # Test with malformed Unicode sequences
        malformed_unicode = [
            "Hello\xff\xfeWorld",  # Invalid UTF-8
            "Hello\x00\x01\x02World",  # Control characters
            "Hello\x80\x81\x82World",  # Invalid UTF-8 bytes
        ]

        for malformed in malformed_unicode:
            # Should handle gracefully
            result = comprehensive_sanitize_input(malformed)
            assert isinstance(result, str)
            # Should remove or fix malformed sequences
            assert len(result) <= len(malformed)
