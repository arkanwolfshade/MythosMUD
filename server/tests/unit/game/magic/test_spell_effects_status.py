"""Unit tests for spell status effects stored as player_effects rows (ADR-029 step 3b-i)."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from unittest.mock import MagicMock

import pytest

from server.async_persistence_types import PlayerEffectOptions
from server.game.magic import spell_effects_status as status
from server.models.game import StatusEffectType
from server.models.spell import Spell
from server.schemas.shared import TargetMatch, TargetType


@dataclass
class FakePersistence:
    """The effect surface the status-effect spells use, recording each write."""

    added: list[tuple[uuid.UUID, str, str, int | None, PlayerEffectOptions | None]] = field(default_factory=list)
    removed: list[tuple[uuid.UUID, str]] = field(default_factory=list)

    async def get_player_by_id(self, player_id: uuid.UUID) -> object | None:
        return player_id

    async def add_player_effect(
        self,
        player_id: uuid.UUID,
        effect_type: str,
        category: str,
        remaining_seconds: int | None,
        options: PlayerEffectOptions | None = None,
    ) -> str:
        self.added.append((player_id, effect_type, category, remaining_seconds, options))
        return "effect-id"

    async def remove_player_effects_by_type(self, player_id: uuid.UUID, effect_type: str) -> int:
        self.removed.append((player_id, effect_type))
        return 1


@dataclass
class FakePlayerService:
    persistence: FakePersistence = field(default_factory=FakePersistence)


@dataclass
class FakeEngine:
    player_service: FakePlayerService = field(default_factory=FakePlayerService)


def _spell() -> Spell:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "blinding_flash"
    return spell


def _target() -> TargetMatch:
    return TargetMatch(
        target_id=str(uuid.uuid4()), target_name="Hero", target_type=TargetType.PLAYER, room_id="room_001"
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(("duration", "remaining"), [(30, 30), (0, None)])
async def test_a_status_effect_is_stored_for_its_duration_in_game_seconds(duration: int, remaining: int | None) -> None:
    engine, target = FakeEngine(), _target()

    result = await status._apply_status_effect_to_player(  # pyright: ignore[reportPrivateUsage]  # Reason: TEST_MOCK - the storage step is tested directly, as test_spell_effects.py does its _process_* helpers
        engine, uuid.UUID(target.target_id), StatusEffectType.BLINDED, duration, 2, _spell(), target
    )

    assert result["effect_applied"] is True
    assert engine.player_service.persistence.added == [
        # 0 means until removed
        (uuid.UUID(target.target_id), "blinded", "spell", remaining, {"intensity": 2, "source": "spell:blinding_flash"})
    ]


@pytest.mark.asyncio
async def test_removing_a_status_effect_deletes_its_rows() -> None:
    engine, target = FakeEngine(), _target()

    result = await status._remove_player_status_effect(  # pyright: ignore[reportPrivateUsage]  # Reason: TEST_MOCK - the storage step is tested directly, as test_spell_effects.py does its _process_* helpers
        engine, uuid.UUID(target.target_id), target, StatusEffectType.BLINDED
    )

    assert result["status_effect_removed"] == "blinded"
    assert engine.player_service.persistence.removed == [(uuid.UUID(target.target_id), "blinded")]
    assert engine.player_service.persistence.added == []
