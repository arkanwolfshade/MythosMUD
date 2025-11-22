"""
Payload optimization for WebSocket messages.

This module provides utilities for optimizing payload sizes including:
- Size limits and validation
- Compression for large payloads
- Incremental update support
"""

import gzip
import json
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PayloadOptimizer:
    """
    Optimizes payloads for WebSocket transmission.

    Features:
    - Size limit enforcement
    - Compression for large payloads
    - Incremental update support
    """

    # Configuration constants
    MAX_PAYLOAD_SIZE = 100 * 1024  # 100KB maximum uncompressed payload
    COMPRESSION_THRESHOLD = 10 * 1024  # Compress payloads larger than 10KB
    MAX_COMPRESSED_SIZE = 50 * 1024  # 50KB maximum compressed payload

    def __init__(
        self,
        max_payload_size: int | None = None,
        compression_threshold: int | None = None,
        max_compressed_size: int | None = None,
    ):
        """
        Initialize the payload optimizer.

        Args:
            max_payload_size: Maximum payload size in bytes (default: 100KB)
            compression_threshold: Size threshold for compression (default: 10KB)
            max_compressed_size: Maximum compressed payload size (default: 50KB)
        """
        self.max_payload_size = max_payload_size or self.MAX_PAYLOAD_SIZE
        self.compression_threshold = compression_threshold or self.COMPRESSION_THRESHOLD
        self.max_compressed_size = max_compressed_size or self.MAX_COMPRESSED_SIZE

    def get_payload_size(self, payload: dict[str, Any]) -> int:
        """
        Calculate the size of a payload in bytes.

        Args:
            payload: The payload dictionary

        Returns:
            int: Size in bytes
        """
        try:
            json_str = json.dumps(payload, separators=(",", ":"))
            return len(json_str.encode("utf-8"))
        except Exception as e:
            logger.warning("Error calculating payload size", error=str(e))
            return 0

    def compress_payload(self, payload: dict[str, Any]) -> dict[str, Any]:
        """
        Compress a large payload using gzip compression.

        Args:
            payload: The payload dictionary to compress

        Returns:
            dict: Compressed payload with metadata
        """
        try:
            json_str = json.dumps(payload, separators=(",", ":"))
            compressed = gzip.compress(json_str.encode("utf-8"), compresslevel=6)

            return {
                "compressed": True,
                "data": compressed.hex(),  # Convert to hex string for JSON transmission
                "original_size": len(json_str.encode("utf-8")),
                "compressed_size": len(compressed),
                "compression_ratio": len(compressed) / len(json_str.encode("utf-8")) if json_str else 0,
            }
        except Exception as e:
            logger.error("Error compressing payload", error=str(e), exc_info=True)
            return payload

    def optimize_payload(self, payload: dict[str, Any], force_compression: bool = False) -> dict[str, Any]:
        """
        Optimize a payload by applying size limits and compression if needed.

        Args:
            payload: The payload dictionary to optimize
            force_compression: Force compression even if below threshold

        Returns:
            dict: Optimized payload (may be compressed or truncated)

        Raises:
            ValueError: If payload exceeds maximum size even after compression
        """
        size = self.get_payload_size(payload)

        # Check if payload exceeds maximum size
        if size > self.max_payload_size:
            logger.warning(
                "Payload exceeds maximum size",
                payload_size=size,
                max_size=self.max_payload_size,
                exceeds_by=size - self.max_payload_size,
            )

            # Try compression first
            if size > self.compression_threshold or force_compression:
                compressed = self.compress_payload(payload)
                compressed_size = compressed.get("compressed_size", size)

                if compressed_size <= self.max_compressed_size:
                    logger.info(
                        "Payload compressed successfully",
                        original_size=size,
                        compressed_size=compressed_size,
                        compression_ratio=compressed.get("compression_ratio", 0),
                    )
                    return compressed
                else:
                    logger.error(
                        "Payload too large even after compression",
                        original_size=size,
                        compressed_size=compressed_size,
                        max_compressed_size=self.max_compressed_size,
                    )
                    raise ValueError(
                        f"Payload too large: {compressed_size} bytes (max: {self.max_compressed_size} bytes)"
                    )
            else:
                # Payload too large and below compression threshold - truncate or error
                logger.error(
                    "Payload exceeds maximum size and is below compression threshold",
                    payload_size=size,
                    max_size=self.max_payload_size,
                    compression_threshold=self.compression_threshold,
                )
                raise ValueError(f"Payload too large: {size} bytes (max: {self.max_payload_size} bytes)")

        # Apply compression if above threshold
        if size > self.compression_threshold or force_compression:
            compressed = self.compress_payload(payload)
            compressed_size = compressed.get("compressed_size", size)

            # Only use compression if it actually reduces size
            if compressed_size < size * 0.9:  # At least 10% reduction
                logger.debug(
                    "Payload compressed for efficiency",
                    original_size=size,
                    compressed_size=compressed_size,
                    compression_ratio=compressed.get("compression_ratio", 0),
                )
                return compressed

        # Payload is within limits, return as-is
        return payload

    def create_incremental_update(
        self, full_payload: dict[str, Any], previous_payload: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Create an incremental update payload containing only changed fields.

        Args:
            full_payload: The complete current payload
            previous_payload: The previous payload to compare against

        Returns:
            dict: Incremental update payload with only changed fields
        """
        if previous_payload is None:
            # No previous payload, return full payload
            return full_payload

        try:
            # Find changed fields
            changes: dict[str, Any] = {}
            for key, value in full_payload.items():
                if key not in previous_payload or previous_payload[key] != value:
                    changes[key] = value

            if not changes:
                # No changes, return empty update
                return {"incremental": True, "changes": {}}

            return {
                "incremental": True,
                "changes": changes,
                "timestamp": full_payload.get("timestamp"),
            }
        except Exception as e:
            logger.error("Error creating incremental update", error=str(e), exc_info=True)
            # Fallback to full payload on error
            return full_payload


# Global optimizer instance
_payload_optimizer = PayloadOptimizer()


def get_payload_optimizer() -> PayloadOptimizer:
    """Get the global payload optimizer instance."""
    return _payload_optimizer
