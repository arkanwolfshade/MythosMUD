"""GameBundle loads the persisted mute index at startup (#681) and degrades if the DB is unavailable."""

# pyright: reportPrivateUsage=false
# pylint: disable=protected-access  # Reason: exercising GameBundle's private startup step directly

import uuid
from datetime import UTC, datetime
from typing import override

import pytest

from server.container.bundles.game import GameBundle
from server.exceptions import DatabaseError
from server.persistence.repositories.player_mute_repository import PlayerMute, PlayerMuteRepository
from server.services.user_manager import UserManager


class _Repo(PlayerMuteRepository):
    def __init__(self, active: list[PlayerMute] | None, *, fail: bool = False) -> None:
        self.active: list[PlayerMute] = active or []
        self.fail: bool = fail

    @override
    async def load_active(self) -> list[PlayerMute]:
        if self.fail:
            raise DatabaseError("db down")
        return self.active


@pytest.mark.asyncio
async def test_load_player_mutes_fills_user_manager_index() -> None:
    target = uuid.uuid4()
    mute = PlayerMute("global", uuid.uuid4(), "Admin", target, "Noisy", None, "", datetime.now(UTC), None)
    bundle = GameBundle()
    user_manager = UserManager(mute_repository=_Repo([mute]))
    bundle.user_manager = user_manager

    await bundle._load_player_mutes()

    assert user_manager.is_globally_muted(target)


@pytest.mark.asyncio
async def test_load_player_mutes_database_error_starts_with_no_mutes() -> None:
    bundle = GameBundle()
    user_manager = UserManager(mute_repository=_Repo(None, fail=True))
    bundle.user_manager = user_manager

    await bundle._load_player_mutes()  # must not raise: server still starts

    assert not user_manager.is_globally_muted(uuid.uuid4())


@pytest.mark.asyncio
async def test_load_player_mutes_without_user_manager_is_noop() -> None:
    bundle = GameBundle()
    bundle.user_manager = None

    await bundle._load_player_mutes()
