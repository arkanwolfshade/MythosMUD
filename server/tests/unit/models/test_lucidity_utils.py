"""
Unit tests for lucidity model utility functions.

Tests the _utc_now utility function.
"""

from datetime import UTC, datetime

from server.models.lucidity import _utc_now


def test_utc_now_returns_datetime():
    """Test _utc_now returns a datetime object."""
    result = _utc_now()

    assert isinstance(result, datetime)


def test_utc_now_returns_naive_datetime():
    """Test _utc_now returns naive datetime (tzinfo=None)."""
    result = _utc_now()

    assert result.tzinfo is None


def test_utc_now_returns_utc_time():
    """Test _utc_now returns time close to current UTC time."""
    before = datetime.now(UTC)
    result = _utc_now()
    after = datetime.now(UTC)

    # Convert result to UTC for comparison
    # Since result is naive, we assume it represents UTC
    result_utc = result.replace(tzinfo=UTC)

    # Should be within 1 second of current UTC time
    assert before <= result_utc <= after


def test_utc_now_returns_different_times():
    """Test _utc_now returns different times on subsequent calls."""
    result1 = _utc_now()
    result2 = _utc_now()

    # Results should be different (or very close if called quickly)
    # At minimum, result2 should be >= result1
    assert result2 >= result1
