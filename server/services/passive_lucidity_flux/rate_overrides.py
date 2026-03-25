"""Load lucidity rate overrides from PostgreSQL zones/subzones."""

from __future__ import annotations

import asyncio
import json
import os
import threading
from typing import Any

import asyncpg

from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def build_override_key(plane: str | None, zone: str | None, sub_zone: str | None) -> str:
    """Build override key from plane/zone/subzone hierarchy."""
    plane_part = (plane or "*").lower()
    zone_part = (zone or "*").lower()
    sub_zone_part = (sub_zone or "*").lower()
    return f"{plane_part}|{zone_part}|{sub_zone_part}"


def rate_to_flux(rate: float) -> float:
    """
    Convert lucidity_drain_rate to flux value.

    Args:
        rate: Lucidity drain rate (expected range: 0.0 to ~2.0 per minute)

    Returns:
        Negative flux value (since drain is negative)
    """
    rate_float = float(rate)
    if rate_float > 10.0:
        logger.error(
            "Lucidity drain rate exceeds maximum threshold - possible configuration error",
            rate=rate_float,
            message="Rates > 10.0 are likely configuration errors (e.g., 100 instead of 0.1). Clamping to 10.0.",
        )
        rate_float = 10.0
    return -rate_float


def extract_lucidity_rate(config: dict[str, Any]) -> float | None:
    """Extract lucidity_drain_rate from special_rules config."""
    special_rules = config.get("special_rules")
    if not isinstance(special_rules, dict):
        return None
    value = special_rules.get("lucidity_drain_rate")
    if isinstance(value, int | float):
        return float(value)
    return None


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


def _process_override_row(row: asyncpg.Record, result_container: dict[str, Any]) -> None:
    """Process a single zone/subzone row and add override to result_container if valid."""
    zone_stable_id = row["zone_stable_id"]
    subzone_stable_id = row["subzone_stable_id"]
    special_rules = row["special_rules"] or {}
    if isinstance(special_rules, str):
        special_rules = json.loads(special_rules)

    rate = extract_lucidity_rate({"special_rules": special_rules})
    if rate is None:
        return

    if rate > 10.0:
        logger.warning(
            "Lucidity drain rate from database exceeds threshold",
            rate=rate,
            zone_stable_id=zone_stable_id,
            subzone_stable_id=subzone_stable_id,
            message="This may indicate a configuration error (e.g., 100 instead of 0.1)",
        )

    plane, zone = _parse_zone_stable_id(zone_stable_id)
    sub_zone = subzone_stable_id or None
    source = "subzone_config" if subzone_stable_id else "zone_config"

    key = build_override_key(plane, zone, sub_zone)
    flux = rate_to_flux(rate)
    result_container["overrides"][key] = flux
    logger.debug(
        "Loaded lucidity rate override from database",
        key=key,
        rate=rate,
        flux=flux,
        source=source,
    )


async def _async_load_lucidity_rate_overrides(result_container: dict[str, Any]) -> None:
    """Async helper to load lucidity rate overrides from PostgreSQL."""
    try:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL environment variable not set")

        database_url = _normalize_database_url(database_url)
        conn = await asyncpg.connect(database_url)
        try:
            query = """
                SELECT
                    z.stable_id as zone_stable_id,
                    NULL::text as subzone_stable_id,
                    z.special_rules
                FROM zones z
                WHERE z.special_rules IS NOT NULL
                UNION ALL
                SELECT
                    z.stable_id as zone_stable_id,
                    sz.stable_id as subzone_stable_id,
                    sz.special_rules
                FROM subzones sz
                JOIN zones z ON sz.zone_id = z.id
                WHERE sz.special_rules IS NOT NULL
                ORDER BY zone_stable_id, subzone_stable_id
            """
            rows = await conn.fetch(query)
            for row in rows:
                _process_override_row(row, result_container)
        finally:
            await conn.close()
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
        # Reason: Must catch all errors (asyncpg, ValueError, JSON, etc.) and not re-raise so the loader
        # thread exits normally. Re-raising would cause PytestUnhandledThreadExceptionWarning when
        # zones/subzones tables are missing in unit test DB.
        result_container["error"] = e


def load_lucidity_rate_overrides() -> dict[str, float]:
    """Load lucidity rate overrides from PostgreSQL zones/subzones tables."""
    overrides: dict[str, float] = {}
    result_container: dict[str, Any] = {"overrides": {}, "error": None}

    def run_async() -> None:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        try:
            new_loop.run_until_complete(_async_load_lucidity_rate_overrides(result_container))
        finally:
            new_loop.close()

    thread = threading.Thread(target=run_async)
    thread.start()
    thread.join()

    error = result_container.get("error")
    if error is not None:
        logger.warning("Could not load lucidity rate overrides from database", error=str(error))
        return overrides

    overrides = result_container.get("overrides", {})
    if overrides:
        logger.info("Loaded lucidity rate overrides from database", count=len(overrides))
    else:
        logger.info("No lucidity rate overrides found in database")
    return overrides
