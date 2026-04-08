"""
Protocols and module-level helpers for player combat XP and lifecycle lookup.

Split from player_combat_service to keep the main service module under Lizard nloc limits.
"""

from __future__ import annotations

import asyncio
from typing import Protocol, cast
from uuid import UUID

from structlog.stdlib import BoundLogger

from server.npc.lifecycle_manager import NPCLifecycleManager
from server.structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = get_logger(__name__)


class EventBusPublish(Protocol):
    """Minimal event bus surface used by player combat service."""

    def publish(self, event: object) -> None:
        """Publish a domain event."""
        raise NotImplementedError


class NPCCombatRewardsLike(Protocol):
    """NPC combat rewards helper."""

    async def award_xp_to_killer(self, killer_id: str, npc_id: str, _xp: int) -> None:
        """Award XP to the killer for an NPC defeat."""
        raise NotImplementedError


class UUIDMappingXP(Protocol):
    """UUID mapping helper with XP lookup (NPCCombatUUIDMapping)."""

    def get_xp_value(self, npc_id: UUID) -> int | None:
        """Return stored XP for npc_id when present."""
        raise NotImplementedError


class NPCCombatIntegrationReadApi(Protocol):
    """Public read API from NPC combat integration."""

    def get_rewards_service(self) -> NPCCombatRewardsLike | None:
        """Return rewards helper service."""
        raise NotImplementedError

    def get_uuid_mapping(self) -> UUIDMappingXP:
        """Return UUID mapping helper."""
        raise NotImplementedError


class PlayerXpLike(Protocol):
    """Minimal player surface for XP persistence fallback."""

    name: object
    level: int

    def add_experience(self, amount: int) -> None:
        """Apply XP gain."""
        raise NotImplementedError


class PersistenceWithNpcLifecycleManager(Protocol):
    """Persistence layer that can expose the NPC lifecycle manager."""

    def get_npc_lifecycle_manager(self) -> object:
        """Return lifecycle manager (sync); may be wrapped by asyncio.to_thread."""
        raise NotImplementedError


def original_string_id_for_npc(integration: object | None, npc_id: UUID) -> str | None:
    """Return mapped original NPC string id when integration exposes it."""
    if integration is None:
        return None
    get_original = getattr(integration, "get_original_string_id", None)
    if not callable(get_original):
        return None
    original = get_original(npc_id)
    return str(original) if original is not None else None


def lifecycle_lookup_id(integration: object | None, npc_id: UUID) -> str:
    """Resolve string id for lifecycle_records (original NPC id when mapped)."""
    return original_string_id_for_npc(integration, npc_id) or str(npc_id)


async def async_load_lifecycle_manager(persistence: object) -> NPCLifecycleManager | None:
    """Load NPCLifecycleManager from persistence when the API exists."""
    if not hasattr(persistence, "get_npc_lifecycle_manager"):
        return None
    persistence_lm = cast(PersistenceWithNpcLifecycleManager, persistence)
    raw = await asyncio.to_thread(persistence_lm.get_npc_lifecycle_manager)
    return cast(NPCLifecycleManager | None, raw) if raw is not None else None


def available_lifecycle_npc_ids(lifecycle_manager: NPCLifecycleManager | None) -> list[str]:
    """Keys present in lifecycle_records for debug logging."""
    if lifecycle_manager is None:
        return []
    return list(lifecycle_manager.lifecycle_records.keys())


def xp_int_from_base_stats_mapping(base_stats: object) -> int | None:
    """Return xp_value from get_base_stats() result, or None if missing/invalid."""
    if not isinstance(base_stats, dict):
        return None
    stats = cast(dict[str, object], base_stats)
    if "xp_value" not in stats:
        return None
    xp_reward_obj: object = stats["xp_value"]
    if not isinstance(xp_reward_obj, int):
        raise TypeError(f"XP reward must be int, got {type(xp_reward_obj).__name__}")
    return xp_reward_obj


def log_missing_lifecycle_npc(lookup_id: str, lifecycle_manager: NPCLifecycleManager | None) -> None:
    """Debug when a lookup id is missing from lifecycle records."""
    available_ids = available_lifecycle_npc_ids(lifecycle_manager)
    logger.debug(
        "NPC not found in lifecycle records",
        lookup_id=lookup_id,
        has_lifecycle_manager=bool(lifecycle_manager),
        available_ids=available_ids,
        total_records=len(available_ids),
    )
