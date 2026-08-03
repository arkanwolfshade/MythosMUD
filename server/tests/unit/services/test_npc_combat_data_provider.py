"""Unit tests for server.services.npc_combat_data_provider."""

from __future__ import annotations

import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatParticipantType
from server.services.npc_combat_data_provider import NPCCombatDataProvider


@pytest.fixture
def persistence() -> MagicMock:
    return MagicMock()


def test_get_npc_instance_from_lifecycle(persistence: MagicMock) -> None:
    npc = SimpleNamespace(name="Rat")
    lifecycle = MagicMock()
    lifecycle.active_npcs = {"npc-1": npc}
    svc = MagicMock(lifecycle_manager=lifecycle)
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=svc):
        provider = NPCCombatDataProvider(persistence)
        assert provider.get_npc_instance("npc-1") is npc


def test_get_npc_instance_returns_none_on_error(persistence: MagicMock) -> None:
    with patch(
        "server.services.npc_instance_service.get_npc_instance_service",
        side_effect=ImportError("missing"),
    ):
        provider = NPCCombatDataProvider(persistence)
        assert provider.get_npc_instance("npc-1") is None


@pytest.mark.asyncio
async def test_get_npc_definition_from_persistence(persistence: MagicMock) -> None:
    definition = SimpleNamespace(name="Goblin")
    record = SimpleNamespace(definition=definition)
    lifecycle = MagicMock()
    lifecycle.lifecycle_records = {"npc-1": record}
    persistence.get_npc_lifecycle_manager = MagicMock(return_value=lifecycle)
    provider = NPCCombatDataProvider(persistence)
    result = await provider.get_npc_definition("npc-1")
    assert result is definition


@pytest.mark.asyncio
async def test_get_player_name_found(persistence: MagicMock) -> None:
    player_id = uuid.uuid4()
    player = MagicMock()
    player.name = "Arkan"
    persistence.get_player_by_id = AsyncMock(return_value=player)
    provider = NPCCombatDataProvider(persistence)
    assert await provider.get_player_name(str(player_id)) == "Arkan"


@pytest.mark.asyncio
async def test_get_player_name_unknown(persistence: MagicMock) -> None:
    persistence.get_player_by_id = AsyncMock(return_value=None)
    provider = NPCCombatDataProvider(persistence)
    assert await provider.get_player_name(str(uuid.uuid4())) == "Unknown Player"


@pytest.mark.asyncio
async def test_get_player_room_id_invalid_uuid(persistence: MagicMock) -> None:
    provider = NPCCombatDataProvider(persistence)
    assert await provider.get_player_room_id("not-a-uuid") is None


@pytest.mark.asyncio
async def test_get_player_room_id_found(persistence: MagicMock) -> None:
    player_id = uuid.uuid4()
    player = MagicMock(current_room_id="room_001")
    persistence.get_player_by_id = AsyncMock(return_value=player)
    provider = NPCCombatDataProvider(persistence)
    assert await provider.get_player_room_id(str(player_id)) == "room_001"


@pytest.mark.asyncio
async def test_get_player_combat_data(persistence: MagicMock) -> None:
    player_id = uuid.uuid4()
    player = MagicMock()
    player.get_combat_stats.return_value = {
        "current_dp": 80,
        "max_dp": 100,
        "dexterity": 12,
    }
    persistence.get_player_by_id = AsyncMock(return_value=player)
    provider = NPCCombatDataProvider(persistence)
    data = await provider.get_player_combat_data(str(player_id), uuid.uuid4(), "Hero")
    assert data.current_dp == 80
    assert data.participant_type == CombatParticipantType.PLAYER


@pytest.mark.asyncio
async def test_get_player_combat_data_missing_player(persistence: MagicMock) -> None:
    persistence.get_player_by_id = AsyncMock(return_value=None)
    provider = NPCCombatDataProvider(persistence)
    with pytest.raises(ValueError, match="not found"):
        await provider.get_player_combat_data(str(uuid.uuid4()), uuid.uuid4(), "Hero")


def test_get_npc_combat_data_with_get_combat_stats(persistence: MagicMock) -> None:
    npc = MagicMock()
    npc.name = "Shoggoth"
    npc.npc_type = "mob"
    npc.get_combat_stats.return_value = {"current_dp": 50, "max_dp": 50, "dexterity": 8}
    provider = NPCCombatDataProvider(persistence)
    data = provider.get_npc_combat_data(npc, uuid.uuid4())
    assert data.name == "Shoggoth"
    assert data.participant_type == CombatParticipantType.NPC


def test_get_npc_combat_data_fallback_stats(persistence: MagicMock) -> None:
    npc = MagicMock(spec=["name", "get_stats", "id"])
    npc.name = "Cultist"
    npc.id = "c1"
    npc.get_stats.return_value = {"determination_points": 30, "max_dp": 40, "dexterity": 11}
    provider = NPCCombatDataProvider(persistence)
    data = provider.get_npc_combat_data(npc, uuid.uuid4())
    assert data.current_dp == 30
    assert data.max_dp == 40
