"""
Memory profiling utilities for MythosMUD models.

This module provides comprehensive memory profiling tools for analyzing
memory usage of Pydantic models and identifying optimization opportunities.

As noted in the Pnakotic Manuscripts: "The ancient ones consume memory
like the void consumes light. We must measure our own consumption carefully."
"""

import gc
import tracemalloc
from typing import Any

import psutil
from pydantic import BaseModel


class MemoryProfiler:
    """Memory profiler for analyzing model memory usage."""

    def __init__(self) -> None:
        """Initialize the memory profiler."""
        self.process = psutil.Process()
        self.baseline_memory: int | None = None
        self.measurements: list[dict[str, Any]] = []

    def start_profiling(self) -> None:
        """Start memory profiling."""
        gc.collect()  # Clean up before measuring
        self.baseline_memory = self.process.memory_info().rss
        tracemalloc.start()

    def stop_profiling(self) -> None:
        """Stop memory profiling."""
        tracemalloc.stop()

    def get_current_memory_usage(self) -> int:
        """Get current memory usage in bytes."""
        return self.process.memory_info().rss

    def get_memory_delta(self) -> int:
        """Get memory delta from baseline."""
        if self.baseline_memory is None:
            return 0
        return self.get_current_memory_usage() - self.baseline_memory

    def measure_model_instantiation(self, model_class: type, iterations: int = 1000, **kwargs) -> dict[str, Any]:
        """
        Measure memory usage for model instantiation.

        Args:
            model_class: The Pydantic model class to measure
            iterations: Number of instances to create
            **kwargs: Arguments to pass to model constructor

        Returns:
            Dict with memory usage statistics
        """
        self.start_profiling()

        try:
            # Create instances
            instances = []
            for _ in range(iterations):
                instance = model_class(**kwargs)
                instances.append(instance)

            # Measure memory usage (memory_after triggers measurement snapshot)
            _memory_after = self.get_current_memory_usage()  # noqa: F841  # pylint: disable=unused-variable  # pylint: disable=unused-variable
            memory_delta = self.get_memory_delta()
            memory_per_instance = memory_delta / iterations if iterations > 0 else 0

            # Get tracemalloc statistics
            current, peak = tracemalloc.get_traced_memory()

            # Clean up
            del instances
            gc.collect()

            return {
                "model_class": model_class.__name__,
                "iterations": iterations,
                "memory_delta_bytes": memory_delta,
                "memory_per_instance_bytes": memory_per_instance,
                "memory_per_instance_kb": memory_per_instance / 1024,
                "memory_per_instance_mb": memory_per_instance / (1024 * 1024),
                "peak_memory_bytes": peak,
                "current_memory_bytes": current,
            }
        except Exception as e:
            # Clean up on error
            gc.collect()
            raise e
        finally:
            self.stop_profiling()

    def measure_model_serialization(self, instances: list[Any], iterations: int = 100) -> dict[str, Any]:
        """
        Measure memory usage for model serialization.

        Args:
            instances: List of model instances to serialize
            iterations: Number of serialization iterations

        Returns:
            Dict with memory usage statistics
        """
        self.start_profiling()

        # Serialize instances multiple times
        serialized_data = []
        for _ in range(iterations):
            for instance in instances:
                serialized_data.append(instance.model_dump())

        # Measure memory usage (memory_after triggers measurement snapshot)
        _memory_after = self.get_current_memory_usage()  # noqa: F841  # pylint: disable=unused-variable
        memory_delta = self.get_memory_delta()
        memory_per_serialization = memory_delta / (len(instances) * iterations) if iterations > 0 else 0

        self.stop_profiling()

        # Clean up
        del serialized_data
        gc.collect()

        return {
            "instances_count": len(instances),
            "iterations": iterations,
            "total_serializations": len(instances) * iterations,
            "memory_delta_bytes": memory_delta,
            "memory_per_serialization_bytes": memory_per_serialization,
            "memory_per_serialization_kb": memory_per_serialization / 1024,
        }

    def measure_model_deserialization(
        self, model_class: type[BaseModel], serialized_data: list[dict], iterations: int = 100
    ) -> dict[str, Any]:
        """
        Measure memory usage for model deserialization.

        Args:
            model_class: The Pydantic model class to deserialize
            serialized_data: List of serialized data dictionaries
            iterations: Number of deserialization iterations

        Returns:
            Dict with memory usage statistics
        """
        self.start_profiling()

        # Deserialize instances multiple times
        deserialized_instances = []
        for _ in range(iterations):
            for data in serialized_data:
                # Cast is necessary because mypy doesn't recognize class methods on type[BaseModel]
                instance = model_class.model_validate(data)
                deserialized_instances.append(instance)

        # Measure memory usage (memory_after triggers measurement snapshot)
        _memory_after = self.get_current_memory_usage()  # noqa: F841  # pylint: disable=unused-variable
        memory_delta = self.get_memory_delta()
        memory_per_deserialization = memory_delta / (len(serialized_data) * iterations) if iterations > 0 else 0

        self.stop_profiling()

        # Clean up
        del deserialized_instances
        gc.collect()

        return {
            "model_class": model_class.__name__,
            "data_count": len(serialized_data),
            "iterations": iterations,
            "total_deserializations": len(serialized_data) * iterations,
            "memory_delta_bytes": memory_delta,
            "memory_per_deserialization_bytes": memory_per_deserialization,
            "memory_per_deserialization_kb": memory_per_deserialization / 1024,
        }

    def compare_models_memory_usage(
        self, model_classes: list[type], iterations: int = 1000, **kwargs
    ) -> dict[str, Any]:
        """
        Compare memory usage across multiple model classes.

        Args:
            model_classes: List of model classes to compare
            iterations: Number of instances to create for each model
            **kwargs: Arguments to pass to model constructors

        Returns:
            Dict with comparison statistics
        """
        results = {}

        for model_class in model_classes:
            try:
                # Only pass relevant test data for this specific model
                model_name = model_class.__name__
                model_test_data = kwargs.get(model_name, {})

                result = self.measure_model_instantiation(model_class, iterations, **model_test_data)
                results[model_class.__name__] = result
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Model profiling errors unpredictable, must record error and continue
                results[model_class.__name__] = {"error": str(e)}

        # Calculate statistics
        memory_usage = [r["memory_per_instance_bytes"] for r in results.values() if "memory_per_instance_bytes" in r]

        if memory_usage:
            results["_statistics"] = {
                "min_memory_bytes": min(memory_usage),
                "max_memory_bytes": max(memory_usage),
                "avg_memory_bytes": sum(memory_usage) / len(memory_usage),
                "total_models": len(memory_usage),
            }

        return results

    def get_memory_usage_summary(self) -> dict[str, Any]:
        """Get a summary of current memory usage."""
        memory_info = self.process.memory_info()
        return {
            "rss_bytes": memory_info.rss,
            "vms_bytes": memory_info.vms,
            "rss_mb": memory_info.rss / (1024 * 1024),
            "vms_mb": memory_info.vms / (1024 * 1024),
            "percent": self.process.memory_percent(),
            "available_mb": psutil.virtual_memory().available / (1024 * 1024),
            "total_mb": psutil.virtual_memory().total / (1024 * 1024),
        }

    def print_memory_summary(self) -> None:
        """Print a formatted memory usage summary."""
        summary = self.get_memory_usage_summary()
        print("\n=== Memory Usage Summary ===")
        print(f"RSS Memory: {summary['rss_mb']:.2f} MB")
        print(f"VMS Memory: {summary['vms_mb']:.2f} MB")
        print(f"Memory Percent: {summary['percent']:.2f}%")
        print(f"Available Memory: {summary['available_mb']:.2f} MB")
        print(f"Total Memory: {summary['total_mb']:.2f} MB")

    def print_model_memory_usage(self, result: dict[str, Any]) -> None:
        """Print formatted model memory usage results."""
        if "error" in result:
            print(f"Error measuring {result.get('model_class', 'Unknown')}: {result['error']}")
            return

        print(f"\n=== {result['model_class']} Memory Usage ===")
        print(f"Iterations: {result['iterations']}")
        print(f"Memory Delta: {result['memory_delta_bytes']} bytes ({result['memory_delta_bytes'] / 1024:.2f} KB)")
        print(
            f"Memory per Instance: {result['memory_per_instance_bytes']:.2f} bytes ({result['memory_per_instance_kb']:.2f} KB)"
        )
        print(f"Peak Memory: {result['peak_memory_bytes']} bytes ({result['peak_memory_bytes'] / 1024:.2f} KB)")

    def print_comparison_results(self, results: dict[str, Any]) -> None:
        """Print formatted comparison results."""
        print("\n=== Model Memory Usage Comparison ===")

        # Print individual results
        for model_name, result in results.items():
            if model_name.startswith("_"):
                continue
            self.print_model_memory_usage(result)

        # Print statistics
        if "_statistics" in results:
            stats = results["_statistics"]
            print("\n=== Comparison Statistics ===")
            print(f"Models Compared: {stats['total_models']}")
            print(f"Min Memory per Instance: {stats['min_memory_bytes']:.2f} bytes")
            print(f"Max Memory per Instance: {stats['max_memory_bytes']:.2f} bytes")
            print(f"Average Memory per Instance: {stats['avg_memory_bytes']:.2f} bytes")


def benchmark_model_memory_usage() -> dict[str, Any]:
    """Benchmark memory usage for all major models."""
    from server.models.alias import Alias
    from server.models.command import LookCommand, SayCommand
    from server.models.game import Stats, StatusEffect, StatusEffectType
    from server.models.health import HealthResponse, HealthStatus

    profiler = MemoryProfiler()

    print("Starting memory usage benchmark...")
    profiler.print_memory_summary()

    # Test data for different models
    test_data = {
        "Alias": {"name": "test_alias", "command": "go north"},
        "SayCommand": {"message": "Hello, world!"},
        "LookCommand": {"direction": "north"},
        "Stats": {},
        "StatusEffect": {
            "effect_type": StatusEffectType.POISONED,
            "duration": 10,
            "intensity": 5,
            "source": "poison dart",
        },
        "HealthResponse": {
            "status": HealthStatus.HEALTHY,
            "timestamp": "2025-01-01T00:00:00Z",
            "uptime_seconds": 12345.67,
            "version": "1.0.0",
            "components": {
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
            "alerts": [],
        },
    }

    # Compare memory usage
    model_classes = [Alias, SayCommand, LookCommand, Stats, StatusEffect, HealthResponse]
    results = profiler.compare_models_memory_usage(model_classes, iterations=1000, **test_data)  # type: ignore[arg-type]

    profiler.print_comparison_results(results)
    profiler.print_memory_summary()

    return results


if __name__ == "__main__":
    benchmark_model_memory_usage()
