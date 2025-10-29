"""
Performance tests for NATS Subject Manager.

This module tests the performance characteristics of the NATSSubjectManager,
including caching efficiency, validation speed, and pattern matching performance.

Following the rigorous benchmarking methodologies described in the
Pnakotic Manuscripts of Performance Analysis.

AI: Performance tests verify caching effectiveness and operation speeds.
AI: Tests establish performance baselines for monitoring and optimization.
"""

import time

import pytest

from server.logging.enhanced_logging_config import get_logger
from server.services.nats_subject_manager import NATSSubjectManager

logger = get_logger("tests.performance.subject_manager")


class TestSubjectManagerPerformance:
    """Performance tests for subject manager operations."""

    def test_build_subject_performance(self):
        """Test that subject building is fast enough for high-throughput scenarios."""
        manager = NATSSubjectManager()

        # Benchmark: Build 10,000 subjects
        iterations = 10_000
        start_time = time.perf_counter()

        for i in range(iterations):
            subject = manager.build_subject("chat_say_room", room_id=f"room_{i}")
            assert subject.startswith("chat.say.room.")

        elapsed = time.perf_counter() - start_time

        # Performance target: < 100ms for 10,000 builds (< 0.01ms per operation)
        assert elapsed < 0.1, f"Build performance degraded: {elapsed:.4f}s for {iterations} operations"

        # Log performance metrics
        avg_time_ms = (elapsed / iterations) * 1000
        ops_per_second = iterations / elapsed

        logger.info(
            "Build performance benchmark completed",
            total_time_s=elapsed,
            iterations=iterations,
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
        )

    def test_validation_performance_without_cache(self):
        """Test validation performance without caching."""
        manager = NATSSubjectManager(enable_cache=False)

        # Benchmark: Validate 1,000 subjects without cache
        iterations = 1_000
        test_subject = "chat.say.room.test_room"

        start_time = time.perf_counter()

        for _ in range(iterations):
            is_valid = manager.validate_subject(test_subject)
            assert is_valid is True

        elapsed = time.perf_counter() - start_time

        # Performance target: < 50ms for 1,000 validations without cache
        assert elapsed < 0.05, f"Validation performance degraded: {elapsed:.4f}s for {iterations} operations"

        avg_time_ms = (elapsed / iterations) * 1000
        ops_per_second = iterations / elapsed

        logger.info(
            "Validation performance without cache benchmark completed",
            total_time_s=elapsed,
            iterations=iterations,
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
        )

    def test_validation_performance_with_cache(self):
        """Test validation performance with caching enabled."""
        manager = NATSSubjectManager(enable_cache=True)

        # Benchmark: Validate same subject 10,000 times with cache
        iterations = 10_000
        test_subject = "chat.say.room.test_room"

        # Prime the cache
        manager.validate_subject(test_subject)

        start_time = time.perf_counter()

        for _ in range(iterations):
            is_valid = manager.validate_subject(test_subject)
            assert is_valid is True

        elapsed = time.perf_counter() - start_time

        # Performance target: < 100ms for 10,000 cached validations (< 0.01ms per operation)
        assert elapsed < 0.1, f"Cached validation performance degraded: {elapsed:.4f}s for {iterations} operations"

        avg_time_ms = (elapsed / iterations) * 1000
        ops_per_second = iterations / elapsed

        logger.info(
            "Validation performance with cache benchmark completed",
            total_time_s=elapsed,
            iterations=iterations,
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
        )

    def test_cache_effectiveness(self):
        """Test that caching provides significant performance improvement."""
        # Test without cache
        manager_no_cache = NATSSubjectManager(enable_cache=False)
        test_subject = "chat.say.room.test_room"
        iterations = 1_000

        start_no_cache = time.perf_counter()
        for _ in range(iterations):
            manager_no_cache.validate_subject(test_subject)
        time_no_cache = time.perf_counter() - start_no_cache

        # Test with cache
        manager_with_cache = NATSSubjectManager(enable_cache=True)
        manager_with_cache.validate_subject(test_subject)  # Prime cache

        start_with_cache = time.perf_counter()
        for _ in range(iterations):
            manager_with_cache.validate_subject(test_subject)
        time_with_cache = time.perf_counter() - start_with_cache

        # Cache should provide at least 3x speedup
        speedup = time_no_cache / time_with_cache
        assert speedup > 3, f"Cache speedup insufficient: {speedup:.1f}x (expected > 3x)"

        logger.info(
            "Cache effectiveness benchmark completed",
            time_no_cache_s=time_no_cache,
            time_with_cache_s=time_with_cache,
            speedup_factor=speedup,
            iterations=iterations,
        )

    def test_pattern_matching_performance(self):
        """Test pattern matching performance across all patterns."""
        manager = NATSSubjectManager()

        # Test subjects for each pattern type
        test_subjects = [
            "chat.say.room.arkham_1",
            "chat.local.subzone.miskatonic",
            "chat.global",
            "chat.whisper.player.player_123",
            "chat.system",
            "chat.emote.room.innsmouth_1",
            "chat.pose.room.dunwich_1",
            "events.player_entered.room_1",
            "combat.attack.room_2",
        ]

        iterations = 1_000
        start_time = time.perf_counter()

        for _ in range(iterations):
            for subject in test_subjects:
                is_valid = manager.validate_subject(subject)
                assert is_valid is True

        elapsed = time.perf_counter() - start_time
        total_operations = iterations * len(test_subjects)

        # Performance target: < 100ms for 9,000 pattern matches
        assert elapsed < 0.1, f"Pattern matching performance degraded: {elapsed:.4f}s for {total_operations} operations"

        avg_time_ms = (elapsed / total_operations) * 1000
        ops_per_second = total_operations / elapsed

        logger.info(
            "Pattern matching performance benchmark completed",
            total_time_s=elapsed,
            total_operations=total_operations,
            unique_patterns=len(test_subjects),
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
        )

    def test_metrics_collection_overhead(self):
        """Test that metrics collection adds minimal overhead."""
        # Test with metrics enabled
        manager_with_metrics = NATSSubjectManager(enable_metrics=True)
        iterations = 1_000

        start_with_metrics = time.perf_counter()
        for i in range(iterations):
            manager_with_metrics.build_subject("chat_say_room", room_id=f"room_{i}")
        time_with_metrics = time.perf_counter() - start_with_metrics

        # Test with metrics disabled
        manager_no_metrics = NATSSubjectManager(enable_metrics=False)

        start_no_metrics = time.perf_counter()
        for i in range(iterations):
            manager_no_metrics.build_subject("chat_say_room", room_id=f"room_{i}")
        time_no_metrics = time.perf_counter() - start_no_metrics

        # Metrics should add < 30% overhead
        overhead_ratio = time_with_metrics / time_no_metrics
        assert overhead_ratio < 1.3, f"Metrics overhead too high: {overhead_ratio:.2f}x (expected < 1.3x)"

        logger.info(
            "Metrics collection overhead benchmark completed",
            time_without_metrics_s=time_no_metrics,
            time_with_metrics_s=time_with_metrics,
            overhead_ratio=overhead_ratio,
            overhead_percent=(overhead_ratio - 1) * 100,
            iterations=iterations,
        )

    def test_subscription_pattern_generation_performance(self):
        """Test performance of subscription pattern generation."""
        manager = NATSSubjectManager()

        # Benchmark: Generate subscription patterns
        iterations = 10_000
        start_time = time.perf_counter()

        for _ in range(iterations):
            chat_patterns = manager.get_chat_subscription_patterns()
            assert len(chat_patterns) == 7

        elapsed = time.perf_counter() - start_time

        # Performance target: < 200ms for 10,000 pattern generations
        assert elapsed < 0.2, f"Subscription pattern generation too slow: {elapsed:.4f}s for {iterations} operations"

        avg_time_ms = (elapsed / iterations) * 1000
        ops_per_second = iterations / elapsed

        logger.info(
            "Subscription pattern generation performance benchmark completed",
            total_time_s=elapsed,
            iterations=iterations,
            patterns_per_generation=len(chat_patterns),
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
        )

    def test_concurrent_validation_performance(self):
        """Test performance of concurrent validations from multiple threads."""
        import concurrent.futures

        manager = NATSSubjectManager()

        test_subjects = [
            "chat.say.room.arkham_1",
            "chat.local.subzone.miskatonic",
            "chat.global",
            "chat.whisper.player.player_123",
        ]

        def validate_subjects(iterations: int):
            """Validate subjects multiple times."""
            for _ in range(iterations):
                for subject in test_subjects:
                    manager.validate_subject(subject)

        # Benchmark: 4 threads each doing 250 iterations (1,000 total per thread)
        num_threads = 4
        iterations_per_thread = 250

        start_time = time.perf_counter()

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(validate_subjects, iterations_per_thread) for _ in range(num_threads)]
            concurrent.futures.wait(futures)

        elapsed = time.perf_counter() - start_time
        total_operations = num_threads * iterations_per_thread * len(test_subjects)

        # Performance target: < 200ms for 4,000 concurrent validations
        assert elapsed < 0.2, f"Concurrent validation too slow: {elapsed:.4f}s for {total_operations} operations"

        avg_time_ms = (elapsed / total_operations) * 1000
        ops_per_second = total_operations / elapsed

        logger.info(
            "Concurrent validation performance benchmark completed",
            num_threads=num_threads,
            iterations_per_thread=iterations_per_thread,
            total_time_s=elapsed,
            total_operations=total_operations,
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
        )

    def test_memory_efficiency_validation_cache(self):
        """Test that validation cache maintains reasonable memory footprint."""
        import sys

        manager = NATSSubjectManager()

        # Validate 2,000 unique subjects to fill cache beyond rolling window
        for i in range(2_000):
            subject = f"chat.say.room.room_{i}"
            manager.validate_subject(subject)

        # Cache should only keep entries (no hard limit, but should be reasonable)
        cache_size = len(manager._validation_cache)
        cache_memory_bytes = sys.getsizeof(manager._validation_cache)

        # Cache should not exceed reasonable size (< 1MB for 2,000 entries)
        assert cache_memory_bytes < 1_000_000, f"Validation cache too large: {cache_memory_bytes:,} bytes"

        logger.info(
            "Validation cache memory efficiency verified",
            cache_entries=cache_size,
            memory_bytes=cache_memory_bytes,
            memory_kb=cache_memory_bytes / 1024,
        )

    def test_memory_efficiency_metrics(self):
        """Test that metrics collection maintains reasonable memory footprint."""
        import sys

        manager = NATSSubjectManager(enable_metrics=True)

        # Perform 2,000 operations to test rolling window
        for i in range(2_000):
            manager.build_subject("chat_say_room", room_id=f"room_{i}")
            manager.validate_subject(f"chat.say.room.room_{i}")

        # Metrics should only keep last 1,000 times for each operation type
        assert len(manager.metrics.build_times) == 1_000, "Build times should maintain rolling window of 1,000"
        assert len(manager.metrics.validation_times) == 1_000, (
            "Validation times should maintain rolling window of 1,000"
        )

        # Calculate memory usage
        build_times_memory = sys.getsizeof(manager.metrics.build_times)
        validation_times_memory = sys.getsizeof(manager.metrics.validation_times)
        total_metrics_memory = build_times_memory + validation_times_memory

        # Metrics should not exceed reasonable size (< 100KB for 2,000 float values)
        assert total_metrics_memory < 100_000, f"Metrics memory too large: {total_metrics_memory:,} bytes"

        logger.info(
            "Metrics memory efficiency verified",
            build_times_entries=len(manager.metrics.build_times),
            validation_times_entries=len(manager.metrics.validation_times),
            build_times_memory_bytes=build_times_memory,
            validation_times_memory_bytes=validation_times_memory,
            total_metrics_memory_bytes=total_metrics_memory,
            total_metrics_memory_kb=total_metrics_memory / 1024,
        )


class TestCachePerformance:
    """Performance tests specifically for caching mechanisms."""

    def test_cache_hit_rate_single_subject(self):
        """Test cache hit rate for repeated validation of single subject."""
        manager = NATSSubjectManager()

        test_subject = "chat.say.room.arkham_1"
        iterations = 1_000

        # Perform validations
        for _ in range(iterations):
            manager.validate_subject(test_subject)

        # Check metrics
        metrics = manager.get_performance_metrics()

        # Should have high cache hit rate (999 hits, 1 miss)
        expected_hits = iterations - 1
        expected_misses = 1
        expected_hit_rate = expected_hits / iterations

        assert metrics["cache"]["hits"] == expected_hits
        assert metrics["cache"]["misses"] == expected_misses
        assert metrics["cache"]["hit_rate"] == pytest.approx(expected_hit_rate, rel=0.01)

        logger.info(
            "Cache hit rate test completed for single subject",
            iterations=iterations,
            cache_hits=metrics["cache"]["hits"],
            cache_misses=metrics["cache"]["misses"],
            hit_rate=metrics["cache"]["hit_rate"],
        )

    def test_cache_hit_rate_multiple_subjects(self):
        """Test cache hit rate for validation of multiple subjects."""
        manager = NATSSubjectManager()

        test_subjects = [f"chat.say.room.room_{i}" for i in range(10)]  # 10 unique subjects
        iterations_per_subject = 100

        # Validate each subject multiple times
        for _ in range(iterations_per_subject):
            for subject in test_subjects:
                manager.validate_subject(subject)

        # Check metrics
        metrics = manager.get_performance_metrics()

        total_operations = len(test_subjects) * iterations_per_subject
        expected_hits = total_operations - len(test_subjects)  # First validation of each is a miss
        expected_misses = len(test_subjects)
        expected_hit_rate = expected_hits / total_operations

        assert metrics["cache"]["hits"] == expected_hits
        assert metrics["cache"]["misses"] == expected_misses
        assert metrics["cache"]["hit_rate"] == pytest.approx(expected_hit_rate, rel=0.01)

        logger.info(
            "Cache hit rate test completed for multiple subjects",
            unique_subjects=len(test_subjects),
            iterations_per_subject=iterations_per_subject,
            total_operations=total_operations,
            cache_hits=metrics["cache"]["hits"],
            cache_misses=metrics["cache"]["misses"],
            hit_rate=metrics["cache"]["hit_rate"],
        )

    def test_cache_speedup_factor(self):
        """Test that cache provides measurable speedup."""
        # Measure without cache
        manager_no_cache = NATSSubjectManager(enable_cache=False, enable_metrics=False)
        test_subject = "chat.say.room.test_room"
        iterations = 1_000

        start_no_cache = time.perf_counter()
        for _ in range(iterations):
            manager_no_cache.validate_subject(test_subject)
        time_no_cache = time.perf_counter() - start_no_cache

        # Measure with cache
        manager_with_cache = NATSSubjectManager(enable_cache=True, enable_metrics=False)
        manager_with_cache.validate_subject(test_subject)  # Prime cache

        start_with_cache = time.perf_counter()
        for _ in range(iterations):
            manager_with_cache.validate_subject(test_subject)
        time_with_cache = time.perf_counter() - start_with_cache

        # Calculate speedup
        speedup = time_no_cache / time_with_cache

        # Cache should provide at least 5x speedup for repeated validations
        assert speedup > 5, f"Cache speedup insufficient: {speedup:.1f}x (expected > 5x)"

        logger.info(
            "Cache speedup analysis completed",
            time_no_cache_s=time_no_cache,
            time_with_cache_s=time_with_cache,
            time_no_cache_per_op_ms=time_no_cache / iterations * 1000,
            time_with_cache_per_op_ms=time_with_cache / iterations * 1000,
            speedup_factor=speedup,
            iterations=iterations,
        )


class TestMetricsPerformance:
    """Performance tests for metrics collection."""

    def test_metrics_percentile_calculation_performance(self):
        """Test that percentile calculation is fast enough."""
        manager = NATSSubjectManager()

        # Generate 1,000 operations to fill metrics
        for i in range(1_000):
            manager.build_subject("chat_say_room", room_id=f"room_{i}")

        # Benchmark: Get metrics 1,000 times
        iterations = 1_000
        start_time = time.perf_counter()

        for _ in range(iterations):
            metrics = manager.get_performance_metrics()
            assert metrics is not None

        elapsed = time.perf_counter() - start_time

        # Performance target: < 50ms for 1,000 metric retrievals
        assert elapsed < 0.05, f"Metrics retrieval too slow: {elapsed:.4f}s for {iterations} operations"

        avg_time_ms = (elapsed / iterations) * 1000
        ops_per_second = iterations / elapsed

        logger.info(
            "Metrics retrieval performance benchmark completed",
            total_time_s=elapsed,
            iterations=iterations,
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
        )

    def test_rolling_window_performance(self):
        """Test that rolling window maintenance doesn't degrade performance."""
        manager = NATSSubjectManager()

        # Perform 2,000 operations (rolling window keeps last 1,000)
        iterations = 2_000
        start_time = time.perf_counter()

        for i in range(iterations):
            manager.build_subject("chat_say_room", room_id=f"room_{i}")

        elapsed = time.perf_counter() - start_time

        # Should not degrade significantly when rolling window activates
        avg_time_ms = (elapsed / iterations) * 1000
        ops_per_second = iterations / elapsed

        # Performance target: Still < 100ms for 2,000 operations
        assert elapsed < 0.1, f"Rolling window maintenance degraded performance: {elapsed:.4f}s"

        # Verify window size is maintained
        assert len(manager.metrics.build_times) == 1_000

        logger.info(
            "Rolling window performance benchmark completed",
            total_operations=iterations,
            window_size=len(manager.metrics.build_times),
            total_time_s=elapsed,
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
        )


class TestScalability:
    """Scalability tests for subject manager under load."""

    def test_large_pattern_registry_performance(self):
        """Test performance with large number of registered patterns."""
        manager = NATSSubjectManager()

        # Register 100 additional patterns
        for i in range(100):
            manager.register_pattern(
                name=f"custom_pattern_{i}",
                pattern=f"custom.type.{i}.{{param}}",
                required_params=["param"],
                description=f"Custom pattern {i}",
            )

        # Total patterns: 23 (predefined) + 100 (custom) = 123
        assert len(manager.patterns) == 123

        # Benchmark: Validate subjects with large pattern registry
        test_subject = "chat.say.room.test"
        iterations = 1_000

        start_time = time.perf_counter()

        for _ in range(iterations):
            is_valid = manager.validate_subject(test_subject)
            assert is_valid is True

        elapsed = time.perf_counter() - start_time

        # Performance should not degrade significantly with more patterns
        # Target: < 50ms for 1,000 validations
        assert elapsed < 0.05, f"Large registry degraded performance: {elapsed:.4f}s for {iterations} operations"

        avg_time_ms = (elapsed / iterations) * 1000
        ops_per_second = iterations / elapsed

        logger.info(
            "Large pattern registry performance benchmark completed",
            total_patterns=len(manager.patterns),
            total_time_s=elapsed,
            iterations=iterations,
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
        )

    def test_high_throughput_scenario(self):
        """Test subject manager under high-throughput conditions."""
        manager = NATSSubjectManager()

        # Simulate high-throughput scenario: 50,000 operations
        iterations = 50_000
        start_time = time.perf_counter()

        for i in range(iterations):
            # Mix of build and validate operations
            if i % 2 == 0:
                manager.build_subject("chat_say_room", room_id=f"room_{i % 100}")
            else:
                manager.validate_subject(f"chat.say.room.room_{i % 100}")

        elapsed = time.perf_counter() - start_time

        # Performance target: < 500ms for 50,000 mixed operations
        assert elapsed < 0.5, f"High-throughput scenario too slow: {elapsed:.4f}s for {iterations} operations"

        avg_time_ms = (elapsed / iterations) * 1000
        ops_per_second = iterations / elapsed

        # Verify metrics are collected properly
        metrics = manager.get_performance_metrics()
        assert metrics["build"]["total_count"] == iterations // 2
        assert metrics["validation"]["total_count"] == iterations // 2

        logger.info(
            "High-throughput scenario benchmark completed",
            total_operations=iterations,
            build_operations=metrics["build"]["total_count"],
            validation_operations=metrics["validation"]["total_count"],
            total_time_s=elapsed,
            avg_time_ms=avg_time_ms,
            throughput_ops_per_sec=ops_per_second,
            cache_hit_rate=metrics["cache"]["hit_rate"],
        )
