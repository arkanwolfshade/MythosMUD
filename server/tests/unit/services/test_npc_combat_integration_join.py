"""Unit tests for joining an in-progress combat through NPCCombatIntegrationService (#833 slice 1)."""

# pyright: reportPrivateUsage=false
# Reason: _process_combat_attack and _complete_player_attack_on_npc_after_grace are the units under test.
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services.combat_types import AlreadyEngagedError, CombatParticipantData
from server.services.npc_combat_integration_service import NPCCombatIntegrationService


class _StubGameConfig:
    combat_tick_interval: int = 10


class _StubConfigRoot:
    game: _StubGameConfig = _StubGameConfig()


@pytest.fixture
def combat_service() -> MagicMock:
    service: MagicMock = MagicMock()
    service.auto_progression_enabled = False
    service.turn_interval_seconds = 10
    return service


@pytest.fixture
def integration_service(combat_service: MagicMock) -> NPCCombatIntegrationService:
    with patch("server.services.npc_combat_integration_service.get_config") as mock_config:
        mock_config.return_value = _StubConfigRoot()
        return NPCCombatIntegrationService(
            event_bus=None,
            combat_service=combat_service,
            player_combat_service=None,
            connection_manager=MagicMock(),
            async_persistence=MagicMock(),
        )


def _participant(name: str, ptype: CombatParticipantType, pid: uuid.UUID | None = None) -> CombatParticipant:
    return CombatParticipant(
        participant_id=pid or uuid.uuid4(),
        participant_type=ptype,
        name=name,
        current_dp=50,
        max_dp=100,
        dexterity=10,
    )


def _fight(npc: CombatParticipant, *players: CombatParticipant) -> CombatInstance:
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id="r1")
    for p in (*players, npc):
        combat.participants[p.participant_id] = p
    return combat


@pytest.mark.asyncio
async def test_attacking_an_npc_already_in_combat_joins_the_fight(
    integration_service: NPCCombatIntegrationService, combat_service: MagicMock
) -> None:
    """#833: the second player joins (no 'cannot attack right now'), queues an attack, room hears about it."""
    attacker_uuid, ghoul = uuid.uuid4(), _participant("Ghoul", CombatParticipantType.NPC)
    fight = _fight(ghoul, _participant("Ashcroft", CombatParticipantType.PLAYER))
    joiner_data = CombatParticipantData(
        participant_id=attacker_uuid,
        name="Blackwood",
        current_dp=40,
        max_dp=100,
        dexterity=12,
        participant_type=CombatParticipantType.PLAYER,
    )
    get_player_name: AsyncMock = AsyncMock(return_value="Blackwood")
    get_player_combat_data: AsyncMock = AsyncMock(return_value=joiner_data)
    broadcast: AsyncMock = AsyncMock()
    join_combat: AsyncMock = AsyncMock()
    queue_action: AsyncMock = AsyncMock(return_value=True)
    data_provider: MagicMock = MagicMock()
    data_provider.get_player_name = get_player_name
    data_provider.get_player_combat_data = get_player_combat_data
    messaging: MagicMock = MagicMock()
    messaging.broadcast_player_joined_combat = broadcast
    integration_service._data_provider = data_provider
    integration_service._messaging_integration = messaging
    # the attacker is not fighting; the target NPC is
    combat_service.get_combat_by_participant = AsyncMock(side_effect=[None, fight])
    combat_service.join_combat = join_combat
    combat_service.queue_combat_action = queue_action
    player_id = str(uuid.uuid4())

    with patch("server.services.npc_combat_integration_combat_mixin.get_current_tick", return_value=7):
        result = await integration_service._process_combat_attack(
            player_id, "r1", attacker_uuid, ghoul.participant_id, 6, MagicMock()
        )

    assert result.success is True
    assert result.damage == 0
    assert result.combat_id == fight.combat_id
    join_combat.assert_awaited_once_with(fight, joiner_data, "r1")
    queue_action.assert_awaited_once_with(
        combat_id=fight.combat_id,
        participant_id=attacker_uuid,
        action_type="attack",
        target_id=ghoul.participant_id,
        damage=6,
    )
    broadcast.assert_awaited_once_with("r1", str(fight.combat_id), "Blackwood", "Ghoul", player_id)


@pytest.mark.asyncio
async def test_engaged_player_cannot_queue_an_attack_on_a_foe_outside_their_fight(
    integration_service: NPCCombatIntegrationService, combat_service: MagicMock
) -> None:
    """One NPC per combat: queuing an attack on someone else's foe is refused, not silently queued."""
    attacker_uuid, other_foe = uuid.uuid4(), uuid.uuid4()
    own_fight = _fight(
        _participant("Ghoul", CombatParticipantType.NPC), _participant("Me", CombatParticipantType.PLAYER)
    )
    queue_action: AsyncMock = AsyncMock(return_value=True)
    combat_service.get_combat_by_participant = AsyncMock(return_value=own_fight)
    combat_service.queue_combat_action = queue_action

    with patch("server.services.npc_combat_integration_combat_mixin.get_current_tick", return_value=7):
        result = await integration_service._process_combat_attack(
            str(uuid.uuid4()), "r1", attacker_uuid, other_foe, 6, MagicMock()
        )

    assert result.success is False
    assert result.combat_id == own_fight.combat_id
    queue_action.assert_not_awaited()


@pytest.mark.asyncio
async def test_attack_on_another_foe_is_refused_before_first_engagement_side_effects(
    integration_service: NPCCombatIntegrationService, combat_service: MagicMock
) -> None:
    """#833: the refusal comes before attack memory / encounter lucidity fire for the wrong foe."""
    mapping = integration_service.get_uuid_mapping()
    player_id = str(uuid.uuid4())
    ghoul = _participant("Ghoul", CombatParticipantType.NPC, pid=mapping.convert_to_uuid("npc_ghoul"))
    me = _participant("Me", CombatParticipantType.PLAYER, pid=mapping.convert_to_uuid(player_id))
    combat_service.get_combat_by_participant = AsyncMock(return_value=_fight(ghoul, me))
    record_attack: MagicMock = MagicMock()
    memory: MagicMock = MagicMock()
    memory.record_attack = record_attack
    integration_service._combat_memory = memory
    integration_service._validate_and_get_npc_instance = AsyncMock(return_value=MagicMock())
    integration_service._validate_combat_location = AsyncMock(return_value=True)

    with pytest.raises(AlreadyEngagedError) as engaged:
        _ = await integration_service._complete_player_attack_on_npc_after_grace(
            player_id, "npc_cultist", "r1", "punch", 5, None
        )

    assert engaged.value.foe_name == "Ghoul"
    record_attack.assert_not_called()


@pytest.mark.asyncio
async def test_get_engaged_foe_name_reports_the_current_foe_only_for_other_targets(
    integration_service: NPCCombatIntegrationService, combat_service: MagicMock
) -> None:
    mapping = integration_service.get_uuid_mapping()
    player_id = str(uuid.uuid4())
    ghoul = _participant("Ghoul", CombatParticipantType.NPC, pid=mapping.convert_to_uuid("npc_ghoul"))
    me = _participant("Me", CombatParticipantType.PLAYER, pid=mapping.convert_to_uuid(player_id))
    combat_service.get_combat_by_participant = AsyncMock(return_value=_fight(ghoul, me))

    assert await integration_service.get_engaged_foe_name(player_id, "npc_cultist") == "Ghoul"
    assert await integration_service.get_engaged_foe_name(player_id, "npc_ghoul") is None


@pytest.mark.asyncio
async def test_get_engaged_foe_name_is_none_when_not_in_combat(
    integration_service: NPCCombatIntegrationService, combat_service: MagicMock
) -> None:
    combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    assert await integration_service.get_engaged_foe_name(str(uuid.uuid4()), "npc_ghoul") is None
