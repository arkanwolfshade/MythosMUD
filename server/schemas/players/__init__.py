"""Players domain schemas: player, character creation, profession, effects, respawn, requests."""

from .character_creation import (
    CreateCharacterResponse,
    RollStatsResponse,
    StatSummary,
    ValidateStatsResponse,
)
from .player import (
    AvailableClassesResponse,
    CharacterInfo,
    DeleteCharacterResponse,
    LoginGracePeriodResponse,
    MessageResponse,
    PlayerBase,
    PlayerCreate,
    PlayerRead,
    PlayerUpdate,
    PositionState,
)
from .player_effects import EffectResponse
from .player_requests import (
    CorruptionRequest,
    CreateCharacterRequest,
    DamageRequest,
    FearRequest,
    HealRequest,
    LucidityLossRequest,
    OccultKnowledgeRequest,
    RollStatsRequest,
    SelectCharacterRequest,
)
from .player_respawn import RespawnPlayerData, RespawnResponse
from .profession import (
    MechanicalEffect,
    ProfessionData,
    ProfessionListResponse,
    ProfessionResponse,
    StatRequirement,
)

__all__ = [
    "AvailableClassesResponse",
    "CharacterInfo",
    "CreateCharacterRequest",
    "CreateCharacterResponse",
    "CorruptionRequest",
    "DamageRequest",
    "DeleteCharacterResponse",
    "EffectResponse",
    "FearRequest",
    "HealRequest",
    "LoginGracePeriodResponse",
    "LucidityLossRequest",
    "MechanicalEffect",
    "MessageResponse",
    "OccultKnowledgeRequest",
    "PlayerBase",
    "PlayerCreate",
    "PlayerRead",
    "PlayerUpdate",
    "PositionState",
    "ProfessionData",
    "ProfessionListResponse",
    "ProfessionResponse",
    "RespawnPlayerData",
    "RespawnResponse",
    "RollStatsRequest",
    "RollStatsResponse",
    "SelectCharacterRequest",
    "StatRequirement",
    "StatSummary",
    "ValidateStatsResponse",
]
