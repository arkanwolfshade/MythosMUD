"""Unit tests for server/services/passive_corruption_flux/rate_overrides.py.

Mirrors test_rate_overrides.py (lucidity's equivalent module) -- these pure helpers and the
asyncpg-driven load path aren't exercised by test_passive_corruption_flux_service.py, which only
ever supplies an already-resolved overrides dict via config.
"""

# pyright: reportPrivateUsage=false
# TEST_MOCK: deliberately exercises rate_overrides.py's private load-path helpers directly --
# same house style as test_aggro_threat.py and every other private-method-testing suite here.
# pyright: reportAny=false
# TEST_MOCK: MagicMock/AsyncMock attribute and call chains (mock_conn.close, .assert_awaited_once)
# resolve to Any throughout this file, mirroring test_rate_overrides.py's identical pattern for
# the same mock-typing noise -- this file is new, so it has no baseline entry of its own.

from __future__ import annotations

from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import asyncpg
import pytest

from server.services.passive_corruption_flux.config import CorruptionOverride
from server.services.passive_corruption_flux.rate_overrides import (
    _async_load_corruption_overrides,
    _CorruptionOverrideLoadResult,
    _extract_corruption_override,
    _normalize_database_url,
    _parse_special_rules_from_raw,
    _parse_zone_stable_id,
    _process_override_row,
    build_override_key,
    load_corruption_overrides,
)


def _empty_result() -> _CorruptionOverrideLoadResult:
    return {"overrides": {}, "error": None}


def _mock_row(zone_stable_id: str, subzone_stable_id: str | None, special_rules: dict[str, object]) -> asyncpg.Record:
    """Fake an asyncpg.Record via a MagicMock with dict-style __getitem__ (test_rate_overrides.py's pattern)."""
    row = MagicMock()
    data = {
        "zone_stable_id": zone_stable_id,
        "subzone_stable_id": subzone_stable_id,
        "special_rules": special_rules,
    }
    row.__getitem__ = MagicMock(side_effect=data.get)
    return cast(asyncpg.Record, row)


def test_build_override_key_full_hierarchy() -> None:
    assert build_override_key("Earth", "Innsmouth", "Waterfront") == "earth|innsmouth|waterfront"


def test_extract_corruption_override_rate_only() -> None:
    override = _extract_corruption_override({"corruption_rate": 0.05})
    assert override == CorruptionOverride(rate=0.05, target=None)


def test_extract_corruption_override_target_only() -> None:
    override = _extract_corruption_override({"corruption_target": 80})
    assert override == CorruptionOverride(rate=None, target=80.0)


def test_extract_corruption_override_both() -> None:
    override = _extract_corruption_override({"corruption_rate": 0.1, "corruption_target": 50})
    assert override == CorruptionOverride(rate=0.1, target=50.0)


def test_extract_corruption_override_neither_returns_none() -> None:
    assert _extract_corruption_override({}) is None


def test_extract_corruption_override_non_numeric_ignored() -> None:
    assert _extract_corruption_override({"corruption_rate": "fast"}) is None


def test_normalize_database_url_converts_sqlalchemy_scheme() -> None:
    assert _normalize_database_url("postgresql+asyncpg://u:p@host/db") == "postgresql://u:p@host/db"


def test_normalize_database_url_leaves_plain_url_alone() -> None:
    assert _normalize_database_url("postgresql://u:p@host/db") == "postgresql://u:p@host/db"


def test_parse_zone_stable_id_splits_plane_and_zone() -> None:
    assert _parse_zone_stable_id("earth/innsmouth") == ("earth", "innsmouth")


def test_parse_zone_stable_id_no_slash_returns_none_zone() -> None:
    assert _parse_zone_stable_id("earth") == ("earth", None)


def test_parse_special_rules_from_raw_json_string() -> None:
    assert _parse_special_rules_from_raw('{"corruption_rate": 0.2}') == {"corruption_rate": 0.2}


def test_parse_special_rules_from_raw_dict_passthrough() -> None:
    assert _parse_special_rules_from_raw({"corruption_rate": 0.2}) == {"corruption_rate": 0.2}


def test_parse_special_rules_from_raw_none_returns_empty() -> None:
    assert _parse_special_rules_from_raw(None) == {}


def test_process_override_row_zone_level() -> None:
    row = _mock_row("earth/innsmouth", None, {"corruption_rate": 0.05})
    container = _empty_result()
    _process_override_row(row, container)
    assert container["overrides"]["earth|innsmouth|*"] == CorruptionOverride(rate=0.05, target=None)


def test_process_override_row_subzone_level() -> None:
    row = _mock_row("earth/innsmouth", "waterfront", {"corruption_target": 65})
    container = _empty_result()
    _process_override_row(row, container)
    assert container["overrides"]["earth|innsmouth|waterfront"] == CorruptionOverride(rate=None, target=65.0)


def test_process_override_row_missing_keys_is_skipped() -> None:
    row = _mock_row("earth/innsmouth", None, {})
    container = _empty_result()
    _process_override_row(row, container)
    assert container["overrides"] == {}


@pytest.mark.asyncio
async def test_async_load_corruption_overrides_missing_database_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    container = _empty_result()
    await _async_load_corruption_overrides(container)
    assert isinstance(container["error"], ValueError)


@pytest.mark.asyncio
async def test_async_load_corruption_overrides_success(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://u:p@host/db")
    row = _mock_row("earth/innsmouth", None, {"corruption_rate": 0.05})
    mock_conn = AsyncMock()
    mock_conn.fetch = AsyncMock(return_value=[row])
    mock_conn.close = AsyncMock()

    with patch(
        "server.services.passive_corruption_flux.rate_overrides.asyncpg.connect",
        new_callable=AsyncMock,
        return_value=mock_conn,
    ):
        container = _empty_result()
        await _async_load_corruption_overrides(container)

    assert container["error"] is None
    assert container["overrides"]["earth|innsmouth|*"] == CorruptionOverride(rate=0.05, target=None)
    mock_conn.close.assert_awaited_once()


def test_load_corruption_overrides_returns_empty_on_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    result = load_corruption_overrides()
    assert result == {}


def test_load_corruption_overrides_success() -> None:
    row = _mock_row("earth/innsmouth", None, {"corruption_rate": 0.05, "corruption_target": 65})
    mock_conn = MagicMock()
    mock_conn.fetch = AsyncMock(return_value=[row])
    mock_conn.close = AsyncMock()

    with (
        patch.dict("os.environ", {"DATABASE_URL": "postgresql+asyncpg://u:p@host/db"}),
        patch(
            "server.services.passive_corruption_flux.rate_overrides.asyncpg.connect",
            new_callable=AsyncMock,
            return_value=mock_conn,
        ),
    ):
        result = load_corruption_overrides()

    assert result == {"earth|innsmouth|*": CorruptionOverride(rate=0.05, target=65.0)}
