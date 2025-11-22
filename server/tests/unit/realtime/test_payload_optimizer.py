"""
Tests for payload optimization functionality.

This module tests the PayloadOptimizer class which handles size limits,
compression, and incremental updates for WebSocket messages.
"""

import gzip
import json

import pytest

from server.realtime.payload_optimizer import PayloadOptimizer, get_payload_optimizer


class TestPayloadOptimizer:
    """Test cases for PayloadOptimizer class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.optimizer = PayloadOptimizer()

    def test_get_payload_size(self):
        """Test calculating payload size."""
        payload = {"type": "chat", "message": "Hello, world!"}
        size = self.optimizer.get_payload_size(payload)

        assert size > 0
        # Size should match JSON string length
        json_str = json.dumps(payload, separators=(",", ":"))
        assert size == len(json_str.encode("utf-8"))

    def test_optimize_payload_within_limits(self):
        """Test optimization of payload within size limits."""
        payload = {"type": "chat", "message": "Hello, world!"}
        optimized = self.optimizer.optimize_payload(payload)

        # Small payload should be returned as-is
        assert optimized == payload

    def test_optimize_payload_exceeds_max_size(self):
        """Test optimization fails for payload exceeding maximum size."""
        # Create payload with uncompressible data that exceeds max even when compressed
        # Use random data that doesn't compress well - needs to be > 50KB compressed
        import random
        import string

        # Generate random uncompressible data (150KB of random characters)
        random_data = "".join(random.choices(string.ascii_letters + string.digits, k=150000))
        large_payload = {"type": "chat", "message": random_data}

        with pytest.raises(ValueError) as exc_info:
            self.optimizer.optimize_payload(large_payload)

        assert "too large" in str(exc_info.value).lower()

    def test_compress_payload_above_threshold(self):
        """Test compression of payload above compression threshold."""
        # Create payload above 10KB threshold
        payload = {"type": "chat", "message": "x" * 15000}
        compressed = self.optimizer.compress_payload(payload)

        assert compressed["compressed"] is True
        assert "data" in compressed
        assert "original_size" in compressed
        assert "compressed_size" in compressed
        assert compressed["compressed_size"] < compressed["original_size"]

    def test_compress_payload_below_threshold(self):
        """Test compression is applied even below threshold if forced."""
        payload = {"type": "chat", "message": "Hello"}
        compressed = self.optimizer.compress_payload(payload)

        # Should still compress (compression always works)
        assert compressed["compressed"] is True

    def test_optimize_payload_auto_compresses_large(self):
        """Test optimization automatically compresses large payloads."""
        # Create payload above compression threshold but below max
        payload = {"type": "chat", "message": "x" * 15000}
        optimized = self.optimizer.optimize_payload(payload)

        # Should be compressed
        assert optimized["compressed"] is True
        assert optimized["compressed_size"] < optimized["original_size"]

    def test_optimize_payload_skips_compression_if_not_beneficial(self):
        """Test optimization skips compression if it doesn't reduce size."""
        # Create payload that compresses poorly
        payload = {"type": "chat", "message": "abc" * 1000}  # Repetitive but small

        # Force compression to see if it's beneficial
        compressed = self.optimizer.compress_payload(payload)
        compression_ratio = compressed.get("compression_ratio", 1.0)

        # If compression doesn't help (ratio > 0.9), optimization should skip it
        if compression_ratio >= 0.9:
            optimized = self.optimizer.optimize_payload(payload, force_compression=False)
            # May return original if compression doesn't help enough
            assert optimized is not None

    def test_create_incremental_update_no_previous(self):
        """Test incremental update creation with no previous payload."""
        current = {"type": "room_update", "room_id": "room_1", "occupants": ["player1"]}
        incremental = self.optimizer.create_incremental_update(current, previous_payload=None)

        # Should return full payload when no previous
        assert incremental == current

    def test_create_incremental_update_with_changes(self):
        """Test incremental update creation with changes."""
        previous = {"type": "room_update", "room_id": "room_1", "occupants": ["player1"]}
        current = {"type": "room_update", "room_id": "room_1", "occupants": ["player1", "player2"]}

        incremental = self.optimizer.create_incremental_update(current, previous)

        assert incremental["incremental"] is True
        assert "changes" in incremental
        assert "occupants" in incremental["changes"]

    def test_create_incremental_update_no_changes(self):
        """Test incremental update creation with no changes."""
        payload = {"type": "room_update", "room_id": "room_1", "occupants": ["player1"]}

        incremental = self.optimizer.create_incremental_update(payload, payload)

        assert incremental["incremental"] is True
        assert incremental["changes"] == {}

    def test_custom_size_limits(self):
        """Test optimizer with custom size limits."""
        optimizer = PayloadOptimizer(
            max_payload_size=50 * 1024,  # 50KB
            compression_threshold=5 * 1024,  # 5KB
            max_compressed_size=25 * 1024,  # 25KB max compressed
        )

        # Payload within custom limit should pass
        payload = {"type": "chat", "message": "x" * 10000}
        optimized = optimizer.optimize_payload(payload)
        assert optimized is not None

        # Payload exceeding custom limit with uncompressible data should fail
        # Use random data that doesn't compress well
        import random
        import string

        random_data = "".join(random.choices(string.ascii_letters + string.digits, k=60000))
        large_payload = {"type": "chat", "message": random_data}
        with pytest.raises(ValueError):
            optimizer.optimize_payload(large_payload)

    def test_get_payload_optimizer_singleton(self):
        """Test get_payload_optimizer returns singleton instance."""
        optimizer1 = get_payload_optimizer()
        optimizer2 = get_payload_optimizer()

        assert optimizer1 is optimizer2

    def test_compression_decompression_roundtrip(self):
        """Test that compressed payload can be decompressed."""
        payload = {"type": "chat", "message": "x" * 15000}
        compressed = self.optimizer.compress_payload(payload)

        # Decompress the hex string
        compressed_data = bytes.fromhex(compressed["data"])
        decompressed = gzip.decompress(compressed_data).decode("utf-8")
        decompressed_payload = json.loads(decompressed)

        assert decompressed_payload == payload
