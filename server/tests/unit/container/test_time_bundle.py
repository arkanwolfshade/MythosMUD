"""Unit tests for TimeBundle container wiring."""

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest

from server.container.bundles.time import TIME_ATTRS, TimeBundle
from server.time.time_service import MythosChronicle, _ensure_utc, _season_for_month, get_mythos_chronicle


def test_time_bundle_attrs() -> None:
    assert TIME_ATTRS == ("mythos_time_consumer",)


@pytest.mark.asyncio
async def test_time_bundle_initialize_with_dependencies() -> None:
    bundle = TimeBundle()
    container = MagicMock()
    container.event_bus = MagicMock()
    container.holiday_service = MagicMock()
    container.schedule_service = MagicMock()
    container.room_service = MagicMock()
    container.npc_lifecycle_manager = MagicMock()

    with patch("server.time.time_event_consumer.MythosTimeEventConsumer") as mock_consumer_cls:
        with patch("server.time.time_service.get_mythos_chronicle", return_value=MagicMock()):
            mock_consumer_cls.return_value = MagicMock()
            await bundle.initialize(container)

    assert bundle.mythos_time_consumer is not None
    mock_consumer_cls.assert_called_once()


@pytest.mark.asyncio
async def test_time_bundle_initialize_missing_dependencies() -> None:
    bundle = TimeBundle()
    container = MagicMock()
    container.event_bus = None
    container.holiday_service = MagicMock()
    container.schedule_service = MagicMock()
    container.room_service = MagicMock()
    container.npc_lifecycle_manager = MagicMock()

    await bundle.initialize(container)
    assert bundle.mythos_time_consumer is None


def test_ensure_utc_naive_datetime() -> None:
    """Naive datetimes are normalized to UTC."""
    naive = datetime(1926, 10, 31, 12, 0, 0)
    result = _ensure_utc(naive)
    assert result.tzinfo == UTC


def test_season_for_month() -> None:
    """Season mapping follows month bands."""
    assert _season_for_month(12) == "winter"
    assert _season_for_month(4) == "spring"
    assert _season_for_month(7) == "summer"
    assert _season_for_month(10) == "autumn"


@pytest.fixture
def isolated_chronicle(tmp_path):
    """Chronicle with isolated state file."""
    MythosChronicle.reset_instance()
    state_path = tmp_path / "mythos_state.json"
    epoch_real = datetime(2026, 1, 1, 0, 0, 0, tzinfo=UTC)
    epoch_mythos = datetime(1926, 1, 1, 0, 0, 0, tzinfo=UTC)
    with patch("server.time.time_service.get_config") as mock_cfg:
        mock_cfg.return_value.time.compression_ratio = 9.0
        mock_cfg.return_value.time.state_file = str(state_path)
        mock_cfg.return_value.time.real_epoch_utc = epoch_real
        mock_cfg.return_value.time.mythos_epoch = epoch_mythos
        chronicle = MythosChronicle(state_path=state_path)
        yield chronicle
    MythosChronicle.reset_instance()


def test_chronicle_calendar_and_dayparts(isolated_chronicle) -> None:
    """Calendar components and daypart helpers."""
    mythos_dt = datetime(1926, 10, 31, 14, 0, 0, tzinfo=UTC)
    components = isolated_chronicle.get_calendar_components(mythos_dt)
    assert components.season == "autumn"
    assert components.month_name == "October"
    assert isolated_chronicle.is_daytime(mythos_dt) is True
    assert isolated_chronicle.get_daypart(mythos_dt) == "day"
    witching = datetime(1926, 10, 31, 23, 30, 0, tzinfo=UTC)
    assert isolated_chronicle.is_witching_hour(witching) is True
    assert isolated_chronicle.get_daypart(witching) == "witching"


def test_chronicle_time_conversion(isolated_chronicle) -> None:
    """Real/Mythos datetime conversion round-trips approximately."""
    real_dt = datetime(2026, 1, 1, 12, 0, 0, tzinfo=UTC)
    mythos_dt = isolated_chronicle.to_mythos_datetime(real_dt)
    back = isolated_chronicle.to_real_datetime(mythos_dt)
    assert abs((back - real_dt).total_seconds()) < 1


def test_chronicle_advance_and_freeze(isolated_chronicle) -> None:
    """Advance and freeze update persisted state."""
    before = isolated_chronicle.get_state_snapshot()
    advanced = isolated_chronicle.advance_mythos(2.0)
    assert advanced.mythos_timestamp > before.mythos_timestamp
    frozen = isolated_chronicle.freeze()
    assert frozen.real_timestamp is not None
    assert isolated_chronicle.get_last_freeze_state() is not None


def test_chronicle_format_clock(isolated_chronicle) -> None:
    """Clock formatting includes Mythos suffix."""
    mythos_dt = datetime(1926, 1, 1, 8, 5, 0, tzinfo=UTC)
    assert isolated_chronicle.format_clock(mythos_dt) == "08:05 Mythos"


def test_get_mythos_chronicle_singleton() -> None:
    """get_mythos_chronicle returns the same instance."""
    MythosChronicle.reset_instance()
    first = get_mythos_chronicle()
    second = get_mythos_chronicle()
    assert first is second
    MythosChronicle.reset_instance()


def test_chronicle_advance_rejects_negative_delta(isolated_chronicle) -> None:
    """advance_mythos rejects negative hours."""
    with pytest.raises(ValueError, match="positive"):
        isolated_chronicle.advance_mythos(-1.0)
