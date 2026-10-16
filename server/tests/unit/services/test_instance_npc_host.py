"""Unit tests for PopulationInstanceNpcHost: instance NPCs spawned by definition name, cleared by room prefix."""

from unittest.mock import MagicMock

from server.services.instance_npc_host import INSTANCE_SPAWN_REASON, PopulationInstanceNpcHost

INSTANCE_PREFIX = "instance_e4857769-81a3-40dd-bf65-b1811a1904ee_"
ROOM_ID = f"{INSTANCE_PREFIX}earth_demo_zone_room_square_001"


def _definition(name: str) -> MagicMock:
    definition: MagicMock = MagicMock()
    definition.name = name
    return definition


def _host(
    definitions: dict[int, MagicMock],
    *,
    spawn_result: tuple[str | None, str | None] = ("npc-1", None),
    active_npcs: dict[str, MagicMock] | None = None,
) -> tuple[PopulationInstanceNpcHost, MagicMock, MagicMock]:
    spawn_npc: MagicMock = MagicMock(return_value=spawn_result)
    population: MagicMock = MagicMock()
    population.npc_definitions = definitions
    population.spawn_npc = spawn_npc
    despawn_npc: MagicMock = MagicMock(return_value=True)
    lifecycle: MagicMock = MagicMock()
    lifecycle.active_npcs = active_npcs or {}
    lifecycle.despawn_npc = despawn_npc
    return PopulationInstanceNpcHost(population, lifecycle), spawn_npc, despawn_npc


def test_spawn_finds_the_definition_by_name_and_spawns_it_as_an_instance_npc() -> None:
    lamplighter = _definition("Lamplighter")
    host, spawn_npc, _ = _host({1: _definition("Ghoul"), 2: lamplighter})

    assert host.spawn("Lamplighter", ROOM_ID) == "npc-1"

    spawn_npc.assert_called_once_with(lamplighter, ROOM_ID, INSTANCE_SPAWN_REASON)
    assert INSTANCE_SPAWN_REASON == "instance_spawn"


def test_spawn_of_an_unknown_name_spawns_nothing() -> None:
    host, spawn_npc, _ = _host({1: _definition("Ghoul")})

    assert host.spawn("Lamplighter", ROOM_ID) is None
    spawn_npc.assert_not_called()


def test_spawn_reports_a_refused_spawn_as_none() -> None:
    host, _, _ = _host({1: _definition("Ghoul")}, spawn_result=(None, "no lifecycle manager"))

    assert host.spawn("Ghoul", ROOM_ID) is None


def test_despawn_in_rooms_clears_only_npcs_inside_the_prefix() -> None:
    inside: MagicMock = MagicMock()
    inside.current_room = ROOM_ID
    elsewhere: MagicMock = MagicMock()
    elsewhere.current_room = "instance_other_earth_demo_zone_room_square_001"
    world: MagicMock = MagicMock()
    world.current_room = "earth_arkhamcity_sanitarium_room_foyer_001"
    host, _, despawn_npc = _host({}, active_npcs={"a": inside, "b": elsewhere, "c": world})

    assert host.despawn_in_rooms(INSTANCE_PREFIX) == 1

    despawn_npc.assert_called_once_with("a", "instance_teardown")
