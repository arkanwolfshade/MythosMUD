"""
Unit tests for PartyService.

Covers: create_party, disband_party, add_member, remove_member (leave), kick_member,
request_party_invite, accept_party_invite, decline_party_invite, get_party_for_player,
is_leader, get_party_members, on_player_disconnect.
"""

import uuid

import pytest

from server.game.party_service import Party, PartyService

# pylint: disable=protected-access  # Reason: Test file - accessing protected members for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names


@pytest.fixture
def party_service():
    """PartyService with no dependencies (in-memory only)."""
    return PartyService()


# ---- create_party ----
def test_create_party_success(party_service):
    """Leader can create a new party."""
    leader_id = str(uuid.uuid4())
    result = party_service.create_party(leader_id)
    assert result["success"] is True
    assert "formed" in result["result"].lower()
    assert "party_id" in result
    party = party_service.get_party_for_player(leader_id)
    assert party is not None
    assert party.leader_id == leader_id
    assert leader_id in party.member_ids
    assert party_service.is_leader(leader_id) is True


def test_create_party_already_in_party_rejected(party_service):
    """Creating a second party when already in one fails."""
    leader_id = str(uuid.uuid4())
    party_service.create_party(leader_id)
    result = party_service.create_party(leader_id)
    assert result["success"] is False
    assert "already in a party" in result["result"].lower()


# ---- add_member ----
def test_add_member_success(party_service):
    """Leader can add a member (invite flow simulated)."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_id = create["party_id"]
    result = party_service.add_member(party_id, member_id)
    assert result["success"] is True
    party = party_service.get_party(party_id)
    assert party is not None
    assert member_id in party.member_ids
    assert party_service.get_party_for_player(member_id) is not None


def test_add_member_already_in_party_rejected(party_service):
    """Adding a player who is already in a party fails."""
    leader_id = str(uuid.uuid4())
    other_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_service.add_member(create["party_id"], other_id)
    result = party_service.add_member(create["party_id"], other_id)
    assert result["success"] is False
    assert "already in a party" in result["result"].lower()


def test_add_member_no_such_party(party_service):
    """Adding to a non-existent party fails."""
    result = party_service.add_member("no-such-party-id", str(uuid.uuid4()))
    assert result["success"] is False
    assert "no such party" in result["result"].lower()


# ---- request_party_invite / accept_party_invite / decline_party_invite ----
@pytest.mark.asyncio
async def test_request_party_invite_creates_pending(party_service):
    """Requesting a party invite creates a pending invite (target must accept)."""
    leader_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_id = create["party_id"]
    result = await party_service.request_party_invite(leader_id, "Leader", party_id, target_id)
    assert result["success"] is True
    assert "waiting" in result["result"].lower() or "sent" in result["result"].lower()
    assert "invite_id" in result
    assert len(party_service._pending_invites) == 1
    invite_id = list(party_service._pending_invites)[0]
    data = party_service._pending_invites[invite_id]
    assert data["inviter_id"] == leader_id
    assert data["target_id"] == target_id
    assert data["party_id"] == party_id


@pytest.mark.asyncio
async def test_accept_party_invite_success(party_service):
    """Accepting a party invite adds the player to the party."""
    leader_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_id = create["party_id"]
    await party_service.request_party_invite(leader_id, "Leader", party_id, target_id)
    invite_id = list(party_service._pending_invites)[0]
    result = await party_service.accept_party_invite(target_id, invite_id)
    assert result["success"] is True
    assert party_service.get_party_for_player(target_id) is not None
    assert target_id in party_service.get_party(party_id).member_ids
    assert invite_id not in party_service._pending_invites


@pytest.mark.asyncio
async def test_decline_party_invite_success(party_service):
    """Declining removes pending invite and does not add to party."""
    leader_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_id = create["party_id"]
    await party_service.request_party_invite(leader_id, "Leader", party_id, target_id)
    invite_id = list(party_service._pending_invites)[0]
    result = await party_service.decline_party_invite(target_id, invite_id)
    assert result["success"] is True
    assert party_service.get_party_for_player(target_id) is None
    assert invite_id not in party_service._pending_invites


@pytest.mark.asyncio
async def test_request_party_invite_target_already_in_party_rejected(party_service):
    """Request fails if target is already in a party."""
    leader_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    other_leader = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_id = create["party_id"]
    other_create = party_service.create_party(other_leader)
    party_service.add_member(other_create["party_id"], target_id)
    result = await party_service.request_party_invite(leader_id, "Leader", party_id, target_id)
    assert result["success"] is False
    assert "already in a party" in result["result"].lower()


# ---- remove_member (leave) ----
def test_remove_member_leave_success(party_service):
    """Member can leave; party remains."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_service.add_member(create["party_id"], member_id)
    result = party_service.remove_member(create["party_id"], member_id)
    assert result["success"] is True
    assert "left" in result["result"].lower()
    assert party_service.get_party_for_player(member_id) is None
    assert party_service.get_party_for_player(leader_id) is not None


def test_remove_member_leader_leaves_disbands(party_service):
    """When leader leaves, party is disbanded."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_id = create["party_id"]
    party_service.add_member(party_id, member_id)
    result = party_service.remove_member(party_id, leader_id)
    assert result["success"] is True
    assert "disbanded" in result["result"].lower()
    assert party_service.get_party_for_player(leader_id) is None
    assert party_service.get_party_for_player(member_id) is None
    assert party_service.get_party(party_id) is None


# ---- kick_member ----
def test_kick_member_leader_success(party_service):
    """Leader can kick a member."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_service.add_member(create["party_id"], member_id)
    result = party_service.kick_member(create["party_id"], member_id, leader_id)
    assert result["success"] is True
    assert party_service.get_party_for_player(member_id) is None
    assert party_service.get_party_for_player(leader_id) is not None


def test_kick_member_non_leader_rejected(party_service):
    """Non-leader cannot kick."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_service.add_member(create["party_id"], member_id)
    result = party_service.kick_member(create["party_id"], leader_id, member_id)
    assert result["success"] is False
    assert "only the party leader" in result["result"].lower()


def test_kick_self_rejected(party_service):
    """Leader cannot kick themselves."""
    leader_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    result = party_service.kick_member(create["party_id"], leader_id, leader_id)
    assert result["success"] is False
    assert "cannot kick yourself" in result["result"].lower()


# ---- disband_party ----
def test_disband_party_by_leader_success(party_service):
    """Leader can disband the party."""
    leader_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_id = create["party_id"]
    party_service.add_member(party_id, str(uuid.uuid4()))
    result = party_service.disband_party(party_id=None, by_player_id=leader_id)
    assert result["success"] is True
    assert "disbanded" in result["result"].lower()
    assert party_service.get_party(party_id) is None
    assert party_service.get_party_for_player(leader_id) is None


def test_disband_party_by_non_leader_rejected(party_service):
    """Non-leader cannot disband."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_service.add_member(create["party_id"], member_id)
    result = party_service.disband_party(party_id=create["party_id"], by_player_id=member_id)
    assert result["success"] is False
    assert "only the party leader" in result["result"].lower()


def test_disband_party_by_id_without_caller(party_service):
    """Disband by party_id without by_player_id (e.g. internal cleanup) succeeds."""
    leader_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_id = create["party_id"]
    result = party_service.disband_party(party_id=party_id, by_player_id=None)
    assert result["success"] is True
    assert party_service.get_party(party_id) is None


# ---- get_party_for_player, is_leader, get_party_members ----
def test_get_party_for_player_not_in_party(party_service):
    """Returns None when player is not in a party."""
    assert party_service.get_party_for_player(str(uuid.uuid4())) is None


def test_get_party_members_empty_when_not_in_party(party_service):
    """get_party_members returns empty list when not in party."""
    assert party_service.get_party_members(str(uuid.uuid4())) == []


def test_get_party_members_includes_self(party_service):
    """get_party_members returns all members including caller."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    party_service.create_party(leader_id)
    party = party_service.get_party_for_player(leader_id)
    assert party is not None
    party_service.add_member(party.party_id, member_id)
    members = party_service.get_party_members(leader_id)
    assert leader_id in members
    assert member_id in members
    assert len(members) == 2


def test_is_leader_false_when_not_in_party(party_service):
    """is_leader is False when not in a party."""
    assert party_service.is_leader(str(uuid.uuid4())) is False


def test_is_leader_false_when_member(party_service):
    """is_leader is False for non-leader member."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_service.add_member(create["party_id"], member_id)
    assert party_service.is_leader(leader_id) is True
    assert party_service.is_leader(member_id) is False


# ---- on_player_disconnect ----
def test_on_player_disconnect_member_removed(party_service):
    """Disconnect removes member from party; party remains."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_service.add_member(create["party_id"], member_id)
    party_service.on_player_disconnect(member_id)
    assert party_service.get_party_for_player(member_id) is None
    assert party_service.get_party_for_player(leader_id) is not None
    party = party_service.get_party(create["party_id"])
    assert party is not None
    assert member_id not in party.member_ids


def test_on_player_disconnect_leader_disbands_party(party_service):
    """Disconnect of leader disbands the party."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    create = party_service.create_party(leader_id)
    party_id = create["party_id"]
    party_service.add_member(party_id, member_id)
    party_service.on_player_disconnect(leader_id)
    assert party_service.get_party_for_player(leader_id) is None
    assert party_service.get_party_for_player(member_id) is None
    assert party_service.get_party(party_id) is None


def test_on_player_disconnect_not_in_party_no_op(party_service):
    """Disconnect of player not in a party is a no-op."""
    party_service.on_player_disconnect(str(uuid.uuid4()))
    assert len(party_service._parties) == 0
    assert len(party_service._player_to_party) == 0


# ---- Party model ----
def test_party_post_init_includes_leader_in_members():
    """Party __post_init__ ensures leader is in member_ids."""
    party = Party(party_id="p1", leader_id="lead", member_ids=set())
    assert "lead" in party.member_ids


def test_party_post_init_preserves_other_members():
    """Party __post_init__ keeps existing members and adds leader."""
    party = Party(party_id="p1", leader_id="lead", member_ids={"other"})
    assert "lead" in party.member_ids
    assert "other" in party.member_ids


# ---- is_in_same_party (combat/validator hook) ----
def test_is_in_same_party_true_when_both_in_party(party_service):
    """is_in_same_party returns True when both players are in the same party."""
    leader_id = str(uuid.uuid4())
    member_id = str(uuid.uuid4())
    party_service.create_party(leader_id)
    party = party_service.get_party_for_player(leader_id)
    assert party is not None
    party_service.add_member(party.party_id, member_id)
    assert party_service.is_in_same_party(leader_id, member_id) is True
    assert party_service.is_in_same_party(member_id, leader_id) is True


def test_is_in_same_party_false_when_different_parties(party_service):
    """is_in_same_party returns False when players are in different parties."""
    a_id = str(uuid.uuid4())
    b_id = str(uuid.uuid4())
    party_service.create_party(a_id)
    party_service.create_party(b_id)
    assert party_service.is_in_same_party(a_id, b_id) is False


def test_is_in_same_party_false_when_one_not_in_party(party_service):
    """is_in_same_party returns False when one player is not in a party."""
    leader_id = str(uuid.uuid4())
    party_service.create_party(leader_id)
    other_id = str(uuid.uuid4())
    assert party_service.is_in_same_party(leader_id, other_id) is False
    assert party_service.is_in_same_party(other_id, leader_id) is False
