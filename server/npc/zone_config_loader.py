"""
Zone Configuration Loader Module.

This module handles loading zone and sub-zone configurations from the PostgreSQL
database.
"""

import asyncio
import json
import os
import threading
from typing import TypedDict, cast, overload

import asyncpg

from ..database_config_helpers import get_asyncpg_server_settings_for_database_url
from ..structured_logging.enhanced_logging_config import get_logger
from .zone_configuration import ZoneConfiguration, ZoneConfigurationData, ZoneSpecialRules

logger = get_logger(__name__)


class _ZoneConfigBucket(TypedDict):
    zone: dict[str, ZoneConfiguration]
    subzone: dict[str, ZoneConfiguration]


class ZoneLoadResult(TypedDict):
    """Result of loading zone and sub-zone configs from PostgreSQL."""

    configs: _ZoneConfigBucket
    error: BaseException | None


@overload
def parse_json_field(field_value: object | None, default: list[object]) -> list[object]: ...


@overload
def parse_json_field(field_value: object | None, default: dict[str, object]) -> dict[str, object]: ...


def parse_json_field(
    field_value: object | None, default: list[object] | dict[str, object]
) -> list[object] | dict[str, object]:
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
        if isinstance(default, list):
            return cast(list[object], json.loads(field_value))
        return cast(dict[str, object], json.loads(field_value))
    if isinstance(default, list):
        return cast(list[object], field_value)
    return cast(dict[str, object], field_value)


def parse_zone_special_rules(field_value: object | None) -> ZoneSpecialRules:
    """Parse a zone special_rules field from the database."""
    default: dict[str, object] = {}
    return cast(
        ZoneSpecialRules,
        cast(object, parse_json_field(field_value, default)),
    )


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


async def process_zone_rows(conn: asyncpg.Connection, result_container: ZoneLoadResult) -> None:
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
        zone_stable_id = cast(str, row["zone_stable_id"])
        zone_name = extract_zone_name(zone_stable_id)
        weather_patterns = cast(
            list[str],
            parse_json_field(cast(object, row["weather_patterns"]), []),
        )
        special_rules = parse_zone_special_rules(cast(object, row["special_rules"]))

        config_data: ZoneConfigurationData = {
            "zone_type": cast(str, row["zone_type"]),
            "environment": cast(str, row["environment"]),
            "description": cast(str, row["description"]),
            "weather_patterns": weather_patterns,
            "special_rules": special_rules,
        }

        zone_config = ZoneConfiguration(config_data)
        result_container["configs"]["zone"][zone_name] = zone_config


_SUBZONE_QUERY = """
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


def _store_subzone_row(row: asyncpg.Record, result_container: ZoneLoadResult) -> None:
    """Build and store one subzone configuration from a database row."""
    zone_stable_id = cast(str, row["zone_stable_id"])
    subzone_stable_id = cast(str, row["subzone_stable_id"])
    zone_name = extract_zone_name(zone_stable_id)
    weather_patterns = cast(
        list[str],
        parse_json_field(cast(object, row["weather_patterns"]), []),
    )
    special_rules = parse_zone_special_rules(cast(object, row["special_rules"]))

    config_data: ZoneConfigurationData = {
        "zone_type": cast(str, row["zone_type"]),  # Inherited from zone
        "environment": cast(str, row["environment"]),
        "description": cast(str, row["description"]),
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


async def process_subzone_rows(conn: asyncpg.Connection, result_container: ZoneLoadResult) -> None:
    """
    Process subzone rows from database and populate subzone configurations.

    Args:
        conn: Database connection
        result_container: Container to store results
    """
    subzone_rows = await conn.fetch(_SUBZONE_QUERY)
    for row in subzone_rows:
        _store_subzone_row(row, result_container)


async def async_load_zone_configurations(result_container: ZoneLoadResult) -> None:
    """Async helper to load zone configurations from PostgreSQL database."""
    try:
        # Get database URL from environment
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL environment variable not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        server_settings = get_asyncpg_server_settings_for_database_url(database_url)
        # Use asyncpg directly to avoid event loop conflicts; match engine search_path
        conn = await asyncpg.connect(database_url, server_settings=server_settings)
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
    result_container: ZoneLoadResult = {
        "configs": {"zone": {}, "subzone": {}},
        "error": None,
    }

    def run_async() -> None:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        try:
            new_loop.run_until_complete(async_load_zone_configurations(result_container))
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Zone config loading errors unpredictable, must store in container
            # Store exception in result_container if not already stored
            # (async_load_zone_configurations may have already stored it)
            if result_container.get("error") is None:
                result_container["error"] = e
        finally:
            new_loop.close()

    thread = threading.Thread(target=run_async)
    thread.start()
    thread.join()

    error = result_container["error"]
    if error is not None:
        logger.error(
            "Failed to load zone configs from database",
            error=str(error),
            error_type=type(error).__name__,
        )
        raise RuntimeError("Failed to load zone configurations from database") from error

    # Merge zone and subzone configs into a single dict for backward compatibility
    configs = result_container["configs"]
    zone_configs = configs["zone"]
    subzone_configs = configs["subzone"]
    merged_configs = {**zone_configs, **subzone_configs}
    logger.info(
        "Loaded zone configurations from PostgreSQL database",
        zone_count=len(zone_configs),
        subzone_count=len(subzone_configs),
        total_count=len(merged_configs),
    )
    return merged_configs
