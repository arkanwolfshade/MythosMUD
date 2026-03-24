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


def test_select_npc_target_prefers_mortally_wounded_player_over_skipping() -> None:
    """Player at 0 DP is not is_dead; NPC turn must still select them (ADR-016 / auto combat)."""
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
    assert target is player


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
