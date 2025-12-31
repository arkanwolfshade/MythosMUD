"""
Unit tests for memory profiler utilities.

Tests the MemoryProfiler class methods.
"""

from unittest.mock import MagicMock, patch

from pydantic import BaseModel

from server.utils.memory_profiler import MemoryProfiler


class SampleModel(BaseModel):
    """Test Pydantic model for memory profiling tests."""

    name: str
    value: int = 0


def test_memory_profiler_init():
    """Test MemoryProfiler initialization."""
    profiler = MemoryProfiler()

    assert profiler.baseline_memory is None
    assert profiler.measurements == []


def test_memory_profiler_start_profiling():
    """Test MemoryProfiler.start_profiling() sets baseline."""
    profiler = MemoryProfiler()

    with (
        patch("server.utils.memory_profiler.gc.collect"),
        patch("server.utils.memory_profiler.tracemalloc.start"),
        patch.object(profiler.process, "memory_info", return_value=MagicMock(rss=1000)),
    ):
        profiler.start_profiling()

        assert profiler.baseline_memory == 1000


def test_memory_profiler_stop_profiling():
    """Test MemoryProfiler.stop_profiling() stops tracemalloc."""
    profiler = MemoryProfiler()

    with patch("server.utils.memory_profiler.tracemalloc.stop") as mock_stop:
        profiler.stop_profiling()

        mock_stop.assert_called_once()


def test_memory_profiler_get_current_memory_usage():
    """Test MemoryProfiler.get_current_memory_usage() returns RSS."""
    profiler = MemoryProfiler()

    with patch.object(profiler.process, "memory_info", return_value=MagicMock(rss=2000)):
        usage = profiler.get_current_memory_usage()

        assert usage == 2000


def test_memory_profiler_get_memory_delta():
    """Test MemoryProfiler.get_memory_delta() calculates difference."""
    profiler = MemoryProfiler()
    profiler.baseline_memory = 1000

    with patch.object(profiler.process, "memory_info", return_value=MagicMock(rss=1500)):
        delta = profiler.get_memory_delta()

        assert delta == 500


def test_memory_profiler_get_memory_delta_no_baseline():
    """Test MemoryProfiler.get_memory_delta() returns 0 if no baseline."""
    profiler = MemoryProfiler()

    delta = profiler.get_memory_delta()

    assert delta == 0


def test_memory_profiler_measure_model_instantiation():
    """Test MemoryProfiler.measure_model_instantiation() measures memory."""
    profiler = MemoryProfiler()

    with (
        patch("server.utils.memory_profiler.gc.collect"),
        patch("server.utils.memory_profiler.tracemalloc.start"),
        patch("server.utils.memory_profiler.tracemalloc.stop"),
        patch("server.utils.memory_profiler.tracemalloc.get_traced_memory", return_value=(100, 200)),
        patch.object(profiler.process, "memory_info", return_value=MagicMock(rss=1000)),
    ):
        profiler.baseline_memory = 500
        result = profiler.measure_model_instantiation(SampleModel, iterations=10, name="test", value=1)

        assert result["model_class"] == "SampleModel"
        assert result["iterations"] == 10
        assert "memory_delta_bytes" in result
        assert "memory_per_instance_bytes" in result
        assert "peak_memory_bytes" in result


def test_memory_profiler_measure_model_instantiation_zero_iterations():
    """Test MemoryProfiler.measure_model_instantiation() handles zero iterations."""
    profiler = MemoryProfiler()

    with (
        patch("server.utils.memory_profiler.gc.collect"),
        patch("server.utils.memory_profiler.tracemalloc.start"),
        patch("server.utils.memory_profiler.tracemalloc.stop"),
        patch("server.utils.memory_profiler.tracemalloc.get_traced_memory", return_value=(100, 200)),
        patch.object(profiler.process, "memory_info", return_value=MagicMock(rss=1000)),
    ):
        profiler.baseline_memory = 500
        result = profiler.measure_model_instantiation(SampleModel, iterations=0, name="test", value=1)

        assert result["iterations"] == 0
        assert result["memory_per_instance_bytes"] == 0


def test_memory_profiler_get_memory_usage_summary():
    """Test MemoryProfiler.get_memory_usage_summary() returns summary."""
    profiler = MemoryProfiler()

    with (
        patch.object(profiler.process, "memory_info", return_value=MagicMock(rss=2000, vms=3000)),
        patch.object(profiler.process, "memory_percent", return_value=5.0),
        patch(
            "server.utils.memory_profiler.psutil.virtual_memory",
            return_value=MagicMock(available=1000000, total=2000000),
        ),
    ):
        summary = profiler.get_memory_usage_summary()

        assert "rss_bytes" in summary
        assert "rss_mb" in summary
        assert summary["rss_bytes"] == 2000


def test_memory_profiler_print_memory_summary():
    """Test MemoryProfiler.print_memory_summary() doesn't raise."""
    profiler = MemoryProfiler()

    with (
        patch.object(profiler.process, "memory_info", return_value=MagicMock(rss=2000, vms=3000)),
        patch.object(profiler.process, "memory_percent", return_value=5.0),
        patch(
            "server.utils.memory_profiler.psutil.virtual_memory",
            return_value=MagicMock(available=1000000, total=2000000),
        ),
        patch("builtins.print") as mock_print,
    ):
        profiler.print_memory_summary()

        mock_print.assert_called()


def test_memory_profiler_print_model_memory_usage():
    """Test MemoryProfiler.print_model_memory_usage() doesn't raise."""
    profiler = MemoryProfiler()
    result = {
        "model_class": "SampleModel",
        "iterations": 10,
        "memory_delta_bytes": 1500,
        "memory_per_instance_bytes": 150,
        "memory_per_instance_kb": 1.5,
        "peak_memory_bytes": 2000,
    }

    with patch("builtins.print") as mock_print:
        profiler.print_model_memory_usage(result)

        mock_print.assert_called()
