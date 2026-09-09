"""
Unit tests for shared per-viewer phantom visibility (#625, #714).

Moved from test_look_room.py when `_get_viewer_phantom_names` was promoted out of
`look_room.py` into `server.services.phantom_visibility` so realtime room payloads and
`game_state` could reuse the same viewer-scoping logic.
"""

from unittest.mock import patch

from server.services.phantom_visibility import get_viewer_phantom_names, room_has_hallucinating_viewer


def test_get_viewer_phantom_names_no_viewer_or_room():
    """#625: no phantom names without both a viewer id and a room id."""
    assert get_viewer_phantom_names(None, "room_1") == []
    assert get_viewer_phantom_names("player-1", None) == []


def test_get_viewer_phantom_names_matches_own_room():
    """#625: only the viewer's own active phantoms in this room are returned."""
    with (
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_active_phantoms",
            return_value=["phantom_1"],
        ),
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_phantom_data",
            return_value={"phantom_id": "phantom_1", "room_id": "room_1", "name": "Shambling Horror"},
        ),
    ):
        assert get_viewer_phantom_names("player-1", "room_1") == ["Shambling Horror"]


def test_room_has_hallucinating_viewer_false_when_no_phantoms_or_deranged():
    """#714: the fast-path gate is False when nobody has an active phantom or is deranged."""
    with (
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_active_phantoms",
            return_value=[],
        ),
        patch(
            "server.services.lucidity_tier_cache.lucidity_tier_cache.is_deranged",
            return_value=False,
        ),
    ):
        assert room_has_hallucinating_viewer(["player-1", "player-2"]) is False


def test_room_has_hallucinating_viewer_true_when_any_player_has_phantoms():
    """#714: True as soon as one player in the room has an active phantom."""

    def fake_active_phantoms(player_id: object) -> list[str]:
        return ["phantom_1"] if player_id == "player-2" else []

    with (
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_active_phantoms",
            side_effect=fake_active_phantoms,
        ),
        patch(
            "server.services.lucidity_tier_cache.lucidity_tier_cache.is_deranged",
            return_value=False,
        ),
    ):
        assert room_has_hallucinating_viewer(["player-1", "player-2"]) is True


def test_room_has_hallucinating_viewer_true_when_any_player_is_deranged():
    """#714/#626: True as soon as one player is cached as deranged, even with no phantom."""

    def fake_is_deranged(player_id: object) -> bool:
        return player_id == "player-2"

    with (
        patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.get_active_phantoms",
            return_value=[],
        ),
        patch(
            "server.services.lucidity_tier_cache.lucidity_tier_cache.is_deranged",
            side_effect=fake_is_deranged,
        ),
    ):
        assert room_has_hallucinating_viewer(["player-1", "player-2"]) is True
