"""
Unit tests for server-side exit hallucination (#626, #714).

Golden values in test_get_hallucinated_exits_matches_js_reference were captured by running the
original client/src/utils/directionHallucination.ts implementation in Node and diffing against
this Python port -- see PR #714 description. Any change to this file's arithmetic that breaks
those values has broken the port's parity with the client-side original it replaces.
"""

from server.services.exit_hallucination import DIRECTION_POOL, get_hallucinated_exits, mulberry32, seed_from


def test_seed_from_matches_js_reference():
    """seed_from(room, player) must match the Node reference exactly (bit-for-bit port)."""
    assert seed_from("room_001", "player_001") == 2231525315
    assert seed_from("earth_arkhamcity_sanitarium_room_foyer_001", "b3e1c2a4-1234-5678-9abc-def012345678") == 3413891508
    assert seed_from("", "") == 5861881
    assert seed_from("x", "y") == 2090851242


def test_seed_from_order_matters():
    """Room and player aren't interchangeable in the seed -- different rooms, different lies."""
    assert seed_from("room_a", "player_1") != seed_from("player_1", "room_a")


def test_get_hallucinated_exits_matches_js_reference():
    """Golden values from the Node reference implementation -- see module docstring."""
    assert get_hallucinated_exits("room_001", "player_001") == ["south", "down", "east", "west", "up", "north"]
    assert get_hallucinated_exits(
        "earth_arkhamcity_sanitarium_room_foyer_001", "b3e1c2a4-1234-5678-9abc-def012345678"
    ) == ["south", "down", "up"]
    assert get_hallucinated_exits("", "") == ["west", "east", "down", "up"]
    assert get_hallucinated_exits("x", "y") == ["east", "west", "up", "north"]


def test_get_hallucinated_exits_is_stable_for_same_room_and_player():
    """Same (room, player) must yield the same lie every time -- stable across re-entry/re-render."""
    first = get_hallucinated_exits("room_stable", "player_stable")
    second = get_hallucinated_exits("room_stable", "player_stable")
    assert first == second


def test_get_hallucinated_exits_differs_by_player():
    """Different players in the same room see different lies."""
    exits_a = get_hallucinated_exits("shared_room", "player_a")
    exits_b = get_hallucinated_exits("shared_room", "player_b")
    assert exits_a != exits_b


def test_get_hallucinated_exits_only_uses_the_real_direction_pool():
    """The hallucinated set is a subset of the six real directions -- never invents a new one."""
    exits = get_hallucinated_exits("any_room", "any_player")
    assert exits
    assert set(exits).issubset(set(DIRECTION_POOL))
    assert len(exits) == len(set(exits))  # no duplicates


def test_mulberry32_yields_floats_in_unit_interval():
    """The PRNG's output must stay within [0, 1) -- a bug here would silently corrupt every seed."""
    rng = mulberry32(42)
    for _ in range(100):
        value = rng()
        assert 0.0 <= value < 1.0
