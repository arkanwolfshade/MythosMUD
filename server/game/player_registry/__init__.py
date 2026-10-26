"""The authoritative in-memory player registry (ADR-029)."""

from .aggregate import PlayerAggregate, PlayerRowView, PlayerView
from .part import DbSession, Part, PartWrite
from .player_row import PlayerRowData, PlayerRowPart, load_player_row
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
    "LockOrderError",
    "Part",
    "PartWrite",
    "PlayerAggregate",
    "PlayerNotFoundError",
    "PlayerRegistry",
    "PlayerRowData",
    "PlayerRowPart",
    "PlayerRowView",
    "PlayerView",
    "RegistrySettings",
    "SessionFactory",
    "load_player_aggregate",
    "load_player_row",
]
