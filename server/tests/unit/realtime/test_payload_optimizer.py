"""Unit tests for WebSocket payload optimization."""

import json

import pytest

from server.realtime.payload_optimizer import PayloadOptimizer, get_payload_optimizer


@pytest.fixture
def optimizer() -> PayloadOptimizer:
    """Small thresholds so tests stay fast."""
    return PayloadOptimizer(
        max_payload_size=500,
        compression_threshold=100,
        max_compressed_size=400,
    )


def test_get_payload_size_returns_byte_length(optimizer: PayloadOptimizer) -> None:
    payload = {"event": "room_state", "room_id": "earth_arkhamcity_street_room_001"}
    expected = len(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    assert optimizer.get_payload_size(payload) == expected


def test_get_payload_size_returns_zero_on_serialization_error(optimizer: PayloadOptimizer) -> None:
    assert optimizer.get_payload_size({"bad": object()}) == 0


def test_compress_payload_round_trip_metadata(optimizer: PayloadOptimizer) -> None:
    payload = {"data": "x" * 200}
    compressed = optimizer.compress_payload(payload)
    assert compressed["compressed"] is True
    assert compressed["original_size"] > 0
    assert compressed["compressed_size"] > 0
    assert 0 < compressed["compression_ratio"] <= 1


def test_optimize_payload_returns_small_payload_unchanged(optimizer: PayloadOptimizer) -> None:
    payload = {"type": "ping"}
    assert optimizer.optimize_payload(payload) == payload


def test_optimize_payload_compresses_large_payload(optimizer: PayloadOptimizer) -> None:
    payload = {"blob": "z" * 300}
    result = optimizer.optimize_payload(payload)
    assert result.get("compressed") is True


def test_optimize_payload_force_compression_when_beneficial(optimizer: PayloadOptimizer) -> None:
    payload = {"blob": "z" * 150}
    result = optimizer.optimize_payload(payload, force_compression=True)
    assert result.get("compressed") is True


def test_optimize_payload_raises_when_uncompressible_and_oversized(optimizer: PayloadOptimizer) -> None:
    tiny_optimizer = PayloadOptimizer(max_payload_size=50, compression_threshold=1000, max_compressed_size=10)
    payload = {"blob": "a" * 80}
    with pytest.raises(ValueError, match="Payload too large"):
        tiny_optimizer.optimize_payload(payload)


def test_optimize_payload_raises_when_compressed_still_too_large(optimizer: PayloadOptimizer) -> None:
    tiny_optimizer = PayloadOptimizer(max_payload_size=200, compression_threshold=50, max_compressed_size=10)
    payload = {"blob": "b" * 300}
    with pytest.raises(ValueError, match="Payload too large"):
        tiny_optimizer.optimize_payload(payload)


def test_create_incremental_update_no_previous_returns_full(optimizer: PayloadOptimizer) -> None:
    payload = {"hp": 10, "timestamp": 1}
    assert optimizer.create_incremental_update(payload, None) == payload


def test_create_incremental_update_detects_changes(optimizer: PayloadOptimizer) -> None:
    previous = {"hp": 10, "mp": 5, "timestamp": 1}
    current = {"hp": 8, "mp": 5, "timestamp": 2}
    result = optimizer.create_incremental_update(current, previous)
    assert result == {"incremental": True, "changes": {"hp": 8, "timestamp": 2}, "timestamp": 2}


def test_create_incremental_update_empty_when_unchanged(optimizer: PayloadOptimizer) -> None:
    payload = {"hp": 10, "timestamp": 1}
    result = optimizer.create_incremental_update(payload, payload.copy())
    assert result == {"incremental": True, "changes": {}}


class _CompareExplodes:
    def __eq__(self, _other: object) -> bool:
        raise RuntimeError("compare failed")


def test_create_incremental_update_fallback_on_error(optimizer: PayloadOptimizer) -> None:
    full = {"hp": 11, "stat": _CompareExplodes()}
    previous = {"hp": 10, "stat": _CompareExplodes()}
    result = optimizer.create_incremental_update(full, previous)
    assert result == full


def test_get_payload_optimizer_returns_singleton() -> None:
    assert get_payload_optimizer() is get_payload_optimizer()
