"""
Pydantic schemas for MythosMUD.

This package contains all Pydantic schemas including:
- User schemas (FastAPI Users)
- Player schemas (game data)
- Invite schemas (custom invite system)
"""

from .admin import (
    AdminAuditLogResponse,
    AdminCleanupSessionsResponse,
    AdminSessionsResponse,
    NPCDespawnResponse,
    NPCMoveResponse,
    NPCPopulationStatsResponse,
    NPCSpawnResponse,
    NPCStatsResponse,
    NPCSystemStatusResponse,
    NPCZoneStatsResponse,
)
from .auth import InviteCreate, InviteRead, InviteUpdate, UserCreate, UserRead, UserUpdate
from .calendar import HolidayCollection, HolidayEntry, ScheduleCollection, ScheduleEntry
from .containers import (
    ContainerCloseResponse,
    ContainerLootAllResponse,
    ContainerOpenResponse,
    ContainerTransferResponse,
)
from .game import BroadcastMessageResponse, GameStatusResponse, MythosTimeResponse
from .maps import (
    AsciiMapResponse,
    AsciiMinimapResponse,
    CoordinateRecalculationResponse,
    MapOriginSetResponse,
)
from .metrics import (
    DLQMessagesResponse,
    DLQReplayResponse,
    MetricsResponse,
    MetricsSummaryResponse,
    StatusMessageResponse,
)
from .players import (
    AvailableClassesResponse,
    CreateCharacterResponse,
    DeleteCharacterResponse,
    EffectResponse,
    LoginGracePeriodResponse,
    MessageResponse,
    PlayerCreate,
    PlayerRead,
    PlayerUpdate,
    ProfessionListResponse,
    ProfessionResponse,
    RespawnResponse,
    RollStatsResponse,
    ValidateStatsResponse,
)
from .realtime import (
    ConnectionStatisticsResponse,
    NewGameSessionResponse,
    PlayerConnectionsResponse,
)
from .rooms import RoomListResponse, RoomPositionUpdateResponse, RoomResponse

__all__ = [
    "HolidayCollection",
    "HolidayEntry",
    "ScheduleCollection",
    "ScheduleEntry",
    "BroadcastMessageResponse",
    "GameStatusResponse",
    "MythosTimeResponse",
    "CreateCharacterResponse",
    "RollStatsResponse",
    "ValidateStatsResponse",
    "ContainerOpenResponse",
    "ContainerTransferResponse",
    "ContainerCloseResponse",
    "ContainerLootAllResponse",
    "AsciiMapResponse",
    "AsciiMinimapResponse",
    "CoordinateRecalculationResponse",
    "MapOriginSetResponse",
    "DLQMessagesResponse",
    "DLQReplayResponse",
    "MetricsResponse",
    "MetricsSummaryResponse",
    "StatusMessageResponse",
    "RoomListResponse",
    "RoomPositionUpdateResponse",
    "RoomResponse",
    "ConnectionStatisticsResponse",
    "NewGameSessionResponse",
    "PlayerConnectionsResponse",
    "NPCSpawnResponse",
    "NPCDespawnResponse",
    "NPCMoveResponse",
    "NPCStatsResponse",
    "NPCPopulationStatsResponse",
    "NPCZoneStatsResponse",
    "NPCSystemStatusResponse",
    "AdminSessionsResponse",
    "AdminAuditLogResponse",
    "AdminCleanupSessionsResponse",
    "UserCreate",
    "UserRead",
    "UserUpdate",
    "PlayerCreate",
    "PlayerRead",
    "PlayerUpdate",
    "AvailableClassesResponse",
    "DeleteCharacterResponse",
    "LoginGracePeriodResponse",
    "MessageResponse",
    "EffectResponse",
    "RespawnResponse",
    "ProfessionListResponse",
    "ProfessionResponse",
    "InviteCreate",
    "InviteRead",
    "InviteUpdate",
]
