"""
Tests for memory profiling utilities.

This module tests the memory profiling functionality to ensure it correctly
measures and reports memory usage for Pydantic models.
"""

import pytest

from server.models.alias import Alias
from server.models.command import LookCommand, SayCommand
from server.models.game import Stats, StatusEffect, StatusEffectType
from server.models.health import HealthResponse, HealthStatus
from server.utils.memory_profiler import MemoryProfiler


class TestMemoryProfiling:
    """Test memory profiling functionality."""

    def test_memory_profiler_initialization(self):
        """Test that memory profiler initializes correctly."""
        profiler = MemoryProfiler()

        # Should be able to get current memory usage
        memory_usage = profiler.get_current_memory_usage()
        assert isinstance(memory_usage, int)
        assert memory_usage > 0

    def test_memory_profiler_baseline(self):
        """Test that memory profiler can establish baseline."""
        profiler = MemoryProfiler()

        profiler.start_profiling()
        delta = profiler.get_memory_delta()
        profiler.stop_profiling()

        # Delta should be 0 or very small initially
        assert delta >= 0

    def test_model_instantiation_memory_measurement(self):
        """Test memory measurement for model instantiation."""
        profiler = MemoryProfiler()

        # Test with Alias model
        result = profiler.measure_model_instantiation(Alias, iterations=100, name="test_alias", command="go north")

        assert "model_class" in result
        assert result["model_class"] == "Alias"
        assert result["iterations"] == 100
        assert result["memory_delta_bytes"] >= 0
        assert result["memory_per_instance_bytes"] >= 0
        assert result["memory_per_instance_kb"] >= 0

    def test_model_serialization_memory_measurement(self):
        """Test memory measurement for model serialization."""
        profiler = MemoryProfiler()

        # Create some instances
        instances = [Alias(name=f"alias_{i}", command="go north") for i in range(10)]

        result = profiler.measure_model_serialization(instances, iterations=10)

        assert result["instances_count"] == 10
        assert result["iterations"] == 10
        assert result["total_serializations"] == 100
        assert result["memory_delta_bytes"] >= 0
        assert result["memory_per_serialization_bytes"] >= 0

    def test_model_deserialization_memory_measurement(self):
        """Test memory measurement for model deserialization."""
        profiler = MemoryProfiler()

        # Create serialized data
        serialized_data = [{"name": f"alias_{i}", "command": "go north"} for i in range(10)]

        result = profiler.measure_model_deserialization(Alias, serialized_data, iterations=10)

        assert result["model_class"] == "Alias"
        assert result["data_count"] == 10
        assert result["iterations"] == 10
        assert result["total_deserializations"] == 100
        assert result["memory_delta_bytes"] >= 0
        assert result["memory_per_deserialization_bytes"] >= 0

    def test_model_comparison_memory_usage(self):
        """Test memory usage comparison across models."""
        profiler = MemoryProfiler()

        model_classes = [Alias, SayCommand, LookCommand]
        test_data = {
            "Alias": {"name": "test_alias", "command": "go north"},
            "SayCommand": {"message": "Hello, world!"},
            "LookCommand": {"direction": "north"},
        }

        results = profiler.compare_models_memory_usage(model_classes, iterations=100, **test_data)

        # Should have results for each model
        assert "Alias" in results
        assert "SayCommand" in results
        assert "LookCommand" in results
        assert "_statistics" in results

        # Check statistics
        stats = results["_statistics"]
        assert stats["total_models"] == 3
        assert stats["min_memory_bytes"] >= 0
        assert stats["max_memory_bytes"] >= 0
        assert stats["avg_memory_bytes"] >= 0

    def test_memory_usage_summary(self):
        """Test memory usage summary generation."""
        profiler = MemoryProfiler()

        summary = profiler.get_memory_usage_summary()

        assert "rss_bytes" in summary
        assert "vms_bytes" in summary
        assert "rss_mb" in summary
        assert "vms_mb" in summary
        assert "percent" in summary
        assert "available_mb" in summary
        assert "total_mb" in summary

        # Values should be positive
        assert summary["rss_bytes"] > 0
        assert summary["vms_bytes"] > 0
        assert summary["rss_mb"] > 0
        assert summary["vms_mb"] > 0
        assert summary["percent"] > 0
        assert summary["available_mb"] > 0
        assert summary["total_mb"] > 0

    def test_stats_model_memory_usage(self):
        """Test memory usage for Stats model specifically."""
        profiler = MemoryProfiler()

        result = profiler.measure_model_instantiation(Stats, iterations=1000)

        assert result["model_class"] == "Stats"
        assert result["iterations"] == 1000
        assert result["memory_per_instance_bytes"] > 0

        # Stats model should use reasonable memory
        assert result["memory_per_instance_bytes"] < 1500  # Less than 1.5KB per instance

    def test_status_effect_model_memory_usage(self):
        """Test memory usage for StatusEffect model specifically."""
        profiler = MemoryProfiler()

        result = profiler.measure_model_instantiation(
            StatusEffect,
            iterations=1000,
            effect_type=StatusEffectType.POISONED,
            duration=10,
            intensity=5,
            source="poison dart",
        )

        assert result["model_class"] == "StatusEffect"
        assert result["iterations"] == 1000
        assert result["memory_per_instance_bytes"] > 0

        # StatusEffect model should use reasonable memory
        assert result["memory_per_instance_bytes"] < 1000  # Less than 1KB per instance

    def test_health_response_model_memory_usage(self):
        """Test memory usage for HealthResponse model specifically."""
        profiler = MemoryProfiler()

        result = profiler.measure_model_instantiation(
            HealthResponse,
            iterations=100,
            status=HealthStatus.HEALTHY,
            timestamp="2025-01-01T00:00:00Z",
            uptime_seconds=12345.67,
            version="1.0.0",
            components={
                "server": {
                    "status": HealthStatus.HEALTHY,
                    "uptime_seconds": 12345.67,
                    "memory_usage_mb": 256.5,
                    "cpu_usage_percent": 15.2,
                },
                "database": {
                    "status": HealthStatus.HEALTHY,
                    "connection_count": 5,
                    "last_query_time_ms": 12.5,
                },
                "connections": {
                    "status": HealthStatus.HEALTHY,
                    "active_connections": 3,
                    "max_connections": 100,
                    "connection_rate_per_minute": 45.2,
                },
            },
            alerts=[],
        )

        assert result["model_class"] == "HealthResponse"
        assert result["iterations"] == 100
        assert result["memory_per_instance_bytes"] > 0

        # HealthResponse model should use reasonable memory
        assert result["memory_per_instance_bytes"] < 2000  # Less than 2KB per instance

    def test_memory_profiling_with_error_handling(self):
        """Test memory profiling with invalid model class."""
        profiler = MemoryProfiler()

        # Test with invalid model class
        class InvalidModel:
            def __init__(self, **kwargs):
                raise ValueError("Invalid model")

        with pytest.raises(ValueError, match="Invalid model"):
            profiler.measure_model_instantiation(InvalidModel, iterations=10)

    def test_memory_profiling_cleanup(self):
        """Test that memory profiling properly cleans up."""
        profiler = MemoryProfiler()

        # Get initial memory
        initial_memory = profiler.get_current_memory_usage()

        # Create and measure
        _result = profiler.measure_model_instantiation(  # noqa: F841 - Testing side effect
            Alias, iterations=1000, name="test", command="go north"
        )

        # Get memory after cleanup
        final_memory = profiler.get_current_memory_usage()

        # Memory should be similar (allowing for some variance)
        memory_diff = abs(final_memory - initial_memory)
        assert memory_diff < initial_memory * 0.1  # Less than 10% difference

    def test_memory_profiling_print_functions(self):
        """Test that print functions work without errors."""
        profiler = MemoryProfiler()

        # Test memory summary print
        profiler.print_memory_summary()  # Should not raise

        # Test model memory usage print
        result = profiler.measure_model_instantiation(Alias, iterations=100, name="test", command="go north")
        profiler.print_model_memory_usage(result)  # Should not raise

        # Test comparison results print
        results = profiler.compare_models_memory_usage([Alias], iterations=100, name="test", command="go north")
        profiler.print_comparison_results(results)  # Should not raise

    def test_memory_profiling_comprehensive_benchmark(self):
        """Test comprehensive memory benchmark."""
        from server.utils.memory_profiler import benchmark_model_memory_usage

        # This should run without errors
        results = benchmark_model_memory_usage()

        # Should return results for multiple models
        assert isinstance(results, dict)
        assert len(results) > 0

        # Should have statistics
        assert "_statistics" in results
        stats = results["_statistics"]
        assert stats["total_models"] > 0
