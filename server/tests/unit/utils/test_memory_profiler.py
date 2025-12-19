"""
Tests for memory profiler utilities.

This module tests memory profiling tools for analyzing Pydantic model memory usage.
"""

from unittest.mock import MagicMock, Mock, patch

import pytest
from pydantic import BaseModel

from server.utils.memory_profiler import MemoryProfiler, benchmark_model_memory_usage


class SimpleTestModel(BaseModel):
    """Simple test model for memory profiling tests."""

    name: str
    value: int = 0


class TestMemoryProfiler:
    """Test MemoryProfiler class."""

    def test_memory_profiler_init(self) -> None:
        """Test MemoryProfiler initialization."""
        profiler = MemoryProfiler()
        assert profiler.process is not None
        assert profiler.baseline_memory is None
        assert profiler.measurements == []

    def test_start_profiling(self) -> None:
        """Test start_profiling method."""
        profiler = MemoryProfiler()
        with patch("server.utils.memory_profiler.gc.collect") as mock_gc:
            with patch.object(profiler.process, "memory_info") as mock_memory_info:
                mock_memory_info.return_value = Mock(rss=1000000)
                with patch("server.utils.memory_profiler.tracemalloc.start") as mock_tracemalloc:
                    profiler.start_profiling()

                    mock_gc.assert_called_once()
                    mock_memory_info.assert_called_once()
                    mock_tracemalloc.assert_called_once()
                    assert profiler.baseline_memory == 1000000

    def test_stop_profiling(self) -> None:
        """Test stop_profiling method."""
        profiler = MemoryProfiler()
        with patch("server.utils.memory_profiler.tracemalloc.stop") as mock_tracemalloc:
            profiler.stop_profiling()
            mock_tracemalloc.assert_called_once()

    def test_get_current_memory_usage(self) -> None:
        """Test get_current_memory_usage method."""
        profiler = MemoryProfiler()
        with patch.object(profiler.process, "memory_info") as mock_memory_info:
            mock_memory_info.return_value = Mock(rss=2000000)
            result = profiler.get_current_memory_usage()
            assert result == 2000000

    def test_get_memory_delta_no_baseline(self) -> None:
        """Test get_memory_delta when baseline is None."""
        profiler = MemoryProfiler()
        profiler.baseline_memory = None
        assert profiler.get_memory_delta() == 0

    def test_get_memory_delta_with_baseline(self) -> None:
        """Test get_memory_delta with baseline set."""
        profiler = MemoryProfiler()
        profiler.baseline_memory = 1000000
        with patch.object(profiler.process, "memory_info") as mock_memory_info:
            mock_memory_info.return_value = Mock(rss=1500000)
            result = profiler.get_memory_delta()
            assert result == 500000

    def test_measure_model_instantiation(self) -> None:
        """Test measure_model_instantiation method."""
        profiler = MemoryProfiler()
        with patch.object(profiler, "start_profiling"):
            with patch.object(profiler, "stop_profiling"):
                with patch.object(profiler, "get_current_memory_usage", return_value=2000000):
                    with patch.object(profiler, "get_memory_delta", return_value=1000000):
                        with patch(
                            "server.utils.memory_profiler.tracemalloc.get_traced_memory", return_value=(500000, 1500000)
                        ):
                            with patch("server.utils.memory_profiler.gc.collect"):
                                profiler.baseline_memory = 1000000

                                result = profiler.measure_model_instantiation(
                                    SimpleTestModel, iterations=100, name="test", value=42
                                )

                                assert result["model_class"] == "SimpleTestModel"
                                assert result["iterations"] == 100
                                assert result["memory_delta_bytes"] == 1000000
                                assert result["memory_per_instance_bytes"] == 10000
                                assert result["peak_memory_bytes"] == 1500000
                                assert result["current_memory_bytes"] == 500000

    def test_measure_model_instantiation_zero_iterations(self) -> None:
        """Test measure_model_instantiation with zero iterations."""
        profiler = MemoryProfiler()
        with patch.object(profiler, "start_profiling"):
            with patch.object(profiler, "stop_profiling"):
                with patch.object(profiler, "get_current_memory_usage", return_value=2000000):
                    with patch.object(profiler, "get_memory_delta", return_value=0):
                        with patch("server.utils.memory_profiler.tracemalloc.get_traced_memory", return_value=(0, 0)):
                            with patch("server.utils.memory_profiler.gc.collect"):
                                profiler.baseline_memory = 1000000

                                result = profiler.measure_model_instantiation(
                                    SimpleTestModel, iterations=0, name="test", value=42
                                )

                                assert result["memory_per_instance_bytes"] == 0

    def test_measure_model_instantiation_exception_handling(self) -> None:
        """Test measure_model_instantiation handles exceptions."""
        profiler = MemoryProfiler()
        with patch.object(profiler, "start_profiling"):
            with patch.object(profiler, "stop_profiling"):
                with patch("server.utils.memory_profiler.gc.collect"):
                    profiler.baseline_memory = 1000000

                    with pytest.raises(ValueError):
                        profiler.measure_model_instantiation(SimpleTestModel, iterations=100, invalid_arg="test")

    def test_measure_model_serialization(self) -> None:
        """Test measure_model_serialization method."""
        profiler = MemoryProfiler()
        instances = [SimpleTestModel(name=f"test{i}", value=i) for i in range(10)]

        with patch.object(profiler, "start_profiling"):
            with patch.object(profiler, "stop_profiling"):
                with patch.object(profiler, "get_current_memory_usage", return_value=2000000):
                    with patch.object(profiler, "get_memory_delta", return_value=500000):
                        with patch("server.utils.memory_profiler.gc.collect"):
                            profiler.baseline_memory = 1000000

                            result = profiler.measure_model_serialization(instances, iterations=5)

                            assert result["instances_count"] == 10
                            assert result["iterations"] == 5
                            assert result["total_serializations"] == 50
                            assert result["memory_delta_bytes"] == 500000
                            assert result["memory_per_serialization_bytes"] == 10000

    def test_measure_model_serialization_zero_iterations(self) -> None:
        """Test measure_model_serialization with zero iterations."""
        profiler = MemoryProfiler()
        instances = [SimpleTestModel(name="test", value=1)]

        with patch.object(profiler, "start_profiling"):
            with patch.object(profiler, "stop_profiling"):
                with patch.object(profiler, "get_current_memory_usage", return_value=2000000):
                    with patch.object(profiler, "get_memory_delta", return_value=0):
                        with patch("server.utils.memory_profiler.gc.collect"):
                            profiler.baseline_memory = 1000000

                            result = profiler.measure_model_serialization(instances, iterations=0)

                            assert result["memory_per_serialization_bytes"] == 0

    def test_measure_model_deserialization(self) -> None:
        """Test measure_model_deserialization method."""
        profiler = MemoryProfiler()
        serialized_data = [{"name": f"test{i}", "value": i} for i in range(10)]

        with patch.object(profiler, "start_profiling"):
            with patch.object(profiler, "stop_profiling"):
                with patch.object(profiler, "get_current_memory_usage", return_value=2000000):
                    with patch.object(profiler, "get_memory_delta", return_value=300000):
                        with patch("server.utils.memory_profiler.gc.collect"):
                            profiler.baseline_memory = 1000000

                            result = profiler.measure_model_deserialization(
                                SimpleTestModel, serialized_data, iterations=3
                            )

                            assert result["model_class"] == "SimpleTestModel"
                            assert result["data_count"] == 10
                            assert result["iterations"] == 3
                            assert result["total_deserializations"] == 30
                            assert result["memory_delta_bytes"] == 300000
                            assert result["memory_per_deserialization_bytes"] == 10000

    def test_measure_model_deserialization_zero_iterations(self) -> None:
        """Test measure_model_deserialization with zero iterations."""
        profiler = MemoryProfiler()
        serialized_data = [{"name": "test", "value": 1}]

        with patch.object(profiler, "start_profiling"):
            with patch.object(profiler, "stop_profiling"):
                with patch.object(profiler, "get_current_memory_usage", return_value=2000000):
                    with patch.object(profiler, "get_memory_delta", return_value=0):
                        with patch("server.utils.memory_profiler.gc.collect"):
                            profiler.baseline_memory = 1000000

                            result = profiler.measure_model_deserialization(
                                SimpleTestModel, serialized_data, iterations=0
                            )

                            assert result["memory_per_deserialization_bytes"] == 0

    def test_compare_models_memory_usage(self) -> None:
        """Test compare_models_memory_usage method."""
        profiler = MemoryProfiler()

        with patch.object(profiler, "measure_model_instantiation") as mock_measure:
            mock_measure.return_value = {
                "model_class": "TestModel",
                "iterations": 100,
                "memory_per_instance_bytes": 1000,
            }

            result = profiler.compare_models_memory_usage(
                [SimpleTestModel], iterations=100, SimpleTestModel={"name": "test", "value": 1}
            )

            assert "SimpleTestModel" in result
            assert "_statistics" in result
            assert result["_statistics"]["total_models"] == 1
            assert result["_statistics"]["min_memory_bytes"] == 1000
            assert result["_statistics"]["max_memory_bytes"] == 1000
            assert result["_statistics"]["avg_memory_bytes"] == 1000

    def test_compare_models_memory_usage_with_error(self) -> None:
        """Test compare_models_memory_usage handles errors."""
        profiler = MemoryProfiler()

        with patch.object(profiler, "measure_model_instantiation", side_effect=ValueError("Test error")):
            result = profiler.compare_models_memory_usage([SimpleTestModel], iterations=100)

            assert "SimpleTestModel" in result
            assert "error" in result["SimpleTestModel"]

    def test_compare_models_memory_usage_multiple_models(self) -> None:
        """Test compare_models_memory_usage with multiple models."""
        profiler = MemoryProfiler()

        class Model1(BaseModel):
            field1: str

        class Model2(BaseModel):
            field2: int

        with patch.object(profiler, "measure_model_instantiation") as mock_measure:
            mock_measure.side_effect = [
                {"model_class": "Model1", "iterations": 100, "memory_per_instance_bytes": 500},
                {"model_class": "Model2", "iterations": 100, "memory_per_instance_bytes": 1500},
            ]

            result = profiler.compare_models_memory_usage(
                [Model1, Model2], iterations=100, Model1={"field1": "test"}, Model2={"field2": 42}
            )

            assert "Model1" in result
            assert "Model2" in result
            assert "_statistics" in result
            assert result["_statistics"]["min_memory_bytes"] == 500
            assert result["_statistics"]["max_memory_bytes"] == 1500
            assert result["_statistics"]["avg_memory_bytes"] == 1000

    def test_get_memory_usage_summary(self) -> None:
        """Test get_memory_usage_summary method."""
        profiler = MemoryProfiler()
        with patch.object(profiler.process, "memory_info") as mock_memory_info:
            mock_memory_info.return_value = Mock(rss=2000000, vms=3000000)
            with patch.object(profiler.process, "memory_percent", return_value=25.5):
                with patch("server.utils.memory_profiler.psutil.virtual_memory") as mock_virtual:
                    mock_virtual.return_value = Mock(available=8000000, total=10000000)

                    result = profiler.get_memory_usage_summary()

                    assert result["rss_bytes"] == 2000000
                    assert result["vms_bytes"] == 3000000
                    assert result["rss_mb"] == 2000000 / (1024 * 1024)
                    assert result["vms_mb"] == 3000000 / (1024 * 1024)
                    assert result["percent"] == 25.5
                    assert result["available_mb"] == 8000000 / (1024 * 1024)
                    assert result["total_mb"] == 10000000 / (1024 * 1024)

    def test_print_memory_summary(self) -> None:
        """Test print_memory_summary method."""
        profiler = MemoryProfiler()
        with patch.object(profiler, "get_memory_usage_summary") as mock_summary:
            mock_summary.return_value = {
                "rss_mb": 100.5,
                "vms_mb": 200.3,
                "percent": 15.2,
                "available_mb": 500.0,
                "total_mb": 1000.0,
            }
            with patch("builtins.print") as mock_print:
                profiler.print_memory_summary()

                assert mock_print.call_count >= 5
                print_calls = [str(call) for call in mock_print.call_args_list]
                assert any("RSS Memory" in str(call) for call in print_calls)
                assert any("VMS Memory" in str(call) for call in print_calls)

    def test_print_model_memory_usage(self) -> None:
        """Test print_model_memory_usage method."""
        profiler = MemoryProfiler()
        result = {
            "model_class": "TestModel",
            "iterations": 100,
            "memory_delta_bytes": 1000000,
            "memory_per_instance_bytes": 10000,
            "memory_per_instance_kb": 10.0,
            "peak_memory_bytes": 2000000,
        }

        with patch("builtins.print") as mock_print:
            profiler.print_model_memory_usage(result)

            assert mock_print.call_count >= 4
            print_calls = [str(call) for call in mock_print.call_args_list]
            assert any("TestModel" in str(call) for call in print_calls)
            assert any("Iterations" in str(call) for call in print_calls)

    def test_print_model_memory_usage_with_error(self) -> None:
        """Test print_model_memory_usage with error result."""
        profiler = MemoryProfiler()
        result = {"error": "Test error", "model_class": "TestModel"}

        with patch("builtins.print") as mock_print:
            profiler.print_model_memory_usage(result)

            mock_print.assert_called()
            print_calls = [str(call) for call in mock_print.call_args_list]
            assert any("Error" in str(call) for call in print_calls)

    def test_print_comparison_results(self) -> None:
        """Test print_comparison_results method."""
        profiler = MemoryProfiler()
        results = {
            "Model1": {
                "model_class": "Model1",
                "iterations": 100,
                "memory_delta_bytes": 500000,
                "memory_per_instance_bytes": 5000,
                "memory_per_instance_kb": 5.0,
                "peak_memory_bytes": 1000000,
            },
            "Model2": {
                "model_class": "Model2",
                "iterations": 100,
                "memory_delta_bytes": 1500000,
                "memory_per_instance_bytes": 15000,
                "memory_per_instance_kb": 15.0,
                "peak_memory_bytes": 2000000,
            },
            "_statistics": {
                "total_models": 2,
                "min_memory_bytes": 5000,
                "max_memory_bytes": 15000,
                "avg_memory_bytes": 10000,
            },
        }

        with patch.object(profiler, "print_model_memory_usage") as mock_print_model:
            with patch("builtins.print") as mock_print:
                profiler.print_comparison_results(results)

                assert mock_print_model.call_count == 2
                assert mock_print.call_count >= 4
                print_calls = [str(call) for call in mock_print.call_args_list]
                assert any("Comparison Statistics" in str(call) for call in print_calls)


class TestBenchmarkModelMemoryUsage:
    """Test benchmark_model_memory_usage function."""

    @patch("server.utils.memory_profiler.MemoryProfiler")
    def test_benchmark_model_memory_usage(self, mock_profiler_class):
        """Test benchmark_model_memory_usage function."""
        mock_profiler = MagicMock()
        mock_profiler_class.return_value = mock_profiler
        mock_profiler.compare_models_memory_usage.return_value = {"test": "result"}

        with patch("builtins.print"):
            result = benchmark_model_memory_usage()

            assert result == {"test": "result"}
            mock_profiler.start_profiling.assert_not_called()  # Called inside compare_models_memory_usage
            mock_profiler.print_comparison_results.assert_called_once()
            mock_profiler.print_memory_summary.assert_called()
