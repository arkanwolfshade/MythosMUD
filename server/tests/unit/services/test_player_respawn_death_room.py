"""Unit tests for PlayerRespawnService._record_death_room_on_player (#910)."""
# pyright: reportPrivateUsage=false
# #910: the helper is a private staticmethod reached only through move_player_to_limbo, which needs a
# full DB session; it is called directly here to pin the stat-writing contract.

from unittest.mock import MagicMock

import pytest

from server.constants.spawn_defaults import LIMBO_ROOM_ID
from server.models.player import Player
from server.services.player_respawn_service import (
    DEATH_LOCATION_STAT,
    DEATH_ROOM_ID_STAT,
    PlayerRespawnService,
)

ROOM_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


def _player_with_stats(stats: dict[str, object]) -> tuple[Player, MagicMock]:
    """Return a mock player plus a typed handle on its set_stats mock."""
    player = MagicMock(spec=Player)
    set_stats = MagicMock()
    player.get_stats = MagicMock(return_value=stats)
    player.set_stats = set_stats
    return player, set_stats


def test_records_room_id_but_never_writes_it_as_the_display_name():
    """The raw room ID must not land in death_location; login re-resolves the name from death_room_id."""
    stats: dict[str, object] = {}
    player, set_stats = _player_with_stats(stats)

    PlayerRespawnService._record_death_room_on_player(player, ROOM_ID)

    assert stats[DEATH_ROOM_ID_STAT] == ROOM_ID
    assert DEATH_LOCATION_STAT not in stats
    set_stats.assert_called_once_with(stats)


def test_keeps_an_existing_display_name():
    stats: dict[str, object] = {DEATH_LOCATION_STAT: "Arkham City › Sanitarium › Foyer"}
    player, set_stats = _player_with_stats(stats)

    PlayerRespawnService._record_death_room_on_player(player, ROOM_ID)

    assert stats[DEATH_ROOM_ID_STAT] == ROOM_ID
    assert stats[DEATH_LOCATION_STAT] == "Arkham City › Sanitarium › Foyer"
    set_stats.assert_called_once_with(stats)


@pytest.mark.parametrize("death_location", ["", LIMBO_ROOM_ID, "catatonia_failover"])
def test_ignores_non_rooms(death_location: str):
    player, set_stats = _player_with_stats({})

    PlayerRespawnService._record_death_room_on_player(player, death_location)

    set_stats.assert_not_called()
