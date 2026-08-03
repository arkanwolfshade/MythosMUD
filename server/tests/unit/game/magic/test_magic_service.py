"""Unit tests for MagicService and completion mixin paths."""

import uuid
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic.casting_state_manager import CastingState, CastingStateManager
from server.game.magic.magic_service import MagicService
from server.models.spell import (
    Spell,
    SpellEffectType,
    SpellMaterial,
    SpellRangeType,
    SpellSchool,
    SpellTargetType,
)
from server.schemas.shared import TargetMatch, TargetType

# pylint: disable=protected-access,redefined-outer-name


@pytest.fixture
def player_id() -> uuid.UUID:
    return uuid.uuid4()


@pytest.fixture
def base_spell() -> Spell:
    return Spell(
        spell_id="fire_bolt",
        name="Fire Bolt",
        description="A bolt of fire",
        school=SpellSchool.ELEMENTAL,
        mp_cost=5,
        target_type=SpellTargetType.ENTITY,
        range_type=SpellRangeType.SAME_ROOM,
        effect_type=SpellEffectType.DAMAGE,
    )


@pytest.fixture
def mock_player(player_id: uuid.UUID) -> MagicMock:
    player = MagicMock()
    player.name = "Investigator"
    player.current_room_id = "room_001"
    player.get_stats.return_value = {
        "magic_points": 20,
        "max_magic_points": 20,
        "lucidity": 80,
        "intelligence": 60,
        "luck": 70,
        "power": 50,
    }
    return player


@pytest.fixture
def target_match(player_id: uuid.UUID) -> TargetMatch:
    return TargetMatch(
        target_id=str(player_id),
        target_name="Investigator",
        target_type=TargetType.PLAYER,
        room_id="room_001",
    )


def _build_magic_service(
    mock_player: MagicMock,
    *,
    spell_registry: MagicMock | None = None,
    optional_deps: dict[str, Any] | None = None,
) -> MagicService:
    registry = spell_registry or MagicMock()
    player_service = MagicMock()
    player_service.persistence = MagicMock()
    player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    targeting = MagicMock()
    targeting.resolve_spell_target = AsyncMock()
    effects = MagicMock()
    effects.process_effect = AsyncMock(return_value={"success": True, "message": "It burns."})
    deps = optional_deps or {}
    return MagicService(registry, player_service, targeting, effects, deps)


@pytest.fixture
def magic_service(mock_player: MagicMock, base_spell: Spell, target_match: TargetMatch) -> MagicService:
    registry = MagicMock()
    registry.get_spell.return_value = base_spell
    registry.get_spell_by_name.return_value = None
    service = _build_magic_service(mock_player, spell_registry=registry)
    service.spell_targeting_service.resolve_spell_target = AsyncMock(return_value=(target_match, None))
    service.player_spell_repository.get_player_spell = AsyncMock(return_value=MagicMock(mastery=10))
    service.player_spell_repository.record_spell_cast = AsyncMock()
    service.spell_costs_service.apply_costs = AsyncMock()
    service.spell_costs_service.restore_mp = AsyncMock(return_value={"success": True, "message": "MP restored"})
    service.spell_materials_service.check_materials = AsyncMock(return_value=[])
    service.spell_materials_service.consume_materials = AsyncMock(return_value={"success": True})
    service.casting_state_manager = MagicMock(spec=CastingStateManager)
    service.casting_state_manager.is_casting.return_value = False
    service.casting_state_manager.get_casting_state.return_value = None
    service.casting_state_manager.get_all_casting_players.return_value = []
    return service


def test_resolve_heal_spell_id_variants() -> None:
    assert MagicService._resolve_heal_spell_id("fire", None) == "fire"
    assert MagicService._resolve_heal_spell_id("heal", None) == "heal_self"
    assert MagicService._resolve_heal_spell_id("heal", "self") == "heal_self"
    assert MagicService._resolve_heal_spell_id("heal", "Bob") == "heal_other"


def test_check_mp_and_lucidity(magic_service: MagicService, base_spell: Spell) -> None:
    ok, msg = magic_service._check_mp_sufficient({"magic_points": 10}, base_spell)
    assert ok is True and msg == ""
    ok, msg = magic_service._check_mp_sufficient({"magic_points": 1}, base_spell)
    assert ok is False and "Not enough magic points" in msg

    mythos = base_spell.model_copy(update={"school": SpellSchool.MYTHOS, "lucidity_cost": 10})
    ok, msg = magic_service._check_lucidity_sufficient({"lucidity": 5}, mythos)
    assert ok is False and "lucidity" in msg.lower()
    ok, msg = magic_service._check_lucidity_sufficient({"lucidity": 50}, mythos)
    assert ok is True


@pytest.mark.asyncio
async def test_get_player_and_normalized_stats(magic_service: MagicService, player_id: uuid.UUID) -> None:
    player, stats = await magic_service._get_player_and_normalized_stats(player_id)
    assert player is not None
    assert stats["max_magic_points"] == 20

    mock_player = MagicMock()
    mock_player.get_stats.return_value = {"power": 50, "magic_points": 0}
    magic_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    _, stats_no_max = await magic_service._get_player_and_normalized_stats(player_id)
    assert stats_no_max["max_magic_points"] == 10
    assert stats_no_max["magic_points"] == 10


@pytest.mark.asyncio
async def test_can_cast_spell_paths(magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell) -> None:
    ok, msg = await magic_service.can_cast_spell(player_id, base_spell)
    assert ok is True and msg == ""

    magic_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    ok, msg = await magic_service.can_cast_spell(player_id, base_spell)
    assert ok is False and "cosmic forces" in msg


@pytest.mark.asyncio
async def test_can_cast_spell_unknown_and_materials(
    magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell
) -> None:
    magic_service.player_spell_repository.get_player_spell = AsyncMock(return_value=None)
    ok, msg = await magic_service.can_cast_spell(player_id, base_spell)
    assert ok is False and "not learned" in msg

    magic_service.player_spell_repository.get_player_spell = AsyncMock(return_value=MagicMock(mastery=0))
    spell_with_materials = base_spell.model_copy(update={"materials": [SpellMaterial(item_id="herb", consumed=True)]})
    magic_service.spell_materials_service.check_materials = AsyncMock(return_value=["herb"])
    ok, msg = await magic_service.can_cast_spell(player_id, spell_with_materials)
    assert ok is False and "materials" in msg


def test_check_already_casting(magic_service: MagicService, player_id: uuid.UUID) -> None:
    magic_service.casting_state_manager.is_casting.return_value = False
    assert magic_service._check_already_casting(player_id) is None

    magic_service.casting_state_manager.is_casting.return_value = True
    magic_service.casting_state_manager.get_casting_state.return_value = None
    result = magic_service._check_already_casting(player_id)
    assert result is not None and result["success"] is False

    state = MagicMock(spell_name="Fire Bolt")
    magic_service.casting_state_manager.get_casting_state.return_value = state
    result = magic_service._check_already_casting(player_id)
    assert result is not None and "Fire Bolt" in result["message"]


def test_calculate_initiative_tick(magic_service: MagicService) -> None:
    combat = MagicMock(next_turn_tick=100, turn_interval_ticks=10)
    assert magic_service._calculate_initiative_tick(combat, 95) == 100
    combat.next_turn_tick = 90
    assert magic_service._calculate_initiative_tick(combat, 95) == 105


@pytest.mark.asyncio
async def test_cast_spell_instant_success(magic_service: MagicService, player_id: uuid.UUID) -> None:
    with patch("random.randint", return_value=1):
        result = await magic_service.cast_spell(player_id, "fire_bolt")
    assert result["success"] is True
    assert result["spell_name"] == "Fire Bolt"
    magic_service.spell_costs_service.apply_costs.assert_awaited_once()


@pytest.mark.asyncio
async def test_cast_spell_not_found(magic_service: MagicService, player_id: uuid.UUID) -> None:
    magic_service.spell_registry.get_spell.return_value = None
    magic_service.spell_registry.get_spell_by_name.return_value = None
    result = await magic_service.cast_spell(player_id, "missing")
    assert result["success"] is False and "not found" in result["message"]


@pytest.mark.asyncio
async def test_cast_spell_roll_failure(magic_service: MagicService, player_id: uuid.UUID) -> None:
    with patch("random.randint", return_value=100):
        result = await magic_service.cast_spell(player_id, "fire_bolt")
    assert result["success"] is False and result.get("costs_paid") is True


@pytest.mark.asyncio
async def test_cast_spell_delayed(magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell) -> None:
    delayed = base_spell.model_copy(update={"casting_time_seconds": 3})
    magic_service.spell_registry.get_spell.return_value = delayed
    magic_service.casting_state_manager.start_casting = MagicMock()
    with patch("server.game.magic.magic_service.get_current_tick", return_value=50):
        with patch("random.randint", return_value=1):
            result = await magic_service.cast_spell(player_id, "fire_bolt")
    assert result["success"] is True and result["is_casting"] is True
    magic_service.casting_state_manager.start_casting.assert_called_once()


@pytest.mark.asyncio
async def test_cast_spell_material_consume_failure(
    magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell
) -> None:
    spell = base_spell.model_copy(update={"materials": [SpellMaterial(item_id="herb", consumed=True)]})
    magic_service.spell_registry.get_spell.return_value = spell
    magic_service.spell_materials_service.consume_materials = AsyncMock(
        return_value={"success": False, "message": "No herb"}
    )
    with patch("random.randint", return_value=1):
        result = await magic_service.cast_spell(player_id, "fire_bolt")
    assert result["success"] is False and "herb" in result["message"]


@pytest.mark.asyncio
async def test_interrupt_casting_luck_pass(
    magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell
) -> None:
    state = MagicMock(spell_name="Fire Bolt", spell=base_spell, mp_cost=5)
    magic_service.casting_state_manager.get_casting_state.return_value = state
    with patch("random.randint", return_value=1):
        result = await magic_service.interrupt_casting(player_id)
    assert result["success"] is True and result["mp_lost"] is False


@pytest.mark.asyncio
async def test_interrupt_casting_luck_fail(
    magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell
) -> None:
    state = MagicMock(spell_name="Fire Bolt", spell=base_spell, mp_cost=5)
    magic_service.casting_state_manager.get_casting_state.return_value = state
    with patch("random.randint", return_value=100):
        result = await magic_service.interrupt_casting(player_id)
    assert result["success"] is True and result["mp_lost"] is True


@pytest.mark.asyncio
async def test_interrupt_casting_not_casting(magic_service: MagicService, player_id: uuid.UUID) -> None:
    magic_service.casting_state_manager.get_casting_state.return_value = None
    result = await magic_service.interrupt_casting(player_id)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_restore_mp(magic_service: MagicService, player_id: uuid.UUID) -> None:
    result = await magic_service.restore_mp(player_id, 5)
    assert result["success"] is True
    magic_service.spell_costs_service.restore_mp.assert_awaited_once_with(player_id, 5)


@pytest.mark.asyncio
async def test_check_casting_progress_completes(
    magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell, mock_player: MagicMock
) -> None:
    casting_state = CastingState(
        player_id=player_id,
        spell_id=base_spell.spell_id,
        spell_name=base_spell.name,
        start_tick=1,
        casting_time_seconds=0,
        remaining_seconds=0,
        combat_id=None,
        next_initiative_tick=None,
        mp_cost=5,
        target_name="Investigator",
        target_id=str(player_id),
        target_type="player",
        mastery=5,
        spell=base_spell,
    )
    magic_service.casting_state_manager.get_all_casting_players.return_value = [player_id]
    magic_service.casting_state_manager.get_casting_state.return_value = casting_state
    magic_service.casting_state_manager.update_casting_progress.return_value = True
    magic_service.casting_state_manager.complete_casting = MagicMock()
    magic_service.casting_state_manager.is_casting.return_value = False
    magic_service.combat_service = None
    magic_service._send_spell_completion_message = AsyncMock()
    magic_service._send_healing_update_event = AsyncMock()
    await magic_service.check_casting_progress(10)
    magic_service.spell_costs_service.apply_costs.assert_awaited()


def test_recreate_target_from_state(magic_service: MagicService, player_id: uuid.UUID, mock_player: MagicMock) -> None:
    state = MagicMock(
        target_type="player",
        target_id=str(player_id),
        target_name="Investigator",
    )
    target = magic_service._recreate_target_from_state(state, player_id, mock_player, "room_001")
    assert target.target_type == TargetType.PLAYER
    assert target.room_id == "room_001"


def test_parse_casting_target_id(magic_service: MagicService, player_id: uuid.UUID) -> None:
    assert magic_service._parse_casting_target_id(MagicMock(target_id=None)) is None
    assert magic_service._parse_casting_target_id(MagicMock(target_id=str(player_id))) == player_id
    assert magic_service._parse_casting_target_id(MagicMock(target_id="not-a-uuid")) is None


@pytest.mark.asyncio
async def test_complete_casting_via_combat_queue(
    magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell, mock_player: MagicMock
) -> None:
    casting_state = MagicMock(
        spell=base_spell,
        target_id=str(player_id),
        target_name="Investigator",
        target_type="player",
        mastery=5,
    )
    combat = MagicMock(combat_id=uuid.uuid4(), combat_round=1)
    magic_service.combat_service = MagicMock()
    magic_service.combat_service.get_combat_by_participant = AsyncMock(return_value=combat)
    magic_service.combat_service.queue_combat_action = AsyncMock(return_value=True)
    magic_service.casting_state_manager.complete_casting = MagicMock()
    magic_service.casting_state_manager.is_casting.return_value = False
    await magic_service._complete_casting(player_id, casting_state)
    magic_service.combat_service.queue_combat_action.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_player_and_room_missing_player(magic_service: MagicService, player_id: uuid.UUID) -> None:
    magic_service.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    magic_service.casting_state_manager.complete_casting = MagicMock()
    assert await magic_service._get_player_and_room(player_id) is None


@pytest.mark.asyncio
async def test_send_spell_execution_notifications(magic_service: MagicService, player_id: uuid.UUID) -> None:
    magic_service._send_spell_completion_message = AsyncMock()
    magic_service._send_healing_update_event = AsyncMock()
    effect = {"success": True, "message": "Done", "effect_applied": True, "heal_amount": 3}
    await magic_service.send_spell_execution_notifications(player_id, "heal_self", effect, "room_001")
    magic_service._send_spell_completion_message.assert_awaited_once()
    magic_service._send_healing_update_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_spell_completion_message_success(magic_service: MagicService, player_id: uuid.UUID) -> None:
    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as send_event:
        await magic_service._send_spell_completion_message(
            player_id, "fire_bolt", {"success": True, "message": "It worked."}
        )
    send_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_start_delayed_cast_in_combat(
    magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell, target_match: TargetMatch
) -> None:
    delayed = base_spell.model_copy(update={"casting_time_seconds": 2})
    combat = MagicMock(combat_id=uuid.uuid4(), next_turn_tick=120, turn_interval_ticks=10)
    magic_service.combat_service = MagicMock()
    magic_service.combat_service.get_combat_by_participant = AsyncMock(return_value=combat)
    magic_service.casting_state_manager.start_casting = MagicMock()
    result = await magic_service._start_delayed_cast(player_id, delayed, target_match, 5, 100)
    assert result["success"] is True and "combat" in result["message"]


@pytest.mark.asyncio
async def test_start_delayed_cast_value_error(
    magic_service: MagicService, player_id: uuid.UUID, base_spell: Spell, target_match: TargetMatch
) -> None:
    delayed = base_spell.model_copy(update={"casting_time_seconds": 2})
    magic_service.casting_state_manager.start_casting = MagicMock(side_effect=ValueError("Already casting"))
    result = await magic_service._start_delayed_cast(player_id, delayed, target_match, 5, 100)
    assert result["success"] is False
