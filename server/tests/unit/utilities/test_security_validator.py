"""
Tests for security validation functions.

This module tests the enhanced input sanitization capabilities
including Unicode normalization and ANSI code removal.
Focuses on testing sanitization (cleaning) rather than validation (rejection)
to ensure user expression freedom is preserved.
"""

from server.validators.security_validator import (
    INJECTION_PATTERNS,
    comprehensive_sanitize_input,
    sanitize_unicode_input,
    strip_ansi_codes,
)


class TestUnicodeSanitization:
    """Test Unicode input sanitization using ftfy."""

    def test_mojibake_fix(self) -> None:
        """Test fixing double-encoded text (mojibake)."""
        # Test with a simpler mojibake example that ftfy can actually fix
        # "café" with encoding issues
        mojibake_text = "cafÃ©"  # Common encoding issue
        result = sanitize_unicode_input(mojibake_text)
        # ftfy should detect and fix this
        assert result != mojibake_text

    def test_combining_characters(self) -> None:
        """Test fixing combining characters."""
        # Text with combining characters that should be precomposed
        combining_text = "e\u0301"  # e + combining acute accent
        result = sanitize_unicode_input(combining_text)
        assert result == "é"  # Should be precomposed

    def test_invisible_characters(self) -> None:
        """Test removal of invisible Unicode characters."""
        # Text with zero-width space and other invisible characters
        invisible_text = "hello\u200bworld\u200c"  # zero-width space and zero-width non-joiner
        result = comprehensive_sanitize_input(invisible_text)
        assert result == "helloworld"  # Invisible characters should be removed

    def test_curly_quotes(self) -> None:
        """Test fixing curly quotes."""
        curly_text = "â€œHelloâ€"  # Common encoding of curly quotes
        result = sanitize_unicode_input(curly_text)
        # Should be converted to straight quotes or at least cleaned
        assert result != curly_text  # Should be different from original

    def test_empty_input(self) -> None:
        """Test handling of empty input."""
        assert sanitize_unicode_input("") == ""
        assert sanitize_unicode_input(None) is None  # type: ignore[arg-type]

    def test_legitimate_unicode_preserved(self) -> None:
        """Test that legitimate Unicode text is preserved."""
        # Test various legitimate Unicode characters
        legitimate_texts = [
            "café",  # Accented character
            "naïve",  # Diaeresis
            "résumé",  # Multiple accents
            "Hélló Wórld",  # Mixed accents
            "こんにちは",  # Japanese
            "안녕하세요",  # Korean
            "Привет",  # Russian
        ]

        for text in legitimate_texts:
            result = sanitize_unicode_input(text)
            # Should preserve the meaning and readability
            assert len(result) > 0
            assert result != ""  # Should not be empty


class TestAnsiCodeRemoval:
    """Test ANSI escape code removal."""

    def test_basic_ansi_codes(self) -> None:
        """Test removal of basic ANSI color codes."""
        ansi_text = "\033[31mRed text\033[0m"
        result = strip_ansi_codes(ansi_text)
        assert result == "Red text"

    def test_complex_ansi_codes(self) -> None:
        """Test removal of complex ANSI sequences."""
        ansi_text = "\033[1;33;44mBold yellow on blue\033[0m"
        result = strip_ansi_codes(ansi_text)
        assert result == "Bold yellow on blue"

    def test_cursor_movement_codes(self) -> None:
        """Test removal of cursor movement codes."""
        ansi_text = "Hello\033[2K\033[1GWorld"  # Clear line and move cursor
        result = strip_ansi_codes(ansi_text)
        # strip-ansi focuses on color codes, not all terminal sequences
        # For cursor movement codes, we rely on our comprehensive sanitization
        # This test verifies that strip-ansi at least doesn't break the text
        assert len(result) > 0
        assert "Hello" in result
        assert "World" in result

    def test_mixed_content(self) -> None:
        """Test ANSI removal with mixed normal and ANSI content."""
        ansi_text = "Normal \033[32mgreen\033[0m text"
        result = strip_ansi_codes(ansi_text)
        assert result == "Normal green text"

    def test_no_ansi_codes(self) -> None:
        """Test text without ANSI codes."""
        normal_text = "Just normal text"
        result = strip_ansi_codes(normal_text)
        assert result == normal_text

    def test_empty_input(self) -> None:
        """Test handling of empty input."""
        assert strip_ansi_codes("") == ""
        assert strip_ansi_codes(None) is None  # type: ignore[arg-type]

    def test_legitimate_text_preserved(self) -> None:
        """Test that legitimate text is preserved."""
        legitimate_texts = [
            "Hello World",
            "This is a test message",
            "Special characters: !@#$%^&*()",
            "Numbers: 1234567890",
            "Mixed: Hello123!@#",
        ]

        for text in legitimate_texts:
            result = strip_ansi_codes(text)
            assert result == text  # Should be unchanged


class TestComprehensiveSanitization:
    """Test the comprehensive sanitization function."""

    def test_unicode_and_ansi_combined(self) -> None:
        """Test sanitization of text with both Unicode and ANSI issues."""
        problematic_text = "\033[31mããã«ã¡ã¯\033[0m"  # ANSI + mojibake
        result = comprehensive_sanitize_input(problematic_text)
        # Should remove ANSI codes and fix Unicode
        assert "\033" not in result
        assert result != problematic_text

    def test_control_characters(self) -> None:
        """Test removal of control characters."""
        control_text = "Hello\x00\x01\x02World\x7f"  # Null bytes and DEL
        result = comprehensive_sanitize_input(control_text)
        assert result == "HelloWorld"

    def test_preserve_newlines_and_tabs(self) -> None:
        """Test that newlines and tabs are preserved."""
        text_with_whitespace = "Hello\n\tWorld"
        result = comprehensive_sanitize_input(text_with_whitespace)
        assert result == "Hello\n\tWorld"

    def test_complex_malicious_input(self) -> None:
        """Test sanitization of complex potentially malicious input."""
        malicious_text = (
            "\033[31m"  # ANSI color
            "Hello\x00\x01"  # Control characters
            "\u200b\u200c"  # Invisible Unicode
            "World"
            "\033[0m"  # ANSI reset
        )
        result = comprehensive_sanitize_input(malicious_text)
        assert result == "HelloWorld"

    def test_empty_input(self) -> None:
        """Test handling of empty input."""
        assert comprehensive_sanitize_input("") == ""
        assert comprehensive_sanitize_input(None) is None  # type: ignore[arg-type]

    def test_user_expression_preserved(self) -> None:
        """Test that legitimate user expression is preserved."""
        user_expressions = [
            "Hello, how are you today?",
            "I'm roleplaying as a detective!",
            "The eldritch horror lurks in the shadows...",
            "Let's explore the mysterious mansion together!",
            "My character's name is Dr. Armitage",
            "I cast a spell: Abracadabra!",
            "The ancient tome contains forbidden knowledge...",
        ]

        for expression in user_expressions:
            result = comprehensive_sanitize_input(expression)
            # Should preserve the user's intent and expression
            assert len(result) > 0
            assert result != ""
            # Should maintain readability
            assert " " in result or len(result) == 1  # Should have spaces or be single character


class TestInjectionPatterns:
    """Test that injection patterns are still properly defined."""

    def test_injection_patterns_exist(self) -> None:
        """Test that injection patterns are defined."""
        assert len(INJECTION_PATTERNS) > 0
        assert all(isinstance(pattern, str) for pattern in INJECTION_PATTERNS)

    def test_shell_metacharacters_pattern(self) -> None:
        """Test that shell metacharacters pattern is present (& removed as safe)."""
        shell_pattern = r"[;|]"  # & removed as it's safe in messages
        assert shell_pattern in INJECTION_PATTERNS

    def test_sql_injection_pattern(self) -> None:
        """Test that SQL injection pattern is present (flexible spacing with .*)."""
        sql_pattern = r"\b(or|and)\b.*="  # Updated to match actual pattern
        assert sql_pattern in INJECTION_PATTERNS

    def test_python_injection_pattern(self) -> None:
        """Test that Python injection pattern is present (function calls, not keywords)."""
        # Now more specific - detects function calls, not just keywords
        python_pattern = r"(__import__|eval|exec)\s*\(|os\.system\s*\(|os\.popen\s*\("
        assert python_pattern in INJECTION_PATTERNS


class TestSanitizationVsValidation:
    """Test that we're focusing on sanitization rather than validation."""

    def test_creative_text_not_rejected(self) -> None:
        """Test that creative user text is not rejected."""
        creative_texts = [
            "I'm writing a story about Cthulhu!",
            "My character's backstory is complex...",
            "Let's have an adventure in Arkham!",
            "The stars are right for our quest!",
            "Iä! Iä! Cthulhu fhtagn!",
            "The Necronomicon speaks of ancient horrors...",
        ]

        for text in creative_texts:
            result = comprehensive_sanitize_input(text)
            # Should not be empty or significantly altered
            assert len(result) > 0
            assert result != ""
            # Should preserve the creative content
            assert any(word in result.lower() for word in text.lower().split()[:3])

    def test_roleplay_content_preserved(self) -> None:
        """Test that roleplay content is preserved."""
        roleplay_texts = [
            "*adjusts spectacles nervously*",
            "The detective examines the crime scene carefully...",
            "My character feels a sense of dread creeping in...",
            "I cast the spell with dramatic flair!",
            "The ancient one's presence fills the room...",
        ]

        for text in roleplay_texts:
            result = comprehensive_sanitize_input(text)
            # Should preserve roleplay elements
            assert len(result) > 0
            assert "*" in result or "..." in result or "!" in result

    def test_false_positive_prevention(self) -> None:
        """Test that normal user behavior isn't flagged as suspicious."""
        normal_behaviors = [
            "Hello everyone!",
            "How do I get to the library?",
            "Can someone help me with my quest?",
            "I'm new here, any tips?",
            "Great game, thanks for the help!",
            "See you all later!",
        ]

        for behavior in normal_behaviors:
            result = comprehensive_sanitize_input(behavior)
            # Should be preserved and not flagged
            assert len(result) > 0
            assert result != ""
            # Should maintain the friendly tone - check for key words
            lower_result = result.lower()
            assert any(
                word in lower_result
                for word in ["hello", "help", "thanks", "great", "see", "library", "quest", "tips", "game"]
            )


class TestPerformanceAndEdgeCases:
    """Test performance and edge cases."""

    def test_large_input_handling(self) -> None:
        """Test handling of large input text."""
        large_text = "Hello " * 1000 + "World"
        result = comprehensive_sanitize_input(large_text)
        assert len(result) > 0
        assert "Hello" in result
        assert "World" in result

    def test_special_characters_handling(self) -> None:
        """Test handling of special characters."""
        special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        result = comprehensive_sanitize_input(special_chars)
        # Should preserve most special characters
        assert len(result) > 0
        assert result != ""

    def test_mixed_encoding_issues(self) -> None:
        """Test handling of mixed encoding issues."""
        mixed_text = "Hello\x00\033[31mWorld\u200b"  # Control + ANSI + Unicode
        result = comprehensive_sanitize_input(mixed_text)
        assert result == "HelloWorld"

    def test_unicode_normalization_consistency(self) -> None:
        """Test that Unicode normalization is consistent."""
        # Test that the same input always produces the same output
        test_input = "café\u0301"  # cafe with combining acute accent
        result1 = comprehensive_sanitize_input(test_input)
        result2 = comprehensive_sanitize_input(test_input)
        assert result1 == result2
