"""The attack command's "You attack X!" acknowledgement styles the foe's name (#1039)."""

# pyright: reportAny=false, reportPrivateUsage=false
# The handler, combat services and player are MagicMock/AsyncMock doubles, and the helpers under test are private by
# design; attribute access on those doubles is Any by construction.

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import combat_attack
from server.constants.message_segments import MessageSegment
from server.constants.npc_disposition import NpcDisposition
from server.models.combat import CombatResult


def _segments(result: object) -> list[MessageSegment]:
    assert isinstance(result, dict)
    return cast("list[MessageSegment]", result["segments"])


def test_acknowledgement_segments_join_to_the_result_for_every_disposition() -> None:
    for disposition in NpcDisposition:
        out = combat_attack._attack_acknowledgement("punch", "Ghoul", disposition)
        assert out["result"] == "You punch Ghoul!"
        assert "".join(segment["text"] for segment in _segments(out)) == out["result"]
        assert [s for s in _segments(out) if "category" in s] == [
            {"text": "Ghoul", "category": f"npc.{disposition.value}"}
        ]


@pytest.mark.asyncio
async def test_attacking_a_real_npc_styles_it_by_its_live_disposition() -> None:
    handler = MagicMock()
    handler.npc_combat_service.handle_player_attack_on_npc = AsyncMock(return_value=True)
    player = MagicMock(player_id=uuid.uuid4())
    with (
        patch.object(
            combat_attack, "_get_combat_action_context", AsyncMock(return_value=(player, MagicMock(), "Elder", None))
        ),
        patch.object(combat_attack, "_resolve_combat_damage", return_value=3),
        patch.object(combat_attack, "get_npc_disposition_from_instance", return_value=NpcDisposition.QUEST_GIVER),
    ):
        out = await combat_attack._execute_combat_action(handler, "hero", "npc-1", "attack", "r1")
    assert out["result"] == "You attack Elder!"
    assert _segments(out)[1] == {"text": "Elder", "category": "npc.quest_giver"}


@pytest.mark.asyncio
async def test_a_refused_attack_stays_plain_text() -> None:
    """In-world refusals are not styled; only the acknowledgement of an attack that began is."""
    handler = MagicMock()
    handler.npc_combat_service.handle_player_attack_on_npc = AsyncMock(return_value=False)
    player = MagicMock(player_id=uuid.uuid4())
    with (
        patch.object(
            combat_attack, "_get_combat_action_context", AsyncMock(return_value=(player, MagicMock(), "Elder", None))
        ),
        patch.object(combat_attack, "_resolve_combat_damage", return_value=3),
    ):
        out = await combat_attack._execute_combat_action(handler, "hero", "npc-1", "attack", "r1")
    assert out == {"result": "You cannot attack Elder right now."}


@pytest.mark.asyncio
async def test_a_phantom_is_acknowledged_exactly_like_a_real_hostile() -> None:
    """ADR-024: nothing in the line tells a hallucinated hostile from a real one."""
    player = MagicMock(player_id=uuid.uuid4())
    player.get_combat_stats = MagicMock(return_value={"current_dp": 10, "max_dp": 20, "dexterity": 10})
    handler = MagicMock()
    handler.persistence.get_player_by_name = AsyncMock(return_value=player)
    handler.persistence.get_player_by_id = AsyncMock(return_value=player)
    handler.combat_service.start_combat = AsyncMock()
    handler.combat_service.process_attack = AsyncMock(
        return_value=CombatResult(success=True, damage=1, target_died=False, combat_ended=False, message="hit")
    )
    phantom = {
        "phantom_id": "ph-1",
        "name": "Shambling Horror",
        "current_dp": 1,
        "max_dp": 1,
        "is_non_damaging": False,
    }
    with (
        patch("server.services.phantom_hostile_service.phantom_hostile_service.get_phantom_data", return_value=phantom),
        patch.object(combat_attack, "_resolve_combat_damage", return_value=5),
    ):
        out = await combat_attack._execute_phantom_combat_action(handler, "hero", "ph-1", "attack", "r1")
    assert out["result"] == "You attack Shambling Horror!"
    assert _segments(out)[1] == {"text": "Shambling Horror", "category": "npc.aggressive_mob"}
