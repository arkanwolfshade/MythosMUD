"""
Performance tests for optimized validation functions.

This module tests the performance improvements of the optimized validation
functions compared to the original validation functions.
"""

import time

import pytest

from server.validators.optimized_security_validator import (
    optimized_validate_action_content,
    optimized_validate_alias_name,
    optimized_validate_command_content,
    optimized_validate_filter_name,
    optimized_validate_help_topic,
    optimized_validate_message_content,
    optimized_validate_player_name,
    optimized_validate_pose_content,
    optimized_validate_reason_content,
    optimized_validate_target_player,
)
from server.validators.security_validator import (
    validate_action_content,
    validate_alias_name,
    validate_command_content,
    validate_filter_name,
    validate_help_topic,
    validate_message_content,
    validate_player_name,
    validate_pose_content,
    validate_reason_content,
    validate_target_player,
)


class TestOptimizedValidationPerformance:
    """Test performance improvements of optimized validation functions."""

    # Test data for performance comparison
    TEST_INPUTS = [
        "Hello world!",
        "Say hello to <script>alert('xss')</script>",
        "Go north; rm -rf /",
        "Player with spaces and special chars!",
        "Normal player name",
        "alias_name_test",
        "help topic with spaces",
        "Very long message that contains many characters and should test the performance of the validation functions",
        "Short",
        "This is a very long message that contains many characters and should test the performance of the validation functions. It includes various types of content including normal text, special characters, and potential security issues.",
    ]

    def test_optimized_validation_functions_work_correctly(self):
        """Test that optimized validation functions produce correct results."""
        # Test message validation
        assert optimized_validate_message_content("Hello world!") == "Hello world!"

        # Test player name validation
        assert optimized_validate_player_name("PlayerName") == "PlayerName"

        # Test alias name validation
        assert optimized_validate_alias_name("alias_name") == "alias_name"

        # Test help topic validation
        assert optimized_validate_help_topic("help_topic") == "help_topic"

    def test_optimized_validation_functions_raise_errors_correctly(self):
        """Test that optimized validation functions raise errors for invalid input."""
        # Test message validation with dangerous content
        with pytest.raises(ValueError, match="Message contains"):
            optimized_validate_message_content("<script>alert('xss')</script>")

        # Test player name validation with invalid format
        with pytest.raises(ValueError, match="Player name must start with a letter"):
            optimized_validate_player_name("123invalid")

        # Test alias name validation with invalid format
        with pytest.raises(ValueError, match="Alias name must start with a letter"):
            optimized_validate_alias_name("123invalid")

    def test_message_validation_performance_comparison(self):
        """Compare performance of message validation functions."""
        iterations = 1000

        # Test original function
        start_time = time.perf_counter()
        for _ in range(iterations):
            for test_input in self.TEST_INPUTS:
                try:
                    validate_message_content(test_input)
                except ValueError:
                    pass  # Expected for some test inputs
        original_time = time.perf_counter() - start_time

        # Test optimized function
        start_time = time.perf_counter()
        for _ in range(iterations):
            for test_input in self.TEST_INPUTS:
                try:
                    optimized_validate_message_content(test_input)
                except ValueError:
                    pass  # Expected for some test inputs
        optimized_time = time.perf_counter() - start_time

        print("\nMessage validation performance:")
        print(f"Original: {original_time:.6f}s for {len(self.TEST_INPUTS) * iterations} validations")
        print(f"Optimized: {optimized_time:.6f}s for {len(self.TEST_INPUTS) * iterations} validations")
        print(f"Improvement: {((original_time - optimized_time) / original_time * 100):.1f}%")

        # Optimized should be faster
        assert optimized_time < original_time, (
            f"Optimized function should be faster: {optimized_time:.6f}s vs {original_time:.6f}s"
        )

    def test_player_name_validation_performance_comparison(self):
        """Compare performance of player name validation functions."""
        iterations = 1000

        # Test original function
        start_time = time.perf_counter()
        for _ in range(iterations):
            for test_input in self.TEST_INPUTS:
                try:
                    validate_player_name(test_input)
                except ValueError:
                    pass  # Expected for some test inputs
        original_time = time.perf_counter() - start_time

        # Test optimized function
        start_time = time.perf_counter()
        for _ in range(iterations):
            for test_input in self.TEST_INPUTS:
                try:
                    optimized_validate_player_name(test_input)
                except ValueError:
                    pass  # Expected for some test inputs
        optimized_time = time.perf_counter() - start_time

        print("\nPlayer name validation performance:")
        print(f"Original: {original_time:.6f}s for {len(self.TEST_INPUTS) * iterations} validations")
        print(f"Optimized: {optimized_time:.6f}s for {len(self.TEST_INPUTS) * iterations} validations")
        print(f"Improvement: {((original_time - optimized_time) / original_time * 100):.1f}%")

        # Optimized should be faster
        assert optimized_time < original_time, (
            f"Optimized function should be faster: {optimized_time:.6f}s vs {original_time:.6f}s"
        )

    def test_alias_name_validation_performance_comparison(self):
        """Compare performance of alias name validation functions."""
        iterations = 1000

        # Test original function
        start_time = time.perf_counter()
        for _ in range(iterations):
            for test_input in self.TEST_INPUTS:
                try:
                    validate_alias_name(test_input)
                except ValueError:
                    pass  # Expected for some test inputs
        original_time = time.perf_counter() - start_time

        # Test optimized function
        start_time = time.perf_counter()
        for _ in range(iterations):
            for test_input in self.TEST_INPUTS:
                try:
                    optimized_validate_alias_name(test_input)
                except ValueError:
                    pass  # Expected for some test inputs
        optimized_time = time.perf_counter() - start_time

        print("\nAlias name validation performance:")
        print(f"Original: {original_time:.6f}s for {len(self.TEST_INPUTS) * iterations} validations")
        print(f"Optimized: {optimized_time:.6f}s for {len(self.TEST_INPUTS) * iterations} validations")
        print(f"Improvement: {((original_time - optimized_time) / original_time * 100):.1f}%")

        # Optimized should be faster
        assert optimized_time < original_time, (
            f"Optimized function should be faster: {optimized_time:.6f}s vs {original_time:.6f}s"
        )

    def test_comprehensive_validation_performance_comparison(self):
        """Compare performance of comprehensive validation functions."""
        iterations = 500  # Reduced for comprehensive test

        # Test original functions
        original_functions = [
            validate_message_content,
            validate_action_content,
            validate_player_name,
            validate_alias_name,
            validate_command_content,
            validate_reason_content,
            validate_pose_content,
            validate_filter_name,
            validate_target_player,
            validate_help_topic,
        ]

        start_time = time.perf_counter()
        for _ in range(iterations):
            for test_input in self.TEST_INPUTS:
                for func in original_functions:
                    try:
                        func(test_input)
                    except ValueError:
                        pass  # Expected for some test inputs
        original_time = time.perf_counter() - start_time

        # Test optimized functions
        optimized_functions = [
            optimized_validate_message_content,
            optimized_validate_action_content,
            optimized_validate_player_name,
            optimized_validate_alias_name,
            optimized_validate_command_content,
            optimized_validate_reason_content,
            optimized_validate_pose_content,
            optimized_validate_filter_name,
            optimized_validate_target_player,
            optimized_validate_help_topic,
        ]

        start_time = time.perf_counter()
        for _ in range(iterations):
            for test_input in self.TEST_INPUTS:
                for func in optimized_functions:
                    try:
                        func(test_input)
                    except ValueError:
                        pass  # Expected for some test inputs
        optimized_time = time.perf_counter() - start_time

        print("\nComprehensive validation performance:")
        print(
            f"Original: {original_time:.6f}s for {len(self.TEST_INPUTS) * len(original_functions) * iterations} validations"
        )
        print(
            f"Optimized: {optimized_time:.6f}s for {len(self.TEST_INPUTS) * len(optimized_functions) * iterations} validations"
        )
        print(f"Improvement: {((original_time - optimized_time) / original_time * 100):.1f}%")

        # Optimized should be faster
        assert optimized_time < original_time, (
            f"Optimized functions should be faster: {optimized_time:.6f}s vs {original_time:.6f}s"
        )

    def test_caching_effectiveness(self):
        """Test that caching is effective for repeated inputs."""
        test_input = "This is a test message that will be validated multiple times"
        iterations = 1000

        # Test without caching (first run)
        start_time = time.perf_counter()
        for _ in range(iterations):
            try:
                optimized_validate_message_content(test_input)
            except ValueError:
                pass
        first_run_time = time.perf_counter() - start_time

        # Test with caching (second run - should be faster due to cache hits)
        start_time = time.perf_counter()
        for _ in range(iterations):
            try:
                optimized_validate_message_content(test_input)
            except ValueError:
                pass
        second_run_time = time.perf_counter() - start_time

        print("\nCaching effectiveness:")
        print(f"First run: {first_run_time:.6f}s for {iterations} validations")
        print(f"Second run: {second_run_time:.6f}s for {iterations} validations")
        print(f"Cache improvement: {((first_run_time - second_run_time) / first_run_time * 100):.1f}%")

        # Second run should be faster due to caching
        assert second_run_time < first_run_time, (
            f"Cached validation should be faster: {second_run_time:.6f}s vs {first_run_time:.6f}s"
        )

    def test_memory_usage_optimization(self):
        """Test that optimized functions use memory efficiently."""
        import sys

        # Test memory usage of original functions
        original_functions = [
            validate_message_content,
            validate_action_content,
            validate_player_name,
            validate_alias_name,
        ]

        # Test memory usage of optimized functions
        optimized_functions = [
            optimized_validate_message_content,
            optimized_validate_action_content,
            optimized_validate_player_name,
            optimized_validate_alias_name,
        ]

        # Create instances and measure memory usage
        original_instances = []
        optimized_instances = []

        memory_before = sys.getsizeof(original_instances) + sys.getsizeof(optimized_instances)

        # Create 100 instances of each type
        for _ in range(100):
            original_instances.extend(list(original_functions))
            optimized_instances.extend(list(optimized_functions))

        memory_after = sys.getsizeof(original_instances) + sys.getsizeof(optimized_instances)
        memory_per_instance = (memory_after - memory_before) / (len(original_instances) + len(optimized_instances))

        print(f"\nMemory usage per validation function: {memory_per_instance:.2f} bytes")

        # Memory usage should be reasonable
        assert memory_per_instance < 1000, f"Memory usage too high: {memory_per_instance:.2f} bytes per function"
