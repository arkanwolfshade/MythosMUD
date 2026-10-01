"""
Corpse lifecycle service for unified container system.

As documented in the restricted archives of Miskatonic University, corpse
lifecycle automation requires careful orchestration to ensure proper handling
of player death, grace periods, decay timers, and item redistribution.
"""

# pylint: disable=too-many-return-statements  # Reason: Corpse lifecycle methods require multiple return statements for early validation returns (state checks, permission validation, error handling)
# pylint: disable=too-many-lines  # Reason: The service owns the whole corpse lifecycle (create, grace period, decay, loot redistribution); moving a dying player's gear onto the corpse (#917) pushed it past the limit, and splitting the lifecycle is a larger refactor than that fix

from __future__ import annotations

import uuid
from collections.abc import Mapping
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING, Any, Protocol, cast, runtime_checkable
from uuid import UUID

from ..exceptions import MythosMUDError
from ..models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from ..structured_logging.enhanced_logging_config import get_logger

# Removed: from ..persistence import get_persistence - now using async_persistence parameter
from ..utils.error_logging import log_and_raise

if TYPE_CHECKING:
    from .inventory_service import InventoryStack

logger = get_logger(__name__)


class CorpseConnectionManagerLike(Protocol):
    """Minimal shape _emit_corpse_created needs from a connection manager.

    Declared locally (not imported from container_websocket_events.py) because
    this service sits on the combat_service -> ... -> wearable_container_service
    import chain, which already cycles back to models/container.py; importing
    that module here -- even for a type only -- would close a second cycle.
    """

    async def broadcast_room_event(self, event_type: str, room_id: str, data: dict[str, object]) -> dict[str, object]:
        """Broadcast an event to everyone in a room; returns delivery stats."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


@runtime_checkable
class _RoomContainers(Protocol):
    """The in-memory Room's container registry (server/models/room.py::Room).

    An isinstance check against this replaces getattr(room, "add_container", None) + callable(),
    which some pylint versions cannot follow and report as "add_container is not callable".
    """

    def add_container(self, container: dict[str, object]) -> None:
        """Register a runtime-created container so room_state carries it."""

    def remove_container(self, container_id: str) -> None:
        """Drop a container from the room."""


class _SyncRoomLookup(Protocol):
    """The synchronous room lookup _live_room needs from a persistence layer."""

    def get_room_by_id(self, room_id: str) -> object:
        """Return the in-memory Room for room_id (may be an awaitable on async-only layers)."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


class _DyingPlayer(Protocol):
    """The slice of Player that moving a dead player's gear onto a corpse reads (#917)."""

    def get_inventory(self) -> list[dict[str, object]]:
        """Carried stacks."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type

    def get_equipped_items(self) -> dict[str, object]:
        """Equipped stacks keyed by slot."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


class _DeathPersistence(Protocol):
    """The persistence calls moving a dead player's gear onto a corpse makes (#917)."""

    async def get_containers_by_entity_id(self, entity_id: UUID) -> list[dict[str, object]]:
        """Containers owned by an entity (a player's worn-container rows)."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type

    async def delete_container(self, container_id: UUID) -> bool:
        """Delete a container row."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type

    async def clear_player_inventory(self, player_id: UUID) -> bool:
        """Empty only the player's carried and equipped items (never stats: no race with the DP write)."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


# containers_capacity_slots_check in db/schema.sql: a container holds 1..20 stacks.
_CORPSE_MAX_SLOTS = 20


def _get_enum_value(enum_or_str: Any) -> str:
    """
    Safely get enum value, handling both enum instances and string values.

    When containers are deserialized from the database, enum fields may be strings
    instead of enum instances. This helper handles both cases.

    Args:
        enum_or_str: Either an enum instance or a string value

    Returns:
        String value of the enum
    """
    if hasattr(enum_or_str, "value"):
        result: str = cast(str, enum_or_str.value)
        return result
    return str(enum_or_str)


def _filter_container_data(container_data: dict[str, Any]) -> dict[str, Any]:
    """
    Filter out database-specific fields that are not part of the ContainerComponent model.

    The database returns created_at and updated_at fields, but the ContainerComponent
    model has extra="forbid", so these fields must be removed before validation.

    Also converts items_json to items and metadata_json to metadata to match
    the ContainerComponent model field names.

    Args:
        container_data: Raw container data from database

    Returns:
        Filtered container data without database-specific fields, with field names converted
    """
    filtered = {k: v for k, v in container_data.items() if k not in ("created_at", "updated_at")}

    # Convert items_json to items and metadata_json to metadata for ContainerComponent model
    if "items_json" in filtered:
        filtered["items"] = filtered.pop("items_json")
    if "metadata_json" in filtered:
        filtered["metadata"] = filtered.pop("metadata_json")

    return filtered


def _inner_container_of(worn: ContainerComponent) -> dict[str, object]:
    """A worn container's live contents as a stack's `inner_container` (same shape unequip produces)."""
    inner: dict[str, object] = {
        "capacity_slots": worn.capacity_slots,
        "items": worn.items,
        "lock_state": _get_enum_value(worn.lock_state),
    }
    if worn.allowed_roles:
        inner["allowed_roles"] = worn.allowed_roles
    return inner


class CorpseServiceError(MythosMUDError):
    """Base exception for corpse service operations."""


class CorpseNotFoundError(CorpseServiceError):
    """Raised when a corpse container is not found."""


class CorpseLifecycleService:
    """
    Service for managing corpse container lifecycle.

    Handles creation on death, grace period enforcement, decay timers,
    and cleanup with item redistribution.
    """

    def __init__(
        self,
        persistence: Any | None = None,
        connection_manager: CorpseConnectionManagerLike | None = None,
        time_service: Any | None = None,
    ) -> None:
        """
        Initialize the corpse lifecycle service.

        Args:
            persistence: Persistence layer instance (optional, will get if not provided)
            connection_manager: ConnectionManager instance for WebSocket events (optional)
            time_service: Time service instance for decay checks (optional)
        """
        if persistence is None:
            raise ValueError("persistence (async_persistence) is required for CorpseLifecycleService")
        self.persistence = persistence
        self.connection_manager = connection_manager
        self.time_service = time_service

    def _build_corpse_component(
        self,
        player_id: UUID,
        room_id: str,
        player: _DyingPlayer,
        items: list[dict[str, object]],
        grace_period_seconds: int,
        decay_hours: int,
    ) -> ContainerComponent:
        now = datetime.now(UTC)
        return ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.CORPSE,
            owner_id=player_id,
            room_id=room_id,
            capacity_slots=_CORPSE_MAX_SLOTS,
            lock_state=ContainerLockState.UNLOCKED,
            decay_at=now + timedelta(hours=decay_hours),
            items=cast("list[InventoryStack]", items),
            metadata={
                "grace_period_seconds": grace_period_seconds,
                "grace_period_start": now.isoformat(),
                "player_name": getattr(player, "name", "Unknown"),
                "death_timestamp": now.isoformat(),
            },
        )

    async def _persist_corpse(self, corpse: ContainerComponent, player_id: UUID, room_id: str) -> ContainerComponent:
        try:
            items_dicts: list[dict[str, Any]] = [
                cast(dict[str, Any], dict(item) if not isinstance(item, dict) else item) for item in corpse.items
            ]
            container_data = await self.persistence.create_container(
                source_type=_get_enum_value(corpse.source_type),
                owner_id=corpse.owner_id,
                room_id=corpse.room_id,
                capacity_slots=corpse.capacity_slots,
                decay_at=corpse.decay_at,
                items_json=items_dicts,
                metadata_json=corpse.metadata,
            )
            corpse.container_id = UUID(container_data["container_id"])
            logger.info(
                "Corpse container created",
                container_id=str(corpse.container_id),
                player_id=str(player_id),
                room_id=room_id,
                items_count=len(corpse.items),
            )
            self._register_corpse_on_room(corpse, room_id)
            await self._emit_corpse_created(corpse, room_id)
            return corpse
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Convert to domain exception - corpse creation errors unpredictable
            log_and_raise(
                CorpseServiceError,
                f"Failed to create corpse container: {str(e)}",
                operation="create_corpse_on_death",
                player_id=str(player_id),
                room_id=room_id,
                details={"player_id": str(player_id), "room_id": room_id},
                user_friendly="Failed to create corpse container",
            )

    def _register_corpse_on_room(self, corpse: ContainerComponent, room_id: str) -> None:
        """Add the corpse to the in-memory Room so room_state carries it (#711).

        The container.created broadcast only reaches players subscribed at that instant, which
        never includes the corpse's own owner -- they are dead when it spawns. Registering it on
        the Room means the summary rides along in room_state on (re)entry and respawn, so the
        owner can actually see and loot their own corpse.
        """
        try:
            room = self._live_room(room_id)
            if not isinstance(room, _RoomContainers):
                return
            room.add_container(
                {
                    "container_id": str(corpse.container_id),
                    "source_type": _get_enum_value(corpse.source_type),
                    "owner_id": str(corpse.owner_id) if corpse.owner_id else None,
                    "decay_at": corpse.decay_at.isoformat() if corpse.decay_at else None,
                    "metadata": corpse.metadata,
                }
            )
        except (AttributeError, TypeError, RuntimeError, ValueError) as e:
            logger.warning("Failed to register corpse on room", error=str(e), room_id=room_id)

    def _unregister_corpse_from_room(self, container_id: str, room_id: str) -> None:
        """Drop a decayed corpse from the in-memory Room (mirror of _register_corpse_on_room)."""
        try:
            room = self._live_room(room_id)
            if isinstance(room, _RoomContainers):
                room.remove_container(container_id)
        except (AttributeError, TypeError, RuntimeError, ValueError) as e:
            logger.warning("Failed to unregister corpse from room", error=str(e), room_id=room_id)

    def _live_room(self, room_id: str) -> object | None:
        """In-memory Room for room_id, or None when persistence exposes no sync lookup."""
        persistence = cast(object, self.persistence)
        if not hasattr(persistence, "get_room_by_id"):
            return None
        room: object = cast(_SyncRoomLookup, persistence).get_room_by_id(room_id)
        # An awaitable means this persistence layer is async-only here; skip rather than block.
        return None if hasattr(room, "__await__") else room

    async def _emit_corpse_created(self, corpse: ContainerComponent, room_id: str) -> None:
        """Best-effort container.created broadcast so room occupants see the fresh corpse.

        Broadcasts inline rather than importing container_websocket_events.emit_container_created:
        this service sits on the combat_service -> ... -> wearable_container_service import
        chain, which already cycles back to models/container.py (a pre-existing,
        baselined cycle -- see server/app/game_tick_corpses.py's own inline-import comment
        for the decay side of this same event family), so importing that module here
        -- even lazily -- closes a second, unbaselined cycle. Keep this payload in sync
        with emit_container_created's event_data shape if that ever changes.
        """
        if self.connection_manager is None:
            return
        try:
            _ = await self.connection_manager.broadcast_room_event(
                event_type="container.created",
                room_id=room_id,
                data={"container": corpse.model_dump(mode="json")},
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event emission errors unpredictable, must not fail corpse creation
            logger.warning(
                "Failed to emit container.created event for corpse",
                error=str(e),
                container_id=str(corpse.container_id),
                room_id=room_id,
            )

    async def create_corpse_on_death(
        self,
        player_id: UUID,
        room_id: str,
        grace_period_seconds: int = 300,
        decay_hours: int = 1,
    ) -> ContainerComponent:
        """Create a corpse container when a player dies."""
        logger.info("Creating corpse container on death", player_id=str(player_id), room_id=room_id)
        player = await self.persistence.get_player_by_id(player_id)
        if not player:
            log_and_raise(
                CorpseServiceError,
                f"Player not found: {player_id}",
                operation="create_corpse_on_death",
                player_id=str(player_id),
                room_id=room_id,
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )
        dying_player = cast(_DyingPlayer, player)
        stacks, worn_container_ids = await self._collect_death_items(dying_player, player_id)
        # ponytail: a container holds at most _CORPSE_MAX_SLOTS stacks, so a full pack plus worn gear
        # spills onto extra corpses rather than dropping items; merge into one if a bigger corpse is ever allowed.
        chunks = [stacks[i : i + _CORPSE_MAX_SLOTS] for i in range(0, len(stacks), _CORPSE_MAX_SLOTS)] or [[]]
        corpses = [
            await self._persist_corpse(
                self._build_corpse_component(
                    player_id, room_id, dying_player, chunk, grace_period_seconds, decay_hours
                ),
                player_id,
                room_id,
            )
            for chunk in chunks
        ]
        await self._strip_player_after_death(player_id, worn_container_ids)
        return corpses[0]

    async def _collect_death_items(
        self, player: _DyingPlayer, player_id: UUID
    ) -> tuple[list[dict[str, object]], list[UUID]]:
        """Everything a dying player drops: carried and equipped stacks, worn containers nested (#917).

        Also returns the worn-container rows whose contents were folded into their stacks, so the
        caller can delete them once the corpse is safely persisted.
        """
        worn_rows = await self._worn_container_rows(player_id)
        equipped: list[dict[str, object]] = []
        claimed: list[UUID] = []
        for raw in player.get_equipped_items().values():
            if not isinstance(raw, Mapping):
                continue
            stack = dict(cast(Mapping[str, object], raw))
            worn = worn_rows.get(str(stack.get("item_instance_id")))
            if worn is not None:
                stack["inner_container"] = _inner_container_of(worn)
                claimed.append(worn.container_id)
            equipped.append(stack)
        return [dict(stack) for stack in player.get_inventory()] + equipped, claimed

    async def _worn_container_rows(self, player_id: UUID) -> dict[str, ContainerComponent]:
        """The player's equipment-container rows (worn backpacks etc.) keyed by their item_instance_id."""
        persistence = cast(_DeathPersistence, self.persistence)
        rows: dict[str, ContainerComponent] = {}
        for raw in await persistence.get_containers_by_entity_id(player_id):
            if raw.get("source_type") != "equipment":
                continue
            try:
                # Persistence returns items_json/metadata_json; _filter_container_data maps them back.
                row = ContainerComponent.model_validate(_filter_container_data(raw))
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: BLE001  # Reason: one unreadable row must not stop a death; it is left in place, not deleted
                logger.warning(
                    "Skipping unreadable worn container row on death", player_id=str(player_id), error=str(e)
                )
                continue
            item_instance_id: object = row.metadata.get("item_instance_id")
            if item_instance_id:
                rows[str(item_instance_id)] = row
        return rows

    async def _strip_player_after_death(self, player_id: UUID, worn_container_ids: list[UUID]) -> None:
        """Clear what moved onto the corpse, so items are moved rather than copied (#917).

        Runs only after the corpse is persisted, and logs instead of raising: the worst case is the
        old duplication (item on corpse and player), never a lost item. Clears the inventory columns
        only; a whole-row save_player here raced the death's DP write and revived the player.
        """
        persistence = cast(_DeathPersistence, self.persistence)
        try:
            _ = await persistence.clear_player_inventory(player_id)
            for container_id in worn_container_ids:
                _ = await persistence.delete_container(container_id)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: BLE001  # Reason: corpse already exists; failing the death sequence here would be worse than logging
            logger.error(
                "Failed to clear player after corpse creation; items now exist on both corpse and player",
                player_id=str(player_id),
                error=str(e),
                exc_info=True,
            )

    def _grace_period_allows_others(self, corpse: ContainerComponent) -> bool:
        grace_period_seconds = corpse.metadata.get("grace_period_seconds", 300)
        grace_period_start_str = corpse.metadata.get("grace_period_start")
        if not grace_period_start_str:
            return True
        try:
            grace_period_start = datetime.fromisoformat(grace_period_start_str.replace("Z", "+00:00"))
            return datetime.now(UTC) >= grace_period_start + timedelta(seconds=grace_period_seconds)
        except (ValueError, TypeError) as e:
            logger.warning(
                "Error parsing grace period",
                error=str(e),
                container_id=str(corpse.container_id),
                grace_period_start=grace_period_start_str,
            )
            return True

    def can_access_corpse(self, corpse: ContainerComponent, player_id: UUID, is_admin: bool = False) -> bool:
        """True if player may access corpse (owner/admin always; others after grace)."""
        if is_admin or not corpse.owner_id or corpse.owner_id == player_id:
            return True
        return self._grace_period_allows_others(corpse)

    def is_corpse_decayed(self, corpse: ContainerComponent) -> bool:
        """
        Check if a corpse container has decayed.

        Args:
            corpse: Corpse container to check

        Returns:
            bool: True if decayed, False otherwise
        """
        if not corpse.decay_at:
            return False

        # Use real UTC time for decay comparison (decay_at is set using real UTC time)
        # Decay timers should use real-world time, not accelerated Mythos time
        current_time = datetime.now(UTC)

        # Normalize decay_at to UTC if needed (handle both timezone-aware and naive datetimes)
        decay_at = corpse.decay_at
        if decay_at.tzinfo is None:
            # If naive, assume UTC
            decay_at = decay_at.replace(tzinfo=UTC)
        else:
            # If timezone-aware, convert to UTC
            decay_at = decay_at.astimezone(UTC)

        return current_time >= decay_at

    async def get_decayed_corpses_in_room(self, room_id: str) -> list[ContainerComponent]:
        """
        Get all decayed corpse containers in a room.

        Args:
            room_id: Room ID to check

        Returns:
            list[ContainerComponent]: List of decayed corpse containers
        """
        # Get all containers in room
        containers_data = await self.persistence.get_containers_by_room_id(room_id)
        if not containers_data:
            return []

        decayed = []
        for container_data in containers_data:
            try:
                filtered_data = _filter_container_data(container_data)
                container = ContainerComponent.model_validate(filtered_data)
                if container.source_type == ContainerSourceType.CORPSE and self.is_corpse_decayed(container):
                    decayed.append(container)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Continue processing other containers on error - individual container errors should not stop batch operations
                logger.warning(
                    "Error validating container for decay check",
                    error=str(e),
                    container_data=container_data,
                )
                continue

        return decayed

    def _require_corpse_container(self, container_id: UUID, container_data: dict[str, Any]) -> ContainerComponent:
        container = ContainerComponent.model_validate(_filter_container_data(container_data))
        if container.source_type != ContainerSourceType.CORPSE:
            log_and_raise(
                CorpseServiceError,
                f"Container is not a corpse: {container_id}",
                operation="cleanup_decayed_corpse",
                container_id=str(container_id),
                details={"container_id": str(container_id), "source_type": _get_enum_value(container.source_type)},
                user_friendly="Container is not a corpse",
            )
        return container

    async def cleanup_decayed_corpse(self, container_id: UUID) -> None:
        """Delete a decayed corpse container (items discarded with the container)."""
        logger.info("Cleaning up decayed corpse", container_id=str(container_id))
        container_data = await self.persistence.get_container(container_id)
        if not container_data:
            log_and_raise(
                CorpseNotFoundError,
                f"Corpse container not found: {container_id}",
                operation="cleanup_decayed_corpse",
                container_id=str(container_id),
                details={"container_id": str(container_id)},
                user_friendly="Corpse container not found",
            )
        container = self._require_corpse_container(container_id, container_data)
        try:
            await self.persistence.delete_container(container_id)
            if container.room_id:
                self._unregister_corpse_from_room(str(container_id), container.room_id)
            logger.info(
                "Decayed corpse cleaned up",
                container_id=str(container_id),
                room_id=container.room_id,
                items_count=len(container.items),
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Convert to domain exception
            log_and_raise(
                CorpseServiceError,
                f"Failed to delete decayed corpse: {str(e)}",
                operation="cleanup_decayed_corpse",
                container_id=str(container_id),
                details={"container_id": str(container_id)},
                user_friendly="Failed to clean up corpse",
            )

    async def cleanup_decayed_corpses_in_room(self, room_id: str) -> int:
        """
        Clean up all decayed corpse containers in a room.

        Args:
            room_id: Room ID to clean up

        Returns:
            int: Number of corpses cleaned up
        """
        logger.info("Cleaning up decayed corpses in room", room_id=room_id)

        decayed = await self.get_decayed_corpses_in_room(room_id)
        cleaned_count = 0

        for corpse in decayed:
            try:
                await self.cleanup_decayed_corpse(corpse.container_id)
                cleaned_count += 1
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Continue processing other corpses on error - individual corpse cleanup errors should not stop batch operations
                logger.error(
                    "Error cleaning up decayed corpse",
                    error=str(e),
                    container_id=str(corpse.container_id),
                    room_id=room_id,
                )
                continue

        logger.info(
            "Decayed corpses cleanup completed",
            room_id=room_id,
            cleaned_count=cleaned_count,
            total_decayed=len(decayed),
        )

        return cleaned_count

    async def get_all_decayed_corpses(self) -> list[ContainerComponent]:
        """
        Get all decayed corpse containers across all rooms.

        Returns:
            list[ContainerComponent]: List of all decayed corpse containers
        """
        # Use real UTC time for decay comparison (decay_at is set using real UTC time)
        # Decay timers should use real-world time, not accelerated Mythos time
        current_time = datetime.now(UTC)

        logger.debug(
            "Checking for decayed corpses",
            current_time=current_time.isoformat(),
        )

        # Get all decayed containers from persistence
        decayed_data = await self.persistence.get_decayed_containers(current_time)
        if not decayed_data:
            logger.debug("No decayed containers found", current_time=current_time.isoformat())
            return []

        decayed_corpses = []
        for container_data in decayed_data:
            try:
                filtered_data = _filter_container_data(container_data)
                container = ContainerComponent.model_validate(filtered_data)
                if container.source_type == ContainerSourceType.CORPSE:
                    decayed_corpses.append(container)
                    logger.debug(
                        "Found decayed corpse",
                        container_id=str(container.container_id),
                        room_id=container.room_id,
                        decay_at=container.decay_at.isoformat() if container.decay_at else None,
                        current_time=current_time.isoformat(),
                    )
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Continue processing other containers on error - individual container errors should not stop batch operations
                logger.warning(
                    "Error validating decayed container",
                    error=str(e),
                    container_data=container_data,
                )
                continue

        logger.debug(
            "Decayed corpses found",
            total_containers=len(decayed_data),
            corpse_count=len(decayed_corpses),
        )

        return decayed_corpses

    async def cleanup_all_decayed_corpses(self) -> int:
        """
        Clean up all decayed corpse containers across all rooms.

        Returns:
            int: Number of corpses cleaned up
        """
        logger.info("Cleaning up all decayed corpses")

        decayed = await self.get_all_decayed_corpses()
        cleaned_count = 0

        for corpse in decayed:
            try:
                await self.cleanup_decayed_corpse(corpse.container_id)
                cleaned_count += 1
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Continue processing other corpses on error - individual corpse cleanup errors should not stop batch operations
                logger.error(
                    "Error cleaning up decayed corpse",
                    error=str(e),
                    container_id=str(corpse.container_id),
                )
                continue

        logger.info(
            "All decayed corpses cleanup completed",
            cleaned_count=cleaned_count,
            total_decayed=len(decayed),
        )

        return cleaned_count
