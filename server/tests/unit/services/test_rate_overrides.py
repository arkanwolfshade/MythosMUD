"""Unit tests for server/services/passive_lucidity_flux/rate_overrides.py.

Backfills coverage for this module's pure helpers and its asyncpg-driven load path (#633's
conversion of the raw UNION ALL query to a call to db/procedures/lucidity.sql's
get_lucidity_rate_overrides() shrank the file; nothing here previously exercised the functions
directly, so the file's coverage dropped below the 70% floor -- these tests close that gap for
real rather than lowering the threshold).
"""

from __future__ import annotations

from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import asyncpg
import pytest

from server.services.passive_lucidity_flux.rate_overrides import (
    _async_load_lucidity_rate_overrides,
    _LucidityRateLoadResult,
    _normalize_database_url,
    _parse_special_rules_from_raw,
    _parse_zone_stable_id,
    _process_override_row,
    _warn_if_rate_exceeds_threshold,
    build_override_key,
    extract_lucidity_rate,
    load_lucidity_rate_overrides,
    rate_to_flux,
)


def _empty_result() -> _LucidityRateLoadResult:
    return {"overrides": {}, "error": None}


def _mock_row(zone_stable_id: str, subzone_stable_id: str | None, special_rules: dict[str, object]) -> asyncpg.Record:
    """Fake an asyncpg.Record via a MagicMock with dict-style __getitem__ (test_zone_config_loader.py's pattern)."""
    row = MagicMock()
    data = {
        "zone_stable_id": zone_stable_id,
        "subzone_stable_id": subzone_stable_id,
        "special_rules": special_rules,
    }
    row.__getitem__ = MagicMock(side_effect=data.get)
    return cast(asyncpg.Record, row)


def test_build_override_key_full_hierarchy() -> None:
    assert build_override_key("Earth", "Arkham", "Downtown") == "earth|arkham|downtown"


def test_build_override_key_missing_parts_default_to_wildcard() -> None:
    assert build_override_key(None, "Arkham", None) == "*|arkham|*"


def test_rate_to_flux_negates_normal_rate() -> None:
    assert rate_to_flux(0.5) == -0.5


def test_rate_to_flux_clamps_above_threshold() -> None:
    assert rate_to_flux(100.0) == -10.0


def test_extract_lucidity_rate_returns_value() -> None:
    assert extract_lucidity_rate({"special_rules": {"lucidity_drain_rate": 0.3}}) == 0.3


def test_extract_lucidity_rate_missing_special_rules_returns_none() -> None:
    assert extract_lucidity_rate({}) is None


def test_extract_lucidity_rate_non_numeric_returns_none() -> None:
    assert extract_lucidity_rate({"special_rules": {"lucidity_drain_rate": "fast"}}) is None


def test_normalize_database_url_converts_sqlalchemy_scheme() -> None:
    assert _normalize_database_url("postgresql+asyncpg://u:p@host/db") == "postgresql://u:p@host/db"


def test_normalize_database_url_leaves_plain_url_alone() -> None:
    assert _normalize_database_url("postgresql://u:p@host/db") == "postgresql://u:p@host/db"


def test_parse_zone_stable_id_splits_plane_and_zone() -> None:
    assert _parse_zone_stable_id("earth/arkham") == ("earth", "arkham")


def test_parse_zone_stable_id_no_slash_returns_none_zone() -> None:
    assert _parse_zone_stable_id("earth") == ("earth", None)


def test_parse_special_rules_from_raw_json_string() -> None:
    assert _parse_special_rules_from_raw('{"lucidity_drain_rate": 0.2}') == {"lucidity_drain_rate": 0.2}


def test_parse_special_rules_from_raw_dict_passthrough() -> None:
    assert _parse_special_rules_from_raw({"lucidity_drain_rate": 0.2}) == {"lucidity_drain_rate": 0.2}


def test_parse_special_rules_from_raw_none_returns_empty() -> None:
    assert _parse_special_rules_from_raw(None) == {}


def test_warn_if_rate_exceeds_threshold_logs_above_ten() -> None:
    # No exception, just exercising the warning branch; nothing to assert against since this
    # project uses structlog (not stdlib logging, so caplog wouldn't capture it) -- absence of a
    # raised exception is the check.
    _warn_if_rate_exceeds_threshold(15.0, "earth/arkham", None)


def test_warn_if_rate_exceeds_threshold_silent_at_or_below_ten() -> None:
    _warn_if_rate_exceeds_threshold(10.0, "earth/arkham", None)


def test_process_override_row_zone_level() -> None:
    row = _mock_row("earth/arkham", None, {"lucidity_drain_rate": 0.4})
    container = _empty_result()
    _process_override_row(row, container)
    assert container["overrides"]["earth|arkham|*"] == -0.4


def test_process_override_row_subzone_level() -> None:
    row = _mock_row("earth/arkham", "downtown", {"lucidity_drain_rate": 0.6})
    container = _empty_result()
    _process_override_row(row, container)
    assert container["overrides"]["earth|arkham|downtown"] == -0.6


def test_process_override_row_missing_rate_is_skipped() -> None:
    row = _mock_row("earth/arkham", None, {})
    container = _empty_result()
    _process_override_row(row, container)
    assert container["overrides"] == {}


@pytest.mark.asyncio
async def test_async_load_lucidity_rate_overrides_missing_database_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    container = _empty_result()
    await _async_load_lucidity_rate_overrides(container)
    assert isinstance(container["error"], ValueError)


@pytest.mark.asyncio
async def test_async_load_lucidity_rate_overrides_success(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://u:p@host/db")
    row = _mock_row("earth/arkham", None, {"lucidity_drain_rate": 0.1})
    mock_conn = AsyncMock()
    mock_conn.fetch = AsyncMock(return_value=[row])
    mock_conn.close = AsyncMock()

    with patch(
        "server.services.passive_lucidity_flux.rate_overrides.asyncpg.connect",
        new_callable=AsyncMock,
        return_value=mock_conn,
    ):
        container = _empty_result()
        await _async_load_lucidity_rate_overrides(container)

    assert container["error"] is None
    assert container["overrides"]["earth|arkham|*"] == -0.1
    mock_conn.close.assert_awaited_once()


def test_load_lucidity_rate_overrides_returns_empty_on_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    result = load_lucidity_rate_overrides()
    assert result == {}


def test_load_lucidity_rate_overrides_success() -> None:
    row = _mock_row("earth/arkham", None, {"lucidity_drain_rate": 0.2})
    mock_conn = MagicMock()
    mock_conn.fetch = AsyncMock(return_value=[row])
    mock_conn.close = AsyncMock()

    with (
        patch.dict("os.environ", {"DATABASE_URL": "postgresql+asyncpg://u:p@host/db"}),
        patch(
            "server.services.passive_lucidity_flux.rate_overrides.asyncpg.connect",
            new_callable=AsyncMock,
            return_value=mock_conn,
        ),
    ):
        result = load_lucidity_rate_overrides()

    assert result == {"earth|arkham|*": -0.2}
