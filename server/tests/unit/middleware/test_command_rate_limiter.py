"""Unit tests for CommandRateLimiter sliding window."""

from datetime import UTC, datetime, timedelta

from server.middleware.command_rate_limiter import CommandRateLimiter


def _fixed_clock(start: datetime):
    current = {"value": start}

    def now() -> datetime:
        return current["value"]

    def advance(seconds: float) -> None:
        current["value"] = current["value"] + timedelta(seconds=seconds)

    return now, advance


def test_is_allowed_under_limit() -> None:
    start = datetime(2026, 1, 1, tzinfo=UTC)
    now, _ = _fixed_clock(start)
    limiter = CommandRateLimiter(max_commands=3, window_seconds=1, now_provider=now)
    assert limiter.is_allowed("Alice") is True
    assert limiter.is_allowed("Alice") is True
    assert limiter.get_remaining_commands("Alice") == 1


def test_is_allowed_blocks_at_limit() -> None:
    start = datetime(2026, 1, 1, tzinfo=UTC)
    now, _ = _fixed_clock(start)
    limiter = CommandRateLimiter(max_commands=2, window_seconds=1, now_provider=now)
    assert limiter.is_allowed("Bob") is True
    assert limiter.is_allowed("Bob") is True
    assert limiter.is_allowed("Bob") is False


def test_sliding_window_expires_old_commands() -> None:
    start = datetime(2026, 1, 1, tzinfo=UTC)
    now, advance = _fixed_clock(start)
    limiter = CommandRateLimiter(max_commands=1, window_seconds=1, now_provider=now)
    assert limiter.is_allowed("Carol") is True
    assert limiter.is_allowed("Carol") is False
    advance(1.1)
    assert limiter.is_allowed("Carol") is True


def test_get_wait_time_when_rate_limited() -> None:
    start = datetime(2026, 1, 1, tzinfo=UTC)
    now, _ = _fixed_clock(start)
    limiter = CommandRateLimiter(max_commands=1, window_seconds=2, now_provider=now)
    limiter.is_allowed("Dave")
    wait = limiter.get_wait_time("Dave")
    assert 0.0 < wait <= 2.0


def test_reset_player_and_all() -> None:
    start = datetime(2026, 1, 1, tzinfo=UTC)
    now, _ = _fixed_clock(start)
    limiter = CommandRateLimiter(max_commands=1, window_seconds=1, now_provider=now)
    limiter.is_allowed("Eve")
    limiter.reset_player("Eve")
    assert limiter.get_remaining_commands("Eve") == 1
    limiter.is_allowed("Frank")
    limiter.reset_all()
    assert limiter.get_stats()["active_players"] == 0


def test_get_stats_and_cleanup_inactive() -> None:
    start = datetime(2026, 1, 1, tzinfo=UTC)
    now, _ = _fixed_clock(start)
    limiter = CommandRateLimiter(max_commands=2, window_seconds=1, now_provider=now)
    limiter.is_allowed("Grace")
    limiter.is_allowed("Grace")
    stats = limiter.get_stats()
    assert stats["active_players"] == 1
    assert stats["rate_limited_players"] == 1
    cleaned = limiter.cleanup_inactive_players(inactive_threshold_hours=0)
    assert cleaned == 1
