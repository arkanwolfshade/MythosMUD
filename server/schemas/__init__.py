"""
Pydantic schemas for MythosMUD.

This package contains all Pydantic schemas including:
- User schemas (FastAPI Users)
- Player schemas (game data)
- Invite schemas (custom invite system)
"""

from .calendar import HolidayCollection, HolidayEntry, ScheduleCollection, ScheduleEntry
from .character_creation import CreateCharacterResponse, RollStatsResponse, ValidateStatsResponse
from .container import (
    ContainerCloseResponse,
    ContainerLootAllResponse,
    ContainerOpenResponse,
    ContainerTransferResponse,
)
from .game import BroadcastMessageResponse, GameStatusResponse, MythosTimeResponse
from .invite import InviteCreate, InviteRead, InviteUpdate
from .map import (
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
from .npc_admin import (
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
from .player import (
    AvailableClassesResponse,
    DeleteCharacterResponse,
    LoginGracePeriodResponse,
    MessageResponse,
    PlayerCreate,
    PlayerRead,
    PlayerUpdate,
)
from .player_effects import EffectResponse
from .player_respawn import RespawnResponse
from .profession import ProfessionListResponse, ProfessionResponse
from .realtime import (
    ConnectionStatisticsResponse,
    NewGameSessionResponse,
    PlayerConnectionsResponse,
)
from .room import RoomListResponse, RoomPositionUpdateResponse, RoomResponse
from .user import UserCreate, UserRead, UserUpdate

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
