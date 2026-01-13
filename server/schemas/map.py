"""
Map API response schemas for MythosMUD server.

This module provides Pydantic models for map-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from pydantic import BaseModel, ConfigDict, Field


class ViewportInfo(BaseModel):
    """Viewport information for map rendering."""

    x: int = Field(..., description="Viewport X offset")
    y: int = Field(..., description="Viewport Y offset")
    width: int = Field(..., description="Viewport width in characters")
    height: int = Field(..., description="Viewport height in lines")


class AsciiMapResponse(BaseModel):
    """Response model for ASCII map endpoint."""

    map_html: str = Field(..., description="HTML string containing the rendered ASCII map")
    plane: str = Field(..., description="Plane name")
    zone: str = Field(..., description="Zone name")
    sub_zone: str | None = Field(default=None, description="Sub-zone name (if any)")
    viewport: ViewportInfo = Field(..., description="Viewport information")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "map_html": "<pre>...</pre>",
                "plane": "earth",
                "zone": "arkhamcity",
                "sub_zone": "downtown",
                "viewport": {"x": 0, "y": 0, "width": 80, "height": 24},
            }
        }
    )


class AsciiMinimapResponse(BaseModel):
    """Response model for ASCII minimap endpoint."""

    map_html: str = Field(..., description="HTML string containing the rendered ASCII minimap")
    plane: str = Field(..., description="Plane name")
    zone: str = Field(..., description="Zone name")
    sub_zone: str | None = Field(default=None, description="Sub-zone name (if any)")
    size: int = Field(..., description="Minimap size in characters (e.g., 5 means 5x5 grid)")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "map_html": "<pre>...</pre>",
                "plane": "earth",
                "zone": "arkhamcity",
                "sub_zone": "downtown",
                "size": 5,
            }
        }
    )


class CoordinateGenerationResponse(BaseModel):
    """Response model for coordinate generation endpoint."""

    message: str = Field(..., description="Success message")
    plane: str = Field(..., description="Plane name")
    zone: str = Field(..., description="Zone name")
    sub_zone: str | None = Field(default=None, description="Sub-zone name (if any)")
    rooms_processed: int = Field(..., description="Number of rooms that had coordinates generated")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Coordinates generated successfully",
                "plane": "earth",
                "zone": "arkhamcity",
                "sub_zone": "downtown",
                "rooms_processed": 42,
            }
        }
    )


class CoordinateValidationResponse(BaseModel):
    """Response model for coordinate validation endpoint."""

    valid: bool = Field(..., description="Whether coordinates are valid")
    issues: list[str] = Field(default_factory=list, description="List of validation issues found")
    plane: str = Field(..., description="Plane name")
    zone: str = Field(..., description="Zone name")
    sub_zone: str | None = Field(default=None, description="Sub-zone name (if any)")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "valid": True,
                "issues": [],
                "plane": "earth",
                "zone": "arkhamcity",
                "sub_zone": "downtown",
            }
        }
    )


class CoordinateRecalculationResponse(BaseModel):
    """Response model for coordinate recalculation endpoint."""

    message: str = Field(..., description="Success message")
    coordinates_generated: int = Field(..., description="Number of coordinates generated")
    conflicts: list[str] = Field(default_factory=list, description="List of coordinate conflicts found")
    conflict_count: int = Field(..., description="Total number of conflicts")
    valid: bool = Field(..., description="Whether coordinates are valid after recalculation")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Coordinates recalculated",
                "coordinates_generated": 42,
                "conflicts": [],
                "conflict_count": 0,
                "valid": True,
            }
        }
    )


class MapOriginSetResponse(BaseModel):
    """Response model for setting map origin endpoint."""

    room_id: str = Field(..., description="Room ID that was set as origin")
    message: str = Field(..., description="Success message")
    coordinates_generated: int = Field(..., description="Number of coordinates generated")
    conflicts: list[str] = Field(default_factory=list, description="List of coordinate conflicts found")
    conflict_count: int = Field(..., description="Total number of conflicts")
    valid: bool = Field(..., description="Whether coordinates are valid after recalculation")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
                "message": "Map origin set and coordinates recalculated",
                "coordinates_generated": 42,
                "conflicts": [],
                "conflict_count": 0,
                "valid": True,
            }
        }
    )
