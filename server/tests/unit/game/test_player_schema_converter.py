"""PlayerSchemaConverter builds PlayerRead from a Player row (status effects are player_effects rows, ADR-029 3b)."""

import uuid
from datetime import UTC, datetime
from unittest.mock import MagicMock

import pytest

from server.game.player_schema_converter import PlayerSchemaConverter
from server.models.game import PositionState
from server.models.player import Player


def _player(stats: dict[str, object]) -> Player:
    now = datetime.now(UTC)
    player = Player(
        player_id=str(uuid.uuid4()),
        user_id=str(uuid.uuid4()),
        name="Tester",
        current_room_id="room_001",
        experience_points=0,
        level=1,
        is_admin=0,
        created_at=now,
        last_active=now,
    )
    player.set_stats(stats)
    player.set_inventory([])
    return player


@pytest.mark.asyncio
async def test_position_and_derived_stats_come_from_the_player_row() -> None:
    converter = PlayerSchemaConverter(MagicMock())
    player = _player({"position": "sitting", "constitution": 60, "size": 40, "power": 50, "education": 70})

    result = await converter.create_player_read_from_object(
        player, in_combat=False, profession_data=(0, None, None, None)
    )

    assert result.position == PositionState.SITTING
    assert result.stats.max_dp == 20  # (CON + SIZ) // 5, added before position is read
    assert "status_effects" not in result.model_dump()
