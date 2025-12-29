"""
Unit tests for NATS Subject Manager Metrics.

Tests the SubjectManagerMetrics class.
"""

import pytest

from server.services.nats_subject_manager.metrics import SubjectManagerMetrics


@pytest.fixture
def metrics():
    """Create SubjectManagerMetrics instance."""
    return SubjectManagerMetrics()


def test_subject_manager_metrics_init():
    """Test SubjectManagerMetrics initialization."""
    metrics = SubjectManagerMetrics()
    assert metrics.validation_count == 0
    assert metrics.validation_success_count == 0
    assert metrics.validation_failure_count == 0
    assert metrics.cache_hits == 0
    assert metrics.cache_misses == 0
    assert metrics.build_count == 0
    assert metrics.build_success_count == 0
    assert metrics.build_failure_count == 0
    assert metrics.pattern_not_found_errors == 0
    assert metrics.missing_parameter_errors == 0
    assert metrics.validation_errors == 0


def test_record_validation_success(metrics):
    """Test record_validation() records successful validation."""
    metrics.record_validation(0.001, success=True, cache_hit=False)
    assert metrics.validation_count == 1
    assert metrics.validation_success_count == 1
    assert metrics.validation_failure_count == 0
    assert metrics.cache_misses == 1
    assert metrics.cache_hits == 0


def test_record_validation_failure(metrics):
    """Test record_validation() records failed validation."""
    metrics.record_validation(0.001, success=False, cache_hit=False)
    assert metrics.validation_count == 1
    assert metrics.validation_success_count == 0
    assert metrics.validation_failure_count == 1


def test_record_validation_cache_hit(metrics):
    """Test record_validation() records cache hit."""
    metrics.record_validation(0.001, success=True, cache_hit=True)
    assert metrics.cache_hits == 1
    assert metrics.cache_misses == 0


def test_record_validation_multiple(metrics):
    """Test record_validation() records multiple validations."""
    metrics.record_validation(0.001, success=True, cache_hit=False)
    metrics.record_validation(0.002, success=True, cache_hit=True)
    metrics.record_validation(0.003, success=False, cache_hit=False)
    assert metrics.validation_count == 3
    assert metrics.validation_success_count == 2
    assert metrics.validation_failure_count == 1
    assert metrics.cache_hits == 1
    assert metrics.cache_misses == 2


def test_record_validation_stores_times(metrics):
    """Test record_validation() stores validation times."""
    metrics.record_validation(0.001, success=True, cache_hit=False)
    metrics.record_validation(0.002, success=True, cache_hit=False)
    assert len(metrics.validation_times) == 2
    assert 0.001 in metrics.validation_times
    assert 0.002 in metrics.validation_times


def test_record_build_success(metrics):
    """Test record_build() records successful build."""
    metrics.record_build(0.001, success=True)
    assert metrics.build_count == 1
    assert metrics.build_success_count == 1
    assert metrics.build_failure_count == 0


def test_record_build_failure(metrics):
    """Test record_build() records failed build."""
    metrics.record_build(0.001, success=False)
    assert metrics.build_count == 1
    assert metrics.build_success_count == 0
    assert metrics.build_failure_count == 1


def test_record_build_multiple(metrics):
    """Test record_build() records multiple builds."""
    metrics.record_build(0.001, success=True)
    metrics.record_build(0.002, success=True)
    metrics.record_build(0.003, success=False)
    assert metrics.build_count == 3
    assert metrics.build_success_count == 2
    assert metrics.build_failure_count == 1


def test_record_build_stores_times(metrics):
    """Test record_build() stores build times."""
    metrics.record_build(0.001, success=True)
    metrics.record_build(0.002, success=True)
    assert len(metrics.build_times) == 2
    assert 0.001 in metrics.build_times
    assert 0.002 in metrics.build_times


def test_record_error_pattern_not_found(metrics):
    """Test record_error() records pattern_not_found error."""
    metrics.record_error("pattern_not_found")
    assert metrics.pattern_not_found_errors == 1
    assert metrics.missing_parameter_errors == 0
    assert metrics.validation_errors == 0


def test_record_error_missing_parameter(metrics):
    """Test record_error() records missing_parameter error."""
    metrics.record_error("missing_parameter")
    assert metrics.pattern_not_found_errors == 0
    assert metrics.missing_parameter_errors == 1
    assert metrics.validation_errors == 0


def test_record_error_validation_error(metrics):
    """Test record_error() records validation_error."""
    metrics.record_error("validation_error")
    assert metrics.pattern_not_found_errors == 0
    assert metrics.missing_parameter_errors == 0
    assert metrics.validation_errors == 1


def test_record_error_unknown(metrics):
    """Test record_error() ignores unknown error types."""
    metrics.record_error("unknown_error")
    assert metrics.pattern_not_found_errors == 0
    assert metrics.missing_parameter_errors == 0
    assert metrics.validation_errors == 0


def test_get_metrics_empty(metrics):
    """Test get_metrics() returns metrics for empty state."""
    result = metrics.get_metrics()
    assert "validation" in result
    assert "cache" in result
    assert "build" in result
    assert "errors" in result
    assert result["validation"]["total_count"] == 0
    assert result["validation"]["success_rate"] == 0.0


def test_get_metrics_with_data(metrics):
    """Test get_metrics() returns metrics with data."""
    metrics.record_validation(0.001, success=True, cache_hit=False)
    metrics.record_validation(0.002, success=True, cache_hit=True)
    metrics.record_build(0.003, success=True)
    metrics.record_error("pattern_not_found")

    result = metrics.get_metrics()
    assert result["validation"]["total_count"] == 2
    assert result["validation"]["success_count"] == 2
    assert result["validation"]["success_rate"] == 1.0
    assert result["cache"]["hits"] == 1
    assert result["cache"]["misses"] == 1
    assert result["cache"]["hit_rate"] == 0.5
    assert result["build"]["total_count"] == 1
    assert result["build"]["success_count"] == 1
    assert result["errors"]["pattern_not_found"] == 1
    assert result["errors"]["total_errors"] == 1


def test_get_metrics_calculates_percentiles(metrics):
    """Test get_metrics() calculates percentiles."""
    # Add multiple times
    for i in range(10):
        metrics.record_validation(i * 0.001, success=True, cache_hit=False)

    result = metrics.get_metrics()
    assert "p95_time_ms" in result["validation"]
    assert result["validation"]["p95_time_ms"] > 0


def test_calculate_percentile_empty():
    """Test _calculate_percentile() returns 0 for empty list."""
    result = SubjectManagerMetrics._calculate_percentile([], 0.95)
    assert result == 0.0


def test_calculate_percentile_single_value():
    """Test _calculate_percentile() handles single value."""
    result = SubjectManagerMetrics._calculate_percentile([0.001], 0.95)
    assert result == 0.001


def test_calculate_percentile_multiple_values():
    """Test _calculate_percentile() calculates percentile correctly."""
    times = [0.001, 0.002, 0.003, 0.004, 0.005]
    result = SubjectManagerMetrics._calculate_percentile(times, 0.5)  # Median
    assert result == 0.003


def test_reset(metrics):
    """Test reset() clears all metrics."""
    metrics.record_validation(0.001, success=True, cache_hit=False)
    metrics.record_build(0.002, success=True)
    metrics.record_error("pattern_not_found")

    metrics.reset()

    assert metrics.validation_count == 0
    assert metrics.build_count == 0
    assert metrics.pattern_not_found_errors == 0
    assert len(metrics.validation_times) == 0
    assert len(metrics.build_times) == 0


def test_validation_times_maxlen(metrics):
    """Test validation_times deque respects maxlen."""
    # Add more than 1000 times
    for i in range(1500):
        metrics.record_validation(0.001, success=True, cache_hit=False)

    assert len(metrics.validation_times) == 1000


def test_build_times_maxlen(metrics):
    """Test build_times deque respects maxlen."""
    # Add more than 1000 times
    for i in range(1500):
        metrics.record_build(0.001, success=True)

    assert len(metrics.build_times) == 1000
