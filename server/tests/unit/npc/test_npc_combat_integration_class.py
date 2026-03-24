"""
Unit tests for server.npc.combat_integration.NPCCombatIntegration (helpers and small flows).
"""

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events import EventBus
from server.events.event_types import NPCAttacked
from server.npc.combat_integration import NPCCombatIntegration

# pylint: disable=protected-access  # Reason: Testing internal helpers
# pyright: reportPrivateUsage=false
# pylint: disable=redefined-outer-name  # Reason: pytest fixtures share names with test parameters


@pytest.fixture
def mock_persistence() -> MagicMock:
    """Persistence mock with async get_player_by_id for integration tests."""
    p = MagicMock()
    p.get_player_by_id = AsyncMock()
    return p


@pytest.fixture
def integration(mock_persistence: MagicMock) -> NPCCombatIntegration:
    """NPCCombatIntegration wired to the mock persistence layer."""
    return NPCCombatIntegration(event_bus=EventBus(), async_persistence=mock_persistence)


def test_get_npc_stats_defaults(integration: NPCCombatIntegration) -> None:
    """Empty npc_stats yields default strength/constitution."""
    assert integration._get_npc_stats(None) == {"strength": 50, "constitution": 50}


def test_get_npc_stats_preserves_values(integration: NPCCombatIntegration) -> None:
    """Provided npc_stats are returned as-is."""
    stats = {"strength": 60, "constitution": 55}
    assert integration._get_npc_stats(stats) == stats


def test_derive_npc_name_from_id(integration: NPCCombatIntegration) -> None:
    """First underscore segment title-cased."""
    assert integration._derive_npc_name_from_id("nightgaunt_limbo_1") == "Nightgaunt"
    assert integration._derive_npc_name_from_id("") == ""


def test_calculate_damage_physical_strength_bonus(integration: NPCCombatIntegration) -> None:
    """Physical damage adds strength modifier from base 50."""
    dmg = integration.calculate_damage(
        attacker_stats={"strength": 54},
        target_stats={},
        weapon_damage=2,
        damage_type="physical",
    )
    assert dmg >= 3


def test_calculate_damage_weapon_type_no_strength_bonus(integration: NPCCombatIntegration) -> None:
    """Non-physical damage type does not add strength bonus to weapon line."""
    dmg = integration.calculate_damage(
        attacker_stats={"strength": 80},
        target_stats={},
        weapon_damage=4,
        damage_type="slashing",
    )
    assert dmg == 4


def test_get_int_stat_parses_numeric_string(integration: NPCCombatIntegration) -> None:
    """Digit strings coerce to int."""
    assert integration._get_int_stat({"x": "42"}, "x") == 42


def test_calculate_max_dp_from_constitution_and_size(integration: NPCCombatIntegration) -> None:
    """Fallback max_dp uses (con+siz)//5."""
    stats = cast(dict[str, object], {"constitution": 50, "size": 50})
    assert integration._calculate_max_dp(stats) == 20


def test_normalize_npc_stats_adds_hp_from_determination_points(integration: NPCCombatIntegration) -> None:
    """hp alias filled from determination_points."""
    out = integration._normalize_npc_stats({"determination_points": 12})
    assert out["hp"] == 12


@pytest.mark.asyncio
async def test_get_combat_stats_for_player(integration: NPCCombatIntegration, mock_persistence: MagicMock) -> None:
    """Player branch returns combat-shaped stats."""
    pid = uuid.uuid4()
    player = MagicMock()
    player.get_stats = MagicMock(
        return_value={
            "current_dp": 8,
            "max_dp": 20,
            "strength": 40,
            "constitution": 45,
        }
    )
    mock_persistence.get_player_by_id = AsyncMock(return_value=player)
    stats = await integration.get_combat_stats(str(pid))
    assert stats["dp"] == 8
    assert stats["max_dp"] == 20


@pytest.mark.asyncio
async def test_get_combat_stats_npc_only_normalized(integration: NPCCombatIntegration) -> None:
    """Invalid UUID with npc_stats returns normalized NPC stats."""
    stats = await integration.get_combat_stats("not-a-uuid", npc_stats={"hp": 5})
    assert stats.get("hp") == 5


@pytest.mark.asyncio
async def test_handle_npc_death_with_killer_applies_mechanics(
    integration: NPCCombatIntegration, mock_persistence: MagicMock
) -> None:
    """Killer path loads player and calls game mechanics helpers."""
    killer = uuid.uuid4()
    mock_player = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    with patch.object(integration, "_game_mechanics") as gm:
        gm.gain_occult_knowledge = AsyncMock()
        gm.apply_lucidity_loss = AsyncMock()
        ok = await integration.handle_npc_death("npc_x", "room_1", killer_id=str(killer))
    assert ok is True
    gm.gain_occult_knowledge.assert_awaited_once()
    gm.apply_lucidity_loss.assert_awaited_once()


def test_compute_dp_update_fields(integration: NPCCombatIntegration) -> None:
    """After damage, old_dp reflects pre-hit value."""
    player = MagicMock()
    player.get_stats = MagicMock(return_value={"current_dp": 7, "max_dp": 20})
    old, new, mx = integration._compute_dp_update_fields(player, damage=3)
    assert new == 7
    assert old == 10
    assert mx == 20


def test_get_npc_name_from_lifecycle_reads_active_instance(integration: NPCCombatIntegration) -> None:
    """Display name resolves from lifecycle_manager.active_npcs when present."""
    lm = MagicMock()
    inst = MagicMock()
    inst.name = "Byakhee"
    lm.active_npcs = {"byakhee_1": inst}
    with patch.object(integration, "_get_npc_lifecycle_manager", return_value=lm):
        assert integration._get_npc_name_from_lifecycle("byakhee_1") == "Byakhee"


def test_get_npc_name_from_lifecycle_returns_none_when_missing(integration: NPCCombatIntegration) -> None:
    """When lifecycle manager is unavailable, display name lookup returns None."""
    with patch.object(integration, "_get_npc_lifecycle_manager", return_value=None):
        assert integration._get_npc_name_from_lifecycle("ghost") is None


def test_publish_attack_event_emits_npc_attacked(integration: NPCCombatIntegration) -> None:
    """_publish_attack_event forwards to event bus when configured."""
    publish_mock: MagicMock = MagicMock()
    bus = MagicMock()
    bus.publish = publish_mock
    integration.event_bus = bus
    integration._publish_attack_event("npc_a", "player_b", "room_z", 5, "physical")
    publish_mock.assert_called_once()
    call_args = publish_mock.call_args
    assert call_args is not None
    evt = cast(NPCAttacked, call_args[0][0])
    assert evt.npc_id == "npc_a"
    assert evt.target_id == "player_b"
    assert evt.room_id == "room_z"
    assert evt.damage == 5
