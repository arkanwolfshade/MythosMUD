"""Unit tests for utility threat (#833): buffs and debuffs let support pull, plus the queued-spell target fix."""

# pyright: reportPrivateUsage=false
# Reason: CombatTurnProcessor._build_spell_target is the unit under test for the queued-spell target type.

from __future__ import annotations

import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.config.models.game import GameConfig
from server.game.magic.spell_effects import SpellEffects, SpellEffectsDeps
from server.game.magic.spell_effects_threat import add_utility_threat_for_spell
from server.models.combat import CombatAction, CombatInstance, CombatParticipant, CombatParticipantType
from server.models.spell import SpellEffectType
from server.schemas.shared import TargetMatch, TargetType
from server.services import aggro_threat
from server.services.combat_turn_processor import CombatTurnProcessor

PLAYER = CombatParticipantType.PLAYER
NPC = CombatParticipantType.NPC


def _p(
    name: str,
    ptype: CombatParticipantType = PLAYER,
    npc_type: str | None = None,
    aggression_level: int | None = None,
) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=ptype,
        name=name,
        current_dp=50,
        max_dp=100,
        dexterity=10,
        npc_type=npc_type,
        aggression_level=aggression_level,
    )


def _combat(*participants: CombatParticipant) -> CombatInstance:
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id="r1")
    for p in participants:
        combat.participants[p.participant_id] = p
    return combat


def _hate(combat: CombatInstance, npc: CombatParticipant) -> dict[uuid.UUID, float]:
    return combat.npc_hate_lists.get(npc.participant_id, {})


# --- add_utility_threat ---------------------------------------------------------------------------------------


def test_default_utility_threat_comes_from_config() -> None:
    ghoul, support = _p("Ghoul", NPC), _p("Support")
    combat = _combat(ghoul, support)
    fake_config = SimpleNamespace(game=SimpleNamespace(aggro_utility_threat=7.0))

    with patch("server.services.aggro_threat.get_config", return_value=fake_config):
        aggro_threat.add_utility_threat(combat, ghoul.participant_id, support.participant_id)

    assert _hate(combat, ghoul) == {support.participant_id: 7.0}


def test_the_configured_default_is_five() -> None:
    assert GameConfig().aggro_utility_threat == 5.0


def test_utility_threat_accumulates() -> None:
    ghoul, support = _p("Ghoul", NPC), _p("Support")
    combat = _combat(ghoul, support)

    aggro_threat.add_utility_threat(combat, ghoul.participant_id, support.participant_id, 5.0)
    aggro_threat.add_utility_threat(combat, ghoul.participant_id, support.participant_id, 5.0)

    assert _hate(combat, ghoul)[support.participant_id] == pytest.approx(10.0)


@pytest.mark.parametrize(("level", "scale"), [(None, 1.0), (0, 0.5), (4, 0.7), (10, 1.0)])
def test_utility_threat_is_scaled_by_the_npcs_aggression_level(level: int | None, scale: float) -> None:
    ghoul, support = _p("Ghoul", NPC, aggression_level=level), _p("Support")
    combat = _combat(ghoul, support)

    aggro_threat.add_utility_threat(combat, ghoul.participant_id, support.participant_id, 10.0, npc_participant=ghoul)

    assert _hate(combat, ghoul)[support.participant_id] == pytest.approx(10.0 * scale)


def test_passive_mobs_still_take_utility_threat_but_not_damage_threat() -> None:
    """Magic worked near a passive creature can draw it; plain violence cannot."""
    mob, caster = _p("Mouse", NPC, npc_type="passive_mob"), _p("Caster")
    combat = _combat(mob, caster)

    aggro_threat.add_damage_threat(combat, mob.participant_id, caster.participant_id, 50.0, npc_participant=mob)
    assert _hate(combat, mob) == {}

    aggro_threat.add_utility_threat(combat, mob.participant_id, caster.participant_id, 5.0, npc_participant=mob)
    assert _hate(combat, mob)[caster.participant_id] == pytest.approx(5.0)


@pytest.mark.parametrize("amount", [0.0, -3.0])
def test_non_positive_utility_threat_is_ignored(amount: float) -> None:
    ghoul, support = _p("Ghoul", NPC), _p("Support")
    combat = _combat(ghoul, support)

    aggro_threat.add_utility_threat(combat, ghoul.participant_id, support.participant_id, amount)

    assert _hate(combat, ghoul) == {}


# --- which NPCs a spell draws ---------------------------------------------------------------------------------


def _service_for(combat: CombatInstance | None, caster: CombatParticipant) -> MagicMock:
    service: MagicMock = MagicMock()
    service.get_combat_id_for_participant = MagicMock(return_value=None if combat is None else combat.combat_id)
    service.get_combat = MagicMock(return_value=combat)
    _ = caster
    return service


def _target(participant: CombatParticipant, ttype: TargetType) -> TargetMatch:
    return TargetMatch(
        target_id=str(participant.participant_id), target_name=participant.name, target_type=ttype, room_id="r1"
    )


def test_a_debuff_on_one_npc_draws_only_that_npc() -> None:
    ghoul, cultist, support = _p("Ghoul", NPC), _p("Cultist", NPC), _p("Support")
    combat = _combat(ghoul, cultist, support)

    add_utility_threat_for_spell(_service_for(combat, support), support.participant_id, _target(ghoul, TargetType.NPC))

    assert _hate(combat, ghoul)[support.participant_id] == pytest.approx(5.0)
    assert _hate(combat, cultist) == {}


@pytest.mark.parametrize("who", ["ally", "self"])
def test_a_buff_on_an_ally_or_self_draws_every_npc_in_the_fight(who: str) -> None:
    ghoul, cultist, support, ally = _p("Ghoul", NPC), _p("Cultist", NPC), _p("Support"), _p("Ally")
    combat = _combat(ghoul, cultist, support, ally)
    buffed = ally if who == "ally" else support

    add_utility_threat_for_spell(
        _service_for(combat, support), support.participant_id, _target(buffed, TargetType.PLAYER)
    )

    assert _hate(combat, ghoul)[support.participant_id] == pytest.approx(5.0)
    assert _hate(combat, cultist)[support.participant_id] == pytest.approx(5.0)
    assert ally.participant_id not in _hate(combat, ghoul)


def test_nothing_is_added_outside_combat_or_without_a_service() -> None:
    ghoul, support = _p("Ghoul", NPC), _p("Support")
    combat = _combat(ghoul, support)

    add_utility_threat_for_spell(_service_for(None, support), support.participant_id, _target(ghoul, TargetType.NPC))
    add_utility_threat_for_spell(None, support.participant_id, _target(ghoul, TargetType.NPC))

    assert _hate(combat, ghoul) == {}


@pytest.mark.parametrize("ttype", [TargetType.ROOM, TargetType.PHANTOM])
def test_a_target_that_is_not_a_player_or_npc_adds_nothing(ttype: TargetType) -> None:
    """Area effects and hallucinated phantoms (visible to one player only) draw no real NPC."""
    ghoul, support = _p("Ghoul", NPC), _p("Support")
    combat = _combat(ghoul, support)
    other = TargetMatch(target_id="r1", target_name="elsewhere", target_type=ttype, room_id="r1")

    add_utility_threat_for_spell(_service_for(combat, support), support.participant_id, other)

    assert _hate(combat, ghoul) == {}


def test_an_npc_target_outside_the_casters_fight_adds_nothing() -> None:
    ghoul, support = _p("Ghoul", NPC), _p("Support")
    stranger = _p("Stranger", NPC)  # not in this combat
    combat = _combat(ghoul, support)

    add_utility_threat_for_spell(
        _service_for(combat, support), support.participant_id, _target(stranger, TargetType.NPC)
    )

    assert _hate(combat, ghoul) == {}


# --- the hook on SpellEffects.process_effect ------------------------------------------------------------------


def _effects(combat_service: MagicMock) -> SpellEffects:
    return SpellEffects(
        MagicMock(), SpellEffectsDeps(player_spell_repository=MagicMock(), combat_service=combat_service)
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("effect_type", "result", "draws"),
    [
        (SpellEffectType.STATUS_EFFECT, {"success": True}, True),
        (SpellEffectType.STAT_MODIFY, {"success": True}, True),
        (SpellEffectType.STATUS_EFFECT, {"success": False}, False),
        (SpellEffectType.DAMAGE, {"success": True}, False),  # damage and healing have their own threat paths
        (SpellEffectType.HEAL, {"success": True}, False),
    ],
)
async def test_process_effect_adds_utility_threat_only_for_successful_buffs_and_debuffs(
    effect_type: SpellEffectType, result: dict[str, object], draws: bool
) -> None:
    ghoul, support = _p("Ghoul", NPC), _p("Support")
    combat = _combat(ghoul, support)
    spell: MagicMock = MagicMock()
    spell.effect_type = effect_type
    spell.spell_id = "curse"
    effects = _effects(_service_for(combat, support))

    with patch.object(SpellEffects, "_dispatch_effect", new=AsyncMock(return_value=result)):
        returned = await effects.process_effect(spell, _target(ghoul, TargetType.NPC), support.participant_id)

    assert returned == result
    assert (support.participant_id in _hate(combat, ghoul)) is draws


# --- queued-spell target type ---------------------------------------------------------------------------------


def _spell_action(target_id: uuid.UUID, caster: CombatParticipant) -> CombatAction:
    return CombatAction(attacker_id=caster.participant_id, target_id=target_id, action_type="spell", spell_name="bolt")


def test_a_spell_queued_without_a_target_is_aimed_at_the_caster() -> None:
    """queue_combat_action stores the nil UUID when there is no target; that is truthy but means 'the caster'."""
    caster = _p("Caster")
    combat = _combat(caster)

    target = CombatTurnProcessor(MagicMock())._build_spell_target(
        _spell_action(uuid.UUID(int=0), caster), caster, "r1", combat
    )

    assert target.target_type == TargetType.PLAYER
    assert target.target_id == str(caster.participant_id)


def test_a_spell_aimed_at_an_ally_is_a_player_target() -> None:
    caster, ally = _p("Caster"), _p("Ally")
    combat = _combat(caster, ally)

    target = CombatTurnProcessor(MagicMock())._build_spell_target(
        _spell_action(ally.participant_id, caster), caster, "r1", combat
    )

    assert target.target_type == TargetType.PLAYER
    assert target.target_id == str(ally.participant_id)


def test_a_spell_aimed_at_an_npc_is_an_npc_target() -> None:
    caster, ghoul = _p("Caster"), _p("Ghoul", NPC)
    combat = _combat(caster, ghoul)

    target = CombatTurnProcessor(MagicMock())._build_spell_target(
        _spell_action(ghoul.participant_id, caster), caster, "r1", combat
    )

    assert target.target_type == TargetType.NPC
    assert target.target_id == str(ghoul.participant_id)


def test_a_spell_aimed_at_someone_no_longer_in_the_fight_keeps_the_old_npc_behaviour() -> None:
    caster = _p("Caster")
    gone = uuid.uuid4()

    target = CombatTurnProcessor(MagicMock())._build_spell_target(
        _spell_action(gone, caster), caster, "r1", _combat(caster)
    )

    assert target.target_type == TargetType.NPC
    assert target.target_id == str(gone)
