"""Unit tests for the death-room bookkeeping on the player aggregate (#910, ADR-029 step 6a)."""

import uuid

import pytest

from server.constants.spawn_defaults import LIMBO_ROOM_ID
from server.game.player_registry import PlayerAggregate
from server.services.player_respawn_state import (
    DEATH_LOCATION_STAT,
    DEATH_ROOM_ID_STAT,
    clear_death_room,
    record_death_room,
)
from server.tests.fixtures.shared.player_registry import aggregate, raw_row

ROOM_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


def _player(stats: dict[str, object]) -> PlayerAggregate:
    return aggregate(raw_row(uuid.uuid4(), stats={"current_dp": -10, "max_dp": 20, **stats}))


def test_records_room_id_but_never_writes_it_as_the_display_name():
    """The raw room ID must not land in death_location; login re-resolves the name from death_room_id."""
    player = _player({})

    record_death_room(player, ROOM_ID)

    assert player.row.stats[DEATH_ROOM_ID_STAT] == ROOM_ID
    assert DEATH_LOCATION_STAT not in player.row.stats
    assert player.row.sync_required  # it commits with the limbo move


def test_keeps_an_existing_display_name():
    player = _player({DEATH_LOCATION_STAT: "Arkham City › Sanitarium › Foyer"})

    record_death_room(player, ROOM_ID)

    assert player.row.stats[DEATH_ROOM_ID_STAT] == ROOM_ID
    assert player.row.stats[DEATH_LOCATION_STAT] == "Arkham City › Sanitarium › Foyer"


@pytest.mark.parametrize("death_location", ["", LIMBO_ROOM_ID, "catatonia_failover"])
def test_ignores_non_rooms(death_location: str):
    player = _player({})

    record_death_room(player, death_location)

    assert DEATH_ROOM_ID_STAT not in player.row.stats
    assert not player.row.dirty


def test_clear_removes_both_keys():
    player = _player({DEATH_ROOM_ID_STAT: ROOM_ID, DEATH_LOCATION_STAT: "Foyer"})

    clear_death_room(player)

    assert DEATH_ROOM_ID_STAT not in player.row.stats and DEATH_LOCATION_STAT not in player.row.stats
    assert player.row.sync_required
