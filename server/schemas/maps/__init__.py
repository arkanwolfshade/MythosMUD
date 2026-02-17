"""Maps domain schemas: map API responses."""

from .map import (
    AsciiMapResponse,
    AsciiMinimapResponse,
    CoordinateGenerationResponse,
    CoordinateRecalculationResponse,
    CoordinateValidationResponse,
    MapOriginSetResponse,
    ViewportInfo,
)

__all__ = [
    "AsciiMapResponse",
    "AsciiMinimapResponse",
    "CoordinateGenerationResponse",
    "CoordinateRecalculationResponse",
    "CoordinateValidationResponse",
    "MapOriginSetResponse",
    "ViewportInfo",
]
