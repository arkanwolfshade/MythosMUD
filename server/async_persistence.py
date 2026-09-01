"""
Async persistence layer for MythosMUD.

This module provides an async version of the persistence layer using SQLAlchemy ORM
for true async PostgreSQL database operations without blocking the event loop.

This is now a facade that delegates to focused async repositories.
"""

# Facade exposes RoomCacheLoader._* helpers via async_persistence_room_facade (unit tests).

# pylint: disable=too-many-public-methods
# Reason: Facade legitimately exposes many public methods; helpers live in
# async_persistence_room_loader, async_persistence_constants, async_persistence_direct_queries,
# async_persistence_types, and async_persistence_room_facade.

from __future__ import annotations

import asyncio
import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Unpack, cast

from structlog.stdlib import BoundLogger

from .async_persistence_constants import (
    PROFESSION_COLUMNS,
    CreateItemInstanceInput,
    EnsureItemInstanceInput,
)
from .async_persistence_direct_queries import fetch_professions, fetch_user_by_username_case_insensitive
from .async_persistence_room_facade import AsyncPersistenceRoomFacade
from .async_persistence_room_loader import RoomCacheLoader
from .async_persistence_types import (
    ContainerCreateKwargs,
    InstanceRoomLookup,
    PlayerEffectOptions,
)
from .events import EventBus
from .models.player import Player
from .models.player_effect import PlayerEffect
from .models.profession import Profession
from .models.user import User
from .persistence.container_create_params import ContainerCreateParams
from .persistence.protocols import PlayerRepositoryProtocol, RoomRepositoryProtocol
from .persistence.repositories import (
    ContainerRepository,
    ExperienceRepository,
    HealthRepository,
    ItemRepository,
    PlayerEffectRepository,
    PlayerRepository,
    ProfessionRepository,
    RoomRepository,
)
from .persistence.repositories.player_effect_repository import AddEffectInput
from .structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from .models.room import Room

logger = get_logger(__name__)

__all__ = [
    "AsyncPersistenceLayer",
    "PROFESSION_COLUMNS",
]


class AsyncPersistenceLayer(AsyncPersistenceRoomFacade):  # pylint: disable=too-many-instance-attributes  # Reason: Persistence layer requires multiple repository instances and caches
    """
    Async persistence layer using SQLAlchemy ORM for true async PostgreSQL operations.

    This provides async database operations that don't block the event loop.
    Uses SQLAlchemy ORM with async sessions for type-safe, maintainable queries.
    """

    _event_bus: EventBus | None
    _logger: BoundLogger
    _room_cache: dict[str, Room]
    _room_mappings: dict[str, object]
    _room_cache_loaded: bool
    _room_cache_loading: asyncio.Lock | None
    _room_repo: RoomRepositoryProtocol
    _player_repo: PlayerRepositoryProtocol
    _profession_repo: ProfessionRepository
    _experience_repo: ExperienceRepository
    _health_repo: HealthRepository
    _container_repo: ContainerRepository
    _item_repo: ItemRepository
    _player_effect_repo: PlayerEffectRepository
    _instance_manager: InstanceRoomLookup | None
    _room_loader: RoomCacheLoader

    def __init__(
        self,
        _db_path: str | None = None,
        _log_path: str | None = None,
        event_bus: EventBus | None = None,
        _skip_room_cache: bool = False,
    ) -> None:
        """
        Initialize the async persistence layer.

        This facade delegates to focused async repositories for better maintainability.

        Args:
            _db_path: Deprecated - kept for backward compatibility only
            _log_path: Deprecated - kept for backward compatibility only
            event_bus: Optional event bus for publishing events
            _skip_room_cache: Deprecated - room cache is now loaded lazily via warmup_room_cache()
                             or on first async access. This parameter is kept for backward compatibility.
        """
        # Parameters prefixed with _ are kept for backward compatibility but not used
        # Database connection is managed by SQLAlchemy via get_async_session()
        # Logging is managed by enhanced_logging_config
        self._event_bus = event_bus
        self._logger = get_logger(__name__)
        self._room_cache = {}
        self._room_mappings = {}
        self._room_cache_loaded = False
        self._room_cache_loading = None  # Will be created on first async access
        # Don't load room cache during __init__ - use lazy loading instead
        # Room cache will be loaded on first access or via warmup_room_cache()
        # The _skip_room_cache parameter is deprecated but kept for backward compatibility

        # Initialize repositories (facade pattern). Typed to protocols for dependency inversion (ADR-005).
        self._room_repo = RoomRepository(self._room_cache)
        self._player_repo = PlayerRepository(self._room_cache, event_bus)
        self._profession_repo = ProfessionRepository()
        self._experience_repo = ExperienceRepository(event_bus=event_bus)
        self._health_repo = HealthRepository(event_bus=event_bus)
        self._container_repo = ContainerRepository()
        self._item_repo = ItemRepository()
        self._player_effect_repo = PlayerEffectRepository()
        self._instance_manager = None
        self._room_loader = RoomCacheLoader(self._room_cache, self._room_mappings, self._logger, event_bus)

    def set_instance_manager(self, instance_manager: InstanceRoomLookup) -> None:
        """Set the instance manager for instanced room lookup (instance-first)."""
        self._instance_manager = instance_manager

    async def close(self) -> None:
        """Close and cleanup resources.

        Note: SQLAlchemy async sessions are managed by the session context manager,
        so no explicit cleanup is needed here. This method is kept for backward compatibility.
        """
        self._logger.debug("AsyncPersistenceLayer.close() called - no cleanup needed (sessions managed by context)")

    async def get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name. Delegates to PlayerRepository."""
        # Ensure room cache is loaded before validation (validate_and_fix_player_room checks cache)
        await self._ensure_room_cache_loaded()
        return await self._player_repo.get_player_by_name(name)

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        """Get a player by ID. Delegates to PlayerRepository."""
        # Ensure room cache is loaded before validation (validate_and_fix_player_room checks cache)
        await self._ensure_room_cache_loaded()
        return await self._player_repo.get_player_by_id(player_id)

    async def get_players_by_user_id(self, user_id: str) -> list[Player]:
        """Get all players (including deleted) for a user ID. Delegates to PlayerRepository."""
        # Ensure room cache is loaded before validation (validate_and_fix_player_room checks cache)
        await self._ensure_room_cache_loaded()
        return await self._player_repo.get_players_by_user_id(user_id)

    async def get_active_players_by_user_id(self, user_id: str) -> list[Player]:
        """Get active (non-deleted) players for a user ID. Delegates to PlayerRepository."""
        # Ensure room cache is loaded before validation (validate_and_fix_player_room checks cache)
        await self._ensure_room_cache_loaded()
        return await self._player_repo.get_active_players_by_user_id(user_id)

    async def get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get the first active player by user ID (backward compatibility). Delegates to PlayerRepository."""
        # Ensure room cache is loaded before validation (validate_and_fix_player_room checks cache)
        await self._ensure_room_cache_loaded()
        return await self._player_repo.get_player_by_user_id(user_id)

    async def soft_delete_player(self, player_id: uuid.UUID) -> bool:
        """Soft delete a player (sets is_deleted=True). Delegates to PlayerRepository."""
        return await self._player_repo.soft_delete_player(player_id)

    async def get_user_by_username_case_insensitive(self, username: str) -> User | None:
        """
        Get a user by username (case-insensitive).

        MULTI-CHARACTER: Usernames are stored case-sensitively but checked case-insensitively for uniqueness.
        """
        return await fetch_user_by_username_case_insensitive(username)

    async def save_player(self, player: Player) -> None:
        """Save a player. Delegates to PlayerRepository."""
        return await self._player_repo.save_player(player)

    async def list_players(self) -> list[Player]:
        """List all players. Delegates to PlayerRepository."""
        # Ensure room cache is loaded before validation (validate_and_fix_player_room checks cache)
        await self._ensure_room_cache_loaded()
        return await self._player_repo.list_players()

    def get_room_by_id(self, room_id: str) -> Room | None:
        """
        Get a room by ID. Checks instance manager first, then cache.

        Instanced room IDs (instance_*) are looked up via InstanceManager.
        Static rooms are resolved from the room cache.
        """
        if self._instance_manager and room_id and room_id.startswith("instance_"):
            inst_room = self._instance_manager.get_room_by_id(room_id)
            if inst_room is not None:
                return inst_room
        return self._room_repo.get_room_by_id(room_id)

    async def warmup_room_cache(self) -> None:
        """
        Warm up the room cache during application startup.

        This method should be called during app startup to preload the room cache
        and warm up the database connection pool.
        """
        await self._ensure_room_cache_loaded()

    def list_rooms(self) -> list[Room]:
        """
        List all rooms from the cache. Delegates to RoomRepository.

        Returns:
            list[Room]: List of all cached rooms
        """
        return self._room_repo.list_rooms()

    async def async_list_rooms(self) -> list[Room]:
        """
        List all rooms from the cache. Delegates to RoomRepository.

        Returns:
            list[Room]: List of all cached rooms

        Note: This is async for API consistency, though the underlying
        operation is synchronous as rooms are cached in memory.
        """
        # RoomRepository.list_rooms() is synchronous but we expose it as async
        # for consistency with the async API surface
        return self._room_repo.list_rooms()

    async def get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players in a specific room. Delegates to PlayerRepository."""
        # Ensure room cache is loaded before validation (validate_and_fix_player_room checks cache)
        await self._ensure_room_cache_loaded()
        return await self._player_repo.get_players_in_room(room_id)

    async def get_players_batch(self, player_ids: list[uuid.UUID]) -> dict[uuid.UUID, Player]:
        """
        Get multiple players by IDs in a single batch query.

        This method uses a single database query with IN clause instead of
        N individual queries, significantly improving performance.

        Args:
            player_ids: List of player UUIDs to retrieve

        Returns:
            dict: Mapping of player_id (as UUID) to Player object (only includes found players)
        """
        # Ensure room cache is loaded before validation (validate_and_fix_player_room checks cache)
        await self._ensure_room_cache_loaded()
        if not player_ids:
            return {}

        # Use repository batch method which uses single query with IN clause
        players_list = await self._player_repo.get_players_batch(player_ids)

        # Convert list to dict keyed by UUID (Player.player_id is str type, convert to UUID for dict key)
        return {uuid.UUID(player.player_id): player for player in players_list}

    async def save_players(self, players: list[Player]) -> None:
        """Save multiple players in a single transaction. Delegates to PlayerRepository."""
        return await self._player_repo.save_players(players)

    async def delete_player(self, player_id: uuid.UUID) -> bool:
        """Delete a player. Delegates to PlayerRepository."""
        return await self._player_repo.delete_player(player_id)

    async def update_player_last_active(self, player_id: uuid.UUID, last_active: datetime | None = None) -> None:
        """Update the last_active timestamp for a player. Delegates to PlayerRepository."""
        await self._player_repo.update_player_last_active(player_id, last_active)

    async def get_professions(self) -> list[Profession]:
        """Get all available professions using SQLAlchemy ORM."""
        return await fetch_professions()

    async def get_profession_by_id(self, profession_id: int) -> Profession | None:
        """Get a profession by ID. Delegates to ProfessionRepository."""
        return await self._profession_repo.get_profession_by_id(profession_id)

    def validate_and_fix_player_room(self, player: Player) -> bool:
        """Validate and fix player room if needed. Delegates to PlayerRepository."""
        return self._player_repo.validate_and_fix_player_room(player)

    async def apply_lucidity_loss(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Apply lucidity loss to a player. Delegates to ExperienceRepository."""
        player_id = uuid.UUID(str(player.player_id))  # Convert Column to UUID for type checking
        await self._experience_repo.update_player_stat_field(player_id, "lucidity", -amount, f"{source}: lucidity loss")

    async def apply_fear(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Apply fear to a player. Delegates to ExperienceRepository."""
        player_id = uuid.UUID(str(player.player_id))  # Convert Column to UUID for type checking
        await self._experience_repo.update_player_stat_field(player_id, "fear", amount, f"{source}: fear increase")

    async def apply_corruption(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Apply corruption to a player. Delegates to ExperienceRepository."""
        player_id = uuid.UUID(str(player.player_id))  # Convert Column to UUID for type checking
        await self._experience_repo.update_player_stat_field(
            player_id, "corruption", amount, f"{source}: corruption increase"
        )

    async def gain_occult_knowledge(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Gain occult knowledge for a player. Delegates to ExperienceRepository."""
        player_id = uuid.UUID(str(player.player_id))  # Convert Column to UUID for type checking
        await self._experience_repo.update_player_stat_field(
            player_id, "occult_knowledge", amount, f"{source}: occult knowledge gain"
        )

    async def gain_experience(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Award experience to a player atomically. Delegates to ExperienceRepository."""
        await self._experience_repo.gain_experience(player, amount, source)

    async def heal_player(self, player: Player, amount: int) -> None:
        """Heal a player. Delegates to HealthRepository."""
        await self._health_repo.heal_player(player, amount)

    async def async_heal_player(self, player: Player, amount: int) -> None:
        """Async alias for heal_player. Delegates to HealthRepository."""
        await self._health_repo.heal_player(player, amount)

    async def damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """Damage a player. Delegates to HealthRepository."""
        await self._health_repo.damage_player(player, amount, damage_type)

    async def async_damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """Async alias for damage_player. Delegates to HealthRepository."""
        await self._health_repo.damage_player(player, amount, damage_type)

    # Player effects (ADR-019)
    async def add_player_effect(
        self,
        player_id: uuid.UUID | str,
        effect_type: str,
        category: str,
        duration: int,
        applied_at_tick: int,
        options: PlayerEffectOptions | None = None,
    ) -> str:
        """Add a player effect. Returns effect id."""
        effect_options = options or {}
        payload: AddEffectInput = {
            "effect_type": effect_type,
            "category": category,
            "duration": duration,
            "applied_at_tick": applied_at_tick,
            "intensity": effect_options.get("intensity", 1),
            "source": effect_options.get("source"),
            "visibility_level": effect_options.get("visibility_level", "visible"),
        }
        return await self._player_effect_repo.add_effect(player_id, payload)

    async def remove_player_effect_by_id(self, effect_id: uuid.UUID | str) -> None:
        """Remove a player effect by id."""
        await self._player_effect_repo.delete_effect(effect_id)

    async def get_active_player_effects(self, player_id: uuid.UUID | str, current_tick: int) -> list[PlayerEffect]:
        """Get active effects for a player (remaining_ticks > 0). Returns list of PlayerEffect."""
        return await self._player_effect_repo.get_active_effects_for_player(player_id, current_tick)

    async def has_player_effect(self, player_id: uuid.UUID | str, effect_type: str, current_tick: int) -> bool:
        """Return True if player has an active effect of the given type."""
        return await self._player_effect_repo.has_effect(player_id, effect_type, current_tick)

    async def get_player_effect_remaining_ticks(
        self, player_id: uuid.UUID | str, effect_type: str, current_tick: int
    ) -> int | None:
        """Return remaining ticks for the effect, or None."""
        return await self._player_effect_repo.get_effect_remaining_ticks(player_id, effect_type, current_tick)

    async def expire_player_effects_for_tick(self, current_tick: int) -> list[tuple[str, str]]:
        """Expire effects for current tick; return list of (player_id, effect_type) expired."""
        return await self._player_effect_repo.expire_effects_for_tick(current_tick)

    # Container methods
    async def create_container(
        self,
        source_type: str,
        params: ContainerCreateParams | None = None,
        **kwargs: Unpack[ContainerCreateKwargs],
    ) -> dict[str, object]:
        """
        Create a new container.

        Args:
            source_type: Type of container source (required)
            params: ContainerCreateParams object with all optional parameters (preferred)
            **kwargs: Individual parameters for backward compatibility

        Returns:
            dict: Container data dictionary
        """
        # Use params object if provided, otherwise create from kwargs
        if params is None:
            params = ContainerCreateParams(
                owner_id=kwargs.get("owner_id"),
                room_id=kwargs.get("room_id"),
                entity_id=kwargs.get("entity_id"),
                lock_state=kwargs.get("lock_state", "unlocked"),
                capacity_slots=kwargs.get("capacity_slots", 20),
                weight_limit=kwargs.get("weight_limit"),
                decay_at=kwargs.get("decay_at"),
                allowed_roles=kwargs.get("allowed_roles"),
                items_json=kwargs.get("items_json"),
                metadata_json=kwargs.get("metadata_json"),
            )

        return cast(dict[str, object], await self._container_repo.create_container(source_type, params))

    async def get_container(self, container_id: uuid.UUID) -> dict[str, object] | None:
        """Get a container by ID."""
        return cast(dict[str, object] | None, await self._container_repo.get_container(container_id))

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, object]]:
        """Get all containers in a room."""
        return cast(list[dict[str, object]], await self._container_repo.get_containers_by_room_id(room_id))

    async def get_containers_by_entity_id(self, entity_id: uuid.UUID) -> list[dict[str, object]]:
        """Get all containers owned by an entity."""
        return cast(list[dict[str, object]], await self._container_repo.get_containers_by_entity_id(entity_id))

    async def update_container(
        self,
        container_id: uuid.UUID,
        items_json: list[dict[str, object]] | None = None,
        lock_state: str | None = None,
        metadata_json: dict[str, object] | None = None,
    ) -> dict[str, object] | None:
        """Update a container."""
        return cast(
            dict[str, object] | None,
            await self._container_repo.update_container(container_id, items_json, lock_state, metadata_json),
        )

    async def get_decayed_containers(self, current_time: datetime | None = None) -> list[dict[str, object]]:
        """Get decayed containers."""
        return cast(list[dict[str, object]], await self._container_repo.get_decayed_containers(current_time))

    async def delete_container(self, container_id: uuid.UUID) -> bool:
        """Delete a container."""
        return await self._container_repo.delete_container(container_id)

    # Item methods
    async def create_item_instance(
        self,
        item_instance_id: str,
        prototype_id: str,
        data: CreateItemInstanceInput | None = None,
    ) -> None:
        """Create a new item instance. Delegates to ItemRepository."""
        d = data or {}
        return await self._item_repo.create_item_instance(
            item_instance_id,
            prototype_id,
            d,
        )

    async def ensure_item_instance(
        self,
        item_instance_id: str,
        prototype_id: str,
        **kwargs: Unpack[EnsureItemInstanceInput],
    ) -> None:
        """
        Ensure an item instance exists. Delegates to ItemRepository.

        Accepts keyword arguments for owner_type, owner_id, quantity, metadata,
        origin_source, and origin_metadata to stay compatible with existing
        call sites while keeping the formal parameter count low for Lizard.
        """
        payload: EnsureItemInstanceInput = {
            "owner_type": kwargs.get("owner_type", "room"),
            "owner_id": kwargs.get("owner_id"),
            "quantity": kwargs.get("quantity", 1),
            "metadata": kwargs.get("metadata"),
            "origin_source": kwargs.get("origin_source"),
            "origin_metadata": kwargs.get("origin_metadata"),
        }

        return await self._item_repo.ensure_item_instance(item_instance_id, prototype_id, payload)

    async def item_instance_exists(self, item_instance_id: str) -> bool:
        """Check if an item instance exists. Delegates to ItemRepository."""
        return await self._item_repo.item_instance_exists(item_instance_id)
