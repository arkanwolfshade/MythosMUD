"""
Regression tests for #918: NPCs never idle-wander while in combat.

Uses a real CombatService and NPCCombatUUIDMapping (no hand-set private dicts) with a realistic
string NPC id, and drives every wander entry point: IdleMovementHandler, NPCThreadManager and
PassiveMobNPC.
"""

# pyright: reportPrivateUsage=false
# Reason: white-box tests reach NPCThreadManager._process_wander_action and PassiveMobNPC internals.

from __future__ import annotations

import uuid
from collections.abc import Iterator
from dataclasses import dataclass
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.npc.idle_movement import IdleMovementHandler
from server.npc.movement_integration import NPCMovementIntegration, is_npc_in_combat
from server.npc.passive_mob_npc import PassiveMobNPC
from server.npc.threading import NPCThreadManager
from server.services.combat_service import CombatService, set_combat_service
from server.services.npc_combat_uuid_mapping import NPCCombatUUIDMapping

NPC_ID = "cultist_of_the_yellow_sign_earth_arkhamcity_downtown_1790694401_1691"
ROOM_A = "earth_arkhamcity_downtown_room_a"
ROOM_B = "earth_arkhamcity_downtown_room_b"
CONFIG: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}


@dataclass
class Fight:
    """A real CombatService with one NPC-vs-player combat registered."""

    service: CombatService
    combat: CombatInstance


def _participant(kind: CombatParticipantType, participant_id: uuid.UUID, name: str) -> CombatParticipant:
    return CombatParticipant(
        participant_id=participant_id,
        participant_type=kind,
        name=name,
        current_dp=10,
        max_dp=20,
        dexterity=10,
    )


@pytest.fixture(name="service")
def service_fixture() -> Iterator[CombatService]:
    """Real CombatService wired to a real UUID mapping, installed as the global combat service."""
    integration = MagicMock()
    integration._uuid_mapping = NPCCombatUUIDMapping()
    config = SimpleNamespace(game=SimpleNamespace(combat_tick_interval=10))
    with (
        patch("server.services.combat_service.get_config", return_value=config),
        patch("server.services.combat_service.CombatEventPublisher"),
    ):
        svc = CombatService(
            player_combat_service=MagicMock(track_player_combat_state=AsyncMock()),
            nats_service=None,
            npc_combat_integration_service=integration,
        )
        set_combat_service(svc)
        try:
            yield svc
        finally:
            set_combat_service(None)


async def _start_fight(service: CombatService) -> Fight:
    """Register an NPC-initiated fight the way NPCCombatIntegrationService does (string id -> UUID mapping)."""
    integration = service.get_npc_combat_integration_service()
    assert integration is not None
    mapping = integration._uuid_mapping
    npc_uuid = mapping.convert_to_uuid(NPC_ID)
    mapping.store_string_id_mapping(npc_uuid, NPC_ID)
    npc = _participant(CombatParticipantType.NPC, npc_uuid, "Cultist")
    player = _participant(CombatParticipantType.PLAYER, uuid.uuid4(), "Player")
    combat = CombatInstance(
        combat_id=uuid.uuid4(),
        room_id=ROOM_A,
        participants={npc.participant_id: npc, player.participant_id: player},
    )
    await service.register_combat_state(combat, ROOM_A)
    return Fight(service=service, combat=combat)


@pytest.fixture(name="move_spy")
def move_spy_fixture() -> Iterator[MagicMock]:
    """One valid exit and a spy on the actual room move; also pins random so probability always passes."""
    with (
        patch("server.npc.idle_movement.random.random", return_value=0.0),
        patch.object(IdleMovementHandler, "get_valid_exits", return_value={"north": ROOM_B}),
        patch.object(NPCMovementIntegration, "move_npc_to_room", return_value=True) as move,
        patch("server.container.ApplicationContainer.get_instance", return_value=MagicMock()),
    ):
        yield move


def _npc_instance() -> MagicMock:
    npc = MagicMock()
    npc.npc_id = NPC_ID
    npc.current_room = ROOM_A
    npc.is_alive = True
    npc.is_active = True
    npc._behavior_config = dict(CONFIG)
    return npc


@pytest.mark.asyncio
async def test_string_id_resolves_to_combat_through_uuid_mapping(service: CombatService) -> None:
    """A realistic string NPC id is found via the public is_npc_in_combat_sync path."""
    assert service.is_npc_in_combat_sync(NPC_ID) is False
    _ = await _start_fight(service)
    assert service.is_npc_in_combat_sync(NPC_ID) is True


@pytest.mark.asyncio
async def test_execute_idle_movement_blocked_then_resumes_after_combat(
    service: CombatService, move_spy: MagicMock
) -> None:
    """No wander while in combat; wander works again once combat tracking is cleaned up."""
    fight = await _start_fight(service)
    handler = IdleMovementHandler(persistence=MagicMock())
    npc = _npc_instance()

    assert handler.execute_idle_movement(npc, MagicMock(), CONFIG) is False
    move_spy.assert_not_called()

    service.cleanup_combat_tracking(fight.combat)

    assert handler.execute_idle_movement(npc, MagicMock(), CONFIG) is True
    move_spy.assert_called_once_with(NPC_ID, ROOM_A, ROOM_B)


@pytest.mark.asyncio
async def test_process_wander_action_blocked_in_combat(service: CombatService, move_spy: MagicMock) -> None:
    """NPCThreadManager's WANDER action does not move an NPC that is in combat."""
    _ = await _start_fight(service)
    manager = NPCThreadManager()
    with patch.object(manager, "_resolve_wander_npc", return_value=(_npc_instance(), MagicMock())):
        await manager._process_wander_action(NPC_ID, {})
    move_spy.assert_not_called()


@pytest.mark.asyncio
async def test_passive_mob_wander_blocked_in_combat(service: CombatService, move_spy: MagicMock) -> None:
    """PassiveMobNPC.wander does not move the NPC while in combat."""
    _ = await _start_fight(service)
    npc = PassiveMobNPC(definition=SimpleNamespace(name="Cultist", npc_type="passive_mob"), npc_id=NPC_ID)
    npc._behavior_config = dict(CONFIG)
    npc.current_room = ROOM_A

    assert npc.wander() is False
    move_spy.assert_not_called()
    assert npc.current_room == ROOM_A


def test_is_npc_in_combat_fails_closed_on_lookup_error() -> None:
    """An exception during the combat lookup counts as in combat (#918)."""
    broken = MagicMock(is_npc_in_combat_sync=MagicMock(side_effect=RuntimeError("combat service hiccup")))
    with patch("server.services.combat_service.get_combat_service", return_value=broken):
        assert is_npc_in_combat(NPC_ID) is True


def test_is_npc_in_combat_false_without_combat_service() -> None:
    """With no combat service registered there can be no combat."""
    with patch("server.services.combat_service.get_combat_service", return_value=None):
        assert is_npc_in_combat(NPC_ID) is False
