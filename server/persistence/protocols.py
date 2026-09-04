"""
Repository protocols for MythosMUD persistence layer.

Explicit typing.Protocol definitions for key repositories (ADR-005).
Enables dependency inversion: facade and container can depend on protocols
instead of concrete classes for better testability.
"""

# pylint: disable=unnecessary-ellipsis  # Reason: Protocol method bodies use ... per typing.Protocol convention

from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from server.models.player import Player
    from server.models.room import Room


class PlayerRepositoryProtocol(Protocol):
    """
    Protocol for player persistence operations.

    Defines the contract used by AsyncPersistenceLayer and services.
    Implemented by server.persistence.repositories.player_repository.PlayerRepository.
    """

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        """Get a player by ID."""
        ...

    async def get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get the first active player for a user ID."""
        ...

    async def get_players_by_user_id(self, user_id: str) -> list[Player]:
        """Get all players (including deleted) for a user ID."""
        ...

    async def get_active_players_by_user_id(self, user_id: str) -> list[Player]:
        """Get active (non-deleted) players for a user ID."""
        ...

    async def get_player_by_name(self, name: str) -> Player | None:
        """Get an active player by name (case-insensitive)."""
        ...

    async def save_player(self, player: Player) -> None:
        """Save a player to the database."""
        ...

    async def save_players(self, players: list[Player]) -> None:
        """Save multiple players in a single transaction."""
        ...

    async def list_players(self) -> list[Player]:
        """List all players."""
        ...

    async def get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players in a specific room."""
        ...

    async def get_players_batch(self, player_ids: list[uuid.UUID]) -> list[Player]:
        """Get multiple players by IDs in a single query."""
        ...

    async def soft_delete_player(self, player_id: uuid.UUID) -> bool:
        """Soft delete a player (sets is_deleted=True)."""
        ...

    async def delete_player(self, player_id: uuid.UUID) -> bool:
        """Delete a player from the database."""
        ...

    async def update_player_last_active(self, player_id: uuid.UUID, last_active: datetime | None = None) -> None:
        """Update the last_active timestamp for a player."""
        ...

    def validate_and_fix_player_room(self, player: Player) -> bool:
        """Validate player's current room and fix if invalid."""
        ...


class RoomRepositoryProtocol(Protocol):
    """
    Protocol for room persistence operations.

    Defines the contract used by AsyncPersistenceLayer and services.
    Implemented by server.persistence.repositories.room_repository.RoomRepository.
    """

    def get_room_by_id(self, room_id: str) -> Room | None:
        """Get a room by ID from cache."""
        ...

    def list_rooms(self) -> list[Room]:
        """List all cached rooms."""
        ...
