"""
Unit tests for combat_turn_participant_actions (aggro-aware NPC targeting and helpers).
"""

# pyright: reportPrivateUsage=false
# Reason: Tests call module-private NPC combat helpers (_select_npc_target, _resolve_npc_target, etc.).

# pylint: disable=protected-access  # Reason: Unit tests exercise module-private helpers intentionally

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services import combat_turn_participant_actions

# pylint: disable=redefined-outer-name  # pytest fixtures


def test_select_npc_target_skips_a_mortally_wounded_player() -> None:
    """#1058: a player at 0 DP is out of the fight, so an NPC with nobody else to hit has no target."""
    npc_id = uuid.uuid4()
    player_id = uuid.uuid4()
    npc = CombatParticipant(
        participant_id=npc_id,
        participant_type=CombatParticipantType.NPC,
        name="Mob",
        current_dp=20,
        max_dp=20,
        dexterity=50,
    )
    player = CombatParticipant(
        participant_id=player_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Hero",
        current_dp=0,
        max_dp=10,
        dexterity=60,
    )
    combat = MagicMock(spec=CombatInstance)
    combat.participants = {npc_id: npc, player_id: player}
    target = combat_turn_participant_actions._select_npc_target(combat, npc_id)
    assert target is None


def test_select_npc_target_prefers_a_standing_player_over_a_downed_one() -> None:
    """#1058: with a downed player listed first, the NPC still picks the healthy one."""
    npc_id, downed_id, standing_id = uuid.uuid4(), uuid.uuid4(), uuid.uuid4()
    npc = CombatParticipant(
        participant_id=npc_id,
        participant_type=CombatParticipantType.NPC,
        name="Mob",
        current_dp=20,
        max_dp=20,
        dexterity=50,
    )
    downed = CombatParticipant(
        participant_id=downed_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Downed",
        current_dp=-3,
        max_dp=10,
        dexterity=60,
    )
    standing = CombatParticipant(
        participant_id=standing_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Standing",
        current_dp=8,
        max_dp=10,
        dexterity=60,
    )
    combat = MagicMock(spec=CombatInstance)
    combat.participants = {npc_id: npc, downed_id: downed, standing_id: standing}
    assert combat_turn_participant_actions._select_npc_target(combat, npc_id) is standing


@pytest.mark.asyncio
async def test_resolve_npc_target_uses_aggro_current_target() -> None:
    """When get_npc_current_target resolves an id, that participant is returned if alive."""
    npc_id = uuid.uuid4()
    player_id = uuid.uuid4()
    npc = CombatParticipant(
        participant_id=npc_id,
        participant_type=CombatParticipantType.NPC,
        name="Mob",
        current_dp=10,
        max_dp=10,
        dexterity=50,
    )
    player = CombatParticipant(
        participant_id=player_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Hero",
        current_dp=5,
        max_dp=10,
        dexterity=60,
    )
    combat = MagicMock(spec=CombatInstance)
    combat.participants = {npc_id: npc, player_id: player}
    combat.room_id = "room_1"

    broadcast_mock: AsyncMock = AsyncMock()
    mock_cs = MagicMock()
    mock_cs.broadcast_aggro_target_switches = broadcast_mock

    with patch.object(
        combat_turn_participant_actions,
        "update_aggro",
        return_value=(None, False),
    ):
        with patch.object(
            combat_turn_participant_actions,
            "get_npc_current_target",
            return_value=player_id,
        ):
            target = await combat_turn_participant_actions._resolve_npc_target(combat, npc, mock_cs)

    assert target is player
    broadcast_mock.assert_not_awaited()


@pytest.mark.asyncio
async def test_resolve_npc_target_broadcasts_when_aggro_switches() -> None:
    """update_aggro may signal a switch; combat service broadcasts room narrative."""
    npc_id = uuid.uuid4()
    player_id = uuid.uuid4()
    npc = CombatParticipant(
        participant_id=npc_id,
        participant_type=CombatParticipantType.NPC,
        name="Mob",
        current_dp=10,
        max_dp=10,
        dexterity=50,
    )
    player = CombatParticipant(
        participant_id=player_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Hero",
        current_dp=5,
        max_dp=10,
        dexterity=60,
    )
    combat = MagicMock(spec=CombatInstance)
    combat.participants = {npc_id: npc, player_id: player}
    combat.room_id = "room_z"
    combat.combat_id = uuid.uuid4()

    broadcast_mock: AsyncMock = AsyncMock()
    mock_cs = MagicMock()
    mock_cs.broadcast_aggro_target_switches = broadcast_mock

    with patch.object(
        combat_turn_participant_actions,
        "update_aggro",
        return_value=(player_id, True),
    ):
        with patch.object(
            combat_turn_participant_actions,
            "get_npc_current_target",
            return_value=player_id,
        ):
            target = await combat_turn_participant_actions._resolve_npc_target(combat, npc, mock_cs)

    assert target is player
    broadcast_mock.assert_awaited_once()


def test_strength_modifier_from_attacker_stats_defaults() -> None:
    """Strength modifier defaults to 50; digit strings coerce for bonus math."""
    assert combat_turn_participant_actions._strength_modifier_from_attacker_stats({}) == 50
    assert combat_turn_participant_actions._strength_modifier_from_attacker_stats({"strength": "99"}) == 99


def test_apply_physical_strength_bonus_adds_for_physical_only() -> None:
    """Physical damage adds strength bonus above 50; other damage types do not."""
    stats: dict[str, object] = {"strength": 54}
    assert combat_turn_participant_actions._apply_physical_strength_bonus(2, "physical", stats) == 2 + max(
        0, (54 - 50) // 2
    )
    assert combat_turn_participant_actions._apply_physical_strength_bonus(2, "fire", stats) == 2


@pytest.mark.asyncio
async def test_process_npc_turn_ends_combat_when_nobody_is_left_to_fight(monkeypatch: pytest.MonkeyPatch) -> None:
    """#1058: with every opponent incapacitated the NPC has no target, so the fight ends and bleed-out can run."""
    npc_id = uuid.uuid4()
    npc = CombatParticipant(
        participant_id=npc_id,
        participant_type=CombatParticipantType.NPC,
        name="Mob",
        current_dp=10,
        max_dp=10,
        dexterity=50,
    )
    combat_id = uuid.uuid4()
    combat = MagicMock(spec=CombatInstance)
    combat.participants = {npc_id: npc}
    combat.room_id = "r"
    combat.combat_id = combat_id

    mock_cs = MagicMock()
    end_combat_mock: AsyncMock = AsyncMock()
    process_attack_mock: AsyncMock = AsyncMock()
    mock_cs.end_combat = end_combat_mock
    mock_cs.process_attack = process_attack_mock

    async def _no_target(_c: object, _n: CombatParticipant, _svc: object) -> CombatParticipant | None:
        return None

    monkeypatch.setattr(combat_turn_participant_actions, "_resolve_npc_target", _no_target)

    await combat_turn_participant_actions.process_npc_turn(mock_cs, combat, npc, current_tick=7)

    end_combat_mock.assert_awaited_once_with(combat_id, "No remaining targets")
    process_attack_mock.assert_not_awaited()


@pytest.mark.asyncio
async def test_process_npc_turn_calls_process_attack_when_target_resolved(monkeypatch: pytest.MonkeyPatch) -> None:
    """Happy path: living NPC resolves target and combat_service.process_attack runs."""
    npc_id = uuid.uuid4()
    tgt_id = uuid.uuid4()
    npc = CombatParticipant(
        participant_id=npc_id,
        participant_type=CombatParticipantType.NPC,
        name="Mob",
        current_dp=10,
        max_dp=10,
        dexterity=50,
    )
    target = CombatParticipant(
        participant_id=tgt_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Hero",
        current_dp=5,
        max_dp=10,
        dexterity=60,
    )
    combat = MagicMock(spec=CombatInstance)
    combat.participants = {npc_id: npc, tgt_id: target}
    combat.room_id = "r"
    combat.combat_id = uuid.uuid4()

    mock_cs = MagicMock()
    mock_result = MagicMock()
    mock_result.success = True
    process_attack_mock: AsyncMock = AsyncMock(return_value=mock_result)
    mock_cs.process_attack = process_attack_mock

    async def _fake_resolve(_c: object, _n: CombatParticipant, _svc: object) -> CombatParticipant | None:
        return target

    monkeypatch.setattr(combat_turn_participant_actions, "_resolve_npc_target", _fake_resolve)
    monkeypatch.setattr(
        combat_turn_participant_actions, "get_config", lambda: MagicMock(game=MagicMock(basic_unarmed_damage=3))
    )

    await combat_turn_participant_actions.process_npc_turn(mock_cs, combat, npc, current_tick=5)
    process_attack_mock.assert_awaited_once()
    assert npc.last_action_tick == 5
