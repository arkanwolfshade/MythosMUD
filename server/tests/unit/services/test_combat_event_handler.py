"""Unit tests for CombatEventHandler."""

import datetime
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.combat import CombatParticipant, CombatParticipantType
from server.services.combat_event_handler import CombatEventHandler


def _participant(name: str, ptype: CombatParticipantType) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        name=name,
        participant_type=ptype,
        current_dp=50,
        max_dp=100,
        dexterity=50,
    )


def test_resolve_participant_display_name_player() -> None:
    handler = CombatEventHandler(MagicMock())
    p = _participant("Alice", CombatParticipantType.PLAYER)
    assert handler._resolve_participant_display_name(p) == "Alice"


def test_resolve_participant_display_name_npc_fallback() -> None:
    combat_service = MagicMock(_npc_combat_integration_service=None)
    handler = CombatEventHandler(combat_service)
    p = _participant("Mob", CombatParticipantType.NPC)
    assert handler._resolve_participant_display_name(p) == "Mob"


def test_resolve_participant_display_name_npc_from_lifecycle() -> None:
    npc_instance = MagicMock()
    npc_instance.name = "Dr. Morgan"
    data_provider = MagicMock()
    data_provider.get_npc_instance.return_value = npc_instance
    uuid_mapping = MagicMock()
    uuid_mapping.get_original_string_id.return_value = "npc-string-1"
    integration = MagicMock(_uuid_mapping=uuid_mapping, _data_provider=data_provider)
    handler = CombatEventHandler(MagicMock(_npc_combat_integration_service=integration))
    p = _participant("Stale Name", CombatParticipantType.NPC)
    assert handler._resolve_participant_display_name(p) == "Dr. Morgan"


@pytest.mark.asyncio
async def test_publish_attack_events_no_publisher() -> None:
    handler = CombatEventHandler(MagicMock(_combat_event_publisher=None))
    combat = MagicMock()
    await handler._publish_attack_events(
        _participant("A", CombatParticipantType.PLAYER), _participant("B", CombatParticipantType.NPC), 5, combat
    )


@pytest.mark.asyncio
async def test_handle_attack_events_and_xp_npc_death() -> None:
    publisher = MagicMock()
    publisher.publish_npc_attacked = AsyncMock()
    publisher.publish_npc_took_damage = AsyncMock()
    death_handler = MagicMock()
    death_handler.handle_npc_death = AsyncMock()
    player_combat = MagicMock()
    player_combat.calculate_xp_reward = AsyncMock(return_value=50)
    combat_service = MagicMock(
        _combat_event_publisher=publisher,
        _death_handler=death_handler,
        _player_combat_service=player_combat,
    )
    handler = CombatEventHandler(combat_service)
    player = _participant("Hero", CombatParticipantType.PLAYER)
    npc = _participant("Mob", CombatParticipantType.NPC)
    combat = MagicMock(room_id="room-a", combat_id=uuid.uuid4())
    xp = await handler.handle_attack_events_and_xp(player, npc, 10, combat, True, npc.participant_id)
    assert xp == 50
    death_handler.handle_npc_death.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_attack_events_player_target() -> None:
    publisher = MagicMock()
    publisher.publish_player_attacked = AsyncMock()
    combat_service = MagicMock(_combat_event_publisher=publisher)
    handler = CombatEventHandler(combat_service)
    attacker = _participant("Mob", CombatParticipantType.NPC)
    target = _participant("Victim", CombatParticipantType.PLAYER)
    combat = MagicMock(room_id="room-a", combat_id=uuid.uuid4())
    await handler._publish_attack_events(attacker, target, 10, combat)
    publisher.publish_player_attacked.assert_awaited_once()


@pytest.mark.asyncio
async def test_calculate_xp_reward_default() -> None:
    handler = CombatEventHandler(MagicMock(_player_combat_service=None))
    assert await handler._calculate_xp_reward(uuid.uuid4()) == 0


@pytest.mark.asyncio
async def test_award_xp_to_player() -> None:
    player_combat = MagicMock()
    player_combat.award_xp_on_npc_death = AsyncMock()
    handler = CombatEventHandler(MagicMock(_player_combat_service=player_combat))
    player = _participant("Hero", CombatParticipantType.PLAYER)
    npc = _participant("Mob", CombatParticipantType.NPC)
    await handler.award_xp_to_player(player, npc, npc.participant_id, 25)
    player_combat.award_xp_on_npc_death.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_combat_ended_event() -> None:
    publisher = MagicMock()
    publisher.publish_combat_ended = AsyncMock()
    combat = MagicMock(combat_id=uuid.uuid4(), room_id="room-a", start_time=datetime.datetime.now())
    combat.participants = {}
    handler = CombatEventHandler(MagicMock(_combat_event_publisher=publisher))
    await handler.publish_combat_ended_event(combat, "victory")
    publisher.publish_combat_ended.assert_awaited_once()
