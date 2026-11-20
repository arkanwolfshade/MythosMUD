"""PlayerStateService.gain_occult_knowledge calls the persistence layer's real method (the effects API's occult path).

It used to call ``async_gain_occult_knowledge``, which does not exist: every occult-knowledge request raised
AttributeError. A bare AsyncMock answers any name, so the existing tests could not see it; this stub has only the
methods the real layer has.
"""

from __future__ import annotations

import uuid
from types import SimpleNamespace

import pytest

from server.game.player_state_service import PlayerStateService


class _Persistence:
    """The two methods of AsyncPersistenceLayer this path uses, and nothing else."""

    def __init__(self, player: SimpleNamespace | None) -> None:
        self.player: SimpleNamespace | None = player
        self.gains: list[tuple[SimpleNamespace, int, str]] = []

    async def get_player_by_id(self, _player_id: uuid.UUID) -> SimpleNamespace | None:
        return self.player

    async def gain_occult_knowledge(self, player: SimpleNamespace, amount: int, source: str = "unknown") -> None:
        self.gains.append((player, amount, source))


@pytest.mark.asyncio
async def test_gain_occult_knowledge_reaches_the_persistence_layer() -> None:
    player = SimpleNamespace(player_id=str(uuid.uuid4()), name="Seeker")
    persistence = _Persistence(player)

    result = await PlayerStateService(persistence).gain_occult_knowledge(uuid.uuid4(), 3, "tome")

    assert persistence.gains == [(player, 3, "tome")]
    assert result == {"message": "Gained 3 occult knowledge for Seeker"}
