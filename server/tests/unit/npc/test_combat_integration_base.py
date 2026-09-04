"""Unit tests for NPCCombatIntegrationBase helpers."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events import EventBus
from server.npc.combat_integration import NPCCombatIntegration
from server.npc.combat_integration_base import _resolve_npc_combat_service_raw


@pytest.fixture
def integration() -> NPCCombatIntegration:
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=None)
    return NPCCombatIntegration(event_bus=EventBus(), async_persistence=persistence)


def test_resolve_npc_combat_service_from_container() -> None:
    service = MagicMock()
    combat_service = MagicMock()
    combat_service.get_npc_combat_integration_service.return_value = service
    container = MagicMock(combat_service=combat_service)
    app = MagicMock()
    app.state.container = container
    assert _resolve_npc_combat_service_raw(app) is service


def test_calculate_damage_minimum_on_bad_stats(integration: NPCCombatIntegration) -> None:
    assert integration.calculate_damage({"strength": "bad"}, {}, weapon_damage=0) == 1


@pytest.mark.asyncio
async def test_apply_combat_effects_npc_target(integration: NPCCombatIntegration) -> None:
    npc_uuid = uuid.uuid4()
    integration._persistence.get_player_by_id = AsyncMock(return_value=None)
    ok = await integration.apply_combat_effects(str(npc_uuid), 5, "physical")
    assert ok is True


@pytest.mark.asyncio
async def test_apply_combat_effects_invalid_uuid_raises(integration: NPCCombatIntegration) -> None:
    with pytest.raises(ValueError):
        await integration.apply_combat_effects("not-a-player-uuid", 5, "physical")


@pytest.mark.asyncio
async def test_apply_combat_effects_player(integration: NPCCombatIntegration) -> None:
    player_id = uuid.uuid4()
    player = MagicMock()
    integration._persistence.get_player_by_id = AsyncMock(return_value=player)
    integration._game_mechanics = MagicMock()
    integration._game_mechanics.damage_player = AsyncMock(return_value=(True, player))
    integration._game_mechanics.apply_lucidity_loss = AsyncMock(return_value=(True, None))
    integration._game_mechanics.apply_fear = AsyncMock(return_value=(True, None))
    ok = await integration.apply_combat_effects(str(player_id), 4, "mental")
    assert ok is True
    integration._game_mechanics.apply_lucidity_loss.assert_awaited_once()


@pytest.mark.asyncio
async def test_apply_combat_effects_validation_error(integration: NPCCombatIntegration) -> None:
    from server.exceptions import ValidationError as MythosValidationError

    integration._persistence.get_player_by_id = AsyncMock(side_effect=MythosValidationError("bad", context=None))
    ok = await integration.apply_combat_effects(str(uuid.uuid4()), 1, "physical")
    assert ok is False


def test_convert_target_id_to_uuid(integration: NPCCombatIntegration) -> None:
    pid = uuid.uuid4()
    assert integration._convert_target_id_to_uuid(pid) == pid
    assert integration._convert_target_id_to_uuid(str(pid)) == pid


def test_handle_unexpected_error_logs(integration: NPCCombatIntegration) -> None:
    integration._handle_unexpected_error("t1", 1, "physical", RuntimeError("boom"))


@pytest.mark.asyncio
async def test_is_target_in_login_grace_period_false(integration: NPCCombatIntegration) -> None:
    with patch("server.npc.combat_integration_base.get_config") as mock_cfg:
        mock_cfg.return_value = MagicMock(_app_instance=None)
        result = await integration._is_target_in_login_grace_period(str(uuid.uuid4()))
    assert result is False


@pytest.mark.asyncio
async def test_apply_combat_effects_grace_period_blocks_damage(integration: NPCCombatIntegration) -> None:
    player_id = uuid.uuid4()
    player = MagicMock()
    integration._persistence.get_player_by_id = AsyncMock(return_value=player)
    integration._game_mechanics = MagicMock()
    app = MagicMock()
    app.state.connection_manager = MagicMock()
    config = MagicMock(_app_instance=app)
    with patch("server.npc.combat_integration_base.get_config", return_value=config):
        with patch(
            "server.npc.combat_integration_base.is_player_in_login_grace_period",
            return_value=True,
        ):
            ok = await integration.apply_combat_effects(str(player_id), 5, "physical")
    assert ok is False


@pytest.mark.asyncio
async def test_apply_mental_effects_occult(integration: NPCCombatIntegration) -> None:
    integration._game_mechanics = MagicMock()
    integration._game_mechanics.apply_lucidity_loss = AsyncMock(return_value=(True, None))
    integration._game_mechanics.apply_fear = AsyncMock(return_value=(True, None))
    await integration._apply_mental_effects(str(uuid.uuid4()), 9, "occult")
    integration._game_mechanics.apply_lucidity_loss.assert_awaited_once()
    integration._game_mechanics.apply_fear.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_npc_attack_direct_path(integration: NPCCombatIntegration) -> None:
    with patch.object(
        integration, "_try_delegate_npc_attack_to_combat_service", new_callable=AsyncMock, return_value=None
    ):
        with patch.object(integration, "_is_target_in_login_grace_period", new_callable=AsyncMock, return_value=False):
            with patch.object(integration, "_perform_direct_npc_attack", new_callable=AsyncMock) as mock_attack:
                ok = await integration.handle_npc_attack("npc-1", str(uuid.uuid4()), "room-1", 5)
    assert ok is True
    mock_attack.assert_awaited_once()


def test_calculate_damage_with_stats(integration: NPCCombatIntegration) -> None:
    dmg = integration.calculate_damage({"strength": 15}, {"armor": 2}, weapon_damage=3)
    assert dmg >= 1


@pytest.mark.asyncio
async def test_apply_combat_effects_attribute_error_raises(integration: NPCCombatIntegration) -> None:
    integration._persistence.get_player_by_id = AsyncMock(side_effect=AttributeError("missing"))
    with pytest.raises(AttributeError):
        await integration.apply_combat_effects(str(uuid.uuid4()), 1, "physical")


@pytest.mark.asyncio
async def test_perform_direct_npc_attack(integration: NPCCombatIntegration) -> None:
    target_id = str(uuid.uuid4())
    integration._get_target_stats = AsyncMock(return_value={"armor": 0})
    integration.apply_combat_effects = AsyncMock(return_value=True)
    integration._publish_player_dp_updated_after_npc_damage = AsyncMock()
    integration._publish_attack_event = MagicMock()
    integration._publish_npc_attack_to_nats = AsyncMock()
    await integration._perform_direct_npc_attack("npc-1", target_id, "room-1", 5, "physical", {"strength": 10})
    integration.apply_combat_effects.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_npc_attack_delegated(integration: NPCCombatIntegration) -> None:
    with patch.object(
        integration,
        "_try_delegate_npc_attack_to_combat_service",
        new_callable=AsyncMock,
        return_value=True,
    ):
        ok = await integration.handle_npc_attack("npc-1", str(uuid.uuid4()), "room-1", 3)
    assert ok is True
