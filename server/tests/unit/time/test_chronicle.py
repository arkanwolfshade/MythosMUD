from __future__ import annotations

import json
from collections.abc import Generator
from datetime import timedelta
from pathlib import Path
from unittest.mock import Mock

import pytest

from server.config import reset_config
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
