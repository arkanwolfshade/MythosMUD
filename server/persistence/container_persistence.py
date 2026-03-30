"""
Container persistence operations for the unified container system.

As documented in the restricted archives of Miskatonic University, container
persistence requires careful handling to ensure proper storage and retrieval
of investigator artifacts across environmental props, wearable gear, and corpses.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import cast
from uuid import UUID

import psycopg2
from psycopg2.extensions import connection as PsycopgConnection
from psycopg2.extensions import cursor as PsycopgCursor
from psycopg2.extras import RealDictCursor
from structlog.stdlib import BoundLogger

from ..exceptions import DatabaseError, ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise
from .container_create_params import ContainerCreateParams
from .container_data import ContainerData, ContainerDataCore, ContainerDataExtras
from .container_helpers import (
    build_update_query,
    fetch_container_items,
    parse_jsonb_column,
    update_container_items,
    validate_lock_state,
)
from .item_instance_persistence import ensure_item_instance

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))

# Re-export functions with original names for backward compatibility with tests
_fetch_container_items = fetch_container_items
_parse_jsonb_column = parse_jsonb_column


def _as_uuid(value: object) -> UUID:
    if isinstance(value, UUID):
        return value
    return UUID(str(value))


def _as_opt_uuid(value: object) -> UUID | None:
    if value is None:
        return None
    if isinstance(value, UUID):
        return value
    return UUID(str(value))


def _as_opt_str(value: object) -> str | None:
    if value is None:
        return None
    return str(value)


def _as_opt_datetime(value: object) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    return None


def _coerce_item_quantity(value: object) -> int:
    if isinstance(value, bool):
        return 1
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return 1
    if isinstance(value, float):
        return int(value)
    return 1


def _allowed_roles_from_row(value: object) -> list[str]:
    parsed: object = parse_jsonb_column(value, [])
    if isinstance(parsed, list):
        seq = cast(list[object], parsed)
        return [str(x) for x in seq]
    return []


def _metadata_from_row(value: object) -> dict[str, object]:
    parsed: object = parse_jsonb_column(value, {})
    if isinstance(parsed, dict):
        return cast(dict[str, object], parsed)
    return {}


def _int_from_row(value: object, default: int) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return default
    return default


def _opt_int_from_row(value: object) -> int | None:
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return None
    return None


_INSERT_CONTAINER_SQL = """
            INSERT INTO containers (
                source_type, owner_id, room_id, entity_id, lock_state,
                capacity_slots, weight_limit, decay_at, allowed_roles,
                metadata_json, container_item_instance_id, created_at, updated_at
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb, %s, %s, %s
            )
            RETURNING container_instance_id, created_at, updated_at
            """


@dataclass
class _InsertBindSource:
    """Snapshot of row fields for INSERT bind tuple (internal)."""

    source_type: str
    owner_id: UUID | None
    room_id: str | None
    entity_id: UUID | None
    lock_state: str
    capacity_slots: int
    weight_limit: int | None
    decay_at: datetime | None
    allowed_roles: list[str] | None
    metadata_json: dict[str, object] | None
    container_item_instance_id: str | None
    current_time: datetime


@dataclass(frozen=True)
class _CreateOutcome:
    """Post-insert wiring for logging and get_container vs fallback."""

    container_id: UUID
    source_type: str
    owner_id: UUID | None
    room_id: str | None
    entity_id: UUID | None
    lock_state: str
    capacity_slots: int
    weight_limit: int | None
    decay_at: datetime | None
    allowed_roles: list[str]
    items_json: list[dict[str, object]] | None
    metadata_json: dict[str, object] | None
    created_at: datetime | None
    updated_at: datetime | None


_SELECT_CONTAINER_BY_ID_SQL = """
            SELECT
                container_instance_id, source_type, owner_id, room_id, entity_id,
                lock_state, capacity_slots, weight_limit, decay_at,
                allowed_roles, metadata_json, created_at, updated_at,
                container_item_instance_id
            FROM containers
            WHERE container_instance_id = %s
            """


def _validate_new_container_params(source_type: str, capacity_slots: int, lock_state: str) -> None:
    if source_type not in ("environment", "equipment", "corpse"):
        log_and_raise(
            ValidationError,
            f"Invalid source_type: {source_type}. Must be 'environment', 'equipment', or 'corpse'",
            operation="create_container",
            source_type=source_type,
            details={"source_type": source_type},
            user_friendly="Invalid container type",
        )
    if capacity_slots < 1 or capacity_slots > 20:
        log_and_raise(
            ValidationError,
            f"Invalid capacity_slots: {capacity_slots}. Must be between 1 and 20",
            operation="create_container",
            capacity_slots=capacity_slots,
            details={"capacity_slots": capacity_slots},
            user_friendly="Invalid container capacity",
        )
    if lock_state not in ("unlocked", "locked", "sealed"):
        log_and_raise(
            ValidationError,
            f"Invalid lock_state: {lock_state}. Must be 'unlocked', 'locked', or 'sealed'",
            operation="create_container",
            lock_state=lock_state,
            details={"lock_state": lock_state},
            user_friendly="Invalid lock state",
        )


def _insert_container_row(
    conn: PsycopgConnection, bind: tuple[object, ...], source_type: str
) -> tuple[UUID, datetime | None, datetime | None]:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(_INSERT_CONTAINER_SQL, bind)
    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    if not row:
        log_and_raise(
            DatabaseError,
            "Failed to create container - no ID returned",
            operation="create_container",
            source_type=source_type,
            user_friendly="Failed to create container",
        )
    row_dict = cast(dict[str, object], row)
    return (
        _as_uuid(row_dict["container_instance_id"]),
        _as_opt_datetime(row_dict["created_at"]),
        _as_opt_datetime(row_dict["updated_at"]),
    )


def _insert_bind_tuple(src: _InsertBindSource) -> tuple[object, ...]:
    metadata_jsonb = json.dumps(src.metadata_json or {})
    allowed_roles_jsonb = json.dumps(src.allowed_roles or [])
    owner_id_str: str | None = str(src.owner_id) if src.owner_id is not None else None
    entity_id_str: str | None = str(src.entity_id) if src.entity_id is not None else None
    return (
        src.source_type,
        owner_id_str,
        src.room_id,
        entity_id_str,
        src.lock_state,
        src.capacity_slots,
        src.weight_limit,
        src.decay_at,
        allowed_roles_jsonb,
        metadata_jsonb,
        src.container_item_instance_id,
        src.current_time,
        src.current_time,
    )


def _after_container_insert(
    conn: PsycopgConnection,
    src: _InsertBindSource,
    container_id: UUID,
    created_at: datetime | None,
    updated_at: datetime | None,
    items_json: list[dict[str, object]] | None,
) -> ContainerData:
    if items_json:
        _seed_new_container_items(conn, container_id, items_json)
    return _log_and_resolve_created_container(
        conn,
        _CreateOutcome(
            container_id=container_id,
            source_type=src.source_type,
            owner_id=src.owner_id,
            room_id=src.room_id,
            entity_id=src.entity_id,
            lock_state=src.lock_state,
            capacity_slots=src.capacity_slots,
            weight_limit=src.weight_limit,
            decay_at=src.decay_at,
            allowed_roles=src.allowed_roles or [],
            items_json=items_json,
            metadata_json=src.metadata_json,
            created_at=created_at,
            updated_at=updated_at,
        ),
    )


def _log_and_resolve_created_container(conn: PsycopgConnection, out: _CreateOutcome) -> ContainerData:
    logger.info(
        "Container created",
        container_id=str(out.container_id),
        source_type=out.source_type,
        room_id=out.room_id,
        entity_id=str(out.entity_id) if out.entity_id else None,
    )
    return get_container(conn, out.container_id) or ContainerData(
        ContainerDataCore(
            container_instance_id=out.container_id,
            source_type=out.source_type,
            owner_id=out.owner_id,
            room_id=out.room_id,
            entity_id=out.entity_id,
            lock_state=out.lock_state,
            capacity_slots=out.capacity_slots,
        ),
        ContainerDataExtras(
            weight_limit=out.weight_limit,
            decay_at=out.decay_at,
            allowed_roles=out.allowed_roles,
            items_json=out.items_json or [],
            metadata_json=out.metadata_json or {},
            created_at=out.created_at,
            updated_at=out.updated_at,
        ),
    )


def _seed_new_container_items(conn: PsycopgConnection, container_id: UUID, items_json: list[dict[str, object]]) -> None:
    cursor_items = conn.cursor()
    for position, item in enumerate(items_json):
        item_instance_raw: object = item.get("item_instance_id") or item.get("item_id")
        prototype_raw: object = item.get("item_id") or item.get("prototype_id")
        if item_instance_raw is None or prototype_raw is None:
            continue
        item_instance_id = str(item_instance_raw)
        prototype_id = str(prototype_raw)
        md_raw: object = item.get("metadata", {})
        item_metadata: dict[str, object] = cast(dict[str, object], md_raw) if isinstance(md_raw, dict) else {}
        try:
            ensure_item_instance(
                conn,
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                owner_type="container",
                owner_id=str(container_id),
                quantity=_coerce_item_quantity(item.get("quantity", 1)),
                metadata=item_metadata,
            )
        except (DatabaseError, ValidationError) as e:
            logger.warning(
                "Failed to ensure item instance exists, skipping item",
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                error=str(e),
            )
            continue
        cursor_items.execute(
            "SELECT add_item_to_container(%s, %s, %s)",
            (str(container_id), item_instance_id, position),
        )
    conn.commit()
    cursor_items.close()


def _fetch_container_row_dict(conn: PsycopgConnection, container_id_str: str) -> dict[str, object] | None:
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(_SELECT_CONTAINER_BY_ID_SQL, (container_id_str,))
    row = cursor.fetchone()
    cursor.close()
    if not row:
        return None
    return cast(dict[str, object], row)


def _container_data_from_row(conn: PsycopgConnection, row_dict: dict[str, object], container_id: UUID) -> ContainerData:
    items_json = fetch_container_items(conn, container_id)
    return ContainerData(
        ContainerDataCore(
            container_instance_id=_as_uuid(row_dict["container_instance_id"]),
            source_type=str(row_dict["source_type"]),
            owner_id=_as_opt_uuid(row_dict["owner_id"]),
            room_id=_as_opt_str(row_dict["room_id"]),
            entity_id=_as_opt_uuid(row_dict["entity_id"]),
            lock_state=str(row_dict["lock_state"]),
            capacity_slots=_int_from_row(row_dict["capacity_slots"], 20),
        ),
        ContainerDataExtras(
            weight_limit=_opt_int_from_row(row_dict["weight_limit"]),
            decay_at=_as_opt_datetime(row_dict["decay_at"]),
            allowed_roles=_allowed_roles_from_row(row_dict["allowed_roles"]),
            items_json=items_json,
            metadata_json=_metadata_from_row(row_dict["metadata_json"]),
            created_at=_as_opt_datetime(row_dict["created_at"]),
            updated_at=_as_opt_datetime(row_dict["updated_at"]),
        ),
    )


def _run_container_update_execute(
    cursor: PsycopgCursor,
    conn: PsycopgConnection,
    container_id_str: str,
    items_json: list[dict[str, object]] | None,
    lock_state: str | None,
    metadata_json: dict[str, object] | None,
    current_time: datetime,
) -> tuple[object | None, int]:
    if items_json is not None:
        update_container_items(cursor, container_id_str, items_json, conn)
    updates: list[str] = []
    params: list[object] = []
    if lock_state is not None:
        updates.append("lock_state = %s")
        params.append(lock_state)
    if metadata_json is not None:
        updates.append("metadata_json = %s::jsonb")
        params.append(json.dumps(metadata_json))
    if not updates and items_json is None:
        return None, 0
    query = build_update_query(updates, params, container_id_str, current_time)
    # nosemgrep: python.lang.security.audit.sql-injection.sql-injection
    # nosec B608: Using psycopg2.sql.SQL for safe SQL construction (column names are hardcoded)
    cursor.execute(query, params)
    row = cursor.fetchone()
    # build_update_query appends updated_at; exclude it from "user" field count
    return row, len(updates) - 1


def create_container(
    conn: PsycopgConnection,
    source_type: str,
    params: ContainerCreateParams | None = None,
) -> ContainerData:
    """Persist a new container row, optionally seed contents, return hydrated data or fallback."""
    p = params or ContainerCreateParams()
    _validate_new_container_params(source_type, p.capacity_slots, p.lock_state)

    try:
        src = _InsertBindSource(
            source_type=source_type,
            owner_id=p.owner_id,
            room_id=p.room_id,
            entity_id=p.entity_id,
            lock_state=p.lock_state,
            capacity_slots=p.capacity_slots,
            weight_limit=p.weight_limit,
            decay_at=p.decay_at,
            allowed_roles=p.allowed_roles,
            metadata_json=p.metadata_json,
            container_item_instance_id=p.container_item_instance_id,
            current_time=datetime.now(UTC).replace(tzinfo=None),
        )
        cid, c_at, u_at = _insert_container_row(conn, _insert_bind_tuple(src), source_type)
        return _after_container_insert(conn, src, cid, c_at, u_at, p.items_json)

    except psycopg2.Error as e:
        conn.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error creating container: {e}",
            operation="create_container",
            source_type=source_type,
            details={"error": str(e), "source_type": source_type},
            user_friendly="Failed to create container",
        )


def get_container(conn: PsycopgConnection, container_id: UUID) -> ContainerData | None:
    """Load one container by id, or None. Raises DatabaseError on psycopg failure."""
    try:
        container_id_str = str(container_id)
        row_dict = _fetch_container_row_dict(conn, container_id_str)
        if row_dict is None:
            return None
        return _container_data_from_row(conn, row_dict, container_id)

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving container: {e}",
            operation="get_container",
            container_id=str(container_id),
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to retrieve container",
        )


def update_container(
    conn: PsycopgConnection,
    container_id: UUID,
    items_json: list[dict[str, object]] | None = None,
    lock_state: str | None = None,
    metadata_json: dict[str, object] | None = None,
) -> ContainerData | None:
    """Apply item/lock/metadata updates; returns refreshed row or None if missing."""
    validate_lock_state(lock_state)

    try:
        container_id_str = str(container_id)
        current_time = datetime.now(UTC).replace(tzinfo=None)
        cursor = conn.cursor()
        row, updated_fields = _run_container_update_execute(
            cursor,
            conn,
            container_id_str,
            items_json,
            lock_state,
            metadata_json,
            current_time,
        )
        conn.commit()
        cursor.close()

        if not row:
            return None

        logger.info(
            "Container updated",
            container_id=str(container_id),
            updated_fields=updated_fields,
        )

        return get_container(conn, container_id)

    except psycopg2.Error as e:
        conn.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error updating container: {e}",
            operation="update_container",
            container_id=str(container_id),
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to update container",
        )


def delete_container(conn: PsycopgConnection, container_id: UUID) -> bool:
    """Delete by id; True if a row was removed. Raises DatabaseError on failure."""
    try:
        cursor = conn.cursor()
        container_id_str = str(container_id)
        cursor.execute(
            "DELETE FROM containers WHERE container_instance_id = %s RETURNING container_instance_id",
            (container_id_str,),
        )
        row = cursor.fetchone()
        conn.commit()
        cursor.close()

        if row:
            logger.info("Container deleted", container_id=str(container_id))
            return True
        return False

    except psycopg2.Error as e:
        conn.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error deleting container: {e}",
            operation="delete_container",
            container_id=str(container_id),
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to delete container",
        )
