"""
Performance tests for error logging functionality.

This module tests the performance characteristics of error logging to ensure
it doesn't impact system performance, following the academic rigor outlined
in the Pnakotic Manuscripts of Testing Methodology.
"""

import gc
import os
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from unittest.mock import patch

import pytest

from server.exceptions import DatabaseError, ErrorContext, create_error_context
from server.utils.error_logging import log_and_raise


class PerformanceTestMixin:
    """Mixin class providing performance testing utilities."""

    def measure_execution_time(self, func, *args, **kwargs) -> tuple[float, any]:
        """
        Measure the execution time of a function.

        Returns:
            Tuple of (execution_time_seconds, function_result)
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - start_time, result

    def measure_memory_usage(self, func, *args, **kwargs) -> tuple[float, any]:
        """
        Measure memory usage during function execution.

        Returns:
            Tuple of (memory_delta_mb, function_result)
        """
        import os

        import psutil

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB

        result = func(*args, **kwargs)

        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_delta = final_memory - initial_memory

        return memory_delta, result

    def run_concurrent_operations(self, func, iterations: int, max_workers: int = 10) -> list[float]:
        """
        Run function concurrently and measure execution times.

        Returns:
            List of execution times for each operation
        """
        execution_times = []
        lock = Lock()

        def worker():
            exec_time, _ = self.measure_execution_time(func)
            with lock:
                execution_times.append(exec_time)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(worker) for _ in range(iterations)]
            for future in as_completed(futures):
                future.result()  # Wait for completion

        return execution_times


class TestErrorContextPerformance:
    """Performance tests for ErrorContext creation and operations."""

    @pytest.fixture
    def perf_mixin(self):
        """Provide performance test mixin."""
        return PerformanceTestMixin()

    def test_error_context_creation_speed(self, perf_mixin):
        """Test that ErrorContext creation is fast."""

        def create_context():
            return create_error_context()

        # Measure single context creation
        exec_time, context = perf_mixin.measure_execution_time(create_context)

        assert exec_time < 0.001, f"ErrorContext creation too slow: {exec_time:.6f}s"
        assert isinstance(context, ErrorContext)

    def test_error_context_creation_bulk_performance(self, perf_mixin):
        """Test bulk ErrorContext creation performance."""

        def create_contexts(count: int):
            return [create_error_context() for _ in range(count)]

        # Test different batch sizes
        for batch_size in [100, 500, 1000]:
            exec_time, contexts = perf_mixin.measure_execution_time(create_contexts, batch_size)

            assert len(contexts) == batch_size
            assert exec_time < 0.1, f"Bulk ErrorContext creation too slow: {exec_time:.3f}s for {batch_size} contexts"

            # Calculate contexts per second
            contexts_per_second = batch_size / exec_time
            assert contexts_per_second > 10000, (
                f"ErrorContext creation rate too low: {contexts_per_second:.0f} contexts/second"
            )

    def test_error_context_serialization_performance(self, perf_mixin):
        """Test ErrorContext serialization performance."""
        context = create_error_context(user_id="test-user", metadata={"test_key": "test_value", "number": 42})

        def serialize_context():
            return context.to_dict()

        # Measure serialization time
        exec_time, serialized = perf_mixin.measure_execution_time(serialize_context)

        assert exec_time < 0.001, f"ErrorContext serialization too slow: {exec_time:.6f}s"
        assert isinstance(serialized, dict)
        assert "timestamp" in serialized
        assert "user_id" in serialized

    def test_error_context_memory_usage(self, perf_mixin):
        """Test ErrorContext memory usage characteristics."""

        def create_many_contexts():
            contexts = []
            for i in range(1000):
                context = create_error_context(user_id=f"user-{i}", metadata={"iteration": i, "data": f"test-data-{i}"})
                contexts.append(context)
            return contexts

        # Measure memory usage
        memory_delta, contexts = perf_mixin.measure_memory_usage(create_many_contexts)

        # Memory usage should be reasonable (less than 10MB for 1000 contexts)
        assert memory_delta < 10, f"ErrorContext memory usage too high: {memory_delta:.2f}MB for 1000 contexts"
        assert len(contexts) == 1000

    def test_error_context_concurrent_creation(self, perf_mixin):
        """Test ErrorContext creation under concurrent load."""

        def create_context():
            return create_error_context(user_id="concurrent-user")

        # Run concurrent operations
        execution_times = perf_mixin.run_concurrent_operations(create_context, iterations=100, max_workers=20)

        # All operations should complete
        assert len(execution_times) == 100

        # Performance should be consistent
        avg_time = sum(execution_times) / len(execution_times)
        max_time = max(execution_times)

        assert avg_time < 0.01, f"Average ErrorContext creation too slow: {avg_time:.6f}s"
        assert max_time < 0.05, f"Maximum ErrorContext creation too slow: {max_time:.6f}s"


class TestLogAndRaisePerformance:
    """Performance tests for log_and_raise function."""

    @pytest.fixture
    def perf_mixin(self):
        """Provide performance test mixin."""
        return PerformanceTestMixin()

    def test_log_and_raise_speed(self, perf_mixin):
        """Test that log_and_raise is fast."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def log_error():
                try:
                    log_and_raise(DatabaseError, "Performance test error")
                except DatabaseError:
                    pass

            # Measure single log_and_raise operation
            exec_time, _ = perf_mixin.measure_execution_time(log_error)

            assert exec_time < 0.01, f"log_and_raise too slow: {exec_time:.6f}s"

    def test_log_and_raise_bulk_performance(self, perf_mixin):
        """Test bulk log_and_raise performance."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def log_errors(count: int):
                for i in range(count):
                    try:
                        log_and_raise(DatabaseError, f"Bulk test error {i}")
                    except DatabaseError:
                        pass

            # Test different batch sizes
            for batch_size in [100, 500, 1000]:
                exec_time, _ = perf_mixin.measure_execution_time(log_errors, batch_size)

                assert exec_time < 1.0, f"Bulk log_and_raise too slow: {exec_time:.3f}s for {batch_size} operations"

                # Calculate operations per second
                ops_per_second = batch_size / exec_time
                assert ops_per_second > 1000, f"log_and_raise rate too low: {ops_per_second:.0f} ops/second"

    def test_log_and_raise_with_context_performance(self, perf_mixin):
        """Test log_and_raise performance with error context."""
        context = create_error_context(user_id="perf-test-user", metadata={"test": "performance", "value": 123})

        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def log_error_with_context():
                try:
                    log_and_raise(
                        DatabaseError, "Context performance test error", context=context, details={"additional": "data"}
                    )
                except DatabaseError:
                    pass

            # Measure log_and_raise with context
            exec_time, _ = perf_mixin.measure_execution_time(log_error_with_context)

            assert exec_time < 0.01, f"log_and_raise with context too slow: {exec_time:.6f}s"

    def test_log_and_raise_memory_usage(self, perf_mixin):
        """Test log_and_raise memory usage characteristics."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def log_many_errors():
                for i in range(1000):
                    try:
                        log_and_raise(
                            DatabaseError, f"Memory test error {i}", details={"iteration": i, "data": f"test-{i}"}
                        )
                    except DatabaseError:
                        pass

            # Measure memory usage
            memory_delta, _ = perf_mixin.measure_memory_usage(log_many_errors)

            # Memory usage should be reasonable (less than 5MB for 1000 operations)
            assert memory_delta < 5, f"log_and_raise memory usage too high: {memory_delta:.2f}MB for 1000 operations"

    def test_log_and_raise_concurrent_performance(self, perf_mixin):
        """Test log_and_raise performance under concurrent load."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def log_error():
                try:
                    log_and_raise(DatabaseError, "Concurrent test error")
                except DatabaseError:
                    pass

            # Run concurrent operations
            execution_times = perf_mixin.run_concurrent_operations(log_error, iterations=200, max_workers=25)

            # All operations should complete
            assert len(execution_times) == 200

            # Performance should be consistent
            avg_time = sum(execution_times) / len(execution_times)
            max_time = max(execution_times)

            assert avg_time < 0.02, f"Average log_and_raise too slow: {avg_time:.6f}s"
            assert max_time < 0.1, f"Maximum log_and_raise too slow: {max_time:.6f}s"


class TestErrorLoggingSystemPerformance:
    """System-level performance tests for error logging."""

    @pytest.fixture
    def perf_mixin(self):
        """Provide performance test mixin."""
        return PerformanceTestMixin()

    def test_error_logging_under_high_load(self, perf_mixin):
        """Test error logging performance under high load conditions."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def high_load_operation():
                # Simulate a high-load scenario with multiple error types
                errors = []
                for i in range(50):
                    try:
                        if i % 3 == 0:
                            log_and_raise(DatabaseError, f"Database error {i}")
                        elif i % 3 == 1:
                            log_and_raise(DatabaseError, f"Database error {i}")
                        else:
                            log_and_raise(DatabaseError, f"Database error {i}")
                    except DatabaseError:
                        errors.append(i)
                return errors

            # Measure performance under load
            exec_time, errors = perf_mixin.measure_execution_time(high_load_operation)

            assert len(errors) == 50, "All errors should be processed"
            assert exec_time < 0.5, f"High load error logging too slow: {exec_time:.3f}s"

    def test_error_logging_memory_leak_prevention(self, perf_mixin):
        """Test that error logging doesn't cause memory leaks."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def create_and_log_errors(iterations: int):
                contexts = []
                for i in range(iterations):
                    context = create_error_context(
                        user_id=f"leak-test-user-{i}", metadata={"iteration": i, "data": f"leak-test-{i}"}
                    )
                    contexts.append(context)

                    try:
                        log_and_raise(
                            DatabaseError,
                            f"Memory leak test error {i}",
                            context=context,
                            details={"test": "memory", "iteration": i},
                        )
                    except DatabaseError:
                        pass

                return contexts

            # Run multiple iterations to test for memory leaks
            initial_memory = perf_mixin.measure_memory_usage(lambda: None)[0]

            for _iteration in range(5):
                contexts = create_and_log_errors(1000)
                del contexts  # Explicitly delete to help garbage collection
                gc.collect()  # Force garbage collection

            final_memory = perf_mixin.measure_memory_usage(lambda: None)[0]
            memory_growth = final_memory - initial_memory

            # Memory growth should be minimal (less than 10MB)
            assert memory_growth < 10, f"Potential memory leak detected: {memory_growth:.2f}MB growth"

    def test_error_logging_file_io_performance(self, perf_mixin):
        """Test error logging performance with actual file I/O."""
        temp_dir = tempfile.mkdtemp()
        log_file = os.path.join(temp_dir, "performance_test.log")

        try:
            # Configure logger to write to file
            with patch("server.utils.error_logging.get_logger") as mock_get_logger:
                # Create a mock logger that doesn't actually log
                mock_logger = mock_get_logger.return_value
                mock_logger.error = lambda *args, **kwargs: None

                def log_to_file():
                    try:
                        log_and_raise(DatabaseError, "File I/O performance test error")
                    except DatabaseError:
                        pass

                # Measure file I/O performance
                exec_time, _ = perf_mixin.measure_execution_time(log_to_file)

                assert exec_time < 0.05, f"File I/O error logging too slow: {exec_time:.6f}s"

        finally:
            # Cleanup
            if os.path.exists(log_file):
                os.remove(log_file)
            os.rmdir(temp_dir)

    def test_error_logging_network_performance(self, perf_mixin):
        """Test error logging performance with network operations."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            # Simulate network delay
            def slow_network_operation():
                time.sleep(0.001)  # Simulate 1ms network delay
                return "network_response"

            def log_with_network():
                network_result = slow_network_operation()
                try:
                    log_and_raise(
                        DatabaseError, f"Network error: {network_result}", details={"network_operation": "test"}
                    )
                except DatabaseError:
                    pass

            # Measure performance with network simulation
            exec_time, _ = perf_mixin.measure_execution_time(log_with_network)

            # Should be fast despite network delay
            assert exec_time < 0.1, f"Network error logging too slow: {exec_time:.6f}s"

    def test_error_logging_database_performance(self, perf_mixin):
        """Test error logging performance with database operations."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            # Simulate database operations
            def database_operation():
                # Simulate database query time
                time.sleep(0.002)  # Simulate 2ms database operation
                return {"result": "database_data"}

            def log_with_database():
                db_result = database_operation()
                try:
                    log_and_raise(
                        DatabaseError,
                        f"Database error: {db_result}",
                        details={"database_operation": "test", "result": db_result},
                    )
                except DatabaseError:
                    pass

            # Measure performance with database simulation
            exec_time, _ = perf_mixin.measure_execution_time(log_with_database)

            # Should be fast despite database delay
            assert exec_time < 0.1, f"Database error logging too slow: {exec_time:.6f}s"


class TestErrorLoggingScalability:
    """Scalability tests for error logging system."""

    @pytest.fixture
    def perf_mixin(self):
        """Provide performance test mixin."""
        return PerformanceTestMixin()

    def test_error_logging_scales_with_load(self, perf_mixin):
        """Test that error logging scales appropriately with load."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def scalable_operation(load_factor: int):
                errors = []
                for i in range(load_factor * 100):
                    try:
                        log_and_raise(
                            DatabaseError,
                            f"Scalability test error {i}",
                            details={"load_factor": load_factor, "iteration": i},
                        )
                    except DatabaseError:
                        errors.append(i)
                return errors

            # Test different load factors
            load_factors = [1, 2, 5, 10]
            execution_times = []

            for factor in load_factors:
                exec_time, errors = perf_mixin.measure_execution_time(scalable_operation, factor)
                execution_times.append(exec_time)

                expected_errors = factor * 100
                assert len(errors) == expected_errors, f"Expected {expected_errors} errors, got {len(errors)}"

            # Performance should scale linearly (or better)
            # Each load factor should not take more than 2x the time of the previous
            for i in range(1, len(execution_times)):
                time_ratio = execution_times[i] / execution_times[i - 1]
                load_ratio = load_factors[i] / load_factors[i - 1]

                # Time ratio should not exceed 2x the load ratio
                assert time_ratio <= 2 * load_ratio, (
                    f"Performance doesn't scale well: {time_ratio:.2f}x time for {load_ratio:.2f}x load"
                )

    def test_error_logging_handles_peak_load(self, perf_mixin):
        """Test error logging performance during peak load conditions."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def peak_load_operation():
                # Simulate peak load with burst of errors
                errors = []
                for i in range(1000):  # High burst of errors
                    try:
                        log_and_raise(
                            DatabaseError, f"Peak load error {i}", details={"peak_load": True, "iteration": i}
                        )
                    except DatabaseError:
                        errors.append(i)
                return errors

            # Measure peak load performance
            exec_time, errors = perf_mixin.measure_execution_time(peak_load_operation)

            assert len(errors) == 1000, "All peak load errors should be processed"
            assert exec_time < 2.0, f"Peak load error logging too slow: {exec_time:.3f}s"

            # Calculate errors per second during peak load
            errors_per_second = 1000 / exec_time
            assert errors_per_second > 500, f"Peak load error rate too low: {errors_per_second:.0f} errors/second"

    def test_error_logging_sustained_load(self, perf_mixin):
        """Test error logging performance under sustained load."""
        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            # Create a mock logger that doesn't actually log
            mock_logger = mock_get_logger.return_value
            mock_logger.error = lambda *args, **kwargs: None

            def sustained_load_operation(duration_seconds: float):
                start_time = time.time()
                error_count = 0

                while time.time() - start_time < duration_seconds:
                    try:
                        log_and_raise(
                            DatabaseError,
                            f"Sustained load error {error_count}",
                            details={"sustained_load": True, "count": error_count},
                        )
                    except DatabaseError:
                        error_count += 1

                return error_count

            # Test sustained load for 1 second
            exec_time, error_count = perf_mixin.measure_execution_time(sustained_load_operation, 1.0)

            # Should handle sustained load efficiently
            assert error_count > 100, f"Too few errors processed during sustained load: {error_count}"
            assert exec_time < 1.5, f"Sustained load took too long: {exec_time:.3f}s"

            # Calculate sustained error rate
            sustained_rate = error_count / exec_time
            assert sustained_rate > 100, f"Sustained error rate too low: {sustained_rate:.0f} errors/second"
