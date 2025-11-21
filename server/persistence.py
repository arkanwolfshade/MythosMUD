import asyncio
import json
import os
import threading
from collections.abc import Callable
from contextlib import contextmanager
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, TypedDict, cast
from uuid import UUID

import psycopg2

from .exceptions import DatabaseError, ValidationError
from .logging.enhanced_logging_config import get_logger
from .models.player import Player
from .models.room import Room
from .postgres_adapter import connect_postgres
from .schemas.inventory_schema import InventorySchemaValidationError, validate_inventory_payload
from .utils.error_logging import create_error_context, log_and_raise

if TYPE_CHECKING:
    from .models.profession import Profession

logger = get_logger(__name__)

# Player table columns for explicit SELECT queries (avoids SELECT * anti-pattern)
PLAYER_COLUMNS = (
    "player_id, user_id, name, current_room_id, profession_id, "
    "experience_points, level, stats, inventory, status_effects, "
    "created_at, last_active, is_admin"
)

# Profession table columns for explicit SELECT queries
PROFESSION_COLUMNS = "id, name, description, flavor_text, is_available"


# --- Custom Exceptions ---
# Note: These are kept for backward compatibility
# New code should use the comprehensive exception system in exceptions.py
class PersistenceError(Exception):
    pass


class UniqueConstraintError(PersistenceError):
    pass


class InventoryPayload(TypedDict):
    """Structured representation of player inventory persistence payload."""

    inventory: list[dict[str, Any]]
    equipped: dict[str, Any]
    version: int


# --- Hook Decorator ---
def register_hook(event: str):
    """Decorator to register a hook for a given event."""

    def decorator(func):
        PersistenceLayer._register_hook(event, func)
        return func

    return decorator


# DEPRECATED: Module-level global singleton removed - use ApplicationContainer instead
# Keeping these functions for backward compatibility during migration
_persistence_instance = None
_persistence_lock = threading.Lock()


def get_persistence(event_bus=None) -> "PersistenceLayer":
    """
    Get persistence layer instance.

    DEPRECATED: Use ApplicationContainer.persistence instead.
    This function exists only for backward compatibility during migration.

    Args:
        event_bus: Optional EventBus instance

    Returns:
        PersistenceLayer: The persistence layer instance
    """
    global _persistence_instance
    with _persistence_lock:
        if _persistence_instance is None:
            _persistence_instance = PersistenceLayer(event_bus=event_bus)
        elif event_bus is not None and _persistence_instance._event_bus is None:  # type: ignore[unreachable]
            # Update the event bus if it's not set and we have one to set
            _persistence_instance._event_bus = event_bus
        return _persistence_instance


def reset_persistence():
    """
    Reset the persistence singleton instance.

    DEPRECATED: Use ApplicationContainer.reset_instance() instead.
    This function exists only for backward compatibility during migration.
    """
    global _persistence_instance
    with _persistence_lock:
        if _persistence_instance is not None:
            # Force immediate shutdown of EventBus to prevent async task interference
            if _persistence_instance._event_bus is not None:
                try:
                    # Force shutdown without waiting for async cleanup
                    _persistence_instance._event_bus._running = False
                    _persistence_instance._event_bus._shutdown_event.set()
                    # Clear active tasks immediately
                    _persistence_instance._event_bus._active_tasks.clear()
                except (AttributeError, RuntimeError) as e:
                    logger.warning("Error during event bus cleanup", error=str(e), error_type=type(e).__name__)
                    # Any error during cleanup - just proceed with reset
                    pass
        _persistence_instance = None


# --- PersistenceLayer Class ---
class PersistenceLayer:
    """
    Synchronous persistence layer using psycopg2 for PostgreSQL operations.

    Unified persistence layer for all game data (players, rooms, inventory, etc.).
    Thread-safe, supports hooks, context management, and batch operations.

    DUAL-LAYER PERSISTENCE ARCHITECTURE:

    This codebase maintains two persistence layers to support both synchronous
    and asynchronous code paths:

    1. PersistenceLayer (this class):
       - Synchronous operations using psycopg2
       - Used by legacy sync code
       - Thread-safe with locks
       - Provides async_* wrapper methods that use asyncio.to_thread()

    2. AsyncPersistenceLayer (server/async_persistence.py):
       - Asynchronous operations using asyncpg
       - Used by new async code
       - Non-blocking, event-loop friendly
       - Better performance for async contexts

    MIGRATION STRATEGY:

    Phase 1 (Current): Dual-layer support
    - Legacy sync code uses PersistenceLayer directly
    - New async code uses AsyncPersistenceLayer
    - Async wrappers (async_*) available for gradual migration
    - Both layers share the same database schema

    Phase 2 (Future): Full async migration
    - Migrate all sync code to async
    - Deprecate PersistenceLayer sync methods
    - Standardize on AsyncPersistenceLayer
    - Remove async_* wrapper methods

    Timeline: TBD - Migration will be gradual to avoid breaking changes

    USAGE GUIDELINES:

    For Sync Code:
    - Use PersistenceLayer methods directly
    - Example: persistence.get_player(player_id)
    - Thread-safe, can be called from any thread

    For Async Code:
    - Use AsyncPersistenceLayer for best performance
    - Example: await async_persistence.get_player_by_id(player_id)
    - Non-blocking, event-loop friendly

    For Migration:
    - Use async_* wrapper methods during transition
    - Example: await persistence.async_get_player(player_id)
    - Wraps sync method with asyncio.to_thread() - adds overhead
    - Temporary solution - migrate to AsyncPersistenceLayer when possible

    DEPRECATION WARNING:
    - Async methods (async_*) in this class delegate to sync methods using asyncio.to_thread()
    - This prevents event loop blocking but adds overhead
    - New async code should use AsyncPersistenceLayer directly
    - Legacy sync code can continue using this class
    """

    _hooks: dict[str, list[Callable]] = {}

    # Mapping dictionary for field names to PostgreSQL array literals
    # SECURITY: This provides an additional safety layer beyond whitelist validation
    # Each field name maps to its PostgreSQL ARRAY literal, preventing any possibility
    # of SQL injection even if validation is bypassed
    FIELD_NAME_TO_ARRAY: dict[str, str] = {
        "current_health": "ARRAY['current_health']::text[]",
        "sanity": "ARRAY['sanity']::text[]",
        "occult_knowledge": "ARRAY['occult_knowledge']::text[]",
        "fear": "ARRAY['fear']::text[]",
        "corruption": "ARRAY['corruption']::text[]",
        "cult_affiliation": "ARRAY['cult_affiliation']::text[]",
        "strength": "ARRAY['strength']::text[]",
        "dexterity": "ARRAY['dexterity']::text[]",
        "constitution": "ARRAY['constitution']::text[]",
        "intelligence": "ARRAY['intelligence']::text[]",
        "wisdom": "ARRAY['wisdom']::text[]",
        "charisma": "ARRAY['charisma']::text[]",
    }
    # Note: experience_points is NOT in stats JSONB - it's a separate INTEGER column

    def __init__(self, db_path: str | None = None, log_path: str | None = None, event_bus=None):
        # Use environment variable for database path - require it to be set
        if db_path:
            self.db_path = db_path
        elif os.environ.get("DATABASE_URL"):
            # Use DATABASE_URL directly (PostgreSQL only)
            # Type assertion: we've already checked it's not None above
            database_url = os.environ.get("DATABASE_URL")
            assert database_url is not None, "DATABASE_URL should not be None here"
            self.db_path = database_url
        else:
            context = create_error_context()
            context.metadata["operation"] = "persistence_init"
            log_and_raise(
                ValidationError,
                "DATABASE_URL environment variable must be set",
                context=context,
                details={"config_file": "server/env.example"},
                user_friendly="Database configuration is missing",
            )

        # Logging is now handled by the centralized logging system
        # The log_path parameter is kept for backward compatibility but not used
        self.log_path = None  # No longer needed with centralized logging

        self._lock = threading.RLock()
        self._logger = self._setup_logger()
        self._event_bus = event_bus
        # PostgreSQL-only: Verify we have a PostgreSQL URL
        if self.db_path and not self.db_path.startswith("postgresql"):
            context = create_error_context()
            context.metadata["operation"] = "persistence_init"
            log_and_raise(
                ValidationError,
                f"Unsupported database URL: {self.db_path}. Only PostgreSQL is supported.",
                context=context,
                user_friendly="Database configuration error - PostgreSQL required",
            )
        # TODO: Load config for SQL logging verbosity
        self._load_room_cache()

    def _setup_logger(self):
        # Use centralized logging configuration
        from .logging.enhanced_logging_config import get_logger

        return get_logger("PersistenceLayer")

    def _log(self, msg: str):
        self._logger.info(msg)

    @contextmanager
    def _get_connection(self):
        """Get a PostgreSQL database connection context manager."""
        conn = connect_postgres(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def _convert_insert_or_replace(self, query: str, table_name: str, primary_key: str) -> str:
        """Convert INSERT OR REPLACE to PostgreSQL INSERT ... ON CONFLICT."""
        # Convert INSERT OR REPLACE to PostgreSQL UPSERT syntax
        if "INSERT OR REPLACE" in query.upper():
            # Replace INSERT OR REPLACE with INSERT
            query = query.replace("INSERT OR REPLACE", "INSERT")
            # Find the VALUES clause
            values_idx = query.upper().find("VALUES")
            if values_idx != -1:
                # Extract columns from the INSERT statement
                insert_part = query[:values_idx]
                values_part = query[values_idx:]
                # Find column list
                col_start = insert_part.find("(")
                col_end = insert_part.find(")", col_start)
                if col_start != -1 and col_end != -1:
                    columns_str = insert_part[col_start + 1 : col_end]
                    columns = [col.strip() for col in columns_str.split(",")]
                    # Build ON CONFLICT clause
                    conflict_clause = f" ON CONFLICT ({primary_key}) DO UPDATE SET "
                    update_parts = [f"{col} = EXCLUDED.{col}" for col in columns if col != primary_key]
                    conflict_clause += ", ".join(update_parts)
                    return insert_part + values_part + conflict_clause
        return query

    def _convert_row_to_player_data(self, row: Any) -> dict:
        """
        Convert database row data to proper types for Player constructor.

        Args:
            row: Database row object from query result (PostgreSQL PostgresRow)

        Returns:
            dict: Data with proper types for Player constructor
        """
        data = dict(row)

        # Convert string UUIDs back to UUID objects
        if data.get("player_id"):
            try:
                data["player_id"] = str(data["player_id"])
            except (ValueError, TypeError):
                self._log(f"Invalid player_id format: {data['player_id']}")
                data["player_id"] = None

        if data.get("user_id"):
            try:
                data["user_id"] = str(data["user_id"])
            except (ValueError, TypeError):
                self._log(f"Invalid user_id format: {data['user_id']}")
                data["user_id"] = None

        # Convert is_admin from integer to boolean
        if "is_admin" in data:
            data["is_admin"] = bool(data["is_admin"])

        # Handle stats: JSONB column may return as dict (psycopg2) or string
        # Player model's get_stats() handles both, but we ensure dict for consistency
        if "stats" in data:
            stats_value = data["stats"]
            if isinstance(stats_value, str):
                # JSONB returned as string - parse to dict
                try:
                    data["stats"] = json.loads(stats_value)
                except (json.JSONDecodeError, TypeError):
                    # Invalid JSON - use default stats
                    data["stats"] = {
                        "strength": 10,
                        "dexterity": 10,
                        "constitution": 10,
                        "intelligence": 10,
                        "wisdom": 10,
                        "charisma": 10,
                        "sanity": 100,
                        "occult_knowledge": 0,
                        "fear": 0,
                        "corruption": 0,
                        "cult_affiliation": 0,
                        "current_health": 100,
                        "position": "standing",
                    }
            # If it's already a dict, keep it as-is (psycopg2 may return JSONB as dict)

        # Convert datetime strings back to datetime objects if needed
        # (Player model handles this internally, but we could add explicit conversion here)

        return data

    # --- Context Management ---
    def __enter__(self):
        self._lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock.release()

    # --- Hook Registration ---
    @classmethod
    def _register_hook(cls, event: str, func: Callable):
        if event not in cls._hooks:
            cls._hooks[event] = []
        cls._hooks[event].append(func)

    def _run_hooks(self, event: str, *args, **kwargs):
        for func in self._hooks.get(event, []):
            func(*args, **kwargs)
        # TODO: Support async hooks in the future

    def _prepare_inventory_payload(self, player: Player) -> tuple[str, str]:
        """Validate and serialize inventory payload for storage."""
        inventory_raw: Any = player.get_inventory()
        if isinstance(inventory_raw, str):
            try:
                inventory_raw = json.loads(inventory_raw)
            except (TypeError, json.JSONDecodeError) as exc:
                raise InventorySchemaValidationError(f"Invalid inventory JSON: {exc}") from exc

        if not isinstance(inventory_raw, list):
            raise InventorySchemaValidationError("Inventory payload must be an array of stacks")

        equipped_raw: Any = player.get_equipped_items() or {}
        if isinstance(equipped_raw, str):
            try:
                equipped_raw = json.loads(equipped_raw)
            except (TypeError, json.JSONDecodeError) as exc:
                raise InventorySchemaValidationError(f"Invalid equipped JSON: {exc}") from exc

        if not isinstance(equipped_raw, dict):
            raise InventorySchemaValidationError("Equipped payload must be an object")

        payload_dict: dict[str, Any] = {
            "inventory": cast(list[dict[str, Any]], inventory_raw),
            "equipped": cast(dict[str, Any], equipped_raw),
            "version": 1,
        }
        validate_inventory_payload(payload_dict)
        payload = cast(InventoryPayload, payload_dict)

        inventory_json = json.dumps(payload["inventory"])
        equipped_json = json.dumps(payload["equipped"])
        player.inventory = cast(Any, inventory_json)  # keep ORM column in sync
        player.set_equipped_items(payload["equipped"])
        return inventory_json, equipped_json

    def _ensure_inventory_row(self, conn: Any, player_id: UUID, inventory_json: str, equipped_json: str) -> None:
        insert_query = """
            INSERT OR REPLACE INTO player_inventories (player_id, inventory_json, equipped_json)
            VALUES (%s, %s, %s)
            """
        insert_query = self._convert_insert_or_replace(insert_query, "player_inventories", "player_id")
        # psycopg2 handles UUID objects directly via register_uuid() in postgres_adapter
        conn.execute(
            insert_query,
            (player_id, inventory_json, equipped_json),
        )

    def _load_player_inventory(self, conn: Any, player: Player) -> None:
        cursor = conn.execute(
            """
            SELECT inventory_json, equipped_json
            FROM player_inventories
            WHERE player_id = %s
            """,
            (player.player_id,),
        )
        row = cursor.fetchone()
        if row is None:
            default_inventory = "[]"
            default_equipped = "{}"
            # player.player_id is already a string (UUID(as_uuid=False)), convert to UUID for method call
            player_id_uuid = UUID(str(player.player_id))
            self._ensure_inventory_row(conn, player_id_uuid, default_inventory, default_equipped)
            inventory_json = default_inventory
            equipped_json = default_equipped
        else:
            inventory_column = cast(str | None, row[0])
            equipped_column = cast(str | None, row[1])
            inventory_json = inventory_column if inventory_column is not None else "[]"
            equipped_json = equipped_column if equipped_column is not None else "{}"

        try:
            inventory_raw: Any = json.loads(inventory_json)
            equipped_raw: Any = json.loads(equipped_json)
        except (TypeError, json.JSONDecodeError) as exc:
            logger.error(
                "Stored inventory payload failed to deserialize",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                error=str(exc),
            )
            context = create_error_context()
            context.metadata["operation"] = "load_player_inventory"
            # Structlog handles UUID objects automatically, no need to convert to string
            context.metadata["player_id"] = player.player_id
            log_and_raise(
                DatabaseError,
                "Failed to deserialize stored inventory payload",
                context=context,
                details={"error": str(exc)},
                user_friendly="Player inventory data is corrupted",
            )

        raw_payload: dict[str, Any] = {
            "inventory": inventory_raw,
            "equipped": equipped_raw,
            "version": 1,
        }
        try:
            validate_inventory_payload(raw_payload)
        except InventorySchemaValidationError as exc:
            logger.error(
                "Stored inventory payload failed validation",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                error=str(exc),
            )
            context = create_error_context()
            context.metadata["operation"] = "load_player_inventory"
            # Structlog handles UUID objects automatically, no need to convert to string
            context.metadata["player_id"] = player.player_id
            log_and_raise(
                DatabaseError,
                "Invalid inventory payload detected in storage",
                context=context,
                details={"error": str(exc)},
                user_friendly="Player inventory data is invalid",
            )

        validated_payload = cast(InventoryPayload, raw_payload)
        sanitized_inventory_json = json.dumps(validated_payload["inventory"])
        player.inventory = cast(Any, sanitized_inventory_json)
        player.set_equipped_items(validated_payload["equipped"])

    # --- Room Cache (Loaded at Startup) ---
    def _load_room_cache(self) -> None:
        """Load rooms from PostgreSQL database and convert to Room objects."""
        self._room_cache = {}
        self._room_mappings: dict[str, str] = {}
        try:
            from .world_loader import generate_room_id

            with self._get_connection() as conn:
                # Query rooms with zone/subzone hierarchy
                query = """
                    SELECT
                        r.id as room_uuid,
                        r.stable_id,
                        r.name,
                        r.description,
                        r.attributes,
                        sz.stable_id as subzone_stable_id,
                        z.stable_id as zone_stable_id,
                        -- Extract plane from zone stable_id (format: 'plane/zone')
                        SPLIT_PART(z.stable_id, '/', 1) as plane,
                        SPLIT_PART(z.stable_id, '/', 2) as zone
                    FROM rooms r
                    JOIN subzones sz ON r.subzone_id = sz.id
                    JOIN zones z ON sz.zone_id = z.id
                    ORDER BY z.stable_id, sz.stable_id, r.stable_id
                """
                cursor = conn.execute(query)
                rooms_rows = cursor.fetchall()

                # Query room links (exits) for all rooms
                # Include both source and destination room zone/subzone info
                exits_query = """
                    SELECT
                        r.stable_id as from_room_stable_id,
                        r2.stable_id as to_room_stable_id,
                        rl.direction,
                        sz.stable_id as from_subzone_stable_id,
                        z.stable_id as from_zone_stable_id,
                        sz2.stable_id as to_subzone_stable_id,
                        z2.stable_id as to_zone_stable_id
                    FROM room_links rl
                    JOIN rooms r ON rl.from_room_id = r.id
                    JOIN rooms r2 ON rl.to_room_id = r2.id
                    JOIN subzones sz ON r.subzone_id = sz.id
                    JOIN zones z ON sz.zone_id = z.id
                    JOIN subzones sz2 ON r2.subzone_id = sz2.id
                    JOIN zones z2 ON sz2.zone_id = z2.id
                """
                cursor = conn.execute(exits_query)
                exits_rows = cursor.fetchall()

                # Process rooms and build room data list
                room_data_list = []

                for row in rooms_rows:
                    stable_id = row[1]
                    name = row[2]
                    description = row[3]
                    attributes = row[4] if row[4] else {}
                    subzone_stable_id = row[5]
                    zone_stable_id = row[6]

                    # Generate hierarchical room ID
                    zone_parts = zone_stable_id.split("/")
                    plane_name = zone_parts[0] if len(zone_parts) > 0 else ""
                    zone_name = zone_parts[1] if len(zone_parts) > 1 else zone_stable_id

                    # Check if stable_id already contains the full hierarchical path
                    # Expected format: plane_zone_subzone_room_xxx or plane_zone_subzone_intersection_xxx
                    # If stable_id already starts with plane_zone_subzone, it's a full room ID
                    expected_prefix = f"{plane_name}_{zone_name}_{subzone_stable_id}_"
                    if stable_id.startswith(expected_prefix):
                        # stable_id is already a full hierarchical room ID, use it directly
                        room_id = stable_id
                    else:
                        # stable_id is just the room identifier (e.g., "room_boundary_st_001"), generate full ID
                        room_id = generate_room_id(plane_name, zone_name, subzone_stable_id, stable_id)

                    # Store room data for processing
                    room_data_list.append(
                        {
                            "room_id": room_id,
                            "stable_id": stable_id,
                            "name": name,
                            "description": description,
                            "attributes": attributes,
                            "plane": plane_name,
                            "zone": zone_name,
                            "sub_zone": subzone_stable_id,
                        }
                    )

                # Build exits dictionary keyed by room_id (not stable_id)
                exits_by_room: dict[str, dict[str, str]] = {}
                exit_count = 0
                for row in exits_rows:
                    from_stable_id = row[0]
                    to_stable_id = row[1]
                    direction = row[2]
                    from_subzone = row[3]
                    from_zone = row[4]
                    to_subzone = row[5]
                    to_zone = row[6]

                    # Generate hierarchical room IDs for both source and destination
                    from_zone_parts = from_zone.split("/")
                    from_plane = from_zone_parts[0] if len(from_zone_parts) > 0 else ""
                    from_zone_name = from_zone_parts[1] if len(from_zone_parts) > 1 else from_zone

                    to_zone_parts = to_zone.split("/")
                    to_plane = to_zone_parts[0] if len(to_zone_parts) > 0 else ""
                    to_zone_name = to_zone_parts[1] if len(to_zone_parts) > 1 else to_zone

                    # Check if stable_id already contains the full hierarchical path
                    # Expected format: plane_zone_subzone_room_xxx or plane_zone_subzone_intersection_xxx
                    # If stable_id already starts with plane_zone_subzone, it's a full room ID
                    from_expected_prefix = f"{from_plane}_{from_zone_name}_{from_subzone}_"
                    if from_stable_id.startswith(from_expected_prefix):
                        # stable_id is already a full hierarchical room ID, use it directly
                        from_room_id = from_stable_id
                    else:
                        # stable_id is just the room identifier, generate full ID
                        from_room_id = generate_room_id(from_plane, from_zone_name, from_subzone, from_stable_id)

                    to_expected_prefix = f"{to_plane}_{to_zone_name}_{to_subzone}_"
                    if to_stable_id.startswith(to_expected_prefix):
                        # stable_id is already a full hierarchical room ID, use it directly
                        to_room_id = to_stable_id
                    else:
                        # stable_id is just the room identifier, generate full ID
                        to_room_id = generate_room_id(to_plane, to_zone_name, to_subzone, to_stable_id)

                    # Debug logging for sanitarium exits
                    if from_room_id in (
                        "earth_arkhamcity_sanitarium_room_foyer_001",
                        "earth_arkhamcity_sanitarium_room_foyer_entrance_001",
                    ) or to_room_id in (
                        "earth_arkhamcity_sanitarium_room_foyer_001",
                        "earth_arkhamcity_sanitarium_room_foyer_entrance_001",
                    ):
                        self._logger.info(
                            "DEBUG: Building sanitarium exit",
                            direction=direction,
                            from_stable_id=from_stable_id,
                            from_room_id=from_room_id,
                            to_stable_id=to_stable_id,
                            to_room_id=to_room_id,
                            from_zone=from_zone,
                            from_subzone=from_subzone,
                            to_zone=to_zone,
                            to_subzone=to_subzone,
                        )

                    if from_room_id not in exits_by_room:
                        exits_by_room[from_room_id] = {}

                    exits_by_room[from_room_id][direction] = to_room_id
                    exit_count += 1

                # Convert database rows to Room objects
                for room_data_item in room_data_list:
                    room_id = room_data_item["room_id"]
                    name = room_data_item["name"]
                    description = room_data_item["description"]
                    attributes = room_data_item["attributes"]
                    plane_name = room_data_item["plane"]
                    zone_name = room_data_item["zone"]
                    subzone_stable_id = room_data_item["sub_zone"]

                    # Get exits for this room (already resolved to full room IDs)
                    exits = exits_by_room.get(room_id, {})

                    # Debug: Log exits for specific rooms to verify loading
                    if room_id in (
                        "earth_arkhamcity_sanitarium_room_foyer_001",
                        "earth_arkhamcity_sanitarium_room_foyer_entrance_001",
                    ):
                        self._logger.info(
                            "DEBUG: Loading sanitarium room with exits",
                            room_id=room_id,
                            room_name=name,
                            exits=exits,
                            exits_count=len(exits),
                            exits_by_room_keys=list(exits_by_room.keys())[:10],
                        )

                    # Build room data dictionary matching Room class expectations
                    room_data = {
                        "id": room_id,
                        "name": name,
                        "description": description,
                        "plane": plane_name,
                        "zone": zone_name,
                        "sub_zone": subzone_stable_id,
                        "resolved_environment": attributes.get("environment", "outdoors")
                        if isinstance(attributes, dict)
                        else "outdoors",
                        "exits": exits,
                    }

                    self._room_cache[room_id] = Room(room_data, self._event_bus)

            self._logger.info(
                "Loaded rooms into cache from PostgreSQL database",
                room_count=len(self._room_cache),
                mapping_count=len(self._room_mappings),
                exit_count=exit_count,
                exits_by_room_count=len(exits_by_room),
            )
            # Debug: Log sample room IDs for troubleshooting
            if self._room_cache:
                sample_room_ids = list(self._room_cache.keys())[:5]
                self._logger.debug("Sample room IDs loaded", sample_room_ids=sample_room_ids)
        except Exception as e:
            context = create_error_context()
            context.metadata["operation"] = "load_room_cache"
            log_and_raise(
                DatabaseError,
                f"Room cache load failed: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to load world data from database",
            )

    # --- CRUD for Players ---
    def get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name."""
        context = create_error_context()
        context.metadata["operation"] = "get_player_by_name"
        context.metadata["player_name"] = name

        try:
            with self._lock, self._get_connection() as conn:
                # PostgreSQL uses %s placeholders, not ?
                # NOTE: PLAYER_COLUMNS is a compile-time constant, so f-string is safe
                # Future: Migrate to SQLAlchemy ORM for better query construction
                query = f"SELECT {PLAYER_COLUMNS} FROM players WHERE name = %s"
                row = conn.execute(query, (name,)).fetchone()
                if row:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    self._load_player_inventory(conn, player)
                    return player
                return None
        except psycopg2.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by name '{name}': {e}",
                context=context,
                details={"player_name": name, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )
            return None  # type: ignore[unreachable]  # Defensive return after NoReturn

    def get_player(self, player_id: UUID) -> Player | None:
        """Get a player by ID."""
        context = create_error_context()
        context.metadata["operation"] = "get_player"
        # Structlog handles UUID objects automatically, no need to convert to string
        context.metadata["player_id"] = player_id

        try:
            with self._lock, self._get_connection() as conn:
                # PostgreSQL uses %s placeholders, not ?
                # NOTE: PLAYER_COLUMNS is a compile-time constant, so f-string is safe
                # Future: Migrate to SQLAlchemy ORM for better query construction
                # psycopg2 handles UUID objects directly via register_uuid() in postgres_adapter
                query = f"SELECT {PLAYER_COLUMNS} FROM players WHERE player_id = %s"
                row = conn.execute(query, (player_id,)).fetchone()
                if row:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    self._load_player_inventory(conn, player)
                    return player
                return None
        except psycopg2.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by ID '{player_id}': {e}",
                context=context,
                # Structlog handles UUID objects automatically, no need to convert to string
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )
            return None  # type: ignore[unreachable]  # Defensive return after NoReturn

    def get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get a player by the owning user's ID."""
        context = create_error_context()
        context.metadata["operation"] = "get_player_by_user_id"
        context.metadata["user_id"] = user_id

        try:
            with self._lock, self._get_connection() as conn:
                # PostgreSQL uses %s placeholders, not ?
                # NOTE: PLAYER_COLUMNS is a compile-time constant, so f-string is safe
                # Future: Migrate to SQLAlchemy ORM for better query construction
                user_id_str = str(user_id) if user_id else None
                query = f"SELECT {PLAYER_COLUMNS} FROM players WHERE user_id = %s"
                row = conn.execute(query, (user_id_str,)).fetchone()
                if row:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    self._load_player_inventory(conn, player)
                    return player
                return None
        except psycopg2.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by user ID '{user_id}': {e}",
                context=context,
                details={"user_id": user_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )
            return None  # type: ignore[unreachable]  # Defensive return after NoReturn

    def save_player(self, player: Player):
        """Save or update a player."""
        context = create_error_context()
        context.metadata["operation"] = "save_player"
        context.metadata["player_name"] = player.name
        # Structlog handles UUID objects automatically, no need to convert to string
        context.metadata["player_id"] = player.player_id

        try:
            with self._lock, self._get_connection() as conn:
                try:
                    # Handle datetime fields that might be strings
                    created_at = None
                    last_active = None

                    if player.created_at:
                        if isinstance(player.created_at, str):  # type: ignore[unreachable]
                            created_at = player.created_at  # type: ignore[unreachable]
                        else:
                            created_at = player.created_at.isoformat()

                    if player.last_active:
                        if isinstance(player.last_active, str):  # type: ignore[unreachable]
                            last_active = player.last_active  # type: ignore[unreachable]
                        else:
                            last_active = player.last_active.isoformat()

                    # Convert UUIDs to strings for PostgreSQL storage
                    # Note: player.player_id is always a string (UUID(as_uuid=False) in model)
                    # Ensure we always have a string for psycopg2
                    player_id_str = str(player.player_id) if player.player_id is not None else None
                    user_id_str = str(player.user_id) if player.user_id else None

                    if player_id_str is None:
                        log_and_raise(
                            DatabaseError,
                            "Player ID is required before persistence save",
                            context=context,
                            details={"player_name": player.name},
                            user_friendly="Failed to save player",
                        )

                    try:
                        inventory_json, equipped_json = self._prepare_inventory_payload(player)
                    except InventorySchemaValidationError as exc:
                        logger.error(
                            "Inventory payload validation failed during save",
                            player_id=player_id_str,
                            player_name=player.name,
                            error=str(exc),
                        )
                        log_and_raise(
                            DatabaseError,
                            f"Inventory validation failed: {exc}",
                            context=context,
                            details={
                                "player_name": player.name,
                                "player_id": player_id_str,
                                "error": str(exc),
                            },
                            user_friendly="Player inventory data is invalid",
                        )

                    # Serialize stats to JSON if it's a dict (JSONB column expects JSON string for psycopg2)
                    # Note: mypy sees player.stats as Column[Any], but at runtime SQLAlchemy returns the actual value
                    stats_json = player.stats
                    if isinstance(stats_json, dict):  # type: ignore[unreachable]
                        stats_json = json.dumps(stats_json)  # type: ignore[unreachable]
                    elif stats_json is None:
                        # Use default stats if None
                        stats_json = json.dumps(  # type: ignore[unreachable]
                            {
                                "strength": 10,
                                "dexterity": 10,
                                "constitution": 10,
                                "intelligence": 10,
                                "wisdom": 10,
                                "charisma": 10,
                                "sanity": 100,
                                "occult_knowledge": 0,
                                "fear": 0,
                                "corruption": 0,
                                "cult_affiliation": 0,
                                "current_health": 100,
                                "position": "standing",
                            }
                        )

                    insert_query = """
                        INSERT OR REPLACE INTO players (
                            player_id, user_id, name, stats, inventory, status_effects,
                            current_room_id, experience_points, level, is_admin, profession_id, created_at, last_active
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                    insert_query = self._convert_insert_or_replace(insert_query, "players", "player_id")
                    # Ensure is_admin is an integer (not boolean) for PostgreSQL
                    is_admin_int = int(player.is_admin) if player.is_admin is not None else 0
                    conn.execute(
                        insert_query,
                        (
                            player_id_str,
                            user_id_str,
                            player.name,
                            stats_json,
                            inventory_json,
                            player.status_effects,
                            player.current_room_id,
                            player.experience_points,
                            player.level,
                            is_admin_int,
                            player.profession_id,
                            created_at,
                            last_active,
                        ),
                    )
                    # Convert player_id_str to UUID for _ensure_inventory_row (which expects UUID)
                    player_id_uuid = UUID(player_id_str) if player_id_str else None
                    if player_id_uuid:
                        self._ensure_inventory_row(conn, player_id_uuid, inventory_json, equipped_json)
                    conn.commit()
                    self._log(f"Saved player {player.name}")
                    self._run_hooks("after_save_player", player)
                except psycopg2.IntegrityError as e:
                    log_and_raise(
                        DatabaseError,
                        f"Unique constraint error saving player: {e}",
                        context=context,
                        # Structlog handles UUID objects automatically, no need to convert to string
                        details={"player_name": player.name, "player_id": player.player_id, "error": str(e)},
                        user_friendly="Player name already exists",
                    )
                except psycopg2.Error as e:
                    log_and_raise(
                        DatabaseError,
                        f"Database error saving player: {e}",
                        context=context,
                        # Structlog handles UUID objects automatically, no need to convert to string
                        details={"player_name": player.name, "player_id": player.player_id, "error": str(e)},
                        user_friendly="Failed to save player",
                    )
        except OSError as e:
            log_and_raise(
                DatabaseError,
                f"File system error saving player: {e}",
                context=context,
                # Structlog handles UUID objects automatically, no need to convert to string
                details={"player_name": player.name, "player_id": player.player_id, "error": str(e)},
                user_friendly="Failed to save player - file system error",
            )
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Unexpected error saving player: {e}",
                context=context,
                # Structlog handles UUID objects automatically, no need to convert to string
                details={"player_name": player.name, "player_id": player.player_id, "error": str(e)},
                user_friendly="Failed to save player",
            )

    def update_player_last_active(self, player_id: UUID, last_active: datetime | None = None) -> None:
        """
        Update the last_active timestamp for a player.

        Args:
            player_id: ID or name of the player to update
            last_active: Timestamp to persist (defaults to current UTC time)
        """
        context = create_error_context()
        context.metadata["operation"] = "update_player_last_active"
        context.metadata["player_id"] = player_id

        try:
            with self._lock, self._get_connection() as conn:
                try:
                    if last_active is None:
                        last_active = datetime.now(UTC)

                    # Ensure timestamp is timezone-aware in UTC, then serialize
                    if last_active.tzinfo is None:
                        last_active = last_active.replace(tzinfo=UTC)

                    last_active_iso = last_active.isoformat()
                    # psycopg2 handles UUID objects directly via register_uuid() in postgres_adapter
                    # Query matches by player_id (UUID) or name (string) - both use same value for flexibility
                    # Note: This allows updating by UUID or by name, but name comparison uses UUID string
                    conn.execute(
                        "UPDATE players SET last_active = %s WHERE player_id = %s",
                        (last_active_iso, player_id),
                    )
                    conn.commit()
                except Exception as e:
                    log_and_raise(
                        DatabaseError,
                        f"Database error updating last_active for player '{player_id}': {e}",
                        context=context,
                        details={"player_id": player_id, "error": str(e)},
                        user_friendly="Failed to update player activity",
                    )
        except OSError as e:
            log_and_raise(
                DatabaseError,
                f"File system error updating last_active for player '{player_id}': {e}",
                context=context,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to update player activity - file system error",
            )
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Unexpected error updating last_active for player '{player_id}': {e}",
                context=context,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to update player activity",
            )

    def list_players(self) -> list[Player]:
        """List all players."""
        context = create_error_context()
        context.metadata["operation"] = "list_players"

        try:
            with self._lock, self._get_connection() as conn:
                # NOTE: PLAYER_COLUMNS is a compile-time constant, so f-string is safe
                # Future: Migrate to SQLAlchemy ORM for better query construction
                query = f"SELECT {PLAYER_COLUMNS} FROM players"
                rows = conn.execute(query).fetchall()
                players = []
                for row in rows:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    self._load_player_inventory(conn, player)
                    players.append(player)
                return players
        except psycopg2.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing players: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve player list",
            )
            return []  # type: ignore[unreachable]  # Defensive return after NoReturn

    def get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players currently in a specific room."""
        context = create_error_context()
        context.metadata["operation"] = "get_players_in_room"
        context.metadata["room_id"] = room_id

        try:
            with self._lock, self._get_connection() as conn:
                # PostgreSQL uses %s placeholders, not ?
                # Get all players in a room for message broadcasting. Uses index on current_room_id.
                # NOTE: PLAYER_COLUMNS is a compile-time constant, so f-string is safe
                # Future: Migrate to SQLAlchemy ORM for better query construction
                query = f"SELECT {PLAYER_COLUMNS} FROM players WHERE current_room_id = %s"
                rows = conn.execute(query, (room_id,)).fetchall()
                players = []
                for row in rows:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    self._load_player_inventory(conn, player)
                    players.append(player)
                return players
        except psycopg2.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving players in room '{room_id}': {e}",
                context=context,
                details={"room_id": room_id, "error": str(e)},
                user_friendly="Failed to retrieve players in room",
            )
            return []  # type: ignore[unreachable]  # Defensive return after NoReturn

    def save_players(self, players: list[Player]):
        """Batch save players atomically."""
        context = create_error_context()
        context.metadata["operation"] = "save_players"
        context.metadata["player_count"] = len(players)

        try:
            with self._lock, self._get_connection() as conn:
                try:
                    for player in players:
                        # Handle datetime fields that might be strings
                        created_at = None
                        last_active = None

                        if player.created_at:
                            if isinstance(player.created_at, str):  # type: ignore[unreachable]
                                created_at = player.created_at  # type: ignore[unreachable]
                            else:
                                created_at = player.created_at.isoformat()

                        if player.last_active:
                            if isinstance(player.last_active, str):  # type: ignore[unreachable]
                                last_active = player.last_active  # type: ignore[unreachable]
                            else:
                                last_active = player.last_active.isoformat()

                        # Convert UUIDs to strings for PostgreSQL (VARCHAR storage)
                        player_id_str = str(player.player_id) if player.player_id else None
                        user_id_str = str(player.user_id) if player.user_id else None

                        # Serialize stats to JSON if it's a dict (JSONB column expects JSON string for psycopg2)
                        # Note: mypy sees player.stats as Column[Any], but at runtime SQLAlchemy returns the actual value
                        stats_json = player.stats
                        if isinstance(stats_json, dict):  # type: ignore[unreachable]
                            stats_json = json.dumps(stats_json)  # type: ignore[unreachable]
                        elif stats_json is None:
                            # Use default stats if None
                            stats_json = json.dumps(  # type: ignore[unreachable]
                                {
                                    "strength": 10,
                                    "dexterity": 10,
                                    "constitution": 10,
                                    "intelligence": 10,
                                    "wisdom": 10,
                                    "charisma": 10,
                                    "sanity": 100,
                                    "occult_knowledge": 0,
                                    "fear": 0,
                                    "corruption": 0,
                                    "cult_affiliation": 0,
                                    "current_health": 100,
                                    "position": "standing",
                                }
                            )

                        insert_query = """
                            INSERT OR REPLACE INTO players (
                                player_id, user_id, name, stats, inventory, status_effects,
                                current_room_id, experience_points, level, is_admin, profession_id, created_at, last_active
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """
                        insert_query = self._convert_insert_or_replace(insert_query, "players", "player_id")
                        conn.execute(
                            insert_query,
                            (
                                player_id_str,
                                user_id_str,
                                player.name,
                                stats_json,
                                player.inventory,
                                player.status_effects,
                                player.current_room_id,
                                player.experience_points,
                                player.level,
                                player.is_admin,
                                player.profession_id,
                                created_at,
                                last_active,
                            ),
                        )
                    conn.commit()
                    self._log(f"Batch saved {len(players)} players.")
                    self._run_hooks("after_save_players", players)
                except psycopg2.IntegrityError as e:
                    log_and_raise(
                        DatabaseError,
                        f"Batch unique constraint error: {e}",
                        context=context,
                        details={"player_count": len(players), "error": str(e)},
                        user_friendly="Failed to save players - duplicate data",
                    )
                except psycopg2.Error as e:
                    log_and_raise(
                        DatabaseError,
                        f"Database error in batch save: {e}",
                        context=context,
                        details={"player_count": len(players), "error": str(e)},
                        user_friendly="Failed to save players",
                    )
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Unexpected error in batch save: {e}",
                context=context,
                details={"player_count": len(players), "error": str(e)},
                user_friendly="Failed to save players",
            )

    def delete_player(self, player_id: UUID) -> bool:
        """
        Delete a player from the database.

        Args:
            player_id: The unique identifier of the player to delete

        Returns:
            bool: True if player was deleted, False if player didn't exist

        Raises:
            PersistenceError: If deletion fails due to database constraints or errors
        """
        with self._lock, self._get_connection() as conn:
            try:
                # First check if player exists
                # PostgreSQL uses %s placeholders, not ?
                # psycopg2 handles UUID objects directly via register_uuid() in postgres_adapter
                cursor = conn.execute("SELECT player_id FROM players WHERE player_id = %s", (player_id,))
                if not cursor.fetchone():
                    self._log("Delete attempted for non-existent player")
                    return False

                # Delete the player (foreign key constraints will handle related data)
                cursor = conn.execute("DELETE FROM players WHERE player_id = %s", (player_id,))
                conn.commit()

                if cursor.rowcount > 0:
                    self._log("Successfully deleted player")
                    self._run_hooks("after_delete_player", player_id)
                    return True
                else:
                    self._log("No rows affected when deleting player")
                    return False

            except Exception as e:
                context = create_error_context()
                context.metadata["operation"] = "delete_player"
                context.metadata["player_id"] = player_id
                log_and_raise(
                    DatabaseError,
                    f"Database error deleting player {player_id}: {e}",
                    context=context,
                    details={"player_id": player_id, "error": str(e)},
                    user_friendly="Failed to delete player",
                )
                return False  # type: ignore[unreachable]  # Defensive return after NoReturn

    # --- CRUD for Professions ---
    def get_all_professions(self) -> list:
        """Get all available professions."""
        context = create_error_context()
        context.metadata["operation"] = "get_all_professions"

        try:
            with self._lock, self._get_connection() as conn:
                # NOTE: PROFESSION_COLUMNS is a compile-time constant, so f-string is safe
                # Future: Migrate to SQLAlchemy ORM for better query construction
                query = f"SELECT {PROFESSION_COLUMNS} FROM professions WHERE is_available = true ORDER BY id"
                rows = conn.execute(query).fetchall()

                professions = []
                for row in rows:
                    profession_data = dict(row)
                    # Import here to avoid circular imports
                    from .models.profession import Profession

                    profession = Profession(**profession_data)
                    professions.append(profession)

                return professions
        except psycopg2.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving professions: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve professions",
            )
            return []  # type: ignore[unreachable]  # Defensive return after NoReturn

    def get_profession_by_id(self, profession_id: int) -> "Profession | None":
        """Get a profession by ID."""
        context = create_error_context()
        context.metadata["operation"] = "get_profession_by_id"
        context.metadata["profession_id"] = profession_id

        try:
            with self._lock, self._get_connection() as conn:
                # PostgreSQL uses %s placeholders, not ?
                # NOTE: PROFESSION_COLUMNS is a compile-time constant, so f-string is safe
                # Future: Migrate to SQLAlchemy ORM for better query construction
                query = f"SELECT {PROFESSION_COLUMNS} FROM professions WHERE id = %s"
                row = conn.execute(query, (profession_id,)).fetchone()

                if row:
                    profession_data = dict(row)
                    # Import here to avoid circular imports
                    from .models.profession import Profession

                    profession = Profession(**profession_data)
                    return profession
                return None
        except psycopg2.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving profession {profession_id}: {e}",
                context=context,
                details={"profession_id": profession_id, "error": str(e)},
                user_friendly="Failed to retrieve profession",
            )
            return None  # type: ignore[unreachable]  # Defensive return after NoReturn

    # --- CRUD for Rooms ---
    def get_room(self, room_id: str) -> Room | None:
        """Get a room by ID from the cache and sync with database state."""
        # First try direct lookup
        room = None
        if room_id in self._room_cache:
            room = self._room_cache[room_id]
        elif room_id in self._room_mappings:
            # If not found, check if it's an old ID that maps to a new one
            new_room_id = self._room_mappings[room_id]
            room = self._room_cache.get(new_room_id)

        if room:
            # Sync the room's player state with the database
            self._sync_room_players(room)
            return room

        # Debug logging for missing rooms (only log once per room to avoid spam)
        if not hasattr(self, "_missing_room_warnings"):
            self._missing_room_warnings: set[str] = set()
        if room_id not in self._missing_room_warnings:
            self._missing_room_warnings.add(room_id)
            # Log available room IDs that are similar (for debugging)
            similar_rooms = [
                rid for rid in self._room_cache.keys() if room_id.split("_")[-1] in rid or rid.split("_")[-1] in room_id
            ][:5]
            self._logger.warning(
                "Room not found in cache",
                requested_room_id=room_id,
                cache_size=len(self._room_cache),
                similar_rooms=similar_rooms,
            )

        return None

    def _sync_room_players(self, room: Room, _recursion_depth: int = 0) -> None:
        """
        Clear any ghost players from the room's in-memory state.

        Players should only be in rooms when they're actively connected to the game.
        The database current_room_id is just where the player was last located,
        not where they currently are. This method ensures rooms start clean.

        Args:
            room: The Room object to sync
            _recursion_depth: Internal parameter to prevent infinite recursion
        """
        # Prevent infinite recursion
        if _recursion_depth > 2:
            self._log(f"Preventing infinite recursion in _sync_room_players for room {room.id}")
            return

        try:
            # Get current in-memory player state
            memory_player_ids = set(room.get_players())

            # CRITICAL FIX: Only remove players that are no longer in the database
            # Players should only be added to rooms when they actually connect to the game
            # But we should not clear all players - only remove those that are truly ghost players
            if memory_player_ids:
                # Log player count without exposing GUIDs to prevent infinite loops with PlayerGuidFormatter
                self._log(f"Room {room.id} has {len(memory_player_ids)} players in memory")
                # Note: We don't clear the room's players here because they are added when players connect
                # The room's _players set should only be modified when players actually enter/leave

        except Exception as e:
            context = create_error_context()
            context.metadata["operation"] = "sync_room_players"
            context.metadata["room_id"] = room.id
            context.metadata["recursion_depth"] = _recursion_depth
            # Log as warning since this is a non-critical operation
            self._logger.warning(
                "Error syncing room players",
                context=context.to_dict(),
                error=str(e),
                error_type=type(e).__name__,
            )
            # Don't raise the exception - we want to continue even if sync fails

    def save_room(self, room: Room):
        """Save or update a room. Currently read-only - rooms are stored as JSON files."""
        # TODO: Implement JSON file saving for rooms
        # For now, just update the cache
        self._room_cache[room.id] = room
        self._log(f"Updated room {room.id} in cache (JSON file saving not implemented)")
        self._run_hooks("after_save_room", room)

    def list_rooms(self) -> list[Room]:
        """List all rooms from the cache."""
        return list(self._room_cache.values())

    def save_rooms(self, rooms: list[Room]):
        """Batch save rooms. Currently read-only - rooms are stored as JSON files."""
        # TODO: Implement JSON file saving for rooms
        # For now, just update the cache
        for room in rooms:
            self._room_cache[room.id] = room
        self._log(f"Updated {len(rooms)} rooms in cache (JSON file saving not implemented)")
        self._run_hooks("after_save_rooms", rooms)

    # --- Player Health Management Methods ---

    def damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """
        Damage a player and persist health changes to the database.

        PHASE 2A OPTIMIZATION: Uses atomic field update to prevent race conditions.

        Args:
            player: The player object to damage
            amount: Amount of damage to apply
            damage_type: Type of damage (for future extension)

        Raises:
            ValueError: If damage amount is invalid
            DatabaseError: If database save fails

        Note:
            Uses atomic database update for ONLY current_health field.
            This prevents race conditions where other systems (e.g., XP awards)
            overwrite health changes with stale cached player data.
        """
        try:
            if amount < 0:
                raise ValueError(f"Damage amount must be positive, got {amount}")

            # Get current stats from in-memory player object
            stats = player.get_stats()
            current_health = stats.get("current_health", 100)
            new_health = max(0, current_health - amount)

            # Update the in-memory player object (for immediate UI feedback)
            stats["current_health"] = new_health
            player.set_stats(stats)

            # CRITICAL: Use atomic field update instead of save_player()
            # This prevents race conditions with other systems updating the same player
            # player.player_id is already a string (UUID(as_uuid=False)), convert to UUID for method call
            player_id_uuid = UUID(str(player.player_id))
            self.update_player_health(player_id_uuid, -amount, f"damage:{damage_type}")

            self._logger.info(
                "Player health reduced atomically",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                player_name=player.name,
                damage=amount,
                old_health=current_health,
                new_health=new_health,
                damage_type=damage_type,
            )
        except ValueError as e:
            self._logger.error(
                "Invalid damage amount",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                amount=amount,
                error=str(e),
                exc_info=True,
            )
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player damage",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                player_name=player.name,
                amount=amount,
                damage_type=damage_type,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    def heal_player(self, player: Player, amount: int) -> None:
        """
        Heal a player and persist health changes to the database.

        PHASE 2A OPTIMIZATION: Uses atomic field update to prevent race conditions.

        Args:
            player: The player object to heal
            amount: Amount of healing to apply

        Raises:
            ValueError: If healing amount is invalid
            DatabaseError: If database save fails

        Note:
            Uses atomic database update for ONLY current_health field.
            This prevents race conditions with other systems updating the same player.
        """
        try:
            if amount < 0:
                raise ValueError(f"Healing amount must be positive, got {amount}")

            # Get current stats from in-memory player object
            stats = player.get_stats()
            current_health = stats.get("current_health", 100)
            max_health = 100  # TODO: Make this configurable or player-specific
            new_health = min(max_health, current_health + amount)

            # Update the in-memory player object (for immediate UI feedback)
            stats["current_health"] = new_health
            player.set_stats(stats)

            # CRITICAL: Use atomic field update instead of save_player()
            # player.player_id is already a string (UUID(as_uuid=False)), convert to UUID for method call
            player_id_uuid = UUID(str(player.player_id))
            self.update_player_health(player_id_uuid, amount, "healing")

            self._logger.info(
                "Player health increased atomically",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                player_name=player.name,
                healing=amount,
                old_health=current_health,
                new_health=new_health,
            )
        except ValueError as e:
            self._logger.error(
                "Invalid healing amount",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                amount=amount,
                error=str(e),
                exc_info=True,
            )
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player healing",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                player_name=player.name,
                amount=amount,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    async def async_damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """
        Async wrapper for damage_player to support async contexts.

        CRITICAL FIX: This method was missing, causing async damage calls to fail.

        Args:
            player: The player object to damage
            amount: Amount of damage to apply
            damage_type: Type of damage

        Note:
            Uses asyncio.to_thread() to run blocking synchronous operations in a thread pool,
            preventing event loop blocking. The underlying persistence layer uses PostgreSQL
            via psycopg2 (synchronous driver). For true async operations, use the
            async_persistence layer methods instead.
        """
        # Use asyncio.to_thread() to run blocking operations in thread pool
        # This prevents blocking the event loop during database operations
        await asyncio.to_thread(self.damage_player, player, amount, damage_type)

    async def async_heal_player(self, player: Player, amount: int) -> None:
        """
        Async wrapper for heal_player to support async contexts.

        CRITICAL FIX: This method was missing, causing async heal calls to fail.

        Args:
            player: The player object to heal
            amount: Amount of healing to apply

        Note:
            Uses asyncio.to_thread() to run blocking synchronous operations in a thread pool,
            preventing event loop blocking. The underlying persistence layer uses PostgreSQL
            via psycopg2 (synchronous driver). For true async operations, use the
            async_persistence layer methods instead.

        DEPRECATION: This async wrapper exists for backward compatibility. New async code
        should use AsyncPersistenceLayer directly for better performance.
        """
        # Use asyncio.to_thread() to run blocking operations in thread pool
        # This prevents blocking the event loop during database operations
        await asyncio.to_thread(self.heal_player, player, amount)

    def gain_experience(self, player: Player, amount: int, source: str = "unknown") -> None:
        """
        Award experience points to a player and persist to database.

        PHASE 2A OPTIMIZATION: Uses atomic field update to prevent race conditions.

        Args:
            player: The player object to award XP to
            amount: Amount of XP to award (must be non-negative)
            source: Source of the XP for logging purposes

        Raises:
            ValueError: If amount is negative
            DatabaseError: If database operation fails

        Note:
            Uses atomic database update for ONLY experience_points field.
            This prevents race conditions where XP awards overwrite health changes
            by loading and saving stale cached player data.
        """
        try:
            if amount < 0:
                raise ValueError(f"Experience amount must be non-negative, got {amount}")

            # Get current stats from in-memory player object
            stats = player.get_stats()
            old_xp = stats.get("experience_points", 0)
            new_xp = old_xp + amount

            # Update the in-memory player object (for immediate UI feedback)
            stats["experience_points"] = new_xp
            player.set_stats(stats)

            # CRITICAL: Use atomic field update instead of save_player()
            # This prevents overwriting health or other fields with stale cached values
            # player.player_id is already a string (UUID(as_uuid=False)), convert to UUID for method call
            player_id_uuid = UUID(str(player.player_id))
            self.update_player_xp(player_id_uuid, amount, source)

            self._logger.info(
                "Player experience increased atomically",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                player_name=player.name,
                xp_gained=amount,
                old_xp=old_xp,
                new_xp=new_xp,
                source=source,
            )

        except ValueError as e:
            self._logger.error(
                "Invalid experience amount",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                amount=amount,
                error=str(e),
                exc_info=True,
            )
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player experience gain",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player.player_id,
                player_name=player.name,
                amount=amount,
                source=source,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    async def async_gain_experience(self, player: Player, amount: int, source: str = "unknown") -> None:
        """
        Async wrapper for gain_experience to support async contexts.

        Args:
            player: The player object to award XP to
            amount: Amount of XP to award
            source: Source of the XP for logging purposes

        Note:
            Uses asyncio.to_thread() to run blocking synchronous operations in a thread pool,
            preventing event loop blocking. The underlying persistence layer uses PostgreSQL
            via psycopg2 (synchronous driver). For true async operations, use the
            async_persistence layer methods instead.

        DEPRECATION: This async wrapper exists for backward compatibility. New async code
        should use AsyncPersistenceLayer directly for better performance.
        """
        # Use asyncio.to_thread() to run blocking operations in thread pool
        # This prevents blocking the event loop during database operations
        await asyncio.to_thread(self.gain_experience, player, amount, source)

    def update_player_stat_field(self, player_id: UUID, field_name: str, delta: int | float, reason: str = "") -> None:
        """
        Update a specific numeric field in player stats using atomic database operation.

        CRITICAL FIX: This method prevents race conditions by updating only the specified
        field in the database without loading/saving the entire player object.

        This is the ONLY safe way to update stats when multiple systems may be modifying
        the same player simultaneously (e.g., combat damage + XP awards).

        Args:
            player_id: Player's unique ID (UUID)
            field_name: Name of the stat field to update (e.g., "current_health", "experience_points")
            delta: Amount to add (positive) or subtract (negative) from the field
            reason: Reason for the update (for logging)

        Raises:
            ValueError: If field_name is invalid or delta would result in negative values
            DatabaseError: If database operation fails

        Example:
            # Reduce health by 20 (combat damage)
            persistence.update_player_stat_field(player_id, "current_health", -20, "combat_damage")

            # Increase XP by 100
            persistence.update_player_stat_field(player_id, "experience_points", 100, "killed_npc")

        Note:
            Uses PostgreSQL's jsonb_set() function for atomic field updates.
            Invalidates player cache to ensure fresh data on next get_player().
        """
        try:
            # psycopg2 handles UUID objects directly via register_uuid() in postgres_adapter
            # Structlog handles UUID objects automatically, no need to convert to string

            # Validate delta type (security: prevent SQL injection via type confusion)
            if not isinstance(delta, (int, float)):
                raise TypeError(f"delta must be int or float, got {type(delta).__name__}")

            # Validate field name (whitelist approach for security)
            # Use the mapping dictionary as the source of truth for allowed fields
            if field_name not in self.FIELD_NAME_TO_ARRAY:
                allowed_fields = set(self.FIELD_NAME_TO_ARRAY.keys())
                raise ValueError(f"Invalid stat field name: {field_name}. Must be one of {allowed_fields}")

            # Get the PostgreSQL array literal from the mapping dictionary
            # SECURITY: This provides defense in depth - even if validation is bypassed,
            # the field name cannot be injected into SQL since we use a pre-defined mapping
            array_literal = self.FIELD_NAME_TO_ARRAY[field_name]

            # Execute atomic field update using PostgreSQL jsonb_set()
            # AI Agent: This prevents race conditions by updating ONLY this field
            # without loading/saving the entire player object which might have stale data
            # SECURITY NOTE: field_name is validated against FIELD_NAME_TO_ARRAY dictionary
            # and the array literal is retrieved from the mapping, providing multiple layers
            # of protection against SQL injection. The value access (stats->>%s) is still
            # parameterized for additional defense in depth.
            with self._lock, self._get_connection() as conn:
                # PostgreSQL JSONB path format: array of path elements
                # jsonb_set() requires path as text array, which we get from the mapping dictionary
                # After migration 006, stats is JSONB, so no casting needed
                # Use COALESCE to handle null stats and default to 0 for missing fields
                cursor = conn.execute(
                    f"""
                    UPDATE players
                    SET stats = jsonb_set(
                        COALESCE(stats, '{{}}'::jsonb),
                        {array_literal},
                        to_jsonb((COALESCE(stats->>%s, '0'))::numeric + %s),
                        true
                    )
                    WHERE player_id = %s
                    """,
                    (field_name, delta, player_id),
                )

                if cursor.rowcount == 0:
                    # Structlog handles UUID objects automatically, no need to convert to string
                    raise ValueError(f"Player {player_id} not found")

                conn.commit()

            # AI Agent: No cache invalidation needed - atomic field updates bypass cache entirely
            # This prevents the race condition where XP awards overwrite combat damage

            self._logger.info(
                "Player stat field updated atomically",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id,
                field_name=field_name,
                delta=delta,
                reason=reason,
            )

        except ValueError as e:
            self._logger.error(
                "Invalid stat field update",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id,
                field_name=field_name,
                delta=delta,
                error=str(e),
                exc_info=True,
            )
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to update player stat field",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id,
                field_name=field_name,
                delta=delta,
                reason=reason,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    def update_player_health(self, player_id: UUID, delta: int, reason: str = "") -> None:
        """
        Update player health using atomic database operation.

        CRITICAL FIX: Prevents race conditions where health changes are overwritten
        by other systems (e.g., XP awards) saving stale player data.

        Args:
            player_id: Player's unique ID
            delta: Amount to change health (negative for damage, positive for healing)
            reason: Reason for health change (for logging)

        Example:
            # Combat damage
            update_player_health(player_id, -20, "attacked_by_nightgaunt")

            # Healing
            update_player_health(player_id, 30, "health_potion")
        """
        self.update_player_stat_field(player_id, "current_health", delta, reason)

    def update_player_xp(self, player_id: UUID, delta: int, reason: str = "") -> None:
        """
        Update player experience points using atomic database operation.

        CRITICAL FIX: Prevents race conditions where XP awards overwrite health changes
        by loading stale player data from cache.

        Args:
            player_id: Player's unique ID
            delta: Amount of XP to award (must be positive)
            reason: Reason for XP award (for logging)

        Example:
            update_player_xp(player_id, 100, "killed_nightgaunt")
        """
        if delta < 0:
            raise ValueError(f"XP delta must be non-negative, got {delta}")

        # experience_points is a separate INTEGER column, not in stats JSONB
        # Use atomic UPDATE to prevent race conditions
        context = create_error_context()
        context.metadata["operation"] = "update_player_xp"
        # Structlog handles UUID objects automatically, no need to convert to string
        context.metadata["player_id"] = player_id

        try:
            with self._lock, self._get_connection() as conn:
                # psycopg2 handles UUID objects directly via register_uuid() in postgres_adapter
                cursor = conn.execute(
                    """
                    UPDATE players
                    SET experience_points = experience_points + %s
                    WHERE player_id = %s
                    """,
                    (delta, player_id),
                )

                if cursor.rowcount == 0:
                    # Structlog handles UUID objects automatically, no need to convert to string
                    raise ValueError(f"Player {player_id} not found")

                conn.commit()

                self._logger.info(
                    "Player XP updated atomically",
                    # Structlog handles UUID objects automatically, no need to convert to string
                    player_id=player_id,
                    delta=delta,
                    reason=reason,
                )
        except psycopg2.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating XP for player '{player_id}': {e}",
                context=context,
                # Structlog handles UUID objects automatically, no need to convert to string
                details={"player_id": player_id, "delta": delta, "error": str(e)},
                user_friendly="Failed to update experience points",
            )

    # --- TODO: Inventory, status effects, etc. ---
    # def get_inventory(self, ...): ...
    # def save_inventory(self, ...): ...
    # def list_inventory(self, ...): ...

    def validate_and_fix_player_room(self, player: Player) -> bool:
        """
        Validate that a player's current room exists, and fix if necessary.

        Args:
            player: The player to validate

        Returns:
            True if the room was valid or successfully fixed, False otherwise
        """
        # Check if the player's current room exists
        if self.get_room(str(player.current_room_id)) is not None:
            return True  # Room exists, no fix needed

        # Room doesn't exist, move player to default starting room from config
        old_room = player.current_room_id
        try:
            from .config import get_config

            config = get_config()
            default_room = config.game.default_player_room
        except Exception as e:
            # Fallback to hardcoded default if config loading fails
            context = create_error_context()
            context.metadata["operation"] = "validate_and_fix_player_room"
            context.metadata["player_name"] = player.name
            context.metadata["old_room_id"] = old_room
            self._logger.warning(
                "Config loading failed during room validation, using fallback",
                context=context.to_dict(),
                error=str(e),
                error_type=type(e).__name__,
            )
            default_room = "earth_arkhamcity_sanitarium_room_foyer_001"

        player.current_room_id = default_room  # type: ignore[assignment]

        self._log(f"Player {player.name} was in invalid room '{old_room}', moved to default room '{default_room}'")
        return True

    # --- Async Methods ---
    # These methods now delegate to the true async persistence layer
    # This provides real async database operations without blocking the event loop

    async def async_get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_player_by_name(name)

    async def async_get_player(self, player_id: UUID) -> Player | None:
        """Get a player by ID using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_player_by_id(player_id)

    async def async_get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get a player by user ID using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_player_by_user_id(user_id)

    async def async_save_player(self, player: Player):
        """Save a player using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.save_player(player)

    async def async_list_players(self) -> list[Player]:
        """List all players using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.list_players()

    async def async_get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players in a room using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_players_in_room(room_id)

    async def async_save_players(self, players: list[Player]):
        """Save multiple players using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.save_players(players)

    async def async_delete_player(self, player_id: UUID) -> bool:
        """Delete a player using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.delete_player(player_id)

    async def async_get_all_professions(self) -> list:
        """Get all professions using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_professions()

    async def async_get_profession_by_id(self, profession_id: int) -> object | None:
        """Get a profession by ID using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_profession_by_id(profession_id)

    async def async_get_room(self, room_id: str) -> Room | None:
        """Get a room by ID using async database operations."""
        # Rooms are still handled by the sync layer for now
        return self.get_room(room_id)

    async def async_save_room(self, room: Room):
        """Save a room using async database operations."""
        # Rooms are still handled by the sync layer for now
        return self.save_room(room)

    async def async_list_rooms(self) -> list[Room]:
        """List all rooms using async database operations."""
        # Rooms are still handled by the sync layer for now
        return self.list_rooms()

    async def async_save_rooms(self, rooms: list[Room]):
        """Save multiple rooms using async database operations."""
        # Rooms are still handled by the sync layer for now
        return self.save_rooms(rooms)

    def get_npc_lifecycle_manager(self):
        """
        Get the NPC lifecycle manager from app.state.

        Returns:
            NPCLifecycleManager: The NPC lifecycle manager instance, or None if not available
        """
        try:
            from server.main import app

            lifecycle_manager = getattr(app.state, "npc_lifecycle_manager", None)
            logger.debug(
                "get_npc_lifecycle_manager called",
                has_app=bool(app),
                has_state=bool(getattr(app, "state", None)),
                has_lifecycle_manager=bool(lifecycle_manager),
            )
            return lifecycle_manager
        except Exception as e:
            logger.debug("get_npc_lifecycle_manager failed", error=str(e))
            return None

    # --- TODO: Add async support, other backends, migrations, etc. ---
