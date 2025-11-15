from __future__ import annotations

import json
from collections.abc import Callable, Generator
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import Mock

import pytest

from server.config import reset_config
from server.config.models import TimeConfig
from server.time.time_service import MythosChronicle


@pytest.fixture()
def state_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Generator[Path, None, None]:
    """Provide an isolated chronicle state file for each test."""

    chronicle_path = tmp_path / "chronicle_state.json"
    monkeypatch.setenv("TIME_STATE_FILE", str(chronicle_path))
    monkeypatch.setenv("TIME_COMPRESSION_RATIO", "9.6")
    monkeypatch.setenv("TIME_REAL_EPOCH_UTC", "2025-01-01T00:00:00+00:00")
    monkeypatch.setenv("TIME_MYTHOS_EPOCH", "1930-01-01T00:00:00+00:00")
    reset_config()
    MythosChronicle.reset_instance()
    yield chronicle_path
    MythosChronicle.reset_instance()
    reset_config()


@pytest.fixture()
def chronicle_factory(tmp_path: Path) -> Callable[[datetime, datetime, float], MythosChronicle]:
    """Create arbitrary chronicle instances without touching the singleton."""

    def _factory(
        mythos_epoch: datetime,
        real_epoch: datetime,
        compression_ratio: float = 9.6,
    ) -> MythosChronicle:
        config = TimeConfig(
            compression_ratio=compression_ratio,
            real_epoch_utc=real_epoch,
            mythos_epoch=mythos_epoch,
            state_file=str(tmp_path / f"chronicle_{compression_ratio}.json"),
        )
        return MythosChronicle(config=config, state_path=Path(config.state_file))

    return _factory


def test_conversion_respects_compression_ratio(state_file: Path) -> None:
    chronicle = MythosChronicle.get_instance()
    baseline = chronicle.get_state_snapshot()

    target_real = baseline.real_timestamp + timedelta(hours=2)
    expected_mythos = baseline.mythos_timestamp + timedelta(hours=2 * chronicle.compression_ratio)

    assert chronicle.to_mythos_datetime(target_real) == expected_mythos


def test_state_persists_to_disk_and_reloads(state_file: Path) -> None:
    chronicle = MythosChronicle.get_instance()
    chronicle.advance_mythos(3)
    frozen = chronicle.freeze()

    with state_file.open(encoding="utf-8") as handle:
        payload = json.load(handle)

    assert payload["real_timestamp"] == frozen.real_timestamp.isoformat()
    assert payload["mythos_timestamp"] == frozen.mythos_timestamp.isoformat()

    MythosChronicle.reset_instance()
    reloaded = MythosChronicle.get_instance()
    reloaded_state = reloaded.get_state_snapshot()

    assert reloaded_state.real_timestamp.isoformat() == payload["real_timestamp"]
    assert reloaded_state.mythos_timestamp.isoformat() == payload["mythos_timestamp"]


def test_freeze_emits_metric(state_file: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    mock_counter = Mock()
    monkeypatch.setattr("server.time.time_service.MYTHOS_FREEZE_COUNTER", mock_counter)
    chronicle = MythosChronicle.get_instance()

    chronicle.freeze()

    mock_counter.inc.assert_called_once_with()


def test_daypart_helpers_detect_witching_hour(chronicle_factory: Callable[..., MythosChronicle]) -> None:
    chronicle = chronicle_factory(
        mythos_epoch=datetime(1930, 1, 1, 0, 0, tzinfo=UTC),
        real_epoch=datetime(2025, 1, 1, 0, 0, tzinfo=UTC),
    )
    witching_dt = datetime(1930, 1, 1, 23, 30, tzinfo=UTC)
    assert chronicle.is_witching_hour(witching_dt) is True
    assert chronicle.get_daypart(witching_dt) == "witching"

    midmorning = datetime(1930, 1, 2, 9, 0, tzinfo=UTC)
    assert chronicle.is_witching_hour(midmorning) is False
    assert chronicle.get_daypart(midmorning) == "day"


def test_calendar_components_attach_seasonal_metadata(chronicle_factory: Callable[..., MythosChronicle]) -> None:
    chronicle = chronicle_factory(
        mythos_epoch=datetime(1930, 3, 5, 7, 45, tzinfo=UTC),
        real_epoch=datetime(2025, 3, 1, 0, 0, tzinfo=UTC),
    )
    target_dt = datetime(1930, 3, 5, 7, 45, tzinfo=UTC)
    components = chronicle.get_calendar_components(target_dt)

    assert components.month_name == "March"
    assert components.day_of_month == 5
    assert components.week_of_month == 1  # (5 - 1) // 6 + 1 based on six-day weeks
    assert components.day_of_week == 4
    assert components.season == "spring"
    assert components.is_daytime is True
    assert components.daypart == "day"
