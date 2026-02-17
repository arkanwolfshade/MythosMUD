"""
Game API response schemas for MythosMUD server.

This module provides Pydantic models for game-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from pydantic import BaseModel, ConfigDict, Field

from server.schemas.calendar import HolidayEntry


class GameStatusResponse(BaseModel):
    """Response model for game status endpoint."""

    active_connections: int = Field(..., description="Number of active WebSocket connections")
    active_players: int = Field(..., description="Number of currently connected players")
    room_subscriptions: int = Field(..., description="Number of active room subscriptions")
    server_time: str = Field(..., description="ISO-8601 timestamp of server time")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "active_connections": 5,
                "active_players": 3,
                "room_subscriptions": 12,
                "server_time": "2025-01-12T15:30:45.123456Z",
            }
        }
    )


class BroadcastStats(BaseModel):
    """Statistics for a broadcast operation."""

    successful_deliveries: int = Field(..., description="Number of successful message deliveries")
    failed_deliveries: int = Field(default=0, description="Number of failed message deliveries")
    total_recipients: int = Field(..., description="Total number of recipients attempted")


class BroadcastMessageResponse(BaseModel):
    """Response model for broadcast message endpoint."""

    message: str = Field(..., description="The broadcast message")
    recipients: int = Field(..., description="Number of recipients who received the message")
    broadcaster: str = Field(..., description="Username of the broadcaster")
    broadcast_stats: BroadcastStats = Field(..., description="Detailed broadcast statistics")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Server maintenance in 5 minutes",
                "recipients": 10,
                "broadcaster": "admin",
                "broadcast_stats": {
                    "successful_deliveries": 10,
                    "failed_deliveries": 0,
                    "total_recipients": 10,
                },
            }
        }
    )


class MythosTimeResponse(BaseModel):
    """Response model for Mythos calendar time endpoint."""

    mythos_datetime: str = Field(..., description="ISO-8601 formatted Mythos datetime")
    mythos_clock: str = Field(..., description="Formatted clock time in Mythos format")
    month_name: str = Field(..., description="Name of the current month")
    day_of_month: int = Field(..., description="Day of the month (1-31)")
    day_name: str = Field(..., description="Name of the day of week")
    week_of_month: int = Field(..., description="Week number within the month")
    season: str = Field(..., description="Current season")
    daypart: str = Field(..., description="Time of day (dawn, day, dusk, night)")
    is_daytime: bool = Field(..., description="Whether it is currently daytime")
    is_witching_hour: bool = Field(..., description="Whether it is the witching hour")
    server_timestamp: str = Field(..., description="ISO-8601 timestamp of server time")
    active_holidays: list[HolidayEntry] = Field(default_factory=list, description="Currently active holidays")
    upcoming_holidays: list[HolidayEntry] = Field(default_factory=list, description="Upcoming holidays")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "mythos_datetime": "1926-10-31T23:45:00Z",
                "mythos_clock": "11:45 PM",
                "month_name": "October",
                "day_of_month": 31,
                "day_name": "Sunday",
                "week_of_month": 5,
                "season": "autumn",
                "daypart": "night",
                "is_daytime": False,
                "is_witching_hour": True,
                "server_timestamp": "2025-01-12T15:30:45.123456Z",
                "active_holidays": [],
                "upcoming_holidays": [],
            }
        }
    )
