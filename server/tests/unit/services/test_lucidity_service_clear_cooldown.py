"""LucidityService.clear_cooldown deletes a player's cooldown rows through the repository (used by the debrief)."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import cast

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.services.lucidity_service import LucidityService


@dataclass
class FakeRepo:
    deleted: list[tuple[uuid.UUID, str]] = field(default_factory=lambda: cast(list[tuple[uuid.UUID, str]], []))

    async def delete_cooldowns_by_action_code_pattern(self, player_id: uuid.UUID, pattern: str) -> int:
        self.deleted.append((player_id, pattern))
        return 2


@pytest.mark.asyncio
async def test_clear_cooldown_delegates_to_the_repository_and_returns_the_count(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    service = LucidityService(cast(AsyncSession, object()))
    repo = FakeRepo()
    monkeypatch.setattr(service, "_repo", repo)
    player_id = uuid.uuid4()

    cleared = await service.clear_cooldown(player_id, "debrief_pending")

    assert cleared == 2
    assert repo.deleted == [(player_id, "debrief_pending")]
