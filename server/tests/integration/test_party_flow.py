"""
Integration tests for party (ephemeral grouping) feature.

Flow: Two players; leader creates party, adds member; member leaves; leader disbands.
Verifies in-memory state and PartyUpdated events.
"""

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures use same names as params

import asyncio
import uuid

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import PartyUpdated
from server.game.party_service import PartyService


@pytest.fixture
def event_bus():
    """Real EventBus for integration."""
    return EventBus()


@pytest.fixture
def party_events(event_bus: EventBus) -> list[PartyUpdated]:
    """Collect PartyUpdated events published during test."""
    collected: list[PartyUpdated] = []

    def handler(event: PartyUpdated) -> None:
        collected.append(event)

    event_bus.subscribe(PartyUpdated, handler, service_id="test_party_flow")
    return collected


@pytest.fixture
def party_service(event_bus: EventBus) -> PartyService:
    """PartyService wired to real EventBus."""
    return PartyService(event_bus=event_bus)


@pytest.mark.asyncio
async def test_party_invite_join_leave_disband_state_and_events(
    party_service: PartyService,
    party_events: list[PartyUpdated],
) -> None:
    """
    Two players: A creates party, adds B; B leaves; A disbands.
    Verify in-memory state after each step and PartyUpdated events.
    """
    player_a_id = str(uuid.uuid4())
    player_b_id = str(uuid.uuid4())

    # A creates party (e.g. first "party invite B" creates party)
    create = party_service.create_party(player_a_id)
    assert create["success"] is True
    party_id = create["party_id"]
    assert party_service.get_party_for_player(player_a_id) is not None
    assert party_service.is_leader(player_a_id) is True
    await asyncio.sleep(0.02)
    assert len(party_events) >= 1
    assert party_events[-1].change_type == "created"
    assert party_events[-1].leader_id == player_a_id
    assert player_a_id in party_events[-1].member_ids

    # A adds B
    add_result = party_service.add_member(party_id, player_b_id)
    assert add_result["success"] is True
    party = party_service.get_party_for_player(player_a_id)
    assert party is not None
    assert player_b_id in party.member_ids
    assert party_service.get_party_for_player(player_b_id) is not None
    assert party_service.is_leader(player_b_id) is False
    await asyncio.sleep(0.02)
    assert any(e.change_type == "member_joined" for e in party_events)

    # B leaves
    leave_result = party_service.remove_member(party_id, player_b_id)
    assert leave_result["success"] is True
    assert "left" in leave_result["result"].lower()
    assert party_service.get_party_for_player(player_b_id) is None
    assert party_service.get_party_for_player(player_a_id) is not None
    await asyncio.sleep(0.02)
    assert any(e.change_type == "member_left" for e in party_events)

    # A disbands (by leader)
    disband_result = party_service.disband_party(party_id=None, by_player_id=player_a_id)
    assert disband_result["success"] is True
    assert party_service.get_party_for_player(player_a_id) is None
    assert party_service.get_party(party_id) is None
    await asyncio.sleep(0.02)
    assert any(e.change_type == "disbanded" for e in party_events)


@pytest.mark.asyncio
async def test_party_leader_leaves_disbands(
    party_service: PartyService,
    party_events: list[PartyUpdated],
) -> None:
    """When leader leaves, party is disbanded and disbanded event is emitted."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    assert create["success"] is True
    party_id = create["party_id"]
    party_service.add_member(party_id, member_id)
    await asyncio.sleep(0.02)
    initial_count = len(party_events)

    result = party_service.remove_member(party_id, leader_id)
    assert result["success"] is True
    assert "disbanded" in result["result"].lower()
    assert party_service.get_party_for_player(leader_id) is None
    assert party_service.get_party_for_player(member_id) is None
    assert party_service.get_party(party_id) is None
    await asyncio.sleep(0.02)
    assert any(e.change_type == "disbanded" for e in party_events[initial_count:])
