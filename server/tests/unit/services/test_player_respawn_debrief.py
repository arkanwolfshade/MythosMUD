"""Respawn after delirium or sanitarium failover leaves a pending debrief for the player to spend (ADR-028).

The respawn is one registry unit (ADR-029 step 6a): the room, the lucidity and the pending debrief commit together.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta

import pytest

from server.constants.spawn_defaults import DEFAULT_RESPAWN_ROOM, RECOVERY_WARD_ROOM_ID
from server.game.player_registry import LucidityData
from server.models.lucidity import LucidityActionCode
from server.services.player_respawn_service import PlayerRespawnService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PLAYER_ID = uuid.uuid4()


@pytest.fixture(name="harness")
def _harness() -> LucidityHarness:
    return lucidity_registry(
        {PLAYER_ID: LucidityData(-10, "catatonic")},
        stats={"current_dp": 1, "max_dp": 100, "position": "lying"},
        row={"current_room_id": "somewhere_in_the_tutorial"},
    )


def _debrief_pending_until(harness: LucidityHarness) -> datetime | None:
    return harness.cooldowns(PLAYER_ID).expires_at(LucidityActionCode.DEBRIEF_PENDING)


async def _to_sanitarium_lcd(harness: LucidityHarness) -> None:
    async with harness.registry.mutate(PLAYER_ID) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
        _ = player.lucidity.set(lcd=-100)


@pytest.mark.asyncio
async def test_a_delirium_respawn_leaves_a_pending_debrief_in_the_same_commit(harness: LucidityHarness) -> None:
    respawned = await PlayerRespawnService(player_registry=harness.registry).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is True
    expires_at = _debrief_pending_until(harness)
    assert expires_at is not None
    assert expires_at > datetime.now(UTC) + timedelta(days=300)  # a long-lived flag, cleared by the debrief itself
    assert harness.db.commits == 1  # room, lucidity and debrief: one unit


@pytest.mark.asyncio
async def test_a_sanitarium_respawn_still_leaves_a_pending_debrief(harness: LucidityHarness) -> None:
    await _to_sanitarium_lcd(harness)

    respawned = await PlayerRespawnService(player_registry=harness.registry).respawn_player_from_sanitarium(PLAYER_ID)

    assert respawned is True
    assert _debrief_pending_until(harness) is not None


@pytest.mark.asyncio
async def test_a_delirium_respawn_wakes_the_player_in_the_recovery_ward(harness: LucidityHarness) -> None:
    respawned = await PlayerRespawnService(player_registry=harness.registry).respawn_player_from_delirium(PLAYER_ID)

    assert respawned is True
    assert harness.room(PLAYER_ID) == RECOVERY_WARD_ROOM_ID


@pytest.mark.asyncio
async def test_a_sanitarium_respawn_wakes_the_player_in_the_recovery_ward(harness: LucidityHarness) -> None:
    await _to_sanitarium_lcd(harness)

    respawned = await PlayerRespawnService(player_registry=harness.registry).respawn_player_from_sanitarium(PLAYER_ID)

    assert respawned is True
    assert harness.room(PLAYER_ID) == RECOVERY_WARD_ROOM_ID


def test_death_still_respawns_at_the_main_foyer_not_the_ward() -> None:
    assert DEFAULT_RESPAWN_ROOM != RECOVERY_WARD_ROOM_ID
    assert DEFAULT_RESPAWN_ROOM.endswith("foyer_001")
