"""
Tests for lazy loading optimizations in game models.

This module tests the lazy loading optimizations in the optimized game models
to ensure they provide correct results and performance improvements.
"""

import time

from server.models.game import AttributeType, Stats, StatusEffect, StatusEffectType
from server.models.optimized_game import OptimizedStats, OptimizedStatusEffect


class TestLazyLoadingOptimization:
    """Test lazy loading optimizations in game models."""

    def test_optimized_stats_computed_fields_work_correctly(self):
        """Test that optimized stats computed fields produce correct results."""
        stats = OptimizedStats()

        # Test computed fields
        assert stats.max_health == stats.constitution * 10
        assert stats.max_sanity == stats.wisdom * 5

        # Test attribute modifier
        assert stats.get_attribute_modifier(AttributeType.STR) == (stats.strength - 10) // 2
        assert stats.get_attribute_modifier(AttributeType.CON) == (stats.constitution - 10) // 2

        # Test boolean methods
        assert stats.is_sane() == (stats.sanity > 0)
        assert stats.is_corrupted() == (stats.corruption >= 50)
        assert stats.is_insane() == (stats.sanity <= 0)

    def test_optimized_status_effect_works_correctly(self):
        """Test that optimized status effect works correctly."""
        status_effect = OptimizedStatusEffect(
            effect_type=StatusEffectType.POISONED, duration=10, intensity=5, source="poison dart"
        )

        # Test is_active method
        assert status_effect.is_active(5) is True  # Before duration expires
        assert status_effect.is_active(15) is False  # After duration expires
        assert status_effect.is_active(10) is False  # At duration limit

    def test_optimized_stats_caching_effectiveness(self):
        """Test that caching is effective for computed fields."""
        stats = OptimizedStats()
        iterations = 1000

        # Test max_health caching
        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = stats.max_health
        first_run_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = stats.max_health
        second_run_time = time.perf_counter() - start_time

        print("\nStats max_health caching:")
        print(f"First run: {first_run_time:.6f}s for {iterations} computations")
        print(f"Second run: {second_run_time:.6f}s for {iterations} computations")

        # Second run should be faster due to caching
        assert second_run_time < first_run_time, (
            f"Cached computation should be faster: {second_run_time:.6f}s vs {first_run_time:.6f}s"
        )

    def test_optimized_status_effect_caching_effectiveness(self):
        """Test that caching is effective for status effect methods."""
        status_effect = OptimizedStatusEffect(
            effect_type=StatusEffectType.POISONED, duration=10, intensity=5, source="poison dart"
        )

        iterations = 1000
        current_tick = 5

        # Test is_active caching
        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = status_effect.is_active(current_tick)
        first_run_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = status_effect.is_active(current_tick)
        second_run_time = time.perf_counter() - start_time

        print("\nStatus effect is_active caching:")
        print(f"First run: {first_run_time:.6f}s for {iterations} computations")
        print(f"Second run: {second_run_time:.6f}s for {iterations} computations")

        # Second run should be faster due to caching
        assert second_run_time < first_run_time, (
            f"Cached computation should be faster: {second_run_time:.6f}s vs {first_run_time:.6f}s"
        )

    def test_optimized_stats_attribute_modifier_caching(self):
        """Test that attribute modifier caching is effective."""
        stats = OptimizedStats()
        iterations = 1000

        # Test get_attribute_modifier caching
        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = stats.get_attribute_modifier(AttributeType.STR)
        first_run_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = stats.get_attribute_modifier(AttributeType.STR)
        second_run_time = time.perf_counter() - start_time

        print("\nStats attribute modifier caching:")
        print(f"First run: {first_run_time:.6f}s for {iterations} computations")
        print(f"Second run: {second_run_time:.6f}s for {iterations} computations")

        # Second run should be faster due to caching
        assert second_run_time < first_run_time, (
            f"Cached computation should be faster: {second_run_time:.6f}s vs {first_run_time:.6f}s"
        )

    def test_optimized_vs_original_performance_comparison(self):
        """Compare performance of optimized vs original models."""
        iterations = 500

        # Test original Stats model
        original_stats = Stats()
        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = original_stats.max_health
            _ = original_stats.max_sanity
            _ = original_stats.get_attribute_modifier(AttributeType.STR)
            _ = original_stats.is_sane()
            _ = original_stats.is_corrupted()
            _ = original_stats.is_insane()
        original_time = time.perf_counter() - start_time

        # Test optimized Stats model
        optimized_stats = OptimizedStats()
        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = optimized_stats.max_health
            _ = optimized_stats.max_sanity
            _ = optimized_stats.get_attribute_modifier(AttributeType.STR)
            _ = optimized_stats.is_sane()
            _ = optimized_stats.is_corrupted()
            _ = optimized_stats.is_insane()
        optimized_time = time.perf_counter() - start_time

        print("\nStats model performance comparison:")
        print(f"Original: {original_time:.6f}s for {iterations * 6} computations")
        print(f"Optimized: {optimized_time:.6f}s for {iterations * 6} computations")
        print(f"Improvement: {((original_time - optimized_time) / original_time * 100):.1f}%")

        # Optimized should be faster
        assert optimized_time < original_time, (
            f"Optimized model should be faster: {optimized_time:.6f}s vs {original_time:.6f}s"
        )

    def test_optimized_vs_original_status_effect_performance(self):
        """Compare performance of optimized vs original status effect models."""
        iterations = 500

        # Test original StatusEffect model
        original_status_effect = StatusEffect(
            effect_type=StatusEffectType.POISONED, duration=10, intensity=5, source="poison dart"
        )
        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = original_status_effect.is_active(5)
            _ = original_status_effect.is_active(15)
            _ = original_status_effect.is_active(10)
        original_time = time.perf_counter() - start_time

        # Test optimized StatusEffect model
        optimized_status_effect = OptimizedStatusEffect(
            effect_type=StatusEffectType.POISONED, duration=10, intensity=5, source="poison dart"
        )
        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = optimized_status_effect.is_active(5)
            _ = optimized_status_effect.is_active(15)
            _ = optimized_status_effect.is_active(10)
        optimized_time = time.perf_counter() - start_time

        print("\nStatus effect performance comparison:")
        print(f"Original: {original_time:.6f}s for {iterations * 3} computations")
        print(f"Optimized: {optimized_time:.6f}s for {iterations * 3} computations")
        print(f"Improvement: {((original_time - optimized_time) / original_time * 100):.1f}%")

        # Optimized should be faster
        assert optimized_time < original_time, (
            f"Optimized model should be faster: {optimized_time:.6f}s vs {original_time:.6f}s"
        )

    def test_cache_clearing_functionality(self):
        """Test that cache clearing works correctly."""
        stats = OptimizedStats()
        status_effect = OptimizedStatusEffect(
            effect_type=StatusEffectType.POISONED, duration=10, intensity=5, source="poison dart"
        )

        # Access methods to populate cache
        _ = stats.max_health
        _ = stats.get_attribute_modifier(AttributeType.STR)
        _ = stats.is_sane()
        _ = status_effect.is_active(5)

        # Clear caches
        stats.clear_cache()
        status_effect.clear_cache()

        # Verify caches are cleared (this is internal, but we can test that methods still work)
        assert stats.max_health == stats.constitution * 10
        assert stats.get_attribute_modifier(AttributeType.STR) == (stats.strength - 10) // 2
        assert stats.is_sane() == (stats.sanity > 0)
        assert status_effect.is_active(5) is True

    def test_memory_usage_optimization(self):
        """Test that optimized models use memory efficiently."""
        import sys

        # Test memory usage of original models
        original_stats = Stats()
        original_status_effect = StatusEffect(
            effect_type=StatusEffectType.POISONED, duration=10, intensity=5, source="poison dart"
        )

        # Test memory usage of optimized models
        optimized_stats = OptimizedStats()
        optimized_status_effect = OptimizedStatusEffect(
            effect_type=StatusEffectType.POISONED, duration=10, intensity=5, source="poison dart"
        )

        # Measure memory usage
        original_memory = sys.getsizeof(original_stats) + sys.getsizeof(original_status_effect)
        optimized_memory = sys.getsizeof(optimized_stats) + sys.getsizeof(optimized_status_effect)

        print("\nMemory usage comparison:")
        print(f"Original models: {original_memory} bytes")
        print(f"Optimized models: {optimized_memory} bytes")

        # Memory usage should be reasonable (optimized models may use slightly more due to cache)
        assert optimized_memory < original_memory * 2, f"Optimized models use too much memory: {optimized_memory} bytes"

    def test_lazy_loading_with_different_inputs(self):
        """Test lazy loading with different input values."""
        stats = OptimizedStats()

        # Test with different attribute types
        for attr_type in AttributeType:
            modifier = stats.get_attribute_modifier(attr_type)
            expected = (getattr(stats, attr_type.value, 10) - 10) // 2
            assert modifier == expected, f"Modifier for {attr_type} should be {expected}, got {modifier}"

        # Test status effect with different ticks
        status_effect = OptimizedStatusEffect(
            effect_type=StatusEffectType.POISONED, duration=10, intensity=5, source="poison dart"
        )

        for tick in [0, 5, 10, 15, 20]:
            is_active = status_effect.is_active(tick)
            expected = tick < 10
            assert is_active == expected, (
                f"Status effect should be {'active' if expected else 'inactive'} at tick {tick}"
            )

    def test_lazy_loading_edge_cases(self):
        """Test lazy loading with edge cases."""
        # Test with extreme values
        stats = OptimizedStats()
        stats.strength = 1
        stats.constitution = 20
        stats.wisdom = 1
        stats.sanity = 0
        stats.corruption = 100

        # Clear cache to test with new values
        stats.clear_cache()

        # Test computed fields with extreme values
        assert stats.max_health == 200  # 20 * 10
        assert stats.max_sanity == 5  # 1 * 5
        assert stats.get_attribute_modifier(AttributeType.STR) == -5  # (1 - 10) // 2
        assert stats.is_sane() is False
        assert stats.is_corrupted() is True
        assert stats.is_insane() is True

        # Test status effect with edge cases
        status_effect = OptimizedStatusEffect(
            effect_type=StatusEffectType.POISONED,
            duration=0,  # Permanent
            intensity=10,
            source="permanent poison",
        )

        # Permanent effect should always be active
        assert status_effect.is_active(0) is True
        assert status_effect.is_active(1000) is True
        assert status_effect.is_active(-1) is True
