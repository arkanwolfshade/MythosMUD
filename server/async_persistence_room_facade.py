"""Room-cache loading and RoomCacheLoader test hooks for AsyncPersistenceLayer."""

# Stub-only attrs are provided by AsyncPersistenceLayer.__init__ at runtime.
# pyright: reportPrivateUsage=false, reportUninitializedInstanceVariable=false

from __future__ import annotations

import asyncio
from typing import cast

from sqlalchemy.ext.asyncio import AsyncSession
from structlog.stdlib import BoundLogger

from .async_persistence_room_loader import (
    ExitJsonEntry,
    ProcessedRoomData,
    RoomCacheLoader,
    RoomLoadResult,
)
from .exceptions import DatabaseError
from .models.room import Room


class _AsyncPersistenceRoomFacadeBase:  # pylint: disable=too-few-public-methods  # Reason: mixin attr holder; public API lives on AsyncPersistenceLayer
    """Attrs provided by AsyncPersistenceLayer when mixed in."""

    _logger: BoundLogger
    _room_cache: dict[str, Room]
    _room_cache_loaded: bool
    _room_cache_loading: asyncio.Lock | None
    _room_loader: RoomCacheLoader

    async def _ensure_room_cache_loaded(self) -> None:
        """Ensure room cache is loaded (lazy loading with lock)."""
        if self._room_cache_loaded:
            return

        if self._room_cache_loading is None:
            self._room_cache_loading = asyncio.Lock()

        async with self._room_cache_loading:
            cache_loaded = cast(bool, self._room_cache_loaded)
            if cache_loaded:
                return

            try:
                await self._load_room_cache_async()
                if self._room_cache:
                    self._room_cache_loaded = True
                else:
                    self._room_cache_loaded = False
            except (DatabaseError, OSError, RuntimeError) as e:
                self._logger.error(
                    "Room cache load failed",
                    error=str(e),
                    error_type=type(e).__name__,
                    operation="load_room_cache",
                )
                self._room_cache.clear()
                self._room_cache_loaded = False

    async def _load_room_cache_async(self) -> None:
        """Load rooms from PostgreSQL via RoomCacheLoader."""
        await self._room_loader.load()


class AsyncPersistenceRoomFacade(_AsyncPersistenceRoomFacadeBase):  # pylint: disable=too-few-public-methods  # Reason: test hooks are intentionally private (_process_*)
    """Mixin: lazy room-cache load and loader delegation for unit tests."""

    def _process_room_rows(self, rooms_rows: list[dict[str, object]]) -> list[ProcessedRoomData]:
        """Delegate to room loader; exposed for unit tests."""
        return self._room_loader._process_room_rows(rooms_rows)  # pylint: disable=protected-access  # Reason: test hook

    def _process_exit_rows(self, exits_rows: list[dict[str, object]]) -> dict[str, dict[str, str]]:
        """Delegate to room loader; exposed for unit tests."""
        return self._room_loader._process_exit_rows(exits_rows)  # pylint: disable=protected-access  # Reason: test hook

    def _build_room_objects(
        self,
        room_data_list: list[ProcessedRoomData],
        exits_by_room: dict[str, dict[str, str]],
        result_container: RoomLoadResult,
    ) -> None:
        """Delegate to room loader; exposed for unit tests."""
        self._room_loader._build_room_objects(  # pylint: disable=protected-access  # Reason: test hook
            room_data_list,
            exits_by_room,
            result_container,
        )

    async def _query_rooms_with_exits_async(self, session: AsyncSession) -> list[dict[str, object]]:
        """Delegate to room loader; exposed for unit tests."""
        return await self._room_loader._query_rooms_with_exits_async(session)  # pylint: disable=protected-access

    def _generate_room_id_from_zone_data(
        self, zone_stable_id: str | None, subzone_stable_id: str | None, stable_id: str | None
    ) -> str:
        """Delegate to room loader; exposed for unit tests."""
        return self._room_loader._generate_room_id_from_zone_data(  # pylint: disable=protected-access
            zone_stable_id,
            subzone_stable_id,
            stable_id,
        )

    def _parse_exits_json(self, exits_json: object) -> list[ExitJsonEntry]:
        """Delegate to room loader; exposed for unit tests."""
        return self._room_loader._parse_exits_json(exits_json)  # pylint: disable=protected-access

    def _process_exits_for_room(
        self,
        room_id: str,
        exits_list: list[ExitJsonEntry],
        exits_by_room: dict[str, dict[str, str]],
    ) -> None:
        """Delegate to room loader; exposed for unit tests."""
        self._room_loader._process_exits_for_room(  # pylint: disable=protected-access
            room_id,
            exits_list,
            exits_by_room,
        )

    def _process_combined_rows(
        self, combined_rows: list[dict[str, object]]
    ) -> tuple[list[ProcessedRoomData], dict[str, dict[str, str]]]:
        """Delegate to room loader; exposed for unit tests."""
        return self._room_loader._process_combined_rows(combined_rows)  # pylint: disable=protected-access
