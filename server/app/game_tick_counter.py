"""Shared game tick counter.

Kept in a leaf module so combat services can read the tick without importing
the game tick loop (and its corpse/container import chain).
"""

_current_tick = 0  # pylint: disable=invalid-name  # noqa: N816  # Reason: Mutable module-level tick, not a constant


def get_current_tick() -> int:
    """Get the current game tick."""
    return _current_tick


def set_current_tick(tick_count: int) -> None:
    """Set the current game tick (game tick loop)."""
    global _current_tick  # pylint: disable=global-statement  # Reason: Module-level tick counter
    _current_tick = tick_count


def reset_current_tick() -> None:
    """Reset the current tick for testing."""
    set_current_tick(0)
