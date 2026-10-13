"""
NPC disposition on the per-hit combat events (#1025).

The client words "You attack X", "Dealt N damage to X" and "X attacks you" itself, so the server tells it each NPC's
disposition (``npc_disposition`` / ``attacker_disposition``) and the client styles the name. A player carries no tag.
"""

# pyright: reportAny=false, reportPrivateUsage=false
# These tests drive the handler and publisher through MagicMock/AsyncMock doubles for NATS, the NPC lifecycle and the
# combat service; attribute access on those doubles (await_args, args, ...) is Any by construction, and the events
# under test are plain dataclasses asserted by field.

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.constants.npc_disposition import NpcDisposition
from server.events.combat_events import NPCAttackedEvent, NPCDiedEvent, NPCTookDamageEvent, PlayerAttackedEvent
from server.models.combat import CombatParticipant, CombatParticipantType
from server.services import combat_service_events
from server.services.combat_death_handler import CombatDeathHandler
from server.services.combat_event_handler import CombatEventHandler
from server.services.combat_event_publisher import CombatEventPublisher


def _participant(name: str, ptype: CombatParticipantType) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        name=name,
        participant_type=ptype,
        current_dp=50,
        max_dp=100,
        dexterity=50,
    )


def _event[T](mock: AsyncMock, kind: type[T]) -> T:
    """The first positional argument of the mock's last await, narrowed to the event type under test."""
    args = mock.await_args
    assert args is not None
    event = args.args[0]
    assert isinstance(event, kind)
    return event


class _Wired:
    """A handler whose NPC participants resolve to one live NPC instance, plus the publisher mocks it calls."""

    npc_attacked: AsyncMock
    npc_took_damage: AsyncMock
    player_attacked: AsyncMock
    handler: CombatEventHandler

    def __init__(self, npc_type: object) -> None:
        npc_instance = MagicMock(npc_type=npc_type)
        npc_instance.name = "Rat"
        integration = MagicMock(
            _uuid_mapping=MagicMock(get_original_string_id=MagicMock(return_value="npc-string-1")),
            _data_provider=MagicMock(get_npc_instance=MagicMock(return_value=npc_instance)),
        )
        self.npc_attacked = AsyncMock()
        self.npc_took_damage = AsyncMock()
        self.player_attacked = AsyncMock()
        publisher = MagicMock(
            publish_npc_attacked=self.npc_attacked,
            publish_npc_took_damage=self.npc_took_damage,
            publish_player_attacked=self.player_attacked,
        )
        self.handler = CombatEventHandler(
            MagicMock(_npc_combat_integration_service=integration, _combat_event_publisher=publisher)
        )


COMBAT = MagicMock(room_id="room-a", combat_id=uuid.uuid4())


def test_resolve_npc_disposition_reads_the_live_instance() -> None:
    wired = _Wired("aggressive_mob")
    assert wired.handler._resolve_npc_disposition(_participant("Rat", CombatParticipantType.NPC)) == "aggressive_mob"


def test_resolve_npc_disposition_is_none_for_players_and_phantoms() -> None:
    handler = _Wired("aggressive_mob").handler
    assert handler._resolve_npc_disposition(_participant("Alice", CombatParticipantType.PLAYER)) is None
    assert handler._resolve_npc_disposition(_participant("Horror", CombatParticipantType.PHANTOM)) is None


def test_resolve_npc_disposition_defaults_to_passive_when_the_type_is_unusable() -> None:
    npc = _participant("Rat", CombatParticipantType.NPC)
    assert _Wired("friendly").handler._resolve_npc_disposition(npc) == "passive_mob"
    no_integration = CombatEventHandler(MagicMock(_npc_combat_integration_service=None))
    assert no_integration._resolve_npc_disposition(npc) == "passive_mob"


@pytest.mark.asyncio
async def test_player_attacking_an_npc_tags_the_npc_on_both_events() -> None:
    wired = _Wired("shopkeeper")
    await wired.handler._publish_attack_events(
        _participant("Hero", CombatParticipantType.PLAYER), _participant("Rat", CombatParticipantType.NPC), 5, COMBAT
    )
    assert _event(wired.npc_attacked, NPCAttackedEvent).npc_disposition == "shopkeeper"
    assert _event(wired.npc_took_damage, NPCTookDamageEvent).npc_disposition == "shopkeeper"


@pytest.mark.asyncio
async def test_npc_attacking_a_player_tags_the_attacker_and_a_player_attacker_carries_none() -> None:
    wired = _Wired("aggressive_mob")
    victim = _participant("Victim", CombatParticipantType.PLAYER)

    await wired.handler._publish_attack_events(_participant("Rat", CombatParticipantType.NPC), victim, 5, COMBAT)
    assert _event(wired.player_attacked, PlayerAttackedEvent).attacker_disposition == "aggressive_mob"

    await wired.handler._publish_attack_events(_participant("Bully", CombatParticipantType.PLAYER), victim, 5, COMBAT)
    assert _event(wired.player_attacked, PlayerAttackedEvent).attacker_disposition is None


class _Published:
    """A CombatEventPublisher over mocked NATS; ``sent()`` is the event_data of the last publish."""

    publish: AsyncMock
    publisher: CombatEventPublisher

    def __init__(self) -> None:
        self.publish = AsyncMock(return_value=True)
        nats = MagicMock(is_connected=MagicMock(return_value=True), publish=self.publish)
        subjects = MagicMock(build_subject=MagicMock(return_value="combat.started.room.room_001"))
        self.publisher = CombatEventPublisher(nats, subjects)

    def sent(self) -> dict[str, object]:
        args = self.publish.await_args
        assert args is not None
        event_data = args.args[1]["event_data"]
        assert isinstance(event_data, dict)
        return cast("dict[str, object]", event_data)


@pytest.mark.asyncio
async def test_publishers_put_the_npc_disposition_on_the_wire_only_when_known() -> None:
    """Absent means the client keeps the line plain."""
    out = _Published()
    cid, aid = uuid.uuid4(), uuid.uuid4()

    _ = await out.publisher.publish_npc_attacked(
        NPCAttackedEvent(
            combat_id=cid,
            room_id="r",
            attacker_id=aid,
            attacker_name="A",
            npc_id=uuid.uuid4(),
            npc_name="N",
            damage=1,
            action_type="attack",
            target_current_dp=1,
            target_max_dp=2,
            npc_disposition="shopkeeper",
        )
    )
    assert out.sent()["npc_disposition"] == "shopkeeper"

    _ = await out.publisher.publish_npc_took_damage(
        NPCTookDamageEvent(
            combat_id=cid,
            room_id="r",
            npc_id="n",
            npc_name="N",
            damage=1,
            current_dp=1,
            max_dp=2,
            npc_disposition="quest_giver",
        )
    )
    assert out.sent()["npc_disposition"] == "quest_giver"

    _ = await out.publisher.publish_npc_died(
        NPCDiedEvent(combat_id=cid, room_id="r", npc_id="n", npc_name="N", xp_reward=1, npc_disposition="passive_mob")
    )
    assert out.sent()["npc_disposition"] == "passive_mob"

    _ = await out.publisher.publish_player_attacked(
        PlayerAttackedEvent(
            combat_id=cid,
            room_id="r",
            attacker_id=aid,
            attacker_name="Rat",
            target_id=uuid.uuid4(),
            target_name="V",
            damage=1,
            action_type="attack",
            target_current_dp=1,
            target_max_dp=2,
            attacker_disposition="aggressive_mob",
        )
    )
    assert out.sent()["attacker_disposition"] == "aggressive_mob"

    # Nothing known (a player attacker, or a non-combat damage source): the key is simply absent.
    _ = await out.publisher.publish_npc_took_damage(
        NPCTookDamageEvent(combat_id=cid, room_id="r", npc_id="n", npc_name="N", damage=1, current_dp=1, max_dp=2)
    )
    assert "npc_disposition" not in out.sent()


@pytest.mark.asyncio
async def test_combat_death_event_carries_the_npcs_disposition() -> None:
    """The slain line colours the name from this; it is read while the instance still exists."""
    publish = AsyncMock(return_value=True)
    handler = CombatDeathHandler(MagicMock(publish_npc_died_event_to_nats=publish))
    combat = MagicMock(room_id="room-001", combat_id=uuid.uuid4())
    npc = _participant("Goblin", CombatParticipantType.NPC)
    with patch(
        "server.services.combat_death_handler.get_npc_disposition_from_instance",
        return_value=NpcDisposition.AGGRESSIVE_MOB,
    ):
        await handler._publish_npc_death_event(npc, combat, 50, "killer-1", "npc-string-1")
    assert _event(publish, NPCDiedEvent).npc_disposition == "aggressive_mob"


@pytest.mark.asyncio
async def test_non_combat_death_event_carries_the_npcs_disposition() -> None:
    """Steal-life and other non-combat kills publish the same tagged event."""
    publish = AsyncMock(return_value=True)
    service = MagicMock(publish_npc_died_event_to_nats=publish)
    with patch(
        "server.services.combat_service_events.get_npc_disposition_from_instance",
        return_value=NpcDisposition.QUEST_GIVER,
    ):
        assert await combat_service_events.publish_npc_died_event(service, "room_001", "npc-1", "Elder") is True
    assert _event(publish, NPCDiedEvent).npc_disposition == "quest_giver"
