"""Rooms domain schemas: room API responses."""

from .room import (
    RoomListResponse,
    RoomPositionUpdateResponse,
    RoomResponse,
)
from .room_write import (
    ExitCreateRequest,
    ExitResponse,
    ExitUpdateRequest,
    RoomUpdateRequest,
    RoomUpdateResponse,
)

__all__ = [
    "ExitCreateRequest",
    "ExitResponse",
    "ExitUpdateRequest",
    "RoomListResponse",
    "RoomPositionUpdateResponse",
    "RoomResponse",
    "RoomUpdateRequest",
    "RoomUpdateResponse",
]
