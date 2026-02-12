"""
Metrics data schema for MythosMUD.

This module defines Pydantic models for metrics data structures used in API responses.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class MetricsData(BaseModel):
    """
    Comprehensive system metrics data.

    This model represents system metrics with dynamic structure to accommodate
    various metric types (NATS, circuit breaker, DLQ, performance, etc.).
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic metric structures
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    # Common metric fields (may not always be present)
    uptime_seconds: float | None = Field(default=None, description="System uptime in seconds")
    messages: dict[str, Any] | None = Field(default=None, description="Message processing metrics")
    circuit_breaker: dict[str, Any] | None = Field(default=None, description="Circuit breaker metrics")
    dead_letter_queue: dict[str, Any] | None = Field(default=None, description="DLQ metrics")
    nats_connection: dict[str, Any] | None = Field(default=None, description="NATS connection metrics")
    performance: dict[str, Any] | None = Field(default=None, description="Performance metrics")


class MetricsSummary(BaseModel):
    """
    High-level metrics summary.

    This model represents a concise summary of system health indicators.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic summary data
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    total_messages: int | None = Field(default=None, description="Total messages processed")
    success_rate: float | None = Field(default=None, description="Success rate (0.0-1.0)")


class DLQMessage(BaseModel):
    """
    Dead letter queue message structure.

    This model represents a message that failed processing and was sent to the DLQ.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic message data
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    message_id: str | None = Field(default=None, description="Message identifier")
    subject: str | None = Field(default=None, description="NATS subject")
    timestamp: str | None = Field(default=None, description="ISO format timestamp")
    error: str | None = Field(default=None, description="Error message")
    payload: dict[str, Any] | None = Field(default=None, description="Message payload")
    retry_count: int | None = Field(default=None, description="Number of retry attempts")


class DLQReplayDetails(BaseModel):
    """
    Details for DLQ message replay operation.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic replay details
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    messages_replayed: int | None = Field(default=None, description="Number of messages replayed")
    messages_failed: int | None = Field(default=None, description="Number of messages that failed to replay")
    errors: list[str] | None = Field(default=None, description="List of error messages")
