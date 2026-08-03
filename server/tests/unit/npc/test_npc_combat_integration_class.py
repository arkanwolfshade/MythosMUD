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


def test_get_npc_display_name_prefers_lifecycle(integration: NPCCombatIntegration) -> None:
    with patch.object(integration, "_get_npc_name_from_lifecycle", return_value="Byakhee"):
        assert integration._get_npc_display_name("byakhee_1") == "Byakhee"


def test_get_npc_display_name_falls_back_to_id(integration: NPCCombatIntegration) -> None:
    with patch.object(integration, "_get_npc_name_from_lifecycle", return_value=None):
        assert integration._get_npc_display_name("ghoul_arkham_1") == "Ghoul"


def test_get_npc_lifecycle_manager_from_config(integration: NPCCombatIntegration) -> None:
    manager = MagicMock()
    state = MagicMock()
    state.npc_lifecycle_manager = manager
    app = MagicMock()
    app.state = state
    config = MagicMock()
    config._app_instance = app
    with patch("server.npc.combat_integration.get_config", return_value=config):
        assert integration._get_npc_lifecycle_manager() is manager


def test_get_npc_lifecycle_manager_missing_app(integration: NPCCombatIntegration) -> None:
    config = MagicMock()
    config._app_instance = None
    with patch("server.npc.combat_integration.get_config", return_value=config):
        assert integration._get_npc_lifecycle_manager() is None


def test_get_npc_name_from_lifecycle_swallows_errors(integration: NPCCombatIntegration) -> None:
    with patch.object(integration, "_get_npc_lifecycle_manager", side_effect=RuntimeError("boom")):
        assert integration._get_npc_name_from_lifecycle("npc_x") is None


@pytest.mark.asyncio
async def test_publish_player_dp_updated_after_npc_damage(
    integration: NPCCombatIntegration, mock_persistence: MagicMock
) -> None:
    pid = uuid.uuid4()
    player = MagicMock()
    player.get_stats = MagicMock(return_value={"current_dp": 7, "max_dp": 20})
    mock_persistence.get_player_by_id = AsyncMock(return_value=player)
    bus = MagicMock()
    integration.event_bus = bus
    with patch.object(integration, "_convert_target_id_to_uuid", return_value=pid):
        await integration._publish_player_dp_updated_after_npc_damage(str(pid), 3, "room_a")
    bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_publish_player_dp_updated_skips_without_player_or_bus(
    integration: NPCCombatIntegration, mock_persistence: MagicMock
) -> None:
    pid = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    integration.event_bus = MagicMock()
    with patch.object(integration, "_convert_target_id_to_uuid", return_value=pid):
        await integration._publish_player_dp_updated_after_npc_damage(str(pid), 3, "room_a")
    cast(MagicMock, integration.event_bus).publish.assert_not_called()


@pytest.mark.asyncio
async def test_publish_player_dp_updated_swallows_errors(integration: NPCCombatIntegration) -> None:
    with patch.object(integration, "_get_player_for_dp_update", side_effect=RuntimeError("fail")):
        await integration._publish_player_dp_updated_after_npc_damage("bad", 1, "room_a")


def test_compute_dp_update_fields_non_dict_stats(integration: NPCCombatIntegration) -> None:
    player = MagicMock()
    player.get_stats = MagicMock(return_value="broken")
    old_dp, new_dp, max_dp = integration._compute_dp_update_fields(player, 2)
    assert new_dp == 0
    assert old_dp == 2
    assert max_dp == 20  # empty stats -> default con/siz fallback


def test_publish_player_dp_updated_event_noop_without_bus(integration: NPCCombatIntegration) -> None:
    integration.event_bus = None
    integration._publish_player_dp_updated_event(uuid.uuid4(), 10, 8, 20, 2, "room_a")


@pytest.mark.asyncio
async def test_publish_npc_attack_to_nats_success(
    integration: NPCCombatIntegration, mock_persistence: MagicMock
) -> None:
    pid = uuid.uuid4()
    player = MagicMock()
    player.name = "Investigator"
    player.get_stats = MagicMock(return_value={"current_dp": 9, "max_dp": 20})
    mock_persistence.get_player_by_id = AsyncMock(return_value=player)
    publisher = MagicMock()
    publisher.publish_player_attacked = AsyncMock(return_value=True)
    with (
        patch.object(integration, "_get_combat_event_publisher", return_value=publisher),
        patch.object(integration, "_convert_target_id_to_uuid", return_value=pid),
        patch.object(integration, "_get_npc_display_name", return_value="Ghoul"),
    ):
        await integration._publish_npc_attack_to_nats("npc_1", str(pid), "room_a", 4, "physical")
    publisher.publish_player_attacked.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_npc_attack_to_nats_no_publisher(integration: NPCCombatIntegration) -> None:
    with patch.object(integration, "_get_combat_event_publisher", return_value=None):
        await integration._publish_npc_attack_to_nats("npc_1", str(uuid.uuid4()), "room_a", 4, "physical")


@pytest.mark.asyncio
async def test_publish_npc_attack_to_nats_swallows_errors(integration: NPCCombatIntegration) -> None:
    with patch.object(integration, "_get_combat_event_publisher", side_effect=RuntimeError("nats down")):
        await integration._publish_npc_attack_to_nats("npc_1", str(uuid.uuid4()), "room_a", 4, "physical")


def test_get_combat_event_publisher_from_container(integration: NPCCombatIntegration) -> None:
    publisher = MagicMock()
    combat_service = MagicMock()
    combat_service._combat_event_publisher = publisher
    container = MagicMock()
    container.combat_service = combat_service
    state = MagicMock()
    state.container = container
    app = MagicMock()
    app.state = state
    config = MagicMock()
    config._app_instance = app
    with patch("server.npc.combat_integration.get_config", return_value=config):
        assert integration._get_combat_event_publisher() is publisher


def test_get_combat_event_publisher_missing_pieces(integration: NPCCombatIntegration) -> None:
    config = MagicMock()
    config._app_instance = None
    with patch("server.npc.combat_integration.get_config", return_value=config):
        assert integration._get_combat_event_publisher() is None


@pytest.mark.asyncio
async def test_get_player_and_stats_for_nats_missing_player(
    integration: NPCCombatIntegration, mock_persistence: MagicMock
) -> None:
    pid = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with patch.object(integration, "_convert_target_id_to_uuid", return_value=pid):
        target_uuid, player, stats = await integration._get_player_and_stats_for_nats(str(pid))
    assert target_uuid == pid
    assert player is None
    assert stats is None


def test_build_player_attacked_event_uses_dp_fallback(integration: NPCCombatIntegration) -> None:
    player = MagicMock()
    player.name = "Target"
    with patch.object(integration, "_get_npc_display_name", return_value="Horror"):
        evt = integration._build_player_attacked_event(
            "npc_x",
            "room_a",
            uuid.uuid4(),
            player,
            {"dp": 5, "max_health": 15},
            3,
            "physical",
        )
    assert evt.attacker_name == "Horror"
    assert evt.target_current_dp == 5
    assert evt.target_max_dp == 15


@pytest.mark.asyncio
async def test_handle_npc_death_invalid_killer_returns_false(integration: NPCCombatIntegration) -> None:
    ok = await integration.handle_npc_death("npc_1", "room_a", killer_id="not-a-uuid")
    assert ok is False


def test_calculate_max_dp_from_max_health(integration: NPCCombatIntegration) -> None:
    assert integration._calculate_max_dp({"max_health": 33}) == 33


def test_get_player_combat_stats_string_and_invalid_dp(integration: NPCCombatIntegration) -> None:
    assert integration._get_player_combat_stats({"current_dp": "12", "max_dp": 20})["dp"] == 12
    assert integration._get_player_combat_stats({"current_dp": object(), "max_dp": 20})["dp"] == 100


def test_normalize_npc_stats_from_dp(integration: NPCCombatIntegration) -> None:
    out = integration._normalize_npc_stats({"dp": 9})
    assert out["hp"] == 9


@pytest.mark.asyncio
async def test_get_combat_stats_entity_not_found(integration: NPCCombatIntegration, mock_persistence: MagicMock) -> None:
    pid = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    assert await integration.get_combat_stats(str(pid)) == {}


@pytest.mark.asyncio
async def test_get_combat_stats_error_without_npc_stats(integration: NPCCombatIntegration) -> None:
    with patch.object(integration, "_persistence") as persistence:
        persistence.get_player_by_id = AsyncMock(side_effect=TypeError("bad"))
        # Valid UUID path still hits except when get_player_by_id raises TypeError
        result = await integration.get_combat_stats(str(uuid.uuid4()))
    assert result == {}
