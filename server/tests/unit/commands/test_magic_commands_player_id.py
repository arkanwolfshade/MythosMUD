"""Magic commands hand services a UUID: the ORM Player's id is a str, and casting state and the registry key by UUID.

A Power Drain's transfer failed on it: ``mutate_many`` sorts the ids it is given, and a str does not sort with a UUID.
"""

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.magic_commands import MagicCommandHandler
from server.game.magic.magic_service import MagicService
from server.game.magic.spell_learning_service import SpellLearningService
from server.game.magic.spell_registry import SpellRegistry
from server.models.player import Player
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository

PLAYER_ID = uuid.uuid4()


def _handler(magic_service: MagicMock, learning: MagicMock | None = None) -> MagicCommandHandler:
    player = Player(player_id=str(PLAYER_ID), name="Tester")
    player.set_stats({"current_dp": 20})
    magic_service.player_service = MagicMock(
        persistence=MagicMock(
            get_player_by_name=AsyncMock(return_value=player), get_player_by_id=AsyncMock(return_value=player)
        )
    )
    return MagicCommandHandler(
        cast(MagicService, cast(object, magic_service)),
        cast(SpellRegistry, cast(object, MagicMock())),
        cast(PlayerSpellRepository, cast(object, MagicMock())),
        cast(SpellLearningService, cast(object, learning)),
    )


def _first_arg(mock: AsyncMock) -> object:
    assert mock.await_args is not None
    return cast(object, mock.await_args.args[0])


@pytest.mark.asyncio
async def test_cast_hands_on_a_uuid() -> None:
    cast_spell = AsyncMock(return_value={"success": False, "message": "No"})

    _ = await _handler(MagicMock(cast_spell=cast_spell)).handle_cast_command(
        {"spell_name": "s"}, {}, None, None, "Tester"
    )

    assert _first_arg(cast_spell) == PLAYER_ID


@pytest.mark.asyncio
async def test_stop_hands_on_a_uuid() -> None:
    interrupt_casting = AsyncMock(return_value={"success": True, "message": "Stopped"})

    _ = await _handler(MagicMock(interrupt_casting=interrupt_casting)).handle_stop_command({}, {}, None, None, "Tester")

    assert _first_arg(interrupt_casting) == PLAYER_ID


@pytest.mark.asyncio
async def test_learn_hands_on_a_uuid() -> None:
    learn_spell = AsyncMock(return_value={"success": True, "message": "Learned", "corruption_applied": 0})

    _ = await _handler(MagicMock(), MagicMock(learn_spell=learn_spell)).handle_learn_command(
        {"spell_name": "s"}, {}, None, None, "Tester"
    )

    assert _first_arg(learn_spell) == PLAYER_ID
