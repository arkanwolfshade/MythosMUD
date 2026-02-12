"""
Metrics API response schemas for MythosMUD server.

This module provides Pydantic models for metrics-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from pydantic import BaseModel, ConfigDict, Field

from .metrics_data import DLQMessage, DLQReplayDetails, MetricsData, MetricsSummary


class MetricsResponse(BaseModel):
    """Response model for comprehensive system metrics."""

    metrics: MetricsData = Field(
        ..., description="Comprehensive system metrics including NATS, circuit breaker, and DLQ stats"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "metrics": {
                    "circuit_breaker": {"state": "closed"},
                    "dead_letter_queue": {"total_messages": 0},
                    "nats_connection": {"status": "connected"},
                }
            }
        }
    )


class MetricsSummaryResponse(BaseModel):
    """Response model for concise metrics summary."""

    summary: MetricsSummary = Field(..., description="High-level health indicators and summary metrics")
    dlq_pending: int | None = Field(default=None, description="Number of messages pending in DLQ")
    circuit_state: str | None = Field(default=None, description="Current circuit breaker state")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "summary": {"total_messages": 1000, "success_rate": 0.99},
                "dlq_pending": 5,
                "circuit_state": "closed",
            }
        }
    )


class StatusMessageResponse(BaseModel):
    """Response model for operations that return status and message."""

    status: str = Field(..., description="Operation status (e.g., 'success', 'error')")
    message: str = Field(..., description="Status message")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "success",
                "message": "Operation completed successfully",
            }
        }
    )


class DLQMessagesResponse(BaseModel):
    """Response model for dead letter queue messages."""

    messages: list[DLQMessage] = Field(default_factory=list, description="List of DLQ messages")
    count: int = Field(..., description="Number of messages returned")
    total_in_dlq: int = Field(..., description="Total number of messages in DLQ")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "messages": [],
                "count": 0,
                "total_in_dlq": 0,
            }
        }
    )


class DLQReplayResponse(BaseModel):
    """Response model for DLQ message replay operation."""

    status: str = Field(..., description="Replay status")
    message: str = Field(..., description="Replay result message")
    filepath: str = Field(..., description="Path to the replayed message file")
    details: DLQReplayDetails | None = Field(default=None, description="Additional replay details")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "success",
                "message": "Message replayed successfully",
                "filepath": "/path/to/message.json",
                "details": {},
            }
        }
    )
