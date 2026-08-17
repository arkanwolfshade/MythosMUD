"""Protocol stubs and container access for game tick processing."""

# pylint: disable=missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: PEP 544 Protocol stubs

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable, Mapping
from typing import TYPE_CHECKING, Protocol, cast

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..models.combat import CombatInstance
    from ..models.player import Player
    from ..services.passive_lucidity_flux_service import PassiveLucidityFluxService

__all__ = [
    "_TickCombatService",
    "_TickConnectionManager",
    "_TickContainer",
    "_TickDeathService",
    "_TickEventBus",
    "_TickMagicService",
    "_TickMpRegen",
    "_TickNpcLifecycle",
    "_TickRespawnService",
    "_app_container",
    "_online_player_ids",
    "_tick_online_players",
]


class _TickConnectionManager(Protocol):
    online_players: dict[uuid.UUID, dict[str, object]]
    player_websockets: dict[uuid.UUID, list[str]]

    async def send_personal_message(self, player_id: uuid.UUID, event: dict[str, object]) -> dict[str, object]: ...


class _TickCombatService(Protocol):
    async def process_game_tick(self, current_tick: int) -> None: ...

    async def get_combat_by_participant(self, participant_id: uuid.UUID) -> CombatInstance | None: ...


class _TickMagicService(Protocol):
    async def check_casting_progress(self, current_tick: int) -> None: ...


class _TickDeathService(Protocol):
    async def handle_player_death(
        self,
        player_id: uuid.UUID,
        death_location: str,
        killer_info: Mapping[str, object] | None,
        session: AsyncSession,
    ) -> bool: ...

    async def process_mortally_wounded_tick(self, player_id: uuid.UUID, session: AsyncSession) -> bool: ...

    async def get_mortally_wounded_players(self, session: AsyncSession) -> list[Player]: ...

    async def get_dead_players(self, session: AsyncSession) -> list[Player]: ...


class _TickRespawnService(Protocol):
    async def move_player_to_limbo(self, player_id: uuid.UUID, death_location: str, session: AsyncSession) -> bool: ...


class _TickEventBus(Protocol):
    def publish(self, event: object) -> None: ...


class _TickMpRegen(Protocol):
    async def process_tick_regeneration(self, player_id: uuid.UUID) -> Mapping[str, object]: ...


class _TickNpcLifecycle(Protocol):
    respawn_queue: dict[str, Mapping[str, object]]

    def periodic_maintenance(self) -> dict[str, object]: ...


class _TickContainer(Protocol):
    async_persistence: AsyncPersistenceLayer | None
    connection_manager: _TickConnectionManager | None
    combat_service: _TickCombatService | None
    magic_service: _TickMagicService | None
    player_death_service: _TickDeathService | None
    player_respawn_service: _TickRespawnService | None
    event_bus: _TickEventBus | None
    passive_lucidity_flux_service: PassiveLucidityFluxService | None
    mp_regeneration_service: _TickMpRegen | None
    npc_lifecycle_manager: _TickNpcLifecycle | None


logger = get_logger("server.game_tick")


def _app_container(app: FastAPI) -> _TickContainer | None:
    """Return the DI container from app.state, or None if missing."""
    raw = getattr(app.state, "container", None)
    if raw is None:
        return None
    return cast(_TickContainer, raw)


def _online_player_ids(container: _TickContainer) -> list[uuid.UUID]:
    """Return currently online player UUIDs, or empty if no connection manager."""
    manager = container.connection_manager
    if manager is None:
        return []
    return list(manager.online_players.keys())


async def _tick_online_players(
    online_player_ids: list[uuid.UUID],
    tick_count: int,
    log_message: str,
    process_one: Callable[[str], Awaitable[bool]],
) -> None:
    """Run process_one(str(player_id)) for each online player and log successes."""
    processed_count = 0
    for player_id in online_player_ids:
        if await process_one(str(player_id)):
            processed_count += 1
    if processed_count > 0:
        logger.debug(log_message, tick_count=tick_count, players_processed=processed_count)
