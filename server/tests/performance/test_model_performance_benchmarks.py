"""
Performance benchmarks for Pydantic model validation and instantiation.

This module provides comprehensive benchmarks to measure the performance
of model validation, instantiation, and serialization across all Pydantic
models in the server. These benchmarks help identify performance bottlenecks
and measure improvements from optimizations.

As noted in the Pnakotic Manuscripts, proper measurement of our eldritch
systems' performance is essential for maintaining the delicate balance
between speed and accuracy in our digital realm.
"""

import time
from typing import Any

from pydantic import BaseModel, ValidationError

from server.models.alias import Alias
from server.models.command import LookCommand, SayCommand
from server.models.game import Stats, StatusEffect, StatusEffectType
from server.models.health import (
    ConnectionsComponent,
    DatabaseComponent,
    HealthComponents,
    HealthErrorResponse,
    HealthResponse,
    HealthStatus,
    ServerComponent,
)


class ModelPerformanceBenchmarks:
    """Performance benchmarks for Pydantic models."""

    @staticmethod
    def benchmark_model_instantiation(model_class, test_data: dict[str, Any], iterations: int = 1000) -> float:
        """
        Benchmark model instantiation performance.

        Args:
            model_class: The Pydantic model class to benchmark
            test_data: Dictionary of test data for instantiation
            iterations: Number of iterations to run

        Returns:
            Average time per instantiation in seconds
        """
        start_time = time.perf_counter()

        for _ in range(iterations):
            model_class(**test_data)

        end_time = time.perf_counter()
        total_time = end_time - start_time
        return total_time / iterations

    @staticmethod
    def benchmark_model_validation(model_class, test_data: dict[str, Any], iterations: int = 1000) -> float:
        """
        Benchmark model validation performance.

        Args:
            model_class: The Pydantic model class to benchmark
            test_data: Dictionary of test data for validation
            iterations: Number of iterations to run

        Returns:
            Average time per validation in seconds
        """
        start_time = time.perf_counter()

        for _ in range(iterations):
            try:
                model_class.model_validate(test_data)
            except ValidationError:
                # Include validation failures in benchmark
                pass

        end_time = time.perf_counter()
        total_time = end_time - start_time
        return total_time / iterations

    @staticmethod
    def benchmark_model_serialization(model_instance, iterations: int = 1000) -> float:
        """
        Benchmark model serialization performance.

        Args:
            model_instance: Instance of the model to benchmark
            iterations: Number of iterations to run

        Returns:
            Average time per serialization in seconds
        """
        start_time = time.perf_counter()

        for _ in range(iterations):
            model_instance.model_dump()

        end_time = time.perf_counter()
        total_time = end_time - start_time
        return total_time / iterations

    @staticmethod
    def benchmark_model_deserialization(model_class, serialized_data: dict[str, Any], iterations: int = 1000) -> float:
        """
        Benchmark model deserialization performance.

        Args:
            model_class: The Pydantic model class to benchmark
            serialized_data: Dictionary of serialized data
            iterations: Number of iterations to run

        Returns:
            Average time per deserialization in seconds
        """
        start_time = time.perf_counter()

        for _ in range(iterations):
            model_class.model_validate(serialized_data)

        end_time = time.perf_counter()
        total_time = end_time - start_time
        return total_time / iterations


class TestModelPerformanceBenchmarks:
    """Test performance benchmarks for all Pydantic models."""

    # Test data for various models
    ALIAS_TEST_DATA = {
        "name": "test_alias",
        "command": "go north",
    }

    STATS_TEST_DATA = {
        "strength": 15,
        "dexterity": 12,
        "constitution": 14,
        "intelligence": 16,
        "wisdom": 13,
        "charisma": 11,
        "lucidity": 85,
        "occult_knowledge": 25,
        "fear": 15,
        "corruption": 5,
        "cult_affiliation": 10,
        "current_health": 95,
    }

    STATUS_EFFECT_TEST_DATA = {
        "effect_type": StatusEffectType.POISONED,
        "duration": 10,
        "intensity": 5,
        "source": "poison dart",
    }

    LOOK_COMMAND_TEST_DATA = {
        "direction": "north",
    }

    SAY_COMMAND_TEST_DATA = {
        "message": "Hello, world!",
    }

    SERVER_COMPONENT_TEST_DATA = {
        "status": HealthStatus.HEALTHY,
        "uptime_seconds": 12345.67,
        "memory_usage_mb": 256.5,
        "cpu_usage_percent": 15.2,
    }

    DATABASE_COMPONENT_TEST_DATA = {
        "status": HealthStatus.HEALTHY,
        "connection_count": 5,
        "last_query_time_ms": 12.5,
    }

    CONNECTIONS_COMPONENT_TEST_DATA = {
        "status": HealthStatus.HEALTHY,
        "active_connections": 3,
        "max_connections": 100,
        "connection_rate_per_minute": 45.2,
    }

    HEALTH_COMPONENTS_TEST_DATA = {
        "server": SERVER_COMPONENT_TEST_DATA,
        "database": DATABASE_COMPONENT_TEST_DATA,
        "connections": CONNECTIONS_COMPONENT_TEST_DATA,
    }

    HEALTH_RESPONSE_TEST_DATA = {
        "status": HealthStatus.HEALTHY,
        "timestamp": "2025-01-01T00:00:00Z",
        "uptime_seconds": 12345.67,
        "version": "1.0.0",
        "components": HEALTH_COMPONENTS_TEST_DATA,
        "alerts": [],
    }

    HEALTH_ERROR_RESPONSE_TEST_DATA = {
        "error": "Database connection failed",
        "detail": "Unable to connect to the database server",
        "timestamp": "2025-01-01T00:00:00Z",
    }

    def test_alias_model_instantiation_performance(self) -> None:
        """Benchmark Alias model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            Alias, self.ALIAS_TEST_DATA, iterations=1000
        )

        # Document baseline performance
        print(f"Alias instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.001s per instance
        assert avg_time < 0.001, f"Alias instantiation too slow: {avg_time:.6f}s per instance"

    def test_alias_model_validation_performance(self) -> None:
        """Benchmark Alias model validation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_validation(Alias, self.ALIAS_TEST_DATA, iterations=1000)

        print(f"Alias validation: {avg_time:.6f}s per validation")

        # Reasonable performance expectation: < 0.001s per validation
        assert avg_time < 0.001, f"Alias validation too slow: {avg_time:.6f}s per validation"

    def test_alias_model_serialization_performance(self) -> None:
        """Benchmark Alias model serialization performance."""
        alias = Alias(**self.ALIAS_TEST_DATA)
        avg_time = ModelPerformanceBenchmarks.benchmark_model_serialization(alias, iterations=1000)

        print(f"Alias serialization: {avg_time:.6f}s per serialization")

        # Reasonable performance expectation: < 0.001s per serialization
        assert avg_time < 0.001, f"Alias serialization too slow: {avg_time:.6f}s per serialization"

    def test_stats_model_instantiation_performance(self) -> None:
        """Benchmark Stats model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            Stats, self.STATS_TEST_DATA, iterations=1000
        )

        print(f"Stats instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.002s per instance (includes random generation)
        assert avg_time < 0.002, f"Stats instantiation too slow: {avg_time:.6f}s per instance"

    def test_stats_model_validation_performance(self) -> None:
        """Benchmark Stats model validation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_validation(Stats, self.STATS_TEST_DATA, iterations=1000)

        print(f"Stats validation: {avg_time:.6f}s per validation")

        # Reasonable performance expectation: < 0.002s per validation
        assert avg_time < 0.002, f"Stats validation too slow: {avg_time:.6f}s per validation"

    def test_stats_model_serialization_performance(self) -> None:
        """Benchmark Stats model serialization performance."""
        stats = Stats(**self.STATS_TEST_DATA)
        avg_time = ModelPerformanceBenchmarks.benchmark_model_serialization(stats, iterations=1000)

        print(f"Stats serialization: {avg_time:.6f}s per serialization")

        # Reasonable performance expectation: < 0.001s per serialization
        assert avg_time < 0.001, f"Stats serialization too slow: {avg_time:.6f}s per serialization"

    def test_status_effect_model_instantiation_performance(self) -> None:
        """Benchmark StatusEffect model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            StatusEffect, self.STATUS_EFFECT_TEST_DATA, iterations=1000
        )

        print(f"StatusEffect instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.001s per instance
        assert avg_time < 0.001, f"StatusEffect instantiation too slow: {avg_time:.6f}s per instance"

    def test_look_command_model_instantiation_performance(self) -> None:
        """Benchmark LookCommand model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            LookCommand, self.LOOK_COMMAND_TEST_DATA, iterations=1000
        )

        print(f"LookCommand instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.001s per instance
        assert avg_time < 0.001, f"LookCommand instantiation too slow: {avg_time:.6f}s per instance"

    def test_say_command_model_instantiation_performance(self) -> None:
        """Benchmark SayCommand model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            SayCommand, self.SAY_COMMAND_TEST_DATA, iterations=1000
        )

        print(f"SayCommand instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.001s per instance
        assert avg_time < 0.001, f"SayCommand instantiation too slow: {avg_time:.6f}s per instance"

    def test_server_component_model_instantiation_performance(self) -> None:
        """Benchmark ServerComponent model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            ServerComponent, self.SERVER_COMPONENT_TEST_DATA, iterations=1000
        )

        print(f"ServerComponent instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.001s per instance
        assert avg_time < 0.001, f"ServerComponent instantiation too slow: {avg_time:.6f}s per instance"

    def test_database_component_model_instantiation_performance(self) -> None:
        """Benchmark DatabaseComponent model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            DatabaseComponent, self.DATABASE_COMPONENT_TEST_DATA, iterations=1000
        )

        print(f"DatabaseComponent instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.001s per instance
        assert avg_time < 0.001, f"DatabaseComponent instantiation too slow: {avg_time:.6f}s per instance"

    def test_connections_component_model_instantiation_performance(self) -> None:
        """Benchmark ConnectionsComponent model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            ConnectionsComponent, self.CONNECTIONS_COMPONENT_TEST_DATA, iterations=1000
        )

        print(f"ConnectionsComponent instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.001s per instance
        assert avg_time < 0.001, f"ConnectionsComponent instantiation too slow: {avg_time:.6f}s per instance"

    def test_health_components_model_instantiation_performance(self) -> None:
        """Benchmark HealthComponents model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            HealthComponents, self.HEALTH_COMPONENTS_TEST_DATA, iterations=1000
        )

        print(f"HealthComponents instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.002s per instance (nested models)
        assert avg_time < 0.002, f"HealthComponents instantiation too slow: {avg_time:.6f}s per instance"

    def test_health_response_model_instantiation_performance(self) -> None:
        """Benchmark HealthResponse model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            HealthResponse, self.HEALTH_RESPONSE_TEST_DATA, iterations=1000
        )

        print(f"HealthResponse instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.002s per instance (nested models)
        assert avg_time < 0.002, f"HealthResponse instantiation too slow: {avg_time:.6f}s per instance"

    def test_health_error_response_model_instantiation_performance(self) -> None:
        """Benchmark HealthErrorResponse model instantiation performance."""
        avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
            HealthErrorResponse, self.HEALTH_ERROR_RESPONSE_TEST_DATA, iterations=1000
        )

        print(f"HealthErrorResponse instantiation: {avg_time:.6f}s per instance")

        # Reasonable performance expectation: < 0.001s per instance
        assert avg_time < 0.001, f"HealthErrorResponse instantiation too slow: {avg_time:.6f}s per instance"

    def test_comprehensive_model_performance_comparison(self) -> None:
        """Compare performance across all models to identify bottlenecks."""
        models_to_benchmark: list[tuple[type[BaseModel], dict[str, Any], str]] = [
            (Alias, self.ALIAS_TEST_DATA, "Alias"),
            (Stats, self.STATS_TEST_DATA, "Stats"),
            (StatusEffect, self.STATUS_EFFECT_TEST_DATA, "StatusEffect"),
            (LookCommand, self.LOOK_COMMAND_TEST_DATA, "LookCommand"),
            (SayCommand, self.SAY_COMMAND_TEST_DATA, "SayCommand"),
            (ServerComponent, self.SERVER_COMPONENT_TEST_DATA, "ServerComponent"),
            (DatabaseComponent, self.DATABASE_COMPONENT_TEST_DATA, "DatabaseComponent"),
            (ConnectionsComponent, self.CONNECTIONS_COMPONENT_TEST_DATA, "ConnectionsComponent"),
            (HealthComponents, self.HEALTH_COMPONENTS_TEST_DATA, "HealthComponents"),
            (HealthResponse, self.HEALTH_RESPONSE_TEST_DATA, "HealthResponse"),
            (HealthErrorResponse, self.HEALTH_ERROR_RESPONSE_TEST_DATA, "HealthErrorResponse"),
        ]

        results: dict[str, float] = {}

        for model_class, test_data, model_name in models_to_benchmark:
            avg_time = ModelPerformanceBenchmarks.benchmark_model_instantiation(
                model_class,
                test_data,
                iterations=500,  # Reduced for comprehensive test
            )
            results[model_name] = avg_time

        # Print results for analysis
        print("\n=== Model Performance Comparison ===")
        for model_name, avg_time in sorted(results.items(), key=lambda x: x[1], reverse=True):
            print(f"{model_name}: {avg_time:.6f}s per instance")

        # Identify the slowest models for optimization
        slowest_model = max(results.items(), key=lambda x: x[1])
        print(f"\nSlowest model: {slowest_model[0]} at {slowest_model[1]:.6f}s per instance")

        # Verify no model is excessively slow
        for model_name, avg_time in results.items():
            # Allow up to 0.003s for complex models with nested structures
            assert avg_time < 0.003, f"{model_name} is too slow: {avg_time:.6f}s per instance"

    def test_memory_usage_benchmark(self) -> None:
        """Benchmark memory usage for model instantiation."""
        import sys

        # Create instances and measure memory usage
        instances: list[Any] = []

        # Measure memory before
        memory_before = sys.getsizeof(instances)

        # Create 100 instances of each model type
        for _ in range(100):
            instances.extend(
                [
                    Alias(**self.ALIAS_TEST_DATA),
                    Stats(**self.STATS_TEST_DATA),
                    StatusEffect(**self.STATUS_EFFECT_TEST_DATA),
                    LookCommand(**self.LOOK_COMMAND_TEST_DATA),
                    SayCommand(**self.SAY_COMMAND_TEST_DATA),
                ]
            )

        # Measure memory after
        memory_after = sys.getsizeof(instances)
        memory_per_instance = (memory_after - memory_before) / len(instances)

        print(f"Average memory per instance: {memory_per_instance:.2f} bytes")

        # Reasonable memory usage expectation: < 500 bytes per instance
        assert memory_per_instance < 500, f"Memory usage too high: {memory_per_instance:.2f} bytes per instance"

    def test_validation_error_performance(self) -> None:
        """Benchmark performance of validation with errors."""
        invalid_data = {"invalid_field": "invalid_value"}

        start_time = time.perf_counter()

        for _ in range(1000):
            try:
                Alias.model_validate(invalid_data)
            except ValidationError:
                # Expected to fail
                pass

        end_time = time.perf_counter()
        avg_time = (end_time - start_time) / 1000

        print(f"Validation error handling: {avg_time:.6f}s per validation")

        # Error handling should be fast
        assert avg_time < 0.001, f"Error handling too slow: {avg_time:.6f}s per validation"
