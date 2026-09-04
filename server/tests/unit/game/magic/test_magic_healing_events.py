"""Unit tests for MagicServiceHealingMixin."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic.magic_healing_events import MagicServiceHealingMixin
from server.models.spell import Spell, SpellEffectType, SpellRangeType, SpellSchool, SpellTargetType
from server.schemas.shared import TargetType


class _HealingService(MagicServiceHealingMixin):
    """Concrete stub for mixin tests."""

    def __init__(self) -> None:
        self.player_service = MagicMock()


def _spell(spell_id: str = "heal_self") -> Spell:
    return Spell(
        spell_id=spell_id,
        name="Heal",
        description="Restore DP",
        school=SpellSchool.CLERICAL,
        mp_cost=5,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.SAME_ROOM,
        effect_type=SpellEffectType.HEAL,
        effect_data={"heal_amount": 10},
    )


def test_effect_result_has_healing():
    """_effect_result_has_healing requires success, applied, and amount."""
    svc = _HealingService()
    assert svc._effect_result_has_healing({"success": True, "effect_applied": True, "heal_amount": 5})
    assert not svc._effect_result_has_healing({"success": True, "effect_applied": False, "heal_amount": 5})


def test_is_heal_other_target():
    """_is_heal_other_target detects heal-other on another player."""
    svc = _HealingService()
    caster_id = uuid.uuid4()
    other_id = uuid.uuid4()
    target = MagicMock(target_type=TargetType.PLAYER, target_id=other_id)
    effect = {"effect_applied": True, "heal_amount": 10}
    assert svc._is_heal_other_target(effect, _spell("heal_other"), target, caster_id)
    assert not svc._is_heal_other_target(effect, _spell("steal_life"), target, caster_id)
    assert not svc._is_heal_other_target(effect, _spell("heal_other"), target, other_id)


@pytest.mark.asyncio
async def test_send_healing_update_event_skips_without_healing():
    """No event when effect result lacks healing."""
    svc = _HealingService()
    svc._publish_or_send_dp_update = AsyncMock()  # type: ignore[method-assign]
    await svc._send_healing_update_event(uuid.uuid4(), {"success": False}, "heal_self", "room_1")
    svc._publish_or_send_dp_update.assert_not_awaited()


@pytest.mark.asyncio
async def test_publish_or_send_dp_update_no_player():
    """Missing player record skips publish."""
    svc = _HealingService()
    svc.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    svc._publish_dp_event = AsyncMock()  # type: ignore[method-assign]
    player_id = uuid.uuid4()
    await svc._publish_or_send_dp_update(player_id, {"heal_amount": 5}, "heal_self", "room_1")
    svc._publish_dp_event.assert_not_awaited()


@pytest.mark.asyncio
async def test_publish_or_send_dp_update_publishes_event():
    """Loaded player stats trigger DP event publish."""
    svc = _HealingService()
    player = MagicMock()
    player.get_stats.return_value = {"current_dp": 50, "max_dp": 100}
    svc.player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    svc._publish_dp_event = AsyncMock()  # type: ignore[method-assign]
    player_id = uuid.uuid4()
    await svc._publish_or_send_dp_update(player_id, {"heal_amount": 10}, "heal_self", "room_1")
    svc._publish_dp_event.assert_awaited_once()
    kwargs = svc._publish_dp_event.await_args.kwargs
    assert kwargs["current_dp"] == 50
    assert kwargs["old_dp"] == 40


@pytest.mark.asyncio
async def test_publish_dp_event_uses_event_bus():
    """Event bus path publishes PlayerDPUpdated."""
    svc = _HealingService()
    player_id = uuid.uuid4()
    container = MagicMock()
    container.event_bus = MagicMock()
    with patch("server.container.ApplicationContainer.get_instance", return_value=container):
        await svc._publish_dp_event(player_id, 40, 50, 100, 10, "heal_self", "room_1")
    container.event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_publish_dp_event_fallback_send_game_event():
    """Without event bus, falls back to send_game_event."""
    svc = _HealingService()
    player_id = uuid.uuid4()
    with patch("server.container.ApplicationContainer.get_instance", return_value=None):
        with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as send_event:
            await svc._publish_dp_event(player_id, 40, 50, 100, 10, "heal_self", "room_1")
    send_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_instant_heal_event_if_applied():
    """Instant heal sends update when effect applied."""
    svc = _HealingService()
    svc._send_healing_update_event = AsyncMock()  # type: ignore[method-assign]
    player_id = uuid.uuid4()
    target = MagicMock(room_id="room_1", target_id=str(player_id))
    spell = _spell("heal_self")
    result = {"effect_result": {"success": True, "effect_applied": True, "heal_amount": 8}}
    await svc._send_instant_heal_event_if_applied(player_id, spell, target, result)
    svc._send_healing_update_event.assert_awaited_once()
