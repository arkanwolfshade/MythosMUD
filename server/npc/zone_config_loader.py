"""
Zone Configuration Loader Module.

This module handles loading zone and sub-zone configurations from the PostgreSQL
database.
"""

import asyncio
import json
import os
import threading
from typing import Any

import asyncpg

from ..structured_logging.enhanced_logging_config import get_logger
from .zone_configuration import ZoneConfiguration

logger = get_logger(__name__)


def parse_json_field(field_value: Any, default: Any) -> Any:
    """
    Parse a JSON field from database, handling both dict/list and string formats.

    Args:
        field_value: The field value from the database
        default: Default value if field is None

    Returns:
        Parsed JSON value or default
    """
    if field_value is None:
        return default
    if isinstance(field_value, str):
        return json.loads(field_value)
    return field_value


def extract_zone_name(stable_id: str) -> str:
    """
    Extract zone name from stable_id (format: 'plane/zone').

    Args:
        stable_id: The stable ID in format 'plane/zone'

    Returns:
        Zone name extracted from stable_id
    """
    zone_parts = stable_id.split("/")
    return zone_parts[1] if len(zone_parts) > 1 else stable_id


async def process_zone_rows(conn: Any, result_container: dict[str, Any]) -> None:
    """
    Process zone rows from database and populate zone configurations.

    Args:
        conn: Database connection
        result_container: Container to store results
    """
    zone_query = """
        SELECT
            z.id,
            z.stable_id as zone_stable_id,
            z.zone_type,
            z.environment,
            z.description,
            z.weather_patterns,
            z.special_rules
        FROM zones z
        ORDER BY z.stable_id
    """
    zone_rows = await conn.fetch(zone_query)

    for row in zone_rows:
        zone_stable_id = row["zone_stable_id"]
        zone_name = extract_zone_name(zone_stable_id)
        weather_patterns = parse_json_field(row["weather_patterns"], [])
        special_rules = parse_json_field(row["special_rules"], {})

        config_data = {
            "zone_type": row["zone_type"],
            "environment": row["environment"],
            "description": row["description"],
            "weather_patterns": weather_patterns,
            "special_rules": special_rules,
        }

        zone_config = ZoneConfiguration(config_data)
        result_container["configs"]["zone"][zone_name] = zone_config


async def process_subzone_rows(conn: Any, result_container: dict[str, Any]) -> None:
    """
    Process subzone rows from database and populate subzone configurations.

    Args:
        conn: Database connection
        result_container: Container to store results
    """
    subzone_query = """
        SELECT
            sz.id,
            z.stable_id as zone_stable_id,
            sz.stable_id as subzone_stable_id,
            sz.environment,
            sz.description,
            sz.special_rules,
            z.zone_type,
            z.weather_patterns
        FROM subzones sz
        JOIN zones z ON sz.zone_id = z.id
        ORDER BY z.stable_id, sz.stable_id
    """
    subzone_rows = await conn.fetch(subzone_query)

    for row in subzone_rows:
        zone_stable_id = row["zone_stable_id"]
        subzone_stable_id = row["subzone_stable_id"]
        zone_name = extract_zone_name(zone_stable_id)
        weather_patterns = parse_json_field(row["weather_patterns"], [])
        special_rules = parse_json_field(row["special_rules"], {})

        config_data = {
            "zone_type": row["zone_type"],  # Inherited from zone
            "environment": row["environment"],
            "description": row["description"],
            "weather_patterns": weather_patterns,  # Inherited from zone
            "special_rules": special_rules,
        }

        zone_config = ZoneConfiguration(config_data)
        subzone_key = f"{zone_name}/{subzone_stable_id}"
        result_container["configs"]["subzone"][subzone_key] = zone_config
        logger.debug(
            "Loaded subzone configuration",
            subzone_key=subzone_key,
            zone_stable_id=zone_stable_id,
            subzone_stable_id=subzone_stable_id,
            zone_name=zone_name,
        )


async def async_load_zone_configurations(result_container: dict[str, Any]) -> None:
    """Async helper to load zone configurations from PostgreSQL database."""
    try:
        # Get database URL from environment
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL environment variable not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        # Use asyncpg directly to avoid event loop conflicts
        conn = await asyncpg.connect(database_url)
        try:
            await process_zone_rows(conn, result_container)
            await process_subzone_rows(conn, result_container)
        finally:
            await conn.close()
    except Exception as e:
        result_container["error"] = e
        raise


def load_zone_configurations() -> dict[str, ZoneConfiguration]:
    """
    Load zone and sub-zone configurations from PostgreSQL database.

    Returns:
        Dictionary mapping zone keys to ZoneConfiguration objects

    Raises:
        RuntimeError: If loading fails
    """
    result_container: dict[str, Any] = {"configs": {"zone": {}, "subzone": {}}, "error": None}

    def run_async():
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        try:
            new_loop.run_until_complete(async_load_zone_configurations(result_container))
        finally:
            new_loop.close()

    thread = threading.Thread(target=run_async)
    thread.start()
    thread.join()

    error = result_container.get("error")
    if error is not None:
        logger.error(
            "Failed to load zone configs from database",
            error=str(error),
            error_type=type(error).__name__,
        )
        if isinstance(error, BaseException):
            raise RuntimeError("Failed to load zone configurations from database") from error
        raise RuntimeError(f"Failed to load zone configurations from database: {error}")

    # Merge zone and subzone configs into a single dict for backward compatibility
    configs = result_container.get("configs")
    if configs is None or not isinstance(configs, dict):
        logger.error("Invalid configs in result_container", configs_type=type(configs).__name__)
        raise RuntimeError("Failed to load zone configurations: invalid configs structure")
    zone_configs = configs.get("zone", {})
    subzone_configs = configs.get("subzone", {})
    merged_configs = {**zone_configs, **subzone_configs}
    logger.info(
        "Loaded zone configurations from PostgreSQL database",
        zone_count=len(zone_configs),
        subzone_count=len(subzone_configs),
        total_count=len(merged_configs),
    )
    return merged_configs
