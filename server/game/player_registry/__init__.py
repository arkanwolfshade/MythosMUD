"""The authoritative in-memory player registry (ADR-029)."""

from .aggregate import (
    PlayerAggregate,
    PlayerCooldownsView,
    PlayerExposureView,
    PlayerInventoryView,
    PlayerLucidityView,
    PlayerQuestsView,
    PlayerRowView,
    PlayerView,
)
from .part import DbSession, Part, PartWrite
from .player_cooldowns import REPLACE_CORRUPTION_COOLDOWNS_SQL, PlayerCooldownsPart
from .player_exposure import Exposure, PlayerExposurePart
from .player_inventory import InventoryData, PlayerInventoryPart
from .player_ledger import PlayerLedgerPart
from .player_lucidity import LucidityData, PlayerLucidityPart
from .player_quests import PlayerQuestsPart, QuestInstanceData
from .player_row import PlayerRowData, PlayerRowPart, fetch_player_row
from .registry import (
    LockOrderError,
    PlayerNotFoundError,
    PlayerRegistry,
    RegistrySettings,
    SessionFactory,
    load_player_aggregate,
)

__all__ = [
    "REPLACE_CORRUPTION_COOLDOWNS_SQL",
    "DbSession",
    "Exposure",
    "InventoryData",
    "LockOrderError",
    "LucidityData",
    "Part",
    "PartWrite",
    "PlayerAggregate",
    "PlayerCooldownsPart",
    "PlayerCooldownsView",
    "PlayerExposurePart",
    "PlayerExposureView",
    "PlayerLedgerPart",
    "PlayerInventoryPart",
    "PlayerInventoryView",
    "PlayerLucidityPart",
    "PlayerLucidityView",
    "PlayerNotFoundError",
    "PlayerQuestsPart",
    "PlayerQuestsView",
    "PlayerRegistry",
    "PlayerRowData",
    "PlayerRowPart",
    "PlayerRowView",
    "PlayerView",
    "QuestInstanceData",
    "RegistrySettings",
    "SessionFactory",
    "fetch_player_row",
    "load_player_aggregate",
]
