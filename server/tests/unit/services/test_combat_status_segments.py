"""
Combat status lines carry the NPC's name as a styled segment (#1036): target switch, join, taunt.

The NPC's disposition is looked up from its live instance; where it is unknown the line stays plain.
"""

# pyright: reportAny=false, reportPrivateUsage=false
# The broadcasters are driven through MagicMock/AsyncMock doubles for the connection manager and the integration;
# attribute access on those doubles is Any by construction.

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.constants.message_segments import MessageSegment, SegmentPart
from server.constants.npc_disposition import DEFAULT_NPC_DISPOSITION, NpcDisposition
from server.game.skill_service import SuccessLevel
from server.services import combat_service_events
from server.services.combat_messaging.combat_broadcasts import CombatBroadcastMixin
from server.services.combat_taunt_action import taunt_outcome_line, taunt_outcome_parts
from server.services.npc_combat_integration_service import NPCCombatIntegrationService

GHOUL: MessageSegment = {"text": "Ghoul", "category": "npc.aggressive_mob"}


class _Broadcaster(CombatBroadcastMixin):
    """The mixin over a mocked connection manager; ``sent()`` is the data of the last room event."""

    broadcast: AsyncMock
    connection_manager: MagicMock

    def __init__(self) -> None:
        self.broadcast = AsyncMock(return_value={"successful_deliveries": 1})
        self.connection_manager = MagicMock(broadcast_to_room=self.broadcast)

    def sent(self) -> dict[str, object]:
        args = self.broadcast.await_args
        assert args is not None
        data = args.args[1]["data"]
        assert isinstance(data, dict)
        return cast("dict[str, object]", data)


@pytest.mark.asyncio
async def test_target_switch_styles_the_npc_when_its_disposition_is_known() -> None:
    out = _Broadcaster()
    _ = await out.broadcast_combat_target_switch(
        "r1", "c1", "Ghoul", "Ashcroft", npc_disposition=NpcDisposition.AGGRESSIVE_MOB
    )
    data = out.sent()
    assert data["message"] == "Ghoul turns its gaze to Ashcroft."
    assert data["segments"] == [GHOUL, {"text": " turns its gaze to Ashcroft."}]


@pytest.mark.asyncio
async def test_target_switch_without_a_disposition_stays_plain() -> None:
    out = _Broadcaster()
    _ = await out.broadcast_combat_target_switch("r1", "c1", "Ghoul", "Ashcroft")
    assert out.sent()["message"] == "Ghoul turns its gaze to Ashcroft."
    assert "segments" not in out.sent()


@pytest.mark.asyncio
async def test_disengage_styles_the_npc_and_appends_its_clause() -> None:
    out = _Broadcaster()
    _ = await out.broadcast_npc_disengage(
        "r1", "c1", "Ghoul", "melts into the dark.", npc_disposition=NpcDisposition.AGGRESSIVE_MOB
    )
    data = out.sent()
    assert data["message"] == "Ghoul melts into the dark."
    assert data["segments"] == [GHOUL, {"text": " melts into the dark."}]


@pytest.mark.asyncio
async def test_disengage_without_a_disposition_stays_plain() -> None:
    out = _Broadcaster()
    _ = await out.broadcast_npc_disengage("r1", "c1", "Ghoul", "withdraws.")
    assert out.sent()["message"] == "Ghoul withdraws."
    assert "segments" not in out.sent()


@pytest.mark.asyncio
async def test_join_styles_the_foe_not_the_joiner() -> None:
    out = _Broadcaster()
    _ = await out.broadcast_player_joined_combat(
        "r1", "c1", "Blackwood", "Ghoul", "p1", npc_disposition=NpcDisposition.AGGRESSIVE_MOB
    )
    data = out.sent()
    assert data["message"] == "Blackwood joins the fight against Ghoul!"
    assert data["segments"] == [{"text": "Blackwood joins the fight against "}, GHOUL, {"text": "!"}]


@pytest.mark.asyncio
async def test_taunt_accepts_a_plain_line_or_parts() -> None:
    out = _Broadcaster()
    _ = await out.broadcast_taunt_result("r1", "c1", "Tank bellows a challenge at Ghoul!")
    assert out.sent()["message"] == "Tank bellows a challenge at Ghoul!"
    assert "segments" not in out.sent()

    parts: list[SegmentPart] = ["Tank bellows a challenge at ", GHOUL, "!"]
    _ = await out.broadcast_taunt_result("r1", "c1", parts)
    assert out.sent()["segments"] == [{"text": "Tank bellows a challenge at "}, GHOUL, {"text": "!"}]


@pytest.mark.parametrize("level", [SuccessLevel.FUMBLE, SuccessLevel.REGULAR, SuccessLevel.FAILURE])
def test_taunt_parts_join_to_the_plain_line(level: SuccessLevel) -> None:
    """The flat helper is just the parts joined, so the wording never forks."""
    parts = taunt_outcome_parts(level, "Tank", GHOUL)
    assert "".join(p if isinstance(p, str) else p["text"] for p in parts) == taunt_outcome_line(level, "Tank", "Ghoul")


@pytest.mark.asyncio
async def test_aggro_switches_look_up_each_npcs_disposition() -> None:
    npc_id = uuid.uuid4()
    switch = AsyncMock()
    messaging = MagicMock(broadcast_combat_target_switch=switch)
    integration = MagicMock(
        get_messaging_integration=MagicMock(return_value=messaging),
        get_npc_disposition=MagicMock(return_value=NpcDisposition.SHOPKEEPER),
    )
    service = MagicMock(
        get_npc_combat_integration_service=MagicMock(return_value=integration),
        publish_combat_target_switch_event_to_nats=AsyncMock(),
    )
    await combat_service_events.broadcast_aggro_target_switches(
        service, "r1", uuid.uuid4(), [(npc_id, "Merchant", "Ashcroft")]
    )
    integration.get_npc_disposition.assert_called_once_with(npc_id)
    args = switch.await_args
    assert args is not None
    assert args.kwargs["npc_disposition"] is NpcDisposition.SHOPKEEPER


def test_integration_disposition_lookup_reads_the_mapped_live_instance() -> None:
    participant = uuid.uuid4()
    service = MagicMock(spec=NPCCombatIntegrationService)
    service.get_original_string_id = MagicMock(side_effect={participant: "npc-string-1"}.get)
    with patch(
        "server.services.npc_combat_integration_service.get_npc_disposition_from_instance",
        return_value=NpcDisposition.QUEST_GIVER,
    ) as lookup:
        found = NPCCombatIntegrationService.get_npc_disposition(service, participant)
        unmapped = NPCCombatIntegrationService.get_npc_disposition(service, uuid.uuid4())
    assert found is NpcDisposition.QUEST_GIVER
    lookup.assert_called_once_with("npc-string-1")
    assert unmapped is DEFAULT_NPC_DISPOSITION
