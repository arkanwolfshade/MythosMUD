"""
Unit tests for memory profiler.

Tests the MemoryProfiler class for analyzing model memory usage.
"""

from unittest.mock import MagicMock, patch

import pytest
from pydantic import BaseModel

from server.utils.memory_profiler import MemoryProfiler


class SampleModel(BaseModel):
    """Simple test model for memory profiling."""
    name: str
    value: int


@pytest.fixture
def memory_profiler():
    """Create a MemoryProfiler instance."""
    return MemoryProfiler()


def test_memory_profiler_initialization(memory_profiler):
    """Test MemoryProfiler initialization."""
    assert memory_profiler.process is not None
    assert memory_profiler.baseline_memory is None
    assert memory_profiler.measurements == []


def test_start_profiling(memory_profiler):
    """Test start_profiling sets baseline."""
    memory_profiler.start_profiling()
    assert memory_profiler.baseline_memory is not None
    assert memory_profiler.baseline_memory > 0


def test_stop_profiling(memory_profiler):
    """Test stop_profiling stops tracemalloc."""
    memory_profiler.start_profiling()
    memory_profiler.stop_profiling()
    # Should not raise exception


def test_get_current_memory_usage(memory_profiler):
    """Test get_current_memory_usage returns positive value."""
    usage = memory_profiler.get_current_memory_usage()
    assert usage > 0


def test_get_memory_delta_no_baseline(memory_profiler):
    """Test get_memory_delta returns 0 when no baseline."""
    delta = memory_profiler.get_memory_delta()
    assert delta == 0


def test_get_memory_delta_with_baseline(memory_profiler):
    """Test get_memory_delta returns difference from baseline."""
    memory_profiler.start_profiling()
    baseline = memory_profiler.baseline_memory
    delta = memory_profiler.get_memory_delta()
    # Delta should be small or zero right after baseline
    assert isinstance(delta, int)


def test_measure_model_instantiation(memory_profiler):
    """Test measure_model_instantiation measures memory usage."""
    result = memory_profiler.measure_model_instantiation(SampleModel, iterations=10, name="test", value=42)
    
    assert result["model_class"] == "SampleModel"
    assert result["iterations"] == 10
    assert "memory_delta_bytes" in result
    assert "memory_per_instance_bytes" in result
    assert "memory_per_instance_kb" in result
    assert "memory_per_instance_mb" in result
    assert "peak_memory_bytes" in result
    assert "current_memory_bytes" in result


def test_measure_model_instantiation_zero_iterations(memory_profiler):
    """Test measure_model_instantiation with zero iterations."""
    result = memory_profiler.measure_model_instantiation(SampleModel, iterations=0, name="test", value=42)
    
    assert result["iterations"] == 0
    assert result["memory_per_instance_bytes"] == 0


def test_measure_model_serialization(memory_profiler):
    """Test measure_model_serialization measures memory usage."""
    instances = [SampleModel(name=f"test{i}", value=i) for i in range(5)]
    
    result = memory_profiler.measure_model_serialization(instances, iterations=10)
    
    assert result["instances_count"] == 5
    assert result["iterations"] == 10
    assert result["total_serializations"] == 50
    assert "memory_delta_bytes" in result
    assert "memory_per_serialization_bytes" in result
    assert "memory_per_serialization_kb" in result


def test_measure_model_deserialization(memory_profiler):
    """Test measure_model_deserialization measures memory usage."""
    serialized_data = [{"name": f"test{i}", "value": i} for i in range(5)]
    
    result = memory_profiler.measure_model_deserialization(SampleModel, serialized_data, iterations=10)
    
    assert result["model_class"] == "SampleModel"
    assert result["data_count"] == 5
    assert result["iterations"] == 10
    assert result["total_deserializations"] == 50
    assert "memory_delta_bytes" in result
    assert "memory_per_deserialization_bytes" in result
    assert "memory_per_deserialization_kb" in result


def test_compare_models_memory_usage(memory_profiler):
    """Test compare_models_memory_usage compares multiple models."""
    class Model1(BaseModel):
        field1: str
    
    class Model2(BaseModel):
        field2: int
    
    result = memory_profiler.compare_models_memory_usage(
        [Model1, Model2],
        iterations=10,
        Model1={"field1": "test"},
        Model2={"field2": 42},
    )
    
    assert "Model1" in result
    assert "Model2" in result
    assert "_statistics" in result
    assert result["_statistics"]["total_models"] == 2


def test_get_memory_usage_summary(memory_profiler):
    """Test get_memory_usage_summary returns summary."""
    summary = memory_profiler.get_memory_usage_summary()
    
    assert "rss_bytes" in summary
    assert "vms_bytes" in summary
    assert "rss_mb" in summary
    assert "vms_mb" in summary
    assert "percent" in summary
    assert "available_mb" in summary
    assert "total_mb" in summary
    assert summary["rss_bytes"] > 0
    assert summary["rss_mb"] > 0


def test_print_memory_summary(memory_profiler, capsys):
    """Test print_memory_summary prints formatted summary."""
    memory_profiler.print_memory_summary()
    captured = capsys.readouterr()
    assert "Memory Usage Summary" in captured.out
    assert "RSS Memory" in captured.out
    assert "VMS Memory" in captured.out


def test_print_model_memory_usage(memory_profiler, capsys):
    """Test print_model_memory_usage prints formatted results."""
    result = {
        "model_class": "SampleModel",
        "iterations": 10,
        "memory_delta_bytes": 1024,
        "memory_per_instance_bytes": 102.4,
        "memory_per_instance_kb": 0.1,
        "peak_memory_bytes": 2048,
    }
    
    memory_profiler.print_model_memory_usage(result)
    captured = capsys.readouterr()
    assert "SampleModel Memory Usage" in captured.out
    assert "Iterations" in captured.out


def test_print_model_memory_usage_with_error(memory_profiler, capsys):
    """Test print_model_memory_usage handles error results."""
    result = {"error": "Test error"}
    memory_profiler.print_model_memory_usage(result)
    captured = capsys.readouterr()
    assert "Error" in captured.out


def test_print_comparison_results(memory_profiler, capsys):
    """Test print_comparison_results prints formatted comparison."""
    results = {
        "Model1": {
            "model_class": "Model1",
            "iterations": 10,
            "memory_delta_bytes": 1024,
            "memory_per_instance_bytes": 102.4,
            "memory_per_instance_kb": 0.1,
            "peak_memory_bytes": 2048,
        },
        "_statistics": {
            "total_models": 1,
            "min_memory_bytes": 102.4,
            "max_memory_bytes": 102.4,
            "avg_memory_bytes": 102.4,
        },
    }
    
    memory_profiler.print_comparison_results(results)
    captured = capsys.readouterr()
    assert "Model Memory Usage Comparison" in captured.out
    assert "Comparison Statistics" in captured.out
