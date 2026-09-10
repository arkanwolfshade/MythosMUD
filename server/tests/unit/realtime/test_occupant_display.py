"""
Unit tests for shared occupant display name formatting.

Tests format_occupant_display_name() and its corruption badge (#815) -- the single chokepoint
for per-player adornment visible to OTHER players (room "Also here:" line and Occupants panel).
"""

import uuid
from unittest.mock import MagicMock, patch

from server.models.corruption import CorruptionTier
from server.realtime.occupant_display import format_occupant_display_name
from server.services.corruption_tier_cache import corruption_tier_cache


def _reset_cache():
    corruption_tier_cache._tiers.clear()  # noqa: SLF001  # pyright: ignore[reportPrivateUsage] -- test cleanup, mirrors test_corruption_service.py's identical fixture


def _no_grace_patches():
    return (
        patch("server.realtime.occupant_display.is_player_in_grace_period", return_value=False),
        patch("server.realtime.occupant_display.is_player_in_login_grace_period", return_value=False),
    )


def test_format_occupant_display_name_no_badge_when_pure():
    _reset_cache()
    player_id = uuid.uuid4()
    p1, p2 = _no_grace_patches()
    with p1, p2:
        result = format_occupant_display_name("Ithaqua", player_id, MagicMock())
    assert result == "Ithaqua"


def test_format_occupant_display_name_no_badge_when_touched():
    """#815: the permanent scar is deliberately invisible in the room -- only a deliberate look
    (look_player.py) reveals it. This is what keeps `touched` a private mark."""
    _reset_cache()
    player_id = uuid.uuid4()
    corruption_tier_cache.set_tier(player_id, CorruptionTier.TOUCHED)
    p1, p2 = _no_grace_patches()
    with p1, p2:
        result = format_occupant_display_name("Ithaqua", player_id, MagicMock())
    assert result == "Ithaqua"


def test_format_occupant_display_name_badge_from_marked():
    _reset_cache()
    player_id = uuid.uuid4()
    corruption_tier_cache.set_tier(player_id, CorruptionTier.MARKED)
    p1, p2 = _no_grace_patches()
    with p1, p2:
        result = format_occupant_display_name("Ithaqua", player_id, MagicMock())
    assert result == "Ithaqua (marked)"


def test_format_occupant_display_name_badge_defiled():
    _reset_cache()
    player_id = uuid.uuid4()
    corruption_tier_cache.set_tier(player_id, CorruptionTier.CORRUPTED)
    p1, p2 = _no_grace_patches()
    with p1, p2:
        result = format_occupant_display_name("Ithaqua", player_id, MagicMock())
    assert result == "Ithaqua (defiled)"


def test_format_occupant_display_name_badge_warped():
    _reset_cache()
    player_id = uuid.uuid4()
    corruption_tier_cache.set_tier(player_id, CorruptionTier.WARPED)
    p1, p2 = _no_grace_patches()
    with p1, p2:
        result = format_occupant_display_name("Ithaqua", player_id, MagicMock())
    assert result == "Ithaqua (warped)"


def test_format_occupant_display_name_combines_grace_and_corruption_badges():
    _reset_cache()
    player_id = uuid.uuid4()
    corruption_tier_cache.set_tier(player_id, CorruptionTier.WARPED)
    with (
        patch("server.realtime.occupant_display.is_player_in_grace_period", return_value=True),
        patch("server.realtime.occupant_display.is_player_in_login_grace_period", return_value=False),
    ):
        result = format_occupant_display_name("Ithaqua", player_id, MagicMock())
    assert result == "Ithaqua (linkdead) (warped)"


def test_format_occupant_display_name_no_connection_manager_returns_name_unchanged():
    """No connection_manager means no grace/corruption lookup is even attempted."""
    _reset_cache()
    player_id = uuid.uuid4()
    corruption_tier_cache.set_tier(player_id, CorruptionTier.WARPED)
    result = format_occupant_display_name("Ithaqua", player_id, None)
    assert result == "Ithaqua"


def test_format_occupant_display_name_unparseable_player_id_returns_name_unchanged():
    _reset_cache()
    p1, p2 = _no_grace_patches()
    with p1, p2:
        result = format_occupant_display_name("Ithaqua", "not-a-uuid", MagicMock())
    assert result == "Ithaqua"


if __name__ == "__main__":
    # ponytail: smallest runnable check for the corruption badge threshold.
    _reset_cache()
    pid = uuid.uuid4()
    corruption_tier_cache.set_tier(pid, CorruptionTier.MARKED)
    with (
        patch("server.realtime.occupant_display.is_player_in_grace_period", return_value=False),
        patch("server.realtime.occupant_display.is_player_in_login_grace_period", return_value=False),
    ):
        demo = format_occupant_display_name("Demo", pid, MagicMock())
    assert demo == "Demo (marked)", demo
    print("occupant badge demo OK")
