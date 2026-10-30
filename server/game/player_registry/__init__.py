"""The authoritative in-memory player registry (ADR-029)."""

from .aggregate import PlayerAggregate, PlayerInventoryView, PlayerQuestsView, PlayerRowView, PlayerView
from .part import DbSession, Part, PartWrite
from .player_inventory import InventoryData, PlayerInventoryPart
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
    "DbSession",
    "InventoryData",
    "LockOrderError",
    "Part",
    "PartWrite",
    "PlayerAggregate",
    "PlayerInventoryPart",
    "PlayerInventoryView",
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
