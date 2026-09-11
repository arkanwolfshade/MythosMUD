"""
Load corruption flux rate/target overrides from PostgreSQL zones/subzones (#815 PR-5).

Reuses `get_lucidity_rate_overrides()` (db/procedures/lucidity.sql) rather than adding a parallel
stored procedure -- despite its name, that function does nothing lucidity-specific: it fetches
every zone/subzone row's raw `special_rules` JSONB in one UNION ALL query with no key filtering.
The `lucidity_drain_rate` key lucidity's own reader extracts and the `corruption_rate`/
`corruption_target` keys extracted here coexist in the same JSONB blob without conflict.

`build_override_key` is likewise pure plane/zone/subzone string composition with nothing
lucidity-specific in it -- reused directly rather than duplicated.
"""

from __future__ import annotations

import asyncio
import json
import os
import threading
from collections.abc import Mapping
from typing import TypedDict, cast

import asyncpg

from ...database_config_helpers import get_asyncpg_server_settings_for_database_url
from ...structured_logging.enhanced_logging_config import get_logger
from ..passive_lucidity_flux.rate_overrides import build_override_key
from .config import CorruptionOverride

logger = get_logger(__name__)

__all__ = ["build_override_key", "load_corruption_overrides"]


class _CorruptionOverrideLoadResult(TypedDict):
    overrides: dict[str, CorruptionOverride]
    error: BaseException | None


def _extract_corruption_override(special_rules: Mapping[str, object]) -> CorruptionOverride | None:
    """Extract corruption_rate/corruption_target from a special_rules mapping, or None if neither is set."""
    rate_raw = special_rules.get("corruption_rate")
    target_raw = special_rules.get("corruption_target")
    rate = float(rate_raw) if isinstance(rate_raw, int | float) else None
    target = float(target_raw) if isinstance(target_raw, int | float) else None
    if rate is None and target is None:
        return None
    return CorruptionOverride(rate=rate, target=target)


def _normalize_database_url(url: str) -> str:
    """Convert SQLAlchemy-style URL to asyncpg-compatible format."""
    if url.startswith("postgresql+asyncpg://"):
        return url.replace("postgresql+asyncpg://", "postgresql://", 1)
    return url


def _parse_zone_stable_id(zone_stable_id: str) -> tuple[str | None, str | None]:
    """Parse plane and zone from zone_stable_id (format: 'plane/zone')."""
    parts = zone_stable_id.split("/")
    plane = parts[0] if len(parts) > 0 else None
    zone = parts[1] if len(parts) > 1 else None
    return plane, zone


def _parse_special_rules_from_raw(special_rules_raw: object) -> dict[str, object]:
    """Parse special_rules column value into a dict."""
    if isinstance(special_rules_raw, str):
        parsed_rules = cast(object, json.loads(special_rules_raw))
        if isinstance(parsed_rules, dict):
            return cast(dict[str, object], parsed_rules)
        return {}
    if isinstance(special_rules_raw, dict):
        return cast(dict[str, object], special_rules_raw)
    return {}


def _process_override_row(row: asyncpg.Record, result_container: _CorruptionOverrideLoadResult) -> None:
    """Process a single zone/subzone row and add a corruption override if either key is set."""
    zone_stable_id = str(cast(object, row["zone_stable_id"]))
    subzone_stable_id_raw: object = cast(object, row["subzone_stable_id"])
    subzone_stable_id = str(subzone_stable_id_raw) if subzone_stable_id_raw is not None else None
    special_rules = _parse_special_rules_from_raw(cast(object, row["special_rules"]))

    override = _extract_corruption_override(special_rules)
    if override is None:
        return

    plane, zone = _parse_zone_stable_id(zone_stable_id)
    sub_zone = subzone_stable_id or None
    key = build_override_key(plane, zone, sub_zone)
    result_container["overrides"][key] = override
    logger.debug(
        "Loaded corruption flux override from database",
        key=key,
        rate=override.rate,
        target=override.target,
        source="subzone_config" if subzone_stable_id else "zone_config",
    )


async def _async_load_corruption_overrides(result_container: _CorruptionOverrideLoadResult) -> None:
    """Async helper to load corruption flux overrides from PostgreSQL."""
    try:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL environment variable not set")

        database_url = _normalize_database_url(database_url)
        server_settings = get_asyncpg_server_settings_for_database_url(database_url)
        conn = await asyncpg.connect(database_url, server_settings=server_settings)
        try:
            rows = await conn.fetch(
                "SELECT zone_stable_id, subzone_stable_id, special_rules FROM get_lucidity_rate_overrides()"
            )
            for row in rows:
                _process_override_row(row, result_container)
        finally:
            await conn.close()
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        # Reason: must catch all errors (asyncpg, ValueError, JSON, etc.) and not re-raise so the
        # loader thread exits normally -- mirrors passive_lucidity_flux/rate_overrides.py exactly.
        result_container["error"] = e


def load_corruption_overrides() -> dict[str, CorruptionOverride]:
    """Load corruption flux rate/target overrides from PostgreSQL zones/subzones tables."""
    result_container: _CorruptionOverrideLoadResult = {"overrides": {}, "error": None}

    def run_async() -> None:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        try:
            new_loop.run_until_complete(_async_load_corruption_overrides(result_container))
        finally:
            new_loop.close()

    thread = threading.Thread(target=run_async)
    thread.start()
    thread.join()

    error = result_container.get("error")
    if error is not None:
        logger.warning("Could not load corruption flux overrides from database", error=str(error))
        return {}

    overrides = result_container["overrides"]
    if overrides:
        logger.info("Loaded corruption flux overrides from database", count=len(overrides))
    else:
        logger.info("No corruption flux overrides found in database")
    return overrides
